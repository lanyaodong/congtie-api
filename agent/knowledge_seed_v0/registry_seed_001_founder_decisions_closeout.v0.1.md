# Registry Seed 001 Founder Decisions Closeout v0.1

Version: v0.1
Status: Founder Approved / Schema and Record Production Still Gated
Decision date: 2026-08-22
Owner: Congtie Founder / Congtie Agent Team

## 1. Purpose

This closeout records Founder decisions after the C22 asset reconciliation and C23 Founder review packet. It authorizes draft machine-readable schema and candidate/migration ledgers. It does not authorize active Registry records, numeric ID activation, production storage, runtime use, Service Panels, laboratory integration, or user-health data processing.

## 2. Source Documents and SHAs

| Source | SHA-256 | Role |
| --- | --- | --- |
| `registry_seed_001_asset_reconciliation_and_seed_definition.v0.1.md` | `4eac755441d96bd3113ceda302f049ddfa6d405eaa96989a7a59744ac80930cc` | C22 architecture and asset baseline |
| `registry_seed_001_founder_review_packet.v0.1.md` | `59e933814d1357a625a7d4ed6403ade4210cd3becc20f47d99e48f6b43743817` | C23 candidate, migration, and ID-freeze audit |
| `whole_body_health_information_model_and_biomarker_measurement_registry_mvp_spec.v0.1.md` | `ab887455d878cdc04f3baf596d775be0aef188da19df789eec4f3e8a2339f317` | Canonical conceptual Registry governance |

C22 and C23 remain unchanged review-history inputs. Their prior 48- and 51-concept positions are not rewritten.

## 3. Architecture Decision

Founder decision: `APPROVED WITH C23/C24 REFINEMENTS`.

```text
Knowledge Entry != Registry Concept != User Observation != Service Panel
```

The Registry is a public canonical definition layer. The User Health Information Library is a private, permission-gated user layer.

## 4. Legacy Migration Decision

The approximately 120-item legacy directory changes from `reference_only` to concept-level `partially_migrate`.

```text
semantic inventory
-> normalize aliases
-> split compound rows
-> deduplicate
-> retain useful metadata
-> migrate canonical meaning
-> supersede old representation when appropriate
```

Legacy assets are neither imported mechanically nor discarded. Legacy `optimal_range`, fixed measurement frequency, single-system ownership, and worst-marker semantics are not migrated as authority.

## 5. Final Core Candidate Direction

Founder direction: `53 Core candidate concepts`.

```text
48 C22 candidates - 6 moved from Core + 11 additions = 53
```

This is a candidate scope, not a quota. Concept-boundary correctness takes priority over preserving 53 if later source/schema review requires a justified split or merge.

Expected namespace counts before any justified split/merge:

| Namespace | Count |
| --- | ---: |
| BM | 29 |
| ME | 20 |
| SC | 4 |
| QS | 0 |
| Total | 53 |

## 6. GREEN / YELLOW / RED Policy

- `GREEN`: suitable for Core production after normal source/profile review.
- `YELLOW`: remains Core but has a named preproduction issue that must be resolved.
- `RED`: not suitable for Core at this stage; it remains valid for Extended or device/protocol-specific modeling.

From the original C22 set, 21 GREEN and 21 YELLOW candidates remain. Six RED candidates move out of Core.

## 7. Eleven Additions

Founder-approved additions:

1. Hematocrit / 红细胞压积
2. Red Blood Cell Count / 红细胞计数
3. Urea / BUN construct / 尿素或尿素氮
4. Alkaline Phosphatase / 碱性磷酸酶
5. Total Bilirubin / 总胆红素
6. Sodium / 钠
7. Potassium / 钾
8. Non-HDL Cholesterol / 非高密度脂蛋白胆固醇
9. Time in Bed / 卧床时间
10. Height / 身高
11. Step Count / 步数

Hematocrit, RBC count, ALP, total bilirubin, sodium, potassium, height, and non-HDL-C enter as GREEN planning candidates. Urea/BUN, time in bed, and step count enter as YELLOW planning candidates.

## 8. Namespace Policy

- `BM`: laboratory or molecular biomarker concept.
- `ME`: non-laboratory measurement concept family, including anthropometric, physiological, functional/performance, sleep/behavioral interval, device-measured, and device-estimated measurements of an underlying construct.
- `SC`: formula-derived metric, derived index, or composite score.
- `QS`: validated questionnaire or scale.

Core Seed contains no QS solely to demonstrate namespace coverage.

## 9. Numeric ID Freeze Policy

Founder selects `Option B`: freeze namespace semantics only. C22 numeric IDs remain historical review coordinates.

Candidate planning uses a unique human-readable `candidate_key` and `registry_id: null`. Final IDs are assigned only at a future Founder Gate after schema, semantic deduplication, and record boundaries are approved. IDs must not encode T03 system ownership.

## 10. ME Namespace Clarification

