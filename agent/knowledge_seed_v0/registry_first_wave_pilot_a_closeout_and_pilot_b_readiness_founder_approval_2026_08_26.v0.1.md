# Registry First Wave Pilot A Closeout and Pilot B Readiness Founder Approval 2026-08-26 v0.1

Status: Founder Approved for Version Control / Pilot A Bounded Source-Verification Closed / Pilot B Readiness Baseline Approved / Pilot B Manifest, Numeric IDs and Records Not Authorized

Founder: 蓝耀栋

Approval date: 2026-08-26

## 1. Purpose

This closeout records Founder approval of the exact SHA-identified Pilot A source-verification closeout and Pilot B read-only readiness audit. It preserves both reviewed C45 documents byte-identically and serves as the authoritative approval record for their exact reviewed bytes.

> Founder approves the exact SHA-identified Pilot A source-verification closeout and Pilot B read-only readiness audit for version control. Pilot A's approved bounded source-verification scope is closed in Git, with Height, Body Weight and Creatinine RegistryConcepts and their initial Profiles at `source_verified`, while the Heart Rate RegistryConcept and spot Profile remain `proposed` and only `heart_rate.wearable_ppg_time_series_estimate` is `source_verified`. Pilot B approval establishes a readiness and future-authoring baseline only. It creates no Pilot B authoring manifest, numeric-ID allocation, Registry record, lifecycle transition, claim, threshold, Observation, runtime or retrieval behavior.

## 2. Repository Baseline

```text
Repository: /Users/lanyaodong/Documents/congtie-api
Branch: main
Initial HEAD: 1560cd562b8896e420f296066a6115029b37cefd
Initial origin/main: 1560cd562b8896e420f296066a6115029b37cefd
Approval date: 2026-08-26
Initial staging: empty
```

The C46 baseline, exact artifact SHA gate, and C44 history gate passed before this closeout was created.

## 3. Exact Pilot A Closeout

```text
Path:
agent/knowledge_seed_v0/registry_first_wave_pilot_a_source_verification_closeout_2026_08_25.v0.1.md

SHA-256:
0155c43e725430dc399566f423d3b1767b036868f539c359044124d23e69ed5c

Lines:
263
```

The document retains its reviewed `Draft / Founder Review Pending` status and three pending decision entries. Those historical fields are not rewritten because approval applies to the exact bytes above.

## 4. Exact Pilot B Audit

```text
Path:
agent/knowledge_seed_v0/registry_first_wave_pilot_b_read_only_readiness_audit_2026_08_25.v0.1.md

SHA-256:
03da66dd3d8ad62e985f88c0d2f917cc52a341354dc7c13e5cf37286a5bb9bda

Lines:
455
```

The document retains its reviewed `Draft / Founder Review Pending` status and ten pending decision entries. This closeout records the final decisions without modifying that audit.

## 5. C44 Git Anchor and History

The approved predecessor anchor is:

```text
1560cd562b8896e420f296066a6115029b37cefd
```

| Commit | Parent | Message | Exact scope |
| --- | --- | --- | --- |
| `6a4b3d70919cb1b0b356379558ca669070138176` | `bdbcbeb766101755beaf152c09bb4ef72f6b1937` | `docs: approve Heart Rate S3 plan and authorize execution` | C42 planning packet and C43 execution authorization |
| `42203f8e5d0b3d0c6562b96f2d065d939956e096` | `6a4b3d70919cb1b0b356379558ca669070138176` | `feat: source-verify wearable PPG Heart Rate Profile` | Heart Rate record only |
| `1560cd562b8896e420f296066a6115029b37cefd` | `42203f8e5d0b3d0c6562b96f2d065d939956e096` | `docs: approve Heart Rate source transition S3` | S3 review packet and final Founder approval |

The messages, order, parents, and exact file manifests were rechecked at the C46 baseline.

## 6. Pilot A Founder Decisions

| Decision | Approved result | Founder Decision |
| --- | --- | --- |
| A1 | Exact Pilot A bounded source-verification closeout state | Approved |
| A2 | Final Heart Rate mixed-lifecycle wording | Approved |
| A3 | Controlled versioning of the exact Pilot A closeout | Approved |

```text
Pilot A decisions approved = 3/3
Pilot A pending decisions in this closeout = 0
```

## 7. Pilot A Lifecycle Matrix

