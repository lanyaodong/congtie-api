# Longevity Knowledge Batch 001 Plan v0.1

Version: v0.1  
Project: Congtie  
Status: Draft  
Owner: Congtie Agent Team  
Last Updated: 2026-08-19

---

## 1. Background

Congtie has completed the first version of the Longevity Information Library infrastructure:

```text
Knowledge Item Template
Knowledge Item Schema
Longevity Topic Taxonomy
Evidence Source Type Governance
Single-item Validator
Markdown + Git canonical repository structure
```

Batch 001 moves the workstream from infrastructure design into production of the first official knowledge assets.

Primary governance references:

```text
agent/longevity_knowledge_base/templates/longevity_knowledge_item_template.v0.1.md
agent/longevity_knowledge_item_schema.v0.1.md
agent/knowledge_seed_v0/longevity_topic_taxonomy.v0.1.md
agent/knowledge_seed_v0/longevity_information_library_architecture.v0.1.md
agent/longevity_knowledge_base/schemas/evidence_source_type_enum.v0.1.md
agent/longevity_knowledge_base/schemas/evidence_source_type_alignment_notes.v0.1.md
agent/longevity_knowledge_base/scripts/validate_longevity_knowledge_item.py
```

The task brief refers to `agent/longevity_topic_taxonomy.v0.1.md`. The current repository taxonomy is located at `agent/knowledge_seed_v0/longevity_topic_taxonomy.v0.1.md`; Batch 001 must use that file unless a separately reviewed canonical relocation occurs.

Batch 001 is a content-production plan. It does not approve entries, publish content, enable runtime retrieval, create clinical logic, or store private user health information.

---

## 2. Batch 001 Goal

Batch 001 creates the minimum useful longevity knowledge foundation for the Congtie v0 Public Beta.

Target:

```text
approximately 50 entries
```

Priority:

```text
quality > quantity
```

The original six requested group targets total 56 candidate entries. Founder-approved Group G adds four foundational medical-field and practice-model candidates, expanding the candidate pool from 56 to 60. Founder-approved allocation of the previously unallocated T01.03 Longevity Mindset / 长寿心态 leaf adds `KN-T0103-0001` as a candidate, expanding the candidate pool from 60 to 61. Founder-approved allocation of the T02.06 Longevity Strategy Concept / 长寿策略概念 leaf adds `KN-T0206-0001`, expanding the candidate pool from 61 to 62. Founder-approved allocation of `KN-T0403-0002` for baselines, longitudinal trends, measurement error, and biological variation expands the current candidate pool from 62 to 63. Batch 001 still aims to finish approximately 50 high-quality entries after duplicate review, consolidation, evidence review, and scope control. This candidate-pool expansion does not increase the intended final publication target. Founder-approved entries that have already completed the candidate workflow are recorded separately as completed foundation assets rather than counted again as open production candidates.

The batch should establish enough breadth for Congtie to explain:

- what healthspan means
- how Congtie approaches longevity safely
- the six body systems
- measurement and record context
- the canonical lifestyle foundations
- low-risk action resources
- non-clinical safety boundaries
- how to interpret evidence, progress, and viewpoints

No entry is included merely to satisfy a count. Entries that cannot meet evidence, safety, or review requirements should be merged, revised, or deferred.

---

## 3. Target Users

### 3.1 Primary Users

Batch 001 is designed for Chinese-language Congtie v0 Public Beta users who want understandable, practical, non-clinical longevity information.

Typical needs include:

- understanding healthspan concepts
- organizing health information and measurement context
- understanding body-system concepts without receiving a diagnosis
- understanding lifestyle foundations
- recognizing uncertainty and missing context
- preparing safer questions for professional consultation
- using low-risk tracking or information-completion tools

### 3.2 Secondary Users

Secondary users include:

- Congtie Agent retrieval and explanation workflows
- founders and human reviewers
- content curators
- evidence reviewers
- future product, API, and frontend teams consuming approved content contracts

### 3.3 User Boundary

