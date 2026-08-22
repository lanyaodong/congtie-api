# Registry Seed 001 - Asset Reconciliation and Seed Definition v0.1

Version: v0.1
Project: Congtie
Status: Draft / Founder Review Pending
Owner: Congtie Agent Team
Prepared: 2026-08-21
Document Type: Documentation-only planning baseline
Git Baseline: `f7d59ab476eca343d276ca297be9d60ab97dceee`

---

## 1. Purpose

This document defines the Founder-review baseline for Registry Seed 001. It reconciles existing biomarker, measurement, six-system, observation, freshness, accuracy, and DMIE assets without promoting any legacy record to active canonical status.

Registry Seed 001 should establish the first structurally correct and source-traceable set of public measurement definitions that can later support report ingestion, longitudinal observations, evidence-linked interpretation, and service planning.

This document does not create active Registry records, an executable schema, a database, an API, runtime behavior, a Service Panel, or production user-health storage.

---

## 2. Current Architecture Relationship

```text
Longevity Knowledge Entry
= explains concepts, evidence, and general boundaries

Biomarker and Measurement Registry Item
= defines one public measurement or observable concept

User Observation
= records one user's result at a specific time with provenance

Service Panel
= selects a governed subset of Registry items for a defined service objective
```

The four objects are related but not interchangeable:

```text
Knowledge Entry != Registry Item != User Observation != Service Panel
```

The Whole-Body Health Information Model is the umbrella classification. The Registry is the public canonical definition layer beneath it. The User Health Information Library is the private, permission-gated layer that may reference Registry items and store observations, context, and longitudinal history.

---

## 3. Repository Asset Audit

The audit covered tracked and untracked Markdown, JSON, YAML, Python, schema, example, validation, and prototype assets. Generated dependency directories were excluded. SHA-256 values below identify the files observed at this planning baseline.

