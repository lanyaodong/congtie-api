# Registry First Wave Pilot B1 Proposed-Record Authoring Manifest v0.1

Status: `Draft / Founder Review Pending / Numeric IDs, Allocation and Registry Record Creation Not Authorized`

Prepared date: `2026-08-26`

Repository anchor: `609fb6fedbc486ac957660da0e0a535c6ada888f`

## 1. Purpose

This document freezes two Schema-exact, no-ID proposed-record blueprints for `body_mass_index` and `estimated_glomerular_filtration_rate`. It records source verification, computation contracts, units, mappings, input lineage, privacy boundaries and validation evidence. It creates no Registry ID, allocation, intended canonical record path, Registry record, standalone Profile, lifecycle transition, runtime capability or product authority.

## 2. Repository Baseline

| Gate | Result |
| --- | --- |
| Repository | `/Users/lanyaodong/Documents/congtie-api` |
| Branch | `main` |
| HEAD / `origin/main` | `609fb6fedbc486ac957660da0e0a535c6ada888f` |
| Execution date | `2026-08-26` |
| Staging | empty |
| Pre-existing target | absent |
| Pilot B1 records / IDs / allocations | `0 / 0 / 0` |

## 3. Exact C46 Lineage and SHA

The exact C46 history gate passed:

| Commit | Parent | Message | Exact manifest count |
| --- | --- | --- | ---: |
| `e0538104850aa794b1b764d8c4f41922b767555f` | `1560cd562b8896e420f296066a6115029b37cefd` | `docs: close Pilot A bounded source verification` | 1 |
| `b49bdc3512c456f27f8aad2b5104971bf72b991f` | `e0538104850aa794b1b764d8c4f41922b767555f` | `docs: record Pilot B Registry readiness audit` | 1 |
| `609fb6fedbc486ac957660da0e0a535c6ada888f` | `b49bdc3512c456f27f8aad2b5104971bf72b991f` | `docs: approve Pilot A closeout and Pilot B readiness baseline` | 1 |

All 14 protected SHA gates passed. Key authoring authorities are:

| Artifact | SHA-256 |
| --- | --- |
| C46 Founder approval | `50e66e017de8f49a0a3419858ef8f81ec8b72b6de96b4e667bd57eeeb19bc67b` |
| Pilot B readiness audit | `03da66dd3d8ad62e985f88c0d2f917cc52a341354dc7c13e5cf37286a5bb9bda` |
| First Wave plan | `8266be330cbb15a9526828410e708924a514e1582585a0db17144ad34b34ea63` |
| Registry Schema | `a376b02e8cf50e95392287a8924919e57c6df6e37fa957830d4f1a60d1557aa7` |
| Permanent Validator | `baf2de87085b697ed2c4a990546f2e29b4c938aec36005ce6d3a3348933bddb2` |
| Candidate Ledger | `b97f4b0e0aeaa4fae6e728c561e88019d3c9e0b34ce353c1cc2b27f5cd09bbe5` |
| Migration Ledger | `592408206315e2a404740c0fe5ca1f1ad574d407401d9df9c7f2062a45ad1a56` |

## 4. Authoritative Pilot B1 Scope

| Candidate | Namespace | Initial Profile | Profiles |
| --- | --- | --- | ---: |
| `body_mass_index` | SC | `bmi.metric.standard` | 1 |
| `estimated_glomerular_filtration_rate` | SC | `egfr.ckd_epi_2021_creatinine` | 1 |

Candidates covered: `2/2`. No third candidate is included.

## 5. Explicit Exclusions

Excluded are blood-pressure authoring, Pilot C, Heart Rate lifecycle work, numeric-ID work, allocation work, repository records, standalone Profiles, ReferenceContexts, claims, thresholds, system/lifecycle relations, device mappings, Observation assets, user data and runtime or retrieval work.

## 6. Candidate Ledger Identity Matrix

| Candidate | Chinese | English | Alias | Review | Construct | Allowed natures | Preproduction issue |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `body_mass_index` | 体重指数 | Body Mass Index | BMI | GREEN | `derived_index` | `derived`, `reported` | Height and body-weight provenance must remain linked; BMI is not a diagnosis. |
| `estimated_glomerular_filtration_rate` | 估算肾小球滤过率 | Estimated Glomerular Filtration Rate | eGFR | YELLOW | `derived_index` | `derived`, `reported` | Equation, version, inputs, demographics, unit and lineage are required. |

Both are Core, First Wave, SC, `proposed`, unassigned and `registry_id = null` in the Candidate Ledger.

## 7. Pilot A Dependency Matrix

| Input | Required Profile | Current evidence | Equation unit | Boundary |
| --- | --- | --- | --- | --- |
| `height` | `height.standing.stadiometer` | concept/Profile `source_verified` | `m` | Preserve original observation, Profile, unit, timestamp and provenance. |
| `body_weight` | `body_weight.scale_measured` | concept/Profile `source_verified` | `kg` | No self-report or future household-scale substitution. |
| `creatinine` | `creatinine.serum_or_plasma.enzymatic` | concept/Profile `source_verified` | `mg/dL` | Preserve specimen, assay/platform, traceability, unit and source observation. |

Dependency SHAs remain protected and unchanged. Dependency readiness is not Pilot B1 materialization authority.

## 8. Schema-Exact Authoring Method

Each appendix is a complete RegistryConcept JSON object in current Schema order. Every value is frozen except later controlled injection of `registry_id` and the actual controlled record-creation date. C47 uses `null` and `2026-08-26` only for no-ID validation. Validator fixture wording is not canonical authority.

## 9. RegistryConcept Required-Field Coverage 25/25

Identity, lifecycle, names, aliases, information/construct, measurement natures, value type, UnitPolicy, sources, definition keys, Profiles, mappings, limitations, Agent permissions, target boundary, lifecycle relations and governance metadata are exact. Claims and system/lifecycle relations are exact empty arrays. Programmatic result: `25/25` for both; unresolved required fields: `0`.

## 10. MeasurementProfile Required-Field Coverage 12/12

Both Profiles exactly provide `profile_key`, `profile_status`, `measurement_nature`, `source_modality`, `method_comparability_status`, `accepted_units`, `reference_contexts`, `external_mappings`, `device_mappings`, `profile_limitations`, `source_reference_keys` and `derived_computation`. Programmatic result: `12/12` for both; unresolved required fields: `0`.

## 11. Common No-ID Authoring Rules

```text
registry_id = null
namespace = SC
lifecycle_status = proposed
version = v0.1
information_type = derived_score_index
value_type = number
profiles = exactly 1
use_evidence_claims = []
system_relations = []
lifecycle_relations = []
Profile.reference_contexts = []
Profile.device_mappings = []
reviewed_by = []
reviewed_date = null
```

