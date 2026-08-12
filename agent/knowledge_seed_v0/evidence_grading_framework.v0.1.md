# Evidence Grading Framework v0.1

Version: v0.1  
Project: Congtie  
Status: Draft  
Owner: Congtie Agent Team  
Last Updated: 2026-05-19

---

## 1. Purpose

This document defines the evidence grading framework for the Congtie Longevity Information Library and Knowledge Seed v0.

It provides a shared vocabulary for labeling:

- evidence strength
- evidence maturity
- source type
- source priority
- source reliability
- commercial claim risk
- progress and viewpoints status
- invalid or harmful information
- review and update status

This framework is designed for:

- human review
- AI-assisted drafting
- LLM/agent retrieval
- runtime permission control
- future source monitoring
- future CLI/MCP/API ingestion

This document is not a clinical guideline.

This document does not create diagnosis, treatment, medication advice, dosage advice, clinical recommendation, system scoring, disease risk calculation, disease prediction, personalized supplement protocol, or personalized medical intervention.

---

## 2. One-line Definition

The Evidence Grading Framework is the rule set that helps Congtie label how trustworthy, mature, actionable, and safe an information entry is.

It answers:

```text
Where does this information come from?
How strong is the evidence?
How mature is the evidence?
Is it stable knowledge or only 进展与观点?
Is it commercial or independent?
Can it support explanation?
Can it support action?
Can it be used proactively?
When should it be reviewed again?
```

Evidence grading helps Congtie explain better.

Evidence grading does not authorize clinical advice.

---

## 3. Relationship to Existing Documents

This framework supports and should be referenced by:

```text
agent/knowledge_seed_v0/longevity_information_library_architecture.v0.1.md
agent/knowledge_seed_v0/knowledge_seed_scope.v0.1.md
agent/knowledge_seed_v0/knowledge_seed_content_template.v0.1.md
agent/knowledge_seed_v0/knowledge_seed_topic_plan.v0.1.md
agent/knowledge_seed_v0/action_resource_curation_rules.v0.1.md
agent/knowledge_seed_v0/topics_p0_seed_entries.v0.1.md
```

Future documents may depend on it:

```text
agent/knowledge_seed_v0/action_resource_curation_rules.v0.2.md
agent/knowledge_seed_v0/proactive_action_boundary.v0.1.md
agent/knowledge_seed_v0/user_health_information_library_spec.v0.1.md
agent/knowledge_seed_v0/longevity_information_curation_rules.v0.1.md
```

---

## 4. Core Principle

Evidence level, source type, and evidence posture are not the same thing.

Congtie should track all three.

```text
evidence_level = strength and maturity of evidence
source_type = where the information comes from
evidence_posture = how Congtie should treat the information
```

Example:

```text
A supplement brand page may be an official_product_spec source,
but its evidence_level may still be E0 commercial_or_anecdotal
and its evidence_posture may be commercial_claim_unverified.
```

Another example:

```text
A Chinese official guideline may be source_type official_guideline_china,
evidence_level E1 authority_guideline,
and evidence_posture clinical_guideline_adjacent.
```

Evidence grading is not permission by itself.

Runtime behavior still depends on:

- information layer
- category
- action resource permission level
- safety boundary
- user context
- manual approval state
- whether safety_interruption is active

---

## 5. Evidence Level

Each entry should include:

```text
evidence_level
```

Recommended values:

| Level | Label | Meaning |
|---|---|---|
| E1 | authority_guideline | Chinese official guideline, international guideline, authority consensus |
| E2 | high_quality_review_or_rct | High-quality systematic review, meta-analysis, or randomized controlled trial |
| E3 | observational_or_consensus | Observational study, real-world evidence, expert consensus |
| E4 | early_research | Early clinical research, animal study, mechanistic study |
| E5 | expert_opinion_or_hypothesis | Expert opinion, hypothesis, informed viewpoint, trend interpretation |
| E0 | commercial_or_anecdotal | Commercial claim, user review, anecdote, influencer claim, unverified claim |
| EX | disproven_or_harmful | Disproven, harmful, outdated, unsafe, or not recommended |

---

## 6. Evidence Level Details

### 6.1 E1 — authority_guideline

Use E1 for the most stable and authoritative sources.

Examples:

- Chinese official guidelines
- Chinese professional society guidelines
- Chinese CDC / National Health Commission materials
- international authority guidelines
- WHO materials
- USPSTF guidance
- major professional association guidance
- highly authoritative consensus statements

