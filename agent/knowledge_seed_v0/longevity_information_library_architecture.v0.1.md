# Longevity Information Library Architecture v0.1

Version: v0.1  
Project: Congtie  
Status: Draft  
Owner: Congtie Agent Team  
Last Updated: 2026-05-19

---

## 1. Purpose

This document defines the overall architecture of the Congtie Longevity Information Library for v0.

The Longevity Information Library is the general information foundation that supports Congtie as a proactive longevity agent.

It is designed to help Congtie provide:

- trustworthy explanations
- missing-context clarification
- low-risk next action rationale
- safe action resource suggestions
- progress and viewpoint tracking
- user education
- preparation for professional consultation
- future agent-to-agent collaboration

This document sits above Knowledge Seed v0.

Knowledge Seed v0 is the smallest safe subset of the Longevity Information Library used for M5/M6 internal testing.

This document does not create runtime implementation, loader behavior, schema validation, tests, API contracts, JSON index, or topic files.

---

## 2. One-line Definition

The Congtie Longevity Information Library is the structured, evidence-aware, agent-readable information base organized around the mission of helping users extend healthspan.

It works together with:

```text
model
+ harness
+ longevity information library
+ user health information library
= personalized explanation and safe action support
```

The library is not a diagnostic engine.

The library is not a treatment engine.

The library is not a medication engine.

The library is not a supplement protocol engine.

The library is not a product marketplace.

The library is an information and action-support foundation for a proactive longevity agent.

---

## 3. Relationship Between Major Concepts

### 3.1 Longevity Information Library

The Longevity Information Library is the broad, long-term information asset.

It contains general, reusable, versioned information.

It may include:

- stable knowledge
- invalid or harmful information
- action resources
- progress and viewpoints
- education materials
- evidence summaries
- source metadata
- curation rules
- safety boundaries

It should be organized for both human review and LLM/agent use.

### 3.2 Knowledge Seed v0

Knowledge Seed v0 is the minimum safe subset of the Longevity Information Library.

It supports M5/M6 internal testing.

It includes:

- product role explanations
- system basic explanations
- missing context explanations
- next action rationale
- safety boundaries
- restricted action resources

Knowledge Seed v0 is intentionally small, conservative, and non-clinical.

### 3.3 Action Resources

Action resources are a restricted subset of the Longevity Information Library.

They include:

- products
- services
- devices
- testing services
- lifestyle tools
- nutrition products
- supplements
- information resources
- education resources

Action resources are permission-controlled.

They are not automatic recommendations.

They are not prescriptions.

They are not clinical instructions.

They are not hidden commercial conversion objects.

### 3.4 用户健康信息库

用户健康信息库 is the user-facing Chinese term for the user’s private health information store.

It is separate from the general Longevity Information Library.

The Longevity Information Library contains general information.

The 用户健康信息库 contains private user-specific information.

Examples:

- biomarkers
- body system states
- lab reports
- medical records
- genetic information
- lifestyle records
- user goals and intentions
- existing interventions
- action history
- product or service usage history
- user consent and authorization state

The 用户健康信息库 should be user-controlled, private, exportable, deletable, and shareable only with explicit user permission.

---

## 4. Core Architecture

The v0 architecture should be understood as:

```text
Longevity Information Library
├── Knowledge Layer
│   ├── stable usable knowledge
│   ├── invalid or harmful knowledge
│   └── body system and biomarker knowledge
├── Action Resource Layer
│   ├── products
│   ├── services
│   ├── devices
│   ├── testing services
│   ├── lifestyle tools
│   ├── nutrition products
│   └── supplements
├── Progress and Viewpoints Layer
│   ├── research progress
│   ├── clinical research progress
│   ├── product development progress
│   ├── expert viewpoints
│   └── regulatory or commercialization status
├── Education Layer
│   ├── explainers
│   ├── guides
│   ├── checklists
│   └── clinician conversation preparation materials
└── Governance Layer
    ├── evidence grading
    ├── source rules
    ├── curation rules
    ├── safety boundaries
    ├── commercial boundaries
    └── review and approval workflow
```