An estimate of an ME construct does not automatically become SC. A wearable-estimated heart rate, sleep total time, or step count can remain an ME profile when it estimates the underlying construct. BMI, eGFR, sleep efficiency, and non-HDL-C remain SC because they are explicitly derived formula/index concepts.

## 11. Concept / Profile Architecture

The machine-readable model uses:

```text
Registry Concept
-> Measurement / Method Profile
-> External or Device Metric Mapping
-> Use-Context / Evidence Claim
-> Body-System Relation
```

The concept defines the public construct. Profiles express specimen, modality, measurement nature, method, instrument/device, formula, algorithm/version, unit handling, protocol context, comparability, reference context, and limitations.

Examples:

- Body Fat Percentage: DXA, BIA, and consumer-scale estimate profiles.
- LDL-C: direct assay and calculated equation profiles.
- Sleep Total Time: user-reported, diary, PSG-derived, and wearable-estimated profiles.

## 12. Mapping Layers

External code mappings support LOINC, UCUM, China standards, laboratory/partner local codes, and other reviewed systems. Mapping existence does not prove clinical validity.

Device metric mappings preserve vendor, device family/model, platform, original metric name, firmware/software/algorithm version, measurement nature, mapped candidate key, and limitations. A proprietary score does not become a canonical Core concept merely because it is common.

## 13. Field-Tier Direction

Required concept fields include candidate identity, namespace, names, information/construct type, construct definition, allowed measurement natures, value type, canonical-unit policy, definition sources, limitations, permission boundary, target-support metadata, and lifecycle status.

Profile-, use-, and lifecycle-dependent fields remain conditional. A `proposed` candidate may contain pending fields; source-verified/human-reviewed/active stages progressively require verified sources, use context, method status, evidence scope, system relations where applicable, and Agent permissions.

## 14. Migration Ledger Decision

Project migration workflow is separate from durable Registry lifecycle.

Migration-ledger fields include source asset/record, legacy code/label, semantic cluster, candidate mapping, migration status, split/merge decision, note, and unresolved issue.

Durable Registry lifecycle may retain source provenance, `supersedes`, `superseded_by`, and `duplicate_of`. Internal extraction workflow does not become mandatory permanent record data.

## 15. Reference / Threshold Decision

The public Registry keeps separate structures for:

1. laboratory-reported reference interval metadata;
2. population reference interval;
3. guideline/clinical decision limit;
4. risk-associated threshold;
5. critical/alert value.

An imported observation must preserve its original laboratory interval and flag. A Registry context must not overwrite it.

## 16. Personalized Target Placement

The public Registry stores only `personalized_target_support` capability/prerequisite metadata, such as `supported`, `context_dependent`, `not_applicable`, or `requires_governance`.

Actual user target value, rationale, effective dates, history, and action linkage belong in the User Health Information Library / Personalized Longevity Protocol layer.

## 17. Six-System Relation Governance

System mapping uses many-to-many relation records. `biological_relationship` and `product_grouping` are distinct. Each relation supports system ID, rationale, source, evidence scope, and confidence.

Product primary grouping is optional UI/product organization. It is not biological ownership, diagnosis, a system score, measurement frequency, intervention, or action authorization.

## 18. First-Wave 12 Proposal

The Founder-approved proposal for future record-boundary review is:

1. `apolipoprotein_b`
2. `lipoprotein_a`
3. `hba1c`
4. `creatinine`
5. `estimated_glomerular_filtration_rate`
6. `systolic_blood_pressure`
7. `diastolic_blood_pressure`
8. `height`
9. `body_weight`
10. `heart_rate`
11. `sleep_total_time`
12. `body_mass_index`

These concepts test laboratory analytes, method/unit complexity, formula lineage, physiology, anthropometry, sleep profiles, and concept/profile separation. No Registry records are created by approving this proposal.

## 19. Production Readiness

Current decision: `READY WITH CONDITIONS` for machine-readable schema and planning ledgers only.

Before first-record production, Founder must review the machine-readable schema, 53-item Core ledger, migration ledger, unresolved YELLOW issues, and the First-Wave 12 record boundaries.

## 20. Explicit Non-Authorizations

This closeout does not authorize:

- active Registry records or numeric IDs;
- production database, API, runtime, or indexing;
- Observation/User Health Event schema or personal data storage;
- user consent or cross-border processing implementation;
- Service Panel or critical-result workflow;
- laboratory/provider integration or confirmed partnership;
- report ingestion, diagnosis, prescription, system scoring, or protocol action.

## 21. Next Founder Gate

Founder + ChatGPT review:

1. machine-readable Registry schema;
2. 53-item Core Candidate Ledger;
3. unresolved YELLOW concept boundaries;
4. complete migration coverage and needs-review items;
5. First-Wave 12 record boundaries.

Only a later explicit task may create Registry records or assign numeric Registry IDs.