Allowed use:

- stable explanation
- user education
- missing context explanation
- safety boundary explanation
- clinician conversation preparation

Disallowed use:

- direct diagnosis
- treatment decision
- medication advice
- dosage instruction
- clinical recommendation
- risk calculation unless a validated runtime risk engine is explicitly approved
- system scoring unless a separate approved scoring engine exists

Important:

Even E1 evidence does not allow Congtie v0 to provide diagnosis, treatment, medication, dosage, or clinical decisions.

---

### 6.2 E2 — high_quality_review_or_rct

Use E2 for high-quality research evidence.

Examples:

- systematic review
- meta-analysis
- randomized controlled trial
- high-quality clinical trial
- high-quality evidence synthesis

Allowed use:

- explanation
- evidence summary
- education
- general rationale
- user-initiated discussion
- action resource evidence context

Disallowed use:

- direct personalized medical advice
- personalized supplement protocol
- dosage instruction
- treatment plan
- disease risk prediction

Important:

E2 evidence may support why a topic is relevant, but does not automatically permit personalized action.

---

### 6.3 E3 — observational_or_consensus

Use E3 for moderate maturity evidence.

Examples:

- observational study
- cohort study
- real-world evidence
- expert consensus
- professional consensus
- repeated but non-randomized evidence

Allowed use:

- cautious explanation
- education
- context discussion
- reason for further tracking
- non-clinical action rationale

Disallowed use:

- strong recommendation
- personal protocol
- disease prediction
- clinical action
- causal certainty

Recommended language:

```text
相关资料提示……
一些研究或共识讨论……
这可以作为理解背景的一部分……
```

Avoid:

```text
证明……
确定……
一定……
可以直接用于……
```

---

### 6.4 E4 — early_research

Use E4 for early-stage evidence.

Examples:

- early clinical research
- small trial
- pilot study
- animal study
- cell study
- mechanistic study
- early biomarker research
- early product research

Allowed use:

- 进展与观点
- frontier awareness
- education
- watchlist
- explaining uncertainty
- preparing questions

Disallowed use:

- direct action recommendation
- personalized suggestion
- treatment
- supplement protocol
- disease prevention claim
- commercial claim support

Recommended language:

```text
这仍属于早期研究或机制探索。
目前还不足以作为个人行动建议。
可以作为前沿信息了解。
```

---

### 6.5 E5 — expert_opinion_or_hypothesis

Use E5 for expert viewpoints, hypotheses, predictions, or informed opinions.

Examples:

- expert interview
- expert blog
- conference viewpoint
- hypothesis paper
- informed trend interpretation
- future commercialization prediction

Allowed use:

- 进展与观点
- debate summary
- user education
- explaining uncertainty
- helping users understand different views

Disallowed use:

- consensus claim
- action recommendation
- personal intervention
- clinical recommendation
- product endorsement

Recommended language:

```text
这是专家观点或假说，不等同于已验证知识。
可以帮助理解当前讨论方向，但不应直接作为行动依据。
```

---

### 6.6 E0 — commercial_or_anecdotal

Use E0 for commercial, anecdotal, or unverified claims.

Examples:

- ecommerce claim
- brand marketing copy
- user review
- influencer claim
- forum discussion
- before/after story
- affiliate ranking
- paid advertorial
- media claim without primary source

Allowed use:

- discovery signal
- commercial claim audit
- user education about uncertainty
- explain why the claim should not be treated as evidence

Disallowed use:

- verified fact
- action recommendation
- evidence support
- treatment claim
- disease prevention claim
- product superiority claim

Recommended language:

```text
这是商业宣传或用户经验信息，不能直接视为已验证证据。
如果纳入，只能作为待核验信息或商业声明记录。
```

---

### 6.7 EX — disproven_or_harmful

Use EX for information that is false, harmful, outdated, unsafe, or no longer recommended.

Examples:

- disproven claim
- known harmful practice
- outdated guidance
- unsafe intervention
- pseudoscience
- aggressive anti-aging claim with safety risk
- deprecated product or service claim
- misinformation

Allowed use:

- warning
- boundary explanation
- misinformation correction
- safety education
- “why not” explanation

Disallowed use:

- action suggestion
- product recommendation
- lifestyle recommendation
- treatment recommendation
- positive evidence support

Recommended language:

```text
这类信息已被认为不可靠、过时或存在安全风险，葱铁 v0 不应将其作为行动依据。
```

---

## 7. Evidence Posture

Each entry should also include:

```text
evidence_posture
```

Allowed values:

```text
product_policy
safety_policy
general_consensus
clinical_guideline_adjacent
product_spec
user_manual
commercial_claim_unverified
founder_curated
progress_and_viewpoints
invalid_or_harmful
```

### 7.1 product_policy

Use for Congtie product definitions, role boundaries, user experience principles, or internal product choices.

Examples:

- Congtie is a longevity assistant, not a doctor.
- Knowledge Seed v0 supports explain why and missing context.
- v0 does not provide personalized supplement protocols.

### 7.2 safety_policy

Use for safety boundary entries.

Examples:

- no diagnosis
- no medication or dosage advice
- no emergency substitution
- no disease risk calculation
- no system scoring

### 7.3 general_consensus

Use for broad, low-controversy healthspan concepts.

Examples:

- sleep, nutrition, exercise, and stress are useful lifestyle context categories
- original reports preserve important metadata
- trends are often more informative than isolated records

### 7.4 clinical_guideline_adjacent

Use for information near clinical practice but not used as clinical advice.

Examples:

- guideline-adjacent education
- lab report interpretation context
- professional consultation preparation
- health measurement context

Important:

This posture does not allow Congtie v0 to provide clinical advice.

### 7.5 product_spec

Use for product or service specifications.

Examples:

- what a device measures
- what a service includes
- what data a wearable exports
- what a testing service report may contain

### 7.6 user_manual

Use for instructions from official user manuals.

Examples:

- how a device is used
- how data export works
- what setup is required

Do not turn user manual information into medical claims.

### 7.7 commercial_claim_unverified

Use for marketing or commercial claims that should not be repeated as verified fact.

Examples:

- brand benefit claims
- ecommerce listing claims
- paid advertorial claims
- influencer claims

### 7.8 founder_curated

Use for entries manually selected or summarized by the founder.

Founder curation is useful, but it should not replace source traceability.

Founder-curated entries should still include source notes, evidence level, and review status.

### 7.9 progress_and_viewpoints

Use for 进展与观点 entries.

Examples:

- research progress
- product development progress
- expert viewpoints
- regulatory progress
- commercialization status

### 7.10 invalid_or_harmful

Use for disproven, outdated, harmful, unsafe, or not recommended information.

This posture should usually pair with:

```text
evidence_level: EX
```

---

## 8. Source Type

Each entry should include:

```text
source_type
```

Recommended source types:

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

Multiple source types may apply.

---

## 9. Source Priority

For Congtie v0, source priority should generally follow this order.

```text
P1: Chinese official and professional sources
P2: international authority sources
P3: peer-reviewed literature
P4: professional education sources
P5: official product or service documentation
P6: founder-curated notes
P7: expert interviews, blogs, conference talks
P8: media articles
P9: commercial marketing, ecommerce listings, user reviews
P0: unknown or unverified sources
```

### 9.1 P1 — Chinese official and professional sources

Highest priority for Chinese users.

Examples:

- Chinese National Health Commission
- Chinese CDC
- Chinese Nutrition Society
- Chinese professional society guidelines
- Chinese official public health materials

Use for:

- China-first user explanation
- localization
- regulatory and availability context
- public health and nutrition baseline

### 9.2 P2 — International authority sources

Examples:

- WHO
- USPSTF
- FDA
- EMA
- NIH
- CDC
- major international professional associations

Use when Chinese sources are unavailable, incomplete, or need global comparison.

### 9.3 P3 — Peer-reviewed literature

Examples:

- systematic reviews
- meta-analyses
- RCTs
- cohort studies
- mechanistic studies

Use for evidence summaries and source-backed explanations.

### 9.4 P4 — Professional education sources

Examples:

- professional organization education pages
- university health education pages
- hospital education pages

Use cautiously for user education.

### 9.5 P5 — Official product or service documentation

Examples:

- official product spec
- official user manual
- official service description
- lab report sample documentation

Use for what a resource is and what it does, not as proof of health outcomes.

### 9.6 P6 — Founder-curated notes

Founder-curated notes may be used when manually reviewed.

They should not hide missing source evidence.

### 9.7 P7 — Expert interviews, blogs, and conference talks

Use mainly as 进展与观点.

Do not treat as consensus unless independently supported.

