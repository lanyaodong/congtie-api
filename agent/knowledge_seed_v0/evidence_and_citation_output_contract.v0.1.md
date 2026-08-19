# Evidence and Citation Output Contract v0.1

Version: v0.1
Project: Congtie
Status: Founder Approved / Runtime Implementation Not Yet Authorized
Owner: Congtie Agent Team
Last Updated: 2026-08-19
Founder: 蓝耀栋
Founder Review Date: 2026-08-19

---

## 1. Purpose

This document defines the draft v0.1 product contract for how Congtie should connect substantive longevity answers to evidence, sources, uncertainty, safety boundaries, and, where applicable, user-authorized personal context.

The target traceability chain is:

```text
claim
-> evidence
-> source
-> applicability and uncertainty boundary
```

This document also records the Founder-approved Batch 001 B2-A seven-entry production baseline.

This document does not:

- modify the Knowledge Item Schema;
- modify the Evidence Grading Framework or evidence enums;
- create runtime, API, frontend, database, retrieval, or citation-rendering code;
- authorize diagnosis, treatment, medication, dosage, risk calculation, or a Personalized Longevity Protocol;
- add `KN-T0403-0002` to the Batch 001 Plan;
- create any B2 knowledge entry.

---

## 2. Relationship with Current Governance

This contract complements:

```text
agent/knowledge_seed_v0/evidence_grading_framework.v0.1.md
agent/longevity_knowledge_item_schema.v0.1.md
agent/longevity_knowledge_base/templates/longevity_knowledge_item_template.v0.1.md
agent/longevity_knowledge_base/schemas/evidence_source_type_enum.v0.1.md
agent/longevity_knowledge_base/schemas/evidence_source_type_alignment_notes.v0.1.md
```

The separate draft engineering document:

```text
agent/agent_evidence_closure_spec.v0.1.md
```

already sketches evidence identity, claim attachment, propagation, and runtime rendering concepts. Its existence does not mean those structures are present in the current Knowledge Item Schema or implemented in runtime. This contract defines the user-facing and knowledge-to-answer output expectations that future engineering work should align with.

---

## 3. Current Knowledge Capability Audit

Current canonical knowledge entries already support entry-level evidence governance through:

```yaml
evidence_level:
evidence_posture:
source_type:
source_urls:
source_notes:
last_source_check_date:
next_review_date:
allowed_use:
disallowed_use:
safety_boundary:
```

Current entry bodies also use `Evidence Boundary` or `Evidence and Source Notes`, plus `Safety Boundary` and `Agent Usage Notes`.

### 3.1 Current Capabilities

The current model can support:

- an entry-level evidence grade and posture;
- a reviewed list of source categories and URLs;
- prose explaining each source's role, limitations, and exclusions;
- source check and planned review dates;
- entry-level evidence and applicability boundaries;
- explicit allowed and disallowed use;
- separation of Founder/product policy from external medical evidence;
- manual human review before approval, publication, runtime, or retrieval use.

### 3.2 Current Limitations

The current Knowledge Item Schema does not reliably encode:

- claim-to-source mapping;
- a structured bibliography;
- source title, author, organization, journal, and publication date as separate fields;
- DOI or PMID as separate fields;
- claim-specific evidence level and scope;
- a structured `Supports / 本来源主要支持` field;
- a structured `Why This Source / 为什么引用` role;
- source verification status;
- user-data provenance and personal-context basis;
- retrieval timestamp and live-source freshness at answer time;
- answer-level citation rendering and citation-budget behavior.

These are governance and implementation gaps. They are not reasons to fabricate metadata or infer stronger evidence from existing entry-level fields.

---

## 4. Core Rule: Claim-Level Evidence

Congtie should attach evidence levels and sources to major claims or conclusions whenever practical.

A single answer may combine:

- E1 public-health or guideline claims;
- E2 systematic-review, meta-analysis, or RCT-supported claims;
- E3 observational or consensus claims;
- E5 Founder/product framework claims;
- user-specific inference based on authorized personal context;
- current information obtained through live retrieval.

One evidence level must not automatically be applied to the entire answer.

If a simplified interface shows one headline evidence grade, it must be labeled and interpreted as:

```text
主要结论证据等级
Headline evidence grade for the main conclusion
```

It is not a declaration that every sentence in the answer has the same evidence level.

---

## 5. Canonical Evidence Labels

Congtie continues to use:

| Level | Chinese Description |
| --- | --- |
| E1 | 权威指南、官方或权威共识证据 |
| E2 | 高质量系统综述、Meta分析或随机对照试验证据 |
| E3 | 观察性研究、真实世界证据或专家共识 |
| E4 | 早期临床研究、动物研究或机制研究 |
| E5 | 专家观点、假说或趋势判断 |
| E0 | 商业来源、用户经验、轶事或未经验证信息 |
| EX | 已证伪、有害、过时或不应采用的信息 |

