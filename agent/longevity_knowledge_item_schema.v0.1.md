# Longevity Knowledge Item Schema v0.1

Version: v0.1  
Project: Congtie  
Status: Draft  
Owner: Congtie Agent Team  
Last Updated: 2026-08-07  
Founder Gate: Approved for documentation-only conceptual schema on 2026-08-07

---

## 1. Purpose

This document defines the conceptual schema for one versioned entry in the Congtie Longevity Information Library.

It specifies required and optional fields, conceptual field types, enums, validation rules, relationship constraints, information-layer requirements, topic mappings, content-type extensions, and safety boundaries.

This document is a conceptual schema. It is not:

- a database schema
- an API contract
- a runtime model
- a JSON Schema implementation
- a CMS form implementation
- a persistence model

The canonical content source remains:

```text
Markdown files + Git repository
```

Any executable schema, API contract, runtime model, persistent model, or external integration requires a separate task and any applicable Founder Gate approval.

### 1.1 Reference Files

This schema aligns with the files that currently exist in the repository:

```text
agent/longevity_knowledge_base/templates/longevity_knowledge_item_template.v0.1.md
agent/knowledge_seed_v0/longevity_information_library_architecture.v0.1.md
agent/knowledge_seed_v0/longevity_information_library_architecture_patch_for_taxonomy.v0.1.md
agent/knowledge_seed_v0/longevity_topic_taxonomy.v0.1.md
agent/knowledge_seed_v0/evidence_grading_framework.v0.1.md
```

The task brief referenced root-level architecture and taxonomy paths. The current repository versions are under `agent/knowledge_seed_v0/`; those files are the alignment source for this document.

---

## 2. Relationship with Architecture

The Longevity Information Library architecture defines the vertical information layer and governance structure. This schema translates that architecture into entry-level metadata rules.

The five information layers are:

```text
knowledge
action_resource
progress_and_viewpoints
education
governance
```

Each entry must belong to exactly one primary `information_layer`. The selected layer determines valid content types, conditional fields, actionability metadata, R0/R1/R2/R3 requirements, and safety boundaries.

Architecture rules preserved by this schema:

- Evidence level supports clearer explanation but does not authorize stronger intervention.
- Action resources remain permission-controlled.
- Progress and viewpoints are not stable knowledge by default.
- Education remains non-clinical.
- Governance defines curation rules but does not create runtime behavior by itself.
- Private user health information remains separate from the public library.

Entry metadata does not independently authorize runtime use. Any future runtime use must also consider human review, status, safety, evidence, visibility, permission, and approved runtime policy.

---

## 3. Relationship with Topic Taxonomy

The Longevity Topic Taxonomy defines the horizontal topic and retrieval map.

Every entry must carry both:

```text
information_layer
topic mapping
```

One topic can contain multiple information layers. For example:

```text
T05.01 Sleep 睡眠

knowledge: sleep basics
action_resource: sleep tracker
progress_and_viewpoints: sleep and aging research
education: sleep diary guide
```

Topic placement does not override evidence, safety, permission, clinical sensitivity, or human review.

Allowed top-level topics:

```text
T01 Longevity Foundation 长寿基础
T02 Longevity Strategy 长寿策略
T03 Body Systems 身体系统
T04 Measurement and Records 测量与记录
T05 Lifestyle Foundations 生活方式基础
T06 Risk Prevention and Safety 风险预防与安全
T07 Interventions and Action Resources 干预与行动资源
T08 Progress and Viewpoints 进展与观点
T09 Education, Experts, Sources and Governance 教育、专家、信源与治理
T10 Pet Longevity 宠物长寿
```

T10 is reserved and disabled in v0 runtime.

---

## 4. Entry Object Definition

Each entry represents one versioned information object. Each canonical Markdown file should contain one entry object.

Conceptual minimum object:

```yaml
schema_version: v0.1
entry_id: ""
entry_slug: ""

content_type: ""
information_layer: ""

title_zh: ""
title_en: ""
summary_zh: ""
summary_en: ""
language: zh-CN

primary_topic_id: ""
topic_ids: []
topic_paths: []

status: draft

created_by: ""
created_date: ""
last_modified_by: ""
last_modified_date: ""
version: v0.1

evidence_level: ""
evidence_posture: ""
source_type: []

safety_boundary: ""
allowed_use: []
disallowed_use: []
is_clinical_sensitive: false
```

### 4.1 Required Core Metadata

All entries require:

```text
schema_version
entry_id
entry_slug
content_type
information_layer
title_zh
title_en
summary_zh
summary_en
language
primary_topic_id
topic_ids
topic_paths
status
created_by
created_date
last_modified_by
last_modified_date
version
evidence_level
evidence_posture
source_type
safety_boundary
allowed_use
disallowed_use
is_clinical_sensitive
```

### 4.2 Optional Common Metadata

```yaml
visibility:
runtime_enabled:
retrieval_enabled:
publish_channels: []

source_urls: []
source_notes:
last_source_check_date:
next_review_date:

commercial_boundary:

related_body_systems: []
related_lifestyle_keywords: []
related_biomarkers: []
related_action_resource_ids: []
related_knowledge_ids: []
related_source_ids: []

china_availability:
regulatory_status:
actionability_status:

status_history: []
change_log: []
attachments: []
```

Optional fields become conditionally required when specified by an information layer, content type, topic, or safety rule.

### 4.3 One Status Field

An entry must use only one workflow status field:

```yaml
status:
```

Do not add parallel workflow authorities such as `review_status`, `approval_status`, `curation_status`, or `publication_status`. Review details may be recorded in reviewer, date, note, and history fields without creating another active status.

---

## 5. Field Specification

Field types below are conceptual Markdown/YAML types. They do not define a programming language type, database column, JSON Schema type, or API serialization contract.

### 5.1 Identity Fields

| Field | Required | Conceptual Type | Rule |
|---|---:|---|---|
| `schema_version` | yes | string | Must be `v0.1` for this schema. |
| `entry_id` | yes | string | Stable, unique, and immutable after publication. |
| `entry_slug` | yes | string | Lowercase English, filename-safe slug. |
| `content_type` | yes | enum string | Must use a supported content type. |
| `information_layer` | yes | enum string | Must use one of the five architecture layers. |

Recommended `entry_id` format:

```text
{TYPE_PREFIX}-{PRIMARY_TOPIC_ID_NO_DOT}-{NNNN}
```

Examples:

```text
KN-T0101-0001
AR-T0702-0001
PV-T0802-0001
ED-T0902-0001
GV-T0909-0001
IH-T0609-0001
```

Recommended prefixes:

| Prefix | Typical Content Type |
|---|---|
| `KN` | `knowledge_entry` |
| `AR` | `action_resource` |
| `PV` | `progress_and_viewpoint` |
| `ED` | `education_article` |
| `GV` | governance, curation, or safety entry |
| `IH` | `invalid_or_harmful_note` |
| `ES` | `evidence_summary` |
| `CL` | `checklist` |
| `CC` | `clinician_conversation_preparation` |
| `PN` | `protocol_note` |
| `SN` | `source_note` |
| `GL` | `glossary_entry` |

`entry_slug` uses lowercase ASCII letters and numbers with hyphens or underscores, contains no spaces or sensitive user data, and should not be casually renamed after publication.

### 5.2 Title and Summary Fields

| Field | Required | Conceptual Type | Rule |
|---|---:|---|---|
| `title_zh` | yes | string | Chinese display title. |
| `title_en` | yes | string | English display title. |
| `summary_zh` | yes | string | Concise Chinese summary. |
| `summary_en` | yes | string | Concise English summary. |
| `language` | yes | enum string | Primary language or approved bilingual marker. |

Titles and summaries must be accurate, non-promotional, non-clinical, and free of private user information.

### 5.3 Topic Fields

| Field | Required | Conceptual Type | Rule |
|---|---:|---|---|
| `primary_topic_id` | yes | topic ID string | Must exist in the taxonomy and equal the first `topic_ids` item. |
| `topic_ids` | yes | non-empty list | Multiple topic IDs allowed; duplicates prohibited. |
| `topic_paths` | yes | list of strings | Must correspond one-to-one and in order with `topic_ids`. |

