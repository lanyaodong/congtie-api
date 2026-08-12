# Congtie Longevity Knowledge Base

Version: v0.1  
Project: Congtie  
Status: Draft  
Owner: Congtie Agent Team  
Last Updated: 2026-08-12

---

## 1. Purpose

This directory is the canonical repository structure for the Congtie Longevity Information Library.

The library is the public knowledge foundation for Congtie Agent. It organizes reusable longevity information for human review, evidence tracking, governance, future retrieval, and bounded action support.

It may contain:

- stable longevity knowledge
- permission-controlled action resources
- progress and viewpoints
- education materials
- governance and curation rules
- invalid, harmful, outdated, or exaggerated claim notes
- entry templates
- future indexes and review records

This structure prepares content organization only. It does not create runtime behavior, API contracts, frontend behavior, a production database, or a CMS GUI.

---

## 2. Architecture Relationship

The Longevity Information Library architecture defines the vertical information layers and governance structure.

The topic taxonomy defines the horizontal topic map and retrieval structure.

This directory provides the Git-backed file organization for content governed by those documents.

Primary references:

```text
agent/knowledge_seed_v0/longevity_information_library_architecture.v0.1.md
agent/knowledge_seed_v0/longevity_topic_taxonomy.v0.1.md
agent/knowledge_seed_v0/evidence_grading_framework.v0.1.md
agent/longevity_knowledge_base/templates/longevity_knowledge_item_template.v0.1.md
agent/longevity_knowledge_item_schema.v0.1.md
```

The intended two-axis model is:

```text
information layer
+
topic path
=
governed, retrievable knowledge entry
```

Directory placement identifies the primary information layer. Entry metadata should identify the taxonomy topic and any secondary topics.

Topic placement does not override evidence, safety, publication, commercial, or action-resource permission boundaries.

---

## 3. Relationship with the User Health Information Library

The Longevity Information Library and User Health Information Library are separate foundations.

```text
Longevity Information Library
= public, general, reusable, versioned knowledge

User Health Information Library
= private, user-specific, permission-gated health context
```

This directory contains general information only.

It must not contain:

- personal biomarker values
- personal laboratory reports
- personal medical records
- personal lifestyle logs
- personal supplement or medication history
- personal action history
- private conversation context
- user consent or sharing records

Private user context must not be committed here, copied into entry examples, or mixed into review logs.

Congtie may combine general knowledge with approved private user context only through separately reviewed runtime safety and permission boundaries.

---

## 4. Canonical Source of Truth

The canonical source of truth is:

```text
agent/longevity_knowledge_base/entries/<information_layer>/*.md
+ Git repository
```

Only Markdown entry files stored under `entries/<information_layer>/` are canonical Longevity Information Library entries. Templates, schemas, indexes, review logs, scripts, and legacy directories are supporting assets, not alternative entry sources.

Git provides:

- canonical file history
- version review
- authorship and change traceability
- reversible edits
- branch and pull-request workflows
- human approval records

Feishu may be used as a human review interface.

Feishu is not the canonical source of truth. Content reviewed in Feishu must be reconciled back into the canonical Markdown file through an explicit Git change before it is considered current.

Future CMS or synchronization tools may assist review, but they must not silently replace Markdown, overwrite Git history, or publish unreviewed content.

One knowledge item should have one canonical Markdown source file under `entries/<information_layer>/`. Avoid parallel copies across canonical and legacy layer directories.

---

## 5. Entry Lifecycle

The standard entry lifecycle is:

```text
draft
→ ai_review_pending
→ ai_reviewed
→ human_review_pending
→ approved
→ published
→ archived
```

### 5.1 `draft`

The entry is being created or revised.

It is not approved for publication or runtime use.

### 5.2 `ai_review_pending`

The entry is ready for bounded AI review.

AI review may check structure, naming, evidence metadata, source traceability, safety language, and internal consistency.

### 5.3 `ai_reviewed`