The 用户健康信息库 is adjacent to this structure, not inside the general Longevity Information Library.

```text
Longevity Information Library   +   用户健康信息库
general information                 private user context
versioned knowledge                  user-controlled data
reviewed sources                     personal records
agent-readable                       consent-gated
```

---

## 5. Information Layers

## 5.1 Knowledge Layer

The Knowledge Layer contains relatively stable information that can support trustworthy explanation.

It may include:

- healthspan definitions
- body system concepts
- biomarker definitions
- measurement context
- lifestyle intervention concepts
- widely accepted safety information
- guideline-adjacent education
- invalid or harmful information
- outdated or superseded information

Knowledge entries must include:

- source information
- evidence level
- evidence posture
- last reviewed date
- safety boundary
- allowed use
- disallowed use

The Knowledge Layer must not directly generate:

- diagnosis
- treatment
- medication advice
- dosage advice
- clinical recommendation
- disease risk calculation
- system scoring
- disease prediction
- personalized supplement protocol

---

## 5.2 Invalid or Harmful Information

The library should explicitly track information that is invalid, harmful, outdated, exaggerated, or not suitable for use.

This is important because users may ask about trending claims, old advice, pseudoscience, aggressive anti-aging methods, or commercial claims.

This layer may include:

- disproven claims
- outdated guidance
- unsafe practices
- pseudoscience
- exaggerated commercial claims
- unsupported anti-aging claims
- deprecated product or service claims

Recommended internal category:

```text
invalid_or_harmful_information
```

Allowed use:

- explain why a claim should not be relied on
- warn about weak evidence
- explain that a claim is outdated or unsupported
- prevent unsafe action

Disallowed use:

- repeat harmful claims as advice
- promote disproven interventions
- present unsupported claims as evidence
- use outdated information for action suggestions

---

## 5.3 Action Resource Layer

The Action Resource Layer contains products, services, tools, devices, testing services, nutrition products, supplements, information resources, and education resources that may support safe action.

Action resources may support:

- information completion
- self-tracking
- record keeping
- lifestyle execution
- user education
- preparation for professional consultation

Action resources are governed by:

```text
R0 / R1 / R2 / R3
```

Permission levels:

```text
R0 = prohibited from automatic recommendation
R1 = user-initiated explanation only
R2 = information-completion option
R3 = low-risk general tool option
```

Action resources must follow:

- non-clinical boundary
- commercial transparency
- manual review
- evidence-aware wording
- permission-controlled runtime behavior

Action resources must not become:

- hidden diagnosis
- hidden treatment
- hidden supplement protocol
- hidden product push
- hidden commercial conversion

---

## 5.4 Progress and Viewpoints Layer

研究进展、专家观点、产品研发进展等信息，在 v0 中统一称为：

```text
进展与观点
```

English internal label:

```text
progress_and_viewpoints
```

This layer contains information that is relevant to longevity but is not yet stable usable knowledge.

Examples:

- early academic research
- clinical trial progress
- expert views
- product development progress
- regulatory progress
- expected commercialization timeline
- debate around a new intervention
- early claims that require further validation

This layer is important because users care about what is emerging in longevity science.

However, progress and viewpoints must not be treated as stable knowledge.

Allowed use:

- explain what is being studied
- explain what is not yet proven
- summarize expert viewpoints
- track product development status
- track regulatory or commercialization status
- help users understand why something is not yet actionable

Disallowed use:

- treat early progress as established fact
- recommend action based on early research alone
- provide treatment or supplement protocols
- claim expected commercial timelines as certainty
- present expert opinion as consensus
- use progress as clinical advice

Every progress and viewpoint entry should include:

```text
research_stage
evidence_level
source_type
supporting_viewpoints
opposing_or_cautionary_viewpoints
regulatory_status
commercialization_status
actionability_status
last_reviewed
next_review_date
```

Recommended `actionability_status` values:

```text
not_actionable
education_only
watchlist
requires_professional_context
future_candidate
deprecated
```

---

## 5.5 Education Layer

The Education Layer contains user-facing learning materials.

Examples:

- glossary
- body system explainers
- biomarker explainers
- user guides
- checklists
- clinician conversation preparation sheets
- how-to-read-a-lab-report guides
- safe question prompts

Allowed use:

- explain concepts
- reduce confusion
- help user prepare questions
- help user understand missing context
- help user act safely

Disallowed use:

- diagnosis
- treatment
- dosage
- clinical decision
- disease risk calculation
- personalized supplement protocol

---

## 5.6 Governance Layer

The Governance Layer contains the rules that control how information is collected, reviewed, stored, updated, and used.

It includes:

- evidence grading framework
- source rules
- action resource curation rules
- safety boundary rules
- commercial boundary rules
- manual review workflow
- versioning rules
- deprecation rules
- runtime permission rules

Existing v0 governance documents include:

```text
knowledge_seed_scope.v0.1.md
knowledge_seed_content_template.v0.1.md
knowledge_seed_topic_plan.v0.1.md
topics_p0_seed_entries.v0.1.md
action_resource_curation_rules.v0.1.md
```

Future governance documents may include:

```text
evidence_grading_framework.v0.1.md
proactive_action_boundary.v0.1.md
user_health_information_library_spec.v0.1.md
longevity_information_curation_rules.v0.1.md
```

---

## 6. Evidence Grading

The Longevity Information Library should use both `evidence_posture` and `evidence_level`.

### 6.1 evidence_posture

`evidence_posture` describes the posture or nature of the information.

Allowed values may include:

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

### 6.2 evidence_level

`evidence_level` describes the strength and maturity of the evidence.

Recommended values:

| Level | Label | Meaning |
|---|---|---|
| E1 | authority_guideline | Chinese official guideline, international guideline, authority consensus |
| E2 | high_quality_review_or_rct | High-quality systematic review, meta-analysis, or RCT |
| E3 | observational_or_consensus | Observational study, real-world evidence, expert consensus |
| E4 | early_research | Early clinical research, animal study, mechanistic study |
| E5 | expert_opinion_or_hypothesis | Expert opinion, hypothesis, trend interpretation |
| E0 | commercial_or_anecdotal | Commercial claim, user review, anecdote, unverified claim |
| EX | disproven_or_harmful | Disproven, harmful, outdated, or not recommended |

### 6.3 China-first Source Priority

For Chinese users, source priority should generally be:

```text
Chinese official and professional sources
→ international authority sources
→ peer-reviewed literature
→ professional education sources
→ official product or service documentation
→ founder-curated notes
→ commercial or user-generated sources
```

Commercial sources should not be treated as verified evidence by default.

---

## 7. Source Types

Recommended `source_type` values:

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
commercial_claim_unverified
```

Multiple source types may apply.

---

## 8. Relationship to Examine.com and Similar Sources

Supplement and nutrition information may be manually curated first from high-quality sources such as Examine.com and other reviewed sources.

In v0:

- founder-led manual curation is acceptable
- AI may assist summarization and structuring
- sources must be recorded
- claims should be rewritten conservatively
- evidence level should be assigned
- manual review is required before runtime use

CLI, MCP, API, or automated source integrations may be added in future versions.

v0 should not depend on automated source ingestion.

Recommended v0 principle:

```text
Manual curation first.
AI drafting second.
Automated source ingestion later.
Runtime automation last.
```

---

## 9. Nutrition and Supplement Classification

Nutrition-related resources should be more granular than the generic `nutrition_product` category.

Recommended optional field:

```text
nutrition_category
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

### 9.1 General Nutrition

General nutrition information may include:

- food
- meal pattern
- protein intake context
- fiber intake context
- hydration
- dietary logs
- meal planning education

### 9.2 Nutrition Products

Nutrition products may include:

- protein powder
- protein snack
- meal replacement
- functional beverage
- electrolyte product
- fiber food product

Default permission:

```text
R1
```

unless the product is a low-risk general food or record-keeping tool.

### 9.3 Supplements

Supplements include:

- creatine
- omega-3
- vitamin D
- magnesium
- probiotics
- fiber supplements
- other dietary supplements

Default permission:

```text
R1
auto_trigger_allowed: false
```

### 9.4 Longevity Supplements

Longevity supplements are supplements commonly discussed in relation to maintaining capacity, healthy aging, or biological aging.

Examples may include:

- NMN
- NR
- spermidine
- creatine
- omega-3
- vitamin D
- magnesium
- other emerging supplements

Some substances discussed in longevity contexts may be prescription drugs, off-label drugs, or experimental interventions.

Those must not be treated as supplements.

Examples that should remain excluded from v0 action recommendation:

- rapamycin
- metformin
- GLP-1 medications
- hormone interventions
- peptide protocols
- prescription-only substances
- experimental or invasive interventions

---

## 10. Supplement Boundary in v0

Congtie v0 does not provide personalized supplement protocols.

This includes:

- no personalized supplement recommendation
- no personalized dosage
- no timing
- no cycle
- no stack
- no protocol
- no lab-based supplement prescription
- no disease-specific supplement plan

v0 may allow:

- user-initiated explanation
- general description
- source-based evidence summary
- evidence level
- safety notes
- known caution areas
- common contexts in which people ask about it
- manually curated references

v0 may include a field such as:

```text
common_dosages_in_literature
```

But this field is not a user-specific recommendation.

If included, it must be handled as reference information only and must not be surfaced as a personalized instruction.

Recommended required flag:

```text
not_for_personalized_protocol: true
```

Safe user-facing wording:

```text
以下内容是公开资料中常见讨论的信息，不构成个体化建议，也不是剂量建议或医疗建议。葱铁 v0 不根据你的个人健康数据生成补充剂方案。是否使用以及如何使用，需要结合你的完整健康状况和专业建议。
```

---

## 11. Proactive Longevity Agent Boundary

Congtie v0 should be an early proactive longevity agent.

It should not be only a passive explainer.

However, v0 proactive behavior must be permission-controlled and safety-bounded.

### 11.1 v0 May Proactively Provide

Congtie v0 may proactively provide:

- missing context reminders
- information completion suggestions
- original report preservation suggestions
- low-risk lifestyle tracking suggestions
- sleep / nutrition / exercise / stress record suggestions
- optional measurement resource suggestions
- clinician conversation preparation
- explanation of why a next action matters
- optional non-affiliate product or service links, if approved and safe
- task preparation outputs such as checklists, comparison tables, or question lists

### 11.2 v0 Must Not Proactively Provide

Congtie v0 must not proactively provide:

- diagnosis
- treatment
- medication advice
- dosage advice
- clinical recommendation
- system scoring
- disease risk calculation
- disease prediction
- personalized supplement protocol
- personalized medical intervention
- high-risk intervention recommendation
- emergency-care replacement
- hidden commercial conversion

### 11.3 Future Versions

Future versions may add more personalized capability after:

- stronger user health information library
- better safety context
- medication and contraindication handling
- clinician review workflows
- legal and compliance review
- explicit user consent
- runtime audit trail
- stronger evidence governance
- user feedback from v0

For v0, user feedback should be collected to understand whether users need more specific nutrition, supplement, product, service, and task-execution support.

---

## 12. Product and Service Links

Congtie v0 may include product or service links only under strict boundaries.

Allowed:

- official links
- non-affiliate links
- transparent commercial status
- optional resource framing
- context-completion framing
- user education framing
- founder-curated note when applicable

Disallowed:

- hidden commission
- affiliate-style ranking
- pressure to buy
- “best for you”
- “must buy”
- “medically necessary”
- “treats disease”
- “prevents disease”
- “replaces clinician judgment”
- “guaranteed result”

Default commercial rule:

```text
zero_commission_v0
```

Safe user-facing wording:

```text
这是一个可选资源链接，用于帮助你进一步了解或补全信息。葱铁 v0 默认不收取商品佣金，也不把购买行为作为健康必须项。
```

---

## 13. 用户健康信息库

用户健康信息库 is the private user-specific information layer that supports personalization.

It is not the same as the general Longevity Information Library.

Recommended content categories:

```text
biomarkers
body_system_states
lab_reports
medical_records
genetic_information
lifestyle_records
sleep_records
exercise_records
nutrition_records
stress_records
user_goals
user_intentions
user_questions
existing_interventions
product_service_usage_history
action_history
consent_records
sharing_permissions
export_history
deletion_requests
```

Core principles:

- user-controlled
- private
- exportable
- deletable
- shareable only with explicit permission
- permission-gated for agent-to-agent collaboration
- not used for hidden commercial targeting
- not used for hidden medical personalization
- auditable over time

v0 does not need a full implementation of 用户健康信息库.

However, v0 should define the concept early because it is essential for future personalization.

---

## 14. User Data and General Information Separation

The system must keep a clear conceptual separation:

| Layer | Nature | Example |
|---|---|---|
| Longevity Information Library | General information | biomarker concept, supplement evidence summary, action resource rules |
| 用户健康信息库 | User-specific private context | user’s ApoB value, sleep record, lab report, supplement use history |
| Runtime Agent Reasoning | Temporary task context | current question, selected context, safety state |
| Output | User-facing response | explanation, next action, checklist, boundary message |

The model may combine general information and user context only within approved runtime boundaries.

The system must not silently turn general information into personalized medical advice.

---

## 15. Editing and Curation Interface

v0 should not build a custom backend editing system yet.

Recommended v0 curation interface:

```text
Feishu table / Feishu base
+ Feishu document
+ Markdown files in Git
+ manual review
+ local validation scripts later
```

Recommended future path:

```text
v0: Feishu as pseudo-admin
v0.3/v0.5: add scripts, validators, import/export helpers
v1: consider web admin if entries exceed operational threshold
```

Possible threshold for custom admin:

```text
> 200 reviewed entries
or repeated multi-person review workflow
or frequent source update operations
or runtime publishing queue needed
```

---

## 16. Recommended Feishu Structure

For general entries, Feishu table fields may include:

```text
entry_id
title_zh
title_en
information_layer
category
evidence_level
evidence_posture
source_type
source_urls
summary
user_visible_explanation
allowed_use
disallowed_use
safety_boundary
commercial_boundary
related_body_systems
related_lifestyle_keywords
china_availability
regulatory_status
curation_status
reviewer
review_date
next_review_date
approval_status
approval_note
```

For action resources, use the fields defined in:

```text
action_resource_curation_rules.v0.1.md
```

For supplements and nutrition information, add:

```text
nutrition_category
common_use_context
common_dosages_in_literature
safety_notes
known_interactions
not_for_personalized_protocol
```

---

## 17. Runtime Use Principles

Runtime should use the Longevity Information Library according to information layer and permission.

### 17.1 Knowledge Layer

May be used for:

- explanation
- education
- missing context clarification
- safety boundary

Must not be used for:

- diagnosis
- treatment
- clinical decision
- risk calculation
- system scoring

### 17.2 Action Resource Layer

May be used according to R0/R1/R2/R3 permission.

R0:

```text
Do not recommend. Explain boundary only.
```

R1:

```text
Explain only when user asks. Do not auto-trigger.
```

R2:

```text
May present as optional information-completion support.
```

R3:

```text
May present as low-risk general action support.
```

### 17.3 Progress and Viewpoints Layer

May be used for:

- education
- frontier awareness
- explaining uncertainty
- watchlist discussion

Must not be used for:

- direct action recommendation
- treatment
- supplement protocol
- clinical decision

### 17.4 用户健康信息库

May be used only with user permission and runtime safety controls.

Must not be used for:

- hidden commercial targeting
- hidden medical advice
- unsupported diagnosis
- unauthorized agent-to-agent sharing

---

