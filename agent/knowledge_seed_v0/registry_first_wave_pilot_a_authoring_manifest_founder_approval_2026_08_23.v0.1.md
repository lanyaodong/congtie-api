# Registry First Wave Pilot A Authoring Manifest Founder Approval 2026-08-23 v0.1

- Status: Founder Approved for Numeric-ID Allocation Planning / Record Creation Not Authorized
- Founder: 蓝耀栋
- Approval date: 2026-08-23
- Repository anchor: `9fdd4a16b8430e3553ff53d08a55ab4c05edea47`

## 1. Purpose

This closeout records Founder approval of the exact Pilot A schema-exact authoring manifest and authorizes numeric-ID allocation planning only. It preserves the separation between approved authoring blueprints, proposed ID reservations, effective reservations, and Registry record creation.

## 2. Exact Approved Baseline

| Artifact | Path | SHA-256 |
|---|---|---|
| First Wave 12 Plan | `agent/knowledge_seed_v0/registry_first_wave_12_record_boundary_and_source_verification_plan.v0.1.md` | `8266be330cbb15a9526828410e708924a514e1582585a0db17144ad34b34ea63` |
| Pilot A schema-exact authoring manifest | `agent/knowledge_seed_v0/registry_first_wave_pilot_a_proposed_record_authoring_manifest.v0.1.md` | `951b98de45dbf3de2085041d1e729a2319808858632c97121bd08ab27ce1c757` |
| Registry Schema | `schemas/biomarker_measurement_registry_schema_v0.1.json` | `a376b02e8cf50e95392287a8924919e57c6df6e37fa957830d4f1a60d1557aa7` |
| Candidate Ledger | `agent/knowledge_seed_v0/registry_seed_001_candidate_ledger.v0.1.json` | `b97f4b0e0aeaa4fae6e728c561e88019d3c9e0b34ce353c1cc2b27f5cd09bbe5` |
| Migration Ledger | `agent/knowledge_seed_v0/registry_seed_001_migration_ledger.v0.1.json` | `592408206315e2a404740c0fe5ca1f1ad574d407401d9df9c7f2062a45ad1a56` |
| Permanent Validator | `agent/knowledge_seed_v0/scripts/validate_biomarker_measurement_registry.py` | `52ab54488fe8d018d008de3b45a46d16019445c20f36fa0641465c80ef867ff9` |

Founder approval applies to the exact Pilot A manifest SHA above. Its embedded Draft / Founder Review Pending status is retained to preserve the external verification chain; this closeout is the authoritative approval record.

## 3. Founder Decisions 1-9

1. Approve the schema-exact Height blueprint.
2. Approve the schema-exact Body Weight blueprint.
3. Approve the schema-exact Creatinine blueprint.
4. Approve the schema-exact Heart Rate blueprint.
5. Exclude manual pulse count from the initial Heart Rate profile set.
6. Exclude `SRC-NHC-LITERACY-2024` from the initial Heart Rate record source pool.
7. Approve the concept-level and profile-level LOINC mapping plan.
8. Approve a separate, immutable numeric-ID allocation-ledger contract.
9. Authorize preparation of a numeric-ID allocation proposal.

Founder decisions approved: `9/9`.

## 4. Four Blueprint Approval

The approved Pilot A set is exactly:

| Candidate | Namespace | Approved Initial Profile Scope |
|---|---|---|
| `height` | ME | `height.standing.stadiometer` |
| `body_weight` | ME | `body_weight.scale_measured` |
| `creatinine` | BM | `creatinine.serum_or_plasma.enzymatic` |
| `heart_rate` | ME | `heart_rate.spot_clinical`; `heart_rate.wearable_ppg_time_series_estimate` |

Each future first record remains limited to `lifecycle_status: proposed`. No separate profile file is authorized.

## 5. Source, Mapping, and Unit Approval

The exact Pilot A source pools, source roles, definition/profile source keys, LOINC mapping scopes, UCUM unit objects, accepted representations, conversion boundaries, protocol contexts, interpretation limitations, and Agent permission arrays in the approved Manifest are accepted for controlled allocation planning.

This approval does not elevate source review into a concept lifecycle transition. It does not authorize public thresholds, use-evidence claims, system relations, vendor device mappings, user-specific targets, or action authorization.

## 6. Heart Rate Exclusions

