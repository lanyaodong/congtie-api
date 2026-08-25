# Registry First Wave Pilot A Heart Rate S3 Execution Authorization 2026-08-25 v0.1

Status: Founder Approved C42 Plan / Authorized for Local Heart Rate S3 Execution / Final Version-Control Approval Pending

Founder: 蓝耀栋

Approval and authorization date: 2026-08-25

## 1. Purpose

This document records Founder approval of the exact C42 Heart Rate S3 planning packet and authorizes local execution of its exact six-leaf, Profile-only transition. It does not grant final version-control approval and does not authorize runtime, retrieval, publication, or any product behavior.

## 2. Repository Baseline

- Repository: `/Users/lanyaodong/Documents/congtie-api`
- Branch: `main`
- HEAD: `bdbcbeb766101755beaf152c09bb4ef72f6b1937`
- origin/main: `bdbcbeb766101755beaf152c09bb4ef72f6b1937`
- Execution date: `2026-08-25`
- Initial staging: empty

## 3. Exact C42 Packet

~~~text
Path:
agent/knowledge_seed_v0/registry_first_wave_pilot_a_heart_rate_s3_planning_and_observation_granularity_review_packet_2026_08_25.v0.1.md

SHA-256:
19bbd2cb04a071621c68fcf9df00b99e50b2e8f4af19087fe18a86739163b495

Lines: 496
~~~

The packet remains byte-identical. Its embedded Pending status is the reviewed historical state; this authorization is the authoritative approval record.

## 4. C33 and C41 Lineage

| Artifact | SHA-256 | Governance role |
| --- | --- | --- |
| C33 Founder Approval | `d3d90474ef17233bd8dbe0b7cc39409db061c1b0ee30a45a0e088fe9dac2f0c8` | Approved conservative mixed-Profile S3 model |
| C41 Founder Approval | `d9c03ad141f4cbc646eece2847fede1bfe6ecef62f0e3a8cad76ff1ab8b8ca98` | Approved independent Profile source-lifecycle validation |
| Hardened Permanent Validator | `baf2de87085b697ed2c4a990546f2e29b4c938aec36005ce6d3a3348933bddb2` | Enforces direct source requirements for governed Profiles |

## 5. Current Heart Rate Record

~~~text
Path: agent/biomarker_measurement_registry/records/ME-000020.heart_rate.json
SHA-256 before S3: 1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e
RegistryConcept lifecycle: proposed
Spot Profile: proposed
Wearable PPG Profile: proposed
Version: v0.1
~~~

## 6. Eight Founder Decisions

~~~text
Decision 1:
Existing two PPG sources sufficient; source-content revision prerequisite = no
Founder Decision = Approved

Decision 2:
Wearable PPG Profile scope and raw-waveform exclusion
Founder Decision = Approved

Decision 3:
Point-from-series and time-series Observation representations only
Founder Decision = Approved

Decision 4:
Resting/sleeping/daily/activity/zone/recovery summaries require future Profiles
Founder Decision = Approved

Decision 5:
Profile-aware retrieval/output contract
Founder Decision = Approved

Decision 6:
Exact six-leaf Profile-only S3 plan
Founder Decision = Approved

Decision 7:
Parent and spot remain proposed; version remains v0.1
Founder Decision = Approved

Decision 8:
Local S3 execution
Founder Decision = Authorized

Founder decisions approved = 8/8
Founder pending decisions = 0
~~~

## 7. Core PPG Source Sufficiency Decision

The existing `src-hr-ppg-2020` and `src-interlive-hr` source objects remain sufficient for the narrow wearable PPG Heart Rate estimate Profile. Both sources resolve, remain content-verified, retain appropriate validation-evidence roles, and have no identified correction, retraction, expression of concern, or materially adverse scope change.

No source-content revision prerequisite is required for local S3.

## 8. Class B Newer-Evidence Decision

C42 classified newer 2020-2026 evidence as `Class B - Useful but nonblocking`. It reinforces population, activity, device, firmware, algorithm, processing, missingness, and summary-separation caveats without changing the narrow current Profile.

No newer source may be added by C43. Any later source addition requires a separately approved content revision.

## 9. Approved Wearable Profile Boundary

Approved scope:

> Device-produced, time-stamped Heart Rate estimates derived from wearable photoplethysmography, with explicit device, time-window and provenance context.

The Profile covers only wearable-derived point-from-series and time-series Heart Rate estimates. It does not establish device equivalence, clinical utility, or automatic personal interpretation.

## 10. Raw PPG Waveform Exclusion

