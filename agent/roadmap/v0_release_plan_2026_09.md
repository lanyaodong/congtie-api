# Congtie v0 Release Plan 2026-09

Version: v0.1
Project: Congtie
Status: Draft
Owner: Congtie Agent Team
Last Updated: 2026-08-07

---

## 1. Executive Summary

Congtie has completed the initial foundation stage for a bounded v0 longevity assistant.

Completed foundations include:

- brand migration from Xiaoge to Congtie
- Congtie naming conventions
- `congtieai.com` domain launch
- longevity information architecture
- longevity topic taxonomy
- Knowledge Seed v0
- six body system architecture
- safety boundaries
- action resource governance
- frontend/backend foundation work

The next objective is to prepare Congtie v0 Public Beta release by September 2026.

Congtie v0 is not intended to be a complete longevity system.

Congtie v0 is intended to validate whether:

- users understand Congtie value
- users can interact with a longevity assistant
- users can receive trustworthy longevity explanations
- users can start building personal health context
- users can experience safe proactive health support

---

## 2. Release Goal

Congtie v0 release goal:

```text
Launch a bounded Public Beta Longevity Assistant by September 2026.
```

The release should prove that Congtie can deliver a useful, trustworthy, non-clinical longevity assistant experience.

The release should prioritize:

- clarity of product positioning
- trust and safety
- useful longevity explanation
- personal context collection
- lightweight proactive support
- reviewable knowledge operations

The release should not attempt to deliver full personalization, clinical decision support, medical automation, or complete platform infrastructure.

---

## 3. v0 Product Definition

Congtie v0 = Public Beta Longevity Assistant.

One-sentence definition:

```text
Congtie v0 helps users understand their longevity-related information, organize health context, and take safe next actions through AI-powered explanation and knowledge support.
```

v0 product shape:

- public website
- AI longevity conversation
- knowledge-based explanation
- basic knowledge browsing
- personal health context collection
- safe next action rationale
- human-reviewed internal knowledge workflow

v0 is a product validation release.

It is not:

- a complete longevity platform
- a medical record system
- a diagnosis system
- a treatment system
- a medication advisor
- a supplement protocol generator
- a biological age scoring engine
- a clinical decision support system

---

## 4. Target Users

### 4.1 Primary Users

Primary target users:

```text
40+ proactive longevity users
```

Characteristics:

- care about healthy aging
- willing to track health
- want trustworthy information
- overwhelmed by fragmented health information
- want AI assistance
- may already have lab reports, health records, wearable data, or lifestyle tracking habits
- want to understand what matters without turning every question into a medical decision

### 4.2 Secondary Users

Secondary target users:

```text
20-40 users interested in preventive health
```

Characteristics:

- curious about longevity
- interested in healthspan
- comfortable with AI tools
- may have incomplete health context
- want basic education and low-risk next steps

---

## 5. Core User Value

### 5.1 Information External Brain

Congtie provides:

- structured longevity knowledge
- evidence-aware explanations
- trustworthy source organization
- topic-based navigation
- context-aware explanation
- safety-aware boundaries

User value:

```text
Users can stop holding fragmented longevity information in their head.
```

### 5.2 Personal Health Context Foundation

Congtie helps users:

- collect health information
- organize records
- preserve test dates, units, reference ranges, and source metadata
- provide context for future personalization
- understand what context is missing

User value:

```text
Users can begin building a personal health context foundation without needing a full medical record system.
```

### 5.3 Safe Action Support

Congtie provides:

- explanation
- missing context reminders
- low-risk next action rationale
- safe information-completion suggestions
- preparation for professional conversations when appropriate

Congtie v0 does not provide:

- diagnosis
- treatment
- medication advice
- dosage advice
- clinical recommendation
- disease prediction
- disease risk calculation
- personalized supplement protocol
- personalized medical intervention

User value:

```text
Users can receive proactive support without crossing into clinical automation.
```

---

## 6. Must-have Features

## 6.1 User Side

### 6.1.1 Website

Must include:

- `congtieai.com` public website
- product introduction
- value proposition
- trust explanation
- safety boundary explanation
- clear positioning as a longevity assistant
- simple path to start conversation or join beta

