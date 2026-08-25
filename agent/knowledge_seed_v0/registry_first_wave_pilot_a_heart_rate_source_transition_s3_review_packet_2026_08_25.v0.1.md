# Registry First Wave Pilot A Heart Rate Source Transition S3 Review Packet 2026-08-25 v0.1

Status: Draft / Founder Review Pending / Wearable PPG Profile Source-Verified Transition Not Yet Committed

Prepared date: 2026-08-25

## 1. Purpose

This packet presents the locally executed Heart Rate Source Transition S3 for Founder final review. The exact change promotes only `heart_rate.wearable_ppg_time_series_estimate` from `proposed` to `source_verified`, refreshes its two actually reopened PPG source dates, and updates three governance metadata fields.

The Heart Rate parent RegistryConcept and spot Profile remain `proposed`. No Observation contract, runtime behavior, source content, claim, threshold, target, or action was implemented.

## 2. Repository Baseline

- Repository: `/Users/lanyaodong/Documents/congtie-api`
- Branch: `main`
- HEAD: `bdbcbeb766101755beaf152c09bb4ef72f6b1937`
- origin/main: `bdbcbeb766101755beaf152c09bb4ef72f6b1937`
- Execution date: `2026-08-25`
- Initial staging: empty
- Unrelated working tree: inventoried and preserved

## 3. Exact C42 Packet Lineage

~~~text
Path:
agent/knowledge_seed_v0/registry_first_wave_pilot_a_heart_rate_s3_planning_and_observation_granularity_review_packet_2026_08_25.v0.1.md

SHA-256:
19bbd2cb04a071621c68fcf9df00b99e50b2e8f4af19087fe18a86739163b495

Lines: 496
~~~

The C42 packet remains byte-identical. It established Class B newer-evidence handling, the narrow wearable PPG Profile boundary, Observation granularity, Profile-aware output rules, and the exact six-leaf S3 plan.

## 4. C43 Execution Authorization

~~~text
Path:
agent/knowledge_seed_v0/registry_first_wave_pilot_a_heart_rate_s3_execution_authorization_2026_08_25.v0.1.md

SHA-256:
8f20f8bb53f47497bbaee121b61942608fca611a248236f313640e5e1ddff28a

Lines: 215

Status:
Founder Approved C42 Plan / Authorized for Local Heart Rate S3 Execution / Final Version-Control Approval Pending
~~~

The authorization approved all eight C42 decisions and permitted only local execution. It did not authorize staging, commit, push, runtime, retrieval, or publication.

## 5. Heart Rate SHA Before

~~~text
Path: agent/biomarker_measurement_registry/records/ME-000020.heart_rate.json
Working-tree SHA before S3: 1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e
HEAD blob SHA before S3: 1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e
Baseline parity: PASS
~~~

## 6. Heart Rate SHA After

~~~text
Expected SHA-256:
b1a110d51112414ec12c40fe5418280013884fa8940acb3c6000d71bda26519f

Temporary SHA-256:
b1a110d51112414ec12c40fe5418280013884fa8940acb3c6000d71bda26519f

Repository SHA-256:
b1a110d51112414ec12c40fe5418280013884fa8940acb3c6000d71bda26519f

Temporary/repository byte parity: PASS
Deterministic SHA match: PASS
~~~

The revised record remains local and uncommitted.

## 7. Eight Founder Decisions

| # | Decision | Founder result |
| ---: | --- | --- |
| 1 | Existing PPG sources sufficient; no source-content prerequisite | Approved |
| 2 | Narrow wearable Profile and raw-waveform exclusion | Approved |
| 3 | Point-from-series and time-series representations only | Approved |
| 4 | Resting/sleeping/daily/activity/zone/recovery summaries require future Profiles | Approved |
| 5 | Profile-aware retrieval/output contract | Approved |
| 6 | Exact six-leaf Profile-only S3 | Approved |
| 7 | Parent/spot remain proposed; version remains v0.1 | Approved |
| 8 | Separately controlled local S3 execution | Authorized |

~~~text
Founder decisions approved = 8/8
Founder pending C42 decisions = 0
~~~

## 8. Two PPG Sources Reopened

The following existing sources were actually reopened on `2026-08-25`:

1. `src-hr-ppg-2020`, PMID `32552580`, DOI `10.1080/02640414.2020.1767348`;
2. `src-interlive-hr`, PMID `33397674`, DOI `10.1136/bjsports-2020-103148`, PMCID `PMC8273688`.