~~~text
wearable PPG Heart Rate estimate != raw PPG waveform
~~~

Raw optical waveforms, ECG, rhythm labels, atrial or ventricular rates, spot-clinical Heart Rate, and manual pulse are outside the approved Profile. A raw waveform requires a separate future signal concept and governance Gate.

## 11. Approved Observation Representation Contract

The approved planning representations are limited to:

~~~text
wearable_hr_estimate_point_from_series
wearable_hr_estimate_time_series
~~~

This contract remains planning governance only. C43 does not add it to the Registry record, create an Observation schema, or create user data.

## 12. Approved Summary and Profile Separation

Resting, sleeping, daily, activity, exercise, zone, and recovery summaries require future Profiles with explicit windows, algorithms, missingness rules, provenance, and validation scope. They may not be silently represented by the current time-series Profile.

## 13. Approved Profile-Aware Output Contract

Any future output may identify only `heart_rate.wearable_ppg_time_series_estimate` as `source_verified`. It must not report the parent Heart Rate RegistryConcept or `heart_rate.spot_clinical` as source-verified and must not transfer wearable evidence to the spot Profile.

This contract is not implemented by C43. Runtime and retrieval remain disabled.

## 14. Record-Level Source-Date Semantics

For this transition, `governance_metadata.last_source_check_date` means the latest governed source check relevant to the modified wearable PPG Profile. It does not claim that all four record sources were reopened on that date.

Only the two PPG SourceReference objects actually reopened for C43 may receive `access_date = 2026-08-25`. LOINC and UCUM dates remain `2026-08-22`.

## 15. Exact Permitted S3 Transition

The only lifecycle transition authorized is:

~~~text
heart_rate.wearable_ppg_time_series_estimate.profile_status:
proposed -> source_verified
~~~

The Heart Rate parent remains `proposed`. The spot Profile remains `proposed` with an empty source list. No source object, Profile content, mapping, unit, limitation, permission, claim, threshold, or relation may change.

## 16. Exact Six-Leaf Diff

Authorized leaves:

1. wearable Profile `profile_status`;
2. `src-hr-ppg-2020.access_date`;
3. `src-interlive-hr.access_date`;
4. `governance_metadata.last_modified_date`;
5. `governance_metadata.last_source_check_date`;
6. `governance_metadata.status_note`.

Exact status note:

~~~text
Source verification completed for heart_rate.wearable_ppg_time_series_estimate only. The Heart Rate RegistryConcept and heart_rate.spot_clinical Profile remain proposed. No human review, active status, publication, runtime, retrieval, rhythm diagnosis, clinical claim, threshold or action authorization.
~~~

Expected recursive result:

~~~text
Changed existing scalar leaves = 6
Authorized leaves = 6
Unauthorized leaves = 0
Added keys = 0
Removed keys = 0
SourceReference/Profile additions or removals = 0
Array reordering = 0
~~~

## 17. Expected Final Local Record SHA

With the approved baseline, date, six-leaf diff, original order, UTF-8, LF, two-space indentation, `ensure_ascii = false`, and one final newline, the required local SHA is:

~~~text
b1a110d51112414ec12c40fe5418280013884fa8940acb3c6000d71bda26519f
~~~

No alternate SHA is authorized.

## 18. Version Decision

`version: v0.1` remains unchanged. The transition changes Profile lifecycle and source-check metadata only; it does not revise construct or Profile content.

## 19. Final Founder-Review Requirement

Local execution is not final version-control approval. The resulting exact record, six-leaf diff, source reverification, Schema/Validator results, and C43 review packet require Founder review before any staging, commit, or push.

## 20. Explicit Non-Authorizations

This authorization does not permit parent or spot transition; source-pool or SourceReference edits; new evidence objects; Profile content changes; Observation schema or records; Profile-aware runtime code; human-reviewed or active status; runtime, retrieval, publication, database, API, loader, index, diagnosis, threshold, target, treatment, or action.

## 21. Git Boundary

C43 permits no `git add`, commit, push, amend, rebase, reset, stash, clean, or unrelated restoration. Staging must remain empty, and unrelated working-tree content must remain untouched.

Founder approves the exact SHA-identified C42 Heart Rate S3 planning packet and authorizes local execution of the exact six-leaf Profile-only S3 transition. Authorization applies only to `heart_rate.wearable_ppg_time_series_estimate`. The Heart Rate RegistryConcept and `heart_rate.spot_clinical` remain `proposed`, and `version: v0.1` remains unchanged. The approved Observation-granularity and Profile-aware output contracts remain planning governance only and are not implemented by this task.