| Asset | Path | Tracked? | SHA-256 | Current Meaning / Last Meaningful State |
| --- | --- | ---: | --- | --- |
| Registry MVP Spec | `agent/knowledge_seed_v0/whole_body_health_information_model_and_biomarker_measurement_registry_mvp_spec.v0.1.md` | yes | `ab887455d878cdc04f3baf596d775be0aef188da19df789eec4f3e8a2339f317` | Founder-approved conceptual authority; Seed and runtime not authorized. |
| Evidence Contract | `agent/knowledge_seed_v0/evidence_and_citation_output_contract.v0.1.md` | yes | `21f6db11aeec98a45e460dae66885f6337149cad0b56a8cffec26aa60b4f3457` | Founder-approved answer evidence and citation contract. |
| Knowledge Item Schema | `agent/longevity_knowledge_item_schema.v0.1.md` | yes | `9914746bd71831d3a8848764bc742599ebd0bc04e994ced051c6ab48f6a9953f` | Canonical knowledge-entry governance; not a Registry schema. |
| Evidence Framework | `agent/knowledge_seed_v0/evidence_grading_framework.v0.1.md` | yes | `37ac04a36118fc2c567c13773a9c46a2c1ec74cc72a290d565c00020033b54fc` | Canonical E1-E5, E0, and EX framework. |
| Topic Taxonomy | `agent/knowledge_seed_v0/longevity_topic_taxonomy.v0.1.md` | yes | `25a198dc075d6d78a12d4f962d4f41c2c9a1926218b82dbbd99c3fa723222854` | Canonical knowledge taxonomy; system encoding must not be copied into Registry IDs. |
| Batch 001 Plan | `agent/roadmap/longevity_knowledge_batch_001_plan.v0.1.md` | yes | `060f49fd2312b99f8ecde2197c513a22e5a645fbb149b6549d18d2f93b9d108a` | Knowledge production plan; Registry Seed is parallel infrastructure, not a knowledge candidate. |
| UHIL MVP Spec | `agent/user_health_information_library_mvp_spec.v0.1.md` | yes | `bb321f4579536c5b08febca981bf4f301782c2593a2ef4e93ca590519334c890` | Draft private-library boundary; no executable storage model. |
| User Health Context Schema | `agent/user_health_context_schema.v0.1.md` | yes | `2871f9e8b38a15399789ee796aca1ff75f6ffd7f2fbe9697db0191bc5af5abe7` | Founder-gated documentation-only conceptual schema; its biomarker fields are private-record placeholders. |
| Older UHIL Spec | `agent/knowledge_seed_v0/user_health_information_library_spec.v0.1.md` | no | `6237b094312c75a20eaceb14686dc59f0b6c689c3d0b0f63f41635e196e4f02c` | Earlier overlapping draft; valuable history but not the current Registry authority. |
| Biomarker JSON Inventory | `schemas/biomarker_schema_v0.1.json` | no | `dce36f298f4651ebe25e5ee5926ed88396f87f778d7cf14847d9f4e912a07420` | Twelve-item draft mixing laboratory, physiological, functional, imaging, and score concepts. |
| Xiaoge Biomarker Registry | `spec/biomarker_registry.v0.1.json` | no | `ef689b0851b2287848e5246c1f648357cd4698056f08a4b20ccb10a2c78dafc7` | Twenty-three-item agent-facing legacy inventory; old project naming and single-system ownership. |
| Legacy Biomarker Schema | `spec/biomarker_schema_v0.1.md` | no | `63007d08c8e502830a6d57550c29b67681d55652a07ff3f7ef925e0ae20ef3cd` | Approximately 120 labels; 107 unique textual labels before semantic deduplication. Uses legacy range/frequency assumptions. |
| Six-System Minimum Set | `spec/system_minimum_biomarkers_v0.1.md` | no | `5dbf463c7265bc2343e6b150941dbd6c1a37f9b2f7a166e193f641e01a88be81` | Draft core/supporting proposal tied to a worst-core-marker system-state model. Not clinical or product authority. |
| System Map v0.1 | `agent/biomarker_system_map.v0.1.json` | no | `c9db8e1c6bb8892d671498ec42fb9cc22632bc5fe3907ce28e510971b4cfe001` | Draft skeleton with one placeholder repeated across six systems. |
| System Map v0.2 | `agent/biomarker_system_map.v0.2.draft.json` | no | `5b5759a051148030390b6282df349069d5e44db2f4c89b39aa3fd4263dd710b1` | Founder-accepted non-final mapping inventory with 27 grouped rows; explicitly not production. |
| v0.2 Founder Acceptance | `agent/biomarker_system_map_v0.2_founder_acceptance_2026_07_18.v0.1.md` | no | `98a930e5167d2f0c750cc514db792bac6018c8a5d4ccdc24f21673ac0b641134` | Accepts the map only as a non-final minimal mapping inventory. |
| v0.2 Expansion Acceptance | `agent/biomarker_system_map_v0.2_marker_expansion_founder_acceptance_2026_08_01.v0.1.md` | no | `a1eaac369d8b0d393e848bfe99f1d28d6c89cabf9e52deb3f6979a6197b8b80e` | Accepts expanded rows for continued non-final planning, not production. |
| v0.2 Context Decisions | `agent/biomarker_system_map_v0.2_context_layer_decisions_closeout_2026_08_09.v0.1.md` | no | `5140c4e59ff53e8d19bf1807edf8ea896a7a42795cc9a9fee688101e6c24fb09` | Records context-layer decisions without activating JSON. |
| v0.2 Context Spec | `agent/biomarker_system_map_v0.2_context_layer_spec_2026_08_11.v0.1.md` | no | `9d41bbd21b7b20f834130c6ec7c498ebf65eb12d184c08f88f03ced0bebc9ff0` | Planning-only distinction between system mapping and auxiliary context. |
| v0.2 Supporting Audit Trail | 76 `agent/biomarker_system_map_v0.2_*` planning, prompt, notes, review, validation, acceptance, and closeout files | no | file-specific; four decision anchors are listed above | Historical decision chain for the non-final v0.2 map. Audited as one provenance family; it does not create production authority. |
| v0.2 Validation Tooling | `scripts/validate_biomarker_system_map_v0_2.py` and `tests/test_validate_biomarker_system_map_v0_2.py` | no | `a41aa248bc2c8603f81213dd1970ed8e4f4d802c6a13cdc461a6d7fa682db56e` / `f49229e174f7b634e003259c9aad08b4e024c7b8bc3da73086dba9066ecbbd43` | Prototype guardrails for the non-final map; not a future Registry validator. Thirteen fixture files exercise the old format. |
| System Registry | `spec/system_registry.v0.1.json` | no | `653daf1cfb8a04f06fa65c52a207b7ee01c3c40fb24b5c001856e7197e3e1857` | Legacy six-system product registry with old Xiaoge source-of-truth language and state model. |
| Observation Request Example | `spec/examples/create_observation.request.json` | yes | `826c0b2d249505d3d929edfd0d31129cce74a1c91ca43d7c42dca6ecbe0503c9` | Prototype instance payload using `biomarker_code`, device medium, value, unit, and time. |
| Observation Response Example | `spec/examples/create_observation.response.json` | yes | `35478d90a52c6e1d76bf68faabc5a9394f1ced96aa6fa09c42b0da648ddefd50` | Prototype response with freshness and accuracy but incomplete provenance and interval fields. |
| Observation API Model | `app/main.py` | yes | `64900a13cd5cea6a6911c8840ef9948b88a6b3ecd5fff338ed381eb08cdfac78` | Current prototype route writes observations by legacy `biomarker_code`; database DDL is not present in the audited repository. |
| OpenAPI Observation | `spec/openapi.v0.1.yaml` | yes | `cfd8b45817ff345451e2912ba86f5dcef7c878f450d1354b493bad8737e3a9a0` | Tracked prototype contract; medium and accuracy enums differ from `app/main.py`. |
| User Context Tool | `app/services/tools/get_user_health_context.py` | no | `3320653f52d1c0fd7b66d63bc06c22e9be8abf3c93dd3817aa2a58f6a04224e0` | Placeholder tool response; no production health-data retrieval. |
| System-State Tool | `app/services/tools/evaluate_system_states.py` | no | `72cec7d0e948ae83292bbf9113fc43ed4d9948da79dc5ca558588bb6ace2a044e0` | Placeholder response; real system evaluation explicitly not implemented. |
| System-State Spec | `spec/system_state_evaluation_v0.1.md` | no | `df66ee59c189bb8980453c53791900267a6304036dda656b9cb65987376ac200` | High-risk prototype using thresholds and the worst-core-marker rule. Separate governance required. |
| DMIE Spec and Rules | `spec/dmie_engine_spec_v0.1.md`, `spec/dmie_rules_v0.1.md` | no | `da51e437539b3a5ca7d9ea5ad950cbc7c8d13a281b6814ab4c05f0cfda07890b` / `0bfa3189bb5fe7bebba245861a6e9c48d653bca5e99df2b3eaf7ee22578c874d` | Draft downstream trigger/action concepts; Registry membership must not enable them. |
| Freshness Spec | `spec/freshness_engine_spec_v0.1.md` | no | `1ad27151f41b9589a6efba915440d3f93f4c5fdfc4d660ff262531be3ec7d492` | Draft time-validity rules with fixed legacy windows; candidate provenance input only. |
| Accuracy Spec | `spec/accuracy_rules_spec_v0.1.md` | no | `83ad9943316d1131c5c85dc15ddec9d16d3ea643e1bf4744c0d96088a4db3fd5` | Draft source hierarchy; source quality must not be confused with scientific evidence. |
| Registry Loading Spec | `agent/agent_registry_loading_spec.v0.1.md` | no | `34b3fef63851ac5a16bf27a914892bbd60616b9b5701c1b4358f20816eee45e1` | Draft runtime contract that names system/biomarker registries as future required inputs. |
| Current Registry Loader | `app/agent_runtime/registry_loader.py` | no | `5755078c248618d1af32d8ca7dad214d304d65ab62c19f6636670a8b596bdfb5` | Loads capability-boundary and A2A assets, not the legacy biomarker registry. |
| Four B2-A Foundations | `KN-T0403-0001`, `KN-T0403-0002`, `KN-T0408-0001`, `KN-T0501-0001` | yes | `662ff79916a921d7364c8a2671f396ee320ad22a82d19e96173cfb9bacece5ba`, `f4cade236e972bd1b7e4a0e78a03d3e445e928b859d53117a0f7a2576704fc3f`, `0213c6e49c0bce9dbc4e171ce4ee90fc6113e5087134a616c6b06d3a69e9ba9d`, `d610e41cbab38d06f77cbabb47ffea8cc42ac3a9d2444b045d9d2f43d0923d8a` | Founder-approved knowledge boundaries for biomarker terminology, variation, device data, and sleep metrics. They are not Registry records. |

