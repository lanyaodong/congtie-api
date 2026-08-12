# Evidence Source Type Enum Governance v0.1

Version: v0.1  
Project: Congtie  
Status: Draft  
Owner: Congtie Agent Team  
Last Updated: 2026-08-07  
Founder Gate: Approved for documentation-only enum governance on 2026-08-07

---

## 1. Purpose

This document governs the v0.1 `source_type` enum for entries in the Congtie Longevity Information Library.

It defines:

- canonical `source_type` values
- source-type descriptions
- allowed usage
- migration aliases
- deprecated-value handling
- validator behavior
- future enum extension rules

The main compatibility decision in v0.1 is:

```text
peer_reviewed_review is a canonical source_type.
```

It represents a peer-reviewed review article that is not necessarily a systematic review or meta-analysis.

This document is governance documentation only.

It does not:

- modify existing knowledge entries
- modify the evidence framework
- create validation code
- create JSON Schema
- create a database schema
- create runtime behavior
- create an API contract
- normalize or rewrite files

---

## 2. Relationship with Evidence Framework

This document is a companion to:

```text
agent/knowledge_seed_v0/evidence_grading_framework.v0.1.md
agent/longevity_knowledge_item_schema.v0.1.md
```

The Evidence Grading Framework defines three related but separate concepts:

```text
evidence_level
= strength and maturity of evidence

evidence_posture
= how Congtie should treat the information

source_type
= where the information comes from
```

This document independently governs the third concept: `source_type`.

Important separation:

- A source type does not automatically determine evidence level.
- A source type does not automatically determine evidence posture.
- A source type does not authorize clinical use or stronger intervention.
- Multiple source types may apply to one entry.
- Commercial or weak sources must not be upgraded because they appear beside stronger sources.

Example:

```yaml
source_type:
  - official_product_spec
evidence_level: E0
evidence_posture: commercial_claim_unverified
```

An official product specification may support a feature description. It does not independently verify a health outcome.

Another example:

```yaml
source_type:
  - peer_reviewed_review
evidence_level: E2
evidence_posture: general_consensus
```

`E2` is not automatic in this example. The review's quality, scope, methods, and relevance must still be assessed.

This document does not silently replace source-type lists in older documents. Future alignment patches may update those documents through an explicit governance review.

---

## 3. Source Type Principles

### 3.1 Canonical Values

New entries should use canonical enum values from Section 4.

Canonical values are lowercase snake_case.

### 3.2 Source Type Is Provenance

`source_type` describes the source category.

It is not:

- a quality score
- a trust score
- an evidence level
- an action permission
- a publication approval
- a clinical authority flag

### 3.3 Multiple Values

`source_type` is a non-empty list.

Example:

```yaml
source_type:
  - official_guideline_china
  - peer_reviewed_meta_analysis
  - professional_education_page
```

Rules:

- Values must be unique within the list.
- Order should generally follow source importance for the entry.
- Repeating a type does not increase evidence strength.
- A weak source remains weak even when a strong source is also present.

### 3.4 Conservative Classification

When a source could fit multiple categories, use the most precise category supported by the source itself.

Do not classify:

- a professional education page as a guideline
- a narrative review as a meta-analysis
- an observational study as an RCT
- a product marketing page as an official product specification
- a media article as peer-reviewed research

When the source cannot be classified confidently, do not guess. Submit the value for governance review before publication.

### 3.5 Source Type Does Not Authorize Intervention

No source type authorizes:

- diagnosis
- treatment
- medication advice
- dosage advice
- clinical recommendation
- disease risk calculation
- system scoring
- disease prediction
- personalized supplement protocol
- personalized nutrition prescription
- personalized training prescription
- personalized medical intervention

### 3.6 Traceability

Source classification should remain traceable to the source URL, citation, attachment metadata, or source note where available.

Private user data must not be used as a public knowledge source.

---

## 4. Standard Enum List

The v0.1 canonical enum contains the values below.

### 4.1 Authority Sources

#### `official_guideline_china`

Description:

```text
Official Chinese guideline, standard, public-health guidance, or formally issued authority document relevant to the entry.
```

Allowed usage:

- China-specific public-health or professional context
- official guidance explanation
- official standard or regulatory-boundary context
- authority-guideline evidence review