The dry runs are fixtures, not canonical records, and create no reservation, intended path, Registry authority or runtime capability.

## 12. BMI Concept Boundary

BMI is body weight divided by squared height under an explicit, provenance-preserving computation Profile. It is not body-fat percentage, fat mass, body composition, adiposity or disease diagnosis, pediatric percentile, moral judgment or personal target. Adult interpretation is the v0.1 scope; no threshold object is authored.

## 13. BMI Exact Profile Boundary

The only Profile is `bmi.metric.standard`, `proposed`, `derived`, `calculated`. It only accepts `height.standing.stadiometer` and `body_weight.scale_measured`. Self-reported, estimated, future household-scale and missing inputs are not silently substituted.

## 14. BMI Exact DerivedComputation

```text
computation_key = bmi.weight_kg_height_m2
equation_name = Body Mass Index
equation_version = null
formula_or_equation = body_weight_kg / (height_m * height_m)
output = kg/m2
```

The result retains exact input record/Profile identity, original value/unit, timestamp and provenance and cannot inherit confidence above its inputs.

## 15. BMI Exact Input Objects

| Input | Kind | Candidate | Role | Unit | Initial Profile |
| --- | --- | --- | --- | --- | --- |
| `height_m` | `registry_concept` | `height` | measured standing height converted to metres | `m` | `height.standing.stadiometer` |
| `body_weight_kg` | `registry_concept` | `body_weight` | measured body weight converted to kilograms | `kg` | `body_weight.scale_measured` |

Both are required. Exact notes prohibit silent substitution and require original Observation provenance. Conversion does not create method equivalence.

## 16. BMI Unit Policy

Concept and computation use `single_canonical` UCUM `kg/m2`. The conventional representation is retained and is not normalized to `1`.

## 17. BMI Source Pool and Source Verification

| Source | Role | Status | Supports | Does not support | Freshness result |
| --- | --- | --- | --- | --- | --- |
| `src-loinc-bmi` / LOINC `39156-5` | terminology/formula/mapping | `content_verified` | construct, formula, concept mapping, unit example | method equivalence, diagnosis, targets | active; code last updated in 2.73 |
| `src-who-bmi` / WHO fact sheet | `definition_authority` | `content_verified` | formula, adult context, pediatric separation | device equivalence, personal action | current; dated 2025-12-08 |
| `src-wst428` / WS/T 428-2013 | China context | `content_verified` | China adult construct/formula/scope | global thresholds, personal action | formal 2013 standard; 2025 amendment page is consultation only |
| `src-ucum` / UCUM 2.2 | unit syntax | `content_verified` | `kg/m2` syntax | method or clinical meaning | dated 2024-06-17 |

All four were opened on `2026-08-26`. No source blocker remains for a proposed blueprint. No China ReferenceContext or threshold is created.

## 18. BMI LOINC Mapping

LOINC `39156-5` is a high-confidence `mapped` concept mapping. Its method component is null, so it does not establish Profile, protocol or device equivalence. No China local code is guessed.

## 19. BMI Provenance and Missingness

No BMI is generated if either input or lineage is missing. Future provenance must retain input record/Profile, original value/unit, timestamp, conversion and source. Profile, method, protocol, device or timing changes can form trend breakpoints.

## 20. BMI Agent Permissions

Permitted: construct, formula, unit, provenance, missingness and breakpoint explanation plus context questions. Prohibited: inferred or substituted inputs, inferred body fat, diagnosis, moral judgment, personal targets and action. `action_authorization = none`.

## 21. BMI Validator-Contract Assessment

A BMI-specific `KNOWN_COMPUTATION_CONTRACTS` hardening is not required for this no-ID manifest or a later `proposed` record materialization because the exact manifest and generic lineage checks bind the proposed record. It should be separately approved before any BMI transition to `source_verified`, `human_reviewed` or `active`, so the Permanent Validator can reject missing or substituted Height and Body Weight inputs.

Founder Decision: `Pending`.

## 22. eGFR Concept Boundary

eGFR is an equation-derived estimate under an explicitly named Profile and governed inputs. It is distinct from measured GFR, creatinine clearance, raw creatinine, cystatin-C-only or combined eGFR, CKD diagnosis/stage, medication action and personal target.

## 23. eGFR Exact Profile Boundary

The only Profile is `egfr.ckd_epi_2021_creatinine`, `proposed`, `derived`, `calculated`: the race-free CKD-EPI 2021 creatinine equation for adults age 18+. Its only Registry input Profile is `creatinine.serum_or_plasma.enzymatic`, supplied as standardized creatinine in `mg/dL`.

## 24. CKD-EPI 2021 Exact Equation

```text
computation_key = egfr.ckd_epi_2021_creatinine
equation_name = CKD-EPI 2021 Creatinine Equation
equation_version = 2021 creatinine
142 * min(scr_mg_dl / k, 1)^alpha * max(scr_mg_dl / k, 1)^(-1.200)
    * 0.9938^age_years * sex_factor
female: k = 0.7, alpha = -0.241, sex_factor = 1.012
male:   k = 0.9, alpha = -0.302, sex_factor = 1
race coefficient = absent
```

The constants match NIDDK and Inker 2021. No placeholder or fixture-only formula is used.

## 25. eGFR Exact Input Objects

| Input | Kind | Candidate/context | Role | Unit |
| --- | --- | --- | --- | --- |
| `scr_mg_dl` | `registry_concept` | `creatinine` | standardized serum creatinine used by the named equation | `mg/dL` |
| `age_years` | `user_context` | `age_years` | age in years at calculation time | `a` |
| `sex_at_birth` | `categorical_parameter` | `sex_at_birth` | binary published-equation parameter | `null` |

`sex_at_birth` only resolves the female/male equation parameter. It is not gender-identity inference and is never inferred from proxies. Missing, nonbinary, intersex, unknown or uncovered values are not forcibly mapped and prohibit calculation pending separate governance.

## 26. eGFR 18-25 Age-Overlap Qualification

The adult Profile starts at 18. NIDDK places CKiD U25 at ages 1-25 and recommends considering both calculators at ages 18-25. One equation must not be silently selected; different equations are not merged into one trend; disagreement is not a data error. CKiD U25 is deferred and no second Profile is created.

## 27. eGFR Unit and Output Policy

Concept and computation use `single_canonical` UCUM `mL/min/{1.73_m2}`. Unindexed `mL/min` is not an unconditional equivalent. Creatinine conversion never establishes assay equivalence.

