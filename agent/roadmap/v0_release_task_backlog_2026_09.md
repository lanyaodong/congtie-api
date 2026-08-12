# Congtie v0 Release Task Backlog 2026-09

Version: v0.1
Project: Congtie
Status: Draft
Owner: Congtie Agent Team
Last Updated: 2026-08-07

---

## 1. Overview

Congtie v0 is entering release execution phase.

This document converts release strategy into executable AI team tasks.

Primary input documents:

```text
agent/roadmap/v0_release_plan_2026_09.md
agent/longevity_knowledge_base/templates/longevity_knowledge_item_template.v0.1.md
```

Release goal:

```text
Ship Congtie v0 Public Beta by September 2026.
```

This document defines:

- executable tasks
- priorities
- ownership
- AI execution responsibilities
- founder review gates
- dependencies
- acceptance criteria

This document is the operational task board for v0 release.

It does not approve production clinical behavior.

It does not create diagnosis, treatment, medication advice, dosage advice, clinical recommendation, system scoring, disease risk calculation, disease prediction, personalized supplement protocol, personalized nutrition prescription, personalized training prescription, or personalized medical intervention.

---

## 2. Operating Model

Congtie v0 uses an AI-native team workflow.

```text
Founder
(Product direction, judgement, approval)

+

AI Agents
(implementation, documentation, validation, iteration)

=

Congtie AI-native team workflow
```

Short rule:

```text
AI executes.
Human decides.
```

Founder responsibilities:

- product direction
- scope decisions
- evidence judgement
- safety approval
- content approval
- public release approval

AI agent responsibilities:

- implementation
- documentation
- formatting
- validation
- iteration
- consistency checks
- task execution reports

AI agents must not bypass founder gates.

AI agents must not publish automatically.

AI agents must not introduce production clinical logic.

---

## 3. Task Field Definition

Each task should use this schema:

```yaml
task_id:
task_name:
lane:
priority:
status:
owner:
executor:

goal:

input_files:
output_files:

dependencies:

founder_gate:

acceptance_criteria:

notes:
```

Allowed status values:

```text
backlog
ready
in_progress
blocked
review
completed
deferred
cancelled
```

Allowed priority values:

```text
P0
P1
P2
P3
```

Priority meanings:

```text
P0 = Must complete before v0 release
P1 = Important but can adjust
P2 = Future improvement
P3 = Long-term exploration
```

Recommended owner values:

```text
Founder
Congtie Agent Team
Engineering Agent
Knowledge Agent
Product Agent
Safety Reviewer
```

Recommended executor values:

```text
AI Agent
Founder
Human Reviewer
Engineering Agent
Knowledge Agent
```

---

## 4. Release Lanes

The v0 release backlog is organized into four lanes.

### Lane A: User Product

Scope:

- public website
- AI conversation
- user context input
- feedback loop

### Lane B: Longevity Information Library

Scope:

- templates
- knowledge library structure
- validators
- first knowledge batch
- action resources
- progress and viewpoints watchlist

### Lane C: Engineering Infrastructure

Scope:

- knowledge indexes
- Git workflow
- project rename preparation
- deployment stability

### Lane D: v1 Preparation

Scope:

- user health information library schema planning
- personalized longevity agent architecture
- action tracking concept

---

## 5. Task Backlog

## 5.1 Lane A: User Product

### A-001 Website Foundation

```yaml
task_id: A-001
task_name: Website Foundation
lane: User Product
priority: P0
status: backlog
owner: Product Agent
executor: AI Agent

goal: Ensure congtieai.com clearly communicates Congtie positioning, longevity assistant value, non-clinical boundary, and beta invitation.

input_files:
  - agent/roadmap/v0_release_plan_2026_09.md
  - frontend/

output_files:
  - frontend/
  - agent/roadmap/website_foundation_status_2026_09.md

dependencies:
  - product positioning copy
  - current frontend skeleton

founder_gate: Gate 1 Product positioning approval

acceptance_criteria:
  - congtieai.com explains what Congtie is
  - value proposition is clear
  - non-clinical boundary is visible
  - beta invitation path exists
  - no diagnosis or treatment claims

notes: Website should validate user understanding before product completeness.
```