Batch 001 contains general, reusable information.

It must not contain private user records, personal biomarker values, personal reports, personal histories, or permission state. Those belong to the separately governed User Health Information Library.

---

## 4. Content Principles

### 4.1 Healthspan-first

Content should help users understand how to extend healthspan through measurement, explanation, safe action, and iteration.

It should not become a disease encyclopedia or treatment guide.

### 4.2 China-first, Global-aware

Prefer Chinese official, professional, and public-health context where relevant. Use high-quality international sources when they improve general education or fill a source gap.

### 4.3 Evidence-aware

Every entry must state its evidence level, evidence posture, and source type. Evidence strength supports clearer explanation but does not authorize stronger intervention.

### 4.4 Non-clinical

Batch 001 must not create:

```text
diagnosis
treatment
medication advice
dosage advice
clinical recommendation
system scoring
disease risk calculation
disease prediction
personalized supplement protocol
personalized nutrition prescription
personalized training prescription
personalized medical intervention
```

### 4.5 Plain and Traceable

Each entry should be understandable to a general user and traceable to reviewed sources. The body should distinguish established knowledge, uncertainty, limitations, and safe use.

### 4.6 One Canonical Entry

One concept should have one canonical Markdown entry. Candidate duplicates should be merged or linked rather than maintained as parallel authoritative copies.

Canonical entry path:

```text
agent/longevity_knowledge_base/entries/<information_layer>/<entry_id>.<entry_slug>.md
```

The existing top-level information-layer directories are legacy structure and must not receive new Batch 001 entries.

### 4.7 Human Approval Required

AI may draft and review entries, but it may not approve or publish them. Founder approval remains required for topic mapping, evidence level, wording, safety boundary, and publication status.

### 4.8 Intervention Coverage Guidance

Batch 001 may include selected supplement, medication, and high-risk intervention awareness entries when they are important for user understanding. Such entries require stricter evidence, safety, and permission boundaries.

---

## Longevity Intervention Coverage Principle

### 1. Coverage Principle

The Congtie Longevity Information Library v0 includes information coverage of:

- supplements
- medications discussed in longevity research
- experimental interventions
- high-risk longevity technologies

These topics are frequently followed by proactive longevity users. They are part of the longevity knowledge landscape and should be organized, explained, monitored, and reviewed rather than omitted.

Information coverage does not mean recommendation, endorsement, approval, or runtime actionability.

### 2. Information Purpose

These topics may be used for:

- education
- evidence explanation
- uncertainty clarification
- research progress tracking
- risk awareness
- source comparison

Entries should distinguish stable knowledge, emerging research, expert viewpoints, commercial claims, regulatory status, and known uncertainty.

### 3. Runtime Boundary

These topics must not be used for:

- personalized treatment
- medication recommendation
- medication start, stop, or change advice
- dosage recommendation
- supplement protocol
- personalized intervention plan
- clinical decision making

They also must not create diagnosis, system scoring, disease risk calculation, disease prediction, or personalized medical intervention.

Runtime permission must be derived from information layer, content type, evidence, safety boundary, review status, and R0/R1/R2/R3 controls where an Action Resource is involved. Topic coverage alone never grants runtime permission.

### 4. Information Layer Mapping

#### 4.1 Supplements

Supplements may appear in:

```text
knowledge
action_resource
progress_and_viewpoints
```

Examples include:

- creatine
- omega-3
- vitamin D
- magnesium
- NMN
- NR
- spermidine

Supplement knowledge and progress entries may explain evidence, uncertainty, safety, regulation, and research status. Supplement Action Resources remain permission-controlled and normally default to R1 user-initiated explanation only.

Boundary:

```text
No personalized supplement protocol.
```

#### 4.2 Medications

Medications discussed in longevity research normally appear in:

```text
progress_and_viewpoints
knowledge
```

Examples include:

- rapamycin
- metformin
- GLP-1 medications
- statins

Boundary:

```text
Education and research explanation only.
No prescribing or medication management.
```

