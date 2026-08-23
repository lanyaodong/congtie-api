# Registry First Wave Pilot A Proposed-Record Authoring Manifest v0.1

- Status: Draft / Founder Review Pending / Numeric IDs and Record Creation Not Authorized
- Prepared date: 2026-08-22
- Repository anchor: `9fdd4a16b8430e3553ff53d08a55ab4c05edea47`
- Parent plan: `registry_first_wave_12_record_boundary_and_source_verification_plan.v0.1.md`
- Scope: authoring manifest only; no Registry record, profile record, numeric ID, lifecycle transition, runtime, retrieval, publication, database, API, Observation storage, or Service Panel is authorized

## 1. Purpose

This manifest defines the exact minimum content proposed for the first four Registry authoring records after a separate Founder gate. It freezes the Pilot A candidate set and profile boundaries so a later controlled numeric-ID allocation can occur without encoding body system, priority, dependency, or Pilot order into IDs.

Nothing in this document is a Registry record. Candidate keys and profile keys are authoring references only. The permitted first lifecycle value, if record creation is later authorized, is `proposed`.

## 2. Governance Baseline

```text
boundary approved
-> exact proposed-record authoring manifest approved
-> controlled numeric-ID allocation manifest
-> separately authorized proposed-record creation
```

Founder selected Option B for numeric-ID timing. Namespace is frozen; numeric values are not. IDs must be monotonic and non-semantic. Numeric IDs assigned in this task = 0. Allocation manifests created in this task = 0. Record files created in this task = 0.

Source statuses below describe source review in the approved planning document. They do not set a Registry concept or profile lifecycle to `source_verified`.

## 3. Pilot A Frozen Set

| Order | Candidate Key | Canonical Name zh | Canonical Name en | Namespace | First Lifecycle Target |
|---:|---|---|---|---|---|
| 1 | `height` | 身高 | Height | ME | proposed only |
| 2 | `body_weight` | 体重 | Body Weight | ME | proposed only |
| 3 | `creatinine` | 肌酐 | Creatinine | BM | proposed only |
| 4 | `heart_rate` | 心率 | Heart Rate | ME | proposed only |

No candidate may be added, removed, or substituted without a new Founder gate.


## 4. Schema-Exact Authoring Rule

The governing Schema is `schemas/biomarker_measurement_registry_schema_v0.1.json`. Every future record field is fixed below as an exact literal, exact empty array or `null`, a named exact object, or one of two controlled dynamic values: the approved numeric Registry ID and the actual controlled record-creation date.

C28 uses uppercase planning labels. The Schema requires lowercase `source_key` values. This exact mapping changes key format only:

| C28 Label | Future JSON Key | C28 Label | Future JSON Key |
|---|---|---|---|
| `SRC-LOINC-HEIGHT` | `src-loinc-height` | `SRC-LOINC-WEIGHT` | `src-loinc-weight` |
| `SRC-WHO-STEPS` | `src-who-steps` | `SRC-WST424` | `src-wst424` |
| `SRC-UCUM` | `src-ucum` | `SRC-LOINC-CREAT-MASS` | `src-loinc-creat-mass` |
| `SRC-LOINC-CREAT-MOLAR` | `src-loinc-creat-molar` | `SRC-NIST-CREAT` | `src-nist-creat` |
| `SRC-CREAT-METHOD-2020` | `src-creat-method-2020` | `SRC-WST4045` | `src-wst4045` |
| `SRC-LOINC-HR` | `src-loinc-hr` | `SRC-HR-PPG-2020` | `src-hr-ppg-2020` |
| `SRC-INTERLIVE-HR` | `src-interlive-hr` |  |  |

## 5. Common Proposed-Record Objects

~~~yaml
registry_id: injected only from a future Founder-approved allocation manifest
lifecycle_status: proposed
version: v0.1
use_evidence_claims: []
system_relations: []
lifecycle_relations: []
governance_metadata:
  created_date: actual controlled record-creation date
  last_modified_date: same as created_date
  reviewed_by: []
  reviewed_date: null
  last_source_check_date: 2026-08-22
  status_note: Pilot A proposed Registry record; not source_verified, human_reviewed, active, published, runtime-enabled or retrieval-enabled.
personalized_target_support:
  support_status: requires_governance
  prerequisites: [authorized user context, claim-specific evidence, safety rules, permission, Personalized Longevity Protocol governance]
  boundary_note: Public Registry records contain no user-specific target value, target rationale, effective period or action linkage.
~~~

Every initial profile uses `profile_status: proposed`, `reference_contexts: []`, `device_mappings: []`, and `derived_computation: null`.

## 6. Required Field Coverage

### 6.1 RegistryConcept required fields: 25/25

