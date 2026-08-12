# Evidence Source Type Alignment Notes v0.1

Version: v0.1  
Project: Congtie  
Status: Draft  
Owner: Congtie Agent Team  
Last Updated: 2026-08-07

---

## 1. Purpose

This document records migration and governance decisions for historical `source_type` values found in Congtie Longevity Information Library specifications and Knowledge Seed content.

The reviewed historical values are:

```text
expert_interview
expert_blog
conference_talk
unknown_or_unverified
```

This document defines:

- which values should be kept
- what each kept value means
- typical evidence treatment
- whether a value maps to another canonical value
- how a future validator should handle each value
- how migration should preserve traceability

This is governance documentation only.

It does not:

- modify the evidence framework
- modify the knowledge item conceptual schema
- modify the source type enum document
- modify knowledge entries
- create validator code
- create JSON Schema
- create runtime behavior
- create an API contract

---

## 2. Relationship with `evidence_source_type_enum.v0.1`

This document supplements:

```text
agent/longevity_knowledge_base/schemas/evidence_source_type_enum.v0.1.md
```

The enum governance document defines:

- the v0.1 canonical list
- alias behavior
- deprecated-value behavior
- unknown-value behavior
- future extension rules

Its future-extension section requires older values to be reviewed before inclusion, aliasing, or deprecation.

This alignment note performs that review for four historical values.

The decisions are:

```text
expert_interview       → keep
expert_blog            → keep
conference_talk        → keep
unknown_or_unverified  → do not keep as source_type
```

Until a future versioned enum document incorporates the kept values directly, this alignment note acts as the authoritative compatibility supplement for these four values.

An alignment-aware future validator should treat the three kept values as governed source types.

This document does not silently rewrite or supersede the existing enum file. A future explicit alignment update may merge the decisions into a later enum version.

### 2.1 Evidence Separation

The decisions concern source category only.

They do not automatically determine:

- evidence level
- evidence posture
- source quality
- publication status
- actionability
- clinical permission

Typical evidence levels in this document are defaults for review, not automatic assignments.

### 2.2 Combined v0.1 Governance View

For migration and future validator planning, the governed values consist of:

```text
canonical values in evidence_source_type_enum.v0.1
+
expert_interview
+
expert_blog
+
conference_talk
```

`unknown_or_unverified` is not part of the kept source category set.

---

## 3. Historical Values Review

### 3.1 `expert_interview`

Status:

```text
keep
```

Meaning:

```text
Expert interviews, podcasts, and public conversations in which an identified expert presents views, interpretation, experience, or hypotheses.
```

Typical evidence:

```text
E5 expert opinion or hypothesis
```

Allowed usage:

- expert viewpoint context
- hypothesis or interpretation tracking
- progress and viewpoints entries
- discovery of primary sources
- explanation of active debate

Boundaries:

- The expert's identity and relevant expertise should be reviewable.
- Interview statements are not professional consensus by default.
- An interview is not peer-reviewed research.
- A cited paper should be recorded separately using the appropriate research source type.
- Expert interviews must not directly authorize treatment, medication, dosage, risk calculation, or personalized protocols.

Decision rationale:

The value describes a distinct and useful source category that cannot be represented precisely by `media_article`, `professional_organization_article`, or `founder_curated`.

### 3.2 `expert_blog`

Status:

```text
keep
```

Meaning:

```text
Expert-authored blogs, essays, newsletters, or commentary that present an identified expert's interpretation, opinion, synthesis, or hypothesis.
```

Typical evidence:

```text
E5 expert opinion or hypothesis
```

Allowed usage:

- expert viewpoint context
- interpretation and debate tracking
- progress and viewpoints entries
- discovery of primary sources
- founder-curated background review

Boundaries:

- Authorship and relevant expertise should be reviewable.
- A blog is not peer-reviewed evidence.
- Organization hosting does not automatically make a blog a professional consensus.
- Referenced research should be recorded separately with its own source type.
- Expert commentary must not be presented as diagnosis, treatment, dosage, or clinical recommendation.

Decision rationale:

The value distinguishes identified expert commentary from general media content and internal curation.

### 3.3 `conference_talk`

Status:

```text
keep
```

Meaning:

```text
Conference presentations, keynote talks, symposium materials, panel presentations, posters, or related public conference content.
```

Typical evidence:

```text
E5 expert opinion or hypothesis
```

Exception:

If a conference item is supported by separately published peer-reviewed research, the published research should receive its own appropriate source type and evidence assessment.

Allowed usage:

- emerging research context
- expert viewpoint tracking
- progress and viewpoints entries
- research or product development watchlists
- discovery of later publications

Boundaries:

- Conference presentation does not guarantee peer review.
- Abstract, poster, talk, and full publication must remain distinguishable.
- Preliminary results must not be treated as established findings.
- Conference claims must not directly support treatment, supplementation protocols, clinical decisions, or product endorsements.

Decision rationale:

Conference material is a distinct source category important for progress monitoring, but it requires conservative evidence treatment.

