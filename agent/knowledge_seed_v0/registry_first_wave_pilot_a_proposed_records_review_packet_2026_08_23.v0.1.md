# Registry First Wave Pilot A Proposed Records Review Packet 2026-08-23 v0.1

- Status: Founder Approved for Version Control / Records Remain Proposed and Not Activated
- Founder reviewer: 蓝耀栋
- Founder review date: 2026-08-24
- Prepared date: 2026-08-23
- Repository anchor: `1a7015d1c0c6cf6c04b3d00747dc4631247b150a`
- Scope: Founder review of four proposed RegistryConcept records only

## 1. Purpose

This packet presents the exact four Pilot A proposed RegistryConcept JSON files for Founder human review. It records their source lineage, effective numeric-ID reservations, deterministic materialization, byte parity, validation results, lifecycle boundaries, and pending decisions.

The files exist in the repository working tree for review but are not committed, active, published, runtime-enabled, or retrieval-enabled.

## 2. Repository Baseline

```text
Repository: /Users/lanyaodong/Documents/congtie-api
Branch: main
HEAD: 1a7015d1c0c6cf6c04b3d00747dc4631247b150a
origin/main: 1a7015d1c0c6cf6c04b3d00747dc4631247b150a
Initial staging: empty
Initial Registry record JSON count: 0
```

## 3. Exact Source Artifact SHAs

| Artifact | SHA-256 |
|---|---|
| First Wave 12 Plan | `8266be330cbb15a9526828410e708924a514e1582585a0db17144ad34b34ea63` |
| Pilot A schema-exact authoring manifest | `951b98de45dbf3de2085041d1e729a2319808858632c97121bd08ab27ce1c757` |
| Pilot A authoring-manifest Founder approval | `bb54866c583de0b1b0c1ca6e445aadbb238fb7936b29d80df2343abf724108af` |
| Numeric-ID allocation ledger | `acb03ba4f87595b12f7ae1a2f2d976454e2ab1d5a8b8bcb588ae3d3265ab172c` |
| Numeric-ID allocation Founder approval | `36e9820e9a08cacc6b5c5652796e9950f617ac88b6a06a4221aaebc9ce9645bc` |
| Registry Schema | `a376b02e8cf50e95392287a8924919e57c6df6e37fa957830d4f1a60d1557aa7` |
| Candidate Ledger | `b97f4b0e0aeaa4fae6e728c561e88019d3c9e0b34ce353c1cc2b27f5cd09bbe5` |
| Migration Ledger | `592408206315e2a404740c0fe5ca1f1ad574d407401d9df9c7f2062a45ad1a56` |
| Permanent Validator | `52ab54488fe8d018d008de3b45a46d16019445c20f36fa0641465c80ef867ff9` |

## 4. Effective Allocation Evidence

The allocation ledger and its exact-SHA Founder approval closeout are both tracked and present in current `HEAD`. The approval closeout cites allocation SHA `acb03ba4f87595b12f7ae1a2f2d976454e2ab1d5a8b8bcb588ae3d3265ab172c` and makes these four permanent, non-semantic, non-reusable reservations effective:

| Candidate | Effective ID | Canonical Path |
|---|---|---|
| `height` | `ME-000018` | `agent/biomarker_measurement_registry/records/ME-000018.height.json` |
| `body_weight` | `ME-000019` | `agent/biomarker_measurement_registry/records/ME-000019.body_weight.json` |
| `creatinine` | `BM-000023` | `agent/biomarker_measurement_registry/records/BM-000023.creatinine.json` |
| `heart_rate` | `ME-000020` | `agent/biomarker_measurement_registry/records/ME-000020.heart_rate.json` |

## 5. Four Record Paths and SHAs

| Record | SHA-256 | Lines |
|---|---|---:|
| `ME-000018.height.json` | `6e03ad4435dafb5205212377f1cfb24568be47104769321ac34bd7aba74ee504` | 274 |
| `ME-000019.body_weight.json` | `1f533cd61110d63585589f2c54faccd4366a83862c59506a73570831d1505bcc` | 268 |
| `BM-000023.creatinine.json` | `fa6b2ad250c6c1f8f2e4df6428970eebd5e6497061533f110dabe99c0549cbab` | 323 |
| `ME-000020.heart_rate.json` | `1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e` | 322 |