PubMed metadata was refreshed from official NCBI records. The INTERLIVE lawful open-access full text was also reopened from NCBI PMC.

## 9. Source Reverification Matrix

| Source | Access result | Identity stable | Scope stable | Correction/retraction | Result |
| --- | --- | --- | --- | --- | --- |
| `src-hr-ppg-2020` | PubMed metadata and abstract opened | yes | activity dependence and device/test heterogeneity remain supported | none recorded | PASS |
| `src-interlive-hr` | PubMed metadata and PMC full text opened | yes | target population, criterion, index measure, conditions, processing, and statistics remain supported | none recorded | PASS |

Both source roles remain `validation_evidence`. Existing supports and does-not-support boundaries remain appropriate. No source title, organization, author, date, role, support scope, URL, DOI, PMID, note, or verification status changed.

## 10. Class B Newer-Evidence Decision

The C42 `Class B - Useful but nonblocking` decision remains in force. Newer evidence reinforces context and provenance limitations but does not require a source-content revision before this narrow Profile transition.

No 2022-2026 source was added to the record. Future additions remain separately gated.

## 11. Exact Wearable Profile Lifecycle Change

~~~text
Profile:
heart_rate.wearable_ppg_time_series_estimate

profile_status:
proposed -> source_verified
~~~

This status applies only to the named Profile and its current direct sources. It does not establish equivalence among devices, firmware, algorithms, activities, or derived summaries.

## 12. Parent Lifecycle Non-Change

~~~text
Heart Rate RegistryConcept.lifecycle_status = proposed
~~~

The parent remains `proposed`. The local Profile transition must not be summarized as `Heart Rate = source_verified`.

## 13. Spot Profile Non-Change

~~~text
heart_rate.spot_clinical.profile_status = proposed
heart_rate.spot_clinical.source_reference_keys = []
~~~

Wearable evidence was not transferred to the spot Profile. No spot method source or lifecycle change was introduced.

## 14. Exact Two Source-Date Changes

~~~text
src-hr-ppg-2020.access_date:
2026-08-22 -> 2026-08-25

src-interlive-hr.access_date:
2026-08-22 -> 2026-08-25
~~~

These dates correspond to sources actually reopened for C43.

## 15. LOINC and UCUM Date Non-Change

~~~text
src-loinc-hr.access_date = 2026-08-22
src-ucum.access_date = 2026-08-22
~~~

Neither date was refreshed. The S3 transition is scoped to the two direct wearable Profile sources.

## 16. Governance Metadata Changes

~~~text
governance_metadata.last_modified_date:
2026-08-23 -> 2026-08-25

governance_metadata.last_source_check_date:
2026-08-22 -> 2026-08-25
~~~

`last_source_check_date` means the latest governed source check relevant to the modified wearable Profile. It does not assert that all four record sources were reopened on that date.

Unchanged:

~~~text
created_date = 2026-08-23
reviewed_by = []
reviewed_date = null
~~~

## 17. Exact Status Note

~~~text
Source verification completed for heart_rate.wearable_ppg_time_series_estimate only. The Heart Rate RegistryConcept and heart_rate.spot_clinical Profile remain proposed. No human review, active status, publication, runtime, retrieval, rhythm diagnosis, clinical claim, threshold or action authorization.
~~~

The repository record contains this exact text.

## 18. Exact Six-Leaf Diff

~~~text
Changed existing scalar leaves = 6
Authorized leaves = 6
Unauthorized leaves = 0

Added keys = 0
Removed keys = 0
Added SourceReference objects = 0
Removed SourceReference objects = 0
Added Profiles = 0
Removed Profiles = 0
Array reordering = 0
~~~

Changed leaves:

1. wearable Profile `profile_status`;
2. `src-hr-ppg-2020.access_date`;
3. `src-interlive-hr.access_date`;
4. `governance_metadata.last_modified_date`;
5. `governance_metadata.last_source_check_date`;
6. `governance_metadata.status_note`.

## 19. Deterministic SHA Result

The temporary candidate was serialized as UTF-8 with LF, two-space indentation, `ensure_ascii = false`, original object/array order, and one final newline.

~~~text
Required SHA = b1a110d51112414ec12c40fe5418280013884fa8940acb3c6000d71bda26519f
Actual SHA = b1a110d51112414ec12c40fe5418280013884fa8940acb3c6000d71bda26519f
Match = PASS
~~~