### 3.1 Audit conclusion

There is no active, Founder-approved, machine-readable Biomarker and Measurement Registry in the repository. There are useful source inventories and a prototype observation path, but none satisfies the approved information-type, intended-use, method, reference, provenance, six-system, evidence, lifecycle, and Agent-permission model.

The prototype Observation API and its OpenAPI description also disagree on source-medium and accuracy enums. That mismatch confirms that the current observation surface must be reconciled later rather than treated as a Registry schema.

---

## 4. Asset Reconciliation Matrix

| Asset / Family | Current Role | Quality | Overlap | Proposed Migration Status | Action |
| --- | --- | --- | --- | --- | --- |
| Registry MVP Spec | Canonical conceptual authority | high | None at same authority level | `retain_as_governance` | Use as the controlling design baseline. |
| Evidence Contract | Canonical evidence/output authority | high | Evidence fields in legacy files | `retain_as_governance` | Bind sources and grades to claims/intended uses. |
| UHIL MVP + User Health Context | Private-data boundary | medium; documentation only | Older UHIL draft and Observation prototype | `partially_migrate` | Reuse permission/provenance principles; do not reuse as public Registry storage. |
| Older UHIL Spec | Historical private-layer draft | medium | Newer UHIL documents | `reference_only` | Preserve for history and timeline ideas; do not establish duplicate authority. |
| 12-item Biomarker JSON | Small mixed inventory | low-to-medium | 23-item registry and legacy table | `partially_migrate` | Reuse aliases/names after type, unit, and source verification. |
| 23-item Biomarker Registry | Agent-routing inventory | medium for codes; low for governance | 12-item JSON, minimum set, map v0.2 | `partially_migrate` | Treat codes as aliases, not stable Registry IDs. Split non-biomarker types. |
| Approx. 120-item legacy schema | Broad source inventory | broad but shallow | Repeats items across sections | `reference_only` | Deduplicate into concepts; reject unverified ranges, frequency, and optimal-target fields. |
| Six-System Minimum Set | Product minimum-set proposal | low-to-medium; high-risk semantics | System state and DMIE specs | `reference_only` | Use for candidate discovery only. Do not migrate core/supporting or worst-marker behavior. |
| System Map v0.1 | Placeholder skeleton | low | Superseded conceptually by v0.2 | `supersede` | Preserve history; do not migrate placeholder rows. |
| System Map v0.2 | Non-final grouped mapping inventory | medium | Minimum set and system baselines | `partially_migrate` | Split grouped rows into item concepts; review each biological/product relationship. |
| v0.2 review/acceptance chain | Decision and audit history | medium-to-high for provenance | Repeats the map's non-final boundary | `reference_only` | Retain as source for migration rationale and unresolved ownership. |
| v0.2 context-layer spec | Auxiliary-context design | medium | Registry information types and six-system model | `partially_migrate` | Reuse context/product-grouping distinctions without creating a seventh system. |
| v0.2 validator/tests | Prototype safety linting | medium for old format | Future Registry validator not defined | `keep_prototype` | Do not repurpose until a machine-readable Registry schema is approved. |
| System Registry | Six-system product codes/state model | medium | Taxonomy and system-map assets | `partially_migrate` | Reuse identifiers only after T03 alignment; do not migrate state scoring. |
| Observation request/response | Result-instance prototype | medium | `app/main.py`, OpenAPI | `partially_migrate` | Preserve basic value/time/source concepts; add Registry version, method, report, interval, flags, verification, and permission later. |
| `app/main.py` Observation model | Tracked prototype implementation | medium | OpenAPI enum mismatch | `keep_prototype` | No runtime change in Seed planning. Future migration must be explicit and backward compatible. |
| OpenAPI Observation model | Tracked contract prototype | medium | Differs from `app/main.py` | `needs_founder_review` | Reconcile only after Registry schema and observation event model are approved. |
| User-context/system-state tools | Placeholder tool layer | low | UHIL and system-state documents | `keep_prototype` | Do not infer production readiness. |
| System-state evaluation | Proposed derived assessment | high risk | Minimum set, thresholds, DMIE | `reference_only` | Keep separate. No Registry record may activate a system score. |
| DMIE engine/rules | Future consumer/action layer | high risk | Freshness, state, measurement triggers | `reference_only` | Registry may supply metadata; DMIE requires an independent Founder Gate. |
| Freshness spec | Observation time-validity proposal | medium | Registry frequency and observation freshness | `partially_migrate` | Reuse concepts, not fixed windows. Freshness is observation/use-context specific. |
| Accuracy spec | Source-reliability proposal | medium | Provenance and evidence grading | `partially_migrate` | Reuse provenance vocabulary cautiously; do not equate source tier with evidence grade. |
| Registry loading spec/runtime loader | General runtime infrastructure | mixed | Legacy Registry source-of-truth language | `reference_only` | Reconcile only after storage format and active lifecycle are approved. |
| B2-A knowledge entries | Canonical public knowledge | high | Registry item definitions | `retain_as_governance` | Link future items to concepts; never migrate prose into item data mechanically. |
| Unknown external `biomarker_observations` DDL | Runtime dependency not present in audit | unknown | `app/main.py` SQL assumptions | `needs_founder_review` | Locate and review before any persistence migration. |

No asset is deleted by this plan.

---

## 5. Legacy, Prototype, and Duplicate Findings