| Field | Height | Body Weight | Creatinine | Heart Rate |
|---|---|---|---|---|
| `candidate_key` | `height` | `body_weight` | `creatinine` | `heart_rate` |
| `registry_id` | controlled injection | controlled injection | controlled injection | controlled injection |
| `namespace` | `ME` | `ME` | `BM` | `ME` |
| `lifecycle_status` | `proposed` | `proposed` | `proposed` | `proposed` |
| `canonical_name_zh` | `身高` | `体重` | `肌酐` | `心率` |
| `canonical_name_en` | `Height` | `Body Weight` | `Creatinine` | `Heart Rate` |
| `aliases` | `[standing height]` | `[weight]` | `[]` | `[]` |
| `legacy_codes` | `[]` | `[]` | `[]` | `[]` |
| `information_type` | `physiological_measurement` | `physiological_measurement` | `laboratory_biomarker` | `physiological_measurement` |
| `construct_type` | `anthropometric_measurement` | `anthropometric_measurement` | `analyte` | `physiological_measurement` |
| `construct_definition` | exact blueprint | exact blueprint | exact blueprint | exact blueprint |
| `allowed_measurement_natures` | `[measured]` | `[measured]` | `[measured]` | `[measured, estimated]` |
| `value_type` | `number` | `number` | `number` | `number` |
| `unit_policy` | `height_unit` | `weight_unit` | `creatinine_unit` | `heart_rate_unit` |
| `source_references` | exact 4-source pool | exact 4-source pool | exact 6-source pool | exact 4-source pool |
| `definition_source_keys` | `[src-loinc-height]` | `[src-loinc-weight]` | `[src-loinc-creat-mass, src-loinc-creat-molar]` | `[src-loinc-hr]` |
| `profiles` | 1 exact profile | 1 exact profile | 1 exact profile | 2 exact profiles |
| `use_evidence_claims` | `[]` | `[]` | `[]` | `[]` |
| `system_relations` | `[]` | `[]` | `[]` | `[]` |
| `external_mappings` | `[loinc.height]` | `[loinc.body_weight]` | `[]` | `[loinc.heart_rate]` |
| `interpretation_limitations` | exact array | exact array | exact array | exact array |
| `agent_permissions` | exact object | exact object | exact object | exact object |
| `personalized_target_support` | common exact object | common exact object | common exact object | common exact object |
| `lifecycle_relations` | `[]` | `[]` | `[]` | `[]` |
| `governance_metadata` | common exact object | common exact object | common exact object | common exact object |

Optional RegistryConcept fields are fixed: `version=v0.1`; abbreviations are `null`, `null`, `Cr`, `HR`; measurement domains are `anthropometry`, `anthropometry`, `laboratory_chemistry`, `cardiovascular_physiology`; each blueprint supplies an exact `governance_notes` array.

### 6.2 MeasurementProfile required fields: 12/12

| Field | Height | Body Weight | Creatinine | HR Spot | HR Wearable |
|---|---|---|---|---|---|
| `profile_key` | `height.standing.stadiometer` | `body_weight.scale_measured` | `creatinine.serum_or_plasma.enzymatic` | `heart_rate.spot_clinical` | `heart_rate.wearable_ppg_time_series_estimate` |
| `profile_status` | `proposed` | `proposed` | `proposed` | `proposed` | `proposed` |
| `measurement_nature` | `measured` | `measured` | `measured` | `measured` | `estimated` |
| `source_modality` | `clinical_device` | `clinical_device` | `laboratory` | `clinical_device` | `wearable` |
| `method_comparability_status` | `context_dependent` | `context_dependent` | `context_dependent` | `context_dependent` | `not_comparable` |
| `accepted_units` | `height_units` | `weight_units` | `creatinine_units` | `heart_rate_units` | `heart_rate_units` |
| `reference_contexts` | `[]` | `[]` | `[]` | `[]` | `[]` |
| `external_mappings` | `[]` | `[]` | two exact mappings | `[]` | `[]` |
| `device_mappings` | `[]` | `[]` | `[]` | `[]` | `[]` |
| `profile_limitations` | exact array | exact array | exact array | exact array | exact array |
| `source_reference_keys` | `[src-who-steps, src-wst424]` | `[src-who-steps, src-wst424]` | `[src-nist-creat, src-creat-method-2020, src-wst4045]` | `[]` | `[src-hr-ppg-2020, src-interlive-hr]` |
| `derived_computation` | `null` | `null` | `null` | `null` | `null` |

All optional Profile fields are fixed in the blueprints. Unresolved authoring fields = 0.

## 7. Exact SourceReference Objects