### A-002 AI Conversation Experience

```yaml
task_id: A-002
task_name: AI Conversation Experience
lane: User Product
priority: P0
status: ready
owner: Engineering Agent
executor: AI Agent

goal: Enable users to ask longevity questions, receive explanations, understand sources, and receive safe next action rationale.

input_files:
  - app/
  - agent/knowledge_seed_v0/
  - agent/longevity_knowledge_base/

output_files:
  - app/
  - agent/roadmap/ai_conversation_experience_status_2026_09.md

dependencies:
  - knowledge retrieval
  - safety boundary handling
  - source-aware response pattern

founder_gate: Gate 3 Safety boundary approval

acceptance_criteria:
  - users can ask longevity questions
  - answers use knowledge support when available
  - source-aware explanation is possible
  - missing context reminders work
  - safe next action rationale remains non-clinical
  - no medication, dosage, diagnosis, treatment, or clinical recommendation behavior

notes: This is the core product experience for v0.
```

### A-003 User Context Input

```yaml
task_id: A-003
task_name: User Context Input
lane: User Product
priority: P0
status: backlog
owner: Engineering Agent
executor: AI Agent

goal: Provide minimum user health context capability, including age, goals, lifestyle information, and uploaded documents.

input_files:
  - app/
  - frontend/
  - agent/roadmap/v0_release_plan_2026_09.md

output_files:
  - app/
  - frontend/
  - agent/roadmap/user_context_input_status_2026_09.md

dependencies:
  - user health information library boundary
  - privacy and consent scope

founder_gate: Gate 3 Safety boundary approval

acceptance_criteria:
  - users can provide basic context
  - uploaded health information can be accepted or staged safely
  - conversation can reference user-provided context
  - no full medical record system is created
  - no hidden medical personalization is created

notes: Keep scope deliberately small.
```

### A-004 User Feedback Loop

```yaml
task_id: A-004
task_name: User Feedback Loop
lane: User Product
priority: P1
status: backlog
owner: Product Agent
executor: AI Agent

goal: Collect useful/not useful feedback, missing features, subscription intent, and user expectations.

input_files:
  - frontend/
  - app/

output_files:
  - frontend/
  - app/
  - agent/roadmap/user_feedback_loop_status_2026_09.md

dependencies:
  - website foundation
  - AI conversation experience

founder_gate: Gate 4 Public release approval

acceptance_criteria:
  - user feedback can be collected
  - feedback is traceable
  - feedback fields are simple
  - no sensitive health data is collected unintentionally

notes: Feedback is important for beta learning, but can adjust if release timing is tight.
```

## 5.2 Lane B: Longevity Information Library

### B-001 Knowledge Template

```yaml
task_id: B-001
task_name: Knowledge Template
lane: Longevity Information Library
priority: P0
status: completed
owner: Knowledge Agent
executor: AI Agent

goal: Create standard Markdown template for Longevity Information Library entries.

input_files:
  - agent/roadmap/v0_release_plan_2026_09.md

output_files:
  - agent/longevity_knowledge_base/templates/longevity_knowledge_item_template.v0.1.md

dependencies: []

founder_gate: none

acceptance_criteria:
  - template exists
  - frontmatter fields are defined
  - status workflow is defined
  - agent usage rules are defined
  - validation expectations are defined

notes: Completed foundation task.
```

### B-002 Knowledge Library Structure

