# Registry First Wave Pilot B1 Proposed-Record Authoring Manifest Founder Approval 2026-08-26 v0.1

Status: Founder Approved for Version Control / Pilot B1 BMI + eGFR Schema-Exact Authoring Manifest Approved / Numeric IDs, Allocations and Registry Record Creation Not Authorized

Founder: 蓝耀栋

Approval date: 2026-08-26

## 1. Purpose

This closeout records Founder approval of the exact SHA-identified Pilot B1 schema-exact authoring manifest for Body Mass Index and Estimated Glomerular Filtration Rate. It preserves the reviewed manifest byte-identically and is the authoritative approval record for its exact reviewed bytes.

> Founder approves the exact SHA-identified Pilot B1 BMI and eGFR schema-exact authoring manifest for version control. The two RegistryConcept blueprints, their embedded Profiles, computation contracts, input lineage, source pools, unit policies, external mappings, provenance rules, missingness boundaries, interpretation limitations and Agent permission boundaries are approved. This approval creates no numeric ID, proposed ID, effective reservation, allocation ledger, intended record path, Registry record, standalone Profile, lifecycle transition, runtime authority or retrieval authority.

## 2. Repository Baseline

```text
Repository: /Users/lanyaodong/Documents/congtie-api
Branch: main
Initial HEAD: 609fb6fedbc486ac957660da0e0a535c6ada888f
Initial origin/main: 609fb6fedbc486ac957660da0e0a535c6ada888f
Approval date: 2026-08-26
Initial staging: empty
```

The repository, remote, date, staging, C47 manifest and protected Registry SHA gates passed before this closeout was created.

## 3. C46 Lineage

The approved predecessor history is:

| Commit | Parent | Message | Exact manifest count |
| --- | --- | --- | ---: |
| `e0538104850aa794b1b764d8c4f41922b767555f` | `1560cd562b8896e420f296066a6115029b37cefd` | `docs: close Pilot A bounded source verification` | 1 |
| `b49bdc3512c456f27f8aad2b5104971bf72b991f` | `e0538104850aa794b1b764d8c4f41922b767555f` | `docs: record Pilot B Registry readiness audit` | 1 |
| `609fb6fedbc486ac957660da0e0a535c6ada888f` | `b49bdc3512c456f27f8aad2b5104971bf72b991f` | `docs: approve Pilot A closeout and Pilot B readiness baseline` | 1 |

C46 approved a later Pilot B1 schema-exact authoring-manifest task. It did not authorize numeric-ID planning, allocation, record creation or lifecycle transition.

## 4. Exact C47 Manifest

```text
Path:
agent/knowledge_seed_v0/registry_first_wave_pilot_b1_proposed_record_authoring_manifest.v0.1.md

SHA-256:
256ef864459abc1844ff06e37805451018b3860011ce2ddc91f4a6c8f63d9190

Lines:
1144
```

The manifest retains its reviewed `Draft / Founder Review Pending / Numeric IDs, Allocation and Registry Record Creation Not Authorized` status and fourteen pending decision entries. Those historical fields are not rewritten because this approval applies to the exact bytes above.

## 5. Exact Pilot B1 Candidate Scope

| Candidate | Namespace | Initial Profile | Profiles approved |
| --- | --- | --- | ---: |
| `body_mass_index` | SC | `bmi.metric.standard` | 1 |
| `estimated_glomerular_filtration_rate` | SC | `egfr.ckd_epi_2021_creatinine` | 1 |

```text
Candidates approved = 2/2
Blood-pressure artifacts approved in C48 = 0
Other Pilot B or Pilot C candidates approved in C48 = 0
```

## 6. BMI Blueprint Approval

`body_mass_index` is approved as one SC derived-index RegistryConcept with adult interpretation scope in v0.1. It remains distinct from body-fat percentage, body composition, adiposity or disease diagnosis, pediatric percentile, moral judgment and personal target.

The only initial Profile is `bmi.metric.standard`, with lifecycle target `proposed`, measurement nature `derived` and source modality `calculated`.

## 7. BMI Profile, Computation and Input Approval

The approved BMI computation contract is:

```text
computation_key = bmi.weight_kg_height_m2
equation_name = Body Mass Index
equation_version = null
formula_or_equation = body_weight_kg / (height_m * height_m)
output = kg/m2
```

The exact required Registry inputs are Height through `height.standing.stadiometer` in metres and Body Weight through `body_weight.scale_measured` in kilograms. Original observation, record/Profile identity, value, unit, timestamp, conversion and provenance must remain linked. Missing or unapproved substitute inputs prohibit calculation.

## 8. BMI Source, Unit and Mapping Approval

The approved source pool is the exact four-source collection in the C47 manifest: LOINC BMI, WHO BMI context, WS/T 428 China context and UCUM. The concept uses a single canonical `kg/m2` UnitPolicy and high-confidence concept mapping to LOINC `39156-5`.

The LOINC mapping does not establish Profile, protocol or device equivalence. No China local code, ReferenceContext, clinical threshold or personal target is approved.

## 9. BMI Validator-Contract Timing Approval

A BMI-specific Permanent Validator computation contract is approved as a prerequisite before a future BMI transition to `source_verified`, `human_reviewed` or `active`. It is not a prerequisite for later separately authorized `proposed` record materialization from the exact approved blueprint.

C48 does not modify the Permanent Validator and does not execute record materialization or lifecycle transition.

## 10. eGFR Blueprint Approval

`estimated_glomerular_filtration_rate` is approved as one SC derived-index RegistryConcept with equation-specific Profiles. The only initial Profile is `egfr.ckd_epi_2021_creatinine`, with lifecycle target `proposed`, measurement nature `derived` and source modality `calculated`.

Measured GFR, creatinine clearance, cystatin-C-only eGFR, creatinine-plus-cystatin-C eGFR, CKD diagnosis or stage, medication action and personal target remain separate or deferred.

## 11. CKD-EPI 2021 Formula and Input Approval

The race-free CKD-EPI 2021 creatinine equation is approved exactly as frozen in the C47 manifest:

```text
equation_name = CKD-EPI 2021 Creatinine Equation
equation_version = 2021 creatinine
common leading constant = 142
common creatinine-ratio exponent = -1.200
age factor = 0.9938
female k = 0.7
female alpha = -0.241
female factor = 1.012
male k = 0.9
male alpha = -0.302
male factor = 1
race coefficient = absent
```

The exact inputs are standardized Creatinine through `creatinine.serum_or_plasma.enzymatic` in `mg/dL`, `age_years` in years and the governed binary equation parameter from `sex_at_birth`. Unknown or uncovered parameter values are not forcibly mapped and prohibit calculation pending separate governance.

## 12. Age 18-25 Overlap Qualification

The adult Profile applies from age 18. Ages 18-25 overlap with CKiD U25 applicability in current NIDDK guidance. The future Agent or calculation layer must not silently choose an equation, merge results from different equations into one continuous trend or treat equation disagreement as a data error.

CKiD U25 remains deferred and no second eGFR Profile is created or authorized by C48.

## 13. Reported-versus-Derived Origin Boundary

Laboratory-reported and locally derived eGFR must retain distinct origin and provenance. Future handling must preserve the source report, equation identity and version, source Creatinine observation, age context, governed sex parameter, calculation timestamp, original display and local calculation provenance.

C48 creates no Observation data, storage or calculation service.

## 14. Rounding, Capping and Unindexing Boundary

Silent rounding, capping, greater-than display conversion, equation substitution and cross-equation trend merging are prohibited. Unindexing from `mL/min/{1.73_m2}` is prohibited without separately governed body-surface-area inputs and an approved equation. Equation or reporting changes form trend breakpoints.

## 15. eGFR Source, Unit and Mapping Approval

The approved source pool is the exact six-source collection in the C47 manifest: NIDDK adult equations, Inker 2021, LOINC equation-specific mapping, UCUM, KDIGO 2024 context and NIDDK age-overlap guidance.

The approved canonical output unit is `mL/min/{1.73_m2}`. LOINC `98979-8` is approved as a high-confidence Profile mapping. The concept mapping array remains empty and no China local code is guessed.

## 16. Validation Result

The exact Appendix A and Appendix B JSON objects were deterministically extracted to `/tmp` and revalidated without creating repository records.

