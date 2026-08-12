# Longevity Topic Taxonomy v0.1

Version: v0.1
Project: Congtie
Status: Draft
Owner: Congtie Agent Team
Last Updated: 2026-05-29

---

## 1. Purpose

This document defines the topic taxonomy for the Congtie Longevity Information Library.

The taxonomy is the horizontal topic map of the library.

It helps Congtie organize:

* stable knowledge
* action resources
* progress and viewpoints
* education materials
* source and evidence references
* governance and curation rules
* topic-to-entry mapping
* human-facing navigation
* agent-facing retrieval

This taxonomy aligns with the vertical architecture defined in:

```text
agent/knowledge_seed_v0/longevity_information_library_architecture.v0.1.md
```

The architecture defines the information layers.

This taxonomy defines the topic map.

Both are required.

```text
Architecture = information layer and governance structure
Taxonomy = topic classification and retrieval map
```

This document does not create runtime implementation, loader behavior, schema validation, tests, API contracts, JSON index, or topic files.

---

## 2. One-line Definition

The Congtie Longevity Topic Taxonomy is the structured topic map for organizing information around the user goal and Congtie mission of extending healthspan.

In Congtie v0:

```text
User goal / user result = extend healthspan
Congtie mission = help users extend healthspan
```

Chinese expression:

```text
用户目标 / 结果：延长健康寿命
葱铁使命：帮助用户延长健康寿命
```

The taxonomy exists to support:

```text
measurement
→ explanation
→ safe action
→ iteration
```

It is not a disease taxonomy.

It is not a treatment taxonomy.

It is not a clinical decision taxonomy.

It is a healthspan-oriented information taxonomy.

---

## 3. Design Principles

### 3.1 Mission-derived

The taxonomy is derived from Congtie’s mission:

```text
帮助用户延长健康寿命
```

The taxonomy should organize content around what users need to understand and do safely in order to extend healthspan.

### 3.2 Healthspan-first

The taxonomy prioritizes:

* avoiding premature mortality
* maintaining physical and cognitive capability
* slowing biological aging
* reducing uncertainty through measurement and explanation
* supporting low-risk action
* preparing for professional consultation when needed

It does not prioritize disease labeling.

### 3.3 Dual Users: Humans and Agents

The taxonomy serves two user types.

Human users may access it through:

* Web
* App
* Mini Program
* Search
* Feishu-style knowledge pages
* future dashboards
* future content navigation

Agent users may access it through:

* retrieval
* tool calls
* CLI
* API
* MCP
* A2A workflows
* structured topic IDs
* JSON indexes
* runtime context selection

The taxonomy must be readable by humans and stable enough for agents.

### 3.4 Non-clinical Boundary

This taxonomy must preserve Congtie v0’s non-clinical boundary.

It must not create:

* diagnosis
* treatment
* medication advice
* dosage advice
* clinical recommendation
* system scoring
* disease risk calculation
* disease prediction
* personalized supplement protocol
* personalized medical intervention

### 3.5 China-first but Global-aware

The taxonomy is designed first for Chinese users.

It should support:

* Chinese language usage
* Chinese health service context
* Chinese user behavior
* China availability and regulatory status
* China professional and public-health sources
* international evidence where relevant

China-first does not mean China-only.

### 3.6 Layer-aware

Every topic entry should be compatible with the Longevity Information Library layers:

```text
knowledge
action_resource
progress_and_viewpoints
education
governance
```

The same domain topic may contain entries from different information layers.

For example:

```text
Nutrition can contain:
- stable knowledge
- action resources
- progress and viewpoints
- education materials
- governance rules
```

---

## 4. Relationship to Existing Documents

This taxonomy should be read together with:

```text
agent/knowledge_seed_v0/longevity_information_library_architecture.v0.1.md
agent/knowledge_seed_v0/evidence_grading_framework.v0.1.md
agent/knowledge_seed_v0/action_resource_curation_rules.v0.2.md
agent/knowledge_seed_v0/proactive_action_boundary.v0.1.md
agent/knowledge_seed_v0/user_health_information_library_spec.v0.1.md
agent/knowledge_seed_v0/knowledge_seed_scope.v0.1.md
agent/knowledge_seed_v0/knowledge_seed_content_template.v0.1.md
agent/knowledge_seed_v0/knowledge_seed_topic_plan.v0.1.md
```

### 4.1 Architecture Alignment

The architecture defines:

```text
Knowledge Layer
Action Resource Layer
Progress and Viewpoints Layer
Education Layer
Governance Layer
```

This taxonomy maps topics across those layers.

Therefore, every content entry should include:

```yaml
information_layer:
```

Allowed values:

```text
knowledge
action_resource
progress_and_viewpoints
education
governance
```

### 4.2 用户健康信息库 Boundary

用户健康信息库 is separate from the general Longevity Information Library.