```yaml
task_id: B-002
task_name: Knowledge Library Structure
lane: Longevity Information Library
priority: P0
status: ready
owner: Knowledge Agent
executor: AI Agent

goal: Create the directory structure for the Longevity Information Library.

input_files:
  - agent/longevity_knowledge_base/templates/longevity_knowledge_item_template.v0.1.md
  - agent/roadmap/v0_release_plan_2026_09.md

output_files:
  - agent/longevity_knowledge_base/entries/
  - agent/longevity_knowledge_base/entries/knowledge/
  - agent/longevity_knowledge_base/entries/action_resources/
  - agent/longevity_knowledge_base/entries/progress_and_viewpoints/
  - agent/longevity_knowledge_base/entries/education/
  - agent/longevity_knowledge_base/entries/governance/
  - agent/longevity_knowledge_base/entries/invalid_or_harmful/
  - agent/longevity_knowledge_base/schemas/
  - agent/longevity_knowledge_base/indexes/
  - agent/longevity_knowledge_base/review_logs/

dependencies:
  - B-001

founder_gate: none

acceptance_criteria:
  - expected folders exist
  - future entries use entries/<information_layer>/ as the only canonical path
  - legacy top-level layer directories are not used for new entries
  - README explains folder purpose
  - no runtime code is changed
  - no schema enforcement is introduced unless separately approved

notes: This task prepares file organization only.
```

### B-003 Validator

```yaml
task_id: B-003
task_name: Validator
lane: Longevity Information Library
priority: P0
status: ready
owner: Knowledge Agent
executor: AI Agent

goal: Create validation script for knowledge items.

input_files:
  - agent/longevity_knowledge_base/templates/longevity_knowledge_item_template.v0.1.md

output_files:
  - agent/longevity_knowledge_base/validate_longevity_knowledge_items.py
  - agent/roadmap/knowledge_validator_status_2026_09.md

dependencies:
  - B-001
  - B-002

founder_gate: none

acceptance_criteria:
  - validates frontmatter completeness
  - validates entry_id format
  - validates topic_id validity
  - validates status validity
  - validates evidence fields
  - validates safety boundary
  - validates commercial boundary
  - accumulates all errors before exit
  - uses only Python standard library unless separately approved

notes: Validator should be lightweight and Git-friendly.
```

### B-004 First Knowledge Batch

```yaml
task_id: B-004
task_name: First Knowledge Batch
lane: Longevity Information Library
priority: P0
status: ready
owner: Knowledge Agent
executor: AI Agent

goal: Create first 50-100 high-value knowledge entries.

input_files:
  - agent/longevity_knowledge_base/templates/longevity_knowledge_item_template.v0.1.md
  - agent/knowledge_seed_v0/
  - agent/roadmap/v0_release_plan_2026_09.md

output_files:
  - agent/longevity_knowledge_base/entries/knowledge/
  - agent/roadmap/first_knowledge_batch_status_2026_09.md

dependencies:
  - B-001
  - B-002
  - B-003

founder_gate: Gate 2 Knowledge content approval

acceptance_criteria:
  - 50-100 entries exist or a founder-approved reduced batch exists
  - priority topics are covered
  - entries include metadata
  - entries preserve non-clinical boundary
  - entries are reviewable
  - published entries require human approval

notes: Priority order: T01 Longevity Foundation, T02 Longevity Strategy, T03 Body Systems, T04 Measurement, T05 Lifestyle.
```

### B-005 Action Resource Seed

```yaml
task_id: B-005
task_name: Action Resource Seed
lane: Longevity Information Library
priority: P1
status: backlog
owner: Knowledge Agent
executor: AI Agent

goal: Create low-risk action resources such as records, tracking tools, measurement devices, and education resources.

input_files:
  - agent/knowledge_seed_v0/topics/action_resources/
  - agent/knowledge_seed_v0/action_resource_index.v0.1.json
  - agent/knowledge_seed_v0/action_resource_p0_closeout.v0.1.md

output_files:
  - agent/longevity_knowledge_base/entries/action_resources/
  - agent/roadmap/action_resource_seed_status_2026_09.md

dependencies:
  - B-002
  - B-003

founder_gate: Gate 2 Knowledge content approval

acceptance_criteria:
  - low-risk resources are represented
  - R0/R1/R2/R3 boundaries are preserved
  - no product purchase recommendations are added
  - no clinical recommendation behavior is introduced

notes: Existing Knowledge Seed v0 action resources should be reused conservatively.
```