Boundary:

The issuing body, document status, version, and applicability must be reviewed. An official source does not authorize diagnosis or personalized clinical action.

#### `official_guideline_international`

Description:

```text
Official guideline or public-health guidance from a recognized international or national authority outside China.
```

Allowed usage:

- international authority context
- global comparison
- general education when China-specific sources are incomplete
- guideline-based evidence review

Boundary:

Local applicability and current version must be considered. International authority does not override China-specific regulation or product availability.

#### `professional_consensus`

Description:

```text
Consensus statement, position statement, or formally reviewed recommendation from a recognized professional organization or expert panel.
```

Allowed usage:

- professional consensus explanation
- guideline-adjacent education
- evidence and safety context
- areas where consensus is more appropriate than a formal guideline

Boundary:

Consensus strength depends on methodology, authorship, conflicts, recency, and scope. It is not automatically E1.

### 4.2 Peer Reviewed Research

#### `peer_reviewed_meta_analysis`

Description:

```text
Peer-reviewed systematic review with quantitative meta-analysis or an equivalent formal quantitative evidence synthesis.
```

Allowed usage:

- evidence synthesis
- effect-direction or uncertainty explanation
- research-quality comparison
- general educational rationale

Boundary:

The article must actually include meta-analytic methods. A narrative review must not use this value.

#### `peer_reviewed_rct`

Description:

```text
Peer-reviewed randomized controlled trial.
```

Allowed usage:

- human intervention evidence context
- study design explanation
- evidence summary
- uncertainty and limitation review

Boundary:

One RCT does not establish universal effectiveness, safety, or personalized suitability.

#### `peer_reviewed_observational`

Description:

```text
Peer-reviewed observational, cohort, case-control, cross-sectional, or real-world research.
```

Allowed usage:

- association and trend explanation
- population-level context
- hypothesis support
- real-world evidence review

Boundary:

Associations must not be described as causation without appropriate evidence.

#### `peer_reviewed_mechanistic`

Description:

```text
Peer-reviewed mechanistic, cellular, animal, translational, or pathway-focused research.
```

Allowed usage:

- mechanism education
- early research context
- biological plausibility discussion
- progress and viewpoints

Boundary:

Mechanistic findings must not be presented as proven human outcomes or direct action recommendations.

#### `peer_reviewed_review`

Description:

```text
Peer-reviewed review article that is not necessarily a systematic review or meta-analysis.
```

Allowed usage:

- background synthesis
- field overview
- terminology and mechanism context
- evidence landscape explanation
- identification of primary research

Boundary:

This value must not be used for an unreviewed blog, media summary, marketing article, or conference presentation. It does not imply systematic methods, quantitative synthesis, or E2 quality automatically.

Compatibility decision:

```text
peer_reviewed_review is formally accepted as canonical in v0.1.
```

### 4.3 Professional Education

#### `professional_education_page`

Description:

```text
Patient, public, or professional education page published by a credible health, academic, clinical, public-health, or professional source.
```

Allowed usage:

- user-facing education
- terminology explanation
- report or measurement context
- safe consultation preparation

Boundary:

Educational content is not automatically a guideline, consensus, or peer-reviewed study.

#### `professional_organization_article`

Description:

```text
Informational article published by a recognized professional organization that is not a formal guideline, consensus statement, or standard education page classification.
```

Allowed usage:

- professional background context
- expert organization perspective
- policy or practice explanation
- source discovery

Boundary:

The article must not be upgraded to `professional_consensus` unless it is formally issued and reviewed as consensus.

### 4.4 Product / Service Documentation

#### `official_product_spec`

Description:

```text
Official manufacturer or provider specification describing product features, components, compatibility, or technical characteristics.
```

Allowed usage:

- feature description
- technical compatibility
- product classification context
- model or version identification

Boundary:

Use for specifications, not proof of health outcomes. Commercial claims require independent support.

#### `official_user_manual`

Description:

```text
Official user manual, instructions for use, support document, or safety instruction supplied by the product maker or provider.
```

Allowed usage:

- operating instructions
- device limitations
- warnings stated by the manufacturer
- data export or setup context

Boundary:

A manual supports intended use and instructions, not independent evidence of effectiveness.