If a medication is represented as an Action Resource for boundary or classification purposes, it remains R0 and prohibited from automatic recommendation.

#### 4.3 High-risk Interventions

Examples include:

- stem cell therapy
- exosome therapy
- peptide interventions
- experimental anti-aging procedures

Possible representation includes:

```text
information_layer: progress_and_viewpoints
content_type: invalid_or_harmful_note
content_type: safety_boundary
```

`invalid_or_harmful_note` and `safety_boundary` are content types rather than information-layer values. They may be placed in an appropriate knowledge, education, or governance layer according to the schema and taxonomy.

Boundary:

```text
High-risk awareness and evidence explanation only.
```

High-risk or experimental Action Resources remain R0 unless a future explicit governance review establishes a different bounded classification.

### 5. Batch 001 Placement

Selected awareness entries from these categories may be introduced when they are important for user understanding and can satisfy the stricter review rules above.

Any addition should be handled through Founder-reviewed substitution, consolidation, prioritization, or an explicit candidate-pool decision. The Founder-approved foundational medical-field additions in Group G expand the candidate pool from 56 to 60 because the current plan does not contain four clear and safe substitution slots. This does not change the approximately 50-entry target or T01-T09 coverage.

---

## 5. Topic Coverage

Batch 001 aligns with:

```text
agent/knowledge_seed_v0/longevity_topic_taxonomy.v0.1.md
```

Required top-level coverage:

| Topic | Batch 001 Coverage | Primary Production Group |
|---|---|---|
| T01 Longevity Foundation | included | Group A |
| T02 Longevity Strategy | included | Group B |
| T03 Body Systems | included | Group C |
| T04 Measurement and Records | included | Group D |
| T05 Lifestyle Foundations | included | Group E |
| T06 Risk Prevention and Safety | included | Group A safety foundation |
| T07 Interventions and Action Resources | included | Group F |
| T08 Progress and Viewpoints | included | Group A interpretation foundation |
| T09 Education, Experts, Sources and Governance | included | Group A evidence foundation |
| T10 Pet Longevity | excluded | reserved and disabled in v0 |

T10 Pet Longevity must not be included in Batch 001 production, retrieval, publication, or runtime planning.

Topic IDs must exist in the taxonomy. Multiple topic IDs are allowed, but `primary_topic_id` must be the first item in `topic_ids`.

---

## 6. Planned Entry List

### 6.1 Group A: Congtie Foundation

Target: 9 candidate entries.

Completed foundation and consolidation anchor:

| Entry ID | Canonical Title | Primary Topic | Status | Consolidation Decision |
|---|---|---|---|---|
| KN-T0101-0001 | 什么是健康寿命 | T01.01 | approved | This canonical entry already covers lifespan, healthspan, their distinction, and the HALE boundary. Do not create a separate "lifespan vs healthspan" entry; different user phrasings belong to future retrieval and query expansion. |

The Group A candidate slot that could otherwise have produced a duplicate lifespan-versus-healthspan object is assigned to `KN-T0107-0001`, the Longevity Information Library concept. This is a substitution and consolidation decision, not scope expansion.

| Priority | Planned Entry ID | Working Title | Primary Topic | Content Type | Information Layer |
|---|---|---|---|---|---|
| P0 | KN-T0107-0001 | 长寿信息库是什么 | T01.07 | knowledge_entry | knowledge |
| P0 | KN-T0102-0001 | Congtie 的长寿目标：延长健康寿命 | T01.02 | knowledge_entry | knowledge |
| P0 | KN-T0103-0001 | 什么是长寿心态：把长寿当作一项长期实践 | T01.03 | knowledge_entry | knowledge |
| P0 | KN-T0104-0001 | 从身体黑箱到身体透明 | T01.04 | knowledge_entry | knowledge |
| P0 | KN-T0105-0001 | Congtie 的角色与非临床边界 | T01.05 | knowledge_entry | knowledge |
| P0 | KN-T0106-0001 | 用户健康信息库与公共知识库的边界 | T01.06 | knowledge_entry | knowledge |
| P0 | GV-T0601-0001 | Congtie v0 非临床安全边界 | T06.01 | safety_boundary | governance |
| P1 | ED-T0800-0001 | 如何理解进展与观点 | T08.00 | education_article | education |
| P1 | ED-T0907-0001 | 如何理解证据等级与信源类型 | T09.07 | education_article | education |

