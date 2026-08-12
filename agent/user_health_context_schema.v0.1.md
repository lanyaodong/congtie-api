# User Health Context Schema v0.1

Version: v0.1  
Project: Congtie  
Status: Draft  
Owner: Congtie Agent Team  
Last Updated: 2026-08-07  
Founder Gate: Approved for documentation-only conceptual schema on 2026-08-07

---

## 1. Purpose

This document defines the v0.1 conceptual schema for Congtie User Health Context.

It describes:

- the MVP data model
- data categories
- field definitions
- privacy principles
- permission boundaries
- AI agent usage rules
- safety boundaries
- storage principles
- future v1 expansion

User Health Context is the private information foundation that may help Congtie understand a user's background, goals, records, habits, actions, and preferences.

This document is a documentation-only conceptual schema.

It does not create:

- an executable JSON Schema
- a database
- a database model
- migrations
- persistent storage
- API contracts
- runtime integration
- healthcare interoperability
- external data integrations
- frontend behavior

Any implementation of persistent user data, database models, API contracts, external integrations, or production agent access requires a separate task and any applicable Founder Gate approval.

---

## 2. One-line Definition

> User Health Context is a private, user-controlled and permission-based information layer that stores personal health background, goals, records and actions to support personalized explanation and safe action support.

Chinese product relationship:

```text
User Health Context is the minimum private context model within 用户健康信息库.
```

It is not an electronic medical record system, clinical decision system, diagnosis system, or treatment system.

---

## 3. Relationship with Longevity Information Library

Congtie has two separate information foundations.

```text
                              Congtie Agent
                                    |
                  --------------------------------
                  |                              |
     Longevity Information Library        User Health Context
                  |                              |
          General knowledge                Personal context
          Global evidence                  My records
          Public information               Private information
                  |                              |
                  --------------------------------
                                    |
                                    v
                  Personalized explanation and safe action support
```

The separation is:

```text
Longevity Information Library
= general, reusable, public, versioned information

User Health Context
= private, user-specific, permission-gated information
```

The Longevity Information Library may contain:

- general longevity knowledge
- evidence summaries
- action resources
- education materials
- progress and viewpoints
- governance and curation rules
- safety boundaries

User Health Context may contain:

- user profile information
- user goals
- user-provided biomarker records
- user-provided health report references
- lifestyle context
- action history
- conversation context
- permissions

Congtie may combine the two only within approved safety, privacy, and user-permission boundaries.

Private User Health Context must not be committed into the public Longevity Information Library or its Git-managed knowledge entries.

General longevity information must not be silently converted into personalized medical advice when combined with private context.

---

## 4. Design Principles

### 4.1 User Ownership

The user owns:

- their data
- their permissions
- their sharing decisions

Future implementations should make it possible for the user to understand:

- what is stored
- why it is stored
- how it is used
- which agent or service may access it
- what has been shared
- how permission can be revoked

### 4.2 Privacy First

The design should support future:

- export
- deletion
- sharing control
- access revocation
- correction
- access history

Private information should be private by default.

The system should collect only information needed for an explicit user-facing purpose.

Private context must not be used for hidden commercial targeting or undisclosed third-party sharing.

### 4.3 Context, Not Diagnosis

Stored information provides context.

It does not automatically create:

- diagnosis
- treatment
- medication advice
- dosage advice
- clinical recommendation
- disease risk calculation
- disease prediction
- system scoring
- personalized supplement protocol
- personalized medical intervention

### 4.4 Explicit Permission

Agent access and sharing must be based on explicit, scoped permission.

Prior conversation, data upload, or general acceptance of product terms must not be treated as unlimited consent for future agent use or external sharing.

### 4.5 Data Minimization

Only the minimum context needed for the stated purpose should be collected or retrieved.

Optional fields should remain optional unless a future approved workflow establishes a clear need.

### 4.6 Provenance and Time

Records should preserve source and date information where relevant.

Congtie must not guess missing dates, units, sources, or values.