## 28. eGFR Reported-vs-Derived Origin Policy

Laboratory-reported and locally derived eGFR keep distinct origin/provenance. Future handling must preserve source report, equation identity/version, source creatinine Observation, age context, sex parameter, calculation timestamp, original display and local provenance. This manifest creates no Observation data.

## 29. eGFR Rounding, Capping and Unindexing Policy

Silent rounding, capping and displays such as greater-than cutoffs are prohibited. Unindexing is prohibited without separately governed body-surface-area inputs and an approved equation. Equation/reporting changes form trend breakpoints.

## 30. eGFR Source Pool and Source Verification

| Source | Role | Status | Supports | Does not support | Freshness result |
| --- | --- | --- | --- | --- | --- |
| `src-niddk-egfr-adults` | equation/method | `content_verified` | constants, inputs, units, age 18+ | assay equivalence, diagnosis, dosing | current; reviewed May 2025 |
| `src-inker-2021` | `validation_evidence` | `content_verified` | race-free equation development/validation | universal accuracy, action | lawful PMC manuscript and PubMed metadata; no retraction identified |
| `src-loinc-egfr-2021` / `98979-8` | Profile mapping | `content_verified` | equation-specific mapping, adult scope, indexed unit | measured GFR, diagnosis | active; code last updated in 2.79 |
| `src-ucum` / UCUM 2.2 | unit syntax | `content_verified` | output-unit syntax | equation/clinical meaning | dated 2024-06-17 |
| `src-kdigo-ckd-2024` | context | `content_verified` | scope and limitation boundary | equation identity, automatic stage/action | 2024 remains current; focused Chapter 3 update underway |
| `src-niddk-egfr-age-overlap` | applicability context | `content_verified` | explicit 18-25 overlap | silent selection, CKiD Profile creation | current; reviewed May 2024 |

All six record-local source objects were opened on `2026-08-26`. No source blocker remains for a proposed blueprint.

## 31. eGFR LOINC Mapping

LOINC `98979-8` is a high-confidence `mapped` Profile mapping because it names the CKD-EPI 2021 creatinine formula and indexed output. The concept mapping array stays empty. No China local code is guessed.

## 32. eGFR Agent Permissions

Permitted: construct, equation, input, unit, origin, age-overlap and breakpoint explanation plus context questions. Prohibited: inferred inputs, gender inference, forced category mapping, silent equation selection, cross-equation trend merging, diagnosis/staging, dosing/treatment, personal targets and action. `action_authorization = separately_gated`.

## 33. Claims, Reference and Threshold Non-Authorization

Both blueprints have empty claim and ReferenceContext arrays. No WHO/China BMI category, CKD stage, decision/risk/critical threshold, diagnosis, treatment, dosing, alert or recommendation is authored.

## 34. Personalized-Target Boundary

Both use `support_status = requires_governance` with authorized context, claim-specific evidence, safety, permission and Personalized Longevity Protocol prerequisites. Public Registry records store no user target, rationale, effective period or action linkage.

## 35. No-ID Dry-Run Materialization

Two UTF-8, LF, two-space-indented fixtures with one final newline were generated only under `/tmp/congtie-registry-pilot-b1-c47-dry-run`:

| Fixture | SHA-256 | Authority |
| --- | --- | --- |
| `body_mass_index.no_id.json` | `632239bc55212df66af194873bb44c727ecc3ef6572f5cb4e025322661892d70` | validation fixture only |
| `estimated_glomerular_filtration_rate.no_id.json` | `3b89b2aec1c0e8d141998ef2272b9a7f00f719768bbd76e5c05102c823d18dbe` | validation fixture only |

These are not Founder-approved record SHAs. The temporary directory is deleted at task close; later materialization dates remain controlled values.

## 36. Schema Validation

```text
Python = 3.9.6
jsonschema = 4.25.1
Draft 2020-12 Schema definition = PASS
BMI JSON/Schema = PASS
eGFR JSON/Schema = PASS
```

## 37. Permanent Validator Validation

```text
compile = PASS
valid fixtures = 6/6
invalid fixtures rejected = 17/17
semantic self-test = PASS
Schema-backed self-test = PASS
Draft 2020-12 engine = available
BMI no-ID record = VALID
eGFR no-ID record = VALID
warnings = 0
errors = 0
```

## 38. Negative Candidate-Ledger Gate

The BMI derived record without `--candidate-ledger` returned exit `2` and:

```text
Derived Registry-concept inputs require --candidate-ledger for lineage resolution.
```

Positive runs received the Candidate Ledger and passed lineage resolution.

## 39. Candidate and Migration Ledger Validation

`VALID: Candidate Ledger + Migration Ledger`, exit `0`; both files changed `0`.

## 40. Programmatic and Cross-Blueprint Checks

```text
programmatic checks = 32/32 PASS
RegistryConcept fields = 25/25 for both
MeasurementProfile fields = 12/12 for both
duplicate candidate/Profile/source/mapping keys = 0
dangling source keys = 0
unknown Candidate Ledger inputs = 0
numeric Registry ID literals = 0
personal data fields = 0
Pilot A dependency SHA changes = 0
```

## 41. Numeric-ID Option B Status

Option B remains: exact manifest approval precedes any numeric-ID planning. C47 assigns or proposes no ID, creates no allocation ledger and records no intended path. Future allocation requires separate authorization after exact-SHA approval.

## 42. Strict No-Record and No-Allocation State

```text
Pilot B1 numeric IDs assigned = 0
Pilot B1 proposed IDs = 0
Pilot B1 effective reservations = 0
Pilot B1 allocation ledgers = 0
Pilot B1 intended record paths = 0
Pilot B1 repository Registry records = 0
Pilot B1 standalone Profile files = 0
lifecycle transitions = 0
runtime/retrieval authorizations = 0
```

## 43. Founder Decision Sheet

| # | Decision | Founder Decision |
| ---: | --- | --- |
| 1 | Approve exact BMI RegistryConcept blueprint | Pending |
| 2 | Approve `bmi.metric.standard` Profile and exact inputs | Pending |
| 3 | Approve BMI source pool, unit and LOINC mapping | Pending |
| 4 | Approve BMI `equation_version = null` | Pending |
| 5 | Approve BMI Validator-contract gate before `source_verified`, not before `proposed` materialization | Pending |
| 6 | Approve exact eGFR RegistryConcept blueprint | Pending |
| 7 | Approve `egfr.ckd_epi_2021_creatinine` Profile and exact formula | Pending |
| 8 | Approve exact eGFR input/context contract | Pending |
| 9 | Approve 18-25 overlap and equation-selection/trend boundary | Pending |
| 10 | Approve origin, rounding, capping and unindexing rules | Pending |
| 11 | Approve eGFR source pool, unit and LOINC mapping | Pending |
| 12 | Confirm no claims, thresholds, targets, IDs, allocations or repository records | Pending |
| 13 | Authorize later exact-SHA approval and controlled manifest commit | Pending |
| 14 | Authorize numeric-ID planning only after manifest approval | Pending |