### 5.4 Lifecycle Fields

| Field | Required | Conceptual Type | Rule |
|---|---:|---|---|
| `status` | yes | enum string | The only workflow status field. |
| `created_by` | yes | string | Human role, person, or bounded agent identifier. |
| `created_date` | yes | date string | Use `YYYY-MM-DD`. |
| `last_modified_by` | yes | string | Most recent editor identifier. |
| `last_modified_date` | yes | date string | Use `YYYY-MM-DD`; not before `created_date`. |
| `version` | yes | version string | Entry version such as `v0.1`. |
| `status_history` | no | list | Chronological transitions; not another active status. |
| `change_log` | no | list | Human-readable version changes. |

### 5.5 Evidence and Source Fields

| Field | Required | Conceptual Type | Rule |
|---|---:|---|---|
| `evidence_level` | yes | enum string | E1, E2, E3, E4, E5, E0, or EX. |
| `evidence_posture` | yes | enum string | How conservatively the information may be used. |
| `source_type` | yes | non-empty enum list | Multiple source types allowed. |
| `source_urls` | no | URL list | Reviewed formal URLs; no purchase link framed as recommendation. |
| `source_notes` | no | string | Limitations, exclusions, access, or review notes. |
| `last_source_check_date` | no | date string | Most recent source check. |
| `next_review_date` | no | date string | Planned next review. |

If `source_urls` is empty, `source_notes` should explain why no public URL is represented. Evidence level must not be inferred from source type alone.

### 5.6 Safety and Use Fields

| Field | Required | Conceptual Type | Rule |
|---|---:|---|---|
| `safety_boundary` | yes | non-empty string | Clear boundary on prohibited interpretation or use. |
| `allowed_use` | yes | non-empty string list | Explicit permitted uses. |
| `disallowed_use` | yes | non-empty string list | Explicit prohibited uses. |
| `is_clinical_sensitive` | yes | boolean | True for clinically sensitive topics and entries. |
| `commercial_boundary` | conditional | string | Required for action resources and commercial claims. |

### 5.7 Relationship Fields

| Field | Required | Conceptual Type | Rule |
|---|---:|---|---|
| `related_body_systems` | no | string list | Approved Congtie system identifiers only. |
| `related_lifestyle_keywords` | no | string list | Preserve canonical order when multiple. |
| `related_biomarkers` | no | ID or name list | Must not create biomarker ownership or modify biomarker JSON. |
| `related_action_resource_ids` | no | entry ID list | Resolve or mark as reviewed future references. |
| `related_knowledge_ids` | no | entry ID list | Resolve or mark as reviewed future references. |
| `related_source_ids` | no | source ID list | Resolve or mark as reviewed future references. |

Canonical lifestyle order:

```text
睡眠 / 营养 / 锻炼 / 压力
sleep / nutrition / exercise / stress
```

### 5.8 Publication and Retrieval Fields

| Field | Required | Conceptual Type | Rule |
|---|---:|---|---|
| `visibility` | no | enum string | Human/content visibility; not runtime authorization. |
| `runtime_enabled` | no | boolean | False for drafts and unapproved entries. |
| `retrieval_enabled` | no | boolean | False until separately approved. |
| `publish_channels` | no | string list | Approved publication channels. |

Rules:

- Pre-approval and rejected states cannot set `runtime_enabled: true`.
- `approved` does not automatically mean `published`.
- `published` does not override safety, permission, or clinical sensitivity.
- `archived` is disabled for normal retrieval and runtime use.

---

## 6. Enum Definitions

### 6.1 Content Types

```text
knowledge_entry
action_resource
progress_and_viewpoint
education_article
glossary_entry
checklist
clinician_conversation_preparation
source_note
evidence_summary
protocol_note
invalid_or_harmful_note
governance_rule
curation_rule
safety_boundary
```

### 6.2 Information Layers

