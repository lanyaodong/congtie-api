# Whole-Body Health Information Model + Biomarker and Measurement Registry MVP Specification v0.1

Version: v0.1
Project: Congtie
Status: Founder Approved / Registry Seed and Runtime Implementation Not Yet Authorized
Owner: Congtie Agent Team
Last Updated: 2026-08-19
Founder: 蓝耀栋
Founder Review Date: 2026-08-19
Document Type: Documentation-only MVP specification

---

## 1. Purpose

This document defines a documentation-only MVP specification for two related foundations:

```text
Whole-Body Health Information Model
全身健康信息模型

Biomarker and Measurement Registry
生物标志物与测量项目注册表
```

The Whole-Body Health Information Model describes the complete set of information types that may form a user's health context. The Biomarker and Measurement Registry is the public, canonical terminology and metadata layer for measurable or observable items within that model.

This work is P0 infrastructure for:

- the Congtie Agent;
- the User Health Information Library;
- future Personalized Longevity Protocols;
- longitudinal measurement and interpretation;
- future body-fluid testing service planning;
- evidence and citation traceability.

The goal is not to call every piece of health information a biomarker. The goal is to make each information type explicit, govern how it can be interpreted, and connect public definitions to private observations without mixing them.

### 1.1 Non-goals

This document does not:

- populate a complete Registry of hundreds of items;
- create Registry Seed 001;
- create an executable JSON Schema;
- modify an existing biomarker JSON or system map;
- create a database, migration, API, runtime, UI, report, or service integration;
- define a clinical diagnosis, treatment, prescription, risk score, or individualized medical plan;
- create or modify a knowledge entry;
- change the Batch 001 candidate pool;
- confirm a laboratory, nursing, logistics, or other commercial partnership;
- authorize public launch of a testing service.

---

## 2. Asset Audit

The repository already contains multiple biomarker, measurement, system, observation, and user-context assets. They were created for different stages and must not be treated as one coherent canonical model without review.

### 2.1 Tracked foundation assets

| Asset | Current Role | Reuse Decision |
| --- | --- | --- |
| `agent/user_health_information_library_mvp_spec.v0.1.md` | Product definition for the private User Health Information Library | Preserve as the private context boundary; future observations should live under this user-controlled layer. |
| `agent/user_health_context_schema.v0.1.md` | Conceptual private user-context schema | Reuse its privacy, permission, source, and missing-context principles; do not treat it as an executable data model. |
| `spec/examples/create_observation.request.json` | Example observation write payload | Treat as an implementation-era prototype that demonstrates result instances; it is not a Registry definition. |
| `spec/examples/create_observation.response.json` | Example observation response | Reuse only after future contract review; fields are incomplete for full provenance and reference-interval governance. |

### 2.2 Draft and local biomarker assets

| Asset | Observed Scope | Gap / Treatment |
| --- | --- | --- |
| `schemas/biomarker_schema_v0.1.json` | Small JSON inventory with 12 biomarker-like items | Draft inventory only. It lacks the complete classification, method, reference-interval, provenance, evidence, and governance model defined here. |
| `spec/biomarker_registry.v0.1.json` | Agent-facing registry with 23 items and legacy project naming | Useful code and alias seed, but not accepted as the new canonical Registry. It mixes laboratory biomarkers, physiological measurements, functional measures, device data, and reported states under one biomarker label. |
| `spec/biomarker_schema_v0.1.md` | Older document proposing about 120 biomarkers and single-value range/frequency concepts | Source inventory only. Its `optimal_range`, `reference_range`, frequency, and system ownership assumptions require claim-level and context-level review. |
| `spec/system_minimum_biomarkers_v0.1.md` | Six-system minimum-set proposal | Candidate input for P0 prioritization. A minimum product set is not proof that every item is a biomarker or that its system assignment is uniquely biological. |
| `agent/biomarker_system_map.v0.1.json` | Earlier six-system map skeleton | Historical/draft input only. Do not promote automatically. |
| `agent/biomarker_system_map.v0.2.draft.json` | Expanded non-final mapping inventory with primary and secondary systems | Strong input for many-to-many system mapping, but still non-final and explicitly non-diagnostic. |
| `agent/biomarker_system_map_v0.2_context_layer_spec_2026_08_11.v0.1.md` | Planning-only context-layer specification | Reuse its distinction between six-system routing and auxiliary context; do not infer production readiness. |

### 2.3 Draft interpretation and runtime assets

| Asset | Observed Scope | Gap / Treatment |
| --- | --- | --- |
| `spec/system_state_evaluation_v0.1.md` | Proposed system-state evaluation using core markers | High-risk engineering input. It remains separate from the Registry and requires independent clinical, safety, and product review. |
| `spec/dmie_engine_spec_v0.1.md` | Dynamic Measurement and Intervention Engine concept | Future consumer of Registry metadata and observations, not the owner of terminology or evidence. |
| `spec/dmie_rules_v0.1.md` | Draft trigger rules for measurements, trends, gaps, and freshness | Requires separate rules governance. Registry membership must not auto-enable a DMIE trigger. |
| `spec/freshness_engine_spec_v0.1.md` | Draft freshness rules | Candidate input for observation freshness, not item identity. |
| `spec/accuracy_rules_spec_v0.1.md` | Draft accuracy/source-tier rules | Candidate input for provenance and measurement quality, not an evidence grade. |
| `app/main.py` observation structures | Current prototype accepts biosample, device, questionnaire, imaging, clinical exam, and estimated observations | Confirms a practical observation layer exists, but current sample, method, value, range, and provenance fields are incomplete. This specification does not modify runtime. |

### 2.4 Audit conclusion

The repository contains valuable components, but there is no single reviewed asset that currently provides all of the following:

- a whole-body information-type model;
- BEST-aligned biomarker terminology;
- a public Registry distinct from private observations;
- method-aware and context-aware reference-interval governance;
- many-to-many six-system mapping with biological and product relationships separated;
- structured evidence, source-role, and Agent permission fields;
- panel-view governance for a future testing service.

This specification defines that missing conceptual layer. Existing assets remain unchanged and require explicit mapping during Registry Seed 001.

---

## 3. Model Boundary

### 3.1 Whole-Body Health Information Model

The Whole-Body Health Information Model is the umbrella classification for all information that may be relevant to understanding a user's health context.

It includes measurements, reports, user-reported states, behaviors, exposures, social context, clinical records, and the metadata needed to interpret them. It does not imply that every item is measurable, clinically validated, or a biomarker.

