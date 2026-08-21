# Longevity Knowledge Item Template v0.1

Version: v0.1
Project: Congtie
Status: Draft
Owner: Congtie Agent Team
Last Updated: 2026-08-21

---

## 1. Purpose

This document defines the standard Markdown template for entries in the Congtie Longevity Information Library.

The template supports:

- human review
- AI agent editing
- CLI workflows
- Git version control
- future CMS GUI
- runtime retrieval

The canonical source of truth is:

```text
agent/longevity_knowledge_base/entries/<information_layer>/*.md
+ Git repository
```

Future entries must not be created in the legacy top-level information-layer directories.

Feishu may be used as a human review interface.

Feishu is not the canonical source of truth unless a future explicit sync and governance workflow is approved.

This template does not create runtime behavior, schema validation, API contracts, frontend behavior, scoring, diagnosis, treatment, medication advice, dosage advice, clinical recommendation, disease risk calculation, disease prediction, personalized supplement protocol, personalized nutrition prescription, personalized training prescription, or personalized medical intervention.

---

## 2. Design Principles

The template follows these principles:

1. One Markdown file represents one reusable information item.
2. YAML frontmatter stores machine-readable metadata.
3. Markdown body stores human-readable explanation and review notes.
4. Git history is the canonical version history.
5. Feishu or CMS tools may mirror or review content, but must not silently replace Git history.
6. All entries must remain non-clinical unless a future approved clinical governance layer exists.
7. Human review is required before publication.
8. AI-generated drafts must be reviewable, traceable, and reversible.
9. Runtime retrieval must respect status, visibility, safety, evidence, commercial boundary, and permission metadata.
10. Evidence level supports clearer explanation; it does not authorize stronger intervention.

---

## 3. File Naming Convention

Recommended file path pattern:

```text
agent/longevity_knowledge_base/entries/{information_layer}/{entry_id}.{entry_slug}.md
```

Example:

```text
agent/longevity_knowledge_base/entries/knowledge/KN-T0101-0001.healthspan-definition.md
```

Recommended file naming rule:

```text
{entry_id}.{entry_slug}.md
```

Rules:

- Use lowercase English slugs.
- Use hyphen or underscore consistently within a given directory.
- Do not use spaces in filenames.
- Use only an approved information-layer child directory under `entries/`.
- Do not create a parallel canonical copy in a legacy top-level layer directory.
- Do not rename files casually after publication.
- Historical filenames may be preserved when needed for compatibility.

---

## 4. Entry ID Convention

Entry ID format:

```text
{TYPE_PREFIX}-{PRIMARY_TOPIC_ID_NO_DOT}-{NNNN}
```

Examples:

```text
KN-T0101-0001
AR-T0702-0001
PV-T0802-0001
ED-T0902-0001
GV-T0909-0001
IH-T0609-0001
```

Prefix mapping:

| Prefix | Content Type |
|---|---|
| KN | knowledge_entry |
| AR | action_resource |
| PV | progress_and_viewpoint |
| ED | education_article |
| GV | governance_rule / curation_rule / safety_boundary |
| IH | invalid_or_harmful_note |
| ES | evidence_summary |
| CL | checklist |
| CC | clinician_conversation_preparation |
| PN | protocol_note |
| SN | source_note |
| GL | glossary_entry |

Field notes:

- `PRIMARY_TOPIC_ID_NO_DOT` removes the dot from the primary topic ID.
- `T01.01` becomes `T0101`.
- `T07.02` becomes `T0702`.
- `NNNN` is a zero-padded sequence number within the type and primary topic.
- Entry IDs should not be reused after archival or rejection.

---

## 5. YAML Frontmatter Template

Use one frontmatter block at the top of each file.