## 18. v0 Personalization Boundary

Congtie v0 may personalize:

- what context is missing
- which records are relevant
- which low-risk next action is most useful
- which lifestyle dimension to track
- which optional information-completion resource may be relevant
- which questions to prepare for a clinician
- which source-backed educational explanation to show

Congtie v0 must not personalize:

- diagnosis
- treatment
- medication
- dosage
- supplement protocol
- disease risk score
- system score
- clinical testing requirement
- disease prediction
- high-risk intervention

This boundary should be reviewed after v0 user feedback.

---

## 19. v0 User Feedback Loop

Because v0 does not provide personalized supplement protocols, it should collect user feedback on whether users need more specific support in future versions.

Possible feedback questions:

```text
Was this explanation useful?
Was the next action concrete enough?
Did you want a more specific product or service option?
Did you want supplement information?
Did you expect dosage or protocol-level detail?
Did you understand why Congtie v0 cannot provide that yet?
Would you like a clinician-facing question list instead?
```

Feedback should inform future versions, not override v0 safety boundaries.

---

## 20. Future Automation Direction

Future automation may include:

- source whitelist
- source monitoring
- AI-assisted extraction
- CLI-based source collection
- MCP-based source tools
- API-based evidence retrieval
- duplicate detection
- claim detection
- evidence grading
- commercial language detection
- human review queue
- versioned publishing
- runtime permission enforcement

v0 should remain manual-first.

Recommended principle:

```text
Manual curation first.
AI-assisted drafting second.
Automated ingestion later.
Runtime automation last.
```

---

## 21. Relationship to Future CLI / MCP / API Work

For v0, supplement and nutrition information may be manually curated from reviewed high-quality sources.

Future versions may use:

- CLI workflows
- MCP tools
- APIs
- scheduled source monitoring
- structured source extraction
- evidence update checks

However, automated ingestion must not bypass human review.

Future automation should preserve:

- evidence level
- source traceability
- safety boundary
- commercial transparency
- version history
- manual approval
- runtime permission controls

---

## 22. Non-goals

The Longevity Information Library v0 does not aim to:

- build a complete medical knowledge base
- build a complete clinical decision support system
- build a treatment engine
- build a medication engine
- build a supplement protocol engine
- build a product marketplace
- build a disease risk calculator
- build a system scoring engine
- build a biological age calculator
- build an emergency triage system
- build a custom admin backend
- replace professional medical care
- publish automatically without human review

---

## 23. Acceptance Criteria

This architecture document is acceptable when:

- It defines the Longevity Information Library.
- It clarifies that Knowledge Seed v0 is the minimum subset.
- It defines Knowledge Layer, Action Resource Layer, Progress and Viewpoints Layer, Education Layer, and Governance Layer.
- It uses “进展与观点” for research progress, expert viewpoints, and product development progress.
- It defines 用户健康信息库 as the user-facing Chinese term for user health context.
- It separates general information from private user information.
- It defines evidence_level in addition to evidence_posture.
- It preserves action resource permission levels R0/R1/R2/R3.
- It preserves the v0 non-clinical boundary.
- It states that v0 does not provide personalized supplement protocols.
- It allows manual curation of supplement and nutrition information from high-quality sources such as Examine.com.
- It defers CLI/MCP/API source ingestion to future versions.
- It defines proactive longevity agent boundaries.
- It supports v0 user feedback collection for future personalization.
- It uses `Congtie` as display name.
- It uses `congtie` only in lowercase/code/domain contexts.
- It does not use `CongTie` as the default project spelling.

---

## 24. Final Note

Congtie v0 should be an early proactive longevity agent.

It should actively help users understand what is missing, why it matters, and what safe next action can move them forward.

However, v0 must remain clear about its boundary.

The safest v0 principle is:

```text
Be proactive about explanation.
Be proactive about context completion.
Be proactive about low-risk action support.
Be cautious about supplements.
Be strict about clinical boundaries.
Be transparent about evidence and commerce.
Use user feedback to guide future personalization.
```