### 9.8 P8 — Media articles

Use for discovery and general context.

Do not treat as primary evidence.

### 9.9 P9 — Commercial, ecommerce, or user-generated sources

Use with caution.

Usually label as:

```text
evidence_level: E0
evidence_posture: commercial_claim_unverified
```

### 9.10 P0 — Unknown or unverified sources

Do not use for runtime output unless the entry is explicitly about uncertainty or source insufficiency.

---

## 10. China-first Source Policy

Because Congtie initially serves Chinese users, China-relevant sources should be prioritized when available.

China-first does not mean China-only.

Recommended rule:

```text
Use Chinese official/professional sources first when the topic involves Chinese user-facing health guidance, regulation, availability, or public health baseline.

Use international authority and peer-reviewed sources when Chinese sources are unavailable, outdated, incomplete, or when global evidence comparison is needed.
```

Every entry may include:

```text
china_relevance: high | medium | low | unknown
china_availability: available | partially_available | unavailable | unknown | not_applicable
china_regulatory_status: approved | regulated | restricted | uncertain | not_applicable | unknown
```

Do not make regulatory claims unless reviewed.

---

## 11. Progress and Viewpoints Evidence Rules

研究进展、专家观点、产品研发进展统一称为：

```text
进展与观点
```

English internal label:

```text
progress_and_viewpoints
```

Progress and viewpoints are not stable knowledge by default.

They should usually use:

```text
evidence_posture: progress_and_viewpoints
```

Possible evidence levels:

```text
E4 early_research
E5 expert_opinion_or_hypothesis
E0 commercial_or_anecdotal
```

Sometimes E2 or E3 may apply if a progress item is based on strong research, but actionability still needs separate review.

Required fields:

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

Recommended `research_stage` values:

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

Recommended `actionability_status` values:

```text
not_actionable
education_only
watchlist
requires_professional_context
future_candidate
deprecated
```

Allowed use:

- explain what is being studied
- explain uncertainty
- summarize expert viewpoints
- track product development progress
- track regulatory or commercialization status
- help users understand why something is not yet actionable

Disallowed use:

- direct action recommendation
- treatment recommendation
- supplement protocol
- clinical decision
- product endorsement
- disease risk claim

Safe wording:

```text
这属于进展与观点，不等同于已经稳定可用的知识。它可以帮助了解研究或产品进展，但不应直接作为个人行动依据。
```

---

## 12. Supplement and Nutrition Evidence Rules

Supplement and nutrition information may be manually curated first from high-quality reviewed sources such as Examine.com and other credible sources.

In v0:

- founder-led manual curation is acceptable
- AI may assist summarization and structuring
- sources must be recorded
- evidence level should be assigned
- claims should be rewritten conservatively
- commercial claims should not be treated as verified evidence
- manual review is required before runtime use
- CLI/MCP/API ingestion is deferred to future versions

### 12.1 Supplement Default Boundary

Supplements default to:

```text
recommendation_permission: R1
auto_trigger_allowed: false
not_for_personalized_protocol: true
```

v0 does not provide:

- personalized supplement recommendation
- personalized dosage
- timing
- cycle
- stack
- protocol
- lab-based supplement prescription
- disease-specific supplement plan

### 12.2 Evidence Fields for Supplement Entries

Recommended fields:

```text
evidence_level
evidence_posture
source_type
source_urls
common_use_context
common_dosages_in_literature
safety_notes
known_interactions
china_availability
china_regulatory_status
not_for_personalized_protocol
last_reviewed
next_review_date
```

### 12.3 Common Dosage Field Boundary

The field:

```text
common_dosages_in_literature
```

may be used as internal reference information.

It must not be surfaced as a personalized dosage recommendation.

Safe wording:

```text
以下内容是公开资料中常见讨论的信息，不构成个体化建议，也不是剂量建议或医疗建议。葱铁 v0 不根据你的个人健康数据生成补充剂方案。
```

---

## 13. Action Resource Evidence Rules

Action resources must include evidence metadata.

Required fields:

```text
evidence_level
evidence_posture
source_type
source_urls
source_summary
commercial_claim_risk
clinical_boundary_level
commercial_boundary_level
recommendation_permission
manual_review_status
```

Runtime behavior depends on both evidence and permission.

Example:

```text
A blood pressure monitor may have evidence_level E1/E2 for the importance of blood pressure measurement as a concept,
but the product itself may only have product_spec evidence for its features.
```