```text
Founder approvals = 0
Founder pending decisions = 14
Accidental approvals = 0
```

## 44. Explicit Non-Authorizations

No BP manifest, ID, allocation, record/Profile file, lifecycle promotion, Schema/Validator/Ledger change, claim, threshold, relation, mapping expansion, Observation, user data, publication, runtime, retrieval, database, API, loader, index, diagnosis, treatment, dosing, target or action is authorized.

## 45. Recommended Next Gate

`Step5-C48: Founder Review + Controlled Commit/Push - Pilot B1 Schema-Exact Authoring Manifest`

C48 may review this exact manifest, resolve 14 decisions, create an exact-SHA approval closeout and perform controlled manifest/approval commits. IDs, allocations, records and lifecycle transitions remain zero.

## Appendix A. Exact BMI No-ID Blueprint

```json
{
  "candidate_key": "body_mass_index",
  "registry_id": null,
  "namespace": "SC",
  "lifecycle_status": "proposed",
  "version": "v0.1",
  "canonical_name_zh": "体重指数",
  "canonical_name_en": "Body Mass Index",
  "abbreviation": "BMI",
  "aliases": [
    "BMI"
  ],
  "legacy_codes": [],
  "information_type": "derived_score_index",
  "measurement_domain": "anthropometry",
  "construct_type": "derived_index",
  "construct_definition": "Body weight divided by squared height under an explicit, provenance-preserving computation Profile.",
  "allowed_measurement_natures": [
    "derived",
    "reported"
  ],
  "value_type": "number",
  "unit_policy": {
    "mode": "single_canonical",
    "canonical_unit": {
      "unit_code": "kg/m2",
      "unit_system": "UCUM",
      "status": "canonical",
      "conversion_rule": null,
      "conversion_verified": false,
      "note": "Canonical conventional BMI representation; not silently normalized to unit 1."
    },
    "note": "Mathematical unit conversion does not establish input method, protocol or device equivalence."
  },
  "source_references": [
    {
      "source_key": "src-loinc-bmi",
      "title": "LOINC 39156-5, Body mass index (BMI) [Ratio]",
      "organization_or_journal": "Regenstrief / LOINC",
      "authors": [],
      "publication_date": null,
      "source_type": null,
      "source_role": "other_reviewed_role",
      "supports": [
        "Body mass index construct identity",
        "BMI formula as weight in kilograms divided by height in metres squared",
        "concept-level LOINC mapping 39156-5",
        "conventional UCUM example unit kg/m2"
      ],
      "does_not_support": [
        "input measurement-method equivalence",
        "body-fat percentage or body composition",
        "diagnosis",
        "pediatric percentile",
        "personal target or action"
      ],
      "url": "https://loinc.org/39156-5",
      "doi": null,
      "pmid": null,
      "access_date": "2026-08-26",
      "verification_status": "content_verified",
      "note": "Active LOINC term; the code was last updated in LOINC 2.73. Method remains unspecified by the code."
    },
    {
      "source_key": "src-who-bmi",
      "title": "Obesity and overweight",
      "organization_or_journal": "World Health Organization",
      "authors": [],
      "publication_date": "2025-12-08",
      "source_type": null,
      "source_role": "definition_authority",
      "supports": [
        "BMI formula using measured weight and height",
        "adult BMI interpretation context",
        "age-dependent separation of child and adolescent interpretation"
      ],
      "does_not_support": [
        "input device or protocol equivalence",
        "body-fat percentage identity",
        "universal personal target",
        "automatic diagnosis, treatment or action"
      ],
      "url": "https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight",
      "doi": null,
      "pmid": null,
      "access_date": "2026-08-26",
      "verification_status": "content_verified",
      "note": "Current WHO fact sheet opened in full; adult thresholds are not instantiated in this proposed record."
    },
    {
      "source_key": "src-wst428",
      "title": "WS/T 428-2013, 成人体重判定",
      "organization_or_journal": "National Health Commission of China",
      "authors": [],
      "publication_date": "2013-04-18",
      "source_type": null,
      "source_role": "other_reviewed_role",
      "supports": [
        "China adult BMI construct and formula context",
        "China adult applicability context for BMI"
      ],
      "does_not_support": [
        "global universal thresholds",
        "adoption of the 2025 consultation amendment draft",
        "personal target or action",
        "input measurement-method equivalence"
      ],
      "url": "https://www.nhc.gov.cn/wjw/yingyang/201308/a233d450fdbc47c5ad4f08b7e394d1e8.shtml",
      "doi": null,
      "pmid": null,
      "access_date": "2026-08-26",
      "verification_status": "content_verified",
      "note": "Official standard implemented 2013-10-01. The first amendment posted 2025-12-03 was a consultation ending 2026-01-02 and is not treated as adopted."
    },
    {
      "source_key": "src-ucum",
      "title": "The Unified Code for Units of Measure",
      "organization_or_journal": "Regenstrief Institute and UCUM Organization",
      "authors": [],
      "publication_date": "2024-06-17",
      "source_type": null,
      "source_role": "other_reviewed_role",
      "supports": [
        "UCUM unit syntax",
        "kg/m2 representation",
        "mL and time-unit syntax used in the eGFR output expression"
      ],
      "does_not_support": [
        "measurement-method equivalence",
        "clinical interpretation",
        "equation identity",
        "personal target or action"
      ],
      "url": "https://ucum.org/ucum",
      "doi": null,
      "pmid": null,
      "access_date": "2026-08-26",
      "verification_status": "content_verified",
      "note": "UCUM Specification version 2.2; unit syntax authority only."
    }
  ],
  "definition_source_keys": [
    "src-loinc-bmi",
    "src-who-bmi"
  ],
  "profiles": [
    {
      "profile_key": "bmi.metric.standard",
      "profile_status": "proposed",
      "measurement_nature": "derived",
      "source_modality": "calculated",
      "specimen_type": null,
      "matrix": null,
      "body_site": null,
      "collection_or_protocol_context": {
        "protocol_name": "provenance-preserving metric BMI calculation",
        "protocol_version": null,
        "measurement_window": "single governed calculation event",
        "timing_context": "Height and body-weight observations selected for the same governed calculation context",
        "fasting_status": "not_applicable",
        "fasting_duration_hours": null,
        "posture": null,
        "rest_duration_minutes": null,
        "body_site": null,
        "laterality": "not_applicable",
        "repetition_count": null,
        "pace_or_effort_instruction": null,
        "context_tags": [
          "height_profile_height.standing.stadiometer_required",
          "body_weight_profile_body_weight.scale_measured_required",
          "input_units_required",
          "input_timestamps_required",
          "input_provenance_required"
        ],
        "note": "These tags govern future Observation metadata requirements; this Profile stores no user observation values."
      },
      "method": "body weight in kilograms divided by standing height in metres squared",
      "instrument_or_device": null,
      "vendor_or_model": null,
      "algorithm_version": null,
      "accepted_units": [
        {
          "unit_code": "kg/m2",
          "unit_system": "UCUM",
          "status": "canonical",
          "conversion_rule": null,
          "conversion_verified": false,
          "note": "Canonical conventional BMI representation."
        }
      ],
      "canonicalization_rule": "Retain kg/m2 as the canonical output; preserve each input record, Profile, original value, original unit, timestamp and provenance.",
      "method_comparability_status": "context_dependent",
      "trend_breakpoint_note": "A Height or Body Weight Profile, method, protocol, device, unit-conversion, timing or provenance change may break BMI trend continuity.",
      "cross_platform_comparison_prohibited": true,
      "reference_contexts": [],
      "external_mappings": [],
      "device_mappings": [],
      "profile_limitations": [
        "Only height.standing.stadiometer and body_weight.scale_measured are permitted as initial input Profiles.",
        "Self-reported or estimated Height and self-reported Body Weight are not silently substituted.",
        "BMI is not generated when either required input or its provenance is missing.",
        "The derived result does not inherit confidence higher than its input observations and methods.",
        "Mathematical unit conversion does not make input methods, protocols or devices equivalent.",
        "Adult interpretation is the v0.1 scope; pediatric BMI-for-age and percentile interpretation are deferred.",
        "BMI is not body-fat percentage, fat mass, body composition, adiposity diagnosis, disease diagnosis, moral judgment or a personal target."
      ],
      "source_reference_keys": [
        "src-loinc-bmi",
        "src-who-bmi",
        "src-wst428",
        "src-ucum"
      ],
      "derived_computation": {
        "computation_key": "bmi.weight_kg_height_m2",
        "equation_name": "Body Mass Index",
        "equation_version": null,
        "formula_or_equation": "body_weight_kg / (height_m * height_m)",
        "inputs": [
          {
            "input_key": "height_m",
            "input_kind": "registry_concept",
            "candidate_key": "height",
            "context_key": null,
            "constant_value": null,
            "role": "measured standing height converted to metres",
            "required": true,
            "unit_code": "m",
            "note": "Initial permitted source Profile is height.standing.stadiometer. No self-reported or estimated substitution is allowed. Preserve the original Observation value, unit, timestamp, record/Profile identity and provenance; unit conversion does not create method equivalence."
          },
          {
            "input_key": "body_weight_kg",
            "input_kind": "registry_concept",
            "candidate_key": "body_weight",
            "context_key": null,
            "constant_value": null,
            "role": "measured body weight converted to kilograms",
            "required": true,
            "unit_code": "kg",
            "note": "Initial permitted source Profile is body_weight.scale_measured. No self-reported or future household-scale substitution is allowed. Preserve the original Observation value, unit, timestamp, record/Profile identity and provenance; unit conversion does not create method equivalence."
          }
        ],
        "source_reference_keys": [
          "src-loinc-bmi",
          "src-who-bmi",
          "src-wst428"
        ],
        "output_unit_policy": {
          "mode": "single_canonical",
          "canonical_unit": {
            "unit_code": "kg/m2",
            "unit_system": "UCUM",
            "status": "canonical",
            "conversion_rule": null,
            "conversion_verified": false,
            "note": "Canonical conventional BMI representation."
          },
          "note": "Preserve conventional kg/m2; do not silently normalize the ratio to unit 1."
        },
        "output_unit_note": "The output is kg/m2. Input conversion is mathematical only and never asserts method, protocol or device equivalence.",
        "computation_limitations": [
          "Both governed inputs and their complete provenance are required; missing inputs prohibit computation.",
          "The output retains the exact Height and Body Weight record/Profile identities, original values, original units, timestamps and provenance.",
          "Only height.standing.stadiometer and body_weight.scale_measured are permitted for the initial Profile.",
          "No self-reported or estimated input substitution is permitted.",
          "The output cannot have higher confidence than the source observations and methods.",
          "Adult interpretation is in scope; pediatric BMI-for-age and percentile interpretation are deferred."
        ]
      }
    }
  ],
  "use_evidence_claims": [],
  "system_relations": [],
  "external_mappings": [
    {
      "mapping_key": "loinc.body_mass_index",
      "mapping_scope": "concept",
      "system": "LOINC",
      "code": "39156-5",
      "version": null,
      "status": "mapped",
      "confidence": "high",
      "source_reference_keys": [
        "src-loinc-bmi"
      ],
      "note": "Concept-level BMI ratio mapping. The code has no method component and does not establish input Profile, protocol or device equivalence."
    }
  ],
  "interpretation_limitations": [
    "BMI is a derived index, not body-fat percentage, fat mass or body composition.",
    "BMI alone does not diagnose adiposity, obesity or any disease.",
    "Adult interpretation is the v0.1 scope; pediatric percentile and BMI-for-age interpretation are deferred.",
    "No WHO or China adult classification threshold is instantiated in this record.",
    "No personal target, moral judgment, treatment or action follows from the value.",
    "Input Profile, method, protocol, device, unit, timestamp and provenance determine comparability and trend continuity."
  ],
  "agent_permissions": {
    "permitted_uses": [
      "explain the BMI construct",
      "explain the formula and governed inputs",
      "explain units and conventional representation",
      "explain input provenance and missingness",
      "explain method and trend breakpoints",
      "request missing context"
    ],
    "prohibited_uses": [
      "infer missing Height or Body Weight inputs",
      "substitute self-reported or estimated inputs",
      "infer body-fat percentage or body composition",
      "diagnose obesity or disease",
      "moralize weight",
      "assign a personal target",
      "authorize treatment or action"
    ],
    "action_authorization": "none",
    "authorization_note": "Definition, formula, unit, provenance and missing-context explanation only; no diagnosis, personal target, treatment or action."
  },
  "personalized_target_support": {
    "support_status": "requires_governance",
    "prerequisites": [
      "authorized user context",
      "claim-specific evidence",
      "safety rules",
      "permission",
      "Personalized Longevity Protocol governance"
    ],
    "boundary_note": "Public Registry records contain no user-specific target value, target rationale, effective period or action linkage."
  },
  "lifecycle_relations": [],
  "governance_notes": [
    "Initial Profile is bmi.metric.standard with measured standing Height and measured scale Body Weight lineage only.",
    "No ReferenceContext, use-evidence claim, threshold, system relation, lifecycle relation or device mapping is authorized.",
    "No numeric-ID, allocation, path, lifecycle, runtime or retrieval authority is conferred by the C47 manifest; later record materialization requires separate governance."
  ],
  "governance_metadata": {
    "created_date": "2026-08-26",
    "last_modified_date": "2026-08-26",
    "reviewed_by": [],
    "reviewed_date": null,
    "last_source_check_date": "2026-08-26",
    "status_note": "Pilot B1 proposed Registry record blueprint; not source_verified, human_reviewed, active, published, runtime-enabled or retrieval-enabled."
  }
}
```

