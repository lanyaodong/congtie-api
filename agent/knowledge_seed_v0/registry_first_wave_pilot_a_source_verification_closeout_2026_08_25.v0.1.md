# Registry First Wave Pilot A Source-Verification Closeout 2026-08-25 v0.1

Status: Draft / Founder Review Pending / Pilot A Approved Bounded Source-Verification Scope Completed in Git / Human Review, Active, Runtime and Retrieval Not Authorized

Prepared date: 2026-08-25

## 1. Purpose

This closeout records the exact Git state reached by the approved, bounded Pilot A source-verification work. It closes S1, S2, the mixed-Profile Validator prerequisite, and S3 as a governance sequence without claiming that every Pilot A concept or Profile has the same lifecycle.

Pilot A's approved bounded source-verification work is complete in Git: S1 source-verified Height and Body Weight; S2 source-verified Creatinine after its separately approved NIDDK conversion-source prerequisite; C40.1 versioned mixed-Profile Validator hardening; and S3 source-verified only the wearable PPG Heart Rate Profile. This closeout does not assert that every Pilot A RegistryConcept or every Pilot A Profile is source-verified.

## 2. Repository and Git Anchor

```text
Repository: /Users/lanyaodong/Documents/congtie-api
Branch: main
HEAD: 1560cd562b8896e420f296066a6115029b37cefd
origin/main: 1560cd562b8896e420f296066a6115029b37cefd
Prepared date: 2026-08-25
Staging at audit: empty
```

## 3. Pilot A Initial Record-Production Lineage

The four effective reservations were versioned before record production. The four canonical proposed records were then created under the approved flat storage convention and validated before Founder approval and push.

```text
7d9e929  docs: establish Registry First Wave and storage convention
1a7015d  feat: reserve Pilot A Registry numeric IDs
b1b7153  feat: add Pilot A proposed Registry records
674b62b  docs: approve Pilot A proposed Registry records
```

The resulting concept set is exactly Height, Body Weight, Creatinine, and Heart Rate. No standalone Profile file was created.

## 4. Effective Numeric-ID Reservations

| Candidate | Namespace | Effective reservation | Canonical record path |
| --- | --- | --- | --- |
| `height` | ME | `ME-000018` | `agent/biomarker_measurement_registry/records/ME-000018.height.json` |
| `body_weight` | ME | `ME-000019` | `agent/biomarker_measurement_registry/records/ME-000019.body_weight.json` |
| `creatinine` | BM | `BM-000023` | `agent/biomarker_measurement_registry/records/BM-000023.creatinine.json` |
| `heart_rate` | ME | `ME-000020` | `agent/biomarker_measurement_registry/records/ME-000020.heart_rate.json` |

These IDs are permanent, non-semantic, and non-reusable. Reservation did not create a Registry record or lifecycle promotion.

## 5. S1 Completion

S1 source-verified the Height and Body Weight concepts and their single initial Profiles. The approved transition changed only lifecycle, Profile status, reopened-source access dates, source-check dates, and exact status notes.

```text
d1d8068  docs: approve Pilot A source transition plan
2d54b75  feat: source-verify Height and Body Weight Registry records
2c7c871  docs: approve Pilot A source transition S1
```

S1 did not add claims, thresholds, mappings, Profiles, human review, runtime, or retrieval.

## 6. Creatinine Source-Content Prerequisite

Before S2, the Creatinine record received the separately reviewed NIDDK conversion provenance for the existing `mg/dL x 88.4 = umol/L` rule. The source addition and Profile linkage were content revisions, not lifecycle promotion.

```text
dcd6b94  feat: add NIDDK conversion provenance to Creatinine Registry record
a99b531  docs: approve Creatinine conversion-source revision
```

The conversion source does not establish assay equivalence, a reference interval, diagnosis, or a personal target.

## 7. S2 Completion

S2 subsequently source-verified the Creatinine concept and `creatinine.serum_or_plasma.enzymatic` Profile after the conversion-source prerequisite and source-role audit passed.

```text
ad136fb  docs: authorize Creatinine source transition S2
2b9a10a  feat: source-verify Creatinine Registry record
cdb8003  docs: approve Creatinine source transition S2
```

Jaffe and other assay/platform Profiles remain deferred. S2 did not establish cross-method equivalence or clinical utility.

## 8. Mixed-Profile Validator Prerequisite