### 3.2 Biomarker and Measurement Registry

The Biomarker and Measurement Registry is a public, versioned, canonical registry of definitions and metadata for measurable or observable items.

It answers questions such as:

- What is this item?
- Is it a biomarker, another measurement type, a score, or a reported state?
- What specimen, method, device, or questionnaire produced it?
- Which units and codes can identify it?
- What intended uses and evidence scopes have been reviewed?
- What interpretation, safety, and Agent-use boundaries apply?

It must not contain a user's actual result.

### 3.3 User Health Information Library

The User Health Information Library is the private, user-controlled, permission-based store of user-specific context and observations.

It may reference Registry items, but it owns:

- the user's result;
- date and time;
- source report or device;
- authorization and privacy state;
- longitudinal history;
- user-reported context;
- missing-context and verification status.

### 3.4 User Observation

A user observation is a time-bound result or record instance for one user. It links to a Registry item when an appropriate mapping exists.

```text
Registry definition != user observation
```

For example, the Registry may define how LDL-C is identified and measured. A user's LDL-C value from a specific laboratory, method, date, unit, and report is an observation.

### 3.5 Service Panel

A service Panel is a curated, versioned view of selected Registry items for a defined service objective. A Panel is not the Registry itself.

```text
Whole-Body Health Information Model
  -> classifies all health information

Biomarker and Measurement Registry
  -> defines public measurable/observable items

Service Panel
  -> selects items for one service objective

User Health Information Library
  -> stores private user context and observations
```

### 3.6 Relationship with Knowledge Entries

A concept knowledge entry and a Registry item have different responsibilities.

`KN-T0403-0001` defines what a biomarker is, how biomarkers differ from clinical outcomes, major biomarker types and BEST roles, and general evidence and safety boundaries.

A Registry item defines one concrete item, such as ApoB, HbA1c, creatinine, blood pressure, HRV, or a questionnaire scale, including its identity, specimen or source, method, unit, reference information, intended use, six-system mappings, provenance requirements, limitations, and Agent permissions.

> Registry item 不替代概念知识条目；概念知识条目也不负责保存每个测量项目的 item-level metadata。未来回答具体标志物问题时，可能同时引用概念知识条目和具体 Registry item。

```text
Registry item != knowledge entry
Registry item != user observation
Registry != service Panel
```

---

## 4. Whole-Body Health Information Types

`Biomarker by default` means whether an item in the category should normally be labeled a biomarker before intended use and validation are reviewed.

| Information Type | Definition | Examples | Biomarker by Default | Permitted Uses | Interpretation Boundary |
| --- | --- | --- | --- | --- | --- |
| `laboratory_biomarker` | A measured laboratory characteristic used as an indicator of a biological process, pathogenic process, or response/exposure in a defined context. | LDL-C, HbA1c, hs-CRP | Yes, when the specific analyte and intended use meet biomarker terminology | Definition, trend review, source-aware education, reviewed monitoring context | No diagnosis, treatment, risk calculation, or action from the value alone. |
| `molecular_biomarker` | A molecular characteristic measured in tissue or body material. | DNA variant, transcript, protein, metabolite | Often, after the characteristic and intended use are specified | Research/clinical role education, evidence tracking, method comparison | Molecular presence does not prove clinical utility or personal actionability. |
| `physiological_measurement` | A direct measurement of physiological function or state. | Blood pressure, heart rate, oxygen saturation | Sometimes; role depends on context | Trend review, measurement education, general safety escalation rules | Do not treat one reading as diagnosis or a complete system state. |
| `functional_performance_measurement` | A measured ability or performance outcome. | Grip strength, gait speed, VO2max test result | Not automatically | Capability tracking, baseline and longitudinal comparison | Performance is affected by protocol, effort, equipment, learning, illness, and context. |
| `imaging_derived_measure` | A quantitative or categorical measure derived from imaging. | Bone mineral density, organ volume, coronary calcium score | Sometimes | Method-aware interpretation, longitudinal comparison, report organization | Imaging findings require modality, protocol, reader/software, and clinical context. |
| `device_measured_signal` | A signal directly sensed by a device. | ECG waveform, accelerometer signal, skin temperature signal | Not automatically | Signal storage, quality assessment, trend and artifact review | Device class, body site, sampling, calibration, and validation determine meaning. |
| `device_estimated_metric` | An estimate inferred by an algorithm from one or more device signals. | Estimated sleep stage, wearable stress score, energy expenditure estimate | No | Contextual trend, behavior reflection, product-method education | It is not a direct reading of sleep, mood, stress, recovery, or disease. Algorithm/version and limitations must be recorded. |
| `derived_score_index` | A value mathematically derived from other values or categories. | BMI, composite risk score, readiness score, biological-age estimate | No | Transparent calculation, version comparison, bounded education | Inputs, formula, version, population, validity, and intended use must be explicit. A score is not automatically a clinical conclusion. |
| `patient_user_reported_state` | Information reported by the user about feeling, function, symptoms, goals, or experience. | Mood, perceived stress, fatigue, pain, subjective sleep quality | No | Personal context, longitudinal self-reflection, missing-context detection | User report is important personal evidence but is not automatically a biomarker or scientific evidence. |
| `validated_questionnaire_scale` | A versioned questionnaire or scale with defined language, scoring, population, and psychometric evidence. | PHQ-9, GAD-7, PSQI, other validated scales | No | Structured self-report or professional assessment context under permission and licensing rules | It is distinct from free-text self-report, may be clinically sensitive, and must not automatically generate a diagnosis. Registry metadata must not copy protected full scale content without rights. |
| `behavior_lifestyle_record` | A record of behavior or routine. | Sleep schedule, physical activity, exercise, diet and nutrition, social connection | No | Habit tracking, context assembly, feedback-loop support | Recorded behavior may be incomplete or estimated; it does not prove a health effect. |
| `demographic_social_context` | Relatively stable or contextual information about the person and social environment. | Age, sex, occupation, caregiving, housing, access constraints | No | Applicability assessment, equity/context review, permission-gated personalization | Must not become discriminatory scoring or unsupported causal inference. |
| `exposure_environment_context` | Information about environmental, occupational, infectious, behavioral, or intervention exposure. | Air pollution, heat, shift work, tobacco exposure, medication exposure | No by category; a measured response may be a biomarker | Context assembly, exposure documentation, source-aware education | Exposure record and biological response are distinct. Association does not establish individual causation. |
| `clinical_record` | A document or structured record created within care. | Clinical note, discharge summary, pathology report | No | Record organization, provenance, preparation for professional review | A record can contain diagnoses and measurements, but the document itself is not a biomarker. |
| `diagnosis_medication_procedure` | A recorded clinical diagnosis, prescribed medication, procedure, or intervention. | Diabetes diagnosis record, statin prescription, surgery record | No | Medication/procedure context, interaction and safety context, professional handoff | Congtie must not create, stop, change, or reinterpret clinical care solely from this record. |
| `specimen_measurement_metadata` | Metadata required to understand how a sample or observation was produced. | Specimen, fasting state, posture, method, device, storage, transport | No | Quality control, comparability, uncertainty, provenance | Metadata changes interpretation but is not the health result itself. |