### 3.4 `unknown_or_unverified`

Status:

```text
do not keep as source_type
```

Meaning in historical usage:

```text
The source category or verification state was unknown, incomplete, or not yet reviewed.
```

Reason:

`unknown_or_unverified` describes verification status, not the category from which information came.

It mixes two different dimensions:

```text
source_type
= what kind of source this is

verification status
= whether the source identity, availability, authenticity, or classification has been reviewed
```

Keeping it as a source type would reduce provenance precision and make evidence checks ambiguous.

Future candidate:

```yaml
source_verification_status:
```

This future field is only a design direction.

This document does not define its enum, add it to the knowledge item schema, create validator logic, or authorize implementation.

Migration boundary:

- Do not automatically map `unknown_or_unverified` to a canonical source type.
- Do not guess the original source category.
- Preserve the historical value until a human reviews the source.
- Record a migration warning.
- After review, a human may replace it with the correct canonical source type through a normal Git change.

---

## 4. Mapping Decisions

### 4.1 Decision Table

| Historical Value | Status | Canonical Mapping | Typical Evidence | Migration Action |
|---|---|---|---|---|
| `expert_interview` | keep | `expert_interview` | E5 | Preserve; no normalization needed. |
| `expert_blog` | keep | `expert_blog` | E5 | Preserve; no normalization needed. |
| `conference_talk` | keep | `conference_talk` | E5 unless separately supported by published research | Preserve; no normalization needed. |
| `unknown_or_unverified` | do not keep | none | not determined | Warn and require human source classification. |

### 4.2 Kept Values

Kept values map to themselves.

They are not aliases.

They may be used in new entries when they precisely describe the source and all evidence and safety boundaries are preserved.

Typical E5 treatment does not prevent a reviewer from assigning another evidence level when independently justified by the actual source and governance framework.

The source type itself must never perform that upgrade automatically.

### 4.3 No Mapping for `unknown_or_unverified`

There is no safe one-to-one canonical replacement.

It must not automatically map to:

- `commercial_claim_unverified`
- `media_article`
- `founder_curated`
- `professional_education_page`
- any peer-reviewed source type

Those values describe specific source categories that cannot be inferred from an unknown verification state.

### 4.4 Traceability

Migration should preserve:

- original value
- original file path
- entry ID
- review date when classified
- reviewer or role
- final canonical source type
- migration note

No automated process should erase the historical value from Git history.

### 4.5 Future Enum Alignment

A future `evidence_source_type_enum` version should add:

```text
expert_interview
expert_blog
conference_talk
```

to the canonical list and remove the unresolved compatibility note for those values.

`unknown_or_unverified` should not be added to the canonical source-type list.

---

## 5. Validator Behavior

This section defines documentation-level behavior for a future validator. It does not create code.

### 5.1 Kept Values

The validator should treat:

```text
expert_interview
expert_blog
conference_talk
```

as valid governed values.

Result:

```text
PASS
```

No alias warning or normalization suggestion is needed.

### 5.2 `unknown_or_unverified`

When the validator finds:

```text
unknown_or_unverified
```

it should emit a migration warning.

Example:

```text
WARNING: source_type "unknown_or_unverified" represents verification status rather than a source category; human classification is required.
```

The validator must:

- preserve the source file
- avoid guessing a replacement
- avoid automatic rewriting
- identify the entry and file path
- recommend human review

The warning indicates unresolved migration work. Human approval or publication governance may require resolution before the entry advances.

### 5.3 Other Values

Validator behavior remains:

| Classification | Result | Automatic Rewrite |
|---|---|---|
| Canonical enum value | pass | no |
| Kept alignment value | pass | no |
| Registered alias | normalization warning | no |
| Deprecated value | deprecation warning | no |
| `unknown_or_unverified` | migration warning | no |
| Truly unknown value | error | no |

### 5.4 Evidence Cross-checks

Recommended checks:

- `expert_interview` usually prompts review when evidence level is stronger than E5.
- `expert_blog` usually prompts review when evidence level is stronger than E5.
- `conference_talk` usually prompts review when evidence level is stronger than E5 without separately recorded published research.
- Kept values must not be presented as professional consensus or peer-reviewed research by default.
- `unknown_or_unverified` must not support a high-confidence evidence claim.

These should be review warnings unless a future validator taskpack explicitly defines a stronger failure rule.

### 5.5 No Automatic Rewrite

The validator must never:

- replace a kept value
- infer the source behind `unknown_or_unverified`
- add `source_verification_status`
- modify evidence level
- modify evidence posture
- edit Markdown files

### 5.6 Validation Impact Summary

```text
expert_interview      → pass
expert_blog           → pass
conference_talk       → pass
unknown_or_unverified → migration warning; human review required
```

The safest migration principle is:

```text
Keep precise historical source categories.
Separate source category from verification status.
Warn openly.
Require human classification where provenance is unknown.
Never silently rewrite canonical files.
```
