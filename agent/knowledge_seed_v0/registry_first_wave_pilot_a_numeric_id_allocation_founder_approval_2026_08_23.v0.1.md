# Registry First Wave Pilot A Numeric-ID Allocation Founder Approval 2026-08-23 v0.1

- Status: Founder Approved for Effective Numeric-ID Reservation upon Controlled Commit / Registry Record Creation Not Authorized
- Founder: 蓝耀栋
- Approval date: 2026-08-23
- Repository baseline: `main` at `9fdd4a16b8430e3553ff53d08a55ab4c05edea47`

## 1. Purpose

This closeout records Founder approval of the exact Pilot A numeric-ID allocation proposal. The effectiveness event is the controlled Git commit that contains both the byte-identical allocation ledger and this exact-SHA approval closeout. Registry record creation remains separately gated.

## 2. Repository Baseline

The approved allocation review was completed against repository and `origin/main` anchor:

```text
9fdd4a16b8430e3553ff53d08a55ab4c05edea47
```

Staging was empty before the controlled C31 commit sequence.

## 3. Exact Approved Allocation Manifest

```text
Path:
agent/biomarker_measurement_registry/id_allocations/registry_first_wave_pilot_a_numeric_id_allocation_2026_08_23.v0.1.json

SHA-256:
acb03ba4f87595b12f7ae1a2f2d976454e2ab1d5a8b8bcb588ae3d3265ab172c
```

The approval applies only to these exact reviewed bytes.

## 4. Source Integrity Anchors

| Artifact | SHA-256 |
|---|---|
| Pilot A schema-exact authoring manifest | `951b98de45dbf3de2085041d1e729a2319808858632c97121bd08ab27ce1c757` |
| Candidate Ledger | `b97f4b0e0aeaa4fae6e728c561e88019d3c9e0b34ce353c1cc2b27f5cd09bbe5` |
| Registry Schema | `a376b02e8cf50e95392287a8924919e57c6df6e37fa957830d4f1a60d1557aa7` |
| Permanent authoring Validator | `52ab54488fe8d018d008de3b45a46d16019445c20f36fa0641465c80ef867ff9` |

## 5. Storage Convention

The canonical operational root is `agent/biomarker_measurement_registry/`. Registry records use the flat `agent/biomarker_measurement_registry/records/` directory and filename pattern `<REGISTRY_ID>.<candidate_key>.json`. Each file contains one `RegistryConcept`; Measurement Profiles remain embedded in `RegistryConcept.profiles[]`.

Allocation ledgers are stored separately under `agent/biomarker_measurement_registry/id_allocations/`. Record filenames contain no version, lifecycle, Pilot, body-system, priority, or product-grouping suffix.

## 6. ID Inventory Result

The pre-allocation audit found no formal occupied Registry IDs and no prior effective reservations. Candidate Ledger legacy review coordinates are collision-reserved but are not formal Registry IDs.

| Namespace | Formal Occupied | Prior Effective Reserved | Legacy Collision-Reserved Maximum | Next Allocatable Before Pilot A |
|---|---:|---:|---:|---:|
| BM | 0 | 0 | 22 | 23 |
| ME | 0 | 0 | 17 | 18 |
| SC | 0 | 0 | 3 | 4 |
| QS | 0 | 0 | 0 | 1 |

The four approved IDs are unique, namespace-aligned, monotonic, outside the collision-reserved legacy-coordinate sets, and bound to unique intended paths.

## 7. Four Approved Effective Reservations

| Candidate | Namespace | Effective Reserved ID after Commit | Intended Record Path |
|---|---|---|---|
| `height` | ME | `ME-000018` | `agent/biomarker_measurement_registry/records/ME-000018.height.json` |
| `body_weight` | ME | `ME-000019` | `agent/biomarker_measurement_registry/records/ME-000019.body_weight.json` |
| `creatinine` | BM | `BM-000023` | `agent/biomarker_measurement_registry/records/BM-000023.creatinine.json` |
| `heart_rate` | ME | `ME-000020` | `agent/biomarker_measurement_registry/records/ME-000020.heart_rate.json` |

These reservations are permanent, non-semantic, and non-reusable after the controlled effectiveness commit. They do not encode body system, Pilot, priority, dependency, clinical meaning, lifecycle, or product grouping.

## 8. Dry-Run Validation Result

Four temporary proposed records were expanded outside the repository using the approved IDs and controlled date `2026-08-23`. Validation used Python 3.9, `jsonschema[format]==4.25.1`, the final Registry Schema, permanent semantic Validator, and Candidate Ledger.

```text
ME-000018.height.json: Schema PASS / Semantic Validator PASS
ME-000019.body_weight.json: Schema PASS / Semantic Validator PASS
BM-000023.creatinine.json: Schema PASS / Semantic Validator PASS
ME-000020.heart_rate.json: Schema PASS / Semantic Validator PASS

Total: 4/4
Warnings: 0
Errors: 0
Repository record JSON files created: 0
```

## 9. Effectiveness Event

Founder approves the exact SHA-identified Pilot A numeric-ID allocation proposal. The controlled Git commit containing both the exact allocation ledger and this approval closeout makes `ME-000018`, `ME-000019`, `BM-000023`, and `ME-000020` effective, permanent, non-semantic and non-reusable Registry ID reservations for Height, Body Weight, Creatinine and Heart Rate respectively.

The reservation state after that commit is:

```text
Effective numeric-ID reservations = 4
Registry record files = 0
Active Registry records = 0
Candidate Ledger registry_id values remain null
```

## 10. Historical Embedded-State Explanation

The committed allocation proposal retains its reviewed pre-commit `Draft`, `effective_reserved_id_count: 0`, and `effective_reservation: false` fields. Those fields preserve the reviewed proposal bytes. After the controlled commit, this Founder approval closeout is the authoritative effectiveness event for the four exact reservations.

## 11. Candidate Ledger Boundary

Candidate planning and formal allocation remain separate governance layers. The Candidate Ledger remains byte-identical, its Core count remains 53, its First Wave count remains 12, and all `registry_id` values remain `null`. The approved reservations are represented only by the committed allocation ledger plus this exact-SHA approval closeout.

## 12. Explicit Non-Authorizations

This approval does not authorize creation of the four intended Registry record files, standalone MeasurementProfile files, profile/claim/system-relation/reference-context records, lifecycle above `proposed`, Candidate Ledger mutation, Pilot B/C allocation, runtime, retrieval, database, API, loader, index, Observation processing, user-health storage, Service Panel, publication, public thresholds, personal targets, diagnosis, treatment, or automatic action.

## 13. Next Founder Gate

The next task may propose creation of exactly the four Pilot A Registry records at their approved paths with `lifecycle_status: proposed`. Record bytes must be generated from the exact approved Pilot A authoring manifest and independently validated. No `source_verified`, `human_reviewed`, `active`, runtime, or retrieval transition is automatic.