Group A establishes the Longevity Mindset / 长寿心态 and product mental model, the relationship between 长寿信息库 and 用户健康信息库, the public/private information boundary, core safety posture, and the minimum interpretation guidance needed for T08 and T09 coverage.

### 6.2 Group B: Longevity Strategy

Target: 6 candidate entries.

| Priority | Planned Entry ID | Working Title | Primary Topic | Content Type | Information Layer |
|---|---|---|---|---|---|
| P0 | KN-T0201-0001 | 避免早逝：长寿策略中的一般概念 | T02.01 | knowledge_entry | knowledge |
| P0 | KN-T0202-0001 | 保持身体能力 | T02.02 | knowledge_entry | knowledge |
| P0 | KN-T0202-0002 | 保持认知能力 | T02.02 | knowledge_entry | knowledge |
| P0 | KN-T0203-0001 | 生物衰老是什么 | T02.03 | knowledge_entry | knowledge |
| P0 | KN-T0204-0001 | 测量—解读—行动—复测：长寿实践的反馈闭环 | T02.04 | knowledge_entry | knowledge |
| P0 | KN-T0206-0001 | 长寿策略是什么：从健康寿命目标到持续行动 | T02.06 | knowledge_entry | knowledge |

Risk-factor concepts may be explained at a general level. These entries must not calculate disease risk, predict disease, score users, or generate treatment plans.

### 6.3 Group C: Six Body Systems

Target: 18 candidate entries, three for each system.

| Priority | Planned Entry ID | Working Title | Primary Topic | Content Type | Information Layer |
|---|---|---|---|---|---|
| P0 | KN-T0301-0001 | 能量系统：定义 | T03.01 | knowledge_entry | knowledge |
| P0 | KN-T0301-0002 | 能量系统为什么重要 | T03.01 | knowledge_entry | knowledge |
| P1 | KN-T0301-0003 | 理解能量系统的背景信息 | T03.01 | knowledge_entry | knowledge |
| P0 | KN-T0302-0001 | 代谢系统：定义 | T03.02 | knowledge_entry | knowledge |
| P0 | KN-T0302-0002 | 代谢系统为什么重要 | T03.02 | knowledge_entry | knowledge |
| P1 | KN-T0302-0003 | 理解代谢系统的背景信息 | T03.02 | knowledge_entry | knowledge |
| P0 | KN-T0303-0001 | 心肺循环系统：定义 | T03.03 | knowledge_entry | knowledge |
| P0 | KN-T0303-0002 | 心肺循环系统为什么重要 | T03.03 | knowledge_entry | knowledge |
| P1 | KN-T0303-0003 | 理解心肺循环系统的背景信息 | T03.03 | knowledge_entry | knowledge |
| P0 | KN-T0304-0001 | 肌肉骨骼系统：定义 | T03.04 | knowledge_entry | knowledge |
| P0 | KN-T0304-0002 | 肌肉骨骼系统为什么重要 | T03.04 | knowledge_entry | knowledge |
| P1 | KN-T0304-0003 | 理解肌肉骨骼系统的背景信息 | T03.04 | knowledge_entry | knowledge |
| P0 | KN-T0305-0001 | 神经认知系统：定义 | T03.05 | knowledge_entry | knowledge |
| P0 | KN-T0305-0002 | 神经认知系统为什么重要 | T03.05 | knowledge_entry | knowledge |
| P1 | KN-T0305-0003 | 理解神经认知系统的背景信息 | T03.05 | knowledge_entry | knowledge |
| P0 | KN-T0306-0001 | 修复免疫系统：定义 | T03.06 | knowledge_entry | knowledge |
| P0 | KN-T0306-0002 | 修复免疫系统为什么重要 | T03.06 | knowledge_entry | knowledge |
| P1 | KN-T0306-0003 | 理解修复免疫系统的背景信息 | T03.06 | knowledge_entry | knowledge |