```text
knowledge
action_resource
progress_and_viewpoints
education
governance
```

### 6.3 Status

```text
draft
ai_review_pending
ai_reviewed
human_review_pending
needs_revision
approved
published
archived
rejected
```

No second status field is allowed.

### 6.4 Language

```text
zh-CN
en-US
bilingual_zh_en
```

### 6.5 Evidence Level

| Value | Label | Meaning |
|---|---|---|
| `E1` | `authority_guideline` | Authority guideline or authoritative consensus. |
| `E2` | `high_quality_review_or_rct` | High-quality review, meta-analysis, or RCT. |
| `E3` | `observational_or_consensus` | Observational evidence or professional consensus. |
| `E4` | `early_research` | Early clinical, animal, or mechanistic research. |
| `E5` | `expert_opinion_or_hypothesis` | Expert opinion, hypothesis, or viewpoint. |
| `E0` | `commercial_or_anecdotal` | Commercial, anecdotal, or unverified claim. |
| `EX` | `disproven_or_harmful` | Disproven, harmful, unsafe, outdated, or deprecated. |

Higher evidence does not authorize diagnosis, treatment, dosage, clinical recommendation, risk calculation, system scoring, disease prediction, or personalized protocols.

### 6.6 Evidence Posture

```text
product_policy
safety_policy
general_consensus
clinical_guideline_adjacent
product_spec
user_manual
commercial_claim_unverified
founder_curated
```

New values require governance review.

### 6.7 Source Type

```text
official_guideline_china
official_guideline_international
professional_consensus
peer_reviewed_meta_analysis
peer_reviewed_rct
peer_reviewed_observational
peer_reviewed_mechanistic
professional_education_page
official_product_spec
official_user_manual
official_service_description
founder_curated
founder_direct_experience
commercial_marketing_page
ecommerce_listing
user_review
media_article
expert_interview
expert_blog
conference_talk
commercial_claim_unverified
unknown_or_unverified
```

Historical Knowledge Seed values not listed above, such as `peer_reviewed_review`, require governance review. A future validator should report them rather than silently accept, delete, or rewrite them.

### 6.8 Actionability Status

```text
not_applicable
not_actionable
education_only
watchlist
requires_professional_context
future_candidate
deprecated
```

### 6.9 Recommendation Permission

```text
R0 = prohibited from automatic recommendation
R1 = user-initiated explanation only
R2 = information-completion option
R3 = low-risk general tool option
```

### 6.10 Resource Type

Current P0-compatible values:

```text
information_resource
device
lifestyle_tool
testing_service
nutrition_product
supplement
```

New values require curation review.

### 6.11 Nutrition Category

```text
whole_food
dietary_pattern
meal_replacement
functional_beverage
snack
dietary_supplement
longevity_supplement
```

### 6.12 Research Stage

```text
basic_research
animal_study
early_clinical
clinical_trial
real_world_study
expert_debate
product_development
regulatory_review
commercial_launch
post_market_monitoring
```

### 6.13 Regulatory Status

Conceptual v0 values:

```text
not_applicable
unknown
research_only
under_review
approved
regulated
restricted
not_approved
withdrawn
```

No regulatory status may be asserted without reviewed sources.

### 6.14 Commercialization Status

```text
not_applicable
unknown
research_only
pre_market
limited_availability
available
discontinued
```

Commercialization status is descriptive, not promotional or evidence of safety or effectiveness.

### 6.15 Visibility

```text
internal
founder_review
private_reference
public
archived
```

The public knowledge library must never contain private user health information, regardless of visibility.

---

## 7. Validation Rules

These are documentation-level checks for a future lightweight validator. They do not implement JSON Schema, database enforcement, API validation, or runtime policy.

### 7.1 Identity Checks

A validator should check:

- `schema_version` exists and equals `v0.1`.
- `entry_id` exists, is unique, and follows the approved format.
- `entry_slug` exists and uses a lowercase filename-safe form.
- `content_type` and `information_layer` are valid.
- The same canonical entry is not duplicated in multiple layer directories.

### 7.2 Required Field Checks