### 4.1 Cross-type rule

One concept may have multiple representations, but each Registry record must identify its actual information type and intended use. For example:

- heart rate can be a direct physiological measurement;
- a wearable readiness score derived partly from heart rate is a device-estimated metric;
- perceived stress is a user-reported state;
- cortisol measured in a defined specimen and method may be a laboratory biomarker in a specified context.

These must not be collapsed into one interchangeable concept.

---

## 5. Biomarker Definition Governance

The primary terminology reference is the FDA-NIH BEST Glossary (https://www.ncbi.nlm.nih.gov/books/NBK338448/). The full BEST Resource remains available at https://www.ncbi.nlm.nih.gov/books/NBK326791/.

BEST defines a biomarker as a measured characteristic indicating normal biological processes, pathogenic processes, or biological responses to an exposure or intervention. It also states that a biomarker is not a measure of how an individual feels, functions, or survives.

BEST is a terminology anchor, not a grant of clinical permission to Congtie.

### 5.1 Biomarker roles

The Registry should support the following role labels when the intended use and evidence are verified:

| BEST Role | Registry Meaning | Congtie Boundary |
| --- | --- | --- |
| `susceptibility_risk` | Associated with increased or decreased likelihood of developing a condition in a defined population/context | Does not authorize personal disease-risk calculation. |
| `diagnostic` | Used to detect or confirm a disease/condition or identify a subtype in a defined clinical context | Does not authorize Congtie to diagnose. |
| `monitoring` | Repeatedly assessed to follow status, exposure, or response | Does not make every repeat measurement clinically necessary. |
| `prognostic` | Associated with future clinical events or progression in a defined population | Does not authorize personal prognosis or lifespan prediction. |
| `predictive` | Identifies differing likelihood of response to a specific intervention | Does not authorize intervention selection or prescribing. |
| `pharmacodynamic_response` | Indicates a biological response to an intervention or exposure | Does not prove clinical benefit or a meaningful outcome. |
| `safety` | Indicates or predicts potential harm/toxicity in a defined use context | Does not replace professional monitoring or escalation. |

### 5.2 Intended-use rule

One measured characteristic may have different roles in different contexts. The Registry must therefore attach biomarker roles to a reviewed intended use, not to the item name globally.

```text
registry item + intended use + population + method + evidence scope
```

is the minimum meaningful governance unit for a biomarker role.

BEST roles remain exactly:

- susceptibility/risk;
- diagnostic;
- monitoring;
- prognostic;
- predictive;
- pharmacodynamic/response;
- safety.

`screening` is not an eighth BEST biomarker role. Workflow purpose belongs in a separate `use_context`, which may include `screening`, `diagnosis_support`, `monitoring`, `risk_assessment`, `treatment_response`, `safety_monitoring`, `research`, `wellness_tracking`, and `context_only`. A screening context still requires the actual biomarker role, claim, population, method, intended use, and evidence to be reviewed.

---

## 6. Canonical Registry Record

The future Registry should use structured records. The following fields are conceptual requirements, not an executable schema.

### 6.1 Identity

- `registry_id`
- `canonical_name_zh`
- `canonical_name_en`
- `abbreviation`
- `aliases`
- `version`
- `status`
- `source_asset`
- `migration_status`
- `supersedes`
- `superseded_by`
- `duplicate_of`
- `migration_note`

Stable Registry IDs must not encode a six-system owner because one item may map to multiple systems. Candidate prefixes for separate Seed 001 ID governance are `BM-000001` for laboratory/molecular biomarkers, `ME-000001` for physiological/functional measurements, `SC-000001` for scores/indexes, and `QS-000001` for validated questionnaires/scales. Other types require separate approval. IDs such as `BM-T0302-0001` are prohibited.

### 6.2 Classification

- `information_type`
- `biomarker_type`
- `intended_use`
- `use_context`
- `measurement_domain`

`biomarker_type` may be empty for non-biomarker measurement or context items. `intended_use` may contain multiple separately governed records.

### 6.3 Standards and codes

- `mapping_system`
- `mapping_code`
- `mapping_version`
- `mapping_status`
- `mapping_confidence`
- `mapping_note`
- LOINC where applicable
- UCUM where applicable
- SNOMED CT where applicable
- UniProt where applicable
- applicable China standards
- local and partner laboratory codes
- `mapping_reviewer`

LOINC identifies health observations, measurements, and documents; UCUM provides unambiguous machine-readable units. Other external mappings are optional and item-specific. `mapping_status` may include `mapped`, `not_applicable`, `pending`, `no_match`, and `deprecated_mapping`. External mapping absence does not block every Seed 001 item, but it must be explicit. The stable local Registry ID remains authoritative. Mapping presence improves interoperability but does not validate clinical utility.

### 6.4 Specimen and collection

- `specimen_type`
- `matrix`
- `collection_method`
- `preservation_method`
- `fasting_requirement`
- `time_of_day_context`
- `posture_context`
- `recent_exercise_context`
- `acute_illness_context`
- `medication_context`
- `supplement_context`
- `known_analytical_interferences`
- `preanalytical_confounders`
- `sex_reproductive_context`
- `storage_requirement`
- `transport_requirement`
- `stability_window`

### 6.5 Measurement

- `value_type`
- `canonical_unit`
- `accepted_units`
- `conversion_rule`
- `laboratory_id`
- `laboratory_test_code`
- `assay_method`
- `assay_version`
- `instrument_model`
- `reagent_or_kit_version`
- `device_model`
- `firmware_version`
- `algorithm_version`
- `calibration_date`, where the source provides it
- `method_effective_from`
- `method_effective_to`
- `method_change_breakpoint`
- `method_comparability_status`
- `validated_conversion_rule`
- `harmonization_reference`
- `trend_comparability_note`
- `cross_platform_comparison_prohibited`
- `detection_limit`
- `quantification_limit`
- `analytical_variation`
- `uncertainty_status`
- `source_reported_uncertainty`
- `analytical_cv`
- `biological_variation_available`
- `uncertainty_missing`
- `interpretation_caution`
- `quality_control_note`

No conversion rule should be implemented without dimensional and method review. Most cross-method results cannot be reliably converted by one generic `assay_equivalence_factor`. A conversion is allowed only when a validated relationship exists. Otherwise the Agent must disclose a possible trend breakpoint and must not normalize values on its own. A mathematically convertible unit does not guarantee method comparability.

Not every source provides calibration date or numeric uncertainty. Missing or unavailable metadata should be recorded, not invented. This specification does not require every result to be rendered as `value +/- uncertainty`.

### 6.6 Interpretation

- `biological_meaning`
- `clinical_research_role`
- `common_uses`
- `limitations`
- `confounders`
- `biological_variation`
- `actionability`
- `escalation_boundary`
- `measurement_frequency_principle`
- `minimum_context_required`
- `algorithm_name`
- `algorithm_version`
- `developer`
- `input_features_summary`
- `validation_population`
- `validation_cohort_summary`
- `output_meaning`
- `prohibited_use`
- `model_updated_at`

For proprietary algorithms, unavailable implementation detail should be recorded as `proprietary / unavailable`, not guessed.

Validated questionnaire/scale records should conditionally support `scale_name`, `scale_version`, `language`, `scoring_method`, `validated_population`, `cutpoint_source`, `license_or_rights_status`, `clinical_sensitivity`, and `prohibited_automated_inference`. The Registry stores metadata and does not automatically reproduce copyrighted full scale content.

### 6.7 Reference values and thresholds

- `laboratory_reference_interval_model`
- `population_reference_intervals`
- `clinical_decision_limits`
- `risk_associated_thresholds`
- `critical_alert_values`
- `future_personalized_targets`
- `reference_value_source`
- `applicability_conditions`

These are separate structures, as defined in Section 7.

### 6.8 Six-system mapping

- `primary_system_id`
- `secondary_system_ids`
- `relationship_type`
- `mapping_rationale`
- `mapping_source`
- `mapping_evidence_level`
- `mapping_confidence`
- `cross_system_note`

### 6.9 Evidence and governance

- `evidence_level`
- `evidence_scope`
- `sources`
- `source_role`
- `source_verification_status`
- `last_reviewed`
- `next_review`
- `clinical_sensitivity`
- `permitted_agent_use`
- `prohibited_agent_use`
- `commercial_boundary`
- `review_owner`
- `regulatory_data_classification`

Registry evidence level binds to a specific intended use, claim, and evidence scope, not to the marker as an object. The same item may have different evidence levels when used for risk association, diagnostic support, monitoring, response, or wellness tracking. Congtie continues to use the current canonical E1-E5, E0, and EX framework without replacement.

### 6.10 Lifecycle status

Registry records should use a governed lifecycle:

- `proposed`
- `mapped`
- `source_verified`
- `human_reviewed`
- `active`
- `deprecated`
- `research_only`
- `excluded`

`active` means approved for its defined product uses. It does not mean clinically indicated for every user.

---

## 7. Reference Interval and Threshold Model

The Registry must not use `normal range` as a universal umbrella for all intervals, thresholds, and targets.

### 7.1 Six separate concepts

| Type | Definition | Storage / Display Rule |
| --- | --- | --- |
| `laboratory_reported_reference_interval` | The interval reported by the laboratory for the specific result | Preserve exactly with the user observation, including lab, method, unit, population/context note, and report provenance. |
| `population_reference_interval` | An interval established for a defined reference population and method | Store as contextual Registry metadata with its source, population, method, and applicability limits. |
| `guideline_clinical_decision_limit` | A threshold or range used for a defined clinical decision | Store separately from reference intervals and never relabel as the laboratory range. |
| `risk_associated_threshold` | A value associated with differing outcome risk in a defined population | Preserve evidence design and scope; do not convert directly into personal risk. |
| `critical_alert_value` | A laboratory or care-system value requiring time-sensitive communication under a defined policy | Preserve source organization and escalation workflow; do not invent a universal critical threshold. |
| `future_personalized_target` | A future user-level target selected under authorized product, evidence, safety, and professional governance | Never present as a laboratory reference interval or universal normal value. |

### 7.2 Core rules

1. Every imported user result must preserve the original laboratory-reported reference interval when one is supplied.
2. The Registry must not overwrite that interval with one global Registry interval.
3. Reference information should record laboratory, analytical method, reference population, age, sex, pregnancy or menstrual context where relevant, fasting state, collection conditions, and other applicability factors.
4. Clinical decision limits must remain separate from population reference intervals.
5. Risk-associated thresholds must state population and study context.
6. Critical or alert values must preserve the responsible organization's policy and escalation route.
7. Future personalized targets must be labeled as targets and must not masquerade as laboratory reference intervals.
8. Unknown or absent context must remain unknown; Congtie must not infer a range from appearance alone.
9. When a laboratory interval differs from a Registry population interval, guideline decision limit, or risk-associated threshold, all applicable values and sources must be preserved. Congtie must not silently select or overwrite one.
10. Each interval should support `interval_type`, laboratory, method, platform, population, age/sex/context, effective date, source, version, `effective_from`, `effective_to`, `superseded_by`, and `version_note`.
11. A new interval must not silently rewrite the original interpretation context of a historical observation. Reinterpretation and user notification require separate version-impact governance.

### 7.3 Standards alignment

CLSI EP28 is the primary laboratory reference for establishing and verifying quantitative reference intervals. HL7 FHIR `Observation.referenceRange` demonstrates that multiple contextual ranges may be represented and differentiated for different populations or circumstances.

Future implementation should map these concepts without assuming that the FHIR reference-range element alone represents every clinical decision limit, risk threshold, or personalized target.

---

## 8. Six-System Mapping

Congtie currently uses six product systems:

- `T03.01` Energy System / 能量系统
- `T03.02` Metabolic System / 代谢系统
- `T03.03` Cardiopulmonary System / 心肺循环系统
- `T03.04` Musculoskeletal System / 肌肉骨骼系统
- `T03.05` Neurocognitive System / 神经认知系统
- `T03.06` Repair Immune System / 修复免疫系统

Registry-to-system mapping must be many-to-many.

### 8.1 Biological relationship

This expresses a reviewed biological, physiological, clinical, or research relationship between an item and a system.

It requires:

- a mapping rationale;
- source support;
- evidence level and scope;
- confidence;
- a cross-system note when relevant.

### 8.2 Product grouping

This is a routing or display choice used for UI, reports, Agent context assembly, or service organization.

Product grouping may choose a primary home for clarity. It must not be presented as the item's only biological system or as proof of a clinical relationship.

### 8.3 Mapping rules

- `primary_system_id` is optional when ownership is unresolved or inappropriate.
- `secondary_system_ids` may contain multiple systems.
- `relationship_type` must distinguish at least `biological_relationship`, `clinical_context`, `product_grouping`, and `context_only`.
- one mapping must not transfer evidence or actionability to another system;
- system membership must not enable diagnosis, scoring, intervention, or testing frequency by itself;
- T03.07 Gut and Microbiome Context may be referenced when appropriate, but it does not silently become a seventh core system in this specification.

---

## 9. Sample Type Governance

The Registry must represent the actual specimen or measurement modality. At minimum it should plan for:

- whole blood;
- serum;
- plasma;
- home capillary blood;
- dried blood spot;
- urine;
- saliva;
- buccal/oral epithelial sample;
- stool;
- cervical cell, swab, secretion, or a named preservation medium;
- other specified body fluid;
- imaging;
- wearable/device;
- home measurement;
- functional test;
- questionnaire/user report.

`home_capillary_blood` means wet capillary blood collected at home, such as fingertip or earlobe blood in a microcontainer or named anticoagulant/container. `dried_blood_spot` means blood dried on a specified carrier. Their collection, stability, analyte coverage, analytical methods, and reference intervals may differ and must not be treated as interchangeable.

`宫颈提取液` must not be used as one ambiguous universal specimen type. If a partner, report, or market page uses that original term, preserve it as `original_specimen_text`, map it only after verifying cervical cell, swab, secretion, preservation fluid, test method, and collection site, and use `specimen_mapping_pending` when unresolved. Congtie must not guess.

### 9.1 Sample identity requirements

Where applicable, the record should distinguish:

- human material from measurement modality;
- specimen from matrix;
- collection method from analytical method;
- collection container or preservation medium from specimen;
- collection time from processing time;
- storage duration from stability window.

---

## 10. Result Provenance and Observation Linkage

Every future user observation should link, when applicable, to:

- `user_id`;
- `registry_id` and registry version;
- observation date and time;
- result value and value type;
- original unit and normalized unit where valid;
- specimen and matrix;
- collection conditions;
- source organization;
- laboratory or device;
- method/platform and version;
- original report or source artifact;
- laboratory-reported reference interval;
- original result flag;
- data freshness;
- verification status;
- import/mapping status;
- permission status;
- provenance chain;
- correction or supersession history;
- method and platform version fields from Section 6.5;
- context tags;
- missing-data reason;
- consent scope and purpose of use.

Context tags may include `recent_intense_exercise`, `prolonged_fasting`, `acute_illness`, `recent_infection`, `recent_vaccination`, `medication_started`, `medication_stopped`, `supplement_started`, `supplement_stopped`, `menstrual_phase`, `pregnancy_context`, `sleep_deprivation`, `alcohol_exposure`, `dehydration`, and `recent_travel`. A tag records context; it does not prove causation.

Qualitative results should support `standardized_result_code`, `terminology_system`, `mapping_status`, and `original_report_text` for values such as positive/negative, detected/not detected, high/low, present/absent, and indeterminate. Standard mapping must not overwrite the original report text.

Missing-data semantics must distinguish `not_tested`, `not_collected`, `test_failed`, `insufficient_sample`, `below_detection_limit`, `above_quantification_limit`, `not_applicable`, `unknown`, `withheld`, `permission_denied`, and `source_unavailable`. None may be silently converted to zero, normal, or negative. This follows the design principle of FHIR `dataAbsentReason` without creating an executable FHIR profile.

### 10.1 Separation rule

```text
Registry item
= public definition, methods, mappings, evidence, and boundaries

User observation
= private result instance, source, time, context, provenance, and permission
```

A Registry update must not silently rewrite a historical observation. Observations should retain the Registry version and mapping used when they were ingested or later reprocessed.

Personal longitudinal analytics belong to the User Observation / Derived Analytics Layer, not the public Registry. These include `personal_baseline`, `delta_from_baseline`, `rate_of_change`, `rolling_average`, `trajectory_window`, `biological_variation_ratio`, `method_breakpoint`, `trend_confidence`, and `trend_interpretation_status`. The Registry defines whether and under what conditions an item is comparable longitudinally; it does not store a person's baseline.

The user-data layer should support `consent_scope`, `permission_status`, `purpose_of_use`, `effective_from`, `expires_at`, `withdrawn_at`, `sharing_scope`, `export_allowed`, and `deletion_status`. Public Registry metadata does not contain personal consent records.

```text
Registry record != user consent record
```

Users should receive applicable rights to notice, authorization and withdrawal, access, correction, copying or export, deletion, and other rights under applicable law. Detailed implementation requires a separate data and compliance Gate.

---

## 11. Evidence and Citation Contract Integration

This specification should support, but does not modify:

```text
agent/knowledge_seed_v0/evidence_and_citation_output_contract.v0.1.md
```

The future traceability chain is:

```text
answer claim
-> canonical knowledge entry
-> Registry item and intended use
-> authorized personal observation
-> source organization, specimen, method, and device
-> laboratory reference interval or separately labeled threshold
-> external evidence source
```

### 11.1 Recommended future integration points

- claim-to-Registry mapping;
- claim-to-source mapping;
- structured Registry source records;
- intended-use-specific evidence scope;
- source verification status;
- observation provenance;
- method and code mapping version;
- reference-interval and decision-threshold identity;
- personal-context citation;
- privacy-safe answer rendering;
- retrieval timestamp and live-source freshness;
- explicit separation of external evidence from personal context basis.

### 11.2 Evidence boundary

```text
External Evidence != Personal Context Basis
user observation != scientific evidence
```

Registry evidence should answer whether a definition, role, method, mapping, interval, limitation, or intended use is supported. It must not treat the existence of a measurement as evidence that measuring it improves outcomes or that the item is actionable for every user. E1-E5 applies to an external claim, source body, or product/framework claim, not to a user observation as a personal evidence grade.

---

## 12. Service Panel Views

The Registry can be broad. A service Panel must be curated for a defined purpose.

### 12.1 Panel types

| Panel Type | Purpose | Boundary |
| --- | --- | --- |
| `Core Baseline Panel` | Establish an initial multi-system baseline using reviewed, high-value measures | Not every Registry item belongs in baseline testing. |
| `Follow-up Panel` | Repeat selected items at marker-specific intervals to observe change | Frequency must reflect biology, method, actionability, prior result, and user context. |
| `Age/Sex/Context Module` | Add items based on age, sex, reproductive context, history, exposure, goals, or professional judgment | Context selection is not an automatic clinical recommendation. |
| `Conditional Add-on` | Add an item because history, an initial result, missing context, or professional judgment creates a defined need | The trigger and decision owner must be explicit. |
| `Research/Emerging Panel` | Separate research, early, or limited-actionability measures from core service | Must be labeled `research_only` or equivalent and must not be marketed as established benefit. |

### 12.2 Panel governance principles

- panel size is not a quality metric;
- more testing can create false positives, incidental findings, anxiety, cost, and follow-up burden;
- not every marker should be measured in every user;
- testing frequency must be item-specific and context-specific;
- each Panel needs an objective, inclusion rationale, exclusion rules, review owner, version, and evidence scope;
- a Panel can reference Registry items but may add service-specific operational metadata;
- commercial availability must not determine biological importance or Agent priority.

---

## 13. Planned China Service Context

Founder target:

```text
Build toward Congtie body-fluid testing service capability by the end of December 2026.
```

This is a planning target, not a commitment to a public launch date.

Founder-mentioned candidate ecosystem participants include:

- 迪安诊断;
- 金域医学;
- home nursing or sampling services;
- 顺丰 or comparable specimen-logistics capability.

No signed-partnership evidence was identified in the audited repository. These names must therefore be described only as planned candidate partners or ecosystem references, never as confirmed partners.

### 13.1 Required capability planning

Future service design will need:

- Panel-to-Registry mapping;
- partner test and panel codes;
- partner-specific units and methods;
- collection-site and home-sampling options;
- specimen identity, container, preservation, and chain of custody;
- transport temperature and time requirements;
- stability windows;
- turnaround time;
- cost and settlement price;
- report ingestion and original-report preservation;
- local-code-to-LOINC mapping where applicable;
- reference-range preservation;
- abnormal and critical-result handling;
- privacy, consent, retention, and deletion;
- customer support;
- professional escalation;
- incident and correction workflows.

> 本 Registry 是公共信息与数据治理基础，不构成实验室检测、医学诊断或处方。实际样本采集和检验应由具备相应资质、并在适用执业范围内的第三方机构执行；Congtie 不把自身表述为实验室或医疗机构。

This specification does not design or authorize a clinical service workflow, laboratory order, medical interpretation, logistics contract, or partnership agreement.

Future legal review should classify data with concepts such as `public_registry_metadata`, `sensitive_personal_health_information`, `biometric_information`, `human_genetic_resource_information`, `potentially_important_data`, and `classification_pending_legal_review`. Public Registry definitions are not automatically sensitive personal data; user observations commonly require personal-health-information governance. Genetic/genomic information may require human genetic resource review, but not every clinical, imaging, protein, or metabolite record is automatically human genetic resource information. Cross-border requirements depend on current law, data category, scale, processor, purpose, and recipient. Final legal classification requires a legal/compliance Founder Gate; this specification does not promise permanent domestic storage for all data.

---

## 14. Market Reference Boundary

Function Health and WHOOP Advanced Labs are current public product references for understanding service architecture, not clinical authorities.

Observed public patterns include:

- broad baseline testing plus repeat/follow-up testing;
- comprehensive and specialized Panel views;
- longitudinal result tracking;
- clinician-reviewed interpretation;
- action-plan or protocol presentation;
- linking laboratory results with wearable or user-context data.

Congtie may study these patterns, but must not:

- copy a proprietary catalog;
- treat a marketing claim as medical evidence;
- infer that a large Panel is clinically superior;
- transfer United States ordering, laboratory, privacy, or regulatory arrangements to China;
- copy a competitor's frequency, reference range, action rule, or commercial promise without independent review.

Market references should be recorded with access date and product-region context because their offerings can change.

---

## 15. Completeness Definition

Completeness must be scoped. It must not mean `all human biomarkers ever known`.

### 15.1 Registry completeness

Whether important variables within a stated domain and intended-use scope have reviewed identity, method, unit, mapping, evidence, limitation, and governance metadata.

### 15.2 Panel completeness

Whether a curated Panel is sufficient to answer its defined service objective, with known exclusions and escalation paths.

### 15.3 User-context completeness

Whether enough authorized personal context exists to answer the current question safely and meaningfully.

These completeness states must remain separate. A broad Registry does not make a Panel appropriate, and a broad Panel does not make one user's context complete.

---

## 16. MVP Prioritization

This section defines categories only. It does not enumerate actual Registry records.

### P0

- current planned laboratory Panel items;
- six-system minimum-item candidates after governance review;
- high-frequency core laboratory measurements;
- vital signs;
- body composition;
- major wearable signals and clearly labeled estimated metrics;
- physical capability measurements;
- cognitive capability measurements.

### P1

- extended laboratory markers;
- specialized hormones and nutrients;
- imaging-derived measures;
- home testing;
- validated questionnaires.

### P2

- omics and multi-omics;
- experimental aging clocks;
- research biomarkers;
- low-actionability commercial measurements;
- measures without adequate method, intended-use, or validation metadata.

Priority reflects product sequencing, not evidence strength or medical importance.

---

## 17. Delivery Plan to December 2026

### Phase 1 - Model and Asset Audit

- approve information-type definitions;
- approve Registry/UHIL/Panel/observation boundaries;
- map existing schemas, JSON, six-system assets, DMIE assets, and observation prototypes;
- identify legacy names, duplicate codes, and governance conflicts;
- select terminology and standards profiles.

### Phase 2 - Registry Seed 001

Before creating active records, reconcile the actual repository paths and status of:

- system minimum biomarker drafts;
- biomarker system map v0.1 and v0.2 drafts;
- existing biomarker JSON;
- older biomarker schema records;
- system-state, DMIE, freshness, and accuracy assets;
- observation request and response examples.

Old assets must not be batch-merged directly into active Registry records. Seed 001 should:

- create a reviewed initial item set;
- assign stable canonical IDs and lifecycle states;
- record source asset, migration status, duplicates, supersession, and migration notes;
- verify sources and intended uses;
- map units, methods, sample types, and six systems;
- implement the reference-interval concept model in documentation/data design;
- define validation and Founder review gates.

### Phase 3 - Service Panel Design

- define Core Baseline and Follow-up Panels;
- define Age/Sex/Context Modules;
- define Conditional Add-ons;
- isolate Research/Emerging items;
- document inclusion, exclusion, frequency, safety, and escalation rationale.

### Phase 4 - Partner and Data Mapping

- map laboratory and service codes;
- verify units and analytical methods;
- define specimen, collection, transport, stability, and turnaround requirements;
- design original-report and reference-range-preserving ingestion;
- define cost, settlement, privacy, support, and escalation requirements.

### Phase 5 - Founder / Seed Pilot

- import controlled pilot results;
- verify provenance and code mapping;
- test interpretation with evidence/citation rendering;
- test safety escalation and missing-context behavior;
- review remeasurement and longitudinal comparison;
- document corrections and pilot lessons before any public-launch decision.

The Founder target is capability by the end of December 2026. Each phase remains subject to evidence, safety, legal, privacy, partner, and Founder review.

---

## 18. Batch 001 B2-A Boundary

B2-A is the Founder-approved seven-entry production baseline:

1. `KN-T0403-0001` - 什么是生物标志物 / What Is a Biomarker?
2. `KN-T0403-0002` - 如何理解基线、长期趋势、测量误差与生物波动 / Understanding Baselines, Longitudinal Trends, Measurement Error, and Biological Variation - Founder approved for Batch Plan allocation; allocation pending the next task
3. `KN-T0408-0001` - 如何理解可穿戴与消费级设备数据 / Understanding Wearable and Consumer Device Data
4. `KN-T0501-0001` - 睡眠基础 / Sleep Basics
5. `KN-T0503-0001` - 锻炼基础 / Exercise Basics
6. `KN-T0502-0001` - 饮食与营养基础 / Nutrition Basics
7. `KN-T0504-0001` - 压力、情绪与心理健康基础 / Stress, Emotions, and Mental Well-Being Basics - `is_clinical_sensitive: true`

This Registry specification:

- is not an eighth knowledge entry;
- does not allocate an Entry ID;
- does not add to the Batch 001 candidate pool;
- is parallel P0 infrastructure work;
- does not block lawful public-source production of B2-A entries;
- does not add `KN-T0403-0002` to the Batch Plan in this task;
- leaves the repository candidate pool at 62 until the next allocation task changes it to 63;
- remains an auxiliary P0 line while B2-A knowledge production is the main line.

Registry Seed 001 planning and asset reconciliation may proceed in parallel with B2-A under separate tasks. B2-A knowledge production is the main line; Registry Seed 001 is the auxiliary P0 line. They may exchange definition and source feedback without requiring simultaneous completion.

---

## 19. Governance and Safety Rules

1. Registry membership does not authorize a test, diagnosis, risk score, intervention, medication, dosage, supplement plan, or Personalized Longevity Protocol.
2. A BEST biomarker role does not become a Congtie clinical permission.
3. A user observation is personal context, not scientific evidence.
4. An external evidence source does not prove that one user's observation has the same meaning.
5. A device estimate must be labeled as estimated or inferred and must retain algorithm/version context where available.
6. A derived score must retain its inputs, formula/version, validation population, and intended use.
7. Six-system product grouping must not be presented as unique biological ownership.
8. Reference intervals, decision limits, risk thresholds, alert values, and personalized targets must remain distinct.
9. Missing specimen, method, unit, source, time, or context must be reported as missing rather than guessed.
10. Commercial availability, commission, advertising, sponsorship, gifts, or partner convenience must not determine Registry evidence, Panel priority, or Agent recommendations.
11. Sensitive clinical items require explicit permitted and prohibited Agent-use rules.
12. Deprecated records must remain resolvable for historical observations and must point to replacements when applicable.

### 19.1 Analytical Interference and Preanalytical Context

`known_analytical_interferences` covers assay-process effects such as assay-specific interference, cross-reactivity, hemolysis, lipemia, icterus, biotin interference where applicable, and method-specific substance interference.

`preanalytical_confounders` covers collection and pre-collection factors such as fasting, time of day, posture, recent intense exercise, acute illness, alcohol, sleep loss, medication or supplement changes, menstrual/reproductive context, dehydration, and specimen handling.

These fields require item-specific evidence. The Registry must not claim that every supplement interferes with a test or that a context tag explains a result.

### 19.2 Derived Scores and Algorithms

Wearable recovery scores, device stress estimates, biological-age estimates, composite risk scores, and system-state scores should support algorithm identity, developer, version, input summary, validation population/cohort, output meaning, limitations, intended use, prohibited use, and update date. Proprietary details may be unavailable; absence must be stated rather than reconstructed.

### 19.3 Deprecation and Historical Reproducibility

Registry items are not physically deleted merely because they are deprecated. Governance should retain `status`, `deprecated`, `superseded_by`, `supersedes`, `duplicate_of`, `replacement_reason`, `deprecation_date`, and `historical_use_only`. Historical observations retain the Registry and method version used at the time.

### 19.4 Audit and Legal Implementation Boundary

Future implementation should support immutable audit-trail requirements, retention requirements, user access history, change history, and consent history. This specification does not require every read/write log to use WORM, does not declare FDA 21 CFR Part 11 applicable to all Congtie data, and does not assume HIPAA or GDPR automatically governs all China operations. Requirements depend on jurisdiction, product classification, business role, data category, partner obligations, and separate legal/security review.

---

## 20. Registry Seed 001 Field Tiers and Review Workflow

### 20.1 Required

- stable Registry ID;
- canonical Chinese and English names;
- information type;
- intended use and use context;
- specimen or measurement source;
- value type;
- canonical unit or `not_applicable`;
- method/platform requirement;
- six-system mapping;
- evidence and sources;
- interpretation limitations;
- safety boundary;
- Agent permitted use;
- Agent prohibited use;
- lifecycle status.

### 20.2 Conditionally Required

- reference-interval model;
- LOINC or UCUM mapping;
- collection conditions;
- analytical interferences;
- preanalytical confounders;
- questionnaire version, language, scoring, and rights;
- algorithm version and validation context;
- regulatory classification;
- partner code;
- method comparability.

### 20.3 Optional / Later Enrichment

- detailed biological variation;
- method-comparability studies;
- complete transport/stability data;
- full ontology mapping;
- validation cohort detail;
- extended China reference-population data.

Missing optional fields must not automatically reject a Seed 001 item.

### 20.4 AI Review Checklist

AI review should check at least:

1. information type is correct;
2. a device estimate, user report, or questionnaire is not mislabeled as a biomarker;
3. each BEST role is bound to a specific intended use;
4. screening is a use context, not a BEST role;
5. reference interval, decision limit, and risk threshold remain separate;
6. the original laboratory interval is preserved;
7. specimen, method, and unit identify the item adequately;
8. analytical interference and preanalytical context are appropriately separated;
9. six-system mapping separates biological relationship from product grouping;
10. evidence level binds to the claim/intended use;
11. sources are traceable and verified for their role;
12. safety boundary is explicit;
13. no automatic diagnosis, prescription, risk scoring, or unsupported personalization is authorized;
14. method/platform changes and trend breakpoints are represented;
15. missing data cannot be mistaken for zero or normal;
16. deprecated items remain historically traceable;
17. external codes and mapping versions are real and recorded;
18. user permission data is not written into the public Registry.

### 20.5 Governance Workflow

```text
change proposal
-> AI review
-> Founder Gate
-> human_reviewed
-> active
```

The workflow retains change log, review note, status history, deprecation, and supersession links. v0.1 does not create committee voting, fixed committee size, or voting thresholds.

### 20.6 Docs-only Definition of Done Boundary

The following are deferred implementation criteria and are not blockers for approval of this docs-only specification:

- a minimum Registry item count;
- ingestion latency;
- real-world dataset count;
- penetration-test outcomes;
- OpenAPI coverage;
- runtime or service SLA.

They belong respectively to Registry Seed 001, ingestion/runtime, interoperability, security release, or API implementation gates.

---

## 21. Acceptance Criteria for This MVP Specification

This Founder-approved v0.1 baseline:

- distinguishes the Whole-Body Health Information Model, Registry, Panel, User Health Information Library, observation, and knowledge entry;
- defines the required information types, including `validated_questionnaire_scale`;
- aligns biomarker terminology with the seven FDA-NIH BEST roles;
- keeps screening in `use_context`;
- defines the conceptual Registry record groups and stable ID rule;
- separates the six reference/threshold concepts and versions them;
- requires many-to-many six-system mapping;
- keeps T03.07 Gut and Microbiome Context as `context_only`, not a seventh core system;
- governs specimen identity, including home capillary blood, dried blood spot, and unresolved cervical specimen text;
- defines observation provenance, qualitative and missing-result semantics, consent, and personal analytics boundaries;
- records Evidence and Citation Contract integration through the canonical path;
- defines Panel views and China service-planning boundaries without implying confirmed partnerships;
- records field tiers, AI review, governance workflow, deprecation, and implementation DoD boundaries;
- records the five-phase path toward the December 2026 Founder target;
- keeps B2-A at seven entries and records `KN-T0403-0002` as approved for allocation;
- records `KN-T0504-0001` as clinically sensitive;
- creates no executable schema, Registry data, database, API, runtime, or service integration.

---

## 22. Source and Standards Notes

Primary terminology and interoperability references checked for this baseline:

1. BEST Glossary, FDA-NIH Biomarker Working Group. Primary terminology reference for biomarker definition and role categories. https://www.ncbi.nlm.nih.gov/books/NBK338448/
2. Full BEST Resource, FDA-NIH Biomarker Working Group. Full resource entry and role chapters. https://www.ncbi.nlm.nih.gov/books/NBK326791/
3. CLSI EP28, Defining, Establishing, and Verifying Reference Intervals in the Clinical Laboratory. Supports method-, population-, and laboratory-aware reference-interval governance. https://clsi.org/shop/standards/ep28/
4. HL7 FHIR R4 Observation definitions, including `Observation.referenceRange`. Supports contextual and multiple reference-range representation. https://hl7.org/fhir/R4/observation-definitions.html
5. LOINC. Supports standard identification of laboratory and clinical observations, measurements, panels, and documents. https://loinc.org/about/
6. UCUM. Supports unambiguous electronic representation of units. https://ucum.org/

Product-model references checked for this draft:

7. Function Health, How It Works. Used only to observe baseline/follow-up testing, longitudinal tracking, clinician review, and action presentation. https://www.functionhealth.com/how-it-works
8. WHOOP Advanced Labs. Used only to observe comprehensive/specialized Panels, laboratory/wearable integration, longitudinal tracking, and clinician-reviewed action presentation. https://www.whoop.com/us/en/advanced-labs/

Product-model references are not medical evidence for Congtie claims. Offerings, counts, pricing, regions, and availability are dynamic and must be checked live before future use.

---

## 23. Founder Review Decisions / Deferred or Rejected Suggestions

The following suggestions are not adopted in v0.1:

- adding screening as an eighth BEST biomarker role;
- replacing the canonical Congtie E1-E5 definitions;
- encoding six-system ownership in stable Registry IDs;
- requiring every item to map to every international ontology;
- using a generic assay equivalence factor;
- requiring numeric uncertainty for every result;
- requiring all logs to use WORM;
- declaring FDA 21 CFR Part 11 applicable by default;
- creating committee voting governance now;
- using engineering SLA, security test, or API coverage as this docs-only approval DoD;
- classifying all health data as human genetic resource information;
- stating that Congtie will permanently never provide testing services.

---

## 24. Founder Approval Boundary

Founder approval covers the conceptual architecture, information classifications, field planning, Registry design, reference and provenance governance, B2-A baseline, and Seed 001 planning rules.

It does not authorize:

- production database or user health cloud storage;
- API, runtime, indexing, retrieval, or citation rendering;
- automated diagnosis, treatment, medication, risk scoring, or Personalized Longevity Protocol generation;
- service Panel launch or laboratory integration;
- partner contracts or cross-border transfer;
- bulk activation of Registry Seed 001 records;
- B2 entry approval, publication, runtime, or retrieval.

---

## 25. Next Gate

Under separate tasks:

1. controlled commit and push of the two Founder-approved P0 documents;
2. allocate `KN-T0403-0002` in the Batch Plan and change the candidate pool from 62 to 63;
3. start B2-A knowledge production as the main line;
4. start Registry Seed 001 planning and asset reconciliation as the auxiliary P0 line.

This document does not execute any next-gate task.