## 20. Observation-Contract Non-Implementation

The approved planning representations remain:

~~~text
wearable_hr_estimate_point_from_series
wearable_hr_estimate_time_series
~~~

C43 added neither representation to the Registry JSON. It created no Observation schema, record, user value, time series, provenance store, or user-health data.

## 21. Profile-Aware Output Non-Implementation

The approved output contract remains governance planning. C43 implemented no retrieval filter, output label, generic Heart Rate response, database, API, loader, or index.

Runtime and retrieval remain disabled.

## 22. JSON Result

~~~text
JSON syntax = PASS
Serialization = PASS
Temporary/repository byte parity = PASS
~~~

## 23. Schema Result

~~~text
Draft 2020-12 instance validation = PASS
Format checking = available
Schema errors = 0
~~~

The mixed parent/Profile lifecycle remains structurally valid under Registry Schema v0.1.

## 24. Hardened Validator Result

~~~text
Result = VALID: Registry concept record
Exit code = 0
Warnings = 0
Errors = 0
Mixed-Profile source lifecycle Gate = PASS
Temporary record checks = 23/23 PASS
~~~

Both direct wearable source keys resolve to `content_verified` sources. Parent and spot lifecycles remain unchanged.

## 25. Candidate Ledger Result

~~~text
Candidate Ledger SHA = b97f4b0e0aeaa4fae6e728c561e88019d3c9e0b34ce353c1cc2b27f5cd09bbe5
Candidate Ledger lineage = PASS
Candidate Ledger modified = false
~~~

## 26. Cross-Registry Result

~~~text
Cross-Registry checks = 25/25 PASS
Registry records = 4
Protected record SHAs = PASS
Source-key resolution = PASS
Governed empty collections = PASS
Human-reviewed records = 0
Active/runtime/retrieval/published = 0
~~~

## 27. Version Decision

~~~text
version = v0.1
~~~

No version bump occurred. The exact change is Profile lifecycle and source-check metadata, not construct or Profile content revision.

## 28. Human-Review Boundary

The Profile is `source_verified`, not `human_reviewed`. `reviewed_by` remains empty and `reviewed_date` remains null. This review packet requests Founder approval of the local bytes and later version-control authorization; it does not itself alter lifecycle.

## 29. Registry State

~~~text
Effective numeric-ID reservations = 4
Registry records = 4

Height RegistryConcept/Profile = source_verified
Body Weight RegistryConcept/Profile = source_verified
Creatinine RegistryConcept/Profile = source_verified

Heart Rate RegistryConcept = proposed
heart_rate.spot_clinical = proposed
heart_rate.wearable_ppg_time_series_estimate = source_verified

Source-verified concepts = 3
Source-verified Profiles = 4
Human-reviewed lifecycle records = 0
Active records = 0
Runtime-enabled records = 0
Retrieval-enabled records = 0
Published records = 0
User observations = 0
~~~

## 30. Explicit Non-Authorizations

C43 does not authorize parent or spot transition; source addition or content edit; newer source incorporation; Profile method/unit/mapping/limitation/permission changes; claims, thresholds, relations, targets, diagnosis, treatment, or action; Observation implementation or user data; human-reviewed or active status; runtime, retrieval, publication, database, API, loader, index, staging, commit, or push.

## 31. Founder Decision Sheet

| # | Decision | Founder Decision |
| ---: | --- | --- |
| 1 | Approve final Heart Rate mixed-lifecycle record with wearable PPG Profile at `source_verified` | Pending |
| 2 | Approve exact six-leaf diff and two-source reverification | Pending |
| 3 | Authorize later controlled commit/push of C42 Packet, C43 Execution Authorization, exact record, this Review Packet and an exact-SHA final Founder Approval Closeout | Pending |

~~~text
Founder approvals = 0
Founder pending decisions = 3
Accidental approvals = 0
~~~

## 32. Recommended Next Gate

After Founder approval of the exact revised Heart Rate SHA and this packet's exact SHA, the next separately controlled task should be:

~~~text
Step5-C44: Final Founder Approval + Controlled Three-Commit Push - Heart Rate Source Transition S3
~~~

C44 may version only the previously approved planning/authorization lineage, the exact unchanged S3 record, and the review/final-approval lineage. It may not modify the record, promote parent or spot lifecycle, implement Observation behavior, or enable runtime/retrieval.

No next Gate is executed automatically.