1. The 12-item and 23-item JSON inventories overlap heavily but use different identifiers such as `rhr` versus `resting_heart_rate` and `fpg` versus `fasting_glucose`.
2. The legacy table repeats the same concept under multiple systems and sometimes under multiple names, such as HRV, lean mass, vitamin D, VO2max, CAC, and DEXA records.
3. The 27-row v0.2 map intentionally groups multiple concepts in single rows, including `glucose / HbA1c`, `fasting insulin / HOMA-IR / CGM`, `ApoB / LDL-C`, `CBC / WBC pattern`, and `liver / kidney markers`. Registry records must split these.
4. Old assets call sleep quality, cognitive score, user context, and device-derived values biomarkers. The approved information-type model requires separate classification.
5. Legacy `optimal_range`, single `reference_range`, fixed freshness windows, and measurement-frequency fields cannot be migrated without intended-use and source review.
6. System ownership in old assets is mostly one-to-one. The approved model requires many-to-many relationships and separation of biological relationship from product grouping.
7. The Observation request, response, OpenAPI, and Python model are overlapping but inconsistent. They are result-instance prototypes, not Registry definitions.
8. The database DDL for `biomarker_observations` was not found in the audited repository and remains an unknown dependency.

---

## 6. Proposed Migration Strategy

Each future Registry item should retain migration metadata:

- `source_asset`
- `migration_status`
- `supersedes`
- `superseded_by`
- `duplicate_of`
- `migration_note`

Migration must proceed concept by concept:

```text
source label
-> normalize identity and aliases
-> split grouped rows
-> classify information type
-> verify specimen/source and method
-> review intended use
-> map standards and units
-> review six-system relationships
-> verify evidence and boundaries
-> Founder Gate
-> active only after approval
```

Legacy codes remain aliases until explicitly mapped. A new Registry item must not silently rewrite historical observations that used a legacy code or method.

---

## 7. Seed 001 Scope

### 7.1 Core Seed

Proposed Core Seed size:

```text
48 measurement concepts
```

The Core Seed is a proposed review set, not 48 active records. It is intentionally broad enough to exercise laboratory, physiological, device, sleep, derived-score, and functional-measurement structures while remaining small enough for item-level review.

### 7.2 Extended Candidate Pool

The legacy table contains 107 unique textual labels before semantic deduplication; the v0.2 map adds 27 grouped rows, many of which overlap or require splitting. The proposed Extended Candidate Pool target is:

```text
75-100 deduplicated concepts, proposed / not canonical
```

The exact count remains open until identity normalization. A raw label count is not a Registry completeness claim.

### 7.3 Scope exclusions

Seed 001 does not attempt to cover all known biomarkers, all lab catalogs, all wearable metrics, all questionnaires, all imaging, all omics, all aging clocks, or every proprietary score.

---

## 8. Information Types

Seed 001 adopts the approved canonical names from the Registry MVP Spec:

| Information Type | Core Seed Coverage | Boundary |
| --- | --- | --- |
| `laboratory_biomarker` | yes | Intended use and method must be reviewed. |
| `molecular_biomarker` | later | Omics and research markers remain P2 unless separately selected. |
| `physiological_measurement` | yes | One reading is not a diagnosis or complete system state. |
| `functional_performance_measurement` | yes | Protocol, effort, equipment, and context must be retained. |
| `imaging_derived_measure` | extended pool | Modality, protocol, reader/software, and clinical context are required. |
| `device_measured_signal` | yes | Device, body site, sampling, calibration, and validation matter. |
| `device_estimated_metric` | yes | Estimated/inferred status and algorithm version must be explicit. |
| `derived_score_index` | yes | Inputs, formula/version, validation population, and use limits are required. |
| `patient_user_reported_state` | extended/private context | Not a biomarker or scientific evidence by default. |
| `validated_questionnaire_scale` | extended pool | Version, language, scoring, rights, sensitivity, and diagnostic boundary required. |
| `behavior_lifestyle_record` | later event/timeline layer | A record does not prove a health effect. |
| `demographic_social_context` | private context | Permission-gated and not a Registry biomarker. |
| `exposure_environment_context` | later/context layer | Exposure and biological response are distinct. |
| `clinical_record` | private context | A document can contain measurements but is not itself a biomarker. |
| `diagnosis_medication_procedure` | private context | Does not authorize Congtie to change care. |
| `specimen_measurement_metadata` | required support metadata | Metadata changes interpretation but is not the result. |

---

## 9. Stable ID Principle

Candidate ID namespaces remain:

```text
BM-000001 = laboratory or molecular biomarker
ME-000001 = physiological or functional measurement
SC-000001 = derived score or index
QS-000001 = validated questionnaire or scale
```

The six-system taxonomy is not encoded into the ID. `BM-T0302-0001` and similar designs are prohibited because one item can map to multiple systems.

Every ID in this document is `proposed / not active`. Final assignment order requires Founder approval. Device-estimated categorical metrics and other types that do not fit the four approved namespaces require a separate ID-governance decision rather than an improvised prefix.

---

## 10. Candidate Prioritization

### P0-A - Laboratory foundations

- high-frequency lipid, glycemic, renal, liver-related, hematology, inflammation, thyroid, and selected nutrition measurements;
- actual analytes rather than grouped organ panels;
- no automatic testing frequency or universal range.

### P0-B - Basic physiological measurements

- blood pressure, heart rate, body size/composition, temperature, respiratory rate, and oxygen saturation;
- method and device profiles remain explicit.

### P0-C - Wearable and sleep measurements

- direct signals, algorithm estimates, and derived metrics remain separately typed;
- sleeping heart rate and nocturnal HRV are source/window profiles of heart rate and HRV unless later review justifies separate concepts.

### P0-D - Derived scores

- a small representative set proves formula/version and proprietary-algorithm support;
- generic score concepts do not imply cross-brand comparability.

### P0-E - Functional measurements

- cardiorespiratory fitness, grip strength, gait/mobility, and balance;
- no thresholds or personal performance target in Seed definition.

---

## 11. Proposed Core Seed Candidate List

Legend for existing asset sources:

- `BR23`: `spec/biomarker_registry.v0.1.json`
- `BS12`: `schemas/biomarker_schema_v0.1.json`
- `LEGACY120`: `spec/biomarker_schema_v0.1.md`
- `MIN6`: `spec/system_minimum_biomarkers_v0.1.md`
- `MAP2`: `agent/biomarker_system_map.v0.2.draft.json`
- `B2A`: Founder-approved B2-A knowledge entries