User-reported information should remain distinguishable from report-derived, laboratory-derived, or device-derived information.

### 4.7 Reversible and Reviewable

Future storage and agent use should support correction, deletion, revocation, and auditability.

AI-generated extraction must not silently overwrite original user-provided records.

### 4.8 Non-clinical by Default

Structuring or retaining information does not convert it into a clinical conclusion.

Longitudinal records do not authorize clinical scoring, risk calculation, treatment evaluation, or disease prediction.

---

## 5. v0 MVP Data Model

The v0 MVP model contains eight categories:

```text
profile
goals
biomarkers
reports
lifestyle
actions
conversations
permissions
```

The following YAML illustrates the conceptual shape only.

It is not an executable schema, persistence format, API contract, or validation contract.

```yaml
user_health_context:
  profile:
    user_id:
    age:
    sex:
    height:
    weight:
    body_composition:
    location:
    occupation:

  goals:
    goals: []
    healthspan_goal:
    priority_dimensions:
      - sleep
      - nutrition
      - exercise
      - stress

  biomarkers: []

  reports: []

  lifestyle:
    sleep_context:
    nutrition_context:
    exercise_context:
    stress_context:

  actions: []

  conversations: []

  permissions:
    agent_access:
    sharing_permission:
    export_permission:
    delete_permission:
```

MVP behavior supported by this conceptual model:

- preserve user-provided background
- preserve user-stated healthspan goals
- organize measurement information
- reference user-provided reports
- understand lifestyle context
- remember user-confirmed actions
- reduce repeated context questions
- apply explicit permission boundaries

MVP behavior not supported by this model:

- diagnosis
- clinical decision support
- treatment planning
- medication management
- disease prediction
- disease risk calculation
- system scoring
- personalized protocols

---

## 6. Data Categories

### 6.1 Profile

Purpose:

```text
Basic user background.
```

Conceptual fields:

```yaml
user_id:
age:
sex:
height:
weight:
body_composition:
location:
occupation:
```

`occupation` is optional.

Profile information may improve the relevance of non-clinical explanations and reduce repeated questions.

It must not be used to infer diagnosis, calculate disease risk, or generate treatment or supplement protocols.

### 6.2 Goals

Purpose:

```text
Understand the user's healthspan objectives.
```

Conceptual fields:

```yaml
goals: []
healthspan_goal:
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

Goals may prioritize educational explanations, record organization, and low-risk information collection.

Goals must not become clinical plans, disease diet prescriptions, training prescriptions, or personalized supplement protocols.

### 6.3 Biomarkers

Purpose:

```text
Store and organize user-provided measurement information.
```

Conceptual fields:

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

No:

- diagnosis
- risk calculation
- treatment recommendation
- disease prediction
- system scoring
- clinical interpretation

If unit, measurement date, or source is absent, Congtie should identify the missing context instead of guessing.

This conceptual schema does not modify, replace, or connect any biomarker map JSON.

### 6.4 Reports

Purpose:

```text
Store references and metadata for user-provided health documents.
```

Examples:

- laboratory reports
- physical examination reports
- uploaded documents
- device exports

Conceptual fields:

```yaml
report_id:
report_type:
source:
date:
file_location:
user_notes:
```

`file_location` is a conceptual reference. It does not define a local path, URL contract, cloud provider, or database representation.

Reports may support organization and professional consultation preparation.

They must not be treated as authorization for a new diagnosis, treatment plan, medication change, clinical order, or risk calculation.

### 6.5 Lifestyle

Purpose:

```text
Understand user habits and lifestyle context.
```

Follow the Congtie canonical order:

```text
sleep
nutrition
exercise
stress
```

Conceptual fields:

```yaml
sleep_context:
nutrition_context:
exercise_context:
stress_context:
```

Lifestyle context may support educational explanation, missing-context detection, and low-risk tracking.

It is not clinical judgment.

It must not diagnose sleep disorders, prescribe disease diets, create training or rehabilitation plans, diagnose mental health conditions, or generate personalized supplement protocols.

### 6.6 Actions

Purpose:

```text
Provide a future execution-tracking foundation and preserve user-confirmed action continuity.
```

Conceptual fields:

```yaml
action_id:
action_type:
start_date:
status:
notes:
```

Examples:

- started strength training
- improved sleep schedule
- started tracking nutrition
- uploaded a report
- prepared questions for a clinician

Action history records what the user reports or confirms.

It must not be used to infer clinical improvement, treatment effect, disease risk reduction, or system score changes.

### 6.7 Conversations

Purpose:

```text
Store limited user interaction context to improve continuity.
```

Examples:

- preferences
- goals
- important background
- recurring questions

Conceptual fields:

```yaml
conversation_id:
preferences:
goals_context:
important_background:
recurring_questions: []
updated_at:
```

Do not store:

- medical conclusions generated by Congtie
- inferred diagnoses
- hidden chain-of-thought
- unlimited conversation transcripts without a defined purpose and permission

### 6.8 Permissions

Purpose:

```text
Record user-controlled boundaries for access, sharing, export, and deletion.
```

Conceptual fields:

```yaml
agent_access:
sharing_permission:
export_permission:
delete_permission:
```

Permissions should be explicit, scoped, purpose-limited, and revocable where applicable.

No external sharing or agent use should be inferred from the existence of stored information.

---

## 7. Field Definitions

The field definitions below describe product meaning, not implementation types or validation rules.

No field in this document creates a clinical threshold, calculation formula, database column, or API contract.

### 7.1 Profile Fields

| Field | MVP Presence | Definition | Boundary |
|---|---|---|---|
| `user_id` | required for a context container | Opaque reference identifying the user context owner. | Must not expose secrets or imply identity verification. |
| `age` | optional | User-provided age context. | Must not independently drive diagnosis or risk calculation. |
| `sex` | optional | User-provided sex context when relevant. | Collect only for a clear purpose; do not infer. |
| `height` | optional | User-provided height. | Preserve unit context in future implementation; do not guess. |
| `weight` | optional | User-provided weight. | Context only; not a diagnosis or score. |
| `body_composition` | optional | User-provided or device-derived body-composition context. | Device estimates must not be treated as precise clinical measurements. |
| `location` | optional | User-provided location context at the minimum necessary granularity. | Avoid unnecessary precise location collection. |
| `occupation` | optional | User-provided occupational context when relevant. | Must not be required by default. |

### 7.2 Goal Fields

| Field | MVP Presence | Definition | Boundary |
|---|---|---|---|
| `goals` | optional list | User-stated objectives or areas of interest. | Does not authorize a clinical or personalized intervention plan. |
| `healthspan_goal` | optional | User's primary healthspan-oriented objective. | Must remain user-stated, not inferred as a medical need. |
| `priority_dimensions` | optional ordered list | Selected lifestyle priorities using sleep, nutrition, exercise, stress order. | Guides context and education only. |

### 7.3 Biomarker Fields

| Field | MVP Presence | Definition | Boundary |
|---|---|---|---|
| `biomarker_id` | required when a biomarker record exists | Opaque record identifier. | Does not imply linkage to the public biomarker map. |
| `name` | required when a biomarker record exists | User-visible measurement name from the source. | Preserve original naming where possible. |
| `value` | required when a biomarker record exists | User-provided or extracted measurement value. | Must not be interpreted without necessary context. |
| `unit` | expected when available | Unit shown by the source. | Never guess missing units. |
| `measurement_date` | expected when available | Date associated with the measurement. | Missing date must be represented as missing context. |
| `source` | expected when available | Origin such as user entry, report, laboratory, or device. | Preserve provenance; do not claim unsupported authority. |
| `notes` | optional | User-provided context or record note. | Notes are not clinical conclusions. |

### 7.4 Report Fields

| Field | MVP Presence | Definition | Boundary |
|---|---|---|---|
| `report_id` | required when a report record exists | Opaque report reference. | Must not expose storage credentials. |
| `report_type` | required when a report record exists | General document type. | Classification does not create a clinical interpretation. |
| `source` | expected when available | User-reported issuing or originating source. | Do not infer a provider or institution. |
| `date` | expected when available | Date shown on or associated with the report. | Do not guess a missing date. |
| `file_location` | implementation-deferred | Conceptual pointer to the user-controlled report object. | No provider, path, URL, or access model is approved here. |
| `user_notes` | optional | User-provided comments about the report. | Must remain distinguishable from source content. |

### 7.5 Lifestyle Fields

| Field | MVP Presence | Definition | Boundary |
|---|---|---|---|
| `sleep_context` | optional | User-provided sleep habits, timing, regularity, or subjective experience. | No sleep disorder diagnosis. |
| `nutrition_context` | optional | User-provided food pattern, hydration, alcohol, or nutrition background. | No disease diet or personalized nutrition prescription. |
| `exercise_context` | optional | User-provided activity, training, movement, or recovery background. | No training or rehabilitation prescription. |
| `stress_context` | optional | User-provided perceived stress and related context. | No mental health diagnosis or psychiatric treatment. |

### 7.6 Action Fields

| Field | MVP Presence | Definition | Boundary |
|---|---|---|---|
| `action_id` | required when an action record exists | Opaque action record identifier. | Does not imply automated execution authority. |
| `action_type` | required when an action record exists | User-confirmed action category. | Must remain within approved action boundaries. |
| `start_date` | optional | User-provided or confirmed action start date. | Do not infer if unknown. |
| `status` | optional | User-confirmed action state. | Must not be interpreted as health outcome or treatment response. |
| `notes` | optional | User-provided action context. | Must not become a clinical conclusion. |

### 7.7 Conversation Fields

| Field | MVP Presence | Definition | Boundary |
|---|---|---|---|
| `conversation_id` | optional | Opaque reference for a bounded conversation context item. | Does not authorize indefinite transcript retention. |
| `preferences` | optional | User-stated communication or interaction preferences. | Must not include inferred sensitive traits without permission. |
| `goals_context` | optional | Goal context relevant to ongoing user-directed tasks. | Must remain distinguishable from clinical intent. |
| `important_background` | optional | User-selected background useful for continuity. | Collect only what is needed for the stated purpose. |
| `recurring_questions` | optional list | User questions that remain relevant across interactions. | Questions are not evidence of diagnosis. |
| `updated_at` | future implementation field | Time the context item was last updated. | Exact format is not defined here. |

### 7.8 Permission Fields

| Field | MVP Presence | Definition | Boundary |
|---|---|---|---|
| `agent_access` | required before agent use | User permission for an identified agent purpose and selected context scope. | Denied by default; no broad implicit access. |
| `sharing_permission` | required before sharing | User permission for selected information, recipient, and purpose. | No external sharing by default. |
| `export_permission` | user-controlled | User direction to export selected context. | Export format and delivery security require separate implementation review. |
| `delete_permission` | user-controlled | User direction to delete selected context. | Must not be used to remove or limit user deletion rights. |

---

## 8. Permission Model

### 8.1 Default Posture

Recommended defaults:

```text
private by default
agent access denied by default
external sharing denied by default
minimum necessary scope
purpose-limited use
user-controlled export
user-controlled deletion
```

### 8.2 Agent Access

Before an AI agent uses private context, the product should establish:

- which agent or feature is requesting access
- which data categories are requested
- the purpose of use
- whether access is one-time or ongoing
- how the user may revoke access

An upload does not imply unlimited future agent access.

### 8.3 Sharing Permission

Before information is shared, the user should know:

- what information will be shared
- who or what will receive it
- why it will be shared
- whether continuing access is requested
- whether continuing access can be revoked

No third-party or agent-to-agent sharing is approved by this document.

### 8.4 Export Permission

The user should be able to request export of selected context in a future implementation.

This document does not define export formats, destinations, identity verification, or delivery security.

### 8.5 Delete Permission

The user should be able to request deletion of selected context or their full context library in a future implementation.

Retention, backup, legal, and recovery behavior requires separate review.

### 8.6 Permission Revocation

Revocation should stop future access within the affected scope where technically and legally applicable.

Revocation does not imply deletion unless the user separately requests deletion.

### 8.7 Permission Auditability

Future implementations should preserve a user-visible record of permission grants, revocations, sharing, export, and agent access.

Auditability must not expose hidden chain-of-thought.

This section defines product boundaries only. It does not implement authentication, authorization, consent storage, or access-control policy.

---

## 9. AI Agent Usage Rules

### 9.1 AI May

With appropriate permission, the AI agent may:

- read approved user context
- reduce repeated questions
- personalize educational explanations
- identify missing information
- suggest low-risk information completion
- organize user-provided records
- preserve continuity around user goals and actions
- prepare non-clinical summaries
- help prepare questions for a clinician or qualified professional

### 9.2 AI Must

The AI agent must:

- stay within the approved data scope and purpose
- explain important missing context and uncertainty
- distinguish user-provided, report-derived, and device-derived information
- distinguish public knowledge from private context
- avoid guessing missing values, dates, units, or sources
- respect revoked or expired access
- request confirmation before external sharing or export
- preserve non-clinical boundaries
- avoid hidden commercial targeting

### 9.3 AI Must Not

The AI agent must not:

- diagnose
- prescribe treatment
- recommend medication
- provide dosage advice
- generate a personalized supplement protocol
- generate a personalized nutrition prescription
- generate a personalized training prescription
- calculate disease risk
- calculate body-system scores
- predict disease
- provide clinical recommendations
- make emergency assessments or perform triage
- replace clinicians
- infer broad permission from prior interactions
- share private context without explicit permission

### 9.4 Bounded Personalization

Allowed personalization may affect:

- which missing-context question to ask
- which educational explanation is relevant
- which user-provided record to organize
- which low-risk information category may be useful to complete
- which questions the user may prepare for a professional

Personalization must not affect:

- diagnosis
- treatment
- medication or dosage
- clinical decisions
- disease risk scores
- system scores
- disease predictions
- personalized protocols
- medical interventions

---

## 10. Safety Boundaries

User Health Context does not transform stored information into:

```text
medical diagnosis
treatment plan
medication management
medication recommendation
dosage advice
emergency assessment
clinical decision
clinical recommendation
disease risk calculation
disease prediction
system scoring
personalized supplement protocol
personalized nutrition prescription
personalized training prescription
personalized medical intervention
```

Additional boundaries:

- A biomarker value does not establish a diagnosis.
- A report does not authorize a new clinical interpretation.
- A series of records does not authorize disease prediction or risk scoring.
- A user goal does not authorize a treatment, nutrition, training, or supplement prescription.
- An action status does not establish a health outcome or treatment effect.
- Conversation context does not imply medical consent.
- Private context does not authorize product targeting or commercial conversion.
- Emergency concerns require real-world professional or emergency support; User Health Context is not a triage system.

Medication context, if considered in a future version, may only be handled under separately approved safety and privacy rules. Congtie v0 must not recommend starting, stopping, changing, combining, or dosing medication.

Supplement context must not be used to generate dosage, timing, loading phase, cycle, stack, or personalized protocol advice.

---

## 11. Storage Principles

v0 defines the conceptual schema only.

v0 does not implement:

```text
database
persistent user data model
hospital integration
healthcare APIs
wearable APIs
external data synchronization
cloud storage provider
file storage contract
production encryption
production access control
```

Future storage should follow these principles:

- private by default
- user-owned and permission-controlled
- minimum necessary collection
- separation from the public Longevity Information Library
- least-privilege access
- purpose-limited retrieval
- provenance preservation
- explicit missing-data handling
- correction support
- export support
- deletion support
- revocation support
- auditable use
- no private user data committed to the Git-managed public knowledge base
- no secrets or access credentials stored in content files

The following remain implementation decisions requiring separate review:

- database technology
- physical data model
- field types and validation
- identifier design
- encryption strategy
- authentication and authorization
- retention and backup
- deletion execution
- export delivery
- audit storage
- compliance requirements
- API representation

This approved document does not authorize those implementations.

---

## 12. Future v1 Expansion

All future expansion requires privacy, safety, consent, security, and product review.

### 12.1 Data Integration

Possible future source categories include:

- Apple Health
- Garmin
- WHOOP
- Oura
- continuous glucose monitoring APIs
- laboratory APIs
- other user-authorized health platforms

These names identify possible future integration directions only.

They do not represent approved integrations, product endorsements, purchasing recommendations, commercial relationships, or implementation commitments.

Every external integration requires a separate Founder Gate and review of:

- user permission
- requested data scope
- provider terms
- security
- data retention
- revocation
- deletion
- provenance
- regulatory and legal requirements

### 12.2 Longitudinal Tracking

Possible future capabilities:

- trends
- goals
- actions
- feedback
- data freshness
- source history
- correction history
- permission history

Longitudinal tracking must not become diagnosis, clinical scoring, disease risk calculation, disease prediction, or treatment evaluation without a separately approved clinical governance process.

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
user health context
=
personalized longevity assistant
```