| RegistryConcept | Concept lifecycle | Initial Profile | Profile lifecycle |
| --- | --- | --- | --- |
| Height | `source_verified` | `height.standing.stadiometer` | `source_verified` |
| Body Weight | `source_verified` | `body_weight.scale_measured` | `source_verified` |
| Creatinine | `source_verified` | `creatinine.serum_or_plasma.enzymatic` | `source_verified` |
| Heart Rate | `proposed` | `heart_rate.spot_clinical` | `proposed` |
| Heart Rate | `proposed` | `heart_rate.wearable_ppg_time_series_estimate` | `source_verified` |

## 8. Pilot A Source-Verified Counts

```text
Registry records = 4
Source-verified RegistryConcepts = 3
Source-verified Profiles = 4
Human-reviewed lifecycle records = 0
Active records = 0
```

These counts are derived from the four canonical record JSON files.

## 9. Heart Rate Critical Mixed-Lifecycle Wording

The authoritative wording is:

```text
Heart Rate RegistryConcept = proposed
heart_rate.spot_clinical = proposed
heart_rate.wearable_ppg_time_series_estimate = source_verified
```

The statements `Heart Rate is source_verified`, `All Pilot A records are source_verified`, and `All Pilot A Profiles are source_verified` are prohibited. A verified child Profile does not promote its parent or sibling.

## 10. Pilot A Completed Scope

Pilot A completed the approved bounded source-verification sequence for Height, Body Weight, Creatinine, and the wearable PPG Heart Rate Profile. This includes the NIDDK Creatinine conversion-source prerequisite and Permanent Validator mixed-Profile lifecycle hardening.

The four effective numeric-ID reservations remain permanent, non-semantic, and non-reusable:

```text
ME-000018 height
ME-000019 body_weight
BM-000023 creatinine
ME-000020 heart_rate
```

## 11. Pilot A Deferred Scope

Deferred scope remains outside this approval: self-reported Height and Body Weight; pediatric interpretation; Creatinine Jaffe and other assay/platform Profiles; Heart Rate spot-method source resolution; resting, sleeping, activity, daily, zone, recovery, ECG, and raw-waveform boundaries; human review; active lifecycle; claims; reference contexts; thresholds; system relations; device mappings; and personal targets.

Deferred work is not implicitly authorized by closeout approval.

## 12. Pilot A Runtime and User-Data Boundary

```text
Runtime-enabled records = 0
Retrieval-enabled records = 0
Published records = 0
User observations = 0
Observation storage = not implemented
```

Git versioning and source verification do not authorize product loading, ranking, retrieval, publication, Observation processing, or user-health storage.

## 13. Pilot B Founder Decisions

| Decision | Approved result | Founder Decision |
| --- | --- | --- |
| B1 | Exact four-candidate Pilot B set | Approved |
| B2 | BMI one SC concept, adult v0.1 scope, and derived-computation boundary | Approved |
| B3 | eGFR one SC concept with equation-specific Profiles and CKD-EPI 2021 creatinine first | Approved with age-overlap qualification |
| B4 | Separate SBP and DBP RegistryConcepts with a future shared measurement-event reference | Approved |
| B5 | Office and home upper-arm initial Profiles; ambulatory and cuffless deferred | Approved |
| B6 | Proposed source pools and named source-access and freshness prerequisites | Approved |
| B7 | Jurisdiction-specific threshold/reference separation and no global normal range or personal target | Approved |
| B8 | Option B production order: B1 BMI/eGFR, then B2 SBP/DBP | Approved |
| B9 | Option B numeric-ID timing with no allocation in C45 or C46 | Approved |
| B10 | Later schema-exact Pilot B1 authoring-manifest task | Authorized |

```text
Pilot B decisions approved = 10/10
Pilot B pending decisions in this closeout = 0
```

## 14. Exact Pilot B Candidate Set

| Candidate | Namespace | First Wave | Registry ID | Canonical record |
| --- | --- | --- | --- | --- |
| `body_mass_index` | SC | yes | `null` | none |
| `estimated_glomerular_filtration_rate` | SC | yes | `null` | none |
| `systolic_blood_pressure` | ME | yes | `null` | none |
| `diastolic_blood_pressure` | ME | yes | `null` | none |

No fifth candidate is authorized.

## 15. Pilot B Dependency State

| Pilot B concept | Required Pilot A dependency | Dependency lifecycle |
| --- | --- | --- |
| BMI | Height and Body Weight concepts plus their measured initial Profiles | all `source_verified` |
| eGFR | Creatinine concept and enzymatic serum/plasma Profile | `source_verified` |
| SBP | no Pilot A record dependency | not applicable |
| DBP | no Pilot A record dependency | not applicable |