All sources use `authors: []`, `publication_date: null`, `source_type: null`, `access_date: "2026-08-22"`, and `verification_status: "content_verified"`. The table supplies every other SourceReference field. Semicolon-separated supports and exclusions become exact string arrays.

| Key | Title | Organization / Journal | Role | Supports | Does Not Support | URL | DOI | PMID | Note |
|---|---|---|---|---|---|---|---|---|---|
| `src-ucum` | UCUM Specification | Regenstrief Institute | `other_reviewed_role` | UCUM unit syntax | method equivalence; clinical interpretation; personal targets | https://ucum.org/ucum | `null` | `null` | Unit syntax authority only. |
| `src-loinc-height` | LOINC 8302-2, Body height | Regenstrief / LOINC | `other_reviewed_role` | Body height terminology; LOINC mapping | pediatric interpretation; self-report equivalence; personal targets | https://loinc.org/8302-2 | `null` | `null` | Terminology and code authority. |
| `src-loinc-weight` | LOINC 29463-7, Body weight | Regenstrief / LOINC | `other_reviewed_role` | Body weight terminology; LOINC mapping | body composition; change attribution; self-report equivalence | https://loinc.org/29463-7 | `null` | `null` | Terminology and code authority. |
| `src-who-steps` | WHO STEPwise Approach to NCD Risk Factor Surveillance manuals | World Health Organization | `measurement_method` | standing-height protocol; measured-weight protocol | every device; self-report equivalence; personal targets | https://www.who.int/teams/noncommunicable-diseases/surveillance/systems-tools/steps/manuals | `null` | `null` | International method source. |
| `src-wst424` | WS/T 424-2013, Anthropometric methods in population health monitoring | National Health Commission of China | `measurement_method` | China height/weight protocols | global thresholds; self-report equivalence | https://www.nhc.gov.cn/wjw/yingyang/201308/1f27caef0b22493e93a1da8aec2cd63a.shtml | `null` | `null` | China method source. |
| `src-loinc-creat-mass` | LOINC 2160-0, Creatinine [Mass/volume] in Serum or Plasma | Regenstrief / LOINC | `other_reviewed_role` | mass-concentration terminology/mapping | enzymatic identity; kidney-function equivalence | https://loinc.org/2160-0 | `null` | `null` | Property representation. |
| `src-loinc-creat-molar` | LOINC 14682-9, Creatinine [Moles/volume] in Serum or Plasma | Regenstrief / LOINC | `other_reviewed_role` | molar-concentration terminology/mapping | enzymatic identity; kidney-function equivalence | https://loinc.org/14682-9 | `null` | `null` | Property representation. |
| `src-nist-creat` | Development of Reference Measurement Procedures and Reference Materials for Creatinine | NIST | `measurement_method` | reference measurement; IDMS traceability | every-assay equivalence; diagnosis | https://www.nist.gov/programs-projects/development-reference-measurement-procedures-and-reference-materials-creatinine | `null` | `null` | Traceability source. |
| `src-creat-method-2020` | Clinical and Analytical Impact of Moving from Jaffe to Enzymatic Serum Creatinine Methodology | Journal of Applied Laboratory Medicine | `validation_evidence` | method comparability; interference | universal continuity; diagnosis | `null` | `10.1093/jalm/jfaa053` | `32447368` | No unverified author/date added. |
| `src-wst4045` | WS/T 404.5-2015, Clinical common biochemical test reference intervals, Part 5: serum urea and creatinine | National Health Commission of China | `reference_interval_source` | China interval/method context | universal interval; kidney-function equivalence | https://www.nhc.gov.cn/ewebeditor/uploadfile/2015/05/20150504152412571.pdf | `null` | `null` | No numeric ReferenceContext initially. |
| `src-loinc-hr` | LOINC 8867-4, Heart rate | Regenstrief / LOINC | `other_reviewed_role` | Heart rate terminology/mapping | spot method; PPG-ECG equivalence; rhythm diagnosis | https://loinc.org/8867-4 | `null` | `null` | Terminology and code authority. |
| `src-hr-ppg-2020` | Validity of wrist-worn photoplethysmography devices to measure heart rate | Journal of Sports Sciences | `validation_evidence` | PPG limitations; activity dependence | ECG equivalence; all devices; rhythm diagnosis | `null` | `10.1080/02640414.2020.1767348` | `32552580` | Wearable validation. |
| `src-interlive-hr` | Recommendations for determining the validity of consumer wearable heart rate devices | INTERLIVE Network / British Journal of Sports Medicine | `validation_evidence` | wearable validation framework | device/firmware/algorithm equivalence; diagnosis | `null` | `null` | `33397674` | Validation framework. |

Exact pools:

- Height: `[src-loinc-height, src-who-steps, src-wst424, src-ucum]`
- Body Weight: `[src-loinc-weight, src-who-steps, src-wst424, src-ucum]`
- Creatinine: `[src-loinc-creat-mass, src-loinc-creat-molar, src-nist-creat, src-creat-method-2020, src-wst4045, src-ucum]`
- Heart Rate: `[src-loinc-hr, src-hr-ppg-2020, src-interlive-hr, src-ucum]`

`SRC-NHC-LITERACY-2024` is excluded from the initial Heart Rate source pool.

## 8. Exact Mapping Objects

~~~yaml
concept:
  height: {mapping_key: loinc.height, mapping_scope: concept, system: LOINC, code: 8302-2, version: null, status: mapped, confidence: high, source_reference_keys: [src-loinc-height], note: Protocol provenance remains in the Profile.}
  body_weight: {mapping_key: loinc.body_weight, mapping_scope: concept, system: LOINC, code: 29463-7, version: null, status: mapped, confidence: high, source_reference_keys: [src-loinc-weight], note: Protocol provenance remains in the Profile.}
  heart_rate: {mapping_key: loinc.heart_rate, mapping_scope: concept, system: LOINC, code: 8867-4, version: null, status: mapped, confidence: high, source_reference_keys: [src-loinc-hr], note: Modality and window remain in the Profile.}
profile:
  creatinine_mass: {mapping_key: loinc.creatinine.mass, mapping_scope: profile, system: LOINC, code: 2160-0, version: null, status: mapped, confidence: high, source_reference_keys: [src-loinc-creat-mass], note: Code defines mass representation; enzymatic provenance remains in the Profile.}
  creatinine_molar: {mapping_key: loinc.creatinine.molar, mapping_scope: profile, system: LOINC, code: 14682-9, version: null, status: mapped, confidence: high, source_reference_keys: [src-loinc-creat-molar], note: Code defines molar representation; enzymatic provenance remains in the Profile.}
~~~

Creatinine concept mappings = `[]`. Height, Weight, HR spot, and HR wearable profile mappings = `[]`. Device mappings = `[]` for all profiles.

## 9. Exact Unit Objects

~~~yaml
height_unit:
  mode: single_canonical
  canonical_unit: {unit_code: cm, unit_system: UCUM, status: canonical, conversion_rule: null, conversion_verified: false, note: Canonical representation.}
  note: Conversion does not establish protocol/instrument equivalence.
height_units:
  - {unit_code: cm, unit_system: UCUM, status: canonical, conversion_rule: null, conversion_verified: false, note: Canonical.}
  - {unit_code: m, unit_system: UCUM, status: accepted, conversion_rule: "value_m * 100 = value_cm", conversion_verified: true, note: Exact conversion.}
  - {unit_code: "[in_i]", unit_system: UCUM, status: accepted, conversion_rule: "value_[in_i] * 2.54 = value_cm", conversion_verified: true, note: Exact international-inch conversion.}
weight_unit:
  mode: single_canonical
  canonical_unit: {unit_code: kg, unit_system: UCUM, status: canonical, conversion_rule: null, conversion_verified: false, note: Canonical representation.}
  note: Conversion does not establish scale/protocol equivalence.
weight_units:
  - {unit_code: kg, unit_system: UCUM, status: canonical, conversion_rule: null, conversion_verified: false, note: Canonical.}
  - {unit_code: "[lb_av]", unit_system: UCUM, status: accepted, conversion_rule: "value_[lb_av] * 0.45359237 = value_kg", conversion_verified: true, note: Exact avoirdupois conversion.}
creatinine_unit:
  mode: single_canonical
  canonical_unit: {unit_code: umol/L, unit_system: UCUM, status: canonical, conversion_rule: null, conversion_verified: false, note: Canonical representation.}
  note: Conversion does not establish assay/platform comparability.
creatinine_units:
  - {unit_code: umol/L, unit_system: UCUM, status: canonical, conversion_rule: null, conversion_verified: false, note: Canonical.}
  - {unit_code: mg/dL, unit_system: UCUM, status: accepted, conversion_rule: "value_mg/dL * 88.4 = value_umol/L", conversion_verified: true, note: Reviewed conversion; assay comparability remains separate.}
heart_rate_unit:
  mode: single_canonical
  canonical_unit: {unit_code: /min, unit_system: UCUM, status: canonical, conversion_rule: null, conversion_verified: false, note: Canonical representation.}
  note: bpm is a UI label for /min, not another unit.
heart_rate_units:
  - {unit_code: /min, unit_system: UCUM, status: canonical, conversion_rule: null, conversion_verified: false, note: Canonical for both profiles.}
~~~

## 10. Exact ProtocolContext Objects