```text
Python = 3.9.6
jsonschema = 4.25.1
JSON parse = 2/2 PASS
Draft 2020-12 Schema definition = PASS
Permanent Validator compile = PASS
valid self-test fixtures = 6/6
invalid self-test fixtures rejected = 17/17
semantic self-test = PASS
Schema-backed self-test = PASS
Draft 2020-12 engine = available
BMI no-ID record = VALID
eGFR no-ID record = VALID
Candidate and Migration Ledgers = VALID
warnings = 0
errors = 0
```

The BMI no-ledger negative test returned exit `2` with the required Candidate Ledger lineage-resolution message.

## 17. Founder Decisions

| # | Decision | Founder Decision |
| ---: | --- | --- |
| 1 | Exact BMI RegistryConcept blueprint | Approved |
| 2 | `bmi.metric.standard` Profile and exact inputs | Approved |
| 3 | BMI source pool, unit and LOINC mapping | Approved |
| 4 | BMI `equation_version = null` | Approved |
| 5 | BMI-specific Validator contract before `source_verified`, not before `proposed` materialization | Approved |
| 6 | Exact eGFR RegistryConcept blueprint | Approved |
| 7 | `egfr.ckd_epi_2021_creatinine` Profile and exact formula | Approved |
| 8 | Exact eGFR input and context contract | Approved |
| 9 | Age 18-25 overlap and equation-selection/trend boundary | Approved |
| 10 | Reported-versus-derived origin, rounding, capping and unindexing rules | Approved |
| 11 | eGFR source pool, unit and LOINC mapping | Approved |
| 12 | No claims, thresholds, targets, IDs, allocations or Registry records | Approved |
| 13 | Exact-SHA Founder approval and controlled manifest commit | Approved |
| 14 | A later numeric-ID allocation-planning task after this manifest approval | Approved |

```text
Founder approvals = 14/14
Founder pending decisions = 0
Accidental approvals = 0
```

Decision 14 authorizes only a future, separately gated numeric-ID planning task. It does not propose, calculate, reserve or bind any ID in C48.

## 18. Strict No-ID and No-Record State

```text
Pilot B1 numeric IDs assigned = 0
Pilot B1 proposed IDs = 0
Pilot B1 effective reservations = 0
Pilot B1 allocation ledgers = 0
Pilot B1 intended record paths = 0
Pilot B1 repository Registry records = 0
Pilot B1 standalone Profile files = 0
Pilot B1 lifecycle transitions = 0
Pilot B1 runtime/retrieval authorizations = 0
```

Approval and Git versioning of planning documents do not create Registry records or lifecycle state.

## 19. Explicit Non-Authorizations

This approval does not authorize numeric-ID assignment, proposal or reservation; allocation ledgers; intended canonical record paths; BMI or eGFR Registry JSON records; standalone Profile files; blood-pressure artifacts; Candidate or Migration Ledger mutation; Schema or Validator changes; claims; ReferenceContexts; thresholds; targets; system or lifecycle relations; device mappings; Observation schemas or data; user-health storage; database, API, loader or index work; publication; runtime; retrieval; diagnosis; treatment; dosing; recommendation or action.

Human review, `source_verified`, `human_reviewed` and `active` lifecycle transitions remain separately gated.

## 20. Controlled Two-Commit Plan

The approved Git sequence is:

1. Commit the exact C47 manifest alone with message `docs: add Pilot B1 Registry authoring manifest`.
2. Commit this Founder approval closeout alone with message `docs: approve Pilot B1 Registry authoring manifest`.
3. Recheck `origin/main` against the initial anchor.
4. Perform one ordinary push to `origin/main` if the remote movement Gate passes.

No amend, squash, rebase, merge, force push or unrelated staging is authorized.

## 21. Next Founder Gate

The only recommended next task is `Step5-C49: Pilot B1 Numeric-ID Allocation Proposal - BMI + eGFR Only`.

C49 may read the approved C47 manifest and this exact approval, perform namespace-level collision analysis, propose two non-effective reservations and intended paths, and create an allocation proposal. C49 must not make reservations effective, create Registry records, modify the Candidate Ledger, Schema or Validator, execute lifecycle transition, or enable runtime or retrieval.