The taxonomy covers general reusable information.

The taxonomy does not manage private user data.

User-specific data such as:

* personal biomarker values
* personal lab reports
* personal medical records
* personal lifestyle records
* personal supplement use history
* personal action history

belongs to 用户健康信息库, not to this taxonomy.

The taxonomy may define general concepts such as “lab reports,” “biomarker records,” and “privacy rules,” but it must not store or classify private user records as public knowledge entries.

### 4.3 Progress and Viewpoints Boundary

“进展与观点” uses the internal label:

```text
progress_and_viewpoints
```

Progress and viewpoints are not stable knowledge by default.

Topic 08 is the primary home for cross-domain progress and viewpoints.

However, any topic may contain entries with:

```yaml
information_layer: progress_and_viewpoints
```

For example:

```text
A new biomarker paper may live under Measurement topics
while still using information_layer: progress_and_viewpoints.
```

All progress and viewpoints entries must follow the Progress and Viewpoints boundary:

* education only unless later approved
* no direct action recommendation
* no treatment
* no supplement protocol
* no clinical decision
* no disease risk calculation
* no system scoring

### 4.4 protocol_note

`protocol_note` is an allowed content object type in this taxonomy.

It may include:

* public longevity protocols
* expert protocols
* founder-curated protocol notes
* third-party protocol summaries
* protocol comparisons
* safe boundary notes

Protocol notes must follow R0/R1/R2/R3 permissions when they involve action resources.

Any protocol involving drugs, supplements, hormones, off-label interventions, invasive interventions, experimental therapies, aggressive testing, or personalized plans must default to high safety boundaries.

v0 does not use protocol notes to generate personalized protocols.

---

## 5. Content Object Types

Allowed content object types include:

```text
topic
subtopic
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

### 5.1 topic

A stable classification node.

### 5.2 subtopic

A child topic under a parent topic.

### 5.3 knowledge_entry

A reusable explanation-oriented knowledge entry.

### 5.4 action_resource

A permission-controlled product, service, device, tool, supplement, or information resource.

Action resources must follow:

```text
R0 / R1 / R2 / R3
```

### 5.5 progress_and_viewpoint

A research progress, expert viewpoint, product development progress, regulatory progress, or commercialization status entry.

Must include:

```yaml
research_stage:
actionability_status:
evidence_level:
source_type:
```

### 5.6 education_article

A user-facing educational article.

### 5.7 glossary_entry

A short concept definition.

### 5.8 checklist

A practical checklist for safe information organization or action preparation.

### 5.9 clinician_conversation_preparation

A doctor or professional consultation preparation object.

### 5.10 source_note

A note about a source, source quality, or source use boundary.

### 5.11 evidence_summary

A structured evidence summary.

### 5.12 protocol_note

A non-personalized protocol reference note.

### 5.13 invalid_or_harmful_note

A note explaining invalid, harmful, outdated, exaggerated, unsupported, or unsafe information.

### 5.14 governance_rule

A governance rule for the information library.

### 5.15 curation_rule

A curation, review, or publishing rule.

### 5.16 safety_boundary

A safety boundary entry.

---

## 6. Topic ID Rules

### 6.1 Topic ID Format

Top-level topics use:

```text
T01
T02
T03
...
T10
```

Second-level topics use:

```text
T01.01
T01.02
...
```

Third-level topics use:

```text
T01.01.01
```

Topic IDs should be stable.

Do not reuse retired IDs.

### 6.2 Recommended Topic Metadata

Every topic should include:

```yaml
topic_id:
topic_slug:
title_zh:
title_en:
level:
parent_topic_id:
topic_path:
status:
scope:
information_layer:
allowed_content_types:
default_evidence_level:
default_evidence_posture:
default_permission_level:
is_clinical_sensitive:
actionability_status:
china_availability:
regulatory_status:
related_knowledge_ids:
related_resource_ids:
related_source_ids:
notes:
```

### 6.3 Field Notes

`information_layer` should use:

```text
knowledge
action_resource
progress_and_viewpoints
education
governance
```

`default_permission_level` should use:

```text
R0
R1
R2
R3
not_applicable
```

`is_clinical_sensitive` should be:

```text
true
false
```

Use `true` for disease, medication, clinical testing, high-risk intervention, emergency, supplement protocol, hormone, drug, and disease risk topics.

`actionability_status` should be used especially for progress and viewpoints entries.

Recommended values:

```text
not_actionable
education_only
watchlist
requires_professional_context
future_candidate
deprecated
not_applicable
```

### 6.4 Entry-level Fields

Entry-level metadata should align with the architecture and Feishu fields:

```yaml
entry_id:
title_zh:
title_en:
information_layer:
category:
evidence_level:
evidence_posture:
source_type:
source_urls:
summary:
user_visible_explanation:
allowed_use:
disallowed_use:
safety_boundary:
commercial_boundary:
related_body_systems:
related_lifestyle_keywords:
china_availability:
regulatory_status:
curation_status:
reviewer:
review_date:
next_review_date:
approval_status:
approval_note:
```

For action resources, also include:

```yaml
resource_type:
recommendation_permission:
recommendation_permission_label:
auto_trigger_allowed:
commercial_boundary_level:
privacy_risk:
source_enrichment_status:
```

For nutrition and supplement entries, also include:

```yaml
nutrition_category:
common_use_context:
common_dosages_in_literature:
safety_notes:
known_interactions:
not_for_personalized_protocol:
```

---

## 7. Top-level Topic Map

The v0 top-level taxonomy is:

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

# T01 Longevity Foundation 长寿基础

## T01.00 Scope

This topic defines the basic meaning, mission, boundaries, and user mental model of longevity in Congtie.

It should answer:

```text
What is longevity?
What is healthspan?
What is Congtie trying to help users achieve?
What is Congtie not?
Why does context matter?
Why is this non-clinical?
```

Default information layer:

```text
knowledge
```

Allowed content types:

```text
knowledge_entry
glossary_entry
education_article
safety_boundary
```

Disallowed content types:

```text
treatment_guide
medication_protocol
dosage_protocol
disease_risk_calculator
personalized_supplement_protocol
```

## T01.01 Healthspan 健康寿命

Scope:

* healthspan definition
* lifespan vs healthspan
* functional years
* quality of life
* capability preservation

## T01.02 Longevity Goal 长寿目标

Scope:

```text
延长健康寿命
```

This is both:

```text
user goal / user result
Congtie mission
```

Do not place strategy items here.

Strategy items belong to T02.

## T01.03 Longevity Mindset 长寿心智

Scope:

* long-term orientation
* uncertainty reduction
* body transparency
* ownership of health data
* action with boundaries

## T01.04 Body Transparency 身体透明

Scope:

* from body black box to body state transparency
* records and context
* trend vs single data point
* user attention reduction

## T01.05 Congtie Role and Boundaries 葱铁角色与边界

Scope:

* longevity assistant
* not doctor
* non-diagnostic
* no treatment
* no medication
* no dosage
* no clinical decision
* no emergency replacement

## T01.06 User Health Information Library Concept 用户健康信息库概念

Scope:

* what 用户健康信息库 is
* why it is separate from the Longevity Information Library
* private user data
* user control
* export
* deletion
* sharing permission
* not hidden commercial targeting
* not hidden medical personalization

Note:

This topic explains the concept.

Private user data itself does not belong in this taxonomy.

---

# T02 Longevity Strategy 长寿策略

## T02.00 Scope

This topic defines Congtie’s healthspan strategy logic.

Goal:

```text
延长健康寿命
```

Core strategies:

```text
避免早逝
保持能力
延缓生物衰老
```

Operational approach:

```text
测量
→ 解释
→ 安全行动
→ 迭代
```

Default information layer:

```text
knowledge
```

Allowed content types:

```text
knowledge_entry
education_article
checklist
glossary_entry
```

## T02.01 Prevent Premature Mortality 避免早逝

Scope:

* high-level premature mortality prevention
* non-clinical explanation
* safety boundary
* professional consultation preparation
* no disease risk calculation

## T02.02 Maintain Physical and Cognitive Capability 保持能力

Scope:

* physical capability
* cognitive capability
* strength
* mobility
* endurance
* energy
* recovery
* daily functioning

## T02.03 Slow Biological Aging 延缓生物衰老

Scope:

* biological aging concepts
* biological age as context
* aging hallmarks education
* no biological age scoring engine in v0
* no age-reversal protocol

## T02.04 Measurement-Explanation-Action-Iteration 测量—解释—行动—迭代

Scope:

* measurement
* context
* explanation
* safe next action
* feedback loop
* no hidden medical personalization

## T02.05 Dynamic Measurement and Intervention Strategy 动态测量干预策略

Scope:

* measurement trigger logic
* information completion
* next action rationale
* optional measurement resources
* no clinical order
* no treatment protocol

---

# T03 Body Systems 身体系统

## T03.00 Scope

This topic defines the six body systems used by Congtie.

The six systems are:

```text
Energy System
Metabolic System
Cardiopulmonary System
Musculoskeletal System
Neurocognitive System
Repair Immune System
```

Default information layer:

```text
knowledge
```

Allowed content types:

```text
knowledge_entry
glossary_entry
education_article
```

Disallowed:

```text
diagnosis
system scoring from taxonomy alone
disease risk calculation
clinical interpretation
```

## T03.01 Energy System 能量系统

Scope:

* energy production
* energy use
* fatigue context
* recovery
* vitality
* sleep / nutrition / exercise / stress context

## T03.02 Metabolic System 代谢系统

Scope:

* nutrition use
* glucose/lipid context
* body composition context
* weight context
* metabolic flexibility education
* no disease diagnosis

## T03.03 Cardiopulmonary System 心肺循环系统

Scope:

* oxygen delivery
* heart and vascular context
* exercise capacity
* blood pressure context
* heart rate context
* VO₂max as context
* no cardiovascular risk calculation in v0

## T03.04 Musculoskeletal System 肌肉骨骼系统

Scope:

* muscle
* bone
* strength
* mobility
* balance
* posture
* gait
* physical capability

## T03.05 Neurocognitive System 神经认知系统

Scope:

* sleep
* attention
* cognition
* mood context
* stress response
* mental performance
* no mental health diagnosis

## T03.06 Repair Immune System 修复免疫系统

Scope:

* repair
* resilience
* inflammation context
* immune context
* recovery
* recent illness context
* no immune disease diagnosis

## T03.07 Gut and Microbiome Context 肠道与微生物组背景

Status:

```text
candidate / non-core-system
```

Scope:

* gut health concepts
* microbiome basics
* gut-brain axis context
* fiber and diet connection
* stool and microbiome testing context
* non-clinical boundary

Important:

This topic is not the seventh Congtie body system in v0.

It is a cross-cutting context topic.

---

# T04 Measurement and Records 测量与记录

## T04.00 Scope

This topic defines general measurement knowledge and record organization.

Important boundary:

This topic defines general measurement knowledge and record standards.

Private user test results, biomarker values, lab reports, and lifestyle records belong to 用户健康信息库.

They should not be committed into general taxonomy or public knowledge files.

Default information layer:

```text
knowledge
```

Allowed content types:

```text
knowledge_entry
action_resource
checklist
education_article
clinician_conversation_preparation
```

## T04.01 Test Reports 检测报告

Scope:

* original test reports
* lab reports
* physical exam reports
* imaging reports
* device export reports
* report metadata

## T04.02 Health Records 健康记录

Scope:

* longitudinal health record
* health timeline
* prior records
* data source
* record keeping

## T04.03 Biomarkers 生物标志物

Scope:

* biomarker definition
* biomarker metadata
* unit
* reference range
* test date
* source
* no disease diagnosis from single marker

## T04.04 Freshness 数据新鲜度

Scope:

* test date
* current vs stale data
* freshness status
* time comparison

## T04.05 Units 单位

Scope:

* unit dependency
* unit conversion boundary
* no guessing

## T04.06 Reference Ranges 参考区间

Scope:

* lab-specific reference ranges
* population and method context
* no universal assumption

## T04.07 Data Source 数据来源

Scope:

* lab report
* wearable
* device
* manual entry
* user memory
* app import
* source reliability

## T04.08 Wearable and Device Data 设备数据

Scope:

* consumer device data
* wearable trend data
* algorithmic estimates
* device limitations
* no diagnosis

## T04.09 Imaging and Digital Signals 影像与数字信号

Scope:

* imaging reports
* ECG
* pulse wave
* raw physical signals
* device-generated signals
* no image diagnosis in v0

## T04.10 Sample Types 样本类型

Scope:

* blood
* urine
* saliva
* stool
* microbiome sample
* hair
* skin / sebum
* tissue, when relevant
* breath
* digital signal / imaging

## T04.11 Data Privacy and Consent 数据隐私与授权

Scope:

* personal health data
* user permission
* export
* deletion
* sharing
* no hidden targeting

## T04.12 User Health Information Library Boundary 用户健康信息库边界

Scope:

* private user-specific data
* user control
* not part of general taxonomy
* runtime context only
* permission-gated use

---

# T05 Lifestyle Foundations 生活方式基础

## T05.00 Scope

This topic organizes core lifestyle context.

Canonical lifestyle keyword order:

```text
睡眠 / 营养 / 锻炼 / 压力
sleep / nutrition / exercise / stress
```

Default information layer:

```text
knowledge
```

Allowed content types:

```text
knowledge_entry
action_resource
education_article
checklist
```

## T05.01 Sleep 睡眠

Scope:

* sleep duration
* sleep timing
* sleep regularity
* sleep quality
* sleep diary
* consumer sleep trackers
* PSG boundary
* no sleep disease diagnosis

## T05.02 Nutrition 营养

Scope:

* food patterns
* protein
* fiber
* hydration
* alcohol
* dietary logs
* supplement background
* meal timing
* fasting patterns
* time-restricted eating
* caloric restriction context
* drug-food or supplement boundary, if relevant
* no disease diet prescription

## T05.03 Exercise 锻炼

Scope:

* aerobic exercise
* strength training
* mobility
* balance
* stability
* flexibility
* walking
* sports
* training logs
* VO₂max estimate boundary
* no training prescription in v0

## T05.04 Stress 压力

Scope:

* perceived stress
* work stress
* family stress
* recovery pressure
* emotional load
* stress logs
* no mental health diagnosis

## T05.05 Recovery 恢复

Scope:

* recovery feeling
* fatigue
* soreness
* rest days
* HRV context
* sleep/exercise/nutrition/stress integration

## T05.06 Heat and Cold Exposure 热冷暴露

Scope:

* sauna
* warm bathing
* foot bathing
* hot spring
* cold exposure
* safety boundary
* no treatment claim

## T05.07 Light and Circadian Rhythm 光照与昼夜节律

Scope:

* morning light
* evening light
* blue light context
* circadian timing
* sleep timing

## T05.08 Social Connection 社会连接

Scope:

* relationships
* loneliness context
* family
* friends
* community
* purpose

## T05.09 Nature and Environment 自然与环境

Scope:

* outdoor time
* air quality
* green space
* environmental exposure
* travel context

## T05.10 Food-as-Medicine and Traditional Diet Context 药食同源与食疗语境

Scope:

* Chinese food-as-medicine culture
* traditional diet concepts
* herbs as food context
* non-clinical education
* no treatment
* no prescription
* no herb/drug recommendation
* no personalized protocol

## T05.11 Mind-Body Exercise and Traditional Movement 身心运动与传统功法

Scope:

* tai chi
* ba duan jin
* qigong
* stretching
* breath and movement
* stability
* balance
* body control
* no rehabilitation prescription
* no disease treatment claim

## T05.12 Fasting and Eating Patterns 禁食与进食节律

Scope:

* fasting patterns
* time-restricted eating
* meal timing
* caloric restriction context
* safety boundary
* no disease diet prescription

---

# T06 Risk Prevention and Safety 风险预防与安全

## T06.00 Scope

This topic covers non-clinical risk prevention education and safety boundary topics.

It is not a disease encyclopedia.

It is not a disease risk calculator.

Default information layer:

```text
knowledge
```

Allowed content types:

```text
education_article
glossary_entry
clinician_conversation_preparation
safety_boundary
invalid_or_harmful_note
```

Disallowed content types:

```text
treatment_guide
medication_protocol
disease_risk_calculator
clinical_pathway
personalized_intervention_plan
```

## T06.01 Safety Boundaries 安全边界

Scope:

* no diagnosis
* no treatment
* no medication
* no dosage
* no emergency replacement
* no disease risk calculation
* no system scoring

## T06.02 Emergency and Urgent Care Boundary 急诊与紧急边界

Scope:

* serious symptoms
* sudden worsening
* persistent severe condition
* real-world medical help
* no triage engine

## T06.03 Cardiovascular Risk Topics 心血管风险主题

Scope:

* education only
* risk factors as general concept
* clinician conversation preparation
* no risk score
* no diagnosis
* no treatment

## T06.04 Cancer Risk Topics 癌症风险主题

Scope:

* education only
* screening concept boundary
* no cancer prediction
* no diagnosis
* no screening recommendation as clinical order

## T06.05 Metabolic Risk Topics 代谢风险主题

Scope:

* glucose/lipid context
* body composition context
* education only
* no diabetes diagnosis
* no risk score

## T06.06 Neurocognitive Risk Topics 神经认知风险主题

Scope:

* cognition
* sleep
* memory concern
* education only
* no dementia prediction
* no mental health diagnosis

## T06.07 Musculoskeletal Risk Topics 肌肉骨骼风险主题

Scope:

* falls
* mobility
* strength
* bone context
* injury boundary
* no diagnosis
* no rehab prescription

## T06.08 Oral Health Risk Topics 口腔健康风险主题

Scope:

* oral health education
* gum health context
* inflammation context
* clinician/dentist consultation preparation
* no dental diagnosis
* no treatment plan

## T06.09 Invalid, Harmful and Overhyped Claims 无效、有害与夸大信息

Scope:

* disproven claims
* outdated guidance
* unsafe practices
* pseudoscience
* aggressive anti-aging claims
* commercial exaggeration

Entries should include:

```yaml
invalid_reason:
harm_risk:
superseded_by:
deprecated_date:
source_for_deprecation:
```

---

# T07 Interventions and Action Resources 干预与行动资源

## T07.00 Scope

This topic covers action resources and intervention-related content.

All entries under this topic must follow R0/R1/R2/R3 permission rules.

Default information layer:

```text
action_resource
```

Allowed content types:

```text
action_resource
education_article
protocol_note
safety_boundary
source_note
```

Disallowed in v0:

```text
personalized_protocol
dosage_protocol
treatment_plan
medication_plan
clinical_order
```

## T07.01 Information Resources 信息资源

Scope:

* reports
* records
* summaries
* checklists
* source documents

Default permission:

```text
R3
```

## T07.02 Devices 设备

Scope:

* blood pressure monitor
* body composition monitor
* wearable device
* sleep tracking device
* CGM as future separate topic
* continuous monitoring devices
* device boundaries

Default permission:

```text
R2
```

Some devices may be R0/R1 depending on risk, medical status, and intervention claims.

## T07.03 Testing Services 检测服务

Scope:

* basic blood testing service
* laboratory service
* sample collection
* test report service
* no clinical order

Default permission:

```text
R2
```

## T07.04 Lifestyle Tools 生活方式工具

Scope:

* sleep log
* nutrition log
* exercise log
* stress log
* habit tracker
* checklists

Default permission:

```text
R3
```

## T07.05 Nutrition Products 营养产品

Scope:

* protein powder
* protein nutrition products
* meal replacement
* functional beverage
* protein snacks
* fiber food products

Entries must include:

```yaml
nutrition_category:
```

Allowed values:

```text
whole_food
dietary_pattern
meal_replacement
functional_beverage
snack
dietary_supplement
longevity_supplement
```

Default permission:

```text
R1
```

unless reviewed as low-risk general food or record-keeping context.

## T07.06 Supplements 补充剂

Scope:

* creatine
* omega-3
* vitamin D
* magnesium
* probiotics
* fiber supplements
* longevity supplements
* antioxidant and cellular health topics

Default permission:

```text
R1
auto_trigger_allowed: false
not_for_personalized_protocol: true
```

v0 does not provide supplement dosage, timing, cycle, stack, or personalized protocol.

## T07.07 Medications and Off-label Drug Topics 药物与超适应症药物话题

Default permission:

```text
R0
```

Scope:

* rapamycin
* metformin
* GLP-1 medications
* statins
* blood pressure medications
* sleep medications
* off-label drug protocols

Allowed:

```text
boundary explanation
education-only discussion if user asks
professional context reminder
```

Disallowed:

```text
recommendation
dose
start/stop/change medication
protocol
treatment
```

## T07.08 Hormones and Peptides 激素与肽类

Default permission:

```text
R0
```

Scope:

* hormone therapy
* peptide protocols
* injectable interventions
* experimental interventions

## T07.09 Services 服务

Scope:

* record digitization
* test booking support
* clinician conversation preparation
* health coaching with boundary
* user-confirmed task preparation

## T07.10 Longevity Protocols 长寿方案

Scope:

* public longevity protocols
* expert protocols
* founder-curated protocol notes
* protocol comparison
* protocol safety boundary
* Congtie-localized protocol notes, if reviewed

Rules:

* no personalized protocol in v0
* no dosage
* no drug protocol
* no hidden supplement protocol
* R0/R1 by default when involving drugs, supplements, hormones, experimental interventions, or aggressive protocols
* user-initiated explanation only for high-boundary protocols

## T07.11 Physical Exposure Tools 物理暴露工具

Scope:

* sauna
* warm bathing
* foot bathing
* hot spring
* cold exposure
* red light context
* safety boundary

High-risk or treatment-claim devices require separate review.

## T07.12 Oral Care Resources 口腔护理资源

Scope:

* oral hygiene education
* dentist conversation preparation
* oral care action resources
* no dental diagnosis
* no treatment plan

## T07.13 Skin, Hair, Eye, Ear and Appearance Resources 皮肤、头发、眼耳与外显资源

Scope:

* skin health context
* hair context
* eye/ear context
* appearance aging context
* non-clinical education
* no treatment claim
* high-risk devices reviewed separately

## T07.14 Experimental and High-risk Interventions 实验性与高风险干预

Default permission:

```text
R0
```

Scope:

* stem cell therapy
* exosome therapy
* invasive anti-aging procedures
* experimental longevity interventions
* aggressive detox programs
* unverified clinics

---

# T08 Progress and Viewpoints 进展与观点

## T08.00 Scope

This topic captures research progress, expert viewpoints, product development progress, regulatory progress, and commercialization status.

Internal label:

```text
progress_and_viewpoints
```

This topic is the primary home for cross-domain progress and viewpoints.

However, any domain topic may include entries with:

```yaml
information_layer: progress_and_viewpoints
```

All such entries must follow Progress and Viewpoints boundary rules.

Default information layer:

```text
progress_and_viewpoints
```

Allowed content types:

```text
progress_and_viewpoint
evidence_summary
source_note
education_article
```

Disallowed:

```text
action recommendation
treatment
supplement protocol
clinical decision
risk calculation
system scoring
```

Required metadata:

```yaml
research_stage:
evidence_level:
source_type:
supporting_viewpoints:
opposing_or_cautionary_viewpoints:
regulatory_status:
commercialization_status:
actionability_status:
last_reviewed:
next_review_date:
```

Default `actionability_status`:

```text
education_only
```

## T08.01 Basic Research Progress 基础研究进展

Scope:

* animal studies
* cell studies
* mechanism research
* early biomarkers

## T08.02 Clinical Research Progress 临床研究进展

Scope:

* trials
* trial phases
* human studies
* clinical endpoints
* no clinical recommendation

## T08.03 Expert Viewpoints 专家观点

Scope:

* expert interviews
* expert blogs
* debates
* hypothesis
* not consensus by default

## T08.04 Product Development Progress 产品研发进展

Scope:

* diagnostics and biomarkers
* AI and software services
* devices and wearables
* testing products
* longevity drugs as progress only
* commercialization status

## T08.05 Regulatory and Commercialization Status 监管与商业化状态

Scope:

* approvals
* restrictions
* market availability
* China availability
* global comparison
* no promotion

## T08.06 Watchlist 观察清单

Scope:

* future candidates
* emerging topics
* not actionable
* education-only until reviewed

---

# T09 Education, Experts, Sources and Governance 教育、专家、信源与治理

## T09.00 Scope

This topic organizes education materials, expert/source context, source library, and governance rules.

Default information layer:

```text
education
```

Allowed content types:

```text
education_article
glossary_entry
checklist
clinician_conversation_preparation
source_note
evidence_summary
governance_rule
curation_rule
safety_boundary
```

## T09.01 Glossary 术语表

Scope:

* healthspan terms
* biomarker terms
* body system terms
* evidence terms
* action resource terms

## T09.02 User Guides 用户指南

Scope:

* how to use Congtie
* how to upload reports
* how to ask questions
* how to interpret missing context
* how to understand safety boundaries

## T09.03 Checklists 清单

Scope:

* report upload checklist
* missing context checklist
* doctor conversation checklist
* sleep log checklist
* exercise log checklist
* nutrition log checklist

## T09.04 Clinician Consultation Preparation 就诊准备

Scope:

* question preparation for doctor visits
* report organization before consultation
* communication checklists
* specialist referral preparation
* safe question prompts
* no diagnosis
* no treatment plan

## T09.05 Experts 专家

Scope:

* expert profiles
* expert viewpoints
* source context
* conflict of interest notes
* not authority by default

## T09.06 Source Library 信源库

Scope:

* source metadata
* source quality
* source priority
* source type
* China-first source policy
* source notes

## T09.07 Evidence Grading 证据分级

Scope:

* evidence_level
* evidence_posture
* source_type
* source_priority
* commercial claim handling
* invalid / harmful classification

Use E0-E5 and EX as defined in Evidence Grading Framework.

## T09.08 Invalid, Harmful and Overhyped Information 无效、有害与夸大信息

Scope:

* invalid claims
* harmful claims
* outdated information
* commercial exaggeration
* unsafe practices
* refutes / deprecates links

## T09.09 Curation and Governance Rules 内容治理规则

Default information layer:

```text
governance
```

Scope:

* curation rules
* commercial boundary rules
* safety boundary rules
* review and approval workflow
* versioning
* deprecation
* runtime permission rules
* source update workflow
* human approval gate

## T09.10 User Interaction and Onboarding 用户交互与入门引导

Scope:

* how to talk to Congtie
* how to provide context
* how to upload and describe reports
* how to respond to missing context prompts
* how to understand safety interruption
* how to provide feedback
* how to use generated checklists

## T09.11 Topic Mapping and Indexing 主题映射与索引

Scope:

* topic mapping seed
* knowledge entry mapping
* action resource mapping
* source mapping
* index generation
* retrieval tags
* mapping validation

---

# T10 Pet Longevity 宠物长寿

## T10.00 Status

Status:

```text
reserved
```

T10 is reserved for future versions.

In v0:

```text
runtime_enabled: false
retrieval_enabled: false
recommendation_enabled: false
context_construction_enabled: false
```

Pet longevity must not be used in v0 runtime.

## T10.01 Future Scope

Future possible scope:

* pet healthspan education
* pet nutrition
* pet veterinary preparation
* pet records
* pet aging research

Requires separate safety, veterinary, and content governance review.

---

## 8. Mapping Principles

### 8.1 Knowledge Seed Mapping

Knowledge Seed entries should map to:

```text
topic_id
information_layer
allowed_content_types
evidence_level
evidence_posture
clinical_boundary
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