This architecture may support more relevant explanation, reduced repetition, continuity, and safer context completion.

It does not authorize diagnosis, treatment, medication management, disease prediction, clinical decisions, or personalized medical intervention.

---

## 13. Non-goals

Congtie v0 does not build:

- an electronic medical record system
- a hospital system
- a clinical decision support system
- a diagnosis engine
- a treatment engine
- a medication system
- a dosage-management system
- a disease prediction system
- a disease risk calculator
- a body-system scoring engine
- an insurance system
- an emergency triage system
- a personalized supplement protocol engine
- a personalized nutrition prescription engine
- a personalized training prescription engine
- a personalized medical intervention engine
- broad agent-to-agent health-data sharing
- hidden commercial targeting
- production healthcare interoperability

This document does not create or approve:

- executable schema files
- database tables or models
- migrations
- persistent user data storage
- API or CLI contract changes
- runtime integration
- frontend implementation
- external provider integration
- external data synchronization
- biomarker JSON changes
- production clinical logic

---

## 14. Acceptance Criteria

This schema document is acceptable when:

- It defines User Health Context as private, user-controlled, and permission-based.
- It clearly separates User Health Context from the public Longevity Information Library.
- It defines the eight MVP categories: profile, goals, biomarkers, reports, lifestyle, actions, conversations, and permissions.
- It defines the required conceptual fields for each category.
- It preserves the canonical lifestyle order: sleep / nutrition / exercise / stress.
- It defines user ownership, privacy, sharing, export, and deletion principles.
- It defines agent access and sharing as explicit, scoped permissions.
- It defines allowed AI use for explanation, continuity, missing-context detection, and low-risk information completion.
- It preserves the non-clinical boundary.
- It does not authorize diagnosis, treatment, medication advice, dosage advice, clinical recommendation, system scoring, disease risk calculation, disease prediction, personalized supplement protocol, personalized nutrition prescription, personalized training prescription, or personalized medical intervention.
- It defines v0 as a conceptual schema only.
- It does not implement a database, healthcare API, wearable API, external synchronization, or hospital integration.
- It describes future integration names as candidates only, without endorsement or implementation approval.
- It records that any persistent model or external integration requires separate review.
- It uses `Congtie` as the display name.
- It uses `congtie` only for lowercase paths, code, or domains.
- It does not use the deprecated camel-case brand spelling.

---

## Final Note

User Health Context exists to make Congtie more relevant without turning Congtie into a clinical system.

The safest v0 principle is:

```text
Store only approved context.
Keep the user in control.
Use private information only for the stated purpose.
Personalize explanation and safe information support, not medical decisions.
```