- Every required common field exists.
- Required strings are non-empty.
- Required lists are non-empty.
- `is_clinical_sensitive` is boolean.
- Conceptual field shapes match this specification.

### 7.3 Topic Checks

- `primary_topic_id` exists.
- `topic_ids` is non-empty and contains no duplicates.
- Every topic ID has valid format and exists in the taxonomy.
- `primary_topic_id` equals the first `topic_ids` item.
- `topic_paths` length equals `topic_ids` length.
- Every topic path starts with its corresponding topic ID.
- The content type is allowed by the mapped taxonomy topic or has reviewed cross-layer rationale.
- T10 remains disabled for v0 runtime and retrieval.

### 7.4 Lifecycle Checks

- `status` is valid.
- No parallel workflow status field exists.
- Dates use `YYYY-MM-DD`.
- `last_modified_date` is not before `created_date`.
- `approved` requires a human review record.
- `published` requires prior human approval.
- `archived` is not normally runtime- or retrieval-enabled.
- AI agents do not approve or publish without human authorization.

Recommended lifecycle:

```text
draft
→ ai_review_pending
→ ai_reviewed
→ human_review_pending
→ approved
→ published
```

Revision path:

```text
ai_reviewed / human_review_pending
→ needs_revision
→ draft
```

Closeout paths:

```text
draft / ai_reviewed / human_review_pending / needs_revision
→ rejected

approved / published
→ archived
```

### 7.5 Evidence Checks

- `evidence_level`, `evidence_posture`, and non-empty `source_type` exist and use reviewed values.
- Source URLs are absolute HTTP or HTTPS URLs when provided.
- Empty `source_urls` is explained by `source_notes`.
- E0 and commercial sources are not presented as verified health outcomes.
- EX entries document invalidity, harm, or deprecation.
- Higher evidence is not treated as stronger intervention permission.

### 7.6 Safety Checks

- `safety_boundary`, `allowed_use`, and `disallowed_use` are non-empty.
- `is_clinical_sensitive` exists and is boolean.
- Clinically sensitive entries set it to `true`.
- Metadata and body content do not authorize prohibited clinical behavior.
- Private user data is absent.

### 7.7 Relationship Checks

- Related IDs use approved formats and contain no duplicates.
- Related IDs resolve or are explicitly marked as reviewed future references.
- Self-reference is rejected unless justified.
- Topic relationships do not imply evidence or permission inheritance.
- Biomarker relationships do not modify biomarker ownership or authoritative biomarker JSON.

### 7.8 Conditional Checks

- Apply action resource checks for `information_layer: action_resource`.
- Apply progress and viewpoints checks for `information_layer: progress_and_viewpoints`.
- Apply nutrition and supplement checks for T05.02, T07.05, and T07.06.
- Apply stricter clinical-sensitivity checks for disease, medication, emergency, intervention, and protocol topics.

### 7.9 Error Posture

A future validator should accumulate all errors, report file and field names, distinguish warnings, avoid automatic rewrites, avoid silently normalizing unknown enums, and exit non-zero on failure.

---

## 8. Content Type Rules

### 8.1 Content Type and Layer Compatibility

| Information Layer | Normally Allowed Content Types |
|---|---|
| `knowledge` | `knowledge_entry`, `glossary_entry`, `source_note`, `evidence_summary`, `protocol_note`, `invalid_or_harmful_note`, `safety_boundary` |
| `action_resource` | `action_resource` |
| `progress_and_viewpoints` | `progress_and_viewpoint`, `evidence_summary`, `source_note`, `education_article` |
| `education` | `education_article`, `glossary_entry`, `checklist`, `clinician_conversation_preparation`, `source_note` |
| `governance` | `governance_rule`, `curation_rule`, `safety_boundary`, `source_note`, `evidence_summary`, `invalid_or_harmful_note` |

The taxonomy may explicitly allow a cross-layer content type. Such use requires taxonomy support, clear layer rationale, human review, and no relaxation of safety or permission rules.

### 8.2 Knowledge Entries