### 8.2 Action Resource Mapping

Action Resources should map to:

```text
topic_id
information_layer: action_resource
resource_type
recommendation_permission
auto_trigger_allowed
source_enrichment_status
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

### 8.3 Progress and Viewpoints Mapping

Progress and viewpoints entries should map to both:

```text
domain topic
+
information_layer: progress_and_viewpoints
```

Example:

```text
A new CGM study:
topic_id: T07.02 or T04.08
information_layer: progress_and_viewpoints
```

### 8.4 Governance Mapping

Governance documents map to:

```text
T09.09 Curation and Governance Rules
```

Examples:

```text
evidence_grading_framework.v0.1.md → T09.07 / T09.09
action_resource_curation_rules.v0.2.md → T09.09
proactive_action_boundary.v0.1.md → T09.09
user_health_information_library_spec.v0.1.md → T01.06 / T04.12 / T09.09
```

---

## 9. Topic Mapping Seed Fields

A future `topic_mapping_seed.v0.1.json` should include:

```json
{
  "entry_id": "",
  "entry_type": "",
  "topic_id": "",
  "topic_path": "",
  "information_layer": "",
  "allowed_content_types": [],
  "evidence_level": "",
  "evidence_posture": "",
  "source_type": [],
  "permission_level": "",
  "recommendation_permission": "",
  "auto_trigger_allowed": false,
  "is_clinical_sensitive": false,
  "actionability_status": "",
  "clinical_boundary": "",
  "related_knowledge_ids": [],
  "related_resource_ids": [],
  "related_source_ids": [],
  "notes": ""
}
```

Required for action resources:

```json
{
  "resource_type": "",
  "commercial_boundary_level": "",
  "privacy_risk": "",
  "china_availability": "",
  "regulatory_status": ""
}
```

Required for progress and viewpoints:

```json
{
  "research_stage": "",
  "regulatory_status": "",
  "commercialization_status": "",
  "actionability_status": ""
}
```

---

## 10. Clinical Sensitivity Rules

Any topic or entry involving the following should set:

```yaml
is_clinical_sensitive: true
```

Examples:

* disease topics
* medication
* dosage
* emergency symptoms
* clinical testing
* disease screening
* high-risk interventions
* hormones
* peptides
* invasive procedures
* off-label drugs
* supplement protocol
* clinical imaging
* disease risk calculation
* system scoring

When `is_clinical_sensitive: true`, runtime should apply stricter safety boundaries.

---

## 11. Permission Rules

Action resources must use:

```text
R0 = prohibited from automatic recommendation
R1 = user-initiated explanation only
R2 = information-completion option
R3 = low-risk general tool option
```

Default examples:

```text
R0: medications, off-label drugs, hormones, peptides, experimental interventions
R1: supplements, nutrition products, protocol notes involving supplements
R2: devices, testing services, optional measurement resources
R3: logs, checklists, original report preservation, low-risk tracking tools
```

Permission level does not replace clinical safety.

A resource may require stricter boundary even if evidence is strong.

---

## 12. Evidence Rules

Use evidence fields:

```yaml
evidence_level:
evidence_posture:
source_type:
```

Evidence levels:

```text
E1 authority guideline
E2 high-quality review or RCT
E3 observational or consensus
E4 early research
E5 expert opinion or hypothesis
E0 commercial or anecdotal
EX disproven or harmful
```

A higher evidence level allows clearer explanation.

It does not automatically permit stronger intervention.

---

## 13. v0 Non-goals

Congtie v0 taxonomy must not enable:

* diagnosis
* treatment
* medication advice
* dosage advice
* clinical recommendation
* system scoring
* disease risk calculation
* disease prediction
* personalized supplement protocol
* personalized medical intervention
* emergency triage engine
* product marketplace
* hidden commercial conversion
* automatic publication without human review
* private user data storage inside the public knowledge taxonomy

---

## 14. Acceptance Criteria

This taxonomy is acceptable when:

* It defines a stable topic map for the Longevity Information Library.
* It aligns with the architecture document’s five information layers.
* It defines the user goal/result and Congtie mission as “extend healthspan.”
* It separates longevity goal from longevity strategy.
* It places “avoid premature mortality / maintain capability / slow biological aging” under strategy.
* It uses `Progress and Viewpoints / 进展与观点`.
* It uses `progress_and_viewpoints` as internal label.
* It clarifies that progress and viewpoints can be cross-topic information-layer entries.
* It clarifies that 用户健康信息库 is separate from the general taxonomy.
* It includes App as a human access method.
* It defines topic metadata fields including `information_layer`.
* It defines actionability status for progress and viewpoints.
* It includes governance and curation rules as a topic.
* It includes clinician consultation preparation as a topic.
* It includes nutrition_category requirement for nutrition and supplement entries.
* It preserves R0/R1/R2/R3 permissions.
* It preserves v0 non-clinical boundaries.
* It keeps Pet Longevity disabled in v0 runtime.
* It uses `Congtie` as display name.
* It uses `congtie` only in lowercase/code/domain contexts.
* It does not use the deprecated camel-case spelling.

---

## 15. Final Note

The taxonomy should help Congtie become a proactive longevity agent without becoming a clinical system.

The safest v0 principle is:

```text
Map the knowledge clearly.
Separate general information from private user data.
Use layers and topics together.
Be proactive about safe explanation and context completion.
Stay strict about clinical boundaries.
Keep all action resources permission-controlled.
```