AI review is complete and its findings have been recorded or addressed.

AI review does not grant human approval.

### 5.4 `human_review_pending`

The entry is ready for an authorized human reviewer.

Clinical sensitivity, evidence posture, product claims, commercial boundaries, and action-resource permissions require particular attention where applicable.

### 5.5 `approved`

An authorized human reviewer has approved the content version.

Approval does not automatically publish the entry or connect it to runtime retrieval.

### 5.6 `published`

The approved entry has passed the separately defined publication workflow and is eligible for its approved use.

Publication must still respect evidence, safety, visibility, and permission metadata.

### 5.7 `archived`

The entry is retained for history but is no longer current.

Archived entries should not be selected for normal runtime use.

Lifecycle transitions should be explicit, reviewable, and recorded in Git. AI agents must not self-approve or self-publish entries.

---

## 6. Directory Structure

```text
agent/longevity_knowledge_base/
├── README.md
├── entries/
│   ├── knowledge/
│   ├── action_resources/
│   ├── progress_and_viewpoints/
│   ├── education/
│   ├── governance/
│   └── invalid_or_harmful/
├── templates/
├── schemas/
├── indexes/
├── review_logs/
├── scripts/
├── knowledge/                 # legacy; do not add future entries
├── action_resources/          # legacy; do not add future entries
├── progress_and_viewpoints/   # legacy; do not add future entries
├── education/                 # legacy; do not add future entries
├── governance/                # legacy; do not add future entries
└── invalid_or_harmful/        # legacy; do not add future entries
```

### 6.1 `entries/`

The only canonical storage root for actual Longevity Information Library entries.

Canonical path pattern:

```text
agent/longevity_knowledge_base/entries/<information_layer>/<entry_id>.<entry_slug>.md
```

Allowed information-layer directories:

```text
knowledge
action_resources
progress_and_viewpoints
education
governance
invalid_or_harmful
```

Metadata values and filesystem directories map as follows:

| `information_layer` metadata | Canonical entry directory |
|---|---|
| `knowledge` | `entries/knowledge/` |
| `action_resource` | `entries/action_resources/` |
| `progress_and_viewpoints` | `entries/progress_and_viewpoints/` |
| `education` | `entries/education/` |
| `governance` | `entries/governance/` |

`entries/invalid_or_harmful/` is a dedicated content directory, not a separate `information_layer` enum value. An `invalid_or_harmful_note` stored there must use an allowed primary information layer, normally `knowledge` or `governance`, according to its content and governance role.

Future entries must be created under the matching child directory. `entries/` is not a temporary intake or migration-staging area, and canonical files must not be duplicated elsewhere.

#### 6.1.1 `entries/knowledge/`

Stable, reusable explanation-oriented knowledge entries.

Typical content includes healthspan foundations, body-system concepts, measurement concepts, lifestyle foundations, and non-clinical safety explanations.

#### 6.1.2 `entries/action_resources/`

Permission-controlled products, services, devices, tools, supplements, and information resources.

Entries must preserve the approved action-resource permission model:

```text
R0 = prohibited from automatic recommendation
R1 = user-initiated explanation only
R2 = information-completion option
R3 = low-risk general tool option
```

Evidence strength does not override permission level.

#### 6.1.3 `entries/progress_and_viewpoints/`

Research progress, expert viewpoints, product-development progress, regulatory changes, and commercialization status.

These entries are not stable knowledge by default. Their default actionability is education only unless separately reviewed and approved.

#### 6.1.4 `entries/education/`

User-facing educational articles, glossaries, checklists, consultation-preparation materials, and guides.

Education content must remain within the approved non-clinical boundary.

#### 6.1.5 `entries/governance/`

Curation rules, evidence rules, source policies, safety boundaries, commercial boundaries, review workflows, versioning rules, and publication rules.

Governance entries define how content may be created and used; they do not create runtime policy by themselves.

#### 6.1.6 `entries/invalid_or_harmful/`