C40.1 hardened the Permanent Validator before S3. The Validator now evaluates every Profile at `source_verified`, `human_reviewed`, or `active` independently of the parent concept lifecycle, including source-key non-emptiness, resolution, and allowed source lifecycle.

```text
d5f0d2f  docs: authorize mixed-profile lifecycle validator hardening
7b8d68a  fix: harden Registry mixed-profile source lifecycle validation
bdbcbeb  docs: approve mixed-profile lifecycle validator hardening

Final Validator SHA-256:
baf2de87085b697ed2c4a990546f2e29b4c938aec36005ce6d3a3348933bddb2
```

This hardening did not promote any record and did not authorize product output.

## 9. S3 Completion

S3 source-verified only `heart_rate.wearable_ppg_time_series_estimate`. The Heart Rate parent and `heart_rate.spot_clinical` remained `proposed`.

```text
6a4b3d7  docs: approve Heart Rate S3 plan and authorize execution
42203f8  feat: source-verify wearable PPG Heart Rate Profile
1560cd5  docs: approve Heart Rate source transition S3
```

The two wearable PPG sources support the bounded Profile. They do not establish ECG equivalence, rhythm diagnosis, every device, or cross-device normalization.

## 10. C44 Exact Three-Commit Lineage

| Commit | Parent | Message | Exact scope |
| --- | --- | --- | --- |
| `6a4b3d70919cb1b0b356379558ca669070138176` | `bdbcbeb766101755beaf152c09bb4ef72f6b1937` | `docs: approve Heart Rate S3 plan and authorize execution` | C42 packet and C43 execution authorization |
| `42203f8e5d0b3d0c6562b96f2d065d939956e096` | `6a4b3d70919cb1b0b356379558ca669070138176` | `feat: source-verify wearable PPG Heart Rate Profile` | Heart Rate record only |
| `1560cd562b8896e420f296066a6115029b37cefd` | `42203f8e5d0b3d0c6562b96f2d065d939956e096` | `docs: approve Heart Rate source transition S3` | C43 review packet and C44 approval closeout |

The local HEAD, `origin/main`, and remote `main` resolved to the third commit during the C45 audit.

## 11. Four Final Record Paths and SHAs

| Record | Path | Final SHA-256 |
| --- | --- | --- |
| Height | `agent/biomarker_measurement_registry/records/ME-000018.height.json` | `96434a7232da7f4fe3b91bb299e086ee5ba550378e9524a5bd81d6f202f465a1` |
| Body Weight | `agent/biomarker_measurement_registry/records/ME-000019.body_weight.json` | `3065394413200d62f2395c761d209f5b8a38ac1e3840bc472b30c103d2d2649b` |
| Creatinine | `agent/biomarker_measurement_registry/records/BM-000023.creatinine.json` | `396661e7b187beaab9717b042a991dc185a62857f3f1b01a3aa1b4d9d3b51e01` |
| Heart Rate | `agent/biomarker_measurement_registry/records/ME-000020.heart_rate.json` | `b1a110d51112414ec12c40fe5418280013884fa8940acb3c6000d71bda26519f` |

## 12. Exact Final Concept/Profile Lifecycle Matrix

| RegistryConcept | Concept lifecycle | Profile | Profile lifecycle |
| --- | --- | --- | --- |
| Height | `source_verified` | `height.standing.stadiometer` | `source_verified` |
| Body Weight | `source_verified` | `body_weight.scale_measured` | `source_verified` |
| Creatinine | `source_verified` | `creatinine.serum_or_plasma.enzymatic` | `source_verified` |
| Heart Rate | `proposed` | `heart_rate.spot_clinical` | `proposed` |
| Heart Rate | `proposed` | `heart_rate.wearable_ppg_time_series_estimate` | `source_verified` |

## 13. Source-Verified Concept/Profile Counts

```text
Registry records = 4
Source-verified RegistryConcepts = 3
Source-verified Profiles = 4
Human-reviewed lifecycle records = 0
Active records = 0
```

Counts are derived from the canonical record JSON, not from this closeout.

## 14. Schema and Validator Result

The final C45 verification used Python `3.9.6`, `jsonschema 4.25.1`, the Draft 2020-12 Registry Schema, and the hardened Permanent Validator.

```text
Python compile = PASS
Semantic self-test valid fixtures = 6/6
Semantic self-test invalid fixtures rejected = 17/17
Schema-backed self-test = PASS
Draft 2020-12 engine = available
Four canonical records = 4/4 VALID
Warnings = 0
Errors = 0
```