The initial Heart Rate record plan excludes manual pulse count and excludes `SRC-NHC-LITERACY-2024` from its source pool. Resting, sleeping, activity/exercise summaries, zones, and recovery remain deferred. Wearable PPG remains an estimate and is not treated as ECG.

## 7. Founder-Approved Storage Convention

The canonical operational root is `agent/biomarker_measurement_registry/`. Registry records, if separately authorized later, use the flat directory `agent/biomarker_measurement_registry/records/` and filename pattern `<REGISTRY_ID>.<candidate_key>.json`. One RegistryConcept is stored per JSON file and profiles remain embedded in `RegistryConcept.profiles[]`.

Allocation ledgers use `agent/biomarker_measurement_registry/id_allocations/`. Version, lifecycle, namespace subdirectories, body-system grouping, and Pilot labels do not enter record filenames.

## 8. Independent Dry-Run Result

Four temporary records were expanded outside the repository at `/tmp/congtie-pilot-a-c30-1-dry-run` by injecting only the proposed numeric ID and controlled creation date `2026-08-23` into the exact approved Manifest content.

```text
ME-000018.height.json: Schema PASS / Semantic Validator PASS
ME-000019.body_weight.json: Schema PASS / Semantic Validator PASS
BM-000023.creatinine.json: Schema PASS / Semantic Validator PASS
ME-000020.heart_rate.json: Schema PASS / Semantic Validator PASS

Total: 4/4
Errors: 0
Warnings: 0
Repository record files created: 0
```

Validation used Python 3.9, `jsonschema[format]==4.25.1`, the final Registry Schema, the permanent Registry authoring Validator, and the final Candidate Ledger.

## 9. Numeric-ID Option B

Option B remains binding:

```text
approved boundary and exact authoring manifest
-> proposed numeric-ID allocation manifest
-> Founder approval of the exact allocation-manifest SHA
-> controlled Git commit makes reservations effective
-> separately authorized proposed-record creation
```

IDs are namespace-level, monotonic, non-semantic, and never reused. They do not encode body system, Pilot, priority, dependency, clinical meaning, lifecycle, or product grouping.

## 10. Legacy-Coordinate Collision Rule

Every non-null Candidate Ledger `legacy_review_coordinate` matching `^(BM|ME|SC|QS)-[0-9]{6}$` is collision-reserved. These coordinates are not formal Registry IDs, are not active reservations, and gain no Registry authority. Their literal strings must nevertheless never be reused as formal Registry IDs, preventing ambiguity in documents, knowledge graphs, and the audit chain.

The current collision-reserved maxima are BM 22, ME 17, SC 3, and QS 0. Formal occupied IDs and prior effective reservations are both zero.

## 11. Allocation Status Boundary

The current allocation proposal may contain these non-effective proposed reservations and intended paths:

| Candidate | Proposed ID | Intended Record Path |
|---|---|---|
| `height` | `ME-000018` | `agent/biomarker_measurement_registry/records/ME-000018.height.json` |
| `body_weight` | `ME-000019` | `agent/biomarker_measurement_registry/records/ME-000019.body_weight.json` |
| `creatinine` | `BM-000023` | `agent/biomarker_measurement_registry/records/BM-000023.creatinine.json` |
| `heart_rate` | `ME-000020` | `agent/biomarker_measurement_registry/records/ME-000020.heart_rate.json` |

```text
Proposed IDs = 4
Effective reservations = 0
Repository Registry records = 0
Candidate Ledger modified = false
```

## 12. Approval Language

Founder approves the exact SHA-identified Pilot A schema-exact authoring manifest. Height, Body Weight, Creatinine and Heart Rate blueprints, their initial Profile scopes, source pools, LOINC mappings, UCUM units, protocol contexts, interpretation boundaries and Agent permission boundaries are approved for controlled numeric-ID allocation planning. This approval does not authorize Registry record creation or make any proposed ID reservation effective.

## 13. Explicit Non-Authorizations

This approval does not authorize an effective numeric-ID reservation, Candidate Ledger mutation, Registry or profile record creation, lifecycle above `proposed`, public Schema publication, runtime, retrieval, database, API, loader, index, Observation processing, user-health storage, Service Panel, personal target, diagnosis, treatment, or automatic action.

## 14. Next Founder Gate

Founder + ChatGPT reviews the exact allocation proposal, ID inventory, intended record paths, collision checks, dry-run validation, and allocation-manifest SHA. Only Founder approval of that exact SHA plus a controlled Git commit can make the four reservations effective. Record creation remains a separate later authorization.