This contract does not replace the Evidence Grading Framework, introduce GRADE, or change any enum.

---

## 6. Evidence Scope Rule

```text
evidence level != unlimited applicability
```

For example, `KN-T0206-0001` uses `E5 / product_policy` for the Founder-curated Congtie Longevity Strategy framework. Its components retain their own claim-specific evidence:

- premature-mortality prevention may be supported by E1 public-health evidence;
- physical and cognitive capability may be supported by E3 population research and professional consensus;
- biological-aging concepts may be supported by E2 high-quality reviews;
- the complete Congtie strategy framework remains E5 / product policy.

Congtie must not downgrade every component to E5 because it appears within KN-T0206. It must also not upgrade the complete framework to E1 because one component has an E1 source.

---

## 7. Default User Answer Structure

For substantive longevity answers, the default structure should be:

```text
回答 / 解读
[main answer]

依据与证据
[evidence summary]

个人依据（如适用）
[personal context basis]

参考来源
[references]
```

Simple, low-risk answers may render this structure compactly. High-risk, uncertain, or mixed-evidence answers should expose more detail.

---

## 8. Evidence Summary Contract

An evidence summary should identify:

### 8.1 Major Claim

The main conclusion being supported.

### 8.2 Evidence Level

Show both code and Chinese description, for example:

```text
E2（高质量系统综述、Meta分析或随机对照试验证据）
```

### 8.3 Evidence Scope

State exactly what the grade supports and what it does not support.

### 8.4 Evidence Consistency

Where useful, plain-language descriptions may include:

```text
broadly_consistent
mixed
conflicting
insufficient
```

These are explanatory phrases and a future structured answer descriptor, not a replacement for E1-E5 and not a new formal enum. Evidence consistency asks whether multiple high-quality sources agree; evidence level asks what kind of evidence supports the claim.

### 8.5 Key Uncertainty

Identify relevant limitations, such as:

- data quality or missing data;
- population and generalizability limits;
- measurement and device limits;
- causality limits;
- applicability to the current user;
- source freshness or regulatory-jurisdiction limits.

---

## 9. Personal Context Basis

When an answer interprets a biomarker, body state, personal action, or future Personalized Longevity Protocol, Congtie must distinguish:

```text
External Evidence
!=
Personal Context Basis
```

The governing distinction is:

> 外部证据说明“一般情况下什么可能成立”；个人依据说明“为什么该信息可能与当前用户相关”。用户自述、设备数据、检测结果和临床记录可以成为个性化解读依据，但不会因为属于用户本人，就自动成为科学证据。

E1-E5 evaluates an external claim, source body, or product/framework claim. It must not be assigned to a user observation as a user evidence grade.

### 9.1 User-Reported State / 用户自述状态

Examples include:

- mood / 情绪状态;
- perceived stress / 主观压力;
- fatigue / 疲劳感;
- subjective well-being / 心理感受;
- major life event / 重要生活事件;
- work, family, or relationship context.

User-reported state is personal context and a personalization basis. It is not assigned a scientific evidence level merely because it is structured or recorded repeatedly.

### 9.2 Behavior and Lifestyle Record / 行为与生活方式记录

Examples include:

- sleep;
- exercise and physical activity;
- diet and nutrition;
- social connection;
- workload;
- relaxation or recovery practice.

These records may help explain timing, patterns, and possible relationships. They do not by themselves establish causality or a medical conclusion.

### 9.3 Device-Derived Proxy / 设备推断或数字代理信号

Examples include:

- device stress estimate / 设备压力估算;
- device-inferred stress index / 设备推断压力指数;
- estimated sleep stage;
- HRV-derived readiness or recovery score;
- digital phenotype;
- algorithm-derived mood or stress estimate.

A manufacturer or device's official metric name must be preserved. If the official name is `Stress Score`, Congtie may display:

```text
原始名称：Stress Score
用户解释：设备推断压力指数
```

Where available, record:

- device or platform;
- metric name;
- date and time;
- algorithm or version;
- whether the value is measured, estimated, or inferred;
- known limitations and validation scope.

A device-derived proxy is an algorithmic proxy signal. It is not a direct reading of emotion, mental state, or diagnosis, and one device stress estimate must not independently generate a medical conclusion.

### 9.4 Clinical or Biomedical Information / 临床或生物医学信息

Examples include:

- validated professional questionnaire result;
- laboratory biomarker;
- clinical note;
- diagnosis record;
- prescribed medication;
- professional assessment result.

