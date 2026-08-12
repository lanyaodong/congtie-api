# User Health Information Library MVP Specification v0.1

Version: v0.1  
Project: Congtie  
Status: Draft  
Owner: Congtie Agent Team  
Last Updated: 2026-08-07

---

## 1. Purpose

This document defines the minimum product specification for the Congtie User Health Information Library.

The User Health Information Library is the private, user-specific context foundation for future personalization.

This specification defines:

- product definition
- relationship with the Longevity Information Library
- product principles
- v0 MVP scope
- data categories
- conceptual MVP fields
- privacy principles
- permission model
- AI agent usage boundaries
- safety boundaries
- conceptual storage architecture
- future v1 expansion direction

This document is a planning specification only.

It does not create:

- a database schema
- a persistent user data model
- database migrations
- runtime storage
- API contracts
- loaders or validators
- external integrations
- production personalization logic

Any implementation of a schema, database, persistent user data model, external provider integration, or production user-data workflow requires a separate Founder Gate review.

---

## 2. One-line Definition

User Health Information Library is:

> A private, user-controlled, permission-based health context library that helps Congtie understand the user's background, goals, records, and actions to provide personalized explanation and safe action support.

Chinese product term:

```text
用户健康信息库
```

It is a user-controlled health context layer.

It is not:

- an electronic medical record system
- a hospital information system
- a clinical decision support system
- a diagnosis engine
- a treatment engine
- a medication management system
- a disease prediction system

---

## 3. Relationship with Longevity Information Library

Congtie requires two separate information foundations.

```text
                           Congtie Agent
                                 |
                --------------------------------
                |                              |
   Longevity Information Library   User Health Information Library
                |                              |
       General knowledge                 Private user context
       Evidence                          Personal records
       Global longevity information      My body information and history
```

The relationship is:

```text
Longevity Information Library
= general, reusable, versioned information

User Health Information Library
= private, user-specific, permission-gated health context
```

The Longevity Information Library may contain:

- stable longevity knowledge
- evidence summaries
- action resources
- progress and viewpoints
- education materials
- source references
- governance and curation rules
- safety boundaries

The User Health Information Library may contain:

- user profile context
- user goals
- lifestyle context
- biomarker records
- health report metadata
- action history
- conversation context
- permissions

Congtie may combine the two foundations only within approved runtime safety and user-permission boundaries.

General knowledge must not be silently transformed into personalized medical advice.

Private user context must not be copied into the general Longevity Information Library.

---

## 4. Product Principles

### 4.1 User Ownership

The user owns:

- their data
- their permissions
- their sharing decisions
- their export decisions
- their deletion decisions

The system should make it clear:

- what information is stored
- why it is stored
- how it may be used
- which agent or service may access it
- whether it has been shared
- how the user can revoke access

### 4.2 Privacy First

The product direction must support:

- data minimization
- purpose-limited collection
- user-visible permissions
- export
- deletion
- sharing control
- access revocation
- separation of private context from general knowledge

Private health context must not be used for hidden commercial targeting.

Private health context must not be shared with external parties without explicit user permission.

### 4.3 Context, Not Diagnosis

The library provides context.

It does not automatically produce:

- diagnosis
- treatment
- medication decisions
- dosage advice
- clinical recommendations
- disease risk calculations
- disease predictions
- system scores
- personalized supplement protocols
- personalized medical interventions

### 4.4 Minimum Necessary Context

Congtie should collect only context that has a clear user-facing purpose.

The system should avoid collecting sensitive information merely because it may be useful later.

### 4.5 Source and Time Awareness

Health context should preserve source and time information where relevant.

Examples:

- measurement date
- report date
- user-provided date
- source device
- source laboratory
- uploaded document reference
- whether information is user-reported

The system must not guess missing dates, units, sources, or reference ranges.

### 4.6 Transparent AI Use

Users should understand when private context is used by an AI agent and for what purpose.

Agent access should be permission-based, scoped, and revocable where applicable.

### 4.7 Non-clinical by Default

All v0 use remains non-clinical.

Stored information does not become a clinical conclusion simply because it is structured or longitudinal.

---

## 5. v0 MVP Scope

v0 should define and later support the minimum usable health context needed for bounded personalization.

The MVP scope contains seven categories:

```text
1. User Profile
2. User Goals
3. Lifestyle Context
4. Biomarker Information
5. Health Reports
6. Action History
7. Conversation Context
```

Permissions apply across all categories.

The v0 product intent is to support:

- user-provided context collection
- basic health record organization
- preservation of source and date metadata
- reduction of repeated questions
- missing-context explanation
- personalized educational explanation
- low-risk next information collection
- continuity across user-directed tasks

The v0 product intent is not to support:

- full medical record management
- clinical interpretation
- healthcare interoperability
- hospital integration
- insurance integration
- medication management
- automated treatment planning
- full personalized longevity protocols