### 6.1.2 AI Conversation

Must include:

- longevity Q&A
- knowledge-based explanation
- safety boundary handling
- source-aware responses
- missing context prompts
- bounded next action rationale
- user-friendly Chinese language experience

AI conversation must not include:

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

### 6.1.3 Knowledge Access

Must include:

- longevity knowledge browsing
- topic navigation
- article/detail pages
- source-aware explanation
- basic evidence metadata display or explanation
- safety boundary context where relevant

Knowledge access should prioritize usefulness over encyclopedia completeness.

### 6.1.4 User Context

Minimum v0 user context capabilities:

- upload health information
- store user-provided context
- conversation context reference
- collect basic record metadata
- allow user-provided lifestyle context

Do not build a full medical record system in v0.

Do not build hidden medical personalization.

Do not store private user context inside the public knowledge library.

## 6.2 Internal / Admin Side

### 6.2.1 Longevity Information Library

Must include:

- Markdown + Git based storage
- topic mapping
- evidence metadata
- review status
- source URLs and source notes
- content boundaries
- action resource permission metadata

### 6.2.2 Human Review Workflow

Support workflow:

```text
draft
→ ai_review_pending
→ ai_reviewed
→ human_review_pending
→ approved
→ published
```

Workflow rules:

- AI may create drafts.
- AI may perform review support.
- Human approval is required before publication.
- Published content must be traceable.
- Archived and rejected content should remain traceable.

### 6.2.3 Basic Tools

Must include:

- validator
- index generation
- status checking
- lightweight loader
- basic consistency checks

Tools should support:

- CLI workflows
- Git review
- AI editing
- future CMS GUI

---

## 7. Deferred Features

### 7.1 Medical

Explicitly excluded from v0:

- diagnosis
- treatment
- medication recommendation
- dosage
- disease prediction
- clinical decision support
- clinical thresholds
- emergency triage engine
- medical order generation

### 7.2 Advanced Personalization

Explicitly excluded from v0:

- personalized supplement protocols
- personalized medication suggestions
- personalized treatment plans
- personalized nutrition prescriptions
- personalized training prescriptions
- biological age scoring
- system scoring
- disease risk calculation

### 7.3 Automation

Explicitly excluded from v0:

- fully autonomous knowledge production
- automatic publishing
- automatic evidence ingestion
- automatic source approval
- automatic clinical interpretation
- autonomous action execution

### 7.4 Platform

Explicitly excluded from v0:

- complete CMS
- external Agent marketplace
- MCP ecosystem
- API ecosystem
- external provider marketplace
- full multi-user admin console

---

## 8. v1 Preparation Items

v0 should prepare foundations for future versions.

### 8.1 Personalized Longevity Agent

Future model:

```text
model
+
harness
+
longevity information library
+
user health information library
=
personalized longevity assistant
```

v0 should prepare:

- knowledge architecture
- retrieval boundaries
- source metadata
- user context boundary
- permission-controlled action resources
- safety interruption patterns

v0 should not implement full personalization.

### 8.2 User Health Information Library

Future capability:

- biomarkers
- lab reports
- wearable data
- lifestyle records
- longitudinal tracking
- consent-gated context use
- export and deletion

v0 should start with minimum context collection.

v0 should not become a full medical record system.

### 8.3 Action Execution Agent

Future:

- task creation
- reminders
- progress tracking
- habit execution support
- user-confirmed follow-up
- low-risk action loops

v0 should prepare action rationale and permission boundaries.

v0 should not perform autonomous action execution.

---

## 9. Technical Scope

### 9.1 Single Source of Truth

Canonical source:

```text
Markdown + Git
```

Feishu:

```text
human review interface only
```

Feishu may help with review, collaboration, and editing discussion.

Feishu should not silently replace Markdown + Git as source of truth.

### 9.2 AI-first Development

AI executes:

- coding
- documentation
- formatting
- validation
- consistency checking
- draft generation
- review assistance

Human decides:

- product direction
- evidence judgement
- publishing approval
- safety policy
- business boundary
- release readiness