These items must remain distinguishable as a clinical record, personal measurement, or professional assessment. A personal clinical record is not itself scientific evidence for a general claim.

### 9.5 Stress, Emotion, and Biomarker Boundary

Emotion, perceived stress, and mental state are not automatically biomarkers. Depending on provenance and method, they may be user-reported state, psychosocial or lifestyle context, a structured questionnaire result, or a professional assessment result.

Stress-related physiological signals may include:

- heart rate;
- heart-rate variability / HRV;
- sleep signals;
- electrodermal activity;
- cortisol;
- respiratory signals;
- other validated physiological measures.

These signals are often non-specific. A physiological signal may differ from a user's reported experience. Interpretation must consider time, setting, measurement method, algorithm, validation population, and personal context.

Congtie must not state:

```text
HRV = stress
device stress estimate = mental-health diagnosis
```

### 9.6 Core Personal Context Metadata

Personal context may include:

- measurement date;
- value and unit;
- laboratory, device, report, or user-reported source;
- longitudinal trend and baseline;
- freshness;
- relevant lifestyle or action context;
- missing context;
- user permission and intended use.

Internal personal-context governance should be able to represent, without creating a formal enum in this document:

- `consent_scope`;
- `permission_status`;
- `purpose_of_use`;
- `data_used`;
- `authorization_checked_at`;
- `authorization_withdrawn_at`, where applicable.

Possible state concepts include `authorized`, `restricted`, `record_only`, `interpretation_allowed`, `protocol_use_allowed`, `sharing_not_allowed`, `authorization_pending`, and `withdrawn`.

The user interface should not expose a long authorization record in every ordinary answer. It should explicitly surface permission status when sensitive personal data is first used, scope is incomplete, data is record-only, data will inform a Personalized Longevity Protocol, third-party sharing is involved, authorization is pending or withdrawn, or the Agent cannot confirm authority to use the data. A future protocol should support an expandable `本次方案使用了哪些个人健康信息` explanation.

Example rendering:

```text
个人依据：
- 测量日期：2026-08-18
- 数值与单位：[verified value and unit]
- 数据来源：[laboratory / device / report / user report]
- 纵向背景：[verified trend or insufficient history]
- 当前尚缺：[missing context]
```

User data is not scientific evidence. It is the personalization basis and must not be represented as proof of efficacy or general medical knowledge. Personal-context use must also satisfy consent scope, permission status, and purpose limitation.

---

## 10. Reference Rendering Contract

### 10.1 Minimum User-Visible Reference

Each displayed reference should include, when verified and available:

```yaml
source_title:
organization_or_journal:
author:
publication_year_or_date:
source_type:
supports:
source_url:
doi:
pmid:
access_or_check_date:
verification_status:
```

The minimum useful rendering is:

```text
[reference number] Source title
Institution or journal: ...
Type: ...
Supports: ...
Link: ...
Checked: ...
```

Author, DOI, and PMID should be displayed when useful and verified. They must not be guessed.

### 10.2 Supports / 本来源主要支持

Every important reference should explain which claim it supports.

Example:

```text
[1] WHO - Healthy ageing and functional ability
机构：World Health Organization
类型：official public-health source
支持：健康老龄化、功能能力和环境互动的一般框架
链接：[verified stable URL]
```

### 10.3 Why This Source / 为什么引用

The answer harness should be able to distinguish roles such as:

- definition authority;
- guideline recommendation;
- systematic-review evidence;
- measurement-method evidence;
- safety or regulatory status;
- expert viewpoint only;
- commercial self-description only.

`source_type` describes the category of a source. `Why This Source` explains its role for the specific claim. They are related but not interchangeable.

---

## 11. Citation Integrity

Congtie must not:

- invent a source title, author, DOI, PMID, date, or URL;
- cite a source that does not support the claim;
- transfer evidence from one claim to an unrelated claim;
- use a commercial page as efficacy evidence when it only supports product self-description;
- present an abstract, Perspective, Commentary, or organization page as a different source type;
- silently present stale or unverified metadata as current;
- expose private user information in public references.

Source-specific verification should use:

- PubMed, NLM, or the journal's formal page for PMID;
- a DOI resolver, Crossref, or the publisher's formal page for DOI;
- official institution, government, or regulator pages for guidelines, regulations, and policy;
- PubMed, DOI, a journal page, or a formal open-full-text repository for journal articles.

Semantic Scholar and similar discovery tools may help locate sources, but must not be the only authenticity check.

If a title, author, DOI, PMID, or URL cannot be verified, Congtie must not guess. It should omit the field or display:

```text
bibliographic verification pending
```

