# Registry First Wave Pilot A Creatinine S2 Source Addition Review Packet 2026-08-24 v0.1

Status: Draft / Founder Review Pending / Creatinine Source Content Revision Not Yet Committed / Lifecycle Remains Proposed

## 1. Purpose

This packet presents the local Creatinine S2 prerequisite content revision for Founder review. It adds exact NIDDK provenance for the existing serum-creatinine unit conversion and links that source to the existing enzymatic Profile. It does not execute a source_verified lifecycle transition.

## 2. Repository Baseline

- Repository: /Users/lanyaodong/Documents/congtie-api
- Branch: main
- HEAD: 2c7c871d74267ad455f550db97cd068461d32490
- origin/main: 2c7c871d74267ad455f550db97cd068461d32490
- Initial staging: empty
- Execution date: 2026-08-24

## 3. Exact C33 and S1 Lineage

| Artifact | SHA-256 |
| --- | --- |
| C33 Source-Verified Transition Plan | dd627b31e887553b85179da78f47a504ef7da5df8113b6154bbcee4ec5f70121 |
| C33 Transition Plan Founder Approval | d3d90474ef17233bd8dbe0b7cc39409db061c1b0ee30a45a0e088fe9dac2f0c8 |
| Final S1 Review Packet | 0ab06764555e9261f27dfd9c832d800385c1bb830530d72451b8e2377bdfc932 |
| S1 Founder Approval | 9b53c1fc77ae104d7f106af796eed345452de2f410a265a4a42646b1ab872418 |

C33 requires an exact NIDDK conversion source addition before Creatinine S2 lifecycle review. S1 changed only Height and Body Weight.

## 4. Creatinine SHA Before

Path: agent/biomarker_measurement_registry/records/BM-000023.creatinine.json

SHA-256: fa6b2ad250c6c1f8f2e4df6428970eebd5e6497061533f110dabe99c0549cbab

## 5. Creatinine SHA After

Local revised SHA-256: c8fd286a46334e2f9a4856503de37ff5d8f5dcdfc7128f8e5a7308ae75ae0fa6

The revised record is not staged or committed.

## 6. NIDDK Source Identity

- Source key: src-niddk-creatinine-conversion
- Exact title: eGFR Equations for Adults
- Organization: National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK)
- URL: https://www.niddk.nih.gov/research-funding/research-programs/kidney-clinical-research-epidemiology/laboratory/glomerular-filtration-rate-equations/adults
- Source role: other_reviewed_role
- Verification status: content_verified
- Page last reviewed: May 2025

## 7. NIDDK Actual Access Result

The official NIDDK page was opened and content-reviewed on 2026-08-24. It was accessible, retained the expected title and NIDDK identity, and displayed no withdrawal, deprecation, or supersession notice. A general NIH website-migration banner did not alter the source content.

## 8. Exact Conversion Statement

The page states:

> serum creatinine µmol/L to mg/dL, divide by 88.4

It also defines SCr as standardized serum creatinine in mg/dL within the adult eGFR equation context.

## 9. Algebraic Inverse Relationship

The NIDDK statement is algebraically equivalent to the existing Registry rule:

value_mg/dL * 88.4 = value_umol/L

This source supports the numerical unit conversion and standardized-input context. It does not establish assay or platform equivalence, a reference interval, diagnosis, personal target, or action.

## 10. Exact SourceReference Object

~~~json
{
  "source_key": "src-niddk-creatinine-conversion",
  "title": "eGFR Equations for Adults",
  "organization_or_journal": "National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK)",
  "authors": [],
  "publication_date": null,
  "source_type": null,
  "source_role": "other_reviewed_role",
  "supports": [
    "serum creatinine unit conversion using factor 88.4 between umol/L and mg/dL",
    "standardized serum creatinine input context for adult eGFR equations"
  ],
  "does_not_support": [
    "assay or platform equivalence",
    "reference interval",
    "diagnosis",
    "personal target or action"
  ],
  "url": "https://www.niddk.nih.gov/research-funding/research-programs/kidney-clinical-research-epidemiology/laboratory/glomerular-filtration-rate-equations/adults",
  "doi": null,
  "pmid": null,
  "access_date": "2026-08-24",
  "verification_status": "content_verified",
  "note": "Official unit-conversion authority; page last reviewed May 2025."
}
~~~

The object is appended as source number 7. The original six source objects retain their exact order and content.

## 11. Source-Pool Change

~~~text
Existing source count: 6
Revised source count: 7
New source objects: 1
Duplicate source keys: 0
definition_source_keys changes: 0
~~~

## 12. Profile Source-Key Change

Profile: creatinine.serum_or_plasma.enzymatic

~~~json
[
  "src-nist-creat",
  "src-creat-method-2020",
  "src-wst4045",
  "src-niddk-creatinine-conversion"
]
~~~