## 6. Deterministic Materialization and Editorial Correction

The four records were initially materialized from the exact approved Pilot A authoring manifest SHA `951b98de45dbf3de2085041d1e729a2319808858632c97121bd08ab27ce1c757` by injecting only the effective numeric Registry IDs and controlled creation and last-modified date `2026-08-23`.

During Founder final review, one exact editorial correction was authorized in the Heart Rate wearable Profile limitation: punctuation was added to the phrase “Motion, wear, signal sampling, and artifact handling matter.” This correction does not change medical meaning, source scope, Profile boundaries, evidence, units, mappings, permissions, lifecycle, or runtime status.

The manifest remains the initial materialization authority. The corrected Heart Rate record has one Founder-authorized post-materialization editorial clarification and is not claimed to be byte-identical to the original manifest-derived temporary record. Source access dates remain `2026-08-22`; no other content drift occurred.

## 7. Record Field Summaries

| Record | Namespace | Information Type | Value Type | Lifecycle | Version |
|---|---|---|---|---|---|
| Height | ME | `physiological_measurement` | `number` | `proposed` | `v0.1` |
| Body Weight | ME | `physiological_measurement` | `number` | `proposed` | `v0.1` |
| Creatinine | BM | `laboratory_biomarker` | `number` | `proposed` | `v0.1` |
| Heart Rate | ME | `physiological_measurement` | `number` | `proposed` | `v0.1` |

All governance metadata uses `created_date = last_modified_date = 2026-08-23`, `reviewed_by = []`, `reviewed_date = null`, and `last_source_check_date = 2026-08-22`.

## 8. Profile Summaries

| Record | Initial Profiles | Status |
|---|---|---|
| Height | `height.standing.stadiometer` | proposed |
| Body Weight | `body_weight.scale_measured` | proposed |
| Creatinine | `creatinine.serum_or_plasma.enzymatic` | proposed |
| Heart Rate | `heart_rate.spot_clinical`; `heart_rate.wearable_ppg_time_series_estimate` | proposed |

Manual pulse, self-reported anthropometry, household-scale-specific, Jaffe, resting/sleeping/activity summary, zones, and recovery profiles remain deferred and absent.

## 9. Source and Mapping Summaries

| Record | Sources | Concept Mapping | Profile Mapping | Device Mapping |
|---|---:|---|---|---:|
| Height | 4 | LOINC `8302-2` | none | 0 |
| Body Weight | 4 | LOINC `29463-7` | none | 0 |
| Creatinine | 6 | none | LOINC `2160-0`, `14682-9` | 0 |
| Heart Rate | 4 | LOINC `8867-4` | none | 0 |

Source keys are unique within each record, all key references resolve, and mapping keys are unique. `SRC-NHC-LITERACY-2024` is absent from the Heart Rate record.

## 10. Unit Summaries

| Record | Canonical Unit | Accepted Representation | Conversion Boundary |
|---|---|---|---|
| Height | `cm` | `m`, `[in_i]` | mathematical conversion does not establish protocol/instrument equivalence |
| Body Weight | `kg` | `[lb_av]` | mathematical conversion does not establish scale/protocol equivalence |
| Creatinine | `umol/L` | `mg/dL` | reviewed `88.4` conversion does not establish assay/platform comparability |
| Heart Rate | `/min` | `/min` | `bpm` is display text, not a second unit code |

## 11. Lifecycle and Permission Boundaries

All four RegistryConcept records and all five profiles use lifecycle `proposed`. Every record has empty `use_evidence_claims`, `system_relations`, and `lifecycle_relations`. Every profile has empty `reference_contexts` and `device_mappings`, with `derived_computation = null`.

Height and Body Weight use `action_authorization = none`. Creatinine and Heart Rate use `action_authorization = separately_gated`. No record authorizes diagnosis, treatment, personal targets, risk scoring, or automatic action.