## 15. Candidate/Migration Ledger Result

```text
Candidate Ledger + Migration Ledger = VALID
Core candidates = 53
First Wave candidates = 12
Migration rows = 169
First-Wave migration blockers = 0
Silent migration loss = 0
```

Candidate planning remains separate from canonical records and effective ID reservations.

## 16. Version Decisions

All four records remain `version: v0.1`. The approved source-content and lifecycle transitions preserved stable concept/Profile boundaries. Git carries the revision history; no lifecycle-only change was treated as a new construct version.

## 17. Heart Rate Critical Mixed-Lifecycle Wording

```text
Heart Rate RegistryConcept = proposed
heart_rate.spot_clinical = proposed
heart_rate.wearable_ppg_time_series_estimate = source_verified
```

The phrase `Heart Rate is source_verified` is prohibited because it erases the parent/Profile distinction. A source-verified child Profile does not promote its parent or sibling.

## 18. Observation Contract Status

No Observation schema, storage, ingestion, or user observation was created. Future Heart Rate observations must distinguish time-stamped points, device-produced series, window summaries, resting summaries, sleeping summaries, and activity summaries while retaining device, firmware, algorithm, cadence, window, activity context, artifacts, timestamps, and time zone.

## 19. Profile-Aware Output Contract Status

The governance requirement for Profile-aware output is documented, but runtime filtering is not enabled. A product must not present a parent concept as uniformly verified when only one Profile is verified. No retrieval or output implementation is authorized by this closeout.

## 20. Deferred Pilot A Items

| Area | Deferred, not forgotten |
| --- | --- |
| Height | self-reported Profile; pediatric interpretation |
| Body Weight | household-scale-specific Profile; self-reported Profile; body composition remains separate |
| Creatinine | Jaffe Profile; other assay/platform Profiles; `human_reviewed`/`active`; reference contexts; use-evidence claims |
| Heart Rate | spot-clinical method source and possible boundary narrowing; resting, sleeping, activity/exercise, daily, zone, and recovery summary Profiles; raw PPG waveform concept/Profile; ECG-derived Profile; Observation schema/ingestion; Profile-aware runtime output |
| Cross-cutting | human review; active lifecycle; runtime/retrieval; publication; Observation/user-health implementation; personal targets; clinical claims; thresholds; actions |

## 21. Human-Review Lifecycle Boundary

Source verification establishes bounded source support. It is not Founder human review of a Registry lifecycle state. No record has `lifecycle_status: human_reviewed`, no `reviewed_by` identity was added, and no `reviewed_date` was set.

## 22. Runtime, Retrieval, and Publication Boundary

```text
Runtime-enabled records = 0
Retrieval-enabled records = 0
Published records = 0
```

Git versioning and source verification do not authorize product loading, ranking, retrieval, publication, or clinical output.

## 23. User-Data Boundary

```text
User observations = 0
Personal health records = 0
Observation storage = not implemented
```

The Registry stores public concept governance, not individual measurements or user-health context.

## 24. Claims, Thresholds, and Action Boundary

The four records contain no use-evidence claims, public threshold contexts, system relations, or device mappings from these transitions. No diagnosis, treatment, personal target, automated action, or critical-value workflow is authorized.

## 25. Git Closeout State

The Pilot A bounded source-verification sequence is committed and pushed through `1560cd562b8896e420f296066a6115029b37cefd`. This C45 closeout itself is untracked and pending Founder review; it makes no lifecycle or operational change.

## 26. Founder Decision Sheet

| # | Decision | Founder Decision |
| ---: | --- | --- |
| 1 | Approve the exact Pilot A bounded source-verification closeout state | Pending |
| 2 | Approve the final mixed-lifecycle wording for Heart Rate | Pending |
| 3 | Authorize a later controlled commit/push of this exact closeout document | Pending |

```text
Founder approvals = 0
Founder pending decisions = 3
Accidental approvals = 0
```

## 27. Recommended Next Gate

```text
Step5-C46: Founder Review + Controlled Commit/Push - Pilot A Source-Verification Closeout and Pilot B Readiness Audit
```

C46 may create an exact-SHA approval closeout and version the two C45 documents. It must not create Pilot B records or IDs, modify Pilot A records, or change lifecycle/runtime state.