System mappings are preliminary. `P` means proposed product primary grouping; `S` means proposed secondary relationship candidates. They do not establish diagnosis, biological ownership, or actionability.

| Candidate | Proposed ID | Type | Primary Use Context | Specimen / Source | System Mapping | Existing Asset Source | Priority | Migration Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total cholesterol / 总胆固醇 | `BM-000001` proposed / not active | `laboratory_biomarker` | lipid context | serum/plasma lab | P:T03.03; S:T03.02 | LEGACY120, MAP2 | P0-A | `partially_migrate` |
| LDL cholesterol / 低密度脂蛋白胆固醇 | `BM-000002` proposed / not active | `laboratory_biomarker` | lipid/atherosclerotic context | serum/plasma lab | P:T03.03; S:T03.02,T03.05 | LEGACY120, MAP2 | P0-A | `partially_migrate` |
| HDL cholesterol / 高密度脂蛋白胆固醇 | `BM-000003` proposed / not active | `laboratory_biomarker` | lipid context | serum/plasma lab | P:T03.02; S:T03.03 | BR23, LEGACY120, MIN6, MAP2 | P0-A | `partially_migrate` |
| Triglycerides / 甘油三酯 | `BM-000004` proposed / not active | `laboratory_biomarker` | lipid/metabolic context | serum/plasma lab | P:T03.02; S:T03.03 | BR23, LEGACY120, MIN6, MAP2 | P0-A | `partially_migrate` |
| Apolipoprotein B / 载脂蛋白B | `BM-000005` proposed / not active | `laboratory_biomarker` | atherogenic particle context | serum/plasma lab | P:T03.03; S:T03.02,T03.05 | BR23, BS12, LEGACY120, MIN6, MAP2 | P0-A | `partially_migrate` |
| Lipoprotein(a) / 脂蛋白(a) | `BM-000006` proposed / not active | `laboratory_biomarker` | lipid/risk context | serum/plasma lab | P:T03.03; S:T03.02 | BR23, LEGACY120, MIN6, MAP2 | P0-A | `partially_migrate` |
| Fasting plasma glucose / 空腹血糖 | `BM-000007` proposed / not active | `laboratory_biomarker` | glycemic context | plasma lab; fasting context | P:T03.02; S:T03.01,T03.05,T03.06 | BR23, BS12, LEGACY120, MIN6, MAP2 | P0-A | `partially_migrate` |
| HbA1c / 糖化血红蛋白 | `BM-000008` proposed / not active | `laboratory_biomarker` | longer-window glycemic context | whole blood lab | P:T03.02; S:T03.01,T03.03 | BR23, BS12, LEGACY120, MIN6, MAP2 | P0-A | `partially_migrate` |
| Fasting insulin / 空腹胰岛素 | `BM-000009` proposed / not active | `laboratory_biomarker` | insulin/metabolic context | serum/plasma lab; fasting context | P:T03.02; S:T03.01,T03.05 | LEGACY120, MIN6, MAP2 | P0-A | `partially_migrate` |
| Creatinine / 肌酐 | `BM-000010` proposed / not active | `laboratory_biomarker` | renal/organ context | serum/plasma lab | P:pending; S:T03.02,T03.06,T03.01 | LEGACY120, MAP2 grouped | P0-A | `needs_founder_review` |
| Alanine aminotransferase / 丙氨酸氨基转移酶 | `BM-000011` proposed / not active | `laboratory_biomarker` | liver-related context | serum/plasma lab | P:pending; S:T03.02,T03.06 | LEGACY120, MAP2 grouped | P0-A | `needs_founder_review` |
| Aspartate aminotransferase / 天门冬氨酸氨基转移酶 | `BM-000012` proposed / not active | `laboratory_biomarker` | liver/muscle context | serum/plasma lab | P:pending; S:T03.02,T03.04,T03.06 | LEGACY120, MAP2 grouped | P0-A | `needs_founder_review` |
| Gamma-glutamyl transferase / γ-谷氨酰转移酶 | `BM-000013` proposed / not active | `laboratory_biomarker` | liver-related context | serum/plasma lab | P:pending; S:T03.02,T03.06 | LEGACY120, MAP2 grouped | P0-A | `needs_founder_review` |
| Albumin / 白蛋白 | `BM-000014` proposed / not active | `laboratory_biomarker` | liver/nutrition/organ context | serum/plasma lab | P:pending; S:T03.01,T03.02,T03.06 | LEGACY120, MAP2 grouped | P0-A | `needs_founder_review` |
| Hemoglobin / 血红蛋白 | `BM-000015` proposed / not active | `laboratory_biomarker` | hematology/oxygen context | whole blood lab | P:T03.01; S:T03.03,T03.06 | LEGACY120, MIN6 | P0-A | `partially_migrate` |
| White blood cell count / 白细胞计数 | `BM-000016` proposed / not active | `laboratory_biomarker` | hematology/immune context | whole blood lab | P:T03.06; S:T03.01 | BR23, LEGACY120, MIN6, MAP2 | P0-A | `partially_migrate` |
| Platelet count / 血小板计数 | `BM-000017` proposed / not active | `laboratory_biomarker` | hematology context | whole blood lab | P:T03.06; S:T03.03 | MAP2 grouped/CBC source family | P0-A | `partially_migrate` |
| High-sensitivity C-reactive protein / 高敏C反应蛋白 | `BM-000018` proposed / not active | `laboratory_biomarker` | inflammation context | serum/plasma lab | P:T03.06; S:T03.03,T03.01,T03.02 | BR23, BS12, LEGACY120, MIN6, MAP2 | P0-A | `partially_migrate` |
| Thyroid-stimulating hormone / 促甲状腺激素 | `BM-000019` proposed / not active | `laboratory_biomarker` | thyroid context | serum/plasma lab | P:pending; S:T03.01,T03.02,T03.05 | LEGACY120, MAP2 grouped | P0-A | `needs_founder_review` |
| Free thyroxine / 游离甲状腺素 | `BM-000020` proposed / not active | `laboratory_biomarker` | thyroid context | serum/plasma lab | P:pending; S:T03.01,T03.02,T03.05 | LEGACY120, MAP2 grouped | P0-A | `needs_founder_review` |
| Ferritin / 铁蛋白 | `BM-000021` proposed / not active | `laboratory_biomarker` | iron/inflammation context | serum/plasma lab | P:pending; S:T03.06,T03.01,T03.05,T03.04 | LEGACY120, MIN6, MAP2 | P0-A | `needs_founder_review` |
| 25-hydroxyvitamin D / 25-羟维生素D | `BM-000022` proposed / not active | `laboratory_biomarker` | selected nutrient context | serum/plasma lab | P:T03.04; S:T03.06,T03.01 | BR23, LEGACY120, MIN6, MAP2 | P0-A | `partially_migrate` |
| Systolic blood pressure / 收缩压 | `ME-000001` proposed / not active | `physiological_measurement` | pressure/load context | cuff or validated device | P:T03.03; S:T03.02,T03.01 | BR23, BS12, LEGACY120, MIN6, MAP2 | P0-B | `partially_migrate` |
| Diastolic blood pressure / 舒张压 | `ME-000002` proposed / not active | `physiological_measurement` | pressure/load context | cuff or validated device | P:T03.03; S:T03.02,T03.01 | BR23, BS12, LEGACY120, MIN6, MAP2 | P0-B | `partially_migrate` |
| Heart rate / 心率 | `ME-000003` proposed / not active | `physiological_measurement` | resting/sleep/activity context | clinical/home/device | P:pending; S:T03.03,T03.01,T03.05 | BR23 resting profile, BS12, LEGACY120, MAP2 | P0-B/C | `partially_migrate` |
| Heart-rate variability / 心率变异性 | `ME-000004` proposed / not active | `physiological_measurement` or `device_estimated_metric` by source | autonomic/context trend | ECG/device; metric and window required | P:pending; S:T03.03,T03.01,T03.05 | BR23, BS12, LEGACY120, MIN6, MAP2, B2A | P0-C | `needs_founder_review` |
| Body weight / 体重 | `ME-000005` proposed / not active | `physiological_measurement` | body-size context | calibrated scale/home device | P:T03.02; S:T03.04,T03.01 | LEGACY120, MAP2 | P0-B | `partially_migrate` |
| Waist circumference / 腰围 | `ME-000006` proposed / not active | `physiological_measurement` | body-size/adiposity context | standardized manual measurement | P:T03.02; S:T03.04,T03.03 | BR23, LEGACY120, MIN6, MAP2 | P0-B | `partially_migrate` |
| Body fat percentage / 体脂率 | `ME-000007` proposed / not active | `physiological_measurement` or `device_estimated_metric` by method | body-composition context | DXA/BIA/device; method required | P:T03.02; S:T03.04 | LEGACY120, MAP2 | P0-B | `needs_founder_review` |
| Body temperature / 体温 | `ME-000008` proposed / not active | `physiological_measurement` | physiological/safety context | site- and method-specific | P:pending; S:T03.06,T03.01 | new Seed candidate | P0-B | `needs_founder_review` |
| Skin temperature signal / 皮肤温度信号 | `ME-000009` proposed / not active | `device_measured_signal` | wearable trend context | wearable/device; body site required | P:pending; S:T03.01,T03.06 | B2A/Registry Spec | P0-C | `needs_founder_review` |
| Respiratory rate / 呼吸频率 | `ME-000010` proposed / not active | `physiological_measurement` or `device_estimated_metric` by source | respiratory/sleep context | clinical/device | P:T03.03; S:T03.01 | LEGACY120, B2A | P0-B/C | `partially_migrate` |
| Oxygen saturation / 血氧饱和度 | `ME-000011` proposed / not active | `physiological_measurement` or `device_estimated_metric` by source | oxygenation context | clinical/home/device | P:T03.03; S:T03.01 | LEGACY120, B2A | P0-B/C | `partially_migrate` |
| Sleep duration / 睡眠时长 | `ME-000012` proposed / not active | `physiological_measurement` or `device_estimated_metric` by source | sleep duration trend | diary/device/clinical | P:T03.01; S:T03.05,T03.02,T03.06 | BR23, LEGACY120, MIN6, MAP2, B2A | P0-C | `partially_migrate` |
| Sleep latency / 入睡潜伏期 | `ME-000013` proposed / not active | `physiological_measurement` or `device_estimated_metric` by source | sleep continuity | diary/device/clinical | P:T03.05; S:T03.01 | B2A | P0-C | `partially_migrate` |
| Wake after sleep onset / 入睡后清醒时间 | `ME-000014` proposed / not active | `physiological_measurement` or `device_estimated_metric` by source | sleep continuity | diary/device/clinical | P:T03.05; S:T03.01 | B2A | P0-C | `partially_migrate` |
| Cardiorespiratory fitness / VO2max-related result / 心肺适能相关测量 | `ME-000015` proposed / not active | `functional_performance_measurement` | capability tracking | exercise test/device estimate profile | P:T03.03; S:T03.01,T03.04 | BR23, BS12, LEGACY120, MIN6, MAP2 | P0-E | `needs_founder_review` |
| Grip strength / 握力 | `ME-000016` proposed / not active | `functional_performance_measurement` | strength/function context | dynamometry protocol | P:T03.04; S:T03.01,T03.05 | BR23, LEGACY120, MIN6, MAP2 | P0-E | `partially_migrate` |
| Gait speed / 步速 | `ME-000017` proposed / not active | `functional_performance_measurement` | mobility/function context | standardized functional test | P:T03.04; S:T03.05,T03.01 | BR23, LEGACY120, MAP2 | P0-E | `partially_migrate` |
| Balance test measure / 平衡测试测量 | `ME-000018` proposed / not active | `functional_performance_measurement` | balance/function context | named functional protocol | P:T03.04; S:T03.05 | LEGACY120 | P0-E | `partially_migrate` |
| Estimated glomerular filtration rate / 估算肾小球滤过率 | `SC-000001` proposed / not active | `derived_score_index` | renal/organ context | derived from lab inputs; equation/version required | P:pending; S:T03.02,T03.06,T03.01 | LEGACY120, MAP2 grouped | P0-A | `needs_founder_review` |
| Body mass index / 体重指数 | `SC-000002` proposed / not active | `derived_score_index` | body-size context | height and weight | P:T03.02; S:T03.04 | MAP2 | P0-B | `partially_migrate` |
| Sleep efficiency / 睡眠效率 | `SC-000003` proposed / not active | `derived_score_index` | sleep continuity | diary/device/clinical; denominator required | P:T03.01; S:T03.05 | LEGACY120, B2A | P0-C | `partially_migrate` |
| Sleep regularity index / 睡眠规律指数 | `SC-000004` proposed / not active | `derived_score_index` | sleep regularity | event series; formula/version required | P:T03.01; S:T03.05,T03.02 | B2A | P0-C | `needs_founder_review` |
| Sleep score / 睡眠评分 | `SC-000005` proposed / not active | `derived_score_index` | device sleep summary | proprietary device algorithm | P:T03.01; S:T03.05 | BR23 legacy sleep quality, MIN6, B2A | P0-D | `partially_migrate` |
| Recovery score / 恢复评分 | `SC-000006` proposed / not active | `derived_score_index` | device recovery context | proprietary device algorithm | P:T03.01; S:T03.04,T03.05 | B2A | P0-D | `needs_founder_review` |
| Readiness score / 准备度评分 | `SC-000007` proposed / not active | `derived_score_index` | device readiness context | proprietary device algorithm | P:T03.01; S:T03.04,T03.05 | B2A | P0-D | `needs_founder_review` |
| Device stress estimate / 设备压力估算 | `SC-000008` proposed / not active | `derived_score_index` | contextual stress proxy | proprietary device algorithm | P:T03.05; S:T03.01,T03.02,T03.06 | B2A | P0-D | `needs_founder_review` |