These are Profile requirements for future Observation metadata, not stored user observations.

| Field | Height | Body Weight | Creatinine | HR Spot | HR Wearable |
|---|---|---|---|---|---|
| `protocol_name` | standing height with stadiometer | calibrated scale body-weight measurement | serum or plasma enzymatic creatinine assay | device-based spot heart-rate measurement | wearable PPG heart-rate time series |
| `protocol_version` | `null` | `null` | `null` | `null` | `null` |
| `measurement_window` | single measurement event | single measurement event | specimen collection event | spot | time_series |
| `timing_context` | `null` | `null` | `null` | `null` | `null` |
| `fasting_status` | `not_applicable` | `unknown` | `unknown` | `not_applicable` | `not_applicable` |
| `fasting_duration_hours` | `null` | `null` | `null` | `null` | `null` |
| `posture` | `standing` | `standing` | `null` | `null` | `null` |
| `rest_duration_minutes` | `null` | `null` | `null` | `null` | `null` |
| `body_site` | `null` | `null` | `null` | `null` | `null` |
| `laterality` | `not_applicable` | `not_applicable` | `not_applicable` | `not_applicable` | `not_applicable` |
| `repetition_count` | `null` | `null` | `null` | `null` | `null` |
| `pace_or_effort_instruction` | `null` | `null` | `null` | `null` | `null` |
| `context_tags` | `[shoes_recorded, head_position_recorded, stable_surface]` | `[clothing_recorded, footwear_recorded, time_of_day_recorded, scale_recorded]` | `[specimen_recorded, assay_recorded, idms_traceability_recorded]` | `[posture_required_at_observation, rest_required_at_observation, device_method_required_at_observation, measurement_window_required_at_observation]` | `[device_required, firmware_required_if_available, algorithm_version_required_if_available, aggregation_window_required, activity_context_required, artifact_handling_required_if_available]` |
| `note` | preserve protocol/instrument | never assume fasting/post-void | preserve specimen/assay/platform/traceability | Observation supplies posture/rest/device/window | Observation supplies device/firmware/algorithm/aggregation/activity/artifact context |

## 11. Exact Profile Decisions

| Profile | Nature | Modality | Method | Instrument | Comparability | Cross-Platform Prohibited |
|---|---|---|---|---|---|---:|
| `height.standing.stadiometer` | `measured` | `clinical_device` | standing height measured with a stadiometer | stadiometer | `context_dependent` | false |
| `body_weight.scale_measured` | `measured` | `clinical_device` | body weight measured with a calibrated scale | weighing scale | `context_dependent` | false |
| `creatinine.serum_or_plasma.enzymatic` | `measured` | `laboratory` | enzymatic creatinine assay with recorded IDMS traceability status | `null` | `context_dependent` | true |
| `heart_rate.spot_clinical` | `measured` | `clinical_device` | device-based spot heart-rate measurement | clinical heart-rate device | `context_dependent` | true |
| `heart_rate.wearable_ppg_time_series_estimate` | `estimated` | `wearable` | PPG-derived heart-rate estimate | wearable PPG device | `not_comparable` | true |

Manual pulse count is excluded from initial HR. PPG is not ECG. Household-scale, self-report, Jaffe, HR summary/zone/recovery profiles remain deferred and absent from the initial blueprints.

## 12. Exact Blueprint — Height

~~~yaml
candidate_key: height
registry_id: controlled allocation-manifest injection
namespace: ME
lifecycle_status: proposed
version: v0.1
canonical_name_zh: 身高
canonical_name_en: Height
abbreviation: null
aliases: [standing height]
legacy_codes: []
information_type: physiological_measurement
measurement_domain: anthropometry
construct_type: anthropometric_measurement
construct_definition: Vertical body stature measured under an explicit standing-height protocol.
allowed_measurement_natures: [measured]
value_type: number
unit_policy: height_unit
source_references: [src-loinc-height, src-who-steps, src-wst424, src-ucum exact objects]
definition_source_keys: [src-loinc-height]
profiles:
  - {profile_key: height.standing.stadiometer, profile_status: proposed, measurement_nature: measured, source_modality: clinical_device, specimen_type: null, matrix: null, body_site: null, collection_or_protocol_context: Height column in Section 10, method: standing height measured with a stadiometer, instrument_or_device: stadiometer, vendor_or_model: null, algorithm_version: null, accepted_units: height_units, canonicalization_rule: "Retain original value/unit; convert m or [in_i] only by height_units rules.", method_comparability_status: context_dependent, trend_breakpoint_note: "Protocol, instrument, posture, or footwear change may break trends.", cross_platform_comparison_prohibited: false, reference_contexts: [], external_mappings: [], device_mappings: [], profile_limitations: [Quality depends on recorded protocol/instrument., Self-report excluded., Cross-instrument comparison retains provenance.], source_reference_keys: [src-who-steps, src-wst424], derived_computation: null}