---

## 6. Data Categories

### 6.1 User Profile

Purpose:

- provide basic user background
- reduce repeated baseline questions
- improve relevance of non-clinical explanations

Conceptual MVP fields:

```yaml
user_id:
age:
sex:
height:
weight:
body_composition:
location:
occupation_optional:
health_goal:
```

Notes:

- `occupation_optional` is optional and should be collected only when relevant.
- `body_composition` is contextual data, not a diagnosis or system score.
- Profile fields must not be used to infer disease or calculate clinical risk.

### 6.2 User Goals

Purpose:

- preserve user-stated goals
- help prioritize relevant education and low-risk context collection
- support continuity across conversations

Conceptual MVP fields:

```yaml
goals:
  - extend_healthspan
  - maintain_capability
  - improve_energy
  - improve_sleep
  - improve_fitness
priority_dimensions:
  - sleep
  - nutrition
  - exercise
  - stress
```

Canonical lifestyle order:

```text
睡眠 / 营养 / 锻炼 / 压力
sleep / nutrition / exercise / stress
```

Goals may guide explanation and information organization.

Goals must not be converted into clinical plans, treatment plans, personalized supplement protocols, personalized nutrition prescriptions, or personalized training prescriptions.

### 6.3 Lifestyle Context

Purpose:

- help Congtie understand user habits
- provide context for non-clinical explanation
- identify missing lifestyle background
- support low-risk trend observation

Conceptual MVP fields:

```yaml
sleep_context:
nutrition_context:
exercise_context:
stress_context:
```

Possible contextual content includes:

- sleep timing, duration, regularity, and subjective quality
- meal patterns, hydration, protein context, fiber context, and alcohol context
- exercise type, frequency, duration, and subjective effort
- perceived stress, work context, family context, and recovery pressure

Lifestyle context does not create medical judgment.

It must not be used to diagnose sleep disorders, prescribe disease diets, generate training prescriptions, provide rehabilitation plans, or diagnose mental health conditions.

### 6.4 Biomarker Information

Purpose:

- store user-provided measurements
- preserve source and time metadata
- support record organization
- support missing-context explanation

Examples:

- blood markers
- body composition measurements
- wearable summaries

Conceptual MVP fields:

```yaml
biomarker_id:
name:
value:
unit:
measurement_date:
source:
notes:
```

Important boundary:

```text
Storage and organization only.
```

Biomarker information must not automatically produce:

- diagnosis
- clinical interpretation
- disease prediction
- disease risk calculation
- system scoring
- treatment advice
- medication advice
- personalized supplement protocol

If unit, measurement date, or source is missing, Congtie should identify the limitation instead of guessing.

This specification does not modify or replace any biomarker map JSON.

### 6.5 Health Reports

Purpose:

- preserve references to user-provided reports
- support report organization
- maintain source and date context
- support preparation for professional consultation

Examples:

- laboratory reports
- physical examination reports
- uploaded documents
- device exports

Conceptual MVP fields:

```yaml
report_id:
report_type:
source:
date:
file_location:
user_notes:
```

`file_location` is a conceptual reference field. This document does not define a storage provider, filesystem contract, URL format, or database representation.

Uploaded reports remain user-provided context.

They must not be treated as a new diagnosis or used to generate treatment, medication changes, risk calculations, or personalized protocols.

### 6.6 Action History

Purpose:

- preserve user-directed action continuity
- reduce repeated instructions
- help users understand what they have already done
- support future feedback loops

Conceptual MVP fields:

```yaml
action_id:
action_type:
start_date:
status:
notes:
```

Examples:

- started strength training
- changed sleep schedule
- started tracking nutrition
- uploaded a health report
- prepared questions for a professional consultation

Action history records what the user reports or confirms.

It must not be used to infer treatment effect, clinical improvement, disease risk reduction, or system score changes.

### 6.7 Conversation Context

Purpose:

- preserve user preferences
- remember important user-provided background
- maintain continuity around user goals and questions
- reduce unnecessary repetition

Conceptual MVP content:

```text
user preferences
important background
previous goals
user questions
```

Conversation context must not store hidden medical conclusions.

It must not treat a user question as evidence of a diagnosis.

It must not store hidden chain-of-thought.

---

## 7. Data Structure

The following structure is conceptual and non-executable.

It describes the minimum data shape needed for product review. It is not an approved schema, database model, API contract, or persistence format.

```yaml
user_health_information_library:
  user_id:
  profile:
    age:
    sex:
    height:
    weight:
    body_composition:
    location:
    occupation_optional:
    health_goal:
  goals:
    goals: []
    priority_dimensions: []
  lifestyle:
    sleep_context:
    nutrition_context:
    exercise_context:
    stress_context:
  biomarkers: []
  reports: []
  actions: []
  conversations: []
  permissions:
    read_permission:
    write_permission:
    export_permission:
    delete_permission:
    agent_usage_permission:
    external_sharing_permission:
```

