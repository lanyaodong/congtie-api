# Longevity Information Library Architecture Patch for Taxonomy v0.1

Version: v0.1
Project: Congtie
Status: Draft
Owner: Congtie Agent Team
Last Updated: 2026-05-29

---

## 1. Purpose

This patch clarifies the relationship between the Congtie Longevity Information Library Architecture and the Longevity Topic Taxonomy.

It does not replace:

```text
longevity_information_library_architecture.v0.1.md
```

It does not replace:

```text
longevity_topic_taxonomy.v0.1.md
```

It is a small alignment note that makes the connection between the two documents explicit.

This patch is documentation-only.

It does not create runtime logic, loader behavior, schema validation, tests, API contracts, JSON indexes, topic files, or action resource entries.

---

## 2. One-line Summary

The architecture defines the vertical information layer and governance structure.

The taxonomy defines the horizontal topic map and retrieval structure.

Every future knowledge entry, action resource, education item, progress item, or governance item should carry both:

```text
information_layer
topic_id
```

---

## 3. Why This Patch Exists

The architecture document defines the overall structure of the Longevity Information Library.

It defines five main information layers:

```text
Knowledge Layer
Action Resource Layer
Progress and Viewpoints Layer
Education Layer
Governance Layer
```

The taxonomy document defines the topic map.

It defines domain-oriented topic paths such as:

```text
T01 Longevity Foundation
T02 Longevity Strategy
T03 Body Systems
T04 Measurement and Records
T05 Lifestyle Foundations
T06 Risk Prevention and Safety
T07 Interventions and Action Resources
T08 Progress and Viewpoints
T09 Education, Experts, Sources and Governance
T10 Pet Longevity
```

These two documents are complementary.

They are not duplicates.

They answer different questions.

```text
Architecture asks:
What type of information is this, and how should it be governed?

Taxonomy asks:
What topic does this information belong to, and how should it be found?
```

---

## 4. Architecture vs Taxonomy

## 4.1 Architecture

The Longevity Information Library Architecture is the vertical governance structure.

It defines:

* information layers
* evidence requirements
* source rules
* safety boundaries
* action resource permissions
* commercial boundaries
* user health information separation
* manual review
* future automation direction
* runtime principles

The architecture is concerned with:

```text
What this information is.
How it should be governed.
How it can or cannot be used.
```

## 4.2 Taxonomy

The Longevity Topic Taxonomy is the horizontal topic map.

It defines:

* topic IDs
* topic paths
* domain grouping
* navigation
* retrieval tags
* mapping targets
* topic-level metadata
* entry-to-topic relationships

The taxonomy is concerned with:

```text
Where this information belongs.
How humans find it.
How agents retrieve it.
How entries are mapped across domains.
```

---

## 5. Required Dual Metadata

Every future entry should ideally carry both architecture metadata and taxonomy metadata.

Required architecture metadata:

```yaml
information_layer:
evidence_level:
evidence_posture:
source_type:
allowed_use:
disallowed_use:
safety_boundary:
commercial_boundary:
curation_status:
review_status:
```

Required taxonomy metadata:

```yaml
topic_id:
topic_path:
topic_slug:
related_topic_ids:
```

For action resources, also include:

```yaml
recommendation_permission:
auto_trigger_allowed:
resource_type:
commercial_boundary_level:
privacy_risk:
```

For progress and viewpoints, also include:

```yaml
research_stage:
actionability_status:
regulatory_status:
commercialization_status:
```

For user-private data references, do not store private user data in the taxonomy.

Use 用户健康信息库 and runtime context boundaries instead.

---

## 6. The Two-axis Model

The recommended mental model is a two-axis model.

```text
Axis 1: Information Layer
Axis 2: Topic Path
```

Example:

```yaml
entry_id: KS-RESOURCE-006
title_zh: 锻炼日志 / 锻炼追踪工具
information_layer: action_resource
topic_id:
  - T05.03
  - T07.04
recommendation_permission: R3
```

Another example:

```yaml
entry_id: KS-SAFETY-002
title_zh: 为什么葱铁不能给用药或剂量建议
information_layer: knowledge
topic_id:
  - T06.01
  - T07.07
```

Another example:

```yaml
entry_id: future-progress-note-001
title_zh: 某项长寿药物研究进展
information_layer: progress_and_viewpoints
topic_id:
  - T08.02
  - T07.07
actionability_status: education_only
```

---

## 7. How to Map Existing Entries

## 7.1 Knowledge Seed Entries

Knowledge Seed entries should map to:

```yaml
information_layer: knowledge
```

or, when appropriate:

```yaml
information_layer: education
```

Examples:

```text
KS-PRODUCT-001 → T01.05
KS-PRODUCT-002 → T01.01
KS-PRODUCT-004 → T04.00 / T04.07

KS-MISSING-001 → T04.04
KS-MISSING-002 → T04.05
KS-MISSING-003 → T04.06
KS-MISSING-007 → T04.07

KS-SAFETY-001 → T06.01
KS-SAFETY-002 → T06.01 / T07.07
KS-SAFETY-003 → T06.02
KS-SAFETY-005 → T06.01
KS-SAFETY-006 → T03.00
```

## 7.2 Action Resource Entries

Action Resource entries should map to:

```yaml
information_layer: action_resource
```

Examples:

```text
KS-RESOURCE-001 → T04.01 / T07.01
KS-RESOURCE-002 → T07.02 / T03.03
KS-RESOURCE-003 → T07.02 / T03.02 / T03.04
KS-RESOURCE-004 → T07.02 / T04.08
KS-RESOURCE-005 → T05.01 / T07.04
KS-RESOURCE-006 → T05.03 / T07.04
KS-RESOURCE-007 → T05.02 / T07.04
KS-RESOURCE-008 → T04.01 / T07.03
KS-RESOURCE-009 → T07.05
KS-RESOURCE-010 → T07.06
```

## 7.3 Progress and Viewpoints Entries

Progress and viewpoints entries should use:

```yaml
information_layer: progress_and_viewpoints
```

They may also map to domain topics outside T08.

Example:

```yaml
information_layer: progress_and_viewpoints
topic_id:
  - T08.02
  - T04.03
```

A progress item is not stable knowledge by default.

It must include:

```yaml
actionability_status:
research_stage:
regulatory_status:
commercialization_status:
```

Default runtime use:

```text
education only
```

## 7.4 Governance Entries

Governance documents should use:

```yaml
information_layer: governance
```

Examples:

```text
evidence_grading_framework.v0.1.md → T09.07 / T09.09
action_resource_curation_rules.v0.2.md → T09.09
proactive_action_boundary.v0.1.md → T09.09
user_health_information_library_spec.v0.1.md → T01.06 / T04.12 / T09.09
```

---

## 8. 用户健康信息库 Boundary

用户健康信息库 is not part of the general topic taxonomy as a storage layer.

The taxonomy may define topics about:

* health records
* lab reports
* biomarker concepts
* data privacy
* consent
* user health information library concept

But it must not store user-private data.

The following belong to 用户健康信息库, not to the general taxonomy:

* user’s biomarker values
* user’s lab reports
* user’s medical records
* user’s lifestyle logs
* user’s supplement history
* user’s action history
* user’s consent and sharing state

The relationship is:

```text
Longevity Information Library
= general, reusable, versioned information

用户健康信息库
= private, user-specific, consent-gated health context
```

The model may combine both only within approved runtime safety and user-consent boundaries.

---

## 9. Progress and Viewpoints Boundary

Progress and viewpoints are not stable knowledge by default.

They may appear in T08 or in any other topic path.

For example:

```text
A wearable-device validation paper may map to T07.02 and T08.02.
A microbiome research update may map to T05.02 and T08.01.
A longevity-drug clinical trial note may map to T07.07 and T08.02.
```

But they must still follow the progress and viewpoints boundary:

* no direct action recommendation
* no treatment
* no supplement protocol
* no medication advice
* no dosage
* no clinical decision
* no disease risk calculation
* no system scoring

Recommended default:

```yaml
information_layer: progress_and_viewpoints
actionability_status: education_only
```

---

## 10. Topic Mapping Seed

This patch supports a future file:

```text
agent/knowledge_seed_v0/topic_mapping_seed.v0.1.json
```

The mapping seed should connect existing entries to taxonomy topics and architecture layers.

Recommended mapping fields:

```json
{
  "entry_id": "",
  "entry_type": "",
  "information_layer": "",
  "topic_id": [],
  "topic_path": [],
  "permission_level": "",
  "recommendation_permission": "",
  "evidence_level": "",
  "evidence_posture": "",
  "source_type": [],
  "is_clinical_sensitive": false,
  "actionability_status": "",
  "notes": ""
}
```

This mapping seed should initially cover:

```text
19 Knowledge Seed P0 entries
10 Action Resource P0 entries
```

---

## 11. Runtime Guidance

Runtime retrieval should not use topic alone.

It should use:

```text
topic_id
+ information_layer
+ permission_level
+ evidence_level
+ safety_boundary
+ user context permission
```

Example:

A topic under supplements does not mean it can be recommended.

A topic under disease risk does not mean disease risk can be calculated.

A topic under progress and viewpoints does not mean it can become an action plan.

A topic under measurement does not mean the system can issue a clinical test order.

Runtime boundary reminders:

```text
Progress and Viewpoints = 进展与观点
internal label = progress_and_viewpoints

Lifestyle keyword order:
睡眠 / 营养 / 锻炼 / 压力
sleep / nutrition / exercise / stress

Action resource permissions:
R0 = prohibited from automatic recommendation
R1 = user-initiated explanation only
R2 = information-completion option
R3 = low-risk general tool option

v0 non-goals:
no diagnosis
no treatment
no medication advice
no dosage advice
no clinical recommendation
no system scoring
no disease risk calculation
no disease prediction
no personalized supplement protocol
no personalized medical intervention
```

---

## 12. Acceptance Criteria

This patch is acceptable when:

* It clarifies architecture vs taxonomy.
* It states that architecture defines vertical information layers.
* It states that taxonomy defines horizontal topic map.
* It requires entries to carry both `information_layer` and `topic_id`.
* It explains the two-axis model.
* It maps existing Knowledge Seed and Action Resource entries conceptually.
* It clarifies that 用户健康信息库 is private and adjacent, not public taxonomy content.
* It clarifies that progress and viewpoints may appear across topics.
* It preserves R0/R1/R2/R3 permission rules.
* It preserves the non-clinical boundary.
* It preserves the v0 non-goals.
* It supports future `topic_mapping_seed.v0.1.json`.
* It uses `Congtie` as display name.
* It uses `congtie` only in lowercase/code/domain contexts.
* It does not use the deprecated camel-case brand spelling.

---

## 13. Final Note

The architecture and taxonomy should work together.

The safest v0 principle is:

```text
Architecture governs what information is and how it can be used.
Taxonomy governs where information belongs and how it can be found.
Runtime must use both.
```