```yaml
---
schema_version: v0.1

entry_id: ""
entry_slug: ""
content_type: ""
information_layer: ""

title_zh: ""
title_en: ""
summary_zh: ""
summary_en: ""

language: zh-CN

primary_topic_id: ""
topic_ids: []
topic_paths: []

status: draft
visibility: internal
runtime_enabled: false
retrieval_enabled: false
publish_channels: []

created_by: ""
created_date: ""
last_modified_by: ""
last_modified_date: ""

submitted_by: ""
submitted_date: ""

ai_reviewed_by: ""
ai_review_date: ""
ai_review_summary: ""
ai_review_result: ""
ai_review_risk_flags: []

human_reviewer: ""
human_review_date: ""
review_note: ""

published_by: ""
published_date: ""

archived_by: ""
archived_date: ""
archive_reason: ""

status_history: []

version: v0.1
change_log: []

evidence_level: ""
evidence_posture: ""
source_type: []
source_urls: []
source_notes: ""

last_source_check_date: ""
next_review_date: ""

allowed_use: []
disallowed_use: []

safety_boundary: ""
commercial_boundary: ""

is_clinical_sensitive: false

related_body_systems: []
related_lifestyle_keywords: []
related_biomarkers: []
related_action_resource_ids: []
related_knowledge_ids: []
related_source_ids: []

china_availability: ""
regulatory_status: ""

actionability_status: not_applicable

duplicate_check:
  checked: false
  checked_date: ""
  possible_duplicates: []
  note: ""

agent_usage:
  may_edit: true
  may_summarize: true
  may_suggest_mapping: true
  may_publish: false
  requires_human_approval: true

attachments: []
---
```

---

## 6. Field Descriptions

### 6.1 Identity Fields

`schema_version`

Template or metadata schema version.

`entry_id`

Stable unique ID for the entry.

`entry_slug`

Human-readable English slug for filename, search, and review workflows.

`content_type`

The content object type.

`information_layer`

The Longevity Information Library layer.

### 6.2 Title and Summary Fields

`title_zh`

Chinese title.

`title_en`

English title.

`summary_zh`

Short Chinese summary.

`summary_en`

Short English summary.

`language`

Primary language for the entry.

### 6.3 Topic Mapping Fields

`primary_topic_id`

Primary taxonomy topic ID.

`topic_ids`

All taxonomy topic IDs for the entry.

`topic_paths`

Human-readable topic paths corresponding to `topic_ids`.

### 6.4 Workflow Fields

`status`

The single status field for the entry.

`visibility`

Recommended values:

```text
internal
founder_review
private_reference
public
archived
```

`runtime_enabled`

Whether runtime may retrieve or use the entry.

`retrieval_enabled`

Whether retrieval systems may index the entry.

`publish_channels`

Channels where the entry may be published after approval.

### 6.5 Review Fields

`created_by`

Creator of the entry.

`created_date`

Creation date.

`last_modified_by`

Most recent editor.

`last_modified_date`

Most recent edit date.

`submitted_by`

Person or agent that submitted the entry for review.

`submitted_date`

Submission date.

`ai_reviewed_by`

AI reviewer name or system identifier.

`ai_review_date`

AI review date.

`ai_review_summary`

Short AI review summary.

`ai_review_result`

Recommended values:

```text
pass
needs_revision
blocked
not_reviewed
```

`ai_review_risk_flags`

List of risk flags found by AI review.

`human_reviewer`

Human reviewer name or role.

`human_review_date`

Human review date.

`review_note`

Human review notes.

`published_by`

Publisher name or role.

`published_date`

Publication date.

`archived_by`

Archiver name or role.

`archived_date`

Archive date.

`archive_reason`

Reason for archival.

`status_history`

Chronological status transition records.

### 6.6 Version Fields

`version`

Entry version.

`change_log`

Human-readable change history.

### 6.7 Evidence and Source Fields

`evidence_level`

Evidence level according to the evidence grading framework.

`evidence_posture`

Evidence posture for how aggressively or conservatively the evidence may be used.

`source_type`

List of source types.

`source_urls`

Formal source URLs.

`source_notes`

Notes about source selection, exclusions, limitations, or follow-up review.

`last_source_check_date`

Most recent source availability and relevance check date.

`next_review_date`

Next planned review date.

### 6.8 Use Boundary Fields

`allowed_use`

Allowed uses for the entry.

`disallowed_use`

Disallowed uses.

`safety_boundary`

Safety boundary text.

`commercial_boundary`

Commercial boundary text.

`is_clinical_sensitive`