Dependency readiness is not record-production authorization.

## 16. BMI Boundary Approval

`body_mass_index` is approved as one SC derived-index concept with adult interpretation scope in v0.1. It is distinct from body-fat percentage, body composition, adiposity diagnosis, pediatric percentile, disease diagnosis, and personal targets.

The initial `bmi.metric.standard` Profile will preserve Height and Body Weight input lineage, provenance, units, missingness, and method context. It must not silently substitute estimated or self-reported inputs for measured inputs.

## 17. eGFR Boundary Approval

`estimated_glomerular_filtration_rate` is approved as one SC concept with equation-specific Profiles. The first Profile is `egfr.ckd_epi_2021_creatinine`, using the race-free CKD-EPI 2021 creatinine equation for adults age 18 and older.

Measured GFR, creatinine clearance, cystatin-C-only eGFR, and creatinine-plus-cystatin-C eGFR remain distinct or deferred. The equation's binary female/male parameter is not a general gender-identity inference.

## 18. SBP and DBP Separate-Concept Approval

`systolic_blood_pressure` and `diastolic_blood_pressure` remain separate ME RegistryConcepts. A future Observation may associate paired values through one shared measurement-event reference. The event relationship does not merge the RegistryConcepts or infer a missing paired value.

No Observation schema or event implementation is created by this approval.

## 19. Office and Home Profile Approval

The initial SBP and DBP scope includes candidate-specific office upper-arm and home upper-arm Profiles. Ambulatory, cuffless, wrist, central, and invasive Profiles remain deferred.

Future exact Profiles must freeze device class, cuff, site, posture, rest, reading sequence, interval, averaging, measurement window, and source-role boundaries without treating office and home results as interchangeable.

## 20. Pilot B Source Readiness

The approved audit covers 16 unique existing sources. Thirteen received direct content review. Three retained authoritative current metadata or summary access while full-body access was constrained: `SRC-AHA-BP-MEAS`, `SRC-AHA-BP-2025`, and `SRC-AHA-BP-2025-CORR-1436`.

No source addition is currently established as mandatory for a clean proposed concept boundary. The named metadata, access, correction-chain, and freshness prerequisites remain mandatory before precise claims or source-verification authoring.

## 21. eGFR 18-25 Age-Overlap Qualification

The first eGFR Profile remains the race-free CKD-EPI 2021 creatinine equation for adults age 18 and older. The future Pilot B1 schema-exact manifest must additionally state that ages 18-25 overlap with CKiD U25 applicability in current NIDDK guidance. The Agent or calculation layer must not silently select one equation, merge results from different equations into one continuous trend, or treat equation disagreement as data error. This qualification does not create a second initial Registry Profile or change the approved one-concept/equation-specific-Profile architecture.

```text
population = adults age 18+
18-25 overlap note = required
silent equation selection = prohibited
cross-equation trend continuity = prohibited
CKiD U25 Profile creation in B1 = deferred
```

## 22. BMI Equation-Version Qualification

The future BMI manifest must not invent a medical, guideline, or standards version for the conventional BMI formula. It must freeze the computation key, equation name, formula, source keys, input contracts, output-unit policy, provenance, and missingness behavior. `equation_version` remains `null` unless a separately governed, source-supported computation-contract label is deliberately approved.

```text
computation_key = bmi.weight_kg_height_m2
equation_name = Body Mass Index
equation_version = null
formula_or_equation = body_weight_kg / (height_m * height_m)
```

Any future internal computation-contract version must be explicitly identified as a Congtie governance label and must not impersonate a WHO, LOINC, WS/T, or clinical formula version.

## 23. BP Corrected-Source Gate

Before exact BP source objects, precise claim authoring, or `source_verified` transition, a future task must:

1. Reopen legally accessible AHA 2019 measurement-statement content.
2. Reopen the corrected 2025 main guideline.
3. Preserve all three correction notices as linked to the main guideline.
4. Complete content review of correction `1436`.
5. Freeze each source role, `supports`, and `does_not_support` scope.
6. Avoid treating a correction notice as a standalone guideline.

This gate blocks precise BP claim and source-verification authoring. It does not block this readiness baseline or approved concept boundaries. A new source addition is not currently established as necessary.

## 24. WS/T 428 Freshness Gate

WS/T 428-2013 remains the formal China BMI context used by the approved audit unless and until an official amendment or replacement is formally issued. The final amendment status must be rechecked before BMI source verification or any exact China decision-context object is authored. A consultation draft must not be treated as adopted authority.