use_evidence_claims: []
system_relations: []
external_mappings: [loinc.height]
interpretation_limitations: [Requires posture protocol and instrument context., Self-report is not measured standing height., Pediatric interpretation is deferred.]
agent_permissions:
  permitted_uses: [explain construct/protocol, explain units, explain breakpoints, explain BMI lineage, request missing context]
  prohibited_uses: [infer height, equate self-report, diagnose growth disorder, generate personal target, authorize action]
  action_authorization: none
  authorization_note: Explanation and context completion only; no diagnosis, personal target, or action.
personalized_target_support: common exact object
lifecycle_relations: []
governance_notes: [Initial profile is standing stadiometer measurement., Self-report and pediatric interpretation are deferred.]
governance_metadata: common controlled object
~~~

## 13. Exact Blueprint — Body Weight

~~~yaml
candidate_key: body_weight
registry_id: controlled allocation-manifest injection
namespace: ME
lifecycle_status: proposed
version: v0.1
canonical_name_zh: 体重
canonical_name_en: Body Weight
abbreviation: null
aliases: [weight]
legacy_codes: []
information_type: physiological_measurement
measurement_domain: anthropometry
construct_type: anthropometric_measurement
construct_definition: Human body weight measured with a scale under recorded protocol and device context.
allowed_measurement_natures: [measured]
value_type: number
unit_policy: weight_unit
source_references: [src-loinc-weight, src-who-steps, src-wst424, src-ucum exact objects]
definition_source_keys: [src-loinc-weight]
profiles:
  - {profile_key: body_weight.scale_measured, profile_status: proposed, measurement_nature: measured, source_modality: clinical_device, specimen_type: null, matrix: null, body_site: null, collection_or_protocol_context: Body Weight column in Section 10, method: body weight measured with a calibrated scale, instrument_or_device: weighing scale, vendor_or_model: null, algorithm_version: null, accepted_units: weight_units, canonicalization_rule: "Retain original value/unit; convert [lb_av] only by weight_units rule.", method_comparability_status: context_dependent, trend_breakpoint_note: "Scale, calibration, clothing, or protocol change may break trends.", cross_platform_comparison_prohibited: false, reference_contexts: [], external_mappings: [], device_mappings: [], profile_limitations: [Scale and protocol context matter., Fasting/post-void never assumed., Body composition and self-report excluded.], source_reference_keys: [src-who-steps, src-wst424], derived_computation: null}
use_evidence_claims: []
system_relations: []
external_mappings: [loinc.body_weight]
interpretation_limitations: [Body weight is not body composition., Short-term change does not identify cause., Scale/calibration/protocol changes may break trends.]
agent_permissions:
  permitted_uses: [explain construct/protocol, explain units, explain breakpoints, explain BMI lineage, request missing context]
  prohibited_uses: [infer composition, assign change cause, equate self-report, diagnose/prescribe, generate personal target, authorize action]
  action_authorization: none
  authorization_note: Explanation and context completion only; no diagnosis, prescription, personal target, or action.
personalized_target_support: common exact object
lifecycle_relations: []
governance_notes: [Initial profile is calibrated-scale measurement., Household-scale-specific and self-reported profiles are deferred.]
governance_metadata: common controlled object
~~~

## 14. Exact Blueprint — Creatinine

~~~yaml
candidate_key: creatinine
registry_id: controlled allocation-manifest injection
namespace: BM
lifecycle_status: proposed
version: v0.1
canonical_name_zh: 肌酐
canonical_name_en: Creatinine
abbreviation: Cr
aliases: []
legacy_codes: []
information_type: laboratory_biomarker
measurement_domain: laboratory_chemistry
construct_type: analyte
construct_definition: Creatinine concentration in serum or plasma under a specified analytical method.
allowed_measurement_natures: [measured]
value_type: number
unit_policy: creatinine_unit
source_references: [src-loinc-creat-mass, src-loinc-creat-molar, src-nist-creat, src-creat-method-2020, src-wst4045, src-ucum exact objects]
definition_source_keys: [src-loinc-creat-mass, src-loinc-creat-molar]
profiles:
  - {profile_key: creatinine.serum_or_plasma.enzymatic, profile_status: proposed, measurement_nature: measured, source_modality: laboratory, specimen_type: serum_or_plasma, matrix: serum_or_plasma, body_site: null, collection_or_protocol_context: Creatinine column in Section 10, method: enzymatic creatinine assay with recorded IDMS traceability status, instrument_or_device: null, vendor_or_model: null, algorithm_version: null, accepted_units: creatinine_units, canonicalization_rule: "Retain original value/unit; convert mg/dL only by creatinine_units rule without asserting assay equivalence.", method_comparability_status: context_dependent, trend_breakpoint_note: "Laboratory, specimen, assay, calibration, platform, traceability, or method change may break trends.", cross_platform_comparison_prohibited: true, reference_contexts: [], external_mappings: [loinc.creatinine.mass, loinc.creatinine.molar], device_mappings: [], profile_limitations: [Assays remain platform-dependent., Interference and muscle/body context matter., Unit conversion is not method comparability.], source_reference_keys: [src-nist-creat, src-creat-method-2020, src-wst4045], derived_computation: null}