### 9.3 Version Control

All important changes should be:

- traceable
- reviewable
- reversible

Git should preserve:

- content evolution
- review decisions
- source changes
- validator changes
- release status

### 9.4 Runtime Technical Scope

v0 runtime should support:

- public website
- AI conversation endpoint or service flow
- knowledge retrieval
- source-aware answer construction
- safety boundary handling
- basic user context reference
- internal validation workflow

v0 runtime should not include:

- production clinical logic
- clinical scoring
- medication logic
- treatment logic
- disease risk calculators
- hidden commercial conversion

---

## 10. Knowledge Library Scope

Goal:

```text
Minimum useful knowledge base.
```

Not:

```text
complete encyclopedia.
```

Initial target:

```text
50-100 high-value entries
```

Priority scope:

### 10.1 T01 Longevity Foundation

Include:

- healthspan
- lifespan vs healthspan
- Congtie role
- safety boundaries

### 10.2 T02 Longevity Strategy

Include:

- avoid premature mortality
- maintain capability
- slow biological aging
- measurement → explanation → safe action → iteration

### 10.3 T03 Body Systems

Six systems:

- Energy
- Metabolic
- Cardiopulmonary
- Musculoskeletal
- Neurocognitive
- Repair Immune

### 10.4 T04 Measurement

Include:

- biomarkers
- reports
- freshness
- units
- data sources
- reference ranges
- health records

### 10.5 T05 Lifestyle

Canonical order:

```text
sleep
nutrition
exercise
stress
```

Include:

- sleep basics
- nutrition basics
- exercise basics
- stress basics
- recovery context

### 10.6 T07 Action Resources

Initial scope:

```text
Initial low-risk resources only.
```

Include:

- information resources
- low-risk logs and trackers
- information-completion devices
- testing service boundaries
- user-initiated supplement explanations

Action resources must preserve R1/R2/R3 permission boundaries.

---

## 11. User Health Information Library Scope

v0 user health information library should support minimum context collection.

Minimum scope:

- uploaded health information
- user-provided context
- conversation context reference
- basic health record organization
- metadata preservation where possible

Examples:

- test report file
- test date
- units
- reference ranges
- source
- wearable context
- sleep context
- nutrition context
- exercise context
- stress context

v0 should not build:

- full medical record system
- clinical interpretation engine
- disease prediction engine
- automated treatment planner
- hidden commercial targeting system

Boundary:

```text
Longevity Information Library = general reusable knowledge
User Health Information Library = private user-specific context
```

The two may interact only within approved runtime safety and consent boundaries.

---

## 12. Safety Boundaries

Congtie v0 must preserve non-clinical boundaries.

Congtie v0 must not provide:

- diagnosis
- treatment
- medication advice
- dosage advice
- clinical recommendation
- system scoring
- disease risk calculation
- disease prediction
- personalized supplement protocol
- personalized nutrition prescription
- personalized training prescription
- personalized medical intervention
- emergency triage engine

Safety behavior should include:

- clear role boundary
- missing context reminders
- professional consultation preparation when appropriate
- safety interruption where needed
- no clinical automation

Action resource boundaries:

```text
R0 = prohibited automatic recommendation
R1 = user-initiated explanation only
R2 = information-completion option
R3 = low-risk general tool option
```

R1/R2/R3 permission must remain a runtime control.

Evidence level must not override safety boundary.

Topic mapping must not override safety boundary.

---

## 13. Release Milestones

### 13.1 August 2026

Foundation completion:

- knowledge template
- release plan
- validator
- first knowledge entries
- minimum knowledge index
- initial retrieval design
- beta website readiness review
- internal safety boundary review

### 13.2 Early September 2026

Internal beta:

- knowledge retrieval
- user conversation
- basic user context
- internal feedback collection
- source-aware answer checks
- safety behavior smoke tests

### 13.3 Mid September 2026

Founder testing:

- daily usage
- content refinement
- safety validation
- user context flow review
- website positioning review
- beta readiness triage

### 13.4 Late September 2026

Public Beta:

- website
- AI assistant
- knowledge access
- feedback collection
- issue tracking
- lightweight content update loop
- public positioning validation

---

## 14. Task Ownership Model

### 14.1 AI Agent Responsibilities

AI agents execute:

- coding
- documentation drafting
- formatting
- validation
- consistency checks
- source summarization
- topic mapping suggestions
- draft knowledge entry generation
- test and smoke run reporting

AI agents must not:

- bypass human approval
- publish automatically
- create diagnosis
- create treatment plans
- create medication advice
- create dosage advice
- create personalized supplement protocols
- introduce production clinical logic
- modify biomarker JSON without explicit founder approval

### 14.2 Human / Founder Responsibilities

Humans decide:

- product direction
- release scope
- evidence judgement
- publishing approval
- clinical and safety boundary decisions
- commercial boundary decisions
- external launch readiness

### 14.3 Review Responsibilities

Every release-relevant artifact should be:

- traceable
- reviewable
- reversible
- associated with an owner or reviewer

Recommended review gates:

- content review
- safety review
- engineering review
- beta readiness review
- launch approval

---

## 15. Acceptance Criteria

v0 release is acceptable when:

### 15.1 Product

- users understand Congtie positioning
- users can interact with AI assistant
- users can access trustworthy longevity information
- users can provide personal context
- users can understand safety boundaries
- users can submit feedback

### 15.2 Knowledge

- first knowledge library exists
- entries have metadata
- review workflow works
- topic mapping exists
- evidence metadata exists
- source notes exist for key entries
- action resources preserve permission boundaries

### 15.3 Engineering

- repository structure is stable
- validation works
- deployment works
- basic monitoring or smoke checks exist
- response envelope remains stable
- safety interruption behavior remains bounded

### 15.4 Safety

- no diagnosis
- no treatment
- no medication advice
- no dosage advice
- no clinical recommendation
- no personalized supplement protocol
- no disease risk calculation
- no system scoring
- no hidden commercial conversion

---

## 16. Risks and Constraints

### 16.1 Product Risks

- users may not understand the difference between longevity explanation and medical advice
- v0 value may feel too broad without a crisp first-use flow
- users may expect full personalization earlier than the system can safely support
- knowledge browsing may feel thin if fewer than 50 high-value entries are ready

### 16.2 Knowledge Risks

- source review may lag behind content creation
- AI-generated drafts may appear polished before human review
- taxonomy and information layer mapping may become inconsistent without validators
- source URLs may change or disappear

### 16.3 Engineering Risks

- frontend/backend integration may require additional hardening before public beta
- retrieval quality may be uneven with a small knowledge base
- user context storage may need stronger privacy design before wider release
- deployment readiness may lag behind content readiness

### 16.4 Safety Risks

- users may ask for diagnosis, treatment, medication advice, dosage, risk calculation, or emergency triage
- supplement and action resource topics may invite over-prescriptive answers
- evidence metadata may be misinterpreted as permission to recommend
- personal context may be mistaken for clinical personalization

### 16.5 Constraints

- v0 must stay non-clinical
- v0 must preserve safety boundaries
- v0 must use human approval for publication
- v0 must preserve Markdown + Git as source of truth
- v0 must avoid hidden commercial conversion
- v0 must not modify biomarker JSON or connect draft biomarker maps to production without founder approval

---

## 17. Naming Rules

Use:

```text
Congtie
```

as the display name.

Use:

```text
congtie
```

for:

- code
- domain
- lowercase identifiers

Do not use the deprecated camel-case brand spelling.

---

## 18. Recommended Next Steps

Recommended next task sequence:

```text
1. Create v0 release task backlog.
2. Create knowledge entry validator for the new template.
3. Draft the first 20 high-value knowledge entries.
4. Define minimum retrieval contract.
5. Define user context v0 storage boundary.
6. Run website positioning review.
7. Run internal beta readiness checklist.
```

---

## 19. Final Note

Congtie v0 should be ambitious in usefulness and conservative in safety.

The safest v0 release principle is:

```text
Help users understand.
Help users organize context.
Help users take safe next steps.
Do not become a clinical system.
```