Boolean flag for clinical sensitivity.

### 6.9 Relationship Fields

`related_body_systems`

Related Congtie body systems.

`related_lifestyle_keywords`

Related lifestyle keywords.

`related_biomarkers`

Related biomarker IDs or names, when approved.

`related_action_resource_ids`

Related action resource IDs.

`related_knowledge_ids`

Related knowledge entry IDs.

`related_source_ids`

Related source IDs.

### 6.10 China and Regulatory Fields

`china_availability`

China availability context.

`regulatory_status`

Regulatory status or boundary.

### 6.11 Actionability Field

`actionability_status`

Recommended values:

```text
not_applicable
education_only
not_actionable
watchlist
requires_professional_context
future_candidate
deprecated
```

### 6.12 Duplicate Check Field

`duplicate_check`

Tracks whether a duplicate or overlap review has been performed.

### 6.13 Agent Usage Field

`agent_usage`

Defines whether AI agents may edit, summarize, suggest mapping, or publish the entry.

AI agents must never publish automatically.

### 6.14 Attachments Field

`attachments`

Optional list of attachment metadata.

Do not commit copyrighted full text, paid full text, or private user data unless separately reviewed and allowed.

---

## 7. Status Workflow

Only use one status field:

```yaml
status:
```

Allowed status values:

```text
draft
ai_review_pending
ai_reviewed
human_review_pending
needs_revision
approved
published
archived
rejected
```

Status rules:

- `draft` can come from a human or AI.
- AI-generated drafts must enter AI review.
- `ai_review_pending` means an AI review has been requested but not completed.
- `ai_reviewed` means an AI review has completed, but human approval has not necessarily happened.
- `human_review_pending` means a human reviewer must review the entry.
- `needs_revision` means the entry should be revised before approval or publication.
- `approved` requires human approval.
- `published` entries require human approval before publication.
- `archived` entries are not deleted.
- `rejected` entries remain traceable.

Recommended state machine:

```text
draft
→ ai_review_pending
→ ai_reviewed
→ human_review_pending
→ approved
→ published
```

Revision path:

```text
ai_reviewed / human_review_pending
→ needs_revision
→ draft
```

Closeout paths:

```text
draft / ai_reviewed / human_review_pending / needs_revision
→ rejected

approved / published
→ archived
```

---

## 8. Content Type Extensions

## 8.1 Information Layers

Allowed `information_layer` values:

```text
knowledge
action_resource
progress_and_viewpoints
education
governance
```

### 8.2 Content Types

Supported `content_type` values:

```text
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

### 8.3 Action Resource Extra Fields

Action resource entries should add:

```yaml
resource_type:
recommendation_permission:
auto_trigger_allowed:
commercial_boundary_level:
commercial_relationship:
privacy_risk:
source_enrichment_status:

provider:
brand:
model:
official_url:
purchase_urls:

selection_reason:
not_suitable_for:
risk_notes:
```

Permission values:

```text
R0
R1
R2
R3
```

Permission definitions:

```text
R0 = prohibited automatic recommendation
R1 = user initiated explanation only
R2 = information completion option
R3 = low-risk general tool option
```

Action resource rules:

- R0 entries must not be automatically recommended.
- R1 entries may only be explained when the user initiates the topic.
- R2 entries may be offered as optional information-completion context.
- R3 entries may support low-risk general tracking or organization.
- Permission level does not override clinical safety.
- Evidence level does not override permission level.
- Purchase links must not be used as recommendations.
- Commercial relationships must be transparent.

### 8.4 Nutrition / Supplement Extra Fields

Nutrition and supplement entries should add:

```yaml
nutrition_category:
common_use_context:
common_dosages_in_literature:
safety_notes:
known_interactions:
not_for_personalized_protocol:
```

`true` means no direct or standalone Personalized Longevity Protocol generation under the current product boundary; it does not permanently prohibit future governed use as evidence, knowledge, or context. This field is separate from retrieval permission, runtime enablement, publication status, and action authorization.

Boundary:

```text
Congtie v0 does not provide personalized supplement protocols.
```

Nutrition and supplement entries must not create:

```text
dosage advice
personalized supplement protocol
personalized nutrition prescription
medication advice
treatment
disease diet prescription
```

---

## 9. Markdown Body Structure

Use this body structure after frontmatter:

```markdown
# Title