This gate does not block C46 or a clean schema-exact concept boundary. It blocks a source-verified China decision context until rechecked.

## 25. Jurisdiction and Threshold Separation

Future proposed Pilot B records keep `reference_contexts = []` unless a separate Founder task authorizes exact objects. Population reference intervals, clinical decision limits, treatment thresholds, risk thresholds, diagnostic thresholds, critical values, and personalized targets remain separate.

WHO BMI categories, China BMI categories, US BP thresholds, and China BP thresholds are jurisdiction- and use-context-specific. No global `normal_range`, universal `120/80` target, CKD diagnosis, personal target, or action is authorized.

## 26. Production-Order Approval

Founder approves Option B subwaves:

```text
B1: body_mass_index + estimated_glomerular_filtration_rate
B2: systolic_blood_pressure + diastolic_blood_pressure
```

B1 validates derived computation and input lineage first. B2 then keeps the paired BP concept and event-metadata review together. Each subwave requires a separate authorization.

## 27. Numeric-ID Option B Approval

Option B remains controlling:

```text
approved boundary and readiness
-> exact schema-exact authoring manifest
-> controlled numeric-ID allocation proposal
-> exact-SHA Founder approval
-> controlled reservation commit
-> separately authorized proposed-record creation
```

No numeric ID is assigned, proposed, reserved, or made effective in C45 or C46.

## 28. Pilot B No-ID and No-Record State

```text
Pilot B schema-exact authoring manifests = 0
Pilot B numeric IDs assigned = 0
Pilot B effective reservations = 0
Pilot B allocation ledgers = 0
Pilot B Registry records = 0
Pilot B standalone Profile files = 0
```

Read-only namespace arithmetic is nonbinding and not candidate-bound:

| Namespace | Arithmetic next number | Authority status |
| --- | ---: | --- |
| BM | 24 | not proposed; not reserved; not effective |
| ME | 21 | not proposed; not reserved; not effective |
| SC | 4 | not proposed; not reserved; not effective |
| QS | 1 | not proposed; not reserved; not effective |

No intended Pilot B record path exists.

## 29. Schema and Permanent Validator Result

The C46 final gate revalidates the unchanged Draft 2020-12 Schema and hardened Permanent Validator with Python 3.9 and `jsonschema[format]==4.25.1`.

Required result:

```text
Python compile = PASS
Semantic self-test valid fixtures = 6/6
Semantic self-test invalid fixtures rejected = 17/17
Schema-backed self-test = PASS
Draft 2020-12 engine = available
Four canonical Pilot A records = 4/4 VALID
Warnings = 0
Errors = 0
```

## 30. Candidate and Migration Ledger Result

```text
Candidate Ledger + Migration Ledger = VALID
Core candidates = 53
First Wave candidates = 12
Migration rows = 169
First-Wave migration blockers = 0
Silent migration loss = 0
```

Candidate planning remains separate from canonical records and effective ID reservations.

## 31. Explicit Non-Authorizations

This approval does not authorize:

- a Pilot B authoring manifest, intended path, numeric-ID assignment, reservation, allocation ledger, Registry record, or standalone Profile file;
- any Pilot A or Pilot B lifecycle transition;
- Schema, Validator, Candidate Ledger, Migration Ledger, allocation, CI, or dependency changes;
- use-evidence claims, ReferenceContexts, thresholds, system relations, lifecycle relations, or device mappings;
- Observation schema, measurement event, ingestion, or user-health storage;
- database, API, loader, index, runtime, retrieval, publication, diagnosis, treatment, personal target, or action.

## 32. Controlled Three-Commit Plan

The approved version-control sequence is:

| Commit | Exact file | Message |
| --- | --- | --- |
| A | Pilot A source-verification closeout only | `docs: close Pilot A bounded source verification` |
| B | Pilot B read-only readiness audit only | `docs: record Pilot B Registry readiness audit` |
| C | this C46 Founder approval closeout only | `docs: approve Pilot A closeout and Pilot B readiness baseline` |

The three local commits must be created in order, pass exact staged-manifest checks, pass a remote-movement gate against `1560cd562b8896e420f296066a6115029b37cefd`, and be pushed once without force.

## 33. Recommended Next Gate

```text
Step5-C47: Pilot B1 Schema-Exact Authoring Manifest - BMI + eGFR Derived Concepts Only
```

C47 may define exact BMI and eGFR blueprints and perform no-ID dry runs. It must not assign numeric IDs, create allocation proposals or repository records, modify Schema/Validator/Ledgers, create BP manifests, or enable runtime/retrieval.