Body-system entries explain concepts and relevant context. They must not diagnose a system state, assign a system score, or infer disease from taxonomy placement.

### 6.4 Group D: Measurement and Records

Target: 9 candidate entries.

| Priority | Planned Entry ID | Working Title | Primary Topic | Content Type | Information Layer |
|---|---|---|---|---|---|
| P0 | KN-T0403-0001 | 什么是生物标志物 | T04.03 | knowledge_entry | knowledge |
| P0 | KN-T0403-0002 | 如何理解基线、长期趋势、测量误差与生物波动 | T04.03 | knowledge_entry | knowledge |
| P0 | KN-T0401-0001 | 为什么保留原始检测报告 | T04.01 | knowledge_entry | knowledge |
| P0 | KN-T0404-0001 | 数据新鲜度为什么重要 | T04.04 | knowledge_entry | knowledge |
| P0 | KN-T0405-0001 | 为什么单位不能省略或猜测 | T04.05 | knowledge_entry | knowledge |
| P0 | KN-T0406-0001 | 如何理解参考区间 | T04.06 | knowledge_entry | knowledge |
| P1 | KN-T0408-0001 | 如何理解可穿戴与消费级设备数据 | T04.08 | knowledge_entry | knowledge |
| P0 | KN-T0407-0001 | 数据来源为什么重要 | T04.07 | knowledge_entry | knowledge |
| P0 | KN-T0412-0001 | 用户健康信息库的数据边界 | T04.12 | knowledge_entry | knowledge |

Measurement entries explain context, provenance, limitations, and record organization. They must not convert measurements into diagnosis, risk calculation, scoring, or clinical orders.

### 6.5 Group E: Lifestyle Foundations

Target: 12 candidate entries.

Canonical lifestyle order:

```text
sleep
nutrition
exercise
stress
```

| Priority | Planned Entry ID | Working Title | Primary Topic | Content Type | Information Layer |
|---|---|---|---|---|---|
| P0 | KN-T0501-0001 | 睡眠基础 | T05.01 | knowledge_entry | knowledge |
| P1 | KN-T0501-0002 | 睡眠时间、规律与主观质量 | T05.01 | knowledge_entry | knowledge |
| P0 | KN-T0502-0001 | 营养基础 | T05.02 | knowledge_entry | knowledge |
| P0 | KN-T0502-0002 | 蛋白质基础 | T05.02 | knowledge_entry | knowledge |
| P0 | KN-T0502-0003 | 膳食纤维基础 | T05.02 | knowledge_entry | knowledge |
| P1 | KN-T0502-0004 | 水分与饮酒背景 | T05.02 | knowledge_entry | knowledge |
| P0 | KN-T0503-0001 | 锻炼基础 | T05.03 | knowledge_entry | knowledge |
| P0 | KN-T0503-0002 | 运动能力与心肺能力背景 | T05.03 | knowledge_entry | knowledge |
| P1 | KN-T0503-0003 | 力量、活动度与平衡 | T05.03 | knowledge_entry | knowledge |
| P0 | KN-T0504-0001 | 压力背景与主观压力 | T05.04 | knowledge_entry | knowledge |
| P0 | KN-T0505-0001 | 恢复基础 | T05.05 | knowledge_entry | knowledge |
| P1 | KN-T0500-0001 | 睡眠、营养、锻炼、压力的综合背景 | T05.00 | knowledge_entry | knowledge |

Lifestyle entries provide general education and context. They must not generate disease diets, personalized nutrition prescriptions, personalized training prescriptions, rehabilitation plans, or supplement protocols.

### 6.6 Group F: Action Resources

Target: 5 candidate entries.

