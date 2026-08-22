#!/usr/bin/env python3
"""Governance validator for Congtie Registry authoring artifacts.

This tool validates public Registry concept records and Seed 001 planning
ledgers. It does not read user health data, activate records, or provide
runtime, database, API, indexing, or clinical behavior.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Iterable


EXIT_VALID = 0
EXIT_VALIDATION_FAILURE = 1
EXIT_TOOL_FAILURE = 2

REGISTRY_ID_RE = re.compile(r"^(BM|ME|SC|QS)-[0-9]{6}$")
CANDIDATE_KEY_RE = re.compile(r"^[a-z0-9][a-z0-9_]*$")

NAMESPACE_MATRIX = {
    "BM": {"laboratory_biomarker", "molecular_biomarker"},
    "ME": {
        "physiological_measurement",
        "functional_performance_measurement",
        "imaging_derived_measure",
        "device_measured_signal",
        "device_estimated_metric",
        "patient_user_reported_state",
        "behavior_lifestyle_record",
    },
    "SC": {"derived_score_index"},
    "QS": {"validated_questionnaire_scale"},
}

VERIFIED_SOURCE_STATUSES = {"metadata_verified", "content_verified"}
REVIEWED_SOURCE_STATUSES = {"metadata_verified", "content_verified"}
CONTENT_VERIFIED = {"content_verified"}

DEVICE_MAPPING_LAYER_KEYS = {
    "generic_sleep_score",
    "generic_recovery_score",
    "generic_readiness_score",
    "generic_device_stress_estimate",
    "proprietary_device_metric_mapping_family",
}

FORMER_RED_KEYS = {
    "generic_balance_test_measure",
    "generic_sleep_regularity_index",
    "generic_sleep_score",
    "generic_recovery_score",
    "generic_readiness_score",
    "generic_device_stress_estimate",
}

FIRST_WAVE_KEYS = {
    "apolipoprotein_b",
    "lipoprotein_a",
    "hba1c",
    "creatinine",
    "estimated_glomerular_filtration_rate",
    "systolic_blood_pressure",
    "diastolic_blood_pressure",
    "height",
    "body_weight",
    "heart_rate",
    "sleep_total_time",
    "body_mass_index",
}

KNOWN_COMPUTATION_CONTRACTS = {
    "egfr.ckd_epi_2021_creatinine": {
        "registry_inputs": {"creatinine"},
        "context_inputs": {"age_years", "sex_at_birth"},
    },
}

PERSONAL_DATA_FIELDS = {
    "user_id",
    "patient_id",
    "person_id",
    "user_name",
    "patient_name",
    "email",
    "phone",
    "date_of_birth",
    "birth_date",
    "observation_value",
    "result_value",
    "actual_value",
    "personal_target",
    "user_target",
    "consent_record",
}


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, path: str, message: str) -> None:
        self.errors.append(f"{path}: {message}")

    def warn(self, path: str, message: str) -> None:
        self.warnings.append(f"{path}: {message}")

    def extend(self, other: "Report") -> None:
        self.errors.extend(other.errors)
        self.warnings.extend(other.warnings)


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _duplicates(values: Iterable[Any]) -> set[Any]:
    counts = Counter(values)
    return {value for value, count in counts.items() if count > 1}


def _load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _jsonschema_components() -> tuple[Any, Any] | None:
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError:
        return None
    return Draft202012Validator, FormatChecker


def validate_schema_definition(schema: dict[str, Any]) -> tuple[Report, bool]:
    report = Report()
    components = _jsonschema_components()
    if components is None:
        report.warn("schema", "Draft 2020-12 instance validator unavailable")
        return report, False
    engine, _ = components
    try:
        engine.check_schema(schema)
    except Exception as exc:  # jsonschema exposes version-specific subclasses.
        report.error("schema", f"Draft 2020-12 metaschema validation failed: {exc}")
    return report, True


def validate_schema_instance(
    schema: dict[str, Any], record: dict[str, Any]
) -> tuple[Report, bool]:
    report, available = validate_schema_definition(schema)
    if not available or report.errors:
        return report, available
    components = _jsonschema_components()
    assert components is not None
    engine, format_checker = components
    validator = engine(schema, format_checker=format_checker())
    for error in sorted(
        validator.iter_errors(record), key=lambda item: [str(part) for part in item.path]
    ):
        path = ".".join(str(part) for part in error.path) or "record"
        report.error(path, error.message)
    return report, True


def _walk_personal_fields(value: Any, path: str, report: Report) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key in PERSONAL_DATA_FIELDS:
                report.error(child_path, "personal user data is prohibited in a Registry concept")
            _walk_personal_fields(child, child_path, report)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _walk_personal_fields(child, f"{path}[{index}]", report)


def _collect_source_key_references(value: Any, path: str = "record") -> list[tuple[str, str]]:
    references: list[tuple[str, str]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key in {"definition_source_keys", "source_reference_keys"}:
                for index, source_key in enumerate(_as_list(child)):
                    references.append((f"{child_path}[{index}]", source_key))
            elif key != "source_references":
                references.extend(_collect_source_key_references(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            references.extend(_collect_source_key_references(child, f"{path}[{index}]"))
    return references


def _check_source_statuses(
    keys: list[str],
    source_map: dict[str, dict[str, Any]],
    allowed: set[str],
    path: str,
    report: Report,
) -> None:
    for key in keys:
        source = source_map.get(key)
        if source is None:
            continue
        status = source.get("verification_status")
        if status not in allowed:
            report.error(
                path,
                f"source {key!r} has verification_status={status!r}; expected {sorted(allowed)}",
            )


def _source_pool(record: dict[str, Any], report: Report) -> dict[str, dict[str, Any]]:
    sources = _as_list(record.get("source_references"))
    keys: list[str] = []
    source_map: dict[str, dict[str, Any]] = {}
    for index, value in enumerate(sources):
        source = _as_dict(value)
        key = source.get("source_key")
        if not isinstance(key, str) or not key:
            report.error(f"source_references[{index}]", "source_key must be a non-empty string")
            continue
        keys.append(key)
        source_map[key] = source
    for key in sorted(_duplicates(keys)):
        report.error("source_references", f"duplicate source_key {key!r}")

    allowed = set(source_map)
    for path, key in _collect_source_key_references(record):
        if key not in allowed:
            report.error(path, f"dangling source key {key!r}")
    return source_map


def _check_namespace(record: dict[str, Any], report: Report) -> None:
    namespace = record.get("namespace")
    information_type = record.get("information_type")
    allowed = NAMESPACE_MATRIX.get(namespace)
    if allowed is None:
        report.error("namespace", f"unsupported Registry namespace {namespace!r}")
        return
    if information_type not in allowed:
        report.error(
            "information_type",
            f"{information_type!r} is incompatible with namespace {namespace}; expected {sorted(allowed)}",
        )


def _check_registry_id(record: dict[str, Any], report: Report) -> None:
    registry_id = record.get("registry_id")
    if registry_id is None:
        return
    if not isinstance(registry_id, str) or REGISTRY_ID_RE.fullmatch(registry_id) is None:
        report.error("registry_id", "must match (BM|ME|SC|QS)-NNNNNN")
        return
    if registry_id.split("-", 1)[0] != record.get("namespace"):
        report.error("registry_id", "Registry ID prefix does not match namespace")


def _check_unit_policy(record: dict[str, Any], report: Report) -> None:
    policy = _as_dict(record.get("unit_policy"))
    mode = policy.get("mode")
    canonical = policy.get("canonical_unit")
    if mode == "single_canonical":
        unit = _as_dict(canonical)
        if not unit:
            report.error("unit_policy.canonical_unit", "single_canonical requires a unit object")
            return
        if unit.get("status") != "canonical":
            report.error("unit_policy.canonical_unit.status", "must be canonical")
        if not isinstance(unit.get("unit_code"), str) or not unit["unit_code"].strip():
            report.error("unit_policy.canonical_unit.unit_code", "must be a non-empty string")
        if unit.get("unit_system") not in {"UCUM", "local"}:
            report.error("unit_policy.canonical_unit.unit_system", "must be UCUM or reviewed local")
    elif mode in {
        "profile_specific",
        "non_convertible_representations",
        "not_applicable",
        "pending",
    }:
        if canonical is not None:
            report.error("unit_policy.canonical_unit", f"must be null when mode={mode}")
        if mode == "non_convertible_representations":
            note = str(policy.get("note") or "").lower()
            boundary_tokens = ("prohibit", "not permit", "without validated", "不得", "禁止", "未经验证")
            if not any(token in note for token in boundary_tokens):
                report.error(
                    "unit_policy.note",
                    "non_convertible_representations must prohibit unvalidated unified conversion",
                )
    else:
        report.error("unit_policy.mode", f"unsupported mode {mode!r}")


def _all_mappings(record: dict[str, Any]) -> list[tuple[str, dict[str, Any], str]]:
    mappings: list[tuple[str, dict[str, Any], str]] = []
    for index, value in enumerate(_as_list(record.get("external_mappings"))):
        mappings.append((f"external_mappings[{index}]", _as_dict(value), "external"))
    for p_index, value in enumerate(_as_list(record.get("profiles"))):
        profile = _as_dict(value)
        for index, item in enumerate(_as_list(profile.get("external_mappings"))):
            mappings.append(
                (f"profiles[{p_index}].external_mappings[{index}]", _as_dict(item), "external")
            )
        for index, item in enumerate(_as_list(profile.get("device_mappings"))):
            mappings.append(
                (f"profiles[{p_index}].device_mappings[{index}]", _as_dict(item), "device")
            )
    return mappings


def _check_mappings(
    record: dict[str, Any], source_map: dict[str, dict[str, Any]], report: Report
) -> None:
    mappings = _all_mappings(record)
    mapping_keys = [mapping.get("mapping_key") for _, mapping, _ in mappings]
    for key in sorted(_duplicates(key for key in mapping_keys if isinstance(key, str))):
        report.error("mappings", f"duplicate mapping_key {key!r} across concept/profile mappings")

    for path, mapping, kind in mappings:
        refs = _as_list(mapping.get("source_reference_keys"))
        if kind == "external":
            status = mapping.get("status")
            if path.startswith("external_mappings") and mapping.get("mapping_scope") != "concept":
                report.error(f"{path}.mapping_scope", "concept mapping must use mapping_scope=concept")
            if ".external_mappings" in path and mapping.get("mapping_scope") != "profile":
                report.error(f"{path}.mapping_scope", "profile mapping must use mapping_scope=profile")
            if status in {"mapped", "deprecated_mapping"}:
                if not isinstance(mapping.get("code"), str) or not mapping["code"].strip():
                    report.error(f"{path}.code", f"status={status} requires a non-empty code")
                if not refs:
                    report.error(f"{path}.source_reference_keys", f"status={status} requires a source")
                _check_source_statuses(refs, source_map, VERIFIED_SOURCE_STATUSES, path, report)
            if status == "no_match" and not str(mapping.get("note") or "").strip():
                report.error(f"{path}.note", "no_match requires a searched-system conclusion note")
        else:
            status = mapping.get("mapping_status")
            if status in {"source_verified", "human_reviewed", "deprecated"}:
                if not refs:
                    report.error(f"{path}.source_reference_keys", f"status={status} requires a source")
                _check_source_statuses(refs, source_map, VERIFIED_SOURCE_STATUSES, path, report)


def _check_unique_record_keys(record: dict[str, Any], report: Report) -> None:
    profiles = [_as_dict(item) for item in _as_list(record.get("profiles"))]
    claims = [_as_dict(item) for item in _as_list(record.get("use_evidence_claims"))]
    profile_keys = [item.get("profile_key") for item in profiles]
    claim_keys = [item.get("claim_key") for item in claims]
    for key in sorted(_duplicates(value for value in profile_keys if isinstance(value, str))):
        report.error("profiles", f"duplicate profile_key {key!r}")
    for key in sorted(_duplicates(value for value in claim_keys if isinstance(value, str))):
        report.error("use_evidence_claims", f"duplicate claim_key {key!r}")

    context_keys: list[str] = []
    computation_keys: list[str] = []
    for profile in profiles:
        for context in _as_list(profile.get("reference_contexts")):
            key = _as_dict(context).get("context_key")
            if isinstance(key, str):
                context_keys.append(key)
        computation = profile.get("derived_computation")
        if isinstance(computation, dict):
            key = computation.get("computation_key")
            if isinstance(key, str):
                computation_keys.append(key)
    for key in sorted(_duplicates(context_keys)):
        report.error("reference_contexts", f"duplicate context_key {key!r}")
    for key in sorted(_duplicates(computation_keys)):
        report.error("derived_computations", f"duplicate computation_key {key!r}")


def _check_computations(
    record: dict[str, Any], candidate_keys: set[str] | None, report: Report
) -> None:
    for p_index, value in enumerate(_as_list(record.get("profiles"))):
        profile = _as_dict(value)
        path = f"profiles[{p_index}]"
        computation = profile.get("derived_computation")
        if (
            profile.get("measurement_nature") == "derived"
            and profile.get("profile_status") in {"source_verified", "human_reviewed", "active"}
            and not isinstance(computation, dict)
        ):
            report.error(f"{path}.derived_computation", "reviewed derived profile requires computation metadata")
            continue
        if not isinstance(computation, dict):
            continue
        inputs = [_as_dict(item) for item in _as_list(computation.get("inputs"))]
        input_keys = [item.get("input_key") for item in inputs]
        for key in sorted(_duplicates(value for value in input_keys if isinstance(value, str))):
            report.error(f"{path}.derived_computation.inputs", f"duplicate input_key {key!r}")

        registry_inputs: set[str] = set()
        context_inputs: set[str] = set()
        for i_index, item in enumerate(inputs):
            input_path = f"{path}.derived_computation.inputs[{i_index}]"
            kind = item.get("input_kind")
            candidate_key = item.get("candidate_key")
            context_key = item.get("context_key")
            constant_value = item.get("constant_value")
            if kind == "registry_concept":
                if not isinstance(candidate_key, str) or not candidate_key:
                    report.error(f"{input_path}.candidate_key", "registry_concept input requires candidate_key")
                else:
                    registry_inputs.add(candidate_key)
                    if candidate_keys is not None and candidate_key not in candidate_keys:
                        report.error(f"{input_path}.candidate_key", f"unknown candidate {candidate_key!r}")
                if context_key is not None or constant_value is not None:
                    report.error(input_path, "registry_concept input cannot carry context_key or constant_value")
            elif kind == "user_context":
                if not isinstance(context_key, str) or not context_key:
                    report.error(f"{input_path}.context_key", "user_context input requires context_key")
                else:
                    context_inputs.add(context_key)
                if candidate_key is not None or constant_value is not None:
                    report.error(input_path, "user_context input cannot carry candidate_key or constant_value")
            elif kind == "constant":
                if constant_value is None:
                    report.error(f"{input_path}.constant_value", "constant input requires constant_value")
                if candidate_key is not None or context_key is not None:
                    report.error(input_path, "constant input cannot carry candidate_key or context_key")
            elif kind == "categorical_parameter":
                if not isinstance(context_key, str) or not context_key:
                    report.error(f"{input_path}.context_key", "categorical_parameter requires a reviewed parameter key")
                else:
                    context_inputs.add(context_key)
                if candidate_key is not None:
                    report.error(f"{input_path}.candidate_key", "categorical_parameter cannot carry candidate_key")
            else:
                report.error(f"{input_path}.input_kind", f"unsupported input_kind {kind!r}")

        computation_key = str(computation.get("computation_key") or "")
        contract = KNOWN_COMPUTATION_CONTRACTS.get(computation_key)
        if contract is not None:
            missing_registry = sorted(contract["registry_inputs"] - registry_inputs)
            missing_context = sorted(contract["context_inputs"] - context_inputs)
            for key in missing_registry:
                report.error(
                    f"{path}.derived_computation.inputs",
                    f"{computation_key} requires registry_concept input {key!r}",
                )
            for key in missing_context:
                report.error(
                    f"{path}.derived_computation.inputs",
                    f"{computation_key} requires context input {key!r}",
                )

def _check_claims(
    record: dict[str, Any], source_map: dict[str, dict[str, Any]], report: Report
) -> None:
    lifecycle = record.get("lifecycle_status")
    claims = [_as_dict(item) for item in _as_list(record.get("use_evidence_claims"))]
    statuses = [claim.get("claim_status") for claim in claims]
    if lifecycle in {"human_reviewed", "active"}:
        for index, claim in enumerate(claims):
            status = claim.get("claim_status")
            if status not in {"human_reviewed", "deprecated"}:
                report.error(
                    f"use_evidence_claims[{index}].claim_status",
                    f"{lifecycle} concept cannot contain output-eligible claim_status={status!r}",
                )
            if status == "human_reviewed":
                _check_source_statuses(
                    _as_list(claim.get("source_reference_keys")),
                    source_map,
                    CONTENT_VERIFIED,
                    f"use_evidence_claims[{index}]",
                    report,
                )
        if lifecycle == "active" and "human_reviewed" not in statuses:
            report.error("use_evidence_claims", "active concept requires at least one human_reviewed claim")
    for index, claim in enumerate(claims):
        if claim.get("claim_status") == "source_verified":
            _check_source_statuses(
                _as_list(claim.get("source_reference_keys")),
                source_map,
                CONTENT_VERIFIED,
                f"use_evidence_claims[{index}]",
                report,
            )


def _reviewed_source_sections(record: dict[str, Any]) -> list[tuple[str, list[str]]]:
    sections: list[tuple[str, list[str]]] = [
        ("definition_source_keys", _as_list(record.get("definition_source_keys")))
    ]
    for p_index, value in enumerate(_as_list(record.get("profiles"))):
        profile = _as_dict(value)
        if profile.get("profile_status") in {"human_reviewed", "active"}:
            sections.append(
                (f"profiles[{p_index}].source_reference_keys", _as_list(profile.get("source_reference_keys")))
            )
        for r_index, ref in enumerate(_as_list(profile.get("reference_contexts"))):
            sections.append(
                (
                    f"profiles[{p_index}].reference_contexts[{r_index}]",
                    _as_list(_as_dict(ref).get("source_reference_keys")),
                )
            )
    for m_path, mapping, kind in _all_mappings(record):
        status = mapping.get("status" if kind == "external" else "mapping_status")
        if status in {"mapped", "deprecated_mapping", "source_verified", "human_reviewed", "deprecated"}:
            sections.append((m_path, _as_list(mapping.get("source_reference_keys"))))
    return sections


def _check_source_lifecycle(
    record: dict[str, Any], source_map: dict[str, dict[str, Any]], report: Report
) -> None:
    lifecycle = record.get("lifecycle_status")
    definition_keys = _as_list(record.get("definition_source_keys"))
    profiles = [_as_dict(item) for item in _as_list(record.get("profiles"))]
    if lifecycle == "source_verified":
        _check_source_statuses(
            definition_keys, source_map, VERIFIED_SOURCE_STATUSES, "definition_source_keys", report
        )
        if definition_keys and not any(
            source_map.get(key, {}).get("verification_status") == "content_verified"
            for key in definition_keys
        ):
            report.warn(
                "definition_source_keys",
                "definition authority is metadata_verified only; content_verified is recommended",
            )
        for index, profile in enumerate(profiles):
            if profile.get("profile_status") in {"source_verified", "human_reviewed", "active"}:
                _check_source_statuses(
                    _as_list(profile.get("source_reference_keys")),
                    source_map,
                    VERIFIED_SOURCE_STATUSES,
                    f"profiles[{index}]",
                    report,
                )
    if lifecycle in {"human_reviewed", "active"}:
        for path, keys in _reviewed_source_sections(record):
            _check_source_statuses(keys, source_map, REVIEWED_SOURCE_STATUSES, path, report)
        if lifecycle == "active" and source_map and all(
            source.get("verification_status") == "pending" for source in source_map.values()
        ):
            report.error("source_references", "active concept cannot rely only on pending sources")

    for index, profile in enumerate(profiles):
        computation = profile.get("derived_computation")
        if not isinstance(computation, dict):
            continue
        if profile.get("profile_status") not in {"source_verified", "human_reviewed", "active"}:
            continue
        path = f"profiles[{index}].derived_computation.source_reference_keys"
        keys = _as_list(computation.get("source_reference_keys"))
        if not keys:
            report.error(path, "reviewed computation requires a content-verified equation source")
        _check_source_statuses(keys, source_map, CONTENT_VERIFIED, path, report)

def _check_system_relations(
    record: dict[str, Any], source_map: dict[str, dict[str, Any]], report: Report
) -> None:
    if record.get("lifecycle_status") not in {"human_reviewed", "active"}:
        return
    evidence_roles = {
        "definition_authority",
        "measurement_method",
        "guideline_recommendation",
        "systematic_review_evidence",
        "validation_evidence",
        "other_reviewed_role",
    }
    for index, value in enumerate(_as_list(record.get("system_relations"))):
        relation = _as_dict(value)
        path = f"system_relations[{index}]"
        refs = _as_list(relation.get("source_reference_keys"))
        if relation.get("confidence") == "unreviewed":
            report.error(f"{path}.confidence", "reviewed concept cannot use unreviewed system relation")
        _check_source_statuses(refs, source_map, REVIEWED_SOURCE_STATUSES, path, report)
        sources = [source_map[key] for key in refs if key in source_map]
        if relation.get("relationship_type") == "biological_relationship":
            if not any(
                source.get("verification_status") == "content_verified"
                and source.get("source_role") in evidence_roles
                for source in sources
            ):
                report.error(path, "biological relationship requires reviewed evidence source")
        elif relation.get("relationship_type") == "product_grouping":
            if not any(
                source.get("source_role") in {"internal_governance", "other_reviewed_role"}
                and source.get("verification_status") in REVIEWED_SOURCE_STATUSES
                for source in sources
            ):
                report.error(path, "product grouping requires reviewed governance source")


def _check_lifecycle_relations(
    record: dict[str, Any], candidate_keys: set[str] | None, report: Report
) -> None:
    seen: set[tuple[Any, Any]] = set()
    for index, value in enumerate(_as_list(record.get("lifecycle_relations"))):
        relation = _as_dict(value)
        path = f"lifecycle_relations[{index}]"
        target = relation.get("target_candidate_key")
        relation_type = relation.get("relationship_type")
        if not isinstance(target, str) or CANDIDATE_KEY_RE.fullmatch(target) is None:
            report.error(f"{path}.target_candidate_key", "must be a well-formed candidate key")
        elif candidate_keys is not None and target not in candidate_keys:
            report.error(f"{path}.target_candidate_key", f"unknown candidate {target!r}")
        target_id = relation.get("target_registry_id")
        if target_id is not None and (
            not isinstance(target_id, str) or REGISTRY_ID_RE.fullmatch(target_id) is None
        ):
            report.error(f"{path}.target_registry_id", "must be null or a well-formed Registry ID")
        identity = (relation_type, target)
        if identity in seen:
            report.error(path, "duplicate lifecycle relationship")
        seen.add(identity)


def _check_record_lifecycle(record: dict[str, Any], report: Report) -> None:
    lifecycle = record.get("lifecycle_status")
    profiles = [_as_dict(item) for item in _as_list(record.get("profiles"))]
    if lifecycle == "source_verified" and not any(
        profile.get("profile_status") in {"source_verified", "human_reviewed", "active"}
        for profile in profiles
    ):
        report.error("profiles", "source_verified concept requires a source-verified profile")
    if lifecycle == "human_reviewed" and not any(
        profile.get("profile_status") in {"human_reviewed", "active"} for profile in profiles
    ):
        report.error("profiles", "human_reviewed concept requires a reviewed profile")
    if lifecycle == "active":
        if not isinstance(record.get("registry_id"), str):
            report.error("registry_id", "active concept requires Registry ID")
        if not any(profile.get("profile_status") == "active" for profile in profiles):
            report.error("profiles", "active concept requires an active profile")
        governance = _as_dict(record.get("governance_metadata"))
        if not _as_list(governance.get("reviewed_by")) or not governance.get("reviewed_date"):
            report.error("governance_metadata", "active concept requires reviewer and review date")


def _check_governance_formats(record: dict[str, Any], report: Report) -> None:
    reviewed_date = _as_dict(record.get("governance_metadata")).get("reviewed_date")
    if reviewed_date is None:
        return
    if not isinstance(reviewed_date, str):
        report.error("governance_metadata.reviewed_date", "must be an ISO 8601 calendar date")
        return
    try:
        date.fromisoformat(reviewed_date)
    except ValueError:
        report.error("governance_metadata.reviewed_date", "must be a valid ISO 8601 calendar date")


def _record_requires_candidate_ledger(record: dict[str, Any]) -> bool:
    for profile in _as_list(record.get("profiles")):
        computation = _as_dict(_as_dict(profile).get("derived_computation"))
        for item in _as_list(computation.get("inputs")):
            if _as_dict(item).get("input_kind") == "registry_concept":
                return True
    return False


def validate_record_semantics(
    record: dict[str, Any], candidate_keys: set[str] | None = None
) -> Report:
    report = Report()
    if not isinstance(record, dict):
        report.error("record", "must be a JSON object")
        return report
    _walk_personal_fields(record, "record", report)
    _check_namespace(record, report)
    _check_registry_id(record, report)
    _check_unit_policy(record, report)
    _check_governance_formats(record, report)
    source_map = _source_pool(record, report)
    _check_unique_record_keys(record, report)
    _check_mappings(record, source_map, report)
    _check_computations(record, candidate_keys, report)
    _check_claims(record, source_map, report)
    _check_source_lifecycle(record, source_map, report)
    _check_system_relations(record, source_map, report)
    _check_lifecycle_relations(record, candidate_keys, report)
    _check_record_lifecycle(record, report)
    if record.get("candidate_key") in DEVICE_MAPPING_LAYER_KEYS:
        report.error("candidate_key", "device-mapping planning item cannot become a Registry concept")
    return report


def _candidate_keys(ledger: dict[str, Any]) -> set[str]:
    return {
        row.get("candidate_key")
        for row in _as_list(ledger.get("core_candidates"))
        + _as_list(ledger.get("extended_candidates"))
        if isinstance(row, dict) and isinstance(row.get("candidate_key"), str)
    }


def validate_candidate_ledger(ledger: dict[str, Any]) -> Report:
    report = Report()
    metadata = _as_dict(ledger.get("document_metadata"))
    core = [_as_dict(item) for item in _as_list(ledger.get("core_candidates"))]
    extended = [_as_dict(item) for item in _as_list(ledger.get("extended_candidates"))]
    rows = core + extended
    keys = [row.get("candidate_key") for row in rows]
    for key in sorted(_duplicates(value for value in keys if isinstance(value, str))):
        report.error("candidate_ledger", f"duplicate candidate_key {key!r}")
    if len(core) != 53:
        report.error("core_candidates", f"expected 53, found {len(core)}")
    counts = Counter(row.get("namespace") for row in core)
    expected_counts = Counter({"BM": 29, "ME": 20, "SC": 4})
    if counts != expected_counts:
        report.error("core_candidates", f"namespace counts {dict(counts)} != {dict(expected_counts)}")
    expected_metadata_counts = {"BM": 29, "ME": 20, "SC": 4, "QS": 0, "total": 53}
    if metadata.get("core_expected_counts") != expected_metadata_counts:
        report.error("candidate.document_metadata.core_expected_counts", "does not match Core rows")
    if metadata.get("extended_count") != len(extended):
        report.error("candidate.document_metadata.extended_count", f"expected {len(extended)}")
    eligibility_counts = dict(sorted(Counter(row.get("registry_eligibility") for row in extended).items()))
    if metadata.get("extended_eligibility_counts") != eligibility_counts:
        report.error(
            "candidate.document_metadata.extended_eligibility_counts",
            f"{metadata.get('extended_eligibility_counts')!r} != {eligibility_counts!r}",
        )
    active_count = sum(row.get("lifecycle_status") == "active" for row in rows)
    if metadata.get("active_registry_records") != active_count:
        report.error("candidate.document_metadata.active_registry_records", f"expected {active_count}")
    expected_id_policy = "Option B: namespace frozen; numeric IDs not assigned"
    if metadata.get("numeric_id_policy") != expected_id_policy:
        report.error("candidate.document_metadata.numeric_id_policy", "Option B policy is required")
    if any(row.get("registry_id") is not None for row in rows):
        report.error("candidate_ledger", "numeric Registry IDs must remain null")
    if any(row.get("lifecycle_status") == "active" for row in rows):
        report.error("candidate_ledger", "candidate ledger cannot contain active records")
    first_wave = {row.get("candidate_key") for row in core if row.get("first_wave_proposed") is True}
    if first_wave != FIRST_WAVE_KEYS:
        report.error("core_candidates", "First Wave 12 set changed")
    core_keys = {row.get("candidate_key") for row in core}
    if core_keys & FORMER_RED_KEYS:
        report.error("core_candidates", "former RED candidates re-entered Core")
    if core_keys & DEVICE_MAPPING_LAYER_KEYS:
        report.error("core_candidates", "proprietary device-mapping planning item entered Core")

    by_key = {row.get("candidate_key"): row for row in rows}
    for index, row in enumerate(rows):
        namespace = row.get("namespace")
        if namespace is not None:
            allowed = NAMESPACE_MATRIX.get(namespace)
            if allowed is None or row.get("information_type") not in allowed:
                report.error(
                    f"candidates[{index}]",
                    f"namespace/type mismatch: {namespace}/{row.get('information_type')}",
                )
    sleep_midpoint = by_key.get("sleep_midpoint", {})
    if sleep_midpoint.get("namespace") != "SC" or sleep_midpoint.get("information_type") != "derived_score_index":
        report.error("sleep_midpoint", "must be an Extended SC derived_score_index")
    for key in DEVICE_MAPPING_LAYER_KEYS:
        row = by_key.get(key, {})
        if row.get("namespace") is not None:
            report.error(key, "device-mapping layer item namespace must be null")
        if row.get("registry_eligibility") != "device_mapping_layer" or row.get("numeric_id_eligible") is not False:
            report.error(key, "device-mapping layer eligibility is inconsistent")
    sleep = by_key.get("sleep_total_time", {})
    if sleep.get("canonical_name_en") != "Total Sleep Time":
        report.error("sleep_total_time", "canonical English name regressed")
    if "Bilirubin" in _as_list(by_key.get("total_bilirubin", {}).get("aliases")):
        report.error("total_bilirubin", "generic Bilirubin alias is prohibited")
    oxygen_issues = " ".join(_as_list(by_key.get("oxygen_saturation", {}).get("preproduction_issues")))
    if "peripheral oxygen saturation" not in oxygen_issues:
        report.error("oxygen_saturation", "SpO2 peripheral-saturation boundary is missing")
    return report

def validate_migration_ledger(
    ledger: dict[str, Any], candidate_ledger: dict[str, Any]
) -> Report:
    report = Report()
    entries = [_as_dict(item) for item in _as_list(ledger.get("entries"))]
    if len(entries) != 169:
        report.error("migration.entries", f"expected 169, found {len(entries)}")
    family_counts = Counter(row.get("source_family") for row in entries)
    expected_families = Counter({"BS12": 12, "BR23": 23, "LEGACY120": 107, "MAP2": 27})
    if family_counts != expected_families:
        report.error("migration.entries", f"source coverage {dict(family_counts)} != {dict(expected_families)}")
    candidate_keys = _candidate_keys(candidate_ledger)
    for index, row in enumerate(entries):
        for key in _as_list(row.get("candidate_keys")):
            if key not in candidate_keys:
                report.error(f"migration.entries[{index}].candidate_keys", f"unknown candidate {key!r}")
    needs_review = [row for row in entries if row.get("migration_status") == "needs_review"]
    if len(needs_review) != 53:
        report.error("migration.entries", f"expected 53 needs_review rows, found {len(needs_review)}")
    silent = [
        row for row in entries
        if not _as_list(row.get("candidate_keys"))
        and row.get("migration_status") not in {"reference_only", "needs_review"}
    ]
    if silent:
        report.error("migration.entries", f"silent unmapped rows: {len(silent)}")
    scope_counts = Counter(row.get("blocking_scope") for row in entries)
    expected_scopes = Counter({
        "first_wave_blocker": 0,
        "core_preproduction": 10,
        "nonblocking_group_split": 15,
        "extended_deferred": 26,
        "not_blocking": 118,
    })
    if any(scope_counts[key] != count for key, count in expected_scopes.items()):
        report.error("migration.entries", f"blocking scopes {dict(scope_counts)} != {dict(expected_scopes)}")
    metadata = _as_dict(ledger.get("document_metadata"))
    actual_coverage = {
        "BS12": family_counts["BS12"],
        "BR23": family_counts["BR23"],
        "LEGACY120_unique_labels": family_counts["LEGACY120"],
        "MAP2": family_counts["MAP2"],
        "total": len(entries),
    }
    if metadata.get("source_coverage_actual") != actual_coverage:
        report.error("migration.document_metadata.source_coverage_actual", "does not match migration rows")
    if metadata.get("needs_review_count") != len(needs_review):
        report.error("migration.document_metadata.needs_review_count", f"expected {len(needs_review)}")
    if metadata.get("silent_unmapped_count") != len(silent):
        report.error("migration.document_metadata.silent_unmapped_count", f"expected {len(silent)}")
    actual_scope_counts = {
        "core_preproduction": scope_counts["core_preproduction"],
        "extended_deferred": scope_counts["extended_deferred"],
        "first_wave_blocker": scope_counts["first_wave_blocker"],
        "nonblocking_group_split": scope_counts["nonblocking_group_split"],
        "not_blocking": scope_counts["not_blocking"],
    }
    if metadata.get("blocking_scope_counts") != actual_scope_counts:
        report.error("migration.document_metadata.blocking_scope_counts", "does not match migration rows")
    scalar_scope_fields = {
        "first_wave_blocker_count": "first_wave_blocker",
        "core_preproduction_count": "core_preproduction",
        "nonblocking_group_split_count": "nonblocking_group_split",
        "extended_deferred_count": "extended_deferred",
        "not_blocking_count": "not_blocking",
    }
    for field_name, scope_name in scalar_scope_fields.items():
        if field_name in metadata and metadata.get(field_name) != scope_counts[scope_name]:
            report.error(
                f"migration.document_metadata.{field_name}",
                f"expected {scope_counts[scope_name]}",
            )

    generic_bilirubin = next(
        (
            row for row in entries
            if row.get("source_family") == "LEGACY120" and row.get("legacy_label") == "Bilirubin"
        ),
        None,
    )
    if not generic_bilirubin or generic_bilirubin.get("migration_status") != "needs_review":
        report.error("migration.Bilirubin", "generic Bilirubin must remain needs_review")
    expected_sleep_rows = {"BR23:sleep_duration", "LEGACY120:unique_label_004"}
    actual_sleep_rows = {
        row.get("migration_entry_key"): row
        for row in entries if row.get("migration_entry_key") in expected_sleep_rows
    }
    if set(actual_sleep_rows) != expected_sleep_rows:
        report.error("migration.Sleep Duration", "expected legacy Sleep Duration rows are missing")
    for key, row in actual_sleep_rows.items():
        if row.get("migration_status") != "needs_review" or row.get("blocking_scope") != "not_blocking":
            report.error(key, "legacy Sleep Duration must remain needs_review but not_blocking")
        if "does not block clean canonical Total Sleep Time record production" not in str(row.get("migration_note")):
            report.error(key, "nonblocking clean-production note is missing")
    return report


def _source(key: str, role: str, status: str = "content_verified") -> dict[str, Any]:
    return {
        "source_key": key,
        "title": key,
        "source_role": role,
        "verification_status": status,
    }


def _unit_policy(mode: str = "single_canonical", unit_code: str = "/min") -> dict[str, Any]:
    if mode == "single_canonical":
        return {
            "mode": mode,
            "canonical_unit": {
                "unit_code": unit_code,
                "unit_system": "UCUM",
                "status": "canonical",
            },
            "note": "Reviewed canonical unit.",
        }
    return {"mode": mode, "canonical_unit": None, "note": "Pending unit review."}


def _profile(status: str, nature: str = "measured") -> dict[str, Any]:
    return {
        "profile_key": "profile.primary",
        "profile_status": status,
        "measurement_nature": nature,
        "source_modality": "clinical_device",
        "method_comparability_status": "context_dependent",
        "accepted_units": [],
        "reference_contexts": [],
        "external_mappings": [],
        "device_mappings": [],
        "profile_limitations": ["Method context required."],
        "source_reference_keys": ["s.method"] if status != "proposed" else [],
        "derived_computation": None,
    }


def _claim(status: str = "human_reviewed") -> dict[str, Any]:
    return {
        "claim_key": "claim.education",
        "claim_status": status,
        "use_context": "general education",
        "claim_summary": "Bounded educational use.",
        "population_or_context": "General adult context.",
        "evidence_level": "E1",
        "evidence_posture": "general_consensus",
        "source_reference_keys": ["s.claim"],
        "supports": ["General educational interpretation."],
        "does_not_support": ["Diagnosis or treatment."],
        "uncertainty": [],
    }


def _base_record(lifecycle: str = "proposed") -> dict[str, Any]:
    reviewed = lifecycle in {"human_reviewed", "active"}
    record = {
        "candidate_key": "heart_rate",
        "registry_id": "ME-000001" if lifecycle == "active" else None,
        "namespace": "ME",
        "lifecycle_status": lifecycle,
        "canonical_name_zh": "心率",
        "canonical_name_en": "Heart Rate",
        "aliases": [],
        "legacy_codes": [],
        "information_type": "physiological_measurement",
        "construct_type": "physiological_measurement",
        "construct_definition": "Heart beats per unit time under a stated profile.",
        "allowed_measurement_natures": ["measured"],
        "value_type": "number",
        "unit_policy": _unit_policy("single_canonical" if reviewed else "pending"),
        "source_references": [],
        "definition_source_keys": [],
        "profiles": [],
        "use_evidence_claims": [],
        "system_relations": [],
        "external_mappings": [],
        "interpretation_limitations": ["Context and method matter."],
        "agent_permissions": {
            "permitted_uses": ["General education."],
            "prohibited_uses": ["Diagnosis."],
            "action_authorization": "none",
            "authorization_note": "No action authorization.",
        },
        "personalized_target_support": {
            "support_status": "requires_governance",
            "prerequisites": ["User context and permission."],
            "boundary_note": "No public personal target value.",
        },
        "lifecycle_relations": [],
        "governance_metadata": {},
    }
    if reviewed:
        record["version"] = "v0.1"
        record["source_references"] = [
            _source("s.definition", "definition_authority"),
            _source("s.method", "measurement_method"),
            _source("s.claim", "systematic_review_evidence"),
        ]
        record["definition_source_keys"] = ["s.definition"]
        record["profiles"] = [_profile("active" if lifecycle == "active" else "human_reviewed")]
        record["use_evidence_claims"] = [_claim()]
        record["governance_metadata"] = {
            "reviewed_by": ["Founder"],
            "reviewed_date": "2026-08-22",
            "status_note": "Self-test fixture only.",
        }
    return record


def _computation_input(
    input_key: str,
    input_kind: str,
    *,
    candidate_key: str | None = None,
    context_key: str | None = None,
    role: str,
    unit_code: str | None = None,
) -> dict[str, Any]:
    return {
        "input_key": input_key,
        "input_kind": input_kind,
        "candidate_key": candidate_key,
        "context_key": context_key,
        "constant_value": None,
        "role": role,
        "required": True,
        "unit_code": unit_code,
        "note": None,
    }


def _derived_record(kind: str, lifecycle: str = "human_reviewed") -> dict[str, Any]:
    record = _base_record(lifecycle)
    record["namespace"] = "SC"
    if lifecycle == "active":
        record["registry_id"] = "SC-000001"
    record["information_type"] = "derived_score_index"
    record["construct_type"] = "derived_score_index"
    record["allowed_measurement_natures"] = ["derived"]
    record["source_references"].append(_source("s.equation", "measurement_method"))
    profile = _profile("active" if lifecycle == "active" else "human_reviewed", "derived")
    profile["source_modality"] = "calculated"

    if kind == "bmi":
        record.update({
            "candidate_key": "body_mass_index",
            "canonical_name_zh": "身体质量指数",
            "canonical_name_en": "Body Mass Index",
            "construct_definition": "Body weight divided by squared height under a reviewed computation profile.",
            "unit_policy": _unit_policy("single_canonical", "kg/m2"),
        })
        profile["derived_computation"] = {
            "computation_key": "bmi.weight_kg_height_m2",
            "equation_name": "Body Mass Index",
            "equation_version": "reviewed-fixture-v1",
            "formula_or_equation": "body_weight_kg / (height_m * height_m)",
            "inputs": [
                _computation_input(
                    "height", "registry_concept", candidate_key="height", role="height", unit_code="m"
                ),
                _computation_input(
                    "body_weight",
                    "registry_concept",
                    candidate_key="body_weight",
                    role="body weight",
                    unit_code="kg",
                ),
            ],
            "source_reference_keys": ["s.equation"],
            "output_unit_policy": _unit_policy("single_canonical", "kg/m2"),
            "output_unit_note": "Reviewed BMI representation for self-test only.",
            "computation_limitations": ["Input units and measurement context must be verified."],
        }
    elif kind == "egfr":
        record.update({
            "candidate_key": "estimated_glomerular_filtration_rate",
            "canonical_name_zh": "估算肾小球滤过率",
            "canonical_name_en": "Estimated Glomerular Filtration Rate",
            "construct_definition": "Equation-derived kidney filtration estimate under a named computation contract.",
            "unit_policy": _unit_policy("single_canonical", "mL/min/{1.73_m2}"),
        })
        profile["derived_computation"] = {
            "computation_key": "egfr.ckd_epi_2021_creatinine",
            "equation_name": "CKD-EPI 2021 Creatinine Equation",
            "equation_version": "2021 creatinine",
            "formula_or_equation": "Reviewed fixture contract; full clinical equation omitted from self-test data.",
            "inputs": [
                _computation_input(
                    "creatinine",
                    "registry_concept",
                    candidate_key="creatinine",
                    role="serum creatinine",
                    unit_code="mg/dL",
                ),
                _computation_input(
                    "age_years", "user_context", context_key="age_years", role="age in years", unit_code="a"
                ),
                _computation_input(
                    "sex_at_birth",
                    "categorical_parameter",
                    context_key="sex_at_birth",
                    role="equation category parameter",
                ),
            ],
            "source_reference_keys": ["s.equation"],
            "output_unit_policy": _unit_policy("single_canonical", "mL/min/{1.73_m2}"),
            "output_unit_note": "Equation-specific output representation.",
            "computation_limitations": ["Equation applicability and input method must be reviewed."],
        }
    else:
        raise ValueError(f"unsupported derived fixture kind: {kind}")
    record["profiles"] = [profile]
    return record


def run_self_test(schema: dict[str, Any] | None) -> tuple[Report, bool, dict[str, int]]:
    report = Report()
    candidate_keys = {
        "heart_rate",
        "creatinine",
        "estimated_glomerular_filtration_rate",
        "height",
        "body_weight",
        "body_mass_index",
        "total_cholesterol",
        "hdl_cholesterol",
        "sleep_total_time",
        "time_in_bed",
    }
    valid_cases = {
        "valid proposed record": _base_record("proposed"),
        "valid human-reviewed record": _base_record("human_reviewed"),
        "valid active record": _base_record("active"),
        "valid BMI derived record": _derived_record("bmi"),
        "valid eGFR creatinine record": _derived_record("egfr"),
    }

    invalid_cases: dict[str, dict[str, Any]] = {}
    pending = _base_record("active")
    for source in pending["source_references"]:
        source["verification_status"] = "pending"
    invalid_cases["active pending-only sources"] = pending

    mismatch = _base_record("proposed")
    mismatch["namespace"] = "BM"
    invalid_cases["BM physiological measurement"] = mismatch

    bad_unit = _base_record("proposed")
    bad_unit["unit_policy"] = {
        "mode": "single_canonical",
        "canonical_unit": {
            "unit_code": None,
            "unit_system": "pending",
            "status": "pending",
        },
        "note": "Pending.",
    }
    invalid_cases["single canonical pending unit"] = bad_unit

    no_mapping_source = _base_record("proposed")
    no_mapping_source["external_mappings"] = [{
        "mapping_key": "loinc.main",
        "mapping_scope": "concept",
        "system": "LOINC",
        "code": "8867-4",
        "status": "mapped",
        "confidence": "high",
        "source_reference_keys": [],
    }]
    invalid_cases["mapped LOINC without source"] = no_mapping_source

    unreviewed_claim = _base_record("active")
    unreviewed_claim["use_evidence_claims"][0]["claim_status"] = "proposed"
    invalid_cases["active unreviewed claim"] = unreviewed_claim

    egfr = _derived_record("egfr")
    egfr["profiles"][0]["derived_computation"]["inputs"] = [
        egfr["profiles"][0]["derived_computation"]["inputs"][0]
    ]
    invalid_cases["eGFR without user context"] = egfr

    duplicate_source = _base_record("human_reviewed")
    duplicate_source["source_references"].append(copy.deepcopy(duplicate_source["source_references"][0]))
    invalid_cases["duplicate source keys"] = duplicate_source

    dangling = _base_record("human_reviewed")
    dangling["definition_source_keys"] = ["s.missing"]
    invalid_cases["dangling source key"] = dangling

    duplicate_mapping = _base_record("human_reviewed")
    duplicate_mapping["source_references"].append(_source("s.mapping", "measurement_method", "metadata_verified"))
    duplicate_mapping["external_mappings"] = [{
        "mapping_key": "map.same",
        "mapping_scope": "concept",
        "system": "LOINC",
        "code": "8867-4",
        "status": "mapped",
        "confidence": "high",
        "source_reference_keys": ["s.mapping"],
    }]
    duplicate_mapping["profiles"][0]["external_mappings"] = [{
        "mapping_key": "map.same",
        "mapping_scope": "profile",
        "system": "LOINC",
        "code": "8867-4",
        "status": "mapped",
        "confidence": "high",
        "source_reference_keys": ["s.mapping"],
    }]
    invalid_cases["duplicate mapping key"] = duplicate_mapping

    id_mismatch = _base_record("active")
    id_mismatch["registry_id"] = "BM-000001"
    invalid_cases["Registry ID namespace mismatch"] = id_mismatch

    pending_equation = _derived_record("egfr", "active")
    next(
        source for source in pending_equation["source_references"] if source["source_key"] == "s.equation"
    )["verification_status"] = "pending"
    invalid_cases["active derived record with pending equation source"] = pending_equation

    malformed_date = _base_record("active")
    malformed_date["governance_metadata"]["reviewed_date"] = "2026-99-99"
    invalid_cases["malformed reviewed date"] = malformed_date

    schema_available = _jsonschema_components() is not None
    counts = {
        "valid_total": len(valid_cases),
        "valid_passed": 0,
        "valid_failed": 0,
        "invalid_total": len(invalid_cases),
        "invalid_rejected": 0,
        "invalid_accepted": 0,
    }
    schema_failures: list[str] = []

    for name, record in valid_cases.items():
        semantic_report = validate_record_semantics(record, candidate_keys)
        if semantic_report.errors:
            counts["valid_failed"] += 1
            report.error(name, "; ".join(semantic_report.errors))
        else:
            counts["valid_passed"] += 1
        if schema is not None and schema_available:
            schema_report, _ = validate_schema_instance(schema, record)
            if schema_report.errors:
                schema_failures.append(f"{name}: {'; '.join(schema_report.errors)}")

    for name, record in invalid_cases.items():
        semantic_report = validate_record_semantics(record, candidate_keys)
        if semantic_report.errors:
            counts["invalid_rejected"] += 1
        else:
            counts["invalid_accepted"] += 1
            report.error(name, "invalid counterexample was accepted by semantic validation")

    if schema is not None and schema_available:
        malformed_schema_report, _ = validate_schema_instance(schema, malformed_date)
        if not malformed_schema_report.errors:
            schema_failures.append("malformed reviewed date: FormatChecker accepted invalid date")
        for failure in schema_failures:
            report.error("schema-backed self-test", failure)
    elif not schema_available:
        report.warn("self-test", "Draft 2020-12 instance validator unavailable")

    print(f"SELF_TEST_VALID_TOTAL={counts['valid_total']}")
    print(f"SELF_TEST_VALID_PASSED={counts['valid_passed']}")
    print(f"SELF_TEST_VALID_FAILED={counts['valid_failed']}")
    print(f"SELF_TEST_INVALID_TOTAL={counts['invalid_total']}")
    print(f"SELF_TEST_INVALID_REJECTED={counts['invalid_rejected']}")
    print(f"SELF_TEST_INVALID_ACCEPTED={counts['invalid_accepted']}")
    return report, schema_available, counts

def _print_report(report: Report) -> None:
    for warning in report.warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    for error in report.errors:
        print(f"ERROR: {error}", file=sys.stderr)


def _default_schema_path() -> Path:
    return Path(__file__).resolve().parents[3] / "schemas" / "biomarker_measurement_registry_schema_v0.1.json"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate Congtie Biomarker and Measurement Registry authoring artifacts."
    )
    parser.add_argument("--schema", type=Path, help="Draft 2020-12 Registry Schema path")
    parser.add_argument("--record", type=Path, help="Registry concept record JSON path")
    parser.add_argument("--candidate-ledger", type=Path, help="Seed 001 Candidate Ledger path")
    parser.add_argument("--migration-ledger", type=Path, help="Seed 001 Migration Ledger path")
    parser.add_argument("--self-test", action="store_true", help="Run in-memory valid and invalid fixtures")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.self_test:
        if args.record or args.candidate_ledger or args.migration_ledger:
            print("ERROR: --self-test cannot be combined with record or ledger modes", file=sys.stderr)
            return EXIT_TOOL_FAILURE
        schema_path = args.schema or _default_schema_path()
        try:
            schema = _load_json(schema_path)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"ERROR: cannot load schema: {exc}", file=sys.stderr)
            return EXIT_TOOL_FAILURE
        report, available, _ = run_self_test(schema)
        _print_report(report)
        if report.errors:
            print("SEMANTIC_SELF_TEST=FAIL")
            return EXIT_VALIDATION_FAILURE
        print("SEMANTIC_SELF_TEST=PASS")
        if not available:
            print("SCHEMA_BACKED_SELF_TEST=NOT_RUN")
            print("DRAFT_2020_12_ENGINE=unavailable")
            print("RECORD_PRODUCTION=GATED")
            return EXIT_TOOL_FAILURE
        print("SCHEMA_BACKED_SELF_TEST=PASS")
        print("DRAFT_2020_12_ENGINE=available")
        return EXIT_VALID

    if args.record:
        if args.schema is None or args.migration_ledger is not None:
            print("ERROR: record mode requires --schema and cannot use --migration-ledger", file=sys.stderr)
            return EXIT_TOOL_FAILURE
        try:
            schema = _load_json(args.schema)
            record = _load_json(args.record)
            candidate_keys = None
            if args.candidate_ledger:
                candidate_keys = _candidate_keys(_load_json(args.candidate_ledger))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"ERROR: cannot load record-mode input: {exc}", file=sys.stderr)
            return EXIT_TOOL_FAILURE
        if _record_requires_candidate_ledger(record) and args.candidate_ledger is None:
            print(
                "Derived Registry-concept inputs require --candidate-ledger for lineage resolution.",
                file=sys.stderr,
            )
            return EXIT_TOOL_FAILURE
        report = validate_record_semantics(record, candidate_keys)
        schema_report, engine_available = validate_schema_instance(schema, record)
        report.extend(schema_report)
        _print_report(report)
        if report.errors:
            return EXIT_VALIDATION_FAILURE
        if not engine_available:
            print("Draft 2020-12 instance validator unavailable", file=sys.stderr)
            print("RECORD_PRODUCTION=GATED", file=sys.stderr)
            return EXIT_TOOL_FAILURE
        print("VALID: Registry concept record")
        return EXIT_VALID

    if args.candidate_ledger or args.migration_ledger:
        if not args.candidate_ledger or not args.migration_ledger:
            print("ERROR: ledger mode requires both --candidate-ledger and --migration-ledger", file=sys.stderr)
            return EXIT_TOOL_FAILURE
        try:
            candidate = _load_json(args.candidate_ledger)
            migration = _load_json(args.migration_ledger)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"ERROR: cannot load ledger: {exc}", file=sys.stderr)
            return EXIT_TOOL_FAILURE
        report = validate_candidate_ledger(candidate)
        report.extend(validate_migration_ledger(migration, candidate))
        _print_report(report)
        if report.errors:
            return EXIT_VALIDATION_FAILURE
        print("VALID: Candidate Ledger + Migration Ledger")
        return EXIT_VALID

    if args.schema:
        try:
            schema = _load_json(args.schema)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"ERROR: cannot load schema: {exc}", file=sys.stderr)
            return EXIT_TOOL_FAILURE
        report, available = validate_schema_definition(schema)
        _print_report(report)
        if report.errors:
            return EXIT_VALIDATION_FAILURE
        if not available:
            return EXIT_TOOL_FAILURE
        print("VALID: Draft 2020-12 Registry Schema")
        return EXIT_VALID

    print("ERROR: choose --record, ledger mode, --self-test, or --schema", file=sys.stderr)
    return EXIT_TOOL_FAILURE


if __name__ == "__main__":
    raise SystemExit(main())