The Profile source-key count changes from 3 to 4. Existing keys retain their exact order. No mapping source keys change.

## 13. Governance-Date Changes

~~~text
governance_metadata.last_modified_date:
2026-08-23 -> 2026-08-24

governance_metadata.last_source_check_date:
2026-08-22 -> 2026-08-24
~~~

created_date, reviewed_by, reviewed_date, and status_note remain byte-identical.

## 14. Lifecycle Unchanged

~~~text
RegistryConcept.lifecycle_status = proposed
creatinine.serum_or_plasma.enzymatic.profile_status = proposed
~~~

Source completion in this content revision does not constitute lifecycle promotion.

## 15. Version Unchanged

Version remains v0.1.

The revision adds exact source provenance for an already-existing conversion rule. It does not change the Creatinine construct, Profile boundary, method, accepted units, conversion formula, mappings, interpretation limitations, or Agent permissions. Git preserves the content-revision history.

Founder Decision: Pending

## 16. Conversion Rule Unchanged

~~~text
conversion_rule = value_mg/dL * 88.4 = value_umol/L
conversion_verified = true
~~~

No conversion value, direction, accepted unit, or canonical unit changed.

## 17. Method, Mapping, and Permission Boundaries Unchanged

- Profile key, method, specimen, protocol context, and comparability are unchanged.
- LOINC mappings and mapping source keys are unchanged.
- Interpretation limitations are unchanged.
- Agent permissions and personalized-target boundaries are unchanged.
- Claims, reference contexts, system relations, lifecycle relations, and device mappings remain empty.

## 18. Schema Result

The temporary and repository copies pass JSON syntax and the Draft 2020-12 Registry Schema using Python 3.9.6 and jsonschema 4.25.1.

Result: PASS

## 19. Permanent Validator Result

The temporary and repository copies pass:

~~~text
VALID: Registry concept record
~~~

Candidate Ledger lineage resolves. Warnings: 0. Errors: 0.

## 20. Deep-Diff Result

~~~text
Added SourceReference objects = 1
Added Profile source-key references = 1
Changed existing scalar leaves = 2
Removed keys = 0
Reordered arrays = 0
Unauthorized changes = 0
~~~

Result: PASS

## 21. Protected-Record Integrity

| Record | Expected SHA-256 | Result |
| --- | --- | --- |
| Height | 96434a7232da7f4fe3b91bb299e086ee5ba550378e9524a5bd81d6f202f465a1 | Unchanged |
| Body Weight | 3065394413200d62f2395c761d209f5b8a38ac1e3840bc472b30c103d2d2649b | Unchanged |
| Heart Rate | 1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e | Unchanged |

Registry Schema, Candidate Ledger, Migration Ledger, Permanent Validator, allocation assets, Registry READMEs, C33/S1 documents, product assets, and user-data boundaries remain unchanged.

## 22. Registry State

~~~text
Effective numeric-ID reservations = 4
Registry records = 4

Height concept/Profile = source_verified
Body Weight concept/Profile = source_verified

Creatinine concept = proposed
creatinine.serum_or_plasma.enzymatic = proposed
Creatinine source count = 7

Heart Rate concept and both Profiles = proposed

Human-reviewed lifecycle records = 0
Active records = 0
Runtime-enabled records = 0
Retrieval-enabled records = 0
Published records = 0
~~~

## 23. Explicit Non-Authorizations

This review packet does not authorize:

- Creatinine lifecycle or Profile-status transition;
- Heart Rate S3;
- claims, thresholds, reference contexts, system relations, lifecycle relations, or device mappings;
- method, mapping, formula, unit, interpretation, or Agent-permission changes;
- runtime, retrieval, publication, database, API, loader, index, Observation processing, user-health storage, diagnosis, treatment, target, or action;
- staging, commit, or push.

## 24. Founder Decision Sheet

| # | Decision | Founder Decision |
| -: | --- | --- |
| 1 | Approve exact NIDDK SourceReference object | Pending |
| 2 | Approve linkage to creatinine.serum_or_plasma.enzymatic | Pending |
| 3 | Approve version v0.1 remaining unchanged | Pending |
| 4 | Approve final revised Creatinine record at SHA c8fd286a46334e2f9a4856503de37ff5d8f5dcdfc7128f8e5a7308ae75ae0fa6 | Pending |
| 5 | Authorize a later controlled commit/push of the content revision and exact-SHA approval closeout, without lifecycle transition | Pending |

~~~text
Founder approvals = 0
Founder pending decisions = 5
Accidental approvals = 0
~~~

## 25. Recommended Next Gate

Founder and ChatGPT review:

1. the exact NIDDK SourceReference;
2. the Profile source linkage;
3. the revised Creatinine SHA;
4. the v0.1 version decision; and
5. this C36 Review Packet.

Do not commit automatically. Do not execute the Creatinine source_verified lifecycle transition automatically.