## 12. Materialization Parity and Authorized Delta

Initial temporary materialization directory: `/tmp/congtie-pilot-a-c32-records`.

| Record | Final Relationship to Initial Materialization |
|---|---|
| `ME-000018.height.json` | byte-identical |
| `ME-000019.body_weight.json` | byte-identical |
| `BM-000023.creatinine.json` | byte-identical |
| `ME-000020.heart_rate.json` | one Founder-authorized editorial string replacement |

Initial materialization parity was `4/4 PASS` before Founder review. Final integrity is `3/3 unchanged records PASS` plus `1/1 exact authorized Heart Rate correction PASS`; no other record-body drift was detected.

## 13. Schema Validation Result

```text
JSON syntax: 4/4 PASS
Draft 2020-12 Schema: 4/4 PASS
Permanent Semantic Validator: 4/4 PASS
Cross-record checks: 25/25 PASS
Python: 3.9.6
jsonschema: 4.25.1
Warnings: 0
Errors: 0
```

## 14. Semantic Validator Result

The permanent Registry authoring Validator accepted all four repository copies with Candidate Ledger lineage enabled.

```text
ME-000018.height.json: VALID / exit 0
ME-000019.body_weight.json: VALID / exit 0
BM-000023.creatinine.json: VALID / exit 0
ME-000020.heart_rate.json: VALID / exit 0
Semantic Validator: 4/4 PASS
```

## 15. Cross-Record Result

All required identity, uniqueness, path, namespace, lifecycle, source resolution, mapping, privacy, empty-collection, date, target-boundary, Candidate Ledger, and allocation-ledger checks passed.

```text
Cross-record checks: 25/25 PASS
Height record-specific gate: PASS
Body Weight record-specific gate: PASS
Creatinine record-specific gate: PASS
Heart Rate record-specific gate: PASS
```

## 16. Candidate Ledger Integrity

Candidate Ledger SHA remains `b97f4b0e0aeaa4fae6e728c561e88019d3c9e0b34ce353c1cc2b27f5cd09bbe5`. Core remains 53, First Wave remains 12, and all Candidate Ledger `registry_id` values remain `null`.

## 17. Allocation Ledger Integrity

Allocation Ledger SHA remains `acb03ba4f87595b12f7ae1a2f2d976454e2ab1d5a8b8bcb588ae3d3265ab172c`. The four effective reservations remain unique, namespace-aligned, path-aligned, permanent, non-semantic, and non-reusable.

## 18. Explicit State and Non-Authorizations

```text
Records created = 4
Lifecycle = proposed
Source-verified records = 0
Human-reviewed records = 0
Active records = 0
Runtime-enabled records = 0
Retrieval-enabled records = 0
Published records = 0
User observations = 0
```

File existence does not authorize Agent runtime use. No runtime, retrieval, publication, database, API, loader, index, Observation processing, user-health storage, Service Panel, public threshold, critical value, risk threshold, personal target, diagnosis, treatment, or automatic action is authorized.

## 19. Founder Decision Sheet

| # | Decision | Founder Decision |
|---:|---|---|
| 1 | Approve `ME-000018.height.json` | Approved |
| 2 | Approve `ME-000019.body_weight.json` | Approved |
| 3 | Approve `BM-000023.creatinine.json` | Approved |
| 4 | Approve corrected `ME-000020.heart_rate.json` | Approved |
| 5 | Authorize controlled commit/push of the exact four records and approval closeout | Approved |

Founder decisions approved: `5/5`. Founder pending decisions: `0`. Accidental approvals: `0`.

## 20. Next Lifecycle Gate

The record lifecycle remains `proposed`, and every Profile lifecycle remains `proposed`. Founder approval for version control does not create `source_verified`, `human_reviewed`, or `active` lifecycle status and does not authorize runtime or retrieval.

A later source-verification Gate must separately review the Heart Rate spot-clinical method authority, wearable time-series Observation granularity, source completeness and freshness, and any future Profile or claim additions. No lifecycle promotion follows automatically.