`knowledge_entry` is for stable, reusable explanation-oriented information. It must not directly generate diagnosis, treatment, medication or dosage advice, clinical recommendation, risk calculation, system scoring, disease prediction, or personalized protocols.

### 8.3 Action Resources

`action_resource` is for permission-controlled products, services, tools, devices, testing services, supplements, nutrition products, or information resources. It must follow Section 11.

### 8.4 Progress and Viewpoints

`progress_and_viewpoint` is for research progress, expert viewpoints, development progress, regulatory progress, or commercialization status. It must follow Section 12.

### 8.5 Education Types

`education_article`, `glossary_entry`, `checklist`, and `clinician_conversation_preparation` support explanation, navigation, information organization, or consultation preparation. They must not become diagnosis, treatment plans, clinical orders, or personalized medical instructions.

### 8.6 Source and Evidence Types

`source_note` and `evidence_summary` preserve source context, uncertainty, source quality, evidence limitations, and commercial claim boundaries.

### 8.7 Protocol Notes

`protocol_note` is a non-personalized reference note. Notes involving drugs, supplements, hormones, peptides, invasive interventions, experimental therapies, aggressive testing, or personalized plans default to high safety boundaries and R0/R1 handling where applicable.

v0 must not use protocol notes to generate personalized protocols.

### 8.8 Invalid or Harmful Notes

`invalid_or_harmful_note` documents disproven, harmful, unsafe, outdated, unsupported, or exaggerated information. It should explain the invalidity or harm, supporting sources, superseding information when known, educational use, and prohibited reuse as advice.

### 8.9 Governance Types

`governance_rule`, `curation_rule`, and `safety_boundary` define review, source, evidence, publication, and usage boundaries. They do not create executable runtime policy by themselves.

---

## 9. Information Layer Rules

### 9.1 Knowledge Layer

Knowledge entries require evidence metadata, source information, safety boundaries, allowed and disallowed use, and human review before publication.

They may support explanation, education, missing-context clarification, and safety explanation. They must not support diagnosis, treatment, medication or dosage advice, clinical recommendation, risk calculation, system scoring, disease prediction, or personalized supplement protocols.

### 9.2 Action Resource Layer

Every entry uses `content_type: action_resource` and follows R0/R1/R2/R3. Evidence level does not override recommendation permission.

### 9.3 Progress and Viewpoints Layer

Entries are not stable knowledge by default and use:

```yaml
actionability_status: education_only
```

unless a reviewed rule requires a stricter status.

### 9.4 Education Layer

Education may explain concepts, reduce confusion, support safe record organization, and help users prepare questions. It must not create clinical decisions, risk calculations, treatment instructions, dosage instructions, or personalized protocols.

### 9.5 Governance Layer

Governance defines how information is curated, reviewed, versioned, published, deprecated, and used. It requires human approval before becoming authoritative.

### 9.6 Layer Exclusivity

Each entry has exactly one primary `information_layer`. Cross-topic mapping does not create multiple layers. If one subject needs stable knowledge, an action resource, and a progress note, create separate linked entries.

---

## 10. Topic Mapping Rules

### 10.1 Topic ID Format

```text
Top level:    T01
Second level: T01.01
Third level:  T01.01.01
```

Conceptual pattern:

```regex
^T\d{2}(\.\d{2}){0,2}$
```

Pattern validity is insufficient: every ID must exist in the taxonomy.

### 10.2 Primary Topic

- `primary_topic_id` is required and must exist in the taxonomy.
- It equals the first item in `topic_ids`.
- It determines the recommended entry ID topic segment.
- It does not prevent secondary topic mappings.

### 10.3 Multiple Topics

Multiple IDs are allowed when each materially improves classification or retrieval.

Healthspan example:

```yaml
primary_topic_id: T01.01
topic_ids:
  - T01.01
  - T01.02
topic_paths:
  - T01.01 Healthspan 健康寿命
  - T01.02 Longevity Goal 长寿目标
```

Protein example:

```yaml
primary_topic_id: T05.02
topic_ids:
  - T05.02
  - T03.04
  - T02.02
topic_paths:
  - T05.02 Nutrition 营养
  - T03.04 Musculoskeletal System 肌肉骨骼系统
  - T02.02 Maintain Physical and Cognitive Capability 保持能力
```

### 10.4 Topic Paths

`topic_paths` has the same length and order as `topic_ids`; each path starts with the corresponding ID and uses the current taxonomy title. Paths are display labels, not independent authorities.

### 10.5 T10 Boundary

T10 Pet Longevity is reserved. In v0, any T10 entry must use:

```yaml
runtime_enabled: false
retrieval_enabled: false
```

No T10 entry may be used for recommendation, personalization, or runtime context construction in v0.

### 10.6 Topic Inheritance

Child topics inherit broad scope and safety posture from ancestors unless a stricter taxonomy rule applies. Topic defaults do not permit omission of entry-level evidence and safety metadata.

---

## 11. Action Resource Rules

When:

```yaml
information_layer: action_resource
```

require:

```yaml
content_type: action_resource
resource_type:
recommendation_permission:
commercial_boundary:
commercial_relationship:
```

Recommended additional fields from existing governance and templates:

```yaml
auto_trigger_allowed:
commercial_boundary_level:
privacy_risk:
source_enrichment_status:
concept_evidence_level:
resource_claim_evidence_level:
```

### 11.1 Permission Rules

```text
R0 = prohibited from automatic recommendation
R1 = user-initiated explanation only
R2 = information-completion option
R3 = low-risk general tool option
```

Required behavior:

- R0 must not be automatically recommended.
- R1 may only be explained when the user initiates the topic.
- R2 may be presented only as an optional information-completion route.
- R3 may support low-risk general tracking, organization, or education.
- Permission level never overrides clinical safety.
- Evidence level never upgrades recommendation permission automatically.

### 11.2 Commercial Rules

`commercial_boundary` states the commercial-use boundary.

`commercial_relationship` discloses whether Congtie, the curator, or a related party has a commercial relationship.

Rules:

- No hidden commercial conversion.
- No undisclosed commission or referral relationship.
- No required-purchase framing.
- No purchase link presented as a health recommendation.
- Commercial claims remain unverified unless independently supported.
- Official product specifications support feature descriptions, not health outcomes.

### 11.3 Evidence Separation

When relevant, distinguish:

```text
concept_evidence_level
resource_claim_evidence_level
```

Evidence for a general concept does not verify claims of a specific product, service, device, supplement, provider, or model.

### 11.4 Resource Safety

Action resources must not create diagnosis, treatment, medication or dosage advice, clinical recommendations, required clinical testing orders, system scoring, disease risk calculations, disease predictions, personalized protocols, or product pressure.

### 11.5 Nutrition and Supplement Rules

When an entry maps to T05.02, T07.05, or T07.06, support:

```yaml
nutrition_category:
common_use_context:
safety_notes:
known_interactions:
not_for_personalized_protocol:
```

If `common_dosages_in_literature` is included, it is internal reference context only and must not be surfaced as personalized dosage advice.

Supplements and supplement-like nutrition products use:

```yaml
recommendation_permission: R1
auto_trigger_allowed: false
not_for_personalized_protocol: true
```

unless a separately approved curation decision establishes a stricter R0 boundary.

Congtie v0 does not generate personalized supplement protocols, dosage, timing, cycle, loading phase, stack, disease-specific supplement plans, or personalized nutrition prescriptions.

---

## 12. Progress and Viewpoints Rules

When:

```yaml
information_layer: progress_and_viewpoints
```

require:

```yaml
content_type: progress_and_viewpoint
research_stage:
actionability_status:
regulatory_status:
commercialization_status:
```

Recommended additional fields:

```yaml
supporting_viewpoints: []
opposing_or_cautionary_viewpoints: []
last_source_check_date:
next_review_date:
```

Default:

```yaml
actionability_status: education_only
```

Rules:

- Progress and viewpoints are not stable knowledge by default.
- Early research is not established fact.
- Expert opinion is not consensus by default.
- Regulatory or commercial timelines are not certainty.
- Commercial availability is not evidence of safety or effectiveness.
- Entries may explain research and uncertainty.
- Entries must not directly recommend action from early research alone.
- Entries must not provide treatment, supplement protocols, clinical decisions, risk calculations, system scoring, or product endorsements.

Safe boundary:

```text
This is progress and viewpoints information. It is not stable actionable knowledge and should not be used by itself as a personal action plan.
```

Progress entries may map to T08 and a domain topic, but their `information_layer` remains `progress_and_viewpoints`.

---

## 13. Safety Rules

Every entry includes:

```yaml
safety_boundary:
allowed_use: []
disallowed_use: []
is_clinical_sensitive:
```

### 13.1 Clinical Sensitivity

Set `is_clinical_sensitive: true` for entries involving:

- disease
- medication
- dosage
- emergency symptoms
- clinical testing
- disease screening
- high-risk intervention
- hormone
- peptide
- invasive procedure
- off-label drug
- experimental intervention
- supplement protocol
- clinical imaging
- disease risk calculation
- system scoring

Clinical sensitivity does not permit clinical advice. It requires stricter review and safety boundaries.

### 13.2 Universal v0 Non-goals

No entry may authorize:

- diagnosis
- treatment
- medication advice
- medication start, stop, or dose change
- dosage advice
- clinical recommendation
- emergency triage logic
- system scoring
- disease risk calculation
- disease prediction
- personalized supplement protocol
- personalized nutrition prescription
- personalized training prescription
- personalized medical intervention

### 13.3 Safety Metadata Quality

`safety_boundary` must specifically explain the entry's main limitations. Generic text such as `use safely` is insufficient.

`allowed_use` and `disallowed_use` must not contradict each other.

Invalid or harmful entries may support education, warning, or deprecation, but never reenactment or recommendation.

### 13.4 Private User Data Boundary

Knowledge library entries must not contain personal biomarker values, medical records, laboratory reports, private lifestyle logs, supplement or medication history, private conversation context, or consent records.

Private user context belongs to the User Health Information Library and separately approved runtime boundaries.

### 13.5 Human Review

AI may draft, summarize, flag risk, and suggest mappings.

AI must not approve or publish entries, silently upgrade evidence, silently change permission, convert commercial claims into verified claims, or bypass human review.

`approved` and `published` require human authorization.

---

## 14. Future Extension

Possible future artifacts:

```text
JSON Schema
CMS form schema
API contracts
MCP retrieval schema
runtime index schema
```

None are created or approved by this document.

### 14.1 JSON Schema

A future JSON Schema may encode required fields, enums, conditional requirements, topic formats, and conceptual types. It requires separate Founder Gate approval before creation or enforcement.

### 14.2 CMS Form Schema

A future CMS form may assist authors and reviewers. Markdown and Git remain canonical unless a separately approved synchronization and governance workflow changes that rule.

### 14.3 API Contracts

Future APIs may expose approved metadata or retrieval results. Any API contract must preserve existing top-level response envelopes and requires separate review.

### 14.4 MCP Retrieval Schema

A future MCP contract may allow agents to retrieve approved entries. It must enforce layer, status, safety, permission, visibility, and private-data separation.

### 14.5 Runtime Index Schema

A future runtime index may provide retrieval metadata. It must be generated from canonical Markdown and must not become an independent editable source of truth.

### 14.6 Versioning Direction

Future versions should preserve backward readability where practical, document migrations, avoid silently rewriting history, preserve Git history, review enum changes, keep status semantics stable unless approved, and retain explicit permission and safety fields.

### 14.7 Implementation Boundary

Separate approval is required for executable schemas, validators that enforce new semantics, database or persistent models, API or CLI contracts, runtime retrieval, CMS synchronization, external integrations, biomarker JSON changes, and production clinical logic.

The safest v0 rule remains:

```text
Structure knowledge clearly.
Map it to both architecture and taxonomy.
Use evidence to improve explanation, not authorize intervention.
Keep private user context separate.
Keep action resources permission-controlled.
Require human review before approval and publication.
```