Notes about disproven, harmful, unsafe, outdated, unsupported, or exaggerated information.

Entries should explain the reason for invalidation or caution and preserve supporting sources and deprecation history.

### 6.2 Legacy Top-level Information-layer Directories

The following existing directories belong to the previous structure:

```text
knowledge/
action_resources/
progress_and_viewpoints/
education/
governance/
invalid_or_harmful/
```

They are not canonical entry locations after the v0.1 alignment decision. Do not create future entries in them and do not treat files placed there as canonical library entries.

These directories are preserved in place. No directory or entry is moved, renamed, migrated, or deleted by this documentation alignment. Any future migration or cleanup requires a separate exact-file plan and Founder approval.

### 6.3 `templates/`

Reusable Markdown templates and authoring guidance.

The initial template is:

```text
templates/longevity_knowledge_item_template.v0.1.md
```

Templates guide content shape. They do not automatically validate, approve, or publish entries.

### 6.4 `schemas/`

Structural and governance definitions for knowledge entries and evidence metadata.

Current schema-governance documents include:

```text
schemas/evidence_source_type_enum.v0.1.md
schemas/evidence_source_type_alignment_notes.v0.1.md
```

The conceptual entry schema currently lives at:

```text
agent/longevity_knowledge_item_schema.v0.1.md
```

These are documentation and governance definitions. They are not a database schema, persistence model, API contract, runtime model, or JSON Schema implementation. Creating executable schema artifacts requires separate review and any applicable Founder Gate approval.

### 6.5 `indexes/`

Reserved location for generated or reviewed knowledge indexes, manifests, and retrieval metadata.

Indexes should point to canonical Markdown files under `entries/<information_layer>/` and must not become an independent editable source of truth.

No index is created by this structure task.

### 6.6 `review_logs/`

Review outcomes, review metadata, issue lists, approval records, and revision notes.

Review logs must not contain private user health information or hidden chain-of-thought.

### 6.7 `scripts/`

Validation and maintenance tooling for canonical knowledge entries.

Current tooling includes:

```text
scripts/validate_longevity_knowledge_item.py
```

The validator checks approved structural and governance rules for one Markdown entry. It is not a medical fact checker, clinical reviewer, runtime integration, loader, publication system, or database tool. Future scripts should preserve canonical Markdown content and remain reviewable and Git-friendly.

---

## 7. Content Boundaries

This public knowledge base must not create or enable:

- diagnosis
- treatment
- medication advice
- dosage advice
- clinical recommendations
- clinical thresholds or ranges
- system scoring
- disease risk calculations
- disease predictions
- emergency triage logic
- personalized supplement protocols
- personalized nutrition prescriptions
- personalized training prescriptions
- personalized medical interventions
- hidden commercial conversion
- storage of private user health information

Biomarker JSON files remain outside this structure task and must not be modified or replaced through knowledge-base work.

---

## 8. v0.1 Foundation Status

The v0.1 foundation currently includes:

- canonical entry storage under `entries/<information_layer>/`;
- the knowledge item authoring template;
- the conceptual knowledge item schema;
- evidence source-type governance and alignment notes;
- a lightweight single-entry validator;
- future locations for indexes and review logs.

It does not:

- migrate existing Knowledge Seed entries
- create new knowledge content
- create indexes
- create loaders
- connect content to runtime
- modify API or frontend behavior
- create a production database
- create a CMS GUI

Those remaining activities require separate taskpacks and their own acceptance criteria.

---

## 9. Validation Entry Point

Run the current validator from the repository root with a canonical Markdown entry path:

```bash
python3 agent/longevity_knowledge_base/scripts/validate_longevity_knowledge_item.py \
  agent/longevity_knowledge_base/entries/<information_layer>/<entry_id>.<entry_slug>.md
```

Validation success does not approve, publish, index, or enable runtime retrieval for an entry. Human review and separately approved publication and runtime gates remain required.
