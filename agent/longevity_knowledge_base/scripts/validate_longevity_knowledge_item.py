#!/usr/bin/env python3
"""Validate one Congtie Longevity Information Library Markdown entry.

This is a structural and governance validator. It is not a medical fact
checker, clinical reviewer, evidence judge, or AI content reviewer.
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any, Sequence


REQUIRED_METADATA = (
    "schema_version",
    "entry_id",
    "entry_slug",
    "content_type",
    "information_layer",
    "title_zh",
    "title_en",
    "language",
    "primary_topic_id",
    "topic_ids",
    "status",
    "created_by",
    "created_date",
    "version",
)

REQUIRED_EVIDENCE_FIELDS = (
    "evidence_level",
    "evidence_posture",
    "source_type",
)

REQUIRED_SAFETY_FIELDS = (
    "safety_boundary",
    "allowed_use",
    "disallowed_use",
)

LIST_FIELDS = {
    "topic_ids",
    "topic_paths",
    "source_type",
    "source_urls",
    "allowed_use",
    "disallowed_use",
}

ALLOWED_PREFIXES = {
    "KN",
    "AR",
    "PV",
    "ED",
    "GV",
    "IH",
    "ES",
    "CL",
    "CC",
    "PN",
    "SN",
    "GL",
}

ALLOWED_CONTENT_TYPES = {
    "knowledge_entry",
    "action_resource",
    "progress_and_viewpoint",
    "education_article",
    "glossary_entry",
    "checklist",
    "clinician_conversation_preparation",
    "source_note",
    "evidence_summary",
    "protocol_note",
    "invalid_or_harmful_note",
    "governance_rule",
    "curation_rule",
    "safety_boundary",
}

ALLOWED_INFORMATION_LAYERS = {
    "knowledge",
    "action_resource",
    "progress_and_viewpoints",
    "education",
    "governance",
}

ALLOWED_STATUSES = {
    "draft",
    "ai_review_pending",
    "ai_reviewed",
    "human_review_pending",
    "needs_revision",
    "approved",
    "published",
    "archived",
    "rejected",
}

ALLOWED_EVIDENCE_LEVELS = {"E1", "E2", "E3", "E4", "E5", "E0", "EX"}
ALLOWED_RECOMMENDATION_PERMISSIONS = {"R0", "R1", "R2", "R3"}

ALLOWED_RESEARCH_STAGES = {
    "basic_research",
    "animal_study",
    "early_clinical",
    "clinical_trial",
    "real_world_study",
    "expert_debate",
    "product_development",
    "regulatory_review",
    "commercial_launch",
    "post_market_monitoring",
}

ALLOWED_ACTIONABILITY_STATUSES = {
    "not_applicable",
    "not_actionable",
    "education_only",
    "watchlist",
    "requires_professional_context",
    "future_candidate",
    "deprecated",
}

STANDARD_SOURCE_TYPES = {
    "official_guideline_china",
    "official_guideline_international",
    "professional_consensus",
    "peer_reviewed_meta_analysis",
    "peer_reviewed_rct",
    "peer_reviewed_observational",
    "peer_reviewed_mechanistic",
    "peer_reviewed_review",
    "professional_education_page",
    "professional_organization_article",
    "official_product_spec",
    "official_user_manual",
    "official_service_description",
    "founder_curated",
    "founder_direct_experience",
    "commercial_marketing_page",
    "ecommerce_listing",
    "user_review",
    "media_article",
    "commercial_claim_unverified",
}

KEPT_ALIGNMENT_SOURCE_TYPES = {
    "expert_interview",
    "expert_blog",
    "conference_talk",
}

SOURCE_TYPE_ALIASES = {
    "review_article": "peer_reviewed_review",
    "academic_review": "peer_reviewed_review",
    "peer_reviewed_review_article": "peer_reviewed_review",
}

DEPRECATED_SOURCE_TYPES: dict[str, str | None] = {}
MIGRATION_WARNING_SOURCE_TYPES = {"unknown_or_unverified"}

ENTRY_ID_PATTERN = re.compile(
    r"^(?P<prefix>[A-Z]{2})-(?P<topic>T\d{2}(?:\d{2}){0,2})-(?P<number>\d{4})$"
)
ENTRY_SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:[-_][a-z0-9]+)*$")
TOPIC_ID_PATTERN = re.compile(r"^T\d{2}(?:\.\d{2}){0,2}$")
VERSION_PATTERN = re.compile(r"^v\d+\.\d+$")

TAXONOMY_CANDIDATES = (
    Path("agent/longevity_topic_taxonomy.v0.1.md"),
    Path("agent/knowledge_seed_v0/longevity_topic_taxonomy.v0.1.md"),
)

NUTRITION_TOPIC_IDS = {"T05.02", "T07.05", "T07.06"}


class FrontmatterError(ValueError):
    """Raised when the supported YAML frontmatter subset cannot be parsed."""


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def strip_inline_comment(value: str) -> str:
    """Strip a simple YAML comment without touching quoted values."""
    quote: str | None = None
    escaped = False
    for index, character in enumerate(value):
        if escaped:
            escaped = False
            continue
        if character == "\\" and quote == '"':
            escaped = True
            continue
        if character in {"'", '"'}:
            if quote is None:
                quote = character
            elif quote == character:
                quote = None
            continue
        if character == "#" and quote is None:
            return value[:index].rstrip()
    return value.strip()


def parse_scalar(raw_value: str) -> Any:
    value = strip_inline_comment(raw_value.strip())
    if not value:
        return ""
    if value == "[]":
        return []
    if value == "{}":
        return {}
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.lower() in {"null", "none", "~"}:
        return None
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(item.strip()) for item in inner.split(",")]
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        try:
            return ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return value[1:-1]
    return value


def dedent_block(lines: Sequence[str]) -> list[str]:
    non_empty = [line for line in lines if line.strip()]
    if not non_empty:
        return []
    indent = min(len(line) - len(line.lstrip()) for line in non_empty)
    return [line[indent:] if line.strip() else "" for line in lines]


def parse_block_value(key: str, lines: Sequence[str]) -> Any:
    content = dedent_block(lines)
    non_empty = [line for line in content if line.strip() and not line.lstrip().startswith("#")]
    if not non_empty:
        return [] if key in LIST_FIELDS else ""

    if all(re.match(r"^-\s+", line) for line in non_empty):
        return [parse_scalar(re.sub(r"^-\s+", "", line, count=1)) for line in non_empty]

    # Nested mappings are outside the fields checked by this validator. Keep
    # their raw shape so required top-level fields are still distinguishable.
    return {"__raw__": "\n".join(content).strip()}


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str, list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise FrontmatterError("Missing YAML frontmatter")

    closing_index: int | None = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break
    if closing_index is None:
        raise FrontmatterError("Missing closing YAML frontmatter marker")

    frontmatter_lines = lines[1:closing_index]
    body = "\n".join(lines[closing_index + 1 :]).strip()
    data: dict[str, Any] = {}
    errors: list[str] = []

    index = 0
    while index < len(frontmatter_lines):
        line = frontmatter_lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        if line[0].isspace():
            errors.append(f"Unsupported top-level YAML indentation at line {index + 2}")
            index += 1
            continue

        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if not match:
            errors.append(f"Unsupported YAML frontmatter line {index + 2}: {line}")
            index += 1
            continue

        key, raw_value = match.group(1), match.group(2) or ""
        if key in data:
            errors.append(f"Duplicate frontmatter field: {key}")

        if raw_value in {"|", ">"}:
            block_start = index + 1
            block_end = block_start
            while block_end < len(frontmatter_lines):
                candidate = frontmatter_lines[block_end]
                if candidate and not candidate[0].isspace():
                    break
                block_end += 1
            block = dedent_block(frontmatter_lines[block_start:block_end])
            separator = "\n" if raw_value == "|" else " "
            data[key] = separator.join(line.strip() for line in block).strip()
            index = block_end
            continue

        if raw_value:
            data[key] = parse_scalar(raw_value)
            index += 1
            continue

        block_start = index + 1
        block_end = block_start
        while block_end < len(frontmatter_lines):
            candidate = frontmatter_lines[block_end]
            if candidate and not candidate[0].isspace():
                break
            block_end += 1
        data[key] = parse_block_value(key, frontmatter_lines[block_start:block_end])
        index = block_end

    return data, body, errors


def is_missing(value: Any) -> bool:
    return value is None or value == "" or value == []


def require_fields(data: dict[str, Any], fields: Sequence[str], errors: list[str]) -> None:
    for field in fields:
        if field not in data or is_missing(data[field]):
            errors.append(f"Missing required field: {field}")


def ensure_list(data: dict[str, Any], field: str, errors: list[str]) -> list[Any]:
    value = data.get(field)
    if not isinstance(value, list):
        errors.append(f"Field {field} must be a list")
        return []
    return value


def locate_taxonomy(root: Path) -> Path:
    for relative_path in TAXONOMY_CANDIDATES:
        candidate = root / relative_path
        if candidate.is_file():
            return candidate
    expected = ", ".join(str(path) for path in TAXONOMY_CANDIDATES)
    raise OSError(f"taxonomy file not found; checked: {expected}")


def load_taxonomy_ids(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return set(re.findall(r"\bT\d{2}(?:\.\d{2}){0,2}\b", text))


def validate_entry_id(
    data: dict[str, Any], taxonomy_ids: set[str], errors: list[str]
) -> None:
    # Single-file mode validates identity shape only. A future directory mode
    # should collect entry IDs first and report cross-file duplicates here.
    entry_id = data.get("entry_id")
    if not isinstance(entry_id, str) or not entry_id:
        return
    match = ENTRY_ID_PATTERN.fullmatch(entry_id)
    if not match:
        errors.append(
            "entry_id must match PREFIX-TOPICID-NNNN, for example KN-T0101-0001"
        )
        return

    prefix = match.group("prefix")
    if prefix not in ALLOWED_PREFIXES:
        errors.append(f"Unknown entry_id prefix: {prefix}")

    compact_topic = match.group("topic")
    digits = compact_topic[1:]
    topic_id = "T" + ".".join(digits[index : index + 2] for index in range(0, len(digits), 2))
    if topic_id not in taxonomy_ids:
        errors.append(f"entry_id topic does not exist in taxonomy: {topic_id}")

    primary_topic_id = data.get("primary_topic_id")
    if isinstance(primary_topic_id, str) and primary_topic_id and topic_id != primary_topic_id:
        errors.append(
            f"entry_id topic {topic_id} does not match primary_topic_id {primary_topic_id}"
        )


def validate_basic_metadata(data: dict[str, Any], errors: list[str]) -> None:
    require_fields(data, REQUIRED_METADATA, errors)
    require_fields(data, REQUIRED_EVIDENCE_FIELDS, errors)
    require_fields(data, REQUIRED_SAFETY_FIELDS, errors)

    if data.get("schema_version") not in {None, "", "v0.1"}:
        errors.append(f"Unsupported schema_version: {data.get('schema_version')}")

    slug = data.get("entry_slug")
    if isinstance(slug, str) and slug and not ENTRY_SLUG_PATTERN.fullmatch(slug):
        errors.append("entry_slug must use lowercase letters, numbers, hyphens, or underscores")

    content_type = data.get("content_type")
    if content_type not in {None, ""} and content_type not in ALLOWED_CONTENT_TYPES:
        errors.append(f"Unknown content_type: {content_type}")

    information_layer = data.get("information_layer")
    if information_layer not in {None, ""} and information_layer not in ALLOWED_INFORMATION_LAYERS:
        errors.append(f"Unknown information_layer: {information_layer}")

    status = data.get("status")
    if status not in {None, ""} and status not in ALLOWED_STATUSES:
        errors.append(f"Unknown status: {status}")

    evidence_level = data.get("evidence_level")
    if evidence_level not in {None, ""} and evidence_level not in ALLOWED_EVIDENCE_LEVELS:
        errors.append(f"Unknown evidence_level: {evidence_level}")

    version = data.get("version")
    if isinstance(version, str) and version and not VERSION_PATTERN.fullmatch(version):
        errors.append(f"Invalid version format: {version}")

    created_date = data.get("created_date")
    if isinstance(created_date, str) and created_date:
        try:
            date.fromisoformat(created_date)
        except ValueError:
            errors.append(f"created_date must use YYYY-MM-DD: {created_date}")

    for field in ("allowed_use", "disallowed_use"):
        if field in data and not is_missing(data[field]):
            ensure_list(data, field, errors)


def validate_topics(
    data: dict[str, Any], taxonomy_ids: set[str], errors: list[str]
) -> None:
    primary_topic_id = data.get("primary_topic_id")
    topic_ids = ensure_list(data, "topic_ids", errors) if "topic_ids" in data else []

    if isinstance(primary_topic_id, str) and primary_topic_id:
        if not TOPIC_ID_PATTERN.fullmatch(primary_topic_id):
            errors.append(f"Invalid primary_topic_id format: {primary_topic_id}")
        elif primary_topic_id not in taxonomy_ids:
            errors.append(f"primary_topic_id not found in taxonomy: {primary_topic_id}")

    seen: set[str] = set()
    for topic_id in topic_ids:
        if not isinstance(topic_id, str):
            errors.append(f"topic_ids entries must be strings: {topic_id!r}")
            continue
        if not TOPIC_ID_PATTERN.fullmatch(topic_id):
            errors.append(f"Invalid topic_id format: {topic_id}")
        elif topic_id not in taxonomy_ids:
            errors.append(f"topic_id not found in taxonomy: {topic_id}")
        if topic_id in seen:
            errors.append(f"Duplicate topic_id: {topic_id}")
        seen.add(topic_id)

    if topic_ids and primary_topic_id != topic_ids[0]:
        errors.append("primary_topic_id must be the first item in topic_ids")

    if any(topic_id == "T10" or str(topic_id).startswith("T10.") for topic_id in topic_ids):
        if data.get("runtime_enabled") is not False:
            errors.append("T10 entries require runtime_enabled: false")
        if data.get("retrieval_enabled") is not False:
            errors.append("T10 entries require retrieval_enabled: false")


def validate_source_types(
    data: dict[str, Any], errors: list[str], warnings: list[str]
) -> None:
    if "source_type" not in data or is_missing(data.get("source_type")):
        return
    source_types = ensure_list(data, "source_type", errors)
    seen: set[str] = set()
    for source_type in source_types:
        if not isinstance(source_type, str):
            errors.append(f"source_type entries must be strings: {source_type!r}")
            continue
        if source_type in seen:
            errors.append(f"Duplicate source_type: {source_type}")
            continue
        seen.add(source_type)

        if source_type in STANDARD_SOURCE_TYPES or source_type in KEPT_ALIGNMENT_SOURCE_TYPES:
            continue
        if source_type in SOURCE_TYPE_ALIASES:
            canonical = SOURCE_TYPE_ALIASES[source_type]
            warnings.append(f'Normalize source_type "{source_type}" to "{canonical}"')
            continue
        if source_type in DEPRECATED_SOURCE_TYPES:
            replacement = DEPRECATED_SOURCE_TYPES[source_type]
            message = f'Deprecated source_type "{source_type}"'
            if replacement:
                message += f'; use "{replacement}"'
            warnings.append(message)
            continue
        if source_type in MIGRATION_WARNING_SOURCE_TYPES:
            warnings.append(
                f'source_type "{source_type}" represents verification status; '
                "human source classification is required"
            )
            continue
        errors.append(f"Unknown source_type: {source_type}")


def validate_action_resource(data: dict[str, Any], errors: list[str]) -> None:
    if data.get("information_layer") != "action_resource":
        return
    require_fields(
        data,
        ("resource_type", "recommendation_permission", "commercial_boundary"),
        errors,
    )

    permission = data.get("recommendation_permission")
    if permission not in {None, ""} and permission not in ALLOWED_RECOMMENDATION_PERMISSIONS:
        errors.append(f"Unknown recommendation_permission: {permission}")

    commercial_boundary = data.get("commercial_boundary")
    if commercial_boundary not in {None, "", "zero_commission_v0"}:
        errors.append(
            "Action resources require commercial_boundary: zero_commission_v0 in v0"
        )


def validate_progress_and_viewpoints(data: dict[str, Any], errors: list[str]) -> None:
    if data.get("information_layer") != "progress_and_viewpoints":
        return
    require_fields(data, ("research_stage", "actionability_status"), errors)

    research_stage = data.get("research_stage")
    if research_stage not in {None, ""} and research_stage not in ALLOWED_RESEARCH_STAGES:
        errors.append(f"Unknown research_stage: {research_stage}")

    actionability_status = data.get("actionability_status")
    if (
        actionability_status not in {None, ""}
        and actionability_status not in ALLOWED_ACTIONABILITY_STATUSES
    ):
        errors.append(f"Unknown actionability_status: {actionability_status}")


def validate_nutrition_and_supplements(
    data: dict[str, Any], errors: list[str]
) -> None:
    topic_ids = data.get("topic_ids")
    if not isinstance(topic_ids, list) or not NUTRITION_TOPIC_IDS.intersection(topic_ids):
        return

    if "not_for_personalized_protocol" not in data:
        errors.append(
            "Nutrition and supplement topics require not_for_personalized_protocol"
        )
        return

    is_supplement = "T07.06" in topic_ids or data.get("resource_type") == "supplement"
    if is_supplement and data.get("not_for_personalized_protocol") is not True:
        errors.append("Supplement entries require not_for_personalized_protocol: true")


def validate_item(
    path: Path, taxonomy_ids: set[str]
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if path.suffix.lower() != ".md":
        errors.append("File must use the .md extension")

    text = path.read_text(encoding="utf-8-sig")
    try:
        data, body, parse_errors = parse_frontmatter(text)
    except FrontmatterError as exc:
        return [str(exc)], warnings

    errors.extend(parse_errors)
    if not body:
        errors.append("Missing Markdown body")

    validate_basic_metadata(data, errors)
    validate_entry_id(data, taxonomy_ids, errors)
    validate_topics(data, taxonomy_ids, errors)
    validate_source_types(data, errors, warnings)
    validate_action_resource(data, errors)
    validate_progress_and_viewpoints(data, errors)
    validate_nutrition_and_supplements(data, errors)
    return errors, warnings


def print_result(path: Path, errors: Sequence[str], warnings: Sequence[str]) -> None:
    print(f"File: {path}")
    if warnings:
        print("WARNING:")
        for warning in warnings:
            print(f"- {warning}")
    if errors:
        print("ERROR:")
        for error in errors:
            print(f"- {error}")
    else:
        print("VALID")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate one Congtie Longevity Information Library Markdown entry."
    )
    parser.add_argument("path", type=Path, help="Path to one Markdown knowledge item")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    path = args.path.expanduser()

    if not path.exists():
        print(f"File: {path}")
        print("ERROR:")
        print("- Input file does not exist")
        return 2
    if not path.is_file():
        print(f"File: {path}")
        print("ERROR:")
        print("- Input path is not a file")
        return 2

    try:
        taxonomy_path = locate_taxonomy(repo_root())
        taxonomy_ids = load_taxonomy_ids(taxonomy_path)
        errors, warnings = validate_item(path, taxonomy_ids)
    except (OSError, UnicodeError) as exc:
        print(f"File: {path}")
        print("ERROR:")
        print(f"- Execution error: {exc}")
        return 2

    print_result(path, errors, warnings)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