### B-006 Progress and Viewpoints Watchlist

```yaml
task_id: B-006
task_name: Progress and Viewpoints Watchlist
lane: Longevity Information Library
priority: P2
status: backlog
owner: Knowledge Agent
executor: AI Agent

goal: Create initial emerging longevity topics watchlist.

input_files:
  - agent/knowledge_seed_v0/longevity_topic_taxonomy.v0.1.md

output_files:
  - agent/longevity_knowledge_base/entries/progress_and_viewpoints/
  - agent/roadmap/progress_and_viewpoints_watchlist_status_2026_09.md

dependencies:
  - B-002
  - B-003

founder_gate: Gate 2 Knowledge content approval

acceptance_criteria:
  - initial watchlist exists
  - topics are marked education-only
  - no direct action recommendation is created
  - emerging topics remain non-clinical

notes: Example topics: biological aging research, AI4S, biomarkers, longevity biotechnology.
```

## 5.3 Lane C: Engineering Infrastructure

### C-001 Knowledge Index Generator

```yaml
task_id: C-001
task_name: Knowledge Index Generator
lane: Engineering Infrastructure
priority: P0
status: ready
owner: Engineering Agent
executor: AI Agent

goal: Generate retrieval indexes from Markdown knowledge items.

input_files:
  - agent/longevity_knowledge_base/entries/
  - agent/longevity_knowledge_base/templates/longevity_knowledge_item_template.v0.1.md

output_files:
  - agent/longevity_knowledge_base/indexes/
  - agent/roadmap/knowledge_index_generator_status_2026_09.md

dependencies:
  - B-002
  - B-003
  - B-004

founder_gate: none

acceptance_criteria:
  - indexes can be generated deterministically
  - draft/published status is respected
  - runtime_enabled and retrieval_enabled are respected
  - invalid entries are skipped or fail clearly
  - output is reviewable in Git

notes: Index generation must not silently publish content.
```

### C-002 Git Workflow

```yaml
task_id: C-002
task_name: Git Workflow
lane: Engineering Infrastructure
priority: P0
status: backlog
owner: Engineering Agent
executor: AI Agent

goal: Ensure Markdown to validation to Git commit to published index workflow is clear.

input_files:
  - agent/longevity_knowledge_base/
  - agent/roadmap/v0_release_plan_2026_09.md

output_files:
  - agent/roadmap/git_workflow_status_2026_09.md
  - agent/longevity_knowledge_base/README.md

dependencies:
  - B-002
  - B-003
  - C-001

founder_gate: none

acceptance_criteria:
  - workflow is documented
  - validation step is clear
  - review step is clear
  - publishing step requires human approval
  - rollback path is clear

notes: Markdown -> Validation -> Git commit -> Published index.
```

### C-003 Rename Project Directory

```yaml
task_id: C-003
task_name: Rename Project Directory
lane: Engineering Infrastructure
priority: P1
status: backlog
owner: Engineering Agent
executor: AI Agent

goal: Prepare migration from xiaoge-api to congtie-api.

input_files:
  - README.md
  - scripts/
  - app/
  - tests/
  - spec/
  - agent/

output_files:
  - agent/roadmap/project_rename_plan_2026_09.md

dependencies:
  - brand naming decisions

founder_gate: Product direction approval

acceptance_criteria:
  - references are scanned
  - path dependencies are documented
  - documentation updates are planned
  - build/test verification plan exists
  - no unsafe mass rename is performed without approval

notes: This is preparation only unless founder explicitly approves execution.
```

### C-004 Deployment Stability