It should also reduce claim strength and disclose uncertainty. For high-risk, specifically actionable medical advice, failure to verify a core source should pause the specific advice, reduce the answer to general education, request a verifiable source, or recommend professional confirmation. A partial, honest reference is preferable to fabricated completeness.

---

## 12. Canonical Knowledge and Live Retrieval

### 12.1 Canonical Knowledge

Use reviewed canonical knowledge for:

- stable definitions;
- reviewed evidence synthesis;
- safety and commercial boundaries;
- approved high-quality sources;
- stable product and governance concepts.

### 12.2 Live Retrieval

Use live retrieval for time-sensitive facts such as:

- the latest guideline or study;
- current regulation;
- current product or device version;
- provider, price, availability, and China availability;
- current approval or regulatory claims.

Live retrieval must not silently override canonical knowledge. A difference should trigger review of freshness, source quality, claim scope, and jurisdiction.

Freshness metadata should support `source_published_date`, `source_checked_at`, `live_retrieved_at`, `freshness_class`, and `superseded_status`. Where useful, the user may see `依据核验至：YYYY-MM-DD`.

Freshness policy must be domain-specific. Stable definitions and classic methodology may remain valid for long periods, while regulation, medication guidance, infectious-disease guidance, device versions, prices, and availability may change quickly. There is no global `older than two years = obsolete` rule, and ordinary answers need not display the model training cutoff.

---

## 13. Reference Budget and UX

Default user-visible answers should normally show:

```text
1-3 most important references
```

An expanded `查看依据 / 查看全部参考来源` view may expose:

- additional references;
- detailed evidence scope;
- source notes;
- conflicts and uncertainties;
- full bibliographic metadata.

High-risk, high-uncertainty, or conflicting-evidence questions may require more visible sources. This document does not define frontend implementation.

---

## 14. Output by Answer Type

### 14.1 General Longevity Q&A

```text
Answer
-> major claim
-> evidence level and scope
-> uncertainty
-> 1-3 references
```

### 14.2 Biomarker or Body-State Interpretation

```text
Interpretation
-> personal data basis
-> unit, date, source, freshness, and trend
-> measurement uncertainty and reference context
-> external evidence
-> missing context
-> safety boundary
-> references
```

It must not convert one value, one device score, or one reference-range flag into a diagnosis or personal risk conclusion.

#### Stress and Emotion Structure Example

The following illustrates structure only and contains no real user data or medical judgment:

```text
解读
最近的主观压力和情绪记录显示：[describe only the verified pattern and context]

个人依据
- 用户自述压力：[verified user-reported state]
- 记录日期：[date]
- 近期睡眠趋势：[verified trend or insufficient history]
- 重要生活事件：[user-authorized context or not available]
- 设备压力估算：[device-derived estimate or not available]
- 如设备原始名称为 Stress Score，应同时保留原始名称
- 设备压力估算属于算法推断，不是情绪直接读取或心理诊断

外部证据
- 压力、睡眠、行为和心理健康的一般证据：[claim-specific summary]
- 主要结论证据等级：[code + Chinese description]

不确定性
- 自评、设备推断、生理信号和临床状态不能互相替代
- 当前尚缺：[missing context]
```

### 14.3 Action Advice

```text
Suggested low-risk action
-> why this action
-> expected general benefit
-> evidence level and scope
-> personal basis, if authorized
-> risks, contraindication boundary, and escalation conditions
-> review or remeasurement plan
-> references
```

The output must remain within the approved action, clinical, and personalization permissions.

### 14.4 Personalized Longevity Protocol

Future protocol output should include:

```text
protocol component
-> why included
-> evidence and source
-> personal context basis
-> action, cadence, and trigger
-> remeasurement or review
-> update rule
-> uncertainty and safety boundary
```

This contract does not authorize or generate a Personalized Longevity Protocol in Congtie v0.

---

## 15. Future Schema and Governance Gaps

### 15.1 P0 Before Runtime Citation Rendering

- structured source records with stable source IDs;
- claim-to-source mapping;
- claim-specific evidence level and evidence scope;
- source title, organization or journal, publication date, URL, DOI, and PMID fields when available;
- `Supports` and source-role fields;
- source verification status and access or retrieval timestamp;
- separation of external evidence from user-data provenance;
- no-phantom-citation and claim-support validation;
- answer-level rendering contract and safe privacy filtering.

### 15.2 P1 Future Governance

- richer author and contributor records;
- source-version and regulatory-jurisdiction history;
- conflict-of-interest metadata, including `funding_source`, `conflict_of_interest`, `sponsor_role`, and `independence_note` where verifiable and materially relevant;
- structured evidence-consistency and disagreement summaries;
- automated DOI, PMID, and bibliographic resolution;
- channel-specific citation layouts and expanded-reference behavior;
- automated freshness monitoring;
- structured citation-correction workflow;
- multilingual and jurisdiction-aware localization;
- rights, license, local-copy, and retrieval-governance integration.