Therefore, separate:

```text
concept_evidence_level
resource_claim_evidence_level
product_spec_source_type
commercial_claim_risk
```

Recommended optional fields:

```text
concept_evidence_level
resource_claim_evidence_level
```

---

## 14. Commercial Claim Handling

Commercial claims must be handled conservatively.

Commercial sources may help discover a product or service.

Commercial claims must not be treated as evidence.

### 14.1 Commercial Claim Risk

Each product/service/resource entry may include:

```text
commercial_claim_risk
```

Allowed values:

```text
none
low
medium
high
unknown
```

### 14.2 Common High-risk Commercial Claims

Flag claims such as:

```text
最有效
最佳
医学级
临床证明
治疗
预防
逆转
抗衰老奇迹
显著降低风险
适合所有人
医生推荐
必买
替代医生
```

### 14.3 Safe Rewrite

Unsafe:

```text
该产品可以显著改善睡眠并降低疾病风险。
```

Safe:

```text
该产品声称可支持睡眠相关体验，但葱铁 v0 不把商业宣传作为已验证效果。若纳入，只能作为一般工具信息说明。
```

### 14.4 Product Links

Product or service links may be included only with transparent framing.

Default:

```text
commercial_boundary_level: zero_commission_v0
```

Safe wording:

```text
这是一个可选资源链接，用于帮助你进一步了解或补全信息。葱铁 v0 默认不收取商品佣金，也不把购买行为作为健康必须项。
```

---

## 15. Invalid or Harmful Information Rules

The Longevity Information Library should include invalid or harmful information when it helps users avoid unsafe or misleading action.

Use:

```text
evidence_level: EX
evidence_posture: invalid_or_harmful
```

Examples:

- disproven anti-aging claim
- unsafe supplement protocol
- outdated guidance
- commercial exaggeration
- pseudoscience
- harmful intervention
- misleading biological age claim
- unverified disease prevention claim

Allowed output:

- warning
- correction
- “why not” explanation
- safety boundary
- user education

Disallowed output:

- positive recommendation
- action plan
- purchase suggestion
- use as supporting evidence

Recommended fields:

```text
invalid_reason
harm_risk
superseded_by
deprecated_date
source_for_deprecation
```

---

## 16. Review Freshness and Update Rules

Every entry should include review metadata.

Required fields:

```text
last_reviewed
next_review_date
review_status
reviewer
```

Recommended `review_status` values:

```text
draft
needs_source_check
needs_safety_review
needs_commercial_review
reviewed
approved
rejected
deprecated
superseded
```

### 16.1 Review Frequency

Suggested default review frequency:

| Entry Type | Default Review Interval |
|---|---:|
| product policy | 6–12 months |
| safety policy | 3–6 months |
| stable knowledge E1 | 6–12 months |
| E2/E3 research summary | 6 months |
| 进展与观点 | 1–3 months |
| supplement entries | 3–6 months |
| action resources | 3–6 months |
| commercial product claims | 1–3 months |
| invalid or harmful information | 6–12 months |

### 16.2 Deprecated and Superseded

Use:

```text
deprecated: true | false
superseded_by: entry_id | null
deprecated_reason:
deprecated_date:
```

An entry should be deprecated when:

- evidence changes
- guideline changes
- source is retracted
- product is unavailable
- regulatory status changes
- commercial claim is found misleading
- safety risk changes
- the entry conflicts with newer approved content

---

## 17. Minimum Metadata for All Entries

Every Longevity Information Library entry should include:

```yaml
entry_id:
version:
status:
title_zh:
title_en:
information_layer:
category:
evidence_level:
evidence_posture:
source_type:
source_urls:
source_summary:
last_reviewed:
next_review_date:
clinical_boundary_level: non_clinical
allowed_use:
disallowed_use:
requires_manual_review: true
```

---

## 18. Additional Metadata for Action Resources

Every action resource entry should additionally include:

```yaml
resource_type:
recommendation_permission:
recommendation_permission_label:
auto_trigger_allowed:
commercial_boundary_level:
commercial_claim_risk:
source_type:
evidence_level:
evidence_posture:
suitable_context:
not_suitable_context:
safety_note:
approval_status:
```

Optional but recommended:

```yaml
concept_evidence_level:
resource_claim_evidence_level:
china_availability:
china_regulatory_status:
privacy_risk:
commercial_risk:
```