```yaml
task_id: C-004
task_name: Deployment Stability
lane: Engineering Infrastructure
priority: P0
status: backlog
owner: Engineering Agent
executor: AI Agent

goal: Ensure v0 beta deployment reliability.

input_files:
  - app/
  - frontend/
  - agent/roadmap/v0_release_plan_2026_09.md

output_files:
  - agent/roadmap/deployment_stability_status_2026_09.md

dependencies:
  - website foundation
  - AI conversation experience
  - current deployment topology

founder_gate: Gate 4 Public release approval

acceptance_criteria:
  - deployment path is documented
  - smoke checks pass
  - rollback notes exist
  - public beta environment is stable enough for founder-approved launch

notes: Do not change production deployment config without founder approval.
```

## 5.4 Lane D: v1 Preparation

### D-001 User Health Information Library Schema

```yaml
task_id: D-001
task_name: User Health Information Library Schema
lane: v1 Preparation
priority: P1
status: backlog
owner: Knowledge Agent
executor: AI Agent

goal: Define future private health data model without implementation.

input_files:
  - agent/roadmap/v0_release_plan_2026_09.md
  - agent/knowledge_seed_v0/user_health_information_library_spec.v0.1.md

output_files:
  - agent/roadmap/user_health_information_library_schema_plan_2026_09.md

dependencies:
  - user context boundary decisions

founder_gate: Safety boundary approval

acceptance_criteria:
  - future data model scope is defined
  - no implementation is created
  - private user data boundary is preserved
  - no clinical interpretation engine is introduced

notes: This task prepares v1 architecture only.
```

### D-002 Personalized Longevity Agent Architecture

```yaml
task_id: D-002
task_name: Personalized Longevity Agent Architecture
lane: v1 Preparation
priority: P1
status: backlog
owner: Product Agent
executor: AI Agent

goal: Define model + harness + longevity information library + user health information library architecture.

input_files:
  - agent/roadmap/v0_release_plan_2026_09.md

output_files:
  - agent/roadmap/personalized_longevity_agent_architecture_2026_09.md

dependencies:
  - D-001
  - knowledge retrieval architecture

founder_gate: Product direction approval

acceptance_criteria:
  - future architecture is described
  - v0/v1 boundary is clear
  - no production personalization is implemented
  - no clinical decision support is introduced

notes: This is v1 preparation, not v0 implementation.
```

### D-003 Action Tracking Concept

```yaml
task_id: D-003
task_name: Action Tracking Concept
lane: v1 Preparation
priority: P2
status: backlog
owner: Product Agent
executor: AI Agent

goal: Define future tasks, reminders, and execution tracking concept.

input_files:
  - agent/roadmap/v0_release_plan_2026_09.md

output_files:
  - agent/roadmap/action_tracking_concept_2026_09.md

dependencies:
  - action resource governance
  - user context boundary decisions

founder_gate: Product direction approval

acceptance_criteria:
  - concept is documented
  - permission boundaries are preserved
  - no autonomous action execution is introduced
  - no clinical action plan is introduced

notes: Future capability only.
```

---

## 6. Milestones

### 6.1 August 2026

Focus:

- release plan
- backlog
- knowledge infrastructure
- first content migration

Target tasks:

```text
B-001 Knowledge Template
B-002 Knowledge Library Structure
B-003 Validator
B-004 First Knowledge Batch
C-001 Knowledge Index Generator
```

### 6.2 Early September 2026

Focus:

- internal beta
- user testing
- AI conversation refinement

Target tasks:

```text
A-002 AI Conversation Experience
A-003 User Context Input
C-004 Deployment Stability
```

### 6.3 Mid September 2026

Focus:

- founder daily usage
- content improvement
- safety testing

Target tasks:

```text
A-001 Website Foundation
A-004 User Feedback Loop
B-004 First Knowledge Batch refinement
C-002 Git Workflow
```

### 6.4 Late September 2026

Focus:

- public beta release

Target tasks:

```text
Gate 4 Public release approval
Website public readiness
AI assistant public readiness
Knowledge access public readiness
Feedback loop readiness
```

---