### 11.1 Candidate-count check

- `BM`: 22 proposed IDs
- `ME`: 18 proposed IDs
- `SC`: 8 proposed IDs
- total: 48 proposed IDs
- duplicate proposed IDs: 0
- active Registry records created: 0

---

## 12. Extended Candidate Pool

The Extended Candidate Pool should retain, but not yet activate, candidates such as:

- cystatin C, BUN, ALP, bilirubin, uric acid, hematocrit, red blood cell count, differential counts, NLR, ApoA1, non-HDL-C, fibrinogen, homocysteine, and selected cardiac markers;
- vitamin B12, folate, magnesium, zinc, omega-3 index, and other context-specific nutrient measurements;
- selected sex/reproductive and endocrine measurements only after intended-use and life-stage review;
- DXA-derived measures, bone mineral density, coronary calcium, pulse-wave velocity, and other imaging-derived measures;
- sleep timing event concepts, sleep-stage estimates, device-specific nocturnal heart-rate/HRV profiles, and energy-expenditure estimates;
- chair-stand, reaction-time, and cognitive-performance measurements;
- validated questionnaire/scale metadata such as PSQI, PSS, PHQ-9, or GAD-7 only after version, language, license, clinical sensitivity, and safety review;
- biological-age estimates, aging clocks, omics, inflammatory cytokines, and low-actionability commercial measures as P2/research-only candidates.