#### `official_service_description`

Description:

```text
Official description of a service's scope, workflow, eligibility, logistics, deliverables, or access conditions.
```

Allowed usage:

- service scope
- process and logistics
- availability context
- deliverable description

Boundary:

It does not verify health outcomes, clinical quality, or personalized need.

### 4.5 Internal Curation

#### `founder_curated`

Description:

```text
Source selection, synthesis, or contextual note curated by the Congtie founder or an explicitly authorized curator.
```

Allowed usage:

- curation rationale
- source selection notes
- internal context
- conservative synthesis pending broader review

Boundary:

Founder curation does not independently raise evidence level or replace external sources.

#### `founder_direct_experience`

Description:

```text
Direct personal observation or experience reported by the founder or authorized curator.
```

Allowed usage:

- anecdotal background
- product or workflow discovery
- questions for future evidence review
- internal hypothesis generation

Boundary:

Direct experience is anecdotal, must not be generalized, and must not be treated as verified health evidence.

### 4.6 Commercial / Weak Sources

#### `commercial_marketing_page`

Description:

```text
Commercial page primarily intended to market or sell a product, service, program, or claim.
```

Allowed usage:

- claim discovery
- commercial-claim documentation
- feature or positioning comparison with caution
- invalid, harmful, or exaggerated claim review

Boundary:

Commercial claims are unverified unless independently supported. Default evidence posture should be conservative.

#### `ecommerce_listing`

Description:

```text
Marketplace or seller listing for a product or service.
```

Allowed usage:

- availability observation
- packaging or listing comparison
- commercial monitoring

Boundary:

Do not use as evidence of effectiveness, safety, authenticity, or suitability. Do not turn purchase links into recommendations.

#### `user_review`

Description:

```text
User-generated product, service, app, device, or experience review.
```

Allowed usage:

- anecdotal experience context
- usability issue discovery
- product claim monitoring

Boundary:

User reviews are anecdotal and must not support clinical, safety, or effectiveness conclusions.

#### `media_article`

Description:

```text
Journalistic, magazine, news, or general media article that is not itself the underlying research or official authority source.
```

Allowed usage:

- topic discovery
- public discourse context
- links to primary sources
- commercialization or policy reporting with verification

Boundary:

Use the underlying primary source whenever possible. A media article is not peer-reviewed evidence.

#### `commercial_claim_unverified`

Description:

```text
Unverified commercial claim captured as source metadata when a more specific source category is insufficient or when the claim itself is the review object.
```

Allowed usage:

- claim tracking
- commercial-risk review
- cautionary explanation
- invalid or harmful information analysis

Boundary:

It must never be presented as verified evidence. Recommended default is `evidence_level: E0` and `evidence_posture: commercial_claim_unverified`.

### 4.7 Canonical Enum Summary