## 7. Founder Review Gates

### Gate 1: Product Positioning Approval

Required before:

- public website positioning is finalized
- beta invitation language is published
- public-facing claims are locked

Review focus:

- what Congtie is
- what Congtie is not
- target user clarity
- value proposition clarity
- non-clinical boundary clarity

### Gate 2: Knowledge Content Approval

Required before:

- knowledge entries are marked approved
- knowledge entries are published
- action resources are used in public-facing flows

Review focus:

- evidence posture
- source quality
- safety boundaries
- topic mapping
- commercial neutrality

### Gate 3: Safety Boundary Approval

Required before:

- AI conversation is exposed to beta users
- user context is used in responses
- next action rationale is displayed

Review focus:

- no diagnosis
- no treatment
- no medication advice
- no dosage advice
- no clinical recommendation
- no disease risk calculation
- no personalized supplement protocol
- safe handling of urgent or high-risk user inputs

### Gate 4: Public Release Approval

Required before:

- public beta launch
- public traffic invitation
- external user onboarding

Review focus:

- product readiness
- safety readiness
- deployment readiness
- content readiness
- feedback loop readiness

---

## 8. Current Priorities

Initial active P0 queue:

```text
B-002 Knowledge Library Structure
B-003 Validator
B-004 First Knowledge Batch
A-002 AI Conversation Experience
C-001 Knowledge Index Generator
```

Initial active P1 queue:

```text
D-001 User Health Information Library Schema
C-003 Project Rename
```

Recommended execution order:

```text
1. B-002 Knowledge Library Structure
2. B-003 Validator
3. B-004 First Knowledge Batch
4. C-001 Knowledge Index Generator
5. A-002 AI Conversation Experience
6. A-003 User Context Input
7. C-004 Deployment Stability
8. A-001 Website Foundation
```

---

## 9. Deferred Tasks

Deferred from v0:

```text
full CMS
automatic knowledge ingestion
MCP ecosystem
autonomous publishing
personalized supplement protocol
medical decision engine
```

Additional deferred items:

- complete external API ecosystem
- external Agent marketplace
- full medical record system
- biological age scoring
- disease risk calculators
- advanced action execution agent
- automatic evidence approval

---

## 10. Risks

### 10.1 Scope Expansion

Risk:

```text
v0 attempts to become too complete.
```

Mitigation:

- keep P0 list small
- preserve deferred list
- require founder gates for scope expansion

### 10.2 Insufficient Founder Review Time

Risk:

```text
knowledge and safety review bottlenecks delay release.
```

Mitigation:

- batch review
- clear review packets
- AI pre-review summaries
- explicit approval gates

### 10.3 Content Quality Bottleneck

Risk:

```text
first knowledge batch is too thin, inconsistent, or poorly sourced.
```

Mitigation:

- use template
- run validator
- prioritize high-value topics
- keep release scope to 50-100 entries

### 10.4 AI Hallucination

Risk:

```text
AI responses overstate evidence or invent unsupported claims.
```

Mitigation:

- source-aware responses
- safety boundary checks
- non-clinical guardrails
- human-reviewed knowledge entries

### 10.5 Inconsistent Source Quality

Risk:

```text
sources vary in authority, stability, or relevance.
```

Mitigation:

- evidence metadata
- source notes
- source review workflow
- future source manifest

### 10.6 Delayed User Feedback

Risk:

```text
release team does not learn fast enough from beta users.
```

Mitigation:

- simple feedback loop
- daily founder usage
- beta issue log
- lightweight iteration cadence

---

## 11. Naming Rules

Use:

```text
Congtie
```

as display name.

Use:

```text
congtie
```

for:

```text
code
paths
domains
```

Do not use the deprecated camel-case brand spelling.

---

## 12. Final Note

This backlog should help Congtie move from strategy to execution without losing the v0 boundary.

The operating principle is:

```text
AI executes.
Human decides.
Ship the smallest trustworthy Public Beta.
```