No Extended Candidate Pool item receives an active ID in this document.

---

## 13. Required, Conditional, and Optional Fields

### 13.1 Required for Seed review

- proposed/stable `registry_id` and lifecycle status;
- canonical Chinese and English names;
- aliases and legacy codes;
- `information_type`;
- intended use and use context;
- specimen or measurement source;
- value type;
- canonical unit or `not_applicable`;
- method/platform requirement;
- preliminary six-system mappings with relationship type;
- evidence/source references and source roles;
- interpretation limitations;
- safety and escalation boundary;
- permitted Agent use;
- prohibited Agent use;
- migration metadata.

### 13.2 Conditionally required

- reference-interval model;
- clinical decision limit, risk threshold, or critical value when applicable;
- LOINC, UCUM, China standard, local lab, or partner code mapping;
- specimen subtype and collection conditions;
- analytical interference and preanalytical confounders;
- algorithm/formula/version and validation context;
- questionnaire language, scoring, rights, and population;
- method comparability and trend-breakpoint rules;
- regulatory classification.

### 13.3 Optional or later enrichment

- detailed biological variation and RCV-specific data;
- method-equivalence studies;
- transport/stability detail beyond current product need;
- complete external ontology mapping;
- full validation-cohort detail;
- China-specific population interval enrichment.

Missing optional fields must not be invented and must not automatically reject a proposed Seed item.

---

## 14. Reference and Threshold Model

The following remain six separate structures:

1. `laboratory_reported_reference_interval`
2. `population_reference_interval`
3. `guideline_clinical_decision_limit`
4. `risk_associated_threshold`
5. `critical_alert_value`
6. `future_personalized_target`

`normal_range` must not be used as a universal umbrella. Every user observation preserves the original laboratory-reported interval, unit, method, population/context note, and report provenance. Registry context may be displayed alongside it but must not overwrite it.

---

## 15. Provenance

A future observation should be able to link to:

- user and permission scope;
- Registry item and Registry version;
- observation date/time;
- original result and value type;
- original and verified canonical units;
- specimen, matrix, and collection context;
- source organization;
- laboratory, device, or questionnaire;
- method/platform and assay, firmware, or algorithm version;
- original report/source artifact;
- original reference interval and flag;
- freshness, verification, and mapping state;
- correction/supersession history.

```text
User observation != Registry definition
```

The Registry does not store a user's personal baseline, trend, consent record, or observation result.

---

## 16. Method and Platform Comparability

The Seed design must support:

- `method_comparability_status`
- `validated_conversion_rule`
- `harmonization_reference`
- `method_change_breakpoint`
- `trend_comparability_note`
- `cross_platform_comparison_prohibited`

Laboratory, assay, platform, device, firmware, or algorithm changes may create a trend breakpoint. A mathematically convertible unit does not prove method comparability. There is no default generic `assay_equivalence_factor`, and Congtie must not normalize unlike results automatically.

---

## 17. Six-System Mapping