A commercial relationship does not automatically invalidate a study, but a material relationship must not be hidden when it could affect interpretation.

No schema change is made by this document.

---

## 16. Known Source-Type Gaps

The current source-type enum does not precisely represent every reviewed source role. Known gaps include:

- official terminology resource;
- official measurement standard or metrology method;
- internal governance document;
- official regulator page or formal regulation;
- peer-reviewed Perspective;
- peer-reviewed Commentary;
- generic peer-reviewed Journal Article that is not accurately classified as review, RCT, observational, or mechanistic.

These gaps must be recorded rather than hidden through overclassification. This document does not modify the enum.

---

## 17. Batch 001 B2-A Founder-Approved Production Baseline

The following seven-entry set is locked for this proposal and production round and will not be expanded or reordered before the next Founder Gate. Locking does not mean each entry's content, evidence grade, sources, safety wording, or final language has already been approved.

> “锁定”只表示本轮生产集合不再扩充或调整顺序，不表示七条知识内容已经定稿，也不表示可以跳过 AI review 和 Founder 人工审核。

| Order | Candidate Status | Entry ID | Title | Primary Topic | Planning Evidence Estimate |
| --- | --- | --- | --- | --- | --- |
| 1 | Existing candidate | KN-T0403-0001 | 什么是生物标志物 / What Is a Biomarker? | T04.03 | E1, subject to claim-level review |
| 2 | Founder approved for allocation; Batch Plan allocation pending | KN-T0403-0002 | 如何理解基线、长期趋势、测量误差与生物波动 / Understanding Baselines, Longitudinal Trends, Measurement Error, and Biological Variation | T04.03 | E3, subject to source review |
| 3 | Existing candidate, promoted from B2-B | KN-T0408-0001 | 如何理解可穿戴与消费级设备数据 / Understanding Wearable and Consumer Device Data | T04.08 | E3, subject to device-claim scope |
| 4 | Existing candidate | KN-T0501-0001 | 睡眠基础 / Sleep Basics | T05.01 | E1, subject to exact claims |
| 5 | Existing candidate | KN-T0503-0001 | 锻炼基础 / Exercise Basics | T05.03 | E1, subject to exact claims |
| 6 | Existing candidate with proposed Chinese title refinement | KN-T0502-0001 | 饮食与营养基础 / Nutrition Basics | T05.02 | E1, subject to exact claims |
| 7 | Existing candidate; Founder-approved production title; clinically sensitive | KN-T0504-0001 | 压力、情绪与心理健康基础 / Stress, Emotions, and Mental Well-Being Basics | T05.04 | Claim-specific E1, E2-E3, or E5 scope; not one locked grade |

The evidence levels above are planning estimates only. Formal production must determine each entry's evidence level from its actual claims, sources, and evidence scope.

### 17.1 Terminology Requirements

`KN-T0503-0001` must distinguish:

```text
Physical Activity = 身体活动
Exercise = 锻炼
Training = 训练
```

`KN-T0502-0001` should use the user-facing domain term:

```text
饮食与营养
```

The current Batch Plan title `营养基础` has not been modified by this task.

`KN-T0504-0001` should use the proposed user-facing title:

```text
压力、情绪与心理健康基础
Stress, Emotions, and Mental Well-Being Basics
```

The current Batch Plan has not been modified by this task.

---

## 18. B2-A Overlap and Safety Boundaries

### 18.1 KN-T0403-0002 and KN-T0204

`KN-T0204-0001` explains how Congtie organizes the `测量-解读-行动-复测` feedback loop as a product and practice framework.

`KN-T0403-0002` should explain why measurements vary and how to distinguish:

- personal baseline;
- longitudinal trend;
- measurement error;
- preanalytical factors;
- biological variation;
- method or platform changes;
- single-point fluctuation.

The two entries are complementary but not duplicative. `KN-T0403-0002` explains why values change and which changes may not represent a real physiological change. `KN-T0204-0001` explains how measurement, interpretation, action, and remeasurement operate as a long-term product and practice feedback loop. Measurement error and biological variation must not be treated as the same phenomenon.

### 18.2 KN-T0408-0001 and Product Recommendation

The wearable entry may explain:

- consumer-device data;
- measured versus estimated values;
- trends and repeated observations;
- validation and population limits;
- device, algorithm, and firmware dependence;
- clinical and non-clinical boundaries.

It must not:

- recommend or rank brands;
- provide purchasing advice;
- treat a device score as a diagnosis;
- transfer evidence from one device or algorithm to another.