use_evidence_claims: []
system_relations: []
external_mappings: []
interpretation_limitations: [Assay method interference and muscle/body context matter., Creatinine is not kidney function., Cross-method/platform continuity is not assumed.]
agent_permissions:
  permitted_uses: [explain construct/specimen/assay/traceability/units, explain conversion limits, explain report provenance/breakpoints, explain eGFR lineage, request missing context]
  prohibited_uses: [equate with kidney function, diagnose kidney disease, normalize unreviewed methods, discard original report data, prescribe treatment, generate personal target, authorize action without gate]
  action_authorization: separately_gated
  authorization_note: Source-aware explanation only; diagnosis, treatment, personal targets, and actions require separate governance.
personalized_target_support: common exact object
lifecycle_relations: []
governance_notes: [Initial profile is serum/plasma enzymatic creatinine with recorded IDMS status., Jaffe is deferred.]
governance_metadata: common controlled object
~~~

## 15. Exact Blueprint — Heart Rate

~~~yaml
candidate_key: heart_rate
registry_id: controlled allocation-manifest injection
namespace: ME
lifecycle_status: proposed
version: v0.1
canonical_name_zh: 心率
canonical_name_en: Heart Rate
abbreviation: HR
aliases: []
legacy_codes: []
information_type: physiological_measurement
measurement_domain: cardiovascular_physiology
construct_type: physiological_measurement
construct_definition: Rate of cardiac cycles under an explicit measurement modality and time window.
allowed_measurement_natures: [measured, estimated]
value_type: number
unit_policy: heart_rate_unit
source_references: [src-loinc-hr, src-hr-ppg-2020, src-interlive-hr, src-ucum exact objects]
definition_source_keys: [src-loinc-hr]
profiles:
  - {profile_key: heart_rate.spot_clinical, profile_status: proposed, measurement_nature: measured, source_modality: clinical_device, specimen_type: null, matrix: null, body_site: null, collection_or_protocol_context: HR Spot column in Section 10, method: device-based spot heart-rate measurement, instrument_or_device: clinical heart-rate device, vendor_or_model: null, algorithm_version: null, accepted_units: heart_rate_units, canonicalization_rule: "Retain original value and /min; bpm is display text only.", method_comparability_status: context_dependent, trend_breakpoint_note: "Device, method, posture, rest, or window change may break trends.", cross_platform_comparison_prohibited: true, reference_contexts: [], external_mappings: [], device_mappings: [], profile_limitations: [Observation records posture/rest/device/window., Spot and summary values are not interchangeable., Manual pulse count excluded.], source_reference_keys: [], derived_computation: null}
  - {profile_key: heart_rate.wearable_ppg_time_series_estimate, profile_status: proposed, measurement_nature: estimated, source_modality: wearable, specimen_type: null, matrix: null, body_site: null, collection_or_protocol_context: HR Wearable column in Section 10, method: PPG-derived heart-rate estimate, instrument_or_device: wearable PPG device, vendor_or_model: null, algorithm_version: null, accepted_units: heart_rate_units, canonicalization_rule: "Retain device provenance/window and /min; never silently normalize platforms or contexts.", method_comparability_status: not_comparable, trend_breakpoint_note: "Device, firmware, algorithm, wear, sampling, aggregation, or artifact change is a breakpoint unless validated.", cross_platform_comparison_prohibited: true, reference_contexts: [], external_mappings: [], device_mappings: [], profile_limitations: [PPG estimate is not ECG., Motion wear signal sampling and artifact handling matter., Cross-platform normalization prohibited without validation.], source_reference_keys: [src-hr-ppg-2020, src-interlive-hr], derived_computation: null}