---

## 19. Additional Metadata for Supplements and Nutrition

Supplement and nutrition entries should additionally include:

```yaml
nutrition_category:
common_use_context:
common_dosages_in_literature:
safety_notes:
known_interactions:
not_for_personalized_protocol: true
china_availability:
china_regulatory_status:
```

Important:

`common_dosages_in_literature` must not be surfaced as personalized dosage advice.

---

## 20. Additional Metadata for 进展与观点

Progress and viewpoints entries should include:

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

Recommended `actionability_status`:

```text
not_actionable
education_only
watchlist
requires_professional_context
future_candidate
deprecated
```

---

## 21. Manual Review Rules

No entry should be approved for runtime use without manual review.

Manual review should check:

- source existence
- source quality
- evidence level
- evidence posture
- safety boundary
- commercial boundary
- wording safety
- user-facing clarity
- permission level
- review freshness

For v0, founder review is acceptable.

Future versions may add multi-reviewer workflow.

---

## 22. AI-assisted Drafting Rules

AI may assist with:

- source summarization
- field extraction
- evidence level proposal
- source type proposal
- unsafe claim detection
- commercial claim detection
- draft rewriting
- duplicate detection
- update monitoring

AI must not:

- approve entries
- publish entries
- silently upgrade evidence level
- turn commercial claims into verified claims
- create personalized supplement protocols
- create diagnosis or treatment advice
- bypass human review

AI-generated drafts should be marked:

```yaml
drafted_by_ai: true
requires_manual_review: true
```

---

## 23. Runtime Use Rules

Evidence metadata should guide runtime use, but it does not replace safety rules.

### 23.1 E1/E2 Runtime Use

May support:

- explanation
- education
- missing context
- general rationale
- clinician conversation preparation

Must not automatically support:

- diagnosis
- treatment
- dosage
- clinical recommendation
- risk calculation
- system scoring

### 23.2 E3 Runtime Use

May support:

- cautious explanation
- trend discussion
- background context

Must use uncertainty language.

### 23.3 E4/E5 Runtime Use

Usually limited to:

- 进展与观点
- watchlist
- education
- uncertainty explanation

Must not support direct action suggestion.

### 23.4 E0 Runtime Use

Usually limited to:

- commercial claim audit
- uncertainty explanation
- “not verified” warning

Must not support recommendation.

### 23.5 EX Runtime Use

Used only for:

- warning
- correction
- safety boundary
- invalid/harmful explanation

---

## 24. Relationship to Proactive Agent Behavior

Congtie v0 should be proactive, but evidence level and permission must control how proactive it can be.

### 24.1 Proactive Allowed

v0 may proactively suggest:

- missing context completion
- original report preservation
- low-risk lifestyle tracking
- sleep / nutrition / exercise / stress records
- optional R2 information-completion resources
- R3 low-risk general tools
- clinician question preparation

### 24.2 Proactive Restricted

v0 should not proactively suggest:

- R1 supplements
- personalized supplement protocols
- dosage
- medication
- clinical testing as requirement
- high-risk interventions
- 进展与观点 as action plan
- E0 commercial resources as recommendation

### 24.3 Proactive Disallowed

v0 must not proactively provide:

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

---

## 25. Safe Language Patterns by Evidence Level

### 25.1 E1/E2

Allowed:

```text
权威资料/高质量研究支持……
较稳定的共识是……
可以作为一般理解依据……
```

Avoid:

```text
你应该……
你必须……
可以治疗……
可以预防……
```

### 25.2 E3

Allowed:

```text
一些研究或共识讨论……
可以作为背景信息……
仍需结合上下文……
```

Avoid:

```text
已经证明……
确定有效……
适合你……
```

### 25.3 E4/E5

Allowed:

```text
这属于进展与观点……
目前仍处于早期阶段……
不应直接作为个人行动依据……
```

Avoid:

```text
你可以尝试……
建议使用……
即将成为标准方案……
```

### 25.4 E0

Allowed:

```text
这是商业宣传或用户经验信息，不能直接视为已验证证据。
```

Avoid:

```text
该产品有效……
用户反馈证明……
最值得购买……
```

### 25.5 EX

Allowed:

```text
这类信息不应作为行动依据。
```

Avoid:

```text
可以作为替代方案……
仍可以尝试……
```

---

## 26. Feishu Table Fields

For evidence grading in Feishu, recommended columns:

| Column | Type | Example |
|---|---|---|
| entry_id | text | KS-RESOURCE-010 |
| title_zh | text | 肌酸 |
| information_layer | select | action_resource |
| category | select | supplement |
| evidence_level | select | E2 |
| evidence_posture | select | founder_curated |
| source_type | multi-select | peer_reviewed_meta_analysis |
| source_urls | URL / long text | reviewed links |
| source_summary | long text | evidence summary |
| source_priority | select | P3 |
| commercial_claim_risk | select | low |
| china_relevance | select | medium |
| china_availability | select | available |
| china_regulatory_status | select | unknown |
| actionability_status | select | education_only |
| review_status | select | draft |
| last_reviewed | date | 2026-05-19 |
| next_review_date | date | 2026-08-19 |
| reviewer | text | founder |
| approval_note | long text | notes |

---

## 27. Example: Supplement Evidence Entry

Example:

```text
Creatine
```

Possible metadata:

```yaml
entry_id: KS-RESOURCE-010
title_zh: 肌酸
information_layer: action_resource
category: supplement
resource_type: supplement
recommendation_permission: R1
auto_trigger_allowed: false
evidence_level: E2
evidence_posture: founder_curated
source_type:
  - peer_reviewed_meta_analysis
  - professional_education_page
  - founder_curated
commercial_claim_risk: medium
clinical_boundary_level: non_clinical
commercial_boundary_level: zero_commission_v0
not_for_personalized_protocol: true
common_dosages_in_literature: "Internal reference only; not user-facing personalized dosage."
review_status: draft
```

Safe user-facing boundary:

```text
肌酸可以作为一般信息了解。葱铁 v0 不根据个人健康数据判断你是否应该使用，也不提供剂量、周期或组合方案。是否使用应结合饮食、训练、健康背景和专业建议。
```

---

## 28. Example: Progress and Viewpoints Entry

Example:

```text
A new longevity intervention discussed in early research
```

Possible metadata:

```yaml
information_layer: progress_and_viewpoints
evidence_level: E4
evidence_posture: progress_and_viewpoints
source_type:
  - peer_reviewed_mechanistic
research_stage: early_research
actionability_status: education_only
regulatory_status: unknown
commercialization_status: not_available
```

Safe user-facing boundary:

```text
这属于进展与观点，不等同于稳定可用的知识。它可以帮助了解研究方向，但不应直接作为个人行动依据。
```

---

## 29. Example: Commercial Claim Entry

Example:

```text
A sleep product claims to improve sleep quality by 50%.
```

Possible metadata:

```yaml
evidence_level: E0
evidence_posture: commercial_claim_unverified
source_type:
  - commercial_marketing_page
commercial_claim_risk: high
actionability_status: not_actionable
```

Safe rewrite:

```text
该产品声称可支持睡眠相关体验，但葱铁 v0 不把商业宣传作为已验证效果。若纳入，只能作为一般工具信息说明。
```

---

## 30. Acceptance Criteria

This framework is acceptable when:

- It defines evidence_level.
- It defines evidence_posture.
- It defines source_type.
- It defines source_priority.
- It defines China-first source policy.
- It defines 进展与观点 evidence rules.
- It defines supplement and nutrition evidence rules.
- It defines action resource evidence rules.
- It defines commercial claim handling.
- It defines invalid or harmful information rules.
- It defines review freshness and update rules.
- It defines required metadata.
- It defines manual review rules.
- It defines AI-assisted drafting rules.
- It preserves the non-clinical boundary.
- It states that evidence level does not authorize clinical advice.
- It states that v0 does not provide personalized supplement protocols.
- It allows manual curation of supplement and nutrition information from high-quality sources such as Examine.com.
- It defers CLI/MCP/API ingestion to future versions.
- It uses `Congtie` as display name.
- It uses `congtie` only in lowercase/code/domain contexts.
- It does not use `CongTie` as the default project spelling.

---

## 31. Final Note

Evidence grading should make Congtie more trustworthy, not more aggressive.

A higher evidence level allows clearer explanation, but it does not automatically allow diagnosis, treatment, dosage, clinical recommendation, system scoring, disease risk calculation, disease prediction, or personalized supplement protocol.

The safest v0 principle is:

```text
Stronger evidence supports clearer explanation.
It does not automatically permit stronger intervention.
Evidence must work together with permission, safety, context, and human review.
```