```text
official_guideline_china
official_guideline_international
professional_consensus
peer_reviewed_meta_analysis
peer_reviewed_rct
peer_reviewed_observational
peer_reviewed_mechanistic
peer_reviewed_review
professional_education_page
professional_organization_article
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

Canonical enum count:

```text
20
```

---

## 5. Alias Rules

Aliases are accepted for migration compatibility.

Aliases are not canonical values for new entries.

### 5.1 v0.1 Alias Map

| Alias | Canonical Value | Reason |
|---|---|---|
| `review_article` | `peer_reviewed_review` | Common shortened label for a review article. |
| `academic_review` | `peer_reviewed_review` | Historical label for an academic review. |
| `peer_reviewed_review_article` | `peer_reviewed_review` | Verbose historical form of the canonical value. |

### 5.2 Alias Validation Behavior

When a validator finds an alias, it should:

- accept the value for migration compatibility
- emit a normalization suggestion
- identify the canonical replacement
- preserve the original file unchanged
- avoid silently rewriting existing Markdown

Example warning:

```text
WARNING: source_type alias "review_article" should be normalized to "peer_reviewed_review".
```

Alias presence should not fail migration-oriented validation by itself.

New entries should use the canonical value before human approval or publication.

### 5.3 No Ambiguous Aliases

An alias should map to exactly one canonical value.

Do not add aliases that could refer to multiple source categories.

Example:

```text
review
```

is too ambiguous because it could mean a peer-reviewed review, user review, product review, or editorial review.

### 5.4 Alias Changes

Adding, changing, or removing an alias requires:

- a documented reason
- migration impact review
- collision review
- human approval
- a versioned governance update

---

## 6. Deprecated Values

Deprecated values are previously recognized values that should remain traceable but should not be used in new entries.

### 6.1 Required Deprecation Record

Each deprecated value should record:

```yaml
deprecated_value:
replacement_value:
deprecated_date:
reason:
migration_note:
```

### 6.2 Deprecation Behavior

Deprecated values should:

- remain traceable in historical entries and Git history
- trigger a validator warning
- identify the preferred replacement when one exists
- not be used in new entries
- not be silently rewritten
- not be deleted from historical documentation without review

### 6.3 v0.1 Deprecated List

No canonical values are formally deprecated in v0.1.

```text
deprecated_values = none
```

Values present in older documents but absent from the canonical list are not automatically deprecated. They are unknown to this enum version until separately reviewed and governed.

---

## 7. Validator Rules

This section defines conceptual behavior for a future validator. It does not create validator code.

### 7.1 Required Field

The validator should check:

- `source_type` exists
- `source_type` is a list
- the list is non-empty
- every item is a non-empty string
- the list contains no duplicates

### 7.2 Canonical Values

If every value belongs to the canonical enum:

```text
PASS
```

No normalization message is required.

### 7.3 Alias Values

If a value belongs to the alias map:

```text
ACCEPT WITH WARNING
```

The validator should:

- report the alias
- report the canonical value
- suggest normalization
- not modify the file

### 7.4 Deprecated Values

If a value belongs to the versioned deprecated list:

```text
WARNING
```

The validator should:

- identify it as deprecated
- provide the replacement when available
- preserve traceability
- not silently rewrite the file

Publication governance may require correction before approval even when the structural validator reports a warning rather than an error.

### 7.5 Unknown Values

If a value belongs to neither the canonical enum, alias map, nor deprecated list:

```text
ERROR
```

Example:

```text
ERROR: unknown source_type "unverified_academic_source".
```

The validator must not guess the intended mapping.

### 7.6 Validation Summary

| Input Classification | Validator Result | Automatic Rewrite |
|---|---|---|
| Canonical enum | pass | no |
| Alias | warning with normalization suggestion | no |
| Deprecated value | warning with replacement guidance | no |
| Unknown value | error | no |

### 7.7 Cross-field Boundaries

The validator may report cross-field inconsistencies, but must not infer or rewrite evidence metadata.

Examples:

- `commercial_marketing_page` with E1 should trigger review.
- `ecommerce_listing` used as verified outcome evidence should trigger review.
- `peer_reviewed_review` must not be described as a meta-analysis unless the source supports that classification.
- `official_product_spec` must not be treated as independent proof of health outcomes.

Cross-field checks should produce clear warnings or errors defined by a future validator taskpack.

### 7.8 Error Collection

A future validator should:

- accumulate all enum errors
- show entry ID and file path
- show the invalid value
- distinguish errors from warnings
- avoid stopping at the first problem
- never rewrite canonical Markdown automatically

---

## 8. Future Extension

### 8.1 Adding a Canonical Value

A new canonical source type requires:

- a clear definition
- allowed-use description
- boundary description
- overlap review
- migration impact review
- evidence-framework alignment review
- schema alignment review
- human approval
- a versioned governance update

### 8.2 Future Candidate Review

Older documents may mention source types outside this v0.1 canonical list.

They should be reviewed individually before inclusion, aliasing, or deprecation. This document must not silently assign semantics to them.

### 8.3 Machine-readable Enum

A future version may create:

- JSON Schema enum
- validator constant set
- CMS select options
- migration mapping file
- runtime index metadata

None are created or approved by this document.

Executable schema or enforcement requires a separate Founder Gate.

### 8.4 Versioning

Future versions should preserve:

- historical traceability
- explicit alias maps
- explicit deprecated lists
- migration guidance
- Git history
- no silent file rewriting

### 8.5 Final Governance Rule

```text
Classify the source precisely.
Grade the evidence separately.
Preserve historical values.
Suggest normalization openly.
Never silently rewrite canonical knowledge files.
```