Each stored object should eventually preserve, where relevant:

```yaml
record_id:
user_id:
source:
observed_at:
created_at:
updated_at:
user_confirmed:
notes:
```

Data-quality principles:

- do not guess missing values
- distinguish user-reported data from report-derived or device-derived data
- preserve source information where possible
- preserve date information where possible
- allow correction by the user
- represent missing context explicitly

Before engineering implementation, Congtie requires separate approval for:

- field types
- required versus optional fields
- identifiers
- persistence model
- encryption strategy
- access-control implementation
- retention policy
- deletion workflow
- API representation
- audit model

---

## 8. User Permission Model

The user controls access to private health context.

Minimum permission concepts:

```text
read permission
write permission
export permission
delete permission
agent usage permission
external sharing permission
```

### 8.1 Read Permission

Controls whether an approved Congtie component may retrieve selected user context.

Read access should be scoped by purpose and data category.

### 8.2 Write Permission

Controls whether the user or an approved component may create or update selected context.

AI-generated extraction should not silently overwrite original user data.

### 8.3 Export Permission

The user should be able to request an export of selected information.

Future implementation must define export formats and delivery security separately.

### 8.4 Delete Permission

The user should be able to delete selected records or request deletion of their library.

Future implementation must define retention, backup, recovery, and legal requirements separately.

### 8.5 Agent Usage Permission

An AI agent must require permission before using private context.

Permission should identify:

- the purpose
- the selected data scope
- the agent or feature using it
- whether the permission is one-time or ongoing
- whether and how it may be revoked

### 8.6 External Sharing Permission

No external sharing should occur without explicit user permission.

The user should know:

- what will be shared
- who or what will receive it
- why it will be shared
- whether future access continues
- how to revoke future access where applicable

### 8.7 Permission Defaults

Recommended product defaults:

```text
private by default
no external sharing by default
no broad agent access by default
no hidden commercial use
purpose-limited access
minimum necessary data scope
```

This document defines permission concepts only. It does not implement authentication, authorization, consent records, or access-control policy.

---

## 9. AI Agent Usage Rules

### 9.1 AI May

With appropriate user permission, the AI agent may:

- read approved user context
- reduce repeated questions
- explain missing context
- personalize educational explanations
- suggest low-risk next information collection
- organize user-provided records
- preserve continuity around user goals
- prepare a non-clinical summary
- help prepare questions for a clinician or other qualified professional

### 9.2 AI Must

The AI agent must:

- use only context within the approved permission scope
- explain important data limitations
- distinguish general information from private user context
- avoid guessing missing dates, units, sources, or values
- preserve non-clinical safety boundaries
- request user confirmation before sharing or exporting private context
- respect revoked or expired permission
- avoid using private context for hidden commercial targeting

### 9.3 AI Must Not

The AI agent must not:

- diagnose disease
- prescribe treatment
- recommend medication
- provide dosage advice
- provide clinical recommendations
- provide personalized supplement protocols
- provide personalized nutrition prescriptions
- provide personalized training prescriptions
- calculate disease risk
- predict disease
- calculate system scores
- replace clinicians
- perform emergency assessment or triage
- infer consent from prior unrelated conversations
- share context with another agent or external service without explicit permission

### 9.4 Bounded Personalization

v0 personalization may affect:

- which missing context question is shown
- which educational explanation is most relevant
- which records should be organized next
- which low-risk tracking category may be useful
- which questions the user may wish to prepare for a professional

v0 personalization must not affect:

- diagnosis
- treatment
- medication or dosage
- clinical decisions
- disease risk scores
- system scores
- disease predictions
- supplement protocols
- medical interventions

---

## 10. Safety Boundaries

The User Health Information Library does not transform stored data into:

```text
diagnosis
treatment plan
medication recommendation
dosage advice
clinical decision
clinical recommendation
emergency assessment
system scoring
disease risk calculation
disease prediction
personalized supplement protocol
personalized nutrition prescription
personalized training prescription
personalized medical intervention
```

Additional v0 boundaries:

- A single biomarker does not establish a diagnosis.
- A report does not authorize Congtie to reinterpret clinician conclusions.
- Longitudinal data does not authorize disease prediction or clinical risk calculation.
- User goals do not authorize treatment, nutrition, training, or supplement prescriptions.
- Action history does not prove a treatment effect.
- Conversation history does not imply medical consent.
- Emergency concerns require real-world professional or emergency support; the library is not a triage engine.

Medication information, if later collected, may be retained only as user-provided context for record organization and safety reminders. Congtie v0 must not recommend starting, stopping, changing, combining, or dosing medication.