use_evidence_claims: []
system_relations: []
external_mappings: [loinc.heart_rate]
interpretation_limitations: [Modality window and context matter., PPG is not ECG., Spot and summaries are not interchangeable., Device/algorithm changes may break trends., No rhythm diagnosis.]
agent_permissions:
  permitted_uses: [explain construct/modality/window, explain unit/UI label, explain artifact/uncertainty/comparability, explain breakpoints, request missing context]
  prohibited_uses: [diagnose arrhythmia, treat PPG as ECG, interchange spot and summaries, silently normalize platforms/contexts, dismiss symptoms, generate risk score/target, prescribe or auto-authorize action]
  action_authorization: separately_gated
  authorization_note: Modality-aware explanation only; diagnosis, symptom triage, personal targets, and actions require separate governance.
personalized_target_support: common exact object
lifecycle_relations: []
governance_notes: [Initial profiles are spot device and wearable PPG estimate., Manual pulse and summary/zone/recovery profiles are deferred., SRC-NHC-LITERACY-2024 is excluded.]
governance_metadata: common controlled object
~~~

## 16. Exact Empty Collections

Every concept has `use_evidence_claims: []`, `system_relations: []`, and `lifecycle_relations: []`. Every initial profile has `reference_contexts: []` and `device_mappings: []`.

Height, Weight, HR spot, and HR wearable profile `external_mappings` are `[]`. Creatinine profile has only the two mappings in Section 8. Creatinine concept mappings are `[]`; the other concepts contain only their one mapping in Section 8.

## 17. Future Controlled Numeric-ID Allocation Contract

Founder Option B remains binding:

~~~text
boundary approved
-> exact authoring manifest approved
-> controlled numeric-ID allocation
-> separately authorized proposed-record creation
~~~

1. Allocation uses a separate immutable machine-readable ledger.
2. Candidate Ledger remains unchanged.
3. Numeric IDs use a namespace-level monotonic sequence.
4. IDs encode no body system, Pilot, priority, dependency, clinical meaning, product grouping, or action authority.
5. Allocated or reserved IDs are never reused.
6. Allocation scans all Registry records, prior allocation ledgers, reserved IDs, and committed IDs.
7. Each row binds `candidate_key`, `namespace`, `reserved_registry_id`, source Manifest SHA, intended record path, allocation status, and allocation date.
8. Allocation is limited to a Founder-approved allowlist and exact Manifest SHA.
9. Numeric IDs assigned now = 0. Allocation ledgers created now = 0.

## 18. Record Path Gate

The allocation task must inspect the actual Registry directory convention before selecting paths. This task does not guess a canonical directory. Temporary names such as `height.proposed.json` are examples only and are not created. Future filename or metadata must contain both allocated Registry ID and candidate key; the exact convention remains gated.

## 19. Founder Decision Sheet

| # | Decision | AI Recommendation | Founder Decision |
|---:|---|---|---|
| 1 | Approve schema-exact Height blueprint | Approve | Pending |
| 2 | Approve schema-exact Body Weight blueprint | Approve | Pending |
| 3 | Approve schema-exact Creatinine blueprint | Approve | Pending |
| 4 | Approve schema-exact Heart Rate blueprint | Approve | Pending |
| 5 | Exclude manual pulse count from initial Heart Rate | Approve | Pending |
| 6 | Exclude `SRC-NHC-LITERACY-2024` from initial Heart Rate | Approve | Pending |
| 7 | Approve concept/profile LOINC mapping plan | Approve | Pending |
| 8 | Approve separate immutable allocation-ledger contract | Approve | Pending |
| 9 | Authorize next numeric-ID allocation-manifest task | Only after 1-8 | Pending |

Pending decisions = 9. Accidental approvals = 0.

## 20. Validation Contract

- Pilot A coverage = 4/4.
- RegistryConcept required fields = 25/25 for each blueprint.
- MeasurementProfile required fields = 12/12 for each of five profiles.
- Unresolved source, mapping, unit, empty-array, permission, or optional-field choice = 0.
- Numeric IDs assigned = 0.
- Registry/profile record files created = 0.
- Allocation ledgers created = 0.
- Lifecycle values above `proposed` = 0.
- User observations and user-specific targets = 0.

A future generator may inject only the approved Registry ID and controlled creation date, then must pass Draft 2020-12 and the permanent semantic Validator.

## 21. Explicit Non-Authorizations

This manifest does not authorize ID allocation, allocation-ledger creation, Registry/profile record creation, lifecycle transition above `proposed`, Pilot B/C production, runtime, retrieval, publication, database, API, loader, index, Observation storage, Service Panel, user-health data use, personal targets, diagnosis, treatment, automatic action, or modification of protected assets.

## 22. Recommended Next Step

Founder + ChatGPT reviews the four schema-exact blueprints, source/mapping/unit decisions, and separate immutable allocation contract. Only after approval may a separate task prepare a controlled numeric-ID allocation manifest. No ID allocation or record production begins automatically.