The five currently planned Group F Action Resource candidates focus on low-risk tracking, information-completion, measurement, and education resources. This Action Resource selection does not exclude knowledge, progress, safety, or risk-awareness coverage of supplements, medications, experimental interventions, or high-risk longevity technologies elsewhere in Batch 001.

| Priority | Planned Entry ID | Working Title | Primary Topic | Content Type | Information Layer | Planned Permission |
|---|---|---|---|---|---|---|
| P0 | AR-T0701-0001 | 检测报告与健康记录整理 | T07.01 | action_resource | action_resource | R3 |
| P0 | AR-T0702-0001 | 家庭血压趋势记录工具 | T07.02 | action_resource | action_resource | R2 |
| P1 | AR-T0702-0002 | 体重与身体成分趋势记录工具 | T07.02 | action_resource | action_resource | R2 |
| P1 | AR-T0702-0003 | 可穿戴设备趋势记录 | T07.02 | action_resource | action_resource | R2 |
| P0 | AR-T0704-0001 | 睡眠日志与睡眠追踪工具 | T07.04 | action_resource | action_resource | R3 |

Planned permissions remain subject to Founder review. Evidence strength must not raise permission. R2 items are optional information-completion resources and must not be framed as required purchases, medical orders, or clinical recommendations.

Batch 001 may include selected supplement, medication, and high-risk intervention awareness entries when they are important for user understanding. Such entries require stricter evidence, safety, and permission boundaries.

They must not be converted into:

```text
medication recommendations
medication start, stop, or change advice
dosage recommendations
personalized supplements or interventions
personalized protocols
product purchase links
brand or service recommendations
```

Medication and high-risk topics should normally use knowledge, progress and viewpoints, invalid or harmful notes, or safety-boundary content rather than permissive Action Resource behavior. Where an Action Resource representation is necessary for classification, R0/R1/R2/R3 permissions remain controlling.

Existing `KS-RESOURCE-*` drafts may be used as reviewed source material. Before creating an `AR-*` entry, production must perform a duplicate and lineage check so that the new library does not create two canonical copies of the same resource.

### 6.7 Group G: Foundational Medical Fields and Practice Models

Target: 4 candidate entries.

These entries explain field and practice-model labels that proactive longevity users commonly encounter. They are concept education, not intervention endorsement. Each specific test, product, service, therapy, or protocol mentioned under one of these labels still requires separate evidence, safety, regulatory, and actionability review.

| Priority | Planned Entry ID | Working Title | English Title | Primary Topic | Content Type | Information Layer |
|---|---|---|---|---|---|---|
| P0 | KN-T0912-0001 | 长寿医学是什么 | What Is Longevity Medicine? | T09.12 | knowledge_entry | knowledge |
| P0 | KN-T0912-0002 | 生活方式医学是什么 | What Is Lifestyle Medicine? | T09.12 | knowledge_entry | knowledge |
| P1-high | KN-T0912-0003 | 功能医学是什么 | What Is Functional Medicine? | T09.12 | knowledge_entry | knowledge |
| P1-high | KN-T0912-0004 | 再生医学是什么 | What Is Regenerative Medicine? | T09.12 | knowledge_entry | knowledge |

No existing candidate is replaced or removed. The four concepts do not duplicate an existing field-definition candidate, and removing foundational, safety-critical, measurement, body-system, medication, supplement, or high-risk awareness candidates solely to preserve the previous number would weaken the plan. This is therefore a Founder-approved candidate-pool expansion from 56 to 60, while the final target remains approximately 50 accepted entries.

### 6.8 Planned Count Summary

| Group | Candidate Count |
|---|---:|
| Group A: Congtie Foundation | 9 |
| Group B: Longevity Strategy | 6 |
| Group C: Six Body Systems | 18 |
| Group D: Measurement and Records | 9 |
| Group E: Lifestyle Foundations | 12 |
| Group F: Action Resources | 5 |
| Group G: Foundational Medical Fields and Practice Models | 4 |
| **Total planned candidates** | **63** |