## One-line Summary

Short summary of the entry.

## User-facing Explanation

Plain-language explanation for users.

## Key Points

- Key point 1
- Key point 2
- Key point 3

## Evidence and Source Notes

Explain source posture, evidence limits, and what the sources do or do not support.

## Safety Boundary

State what this entry must not be used for.

## Agent Usage Notes

Explain how AI agents may use or edit this entry.

## Founder / Reviewer Notes

Review notes, open questions, founder decisions, and future follow-up.
```

Body rules:

- Keep user-facing language clear and non-clinical.
- Do not include private user health information.
- Do not include hidden commercial prompts.
- Do not use source citations to escalate actionability beyond approved boundaries.
- Do not include diagnosis, treatment, medication advice, dosage advice, clinical recommendation, system scoring, disease risk calculation, disease prediction, personalized supplement protocol, personalized nutrition prescription, personalized training prescription, or personalized medical intervention.

---

## 10. Agent Usage Rules

AI agents may:

```text
create draft entries
modify draft entries
summarize sources
suggest topic mapping
perform AI review
```

AI agents cannot:

```text
bypass human approval
publish automatically
create diagnosis
create treatment plans
create medication advice
create personalized supplement protocols
```

Additional agent rules:

- Agents must preserve entry IDs.
- Agents must preserve status history.
- Agents must record material changes in `change_log`.
- Agents must not set `published` without human approval metadata.
- Agents must not enable runtime retrieval for unapproved entries unless explicitly allowed by governance.
- Agents must not store private user data in public knowledge files.
- Agents must not add product purchase links as recommendations.
- Agents must not add real provider integrations, secrets, production clinical logic, scoring, or thresholds.
- Agents must not modify biomarker JSON from this template workflow.

---

## 11. Validation Expectations

Future validators should check:

```text
schema completeness
entry_id uniqueness
topic_id validity
status validity
evidence fields
safety boundary existence
commercial transparency
duplicate detection
published entry approval
```

Recommended validator checks:

- Frontmatter exists.
- Required fields are present.
- `entry_id` matches `{TYPE_PREFIX}-{PRIMARY_TOPIC_ID_NO_DOT}-{NNNN}`.
- `entry_slug` is filename-safe.
- `content_type` is an allowed value.
- `information_layer` is an allowed value.
- `primary_topic_id` appears in `topic_ids`.
- `topic_ids` and `topic_paths` are aligned.
- `status` is an allowed value.
- Published entries include `human_reviewer`, `human_review_date`, `published_by`, and `published_date`.
- Archived entries include `archived_by`, `archived_date`, and `archive_reason`.
- `runtime_enabled` and `retrieval_enabled` are false for drafts unless explicitly allowed.
- Evidence fields are present.
- Source URLs are valid URLs or intentionally empty for early drafts.
- `allowed_use` and `disallowed_use` are present.
- `safety_boundary` is present.
- `commercial_boundary` is present.
- `duplicate_check` exists.
- `agent_usage.may_publish` is false.
- Deprecated brand spelling is absent.
- Private user health information is absent.
- Biomarker JSON is not modified by template validation.

---

## 12. Template Acceptance Criteria

This template is acceptable when it defines:

- purpose
- design principles
- file naming convention
- entry ID convention
- YAML frontmatter template
- field descriptions
- status workflow
- content type extensions
- Markdown body structure
- agent usage rules
- validation expectations

It must use:

```text
Congtie
```

as the display name.

It may use:

```text
congtie
```

only for lowercase, code, or domain contexts.

It must not use the deprecated camel-case brand spelling.

---

## 13. Final Note

This template is meant to make Congtie knowledge work boring in the best possible way:

```text
one item
one file
one review trail
one stable ID
clear boundaries
human approval before publication
```

The safest v0 principle remains:

```text
Make knowledge easy to review.
Make agent edits traceable.
Keep runtime use permission-controlled.
Do not turn an information library into a clinical system.
```