### 18.3 KN-T0504-0001 - Production Scope and Safety

Primary topic:

```text
T05.04 Stress / 压力
```

Recommended production setting:

```yaml
is_clinical_sensitive: true
```

The entry should explain:

1. stress, stressors, and stress responses;
2. the distinction among emotional state, mental well-being, and mental disorder;
3. normal stress responses versus persistent or severe distress;
4. useful user-reported states and daily context;
5. differences among self-report, professional questionnaires, device inference, physiological signals, and laboratory biomarkers;
6. why HRV, sleep, or a device stress estimate cannot independently determine mental state;
7. how authorized stress and emotion information may enter the User Health Information Library;
8. when everyday self-management is insufficient and professional support is appropriate;
9. how to avoid both pathologizing normal emotion and overlooking persistent, severe, function-limiting, or safety-relevant change;
10. how work stress, emotional labor, occupational burnout, workload, control, organizational environment, workplace relationships, financial pressure, and social support may form important psychosocial context.

It is a general foundation and education entry. It is not:

- a depression or anxiety-disorder guide;
- a diagnosis tool;
- a suicide-risk calculator;
- a psychotherapy protocol;
- a medication guide;
- a supplement recommendation;
- validation of a specific brand's wearable stress score.

Required safety boundaries:

- emotion is not a disease diagnosis;
- a stress score is not a mental-health diagnosis;
- self-report is not a clinical diagnosis;
- a single HRV, heart-rate, sleep, cortisol, or other physiological result cannot establish a mental disorder;
- professional-support signals include persistent or worsening distress, meaningful impairment in work, study, family, or social function, feeling unable to cope, or substantial changes in sleep, appetite, mood, or behavior;
- self-harm, suicide, other safety-related thoughts, or acute danger require an independent urgent safety-escalation path and must not wait for the ordinary feedback loop;
- `two weeks` is not a universal escalation threshold; a specific duration may be used only when a verified disease definition, formal scale, or guideline defines it for that context;
- work stress, emotional labor, and burnout do not automatically equal a mental disorder and must not be reduced to insufficient personal resilience;
- Agent advice should distinguish personally modifiable factors from structural or organizational factors and must not rely only on “adjust your mindset”;
- the entry must not generate a risk score, personalized psychotherapy, medication, supplement plan, diagnosis, or clinical treatment;
- a future Personalized Longevity Protocol may use authorized stress and emotion context, but must not turn that context alone into a medical conclusion.

Evidence planning must remain claim-specific:

- definitions and general safety boundaries may use E1 authority or public-health sources;
- associations, monitoring, validation, and device proxies may use E2-E3 systematic reviews, observational studies, and validation research;
- the Congtie tracking framework may remain E5 / product_policy;
- an E1 WHO source must not upgrade the complete Congtie tracking framework to E1.

---

## 19. B2-A Production Source Strategy

No restricted full text should be downloaded or ingested under this plan.

### 19.1 KN-T0403-0001 - Biomarkers

Preferred sources:

- FDA-NIH BEST Resource for reviewed terminology;
- appropriate peer-reviewed terminology and validation literature;
- claim-specific clinical or laboratory guidance where needed.

Boundary: definition authority does not prove clinical utility for every biomarker and does not automatically make the complete entry E1.

### 19.2 KN-T0403-0002 - Baselines, Trends, Error, and Biological Variation

Preferred sources:

- measurement-science and metrology sources;
- NIST material where applicable;
- peer-reviewed biological-variation literature;
- clinical laboratory measurement and repeated-measurement guidance where needed.

Boundary: analytical error, device error, pre-analytical variation, within-person biological variation, and true longitudinal change require explicit distinction.

### 19.3 KN-T0408-0001 - Wearable and Consumer Device Data

Preferred sources:

- regulator or general-wellness guidance;
- independent device-validation research;
- professional reviews;
- manufacturer documentation only for verified specifications and algorithm descriptions.

Boundary: manufacturer or commercial pages do not independently establish health-outcome efficacy.

### 19.4 KN-T0501-0001 - Sleep Basics

Preferred sources:

- AASM and Sleep Research Society materials;
- NHLBI;
- relevant WHO or other public-health sources;
- systematic reviews for claim-specific relationships.

Boundary: general sleep education must not become diagnosis or a personalized sleep-treatment plan.

### 19.5 KN-T0503-0001 - Exercise Basics

Preferred sources:

- WHO physical-activity guidelines;
- ACSM and other appropriate professional exercise sources;
- verified Chinese formal physical-activity, scientific-fitness, or national-fitness materials for China execution context;
- systematic reviews for claim-specific benefits.