Batch completion target remains approximately 50 accepted entries. A final count between 50 and 63 is acceptable when reductions are caused by evidence gaps, consolidation, duplication, prioritization, or safety review.

The T01.01 consolidation and T01.07 substitution do not increase the original 56-candidate inventory. `KN-T0101-0001` remains the approved canonical healthspan object and is not duplicated as a new open candidate. Group G expanded the pool from 56 to 60. The separately Founder-approved T01.03 candidate allocation adds `KN-T0103-0001` and expands the pool from 60 to 61. The Founder-approved T02.06 strategy-concept allocation adds `KN-T0206-0001` and expands the pool from 61 to 62. The Founder-approved `KN-T0403-0002` allocation expands the current pool from 62 to 63 without changing the approximately 50-entry final target.

---

## 7. Entry ID Planning

Entry IDs follow:

```text
{TYPE_PREFIX}-{PRIMARY_TOPIC_ID_NO_DOT}-{NNNN}
```

Examples:

```text
KN-T0101-0001
AR-T0702-0001
ED-T0907-0001
GV-T0601-0001
```

Batch 001 rules:

1. The prefix must match the content type and intended information layer.
2. The embedded topic must match `primary_topic_id`.
3. `primary_topic_id` must be first in `topic_ids`.
4. The numeric suffix is four digits.
5. IDs are reserved when drafting begins and are not reassigned after rejection or archival.
6. Every planned ID must pass a duplicate check against existing canonical entries and the Batch 001 inventory.
7. Renaming a working title does not change the reserved entry ID.
8. T10 IDs must not be allocated in Batch 001.

The current validator checks single-file Entry ID format. Cross-file uniqueness must be checked manually in Batch 001 until a directory or index validator is separately approved and implemented.

The Founder-approved canonical entry directory convention is `agent/longevity_knowledge_base/entries/<information_layer>/`. Batch 001 must use this path and must not create duplicate canonical files in legacy top-level layer directories or an `items/` tree.

---

## 8. Production Workflow

Recommended production order:

```text
1. Use the canonical `entries/<information_layer>/` directory and reserve IDs.
2. Complete duplicate and Knowledge Seed lineage checks.
3. Create entry from the v0.1 template.
4. Assign primary and secondary taxonomy topics.
5. Draft the Chinese explanation and concise English metadata.
6. Add evidence level, evidence posture, source types, and source URLs.
7. Add allowed use, disallowed use, safety boundary, and clinical sensitivity.
8. Add conditional layer fields, including Action Resource permission fields.
9. Run the single-item validator.
10. Resolve structural errors before AI review.
11. Record AI review findings without changing approval status.
12. Send the reviewed entry to the human review gate.
13. Publish only through a separately approved publication workflow.
```

### 8.1 Required Entry Metadata

At minimum, every Batch 001 entry must include:

```text
schema_version
entry_id
entry_slug
content_type
information_layer
title_zh
title_en
language
primary_topic_id
topic_ids
status
created_by
created_date
version
evidence_level
evidence_posture
source_type
safety_boundary
allowed_use
disallowed_use
```

Entries must also include all additional fields required by `agent/longevity_knowledge_item_schema.v0.1.md` and any conditional fields required by their information layer or topic.

### 8.2 Validation Requirement

Every entry must pass:

```bash
python3 agent/longevity_knowledge_base/scripts/validate_longevity_knowledge_item.py <entry-file>
```

before it may move to human approval.

Validator success confirms structural and governance validity only. It does not confirm medical accuracy, evidence quality, editorial quality, or publication readiness.

### 8.3 Source Production Rules

- Prefer official, professional, peer-reviewed, and high-quality educational sources.
- Use governed `source_type` values.
- Treat aliases as migration warnings and normalize new entries to canonical values.
- Do not use commercial claims as health outcome evidence.
- Record source limitations and uncertainty.
- Do not embed paid or copyrighted full text without separate review and permission.
- Do not add purchase links or conversion-oriented recommendations.