Supplement information, if later collected, must not be used to create dosage, timing, cycle, loading phase, stack, or personalized protocol advice.

---

## 11. Storage Architecture

The conceptual MVP structure is:

```text
user_health_information/
├── profile/
├── goals/
├── biomarkers/
├── reports/
├── lifestyle/
├── actions/
├── conversations/
└── permissions/
```

This tree describes logical ownership and separation only.

It does not require local filesystem storage and must not be interpreted as an approved production directory, database, bucket, or service design.

v0 focuses on:

```text
conceptual data shape
user-controlled storage principles
basic retrieval boundaries
permission concepts
```

v0 does not define:

```text
full healthcare interoperability
hospital integration
insurance data integration
medical workflow
production database schema
database technology
cloud storage provider
encryption implementation
retention implementation
external data provider
```

Storage design principles for future implementation:

- private by default
- separate private user context from general knowledge
- least-privilege access
- purpose-limited retrieval
- user-visible export and deletion controls
- no private user data committed to general repo knowledge files
- no secrets or provider credentials committed to the repo
- auditable access without exposing hidden chain-of-thought

Any production storage architecture, database model, persistent user data model, or external integration is subject to a separate Founder Gate.

---

## 12. Future v1 Expansion

v1 may expand only after privacy, safety, consent, and implementation review.

### 12.1 Data Integration

Possible future directions:

- wearable APIs
- continuous glucose monitoring context
- health platform imports
- laboratory integrations
- structured report extraction
- user-authorized device imports

These are future candidates, not approved integrations.

### 12.2 Longitudinal Tracking

Possible future directions:

- trends over time
- goal progress
- action follow-up
- user feedback
- source freshness
- record correction history
- permission and access history

Trend tracking must not become disease prediction, risk calculation, clinical scoring, or treatment evaluation without separate approval.

### 12.3 Expanded User Controls

Possible future controls:

- view
- edit
- correct
- export
- delete
- share
- revoke
- pause personalization
- inspect access history

### 12.4 Personalized Longevity Agent

Future architecture direction:

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

This direction supports safer relevance and continuity.

It does not authorize clinical decision support, diagnosis, treatment, medication management, disease prediction, or personalized medical intervention.

### 12.5 Required Reviews Before v1 Implementation

Future implementation should separately review:

- privacy and consent
- security and encryption
- data retention and deletion
- access control
- auditability
- regulatory and legal requirements
- external integration risk
- data provenance and correction
- safety behavior
- product claims

---

## 13. Non-goals

Congtie v0 does not build:

- an electronic medical record system
- a hospital medical record replacement
- a clinical decision support system
- a diagnosis engine
- a treatment engine
- medication management
- dosage management
- a disease prediction system
- a disease risk calculator
- a body-system scoring engine
- an insurance platform
- a healthcare provider system
- a hospital integration
- full healthcare interoperability
- an emergency triage engine
- a personalized supplement protocol engine
- a personalized nutrition prescription engine
- a personalized training prescription engine
- a personalized medical intervention engine
- hidden commercial targeting
- broad agent-to-agent health-data sharing
- automatic external sharing
- production persistent storage through this document

This specification does not approve:

- database schema creation
- persistent user data models
- API contract changes
- runtime context integration
- external provider integrations
- biomarker JSON changes
- production clinical logic

---

## 14. Acceptance Criteria

This document is acceptable when:

- It clearly separates public general knowledge from private user context.
- It defines the User Health Information Library as private, user-controlled, and permission-based.
- It defines the minimum v0 user health context scope.
- It covers user profile, goals, lifestyle context, biomarkers, reports, action history, and conversation context.
- It preserves the canonical lifestyle order: sleep / nutrition / exercise / stress.
- It defines conceptual MVP fields without creating an executable schema.
- It defines user ownership and privacy principles.
- It defines read, write, export, delete, agent usage, and external sharing permission concepts.
- It requires permission before AI uses private context.
- It defines allowed AI uses for context completion and educational explanation.
- It preserves the non-clinical boundary.
- It does not authorize diagnosis, treatment, medication advice, dosage advice, clinical recommendation, system scoring, disease risk calculation, disease prediction, personalized supplement protocol, personalized nutrition prescription, personalized training prescription, or personalized medical intervention.
- It supports future development of a personalized longevity agent without overbuilding v0.
- It states that production schema, persistent storage, and external integrations require separate review.
- It uses `Congtie` as the display name.
- It uses `congtie` only for lowercase/code/domain contexts.
- It does not use the deprecated camel-case brand spelling.

---

## Final Note

The User Health Information Library is the private context foundation for future Congtie personalization.

The safest v0 principle is:

```text
General longevity knowledge stays in the Longevity Information Library.
Private user context stays in the User Health Information Library.
The user owns the data and permissions.
The AI uses only approved context for bounded, non-clinical support.
```