## Appendix B. Exact eGFR No-ID Blueprint

```json
{
  "candidate_key": "estimated_glomerular_filtration_rate",
  "registry_id": null,
  "namespace": "SC",
  "lifecycle_status": "proposed",
  "version": "v0.1",
  "canonical_name_zh": "估算肾小球滤过率",
  "canonical_name_en": "Estimated Glomerular Filtration Rate",
  "abbreviation": "eGFR",
  "aliases": [
    "eGFR"
  ],
  "legacy_codes": [],
  "information_type": "derived_score_index",
  "measurement_domain": "kidney_function_estimation",
  "construct_type": "derived_index",
  "construct_definition": "Equation-derived estimate of glomerular filtration under an explicitly named equation Profile and governed input contract.",
  "allowed_measurement_natures": [
    "derived",
    "reported"
  ],
  "value_type": "number",
  "unit_policy": {
    "mode": "single_canonical",
    "canonical_unit": {
      "unit_code": "mL/min/{1.73_m2}",
      "unit_system": "UCUM",
      "status": "canonical",
      "conversion_rule": null,
      "conversion_verified": false,
      "note": "Canonical indexed eGFR representation."
    },
    "note": "Indexed mL/min/{1.73_m2} is not unindexed mL/min and is not silently converted without separately governed body-surface-area inputs and an approved equation."
  },
  "source_references": [
    {
      "source_key": "src-niddk-egfr-adults",
      "title": "eGFR Equations for Adults",
      "organization_or_journal": "National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK)",
      "authors": [],
      "publication_date": null,
      "source_type": null,
      "source_role": "measurement_method",
      "supports": [
        "race-free CKD-EPI 2021 creatinine equation identity and constants",
        "adult age 18 and older applicability",
        "standardized serum creatinine input in mg/dL",
        "age and female/male equation parameter inputs",
        "indexed output in mL/min/1.73 m2",
        "serum creatinine conversion between umol/L and mg/dL using factor 88.4"
      ],
      "does_not_support": [
        "assay or platform equivalence",
        "measured GFR identity",
        "CKD diagnosis or stage",
        "automatic medication dosing",
        "personal target or action"
      ],
      "url": "https://www.niddk.nih.gov/research-funding/research-programs/kidney-clinical-research-epidemiology/laboratory/glomerular-filtration-rate-equations/adults",
      "doi": null,
      "pmid": null,
      "access_date": "2026-08-26",
      "verification_status": "content_verified",
      "note": "Official equation and input authority; page last reviewed May 2025."
    },
    {
      "source_key": "src-inker-2021",
      "title": "New Creatinine- and Cystatin C-Based Equations to Estimate GFR without Race",
      "organization_or_journal": "The New England Journal of Medicine",
      "authors": [],
      "publication_date": "2021-09-23",
      "source_type": null,
      "source_role": "validation_evidence",
      "supports": [
        "development and external validation of the 2021 race-free CKD-EPI creatinine equation",
        "adult study population",
        "equation limitations and estimation accuracy context"
      ],
      "does_not_support": [
        "every population or individual accuracy",
        "assay or platform equivalence",
        "CKD diagnosis or stage from one value",
        "personal target, medication dose or action"
      ],
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8822996/",
      "doi": "10.1056/NEJMoa2102953",
      "pmid": "34554658",
      "access_date": "2026-08-26",
      "verification_status": "content_verified",
      "note": "Lawfully accessible NIH author manuscript and PubMed metadata reviewed; no retraction identified in the audited metadata."
    },
    {
      "source_key": "src-loinc-egfr-2021",
      "title": "LOINC 98979-8, Glomerular filtration rate [Volume Rate/Area] in Serum, Plasma or Blood by Creatinine-based formula (CKD-EPI 2021)/1.73 sq M",
      "organization_or_journal": "Regenstrief / LOINC",
      "authors": [],
      "publication_date": null,
      "source_type": null,
      "source_role": "other_reviewed_role",
      "supports": [
        "profile-level identity for CKD-EPI 2021 creatinine-based indexed eGFR",
        "adult age 18 and older scope",
        "profile-level LOINC mapping 98979-8",
        "example UCUM output mL/min/{1.73_m2}"
      ],
      "does_not_support": [
        "measured GFR identity",
        "creatinine assay equivalence",
        "CKD diagnosis or stage",
        "automatic equation selection",
        "personal target or action"
      ],
      "url": "https://loinc.org/98979-8",
      "doi": null,
      "pmid": null,
      "access_date": "2026-08-26",
      "verification_status": "content_verified",
      "note": "Active LOINC term; the code was last updated in LOINC 2.79 and is equation-specific."
    },
    {
      "source_key": "src-ucum",
      "title": "The Unified Code for Units of Measure",
      "organization_or_journal": "Regenstrief Institute and UCUM Organization",
      "authors": [],
      "publication_date": "2024-06-17",
      "source_type": null,
      "source_role": "other_reviewed_role",
      "supports": [
        "UCUM unit syntax",
        "mL and time-unit syntax used in the indexed eGFR output expression"
      ],
      "does_not_support": [
        "equation identity",
        "measurement-method equivalence",
        "clinical interpretation",
        "personal target or action"
      ],
      "url": "https://ucum.org/ucum",
      "doi": null,
      "pmid": null,
      "access_date": "2026-08-26",
      "verification_status": "content_verified",
      "note": "UCUM Specification version 2.2; unit syntax authority only."
    },
    {
      "source_key": "src-kdigo-ckd-2024",
      "title": "KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease",
      "organization_or_journal": "Kidney Disease: Improving Global Outcomes (KDIGO)",
      "authors": [],
      "publication_date": null,
      "source_type": null,
      "source_role": "guideline_recommendation",
      "supports": [
        "current CKD evaluation and management context",
        "separation of estimated GFR from diagnosis, classification and management decisions",
        "limitations on applying guideline recommendations outside clinical context"
      ],
      "does_not_support": [
        "CKD-EPI 2021 equation identity or constants",
        "automatic CKD diagnosis or stage from one Registry value",
        "automatic medication dosing",
        "personal target or action"
      ],
      "url": "https://kdigo.org/guidelines/ckd-evaluation-and-management/",
      "doi": null,
      "pmid": null,
      "access_date": "2026-08-26",
      "verification_status": "content_verified",
      "note": "Official KDIGO page states publication in March 2024 and that the guideline remains the current global standard while a focused Chapter 3 update is underway; exact publication day is not asserted. Used only for scope and limitation context."
    },
    {
      "source_key": "src-niddk-egfr-age-overlap",
      "title": "eGFR Calculators for Adults & Pediatrics",
      "organization_or_journal": "National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK)",
      "authors": [],
      "publication_date": null,
      "source_type": null,
      "source_role": "other_reviewed_role",
      "supports": [
        "adult CKD-EPI calculator applicability at age 18 and older",
        "CKiD U25 calculator applicability from ages 1 to 25",
        "explicit age 18 to 25 overlap and recommendation to compare both estimates"
      ],
      "does_not_support": [
        "silent selection of one equation for ages 18 to 25",
        "cross-equation trend equivalence",
        "creation of a CKiD U25 Profile in this blueprint",
        "CKD diagnosis, medication dosing or personal action"
      ],
      "url": "https://www.niddk.nih.gov/health-information/professionals/clinical-tools-patient-management/kidney-disease/laboratory-evaluation/estimated-gfr-calculators/adults-pediatrics",
      "doi": null,
      "pmid": null,
      "access_date": "2026-08-26",
      "verification_status": "content_verified",
      "note": "Official applicability-context source; page last reviewed May 2024."
    }
  ],
  "definition_source_keys": [
    "src-niddk-egfr-adults",
    "src-loinc-egfr-2021"
  ],
  "profiles": [
    {
      "profile_key": "egfr.ckd_epi_2021_creatinine",
      "profile_status": "proposed",
      "measurement_nature": "derived",
      "source_modality": "calculated",
      "specimen_type": "serum_or_plasma",
      "matrix": "serum_or_plasma",
      "body_site": null,
      "collection_or_protocol_context": {
        "protocol_name": "race-free CKD-EPI 2021 creatinine equation",
        "protocol_version": "2021 creatinine",
        "measurement_window": "single governed calculation event",
        "timing_context": "Age and equation sex category resolved for the governed calculation time; source creatinine observation retained",
        "fasting_status": "unknown",
        "fasting_duration_hours": null,
        "posture": null,
        "rest_duration_minutes": null,
        "body_site": null,
        "laterality": "not_applicable",
        "repetition_count": null,
        "pace_or_effort_instruction": null,
        "context_tags": [
          "creatinine_profile_creatinine.serum_or_plasma.enzymatic_required",
          "standardized_creatinine_mg_dl_required",
          "age_years_required",
          "sex_at_birth_equation_parameter_required",
          "equation_identity_required",
          "origin_required",
          "calculation_timestamp_required"
        ],
        "note": "These tags govern future calculation and Observation provenance requirements; this Profile stores no user values."
      },
      "method": "race-free CKD-EPI 2021 creatinine equation for adults age 18 and older",
      "instrument_or_device": null,
      "vendor_or_model": null,
      "algorithm_version": "2021 creatinine",
      "accepted_units": [
        {
          "unit_code": "mL/min/{1.73_m2}",
          "unit_system": "UCUM",
          "status": "canonical",
          "conversion_rule": null,
          "conversion_verified": false,
          "note": "Canonical indexed eGFR output."
        }
      ],
      "canonicalization_rule": "Retain indexed mL/min/{1.73_m2}, equation identity, input record/Profile, original report, origin and calculation provenance; no silent rounding, capping or unindexing.",
      "method_comparability_status": "not_comparable",
      "trend_breakpoint_note": "Equation identity/version, creatinine Profile/method/platform, unit conversion, age-context handling, sex-parameter handling, reporting origin, rounding or capping changes break trend continuity.",
      "cross_platform_comparison_prohibited": true,
      "reference_contexts": [],
      "external_mappings": [
        {
          "mapping_key": "loinc.egfr.ckd_epi_2021_creatinine",
          "mapping_scope": "profile",
          "system": "LOINC",
          "code": "98979-8",
          "version": null,
          "status": "mapped",
          "confidence": "high",
          "source_reference_keys": [
            "src-loinc-egfr-2021"
          ],
          "note": "Equation-specific Profile mapping for CKD-EPI 2021 creatinine-based indexed eGFR in serum, plasma or blood. It is not a measured-GFR or CKD-stage code."
        }
      ],
      "device_mappings": [],
      "profile_limitations": [
        "Population scope is adults age 18 and older.",
        "Ages 18 to 25 overlap with CKiD U25 applicability; both estimates should be considered and one equation must not be silently selected.",
        "CKiD U25 is deferred and is not a second Profile in this blueprint.",
        "Only creatinine.serum_or_plasma.enzymatic is permitted as the initial Registry input Profile.",
        "Standardized serum creatinine must be supplied in mg/dL; umol/L conversion does not establish assay equivalence.",
        "Missing creatinine, age or governed equation sex category prohibits calculation.",
        "sex_at_birth resolves only the published binary female/male equation parameter; it is not gender-identity inference.",
        "Nonbinary, intersex, unknown or otherwise uncovered categories are not forcibly mapped and require separately governed handling.",
        "Laboratory-reported eGFR and locally derived eGFR retain distinct origin and provenance.",
        "Silent rounding, capping, unindexing and cross-equation trend continuity are prohibited.",
        "Estimated GFR is not measured GFR, creatinine clearance, raw creatinine, CKD diagnosis, CKD stage, medication dosing action or a personal target."
      ],
      "source_reference_keys": [
        "src-niddk-egfr-adults",
        "src-inker-2021",
        "src-loinc-egfr-2021",
        "src-ucum",
        "src-kdigo-ckd-2024",
        "src-niddk-egfr-age-overlap"
      ],
      "derived_computation": {
        "computation_key": "egfr.ckd_epi_2021_creatinine",
        "equation_name": "CKD-EPI 2021 Creatinine Equation",
        "equation_version": "2021 creatinine",
        "formula_or_equation": "142 * min(scr_mg_dl / k, 1)^alpha * max(scr_mg_dl / k, 1)^(-1.200) * 0.9938^age_years * sex_factor, where female: k = 0.7, alpha = -0.241, sex_factor = 1.012; male: k = 0.9, alpha = -0.302, sex_factor = 1",
        "inputs": [
          {
            "input_key": "scr_mg_dl",
            "input_kind": "registry_concept",
            "candidate_key": "creatinine",
            "context_key": null,
            "constant_value": null,
            "role": "standardized serum creatinine used by the named equation",
            "required": true,
            "unit_code": "mg/dL",
            "note": "Initial reviewed Profile is creatinine.serum_or_plasma.enzymatic. Preserve the source observation, original unit, specimen, assay/platform, traceability, timestamp and provenance. Convert umol/L to mg/dL only by the governed 88.4 rule; conversion does not establish assay equivalence. No future Jaffe Profile is silently substituted."
          },
          {
            "input_key": "age_years",
            "input_kind": "user_context",
            "candidate_key": null,
            "context_key": "age_years",
            "constant_value": null,
            "role": "age in years at the governed calculation time",
            "required": true,
            "unit_code": "a",
            "note": "Age is required at calculation time and is not inferred. The Profile applies at age 18 and older; ages 18 to 25 require the explicit overlap qualification and no silent equation choice."
          },
          {
            "input_key": "sex_at_birth",
            "input_kind": "categorical_parameter",
            "candidate_key": null,
            "context_key": "sex_at_birth",
            "constant_value": null,
            "role": "binary equation parameter required by the published equation",
            "required": true,
            "unit_code": null,
            "note": "sex_at_birth is the governed context source for resolving the published female/male parameter only. It is not gender-identity inference; it is never inferred from name, appearance or proxy data. Missing, nonbinary, intersex, unknown or otherwise uncovered categories are not forcibly mapped and prohibit calculation pending separately governed handling."
          }
        ],
        "source_reference_keys": [
          "src-niddk-egfr-adults",
          "src-inker-2021"
        ],
        "output_unit_policy": {
          "mode": "single_canonical",
          "canonical_unit": {
            "unit_code": "mL/min/{1.73_m2}",
            "unit_system": "UCUM",
            "status": "canonical",
            "conversion_rule": null,
            "conversion_verified": false,
            "note": "Canonical indexed eGFR output."
          },
          "note": "The output remains indexed to 1.73 m2; unindexed mL/min is not an unconditional equivalent."
        },
        "output_unit_note": "Registry-level silent rounding and capping are prohibited. Unindexing is prohibited without separately governed body-surface-area inputs and an approved equation. Preserve the original reported display and local computation provenance.",
        "computation_limitations": [
          "All three required inputs and their governed provenance are mandatory; missing inputs prohibit computation.",
          "The equation is race-free and contains no race coefficient.",
          "The population scope is adults age 18 and older.",
          "For ages 18 to 25, NIDDK guidance overlaps with CKiD U25; both estimates should be considered and one equation must not be silently selected.",
          "Results from different equations are not merged into one continuous trend and disagreement is not treated as data error.",
          "Only creatinine.serum_or_plasma.enzymatic is permitted as the initial Registry input Profile.",
          "Creatinine unit conversion does not establish assay or platform equivalence.",
          "Laboratory-reported and locally derived eGFR retain distinct origin, source report, equation identity/version, input observation, context and calculation timestamp.",
          "Silent rounding, silent capping and silent unindexing are prohibited.",
          "The estimate is not measured GFR, creatinine clearance, CKD diagnosis, CKD stage, medication dosing action or a personal target."
        ]
      }
    }
  ],
  "use_evidence_claims": [],
  "system_relations": [],
  "external_mappings": [],
  "interpretation_limitations": [
    "This concept is equation-derived and distinct from measured GFR, creatinine clearance and raw serum creatinine.",
    "This Profile is the CKD-EPI 2021 creatinine equation only; cystatin-C-only and creatinine-plus-cystatin-C equations are deferred Profiles.",
    "The value alone does not diagnose CKD, assign a CKD stage, determine medication dosing or authorize action.",
    "Ages 18 to 25 require explicit CKiD U25 overlap handling and no silent equation selection.",
    "Equation, input method, assay/platform, origin, rounding, capping and indexing differences break comparability.",
    "No personal target is stored or generated."
  ],
  "agent_permissions": {
    "permitted_uses": [
      "explain the eGFR construct",
      "explain the named equation and version",
      "explain required inputs, units and origin",
      "explain the age 18 to 25 overlap",
      "explain equation, method and trend breakpoints",
      "request missing context"
    ],
    "prohibited_uses": [
      "infer age or the equation sex parameter",
      "infer gender identity",
      "force-map nonbinary, intersex or unknown categories",
      "silently choose an equation",
      "merge different equations into one continuous trend",
      "diagnose CKD or assign CKD stage",
      "recommend medication dose or treatment",
      "generate a personal target",
      "authorize action"
    ],
    "action_authorization": "separately_gated",
    "authorization_note": "Equation, input, unit, origin, applicability and missing-context explanation only; no diagnosis, staging, dosing, treatment, personal target or action."
  },
  "personalized_target_support": {
    "support_status": "requires_governance",
    "prerequisites": [
      "authorized user context",
      "claim-specific evidence",
      "safety rules",
      "permission",
      "Personalized Longevity Protocol governance"
    ],
    "boundary_note": "Public Registry records contain no user-specific target value, target rationale, effective period or action linkage."
  },
  "lifecycle_relations": [],
  "governance_notes": [
    "Initial Profile is egfr.ckd_epi_2021_creatinine for adults age 18 and older.",
    "Ages 18 to 25 overlap with CKiD U25 guidance; no silent equation selection or cross-equation trend continuity is permitted.",
    "CKiD U25, cystatin-C-only, creatinine-plus-cystatin-C, measured GFR and creatinine clearance are not added as Profiles here.",
    "No China-specific equation identity source or local mapping is asserted; China laboratory reporting context remains pending and does not block this proposed Profile.",
    "No ReferenceContext, use-evidence claim, threshold, system relation, lifecycle relation or device mapping is authorized.",
    "No numeric-ID, allocation, path, lifecycle, runtime or retrieval authority is conferred by the C47 manifest; later record materialization requires separate governance."
  ],
  "governance_metadata": {
    "created_date": "2026-08-26",
    "last_modified_date": "2026-08-26",
    "reviewed_by": [],
    "reviewed_date": null,
    "last_source_check_date": "2026-08-26",
    "status_note": "Pilot B1 proposed Registry record blueprint; not source_verified, human_reviewed, active, published, runtime-enabled or retrieval-enabled."
  }
}
```