### 8.4 Action Resource Production Rules

Every Action Resource entry requires:

```text
resource_type
recommendation_permission
commercial_boundary
commercial_relationship
```

Batch 001 must preserve:

```text
R0 = prohibited from automatic recommendation
R1 = user-initiated explanation only
R2 = information-completion option
R3 = low-risk general tool option
```

The expected commercial boundary is:

```text
zero_commission_v0
```

---

## 9. Review Workflow

Standard lifecycle:

```text
draft
↓
ai_review_pending
↓
ai_reviewed
↓
human_review_pending
↓
approved
↓
published
```

`needs_revision`, `rejected`, and `archived` remain valid lifecycle outcomes where appropriate.

### 9.1 Draft Review

The author confirms scope, topic mapping, required fields, sources, and non-clinical language.

### 9.2 AI Review

AI review may check:

- structure and validator compliance
- topic consistency
- evidence metadata completeness
- source-type normalization
- unsupported or overconfident wording
- safety-boundary consistency
- duplication and terminology consistency
- action-resource permission language

AI review may not grant `approved` or `published` status.

### 9.3 Human Review Gate

The Founder approves:

```text
topic mapping
evidence level
wording
safety boundary
publication status
```

For Action Resources, the Founder also confirms recommendation permission, auto-trigger posture, commercial boundary, and whether the resource belongs in Batch 001.

For clinically sensitive entries, human review must verify that the entry remains educational and does not create diagnosis, treatment, dosage, risk calculation, scoring, or personalized intervention.

### 9.4 Publication Separation

`approved` does not automatically mean `published`.

Publication requires an explicit transition and any future publication/index/runtime checks. Batch 001 planning does not connect entries to runtime retrieval.

---

## 10. Acceptance Criteria

Batch 001 is complete when:

- approximately 50 entries have been created, with 63 as the maximum current candidate inventory
- every completed entry follows the Knowledge Item Schema
- every completed entry passes `validate_longevity_knowledge_item.py`
- every completed entry maps to valid taxonomy topics
- T01 through T09 have meaningful coverage
- T10 has no Batch 001 entry
- every completed entry contains evidence metadata and traceable source information
- every completed entry includes allowed use, disallowed use, and a safety boundary
- Action Resources preserve R0/R1/R2/R3 permissions and `zero_commission_v0`
- duplicate and lineage checks have been completed
- AI review findings have been recorded
- Founder review has confirmed topic mapping, evidence level, wording, safety boundary, and publication status
- no entry bypasses the human review gate
- all content respects the v0 non-clinical boundary
- no private user health information is stored in the public knowledge library
- no product marketplace, purchase recommendation, or hidden commercial conversion is introduced

Quality and safety take precedence over reaching 63 entries.

---

## 11. Future Batches

### 11.1 Batch 002

Focus:

```text
deeper nutrition
exercise science
biomarkers
```

Potential expansion includes more detailed dietary concepts, exercise modalities, recovery context, measurement interpretation boundaries, and evidence summaries.

### 11.2 Batch 003

Focus:

```text
action resources
products
services
```

Batch 003 should expand only after Action Resource permissions, commercial boundaries, source governance, and runtime controls have been reviewed.

### 11.3 Batch 004

Focus:

```text
research progress
longevity biotechnology
```

These entries should use `information_layer: progress_and_viewpoints` and default to `actionability_status: education_only`. They must not become treatment, medication, dosage, or personalized protocol recommendations.

### 11.4 Cross-batch Rule

Future batches should reuse the same schema, taxonomy, evidence governance, lifecycle, and human approval gate unless a separately approved version supersedes them.

---

## 12. Final Note

Batch 001 is the first production test of the Congtie Longevity Information Library governance model.

The safest production principle is:

```text
Start with a small, useful foundation.
Prefer quality over count.
Make evidence and limitations traceable.
Keep private user context separate.
Keep every entry non-clinical and human-reviewed.
```