Registry mapping is many-to-many across:

- `T03.01` Energy System / 能量系统
- `T03.02` Metabolic System / 代谢系统
- `T03.03` Cardiopulmonary System / 心肺循环系统
- `T03.04` Musculoskeletal System / 肌肉骨骼系统
- `T03.05` Neurocognitive System / 神经认知系统
- `T03.06` Repair Immune System / 修复免疫系统

Each mapping should support:

- `primary_system_id`
- `secondary_system_ids`
- `relationship_type`
- `mapping_rationale`
- `mapping_source`
- `mapping_evidence_level`
- `mapping_confidence`
- `cross_system_note`

`biological_relationship` and `product_grouping` are different. Product grouping can provide one display home without asserting unique biological ownership. Mapping alone cannot diagnose a system, generate a score, set measurement frequency, or authorize an intervention.

---

## 18. Evidence and Citation Integration

The target traceability chain is:

```text
answer claim
-> canonical knowledge entry
-> Registry item and intended use
-> authorized personal observation
-> source organization, specimen, method, and platform
-> laboratory interval or separately labeled threshold
-> external evidence source
```

Required design principles:

- Registry item existence is not an evidence claim;
- evidence level binds to a claim, intended use, method, population, and scope;
- one item may have different evidence scopes for risk association, diagnosis support, monitoring, response, or wellness tracking;
- user observation is Personal Context Basis, not scientific evidence;
- source role and verification status must be explicit;
- future answer rendering must preserve privacy and authorization.

---

## 19. China Context

Seed production must plan for:

- Chinese laboratory report naming and aliases;
- units commonly reported in China and verified UCUM representations;
- laboratory- and method-specific reference intervals;
- applicable WS/T and other Chinese standards;
- future local/partner laboratory code mapping;
- China-specific population and clinical-decision sources when relevant;
- regulatory and personal-data classification review.

迪安诊断、金域医学、home sampling providers, and 顺丰 or comparable logistics remain planned candidate ecosystem references only. No signed-partnership evidence was identified in the audited assets, and this document does not describe any of them as a confirmed partner.

---

## 20. Service Panel Boundary

```text
Registry = broad canonical measurement foundation
Service Panel = curated subset for one service objective
```

Future Panel views may include Core Baseline, Follow-up, Age/Sex/Context Module, Conditional Add-on, and Research/Emerging. Panel size is not a quality metric; not every marker should be measured in every user; frequency is item- and context-specific.

This document does not create a Panel, testing package, price list, sampling workflow, or order set.

---

## 21. Critical-Result Governance Dependency

Before Congtie operates any laboratory testing service, an independent P0 `Critical Result / Clinical Escalation Governance` Gate must define:

- who receives and reviews a critical result;
- required contact timing;
- receipt confirmation and failed-contact handling;
- emergency/professional escalation;
- laboratory, sampling provider, and Congtie responsibilities;
- what AI may and may not communicate or decide.

This is a service-launch dependency, not a Registry item-definition field set. No clinical operating protocol is created here.

---

## 22. User-Health Data Implementation Dependency

Registry metadata is public definition data. Approval of a Registry concept would not authorize production storage of personally identifiable health data.

Before production user-health storage, separate Gates must cover:

- consent and revocation;
- authentication and least privilege;
- encryption;
- retention, export, correction, and deletion;
- audit and backup;
- third-party sharing and cross-border transfer;
- model-context use and privacy-safe rendering.

---

## 23. Parallel P0 Product Infrastructure

The following remain deferred/parallel:

1. User Health Event / Longitudinal Timeline
2. Proactive Context Completion / Reminder / Result Follow-Up
3. Multimodal Dietary Intake Ingestion
4. Clinician-Ready Longitudinal Summary

Their relationship is:

```text
Registry = what the item means
User Health Event = what happened to the user
Observation = what was measured
Timeline = how events and observations evolve
Clinician Summary = selected longitudinal synthesis
```

None is implemented by this document.

---

## 24. Seed 001 Production Workflow

```text
asset discovery
-> deduplication
-> candidate selection
-> canonical concept definition
-> source verification
-> standards/code mapping
-> six-system mapping
-> evidence/use-context review
-> AI review
-> Founder review
-> active
```

Recommended production waves:

1. Wave 1: 8-12 laboratory and basic physiological concepts to validate record structure.
2. Wave 2: remaining Core Seed laboratory and derived concepts.
3. Wave 3: wearable/sleep and functional concepts, including algorithm/version boundaries.
4. Wave 4: extended candidates only after Core Seed review findings are incorporated.

Each wave should include migration notes, item-level source verification, AI review, and Founder review. No batch promotion from legacy status is allowed.

---

## 25. Founder Decision Gates

Founder review is required for:

1. exact Core Seed 001 candidate set;
2. exact stable ID assignment and whether the proposed order is retained;
3. ID treatment for device-estimated categorical metrics and other types outside BM/ME/SC/QS;
4. first Registry storage format;
5. canonical machine-readable schema;
6. migration, supersession, or archival treatment of legacy assets;
7. preliminary six-system product groupings and unresolved organ-context ownership;
8. China-specific code and standard mapping priority;
9. initial Service Panel timing;
10. critical-result governance timing;
11. observation model and OpenAPI reconciliation;
12. production user-health storage and consent Gates.

---

## 26. Explicit Non-Authorizations

This draft does not authorize:

- active Registry records;
- production database, API, runtime, loader, index, or UI;
- migration or deletion of existing JSON or documentation;
- system-state scoring, diagnosis, risk calculation, treatment, or intervention;
- automatic measurement recommendations or DMIE triggers;
- a Service Panel or laboratory order;
- confirmed partner claims or service integration;
- critical-result operations;
- production personal-health-data storage or sharing;
- Personalized Longevity Protocol generation;
- B2-B knowledge production;
- git staging, commit, or push.

---

## 27. Recommended Next Step

Founder reviews:

1. asset reconciliation decisions;
2. the proposed 48-concept Core Seed set;
3. the exact Seed 001 production boundary;
4. stable-ID assignment timing.

After Founder approval, create the first small Registry Seed production wave under a separate task. Do not create active Registry items automatically from this draft.