A Chinese source is not mandatory for every exercise claim, and sports-promotion material must not be treated as medical-efficacy evidence.

Boundary: general activity guidance must not become a personalized training prescription, rehabilitation plan, or clearance decision.

### 19.6 KN-T0502-0001 - Diet and Nutrition Basics

Preferred sources:

- WHO Healthy Diet;
- the current effective edition of the Chinese Dietary Guidelines as a core source for Chinese users;
- National Health Commission standards where claim-specific;
- high-quality systematic reviews where needed.

The Chinese Dietary Guidelines provide a China-context authority and must not be presented as the only global definition of a healthy diet.

Boundary: general dietary-pattern education must not become a disease diet prescription, individualized calorie or nutrient prescription, or supplement protocol.

### 19.7 KN-T0504-0001 - Stress, Emotions, and Mental Well-Being Basics

Preferred official and professional sources:

- WHO Stress Q&A;
- WHO mental-health materials;
- NIMH stress and mental-health educational resources;
- verified National Health Commission materials;
- verified materials from 国家心理健康和精神卫生防治中心;
- other verified national-level Chinese public mental-health materials.

China CDC-related materials may be used after page-by-page verification. No organization should be predeclared as a fixed authority anchor without verifying its formal name and page responsibility.

Preferred peer-reviewed sources:

- reviews of perceived stress and health outcomes;
- stress-physiology and biological-variation literature;
- wearable and digital stress-monitoring validation research;
- research comparing self-report with physiological measurement.

Chinese population studies or annual reports may support population surveys, social trends, China context, and research questions. They must not be used as clinical diagnostic guidance, regulatory authority, or individualized treatment advice.

Boundaries:

- do not add a low-quality Chinese source merely for localization;
- verify all source names, responsible organizations, and pages during production;
- distinguish general education from diagnosis and treatment;
- distinguish association from causality;
- distinguish a measured physiological signal from an inferred device estimate;
- do not treat one proxy as a direct measure of emotion or mental disorder.

---

## 20. Current B2-B Proposal

The following five entries remain proposed for B2-B and are not created by this task:

| Entry ID | Working Title | Note |
| --- | --- | --- |
| KN-T0501-0002 | 睡眠时长、规律与主观质量 | Retain as the next sleep layer. |
| KN-T0503-0002 | 运动能力与心肺能力背景 | Review exercise terminology during production. |
| KN-T0503-0003 | 力量、活动度与平衡 | Keep behavior-practice scope distinct from KN-T0202-0001. |
| KN-T0502-0002 | 蛋白质基础 | Do not generate individualized intake prescriptions. |
| KN-T0502-0003 | 膳食纤维基础 | Use claim-specific Chinese and international sources. |

---

## 21. Candidate Pool Decision

The current Batch 001 candidate pool remains:

```text
62
```

`KN-T0403-0002` is recorded here as:

```text
Founder approved for Batch Plan allocation
Allocation pending the next task
```

`KN-T0504-0001` already exists in the Batch Plan and is Founder-approved for production with `is_clinical_sensitive: true`. It remains a general education entry, not a mental-disorder diagnostic guide, risk score, psychotherapy protocol, medication guide, or supplement plan.

A separate task should update the Batch Plan:

```text
62 -> 63
```

The approximately 50 accepted-entry target remains unchanged. No Batch Plan modification is made in this task.

---

## 22. Source Library Rights Boundary

`Congtie Source Library + Rights / License / Retrieval Governance v0.1` remains a P0 auxiliary line.

It does not block B2-A production using:

- official public webpages;
- official guidelines;
- PubMed metadata and abstracts;
- open-access papers;
- legally accessible public sources.

Before any of the following, rights and retrieval governance must be completed:

- commercial-book or paid-paper full-text ingestion;
- scanning purchased books for machine ingestion;
- persistent copyrighted PDF chunking;
- embeddings;
- persistent RAG corpus creation;
- large-scale course or textbook machine ingestion.

This contract does not ingest, download, chunk, embed, or persist any external source.

---

## 23. Acceptance Criteria

This v0.1 baseline is Founder-approved when it:

- defines claim-level rather than whole-answer evidence scope;
- separates External Evidence from Personal Context Basis and does not assign E1-E5 to a user observation;
- records consent scope, permission status, and purpose limitation for personal-context use;
- defines minimum reference and `Supports` rendering;
- prohibits fabricated or unsupported citations and defines verification failure behavior;
- distinguishes canonical knowledge from live retrieval and uses domain-specific freshness;
- uses `Explanation / 解释` for general scientific concepts, medical terms, research conclusions, public knowledge, and general evidence background;
- uses `Interpretation / 解读` for a user's measurements, reports, biomarker results, longitudinal trends, body state, device data, and personalized context;
- prohibits a mechanical repository-wide replacement of 解释 with 解读;
- defines output structures for four answer types;
- records P0 and P1 schema/governance gaps without changing schema;
- records known source-type gaps without changing the enum;
- locks the Founder-approved seven-entry B2-A production baseline without bypassing entry-level AI or Founder review;
- preserves B2-B as a five-entry proposal;
- records `KN-T0403-0002` as approved for allocation while leaving the candidate pool and Batch Plan unchanged in this task;
- records `KN-T0504-0001` as clinically sensitive with independent safety escalation;
- creates no knowledge entry, runtime behavior, publication, or retrieval state.

---

## 24. Citation Correction, Localization, and Commercial Independence

Citation correction should classify at least:

- `incorrect_source`;
- `broken_link`;
- `source_does_not_support_claim`;
- `wrong_DOI`;
- `wrong_PMID`;
- `wrong_title_or_author`;
- `outdated_or_superseded_source`;
- `missing_safety_boundary`;
- `translation_or_localization_error`;
- `privacy_or_permission_error`.

Critical errors include source misattribution, a source that does not support a high-risk action, a missing material safety warning, potentially harmful citation error, or privacy overreach. Related content or citations should be paused and reviewed immediately, with same-source use reviewed where appropriate. Major errors include a materially wrong evidence level, a core conclusion inconsistent with its source, or a key source that has been superseded. Minor errors include non-critical formatting, spelling, or display metadata.

This baseline does not promise a public 24-hour correction SLA. A service-level commitment requires later operational and monitoring capability.

For interventions, products, devices, supplements, medications, and commercial services, verifiable funding, employment, patent, consulting, equity, and sponsor roles should be recorded when materially relevant. Conflicts do not automatically invalidate research, but material commercial relationships must not be hidden.

Localization rules are:

1. retain the English term at first use when it prevents medical ambiguity;
2. avoid mechanical translation that changes meaning;
3. distinguish international definitions, Chinese guidance, and regional regulation;
4. prefer the applicable jurisdiction for epidemiology, care standards, medication regulation, and service availability;
5. disclose population and regional limits when only non-China evidence is available;
6. never make the Chinese conclusion stronger than the source.

---

## 25. Cross-Document Consistency Baseline

This contract and the Whole-Body Health Information Model / Registry specification share these rules:

1. External Evidence and Personal Context Basis are separate.
2. A user observation is personal context, not scientific evidence.
3. A Registry item is not a concept knowledge entry.
4. A Registry item is not a user observation.
5. The Registry is not a service Panel.
6. A reference interval is not a clinical decision limit.
7. A device estimate is not a diagnosis.
8. A validated questionnaire or scale is not a biomarker.
9. Screening is a use context, not an eighth BEST role.
10. Evidence level binds to a claim, intended use, and evidence scope.
11. Consent and purpose-of-use records belong to the user-data layer, not the public Registry.
12. Neither document generates or authorizes a Personalized Longevity Protocol.
13. Both documents record the same seven-entry B2-A production baseline.
14. `KN-T0403-0002` is Founder-approved for allocation; the Batch Plan change is pending.
15. `KN-T0504-0001` is clinically sensitive and uses an independent safety-escalation boundary.

---

## 26. Founder Review Decisions / Deferred or Rejected Suggestions

The following suggestions are not adopted in v0.1:

- replacing E1-E5 with `high / medium / low / controversial`;
- displaying the model training cutoff in every answer;
- treating all sources older than two years as obsolete;
- requiring every citation to pass Crossref, PubMed, and Semantic Scholar simultaneously;
- promising a public 24-hour correction SLA before operational capability exists.

Evidence consistency may be recorded as a separate future descriptor. It does not replace the Evidence Framework.

---

## 27. Founder Approval Boundary

Founder approval covers the conceptual output contract, claim-level evidence rules, citation and permission governance, and B2-A production baseline.

It does not authorize:

- runtime citation rendering or retrieval;
- persistent RAG or source ingestion;
- cloud storage of user health information;
- diagnosis, treatment, risk scoring, or medication logic;
- generation of a Personalized Longevity Protocol;
- B2 entry approval, publication, runtime, or retrieval;
- modification of the Knowledge Item Schema or evidence enum.

---

## 28. Next Gate

Under separate tasks:

1. controlled commit and push of the two Founder-approved P0 documents;
2. allocate `KN-T0403-0002` in the Batch Plan and update the candidate pool from 62 to 63;
3. begin B2-A knowledge production as the main line;
4. begin Registry Seed 001 planning and asset reconciliation as the auxiliary P0 line.

This document does not execute any next-gate task.
