# Registry First Wave Pilot A Mixed-Profile Lifecycle Validator Hardening Review Packet 2026-08-25 v0.1

Status: Draft / Founder Review Pending / Validator Hardening Not Yet Committed / Heart Rate S3 Not Authorized

Prepared date: 2026-08-25

## 1. Purpose

This packet presents the locally hardened Permanent Registry Validator for Founder review. The change independently validates source lifecycle requirements for governed Measurement Profiles regardless of parent RegistryConcept lifecycle. It does not approve, commit, or push the Validator and does not execute Heart Rate S3.

## 2. Repository Baseline

- Repository: `/Users/lanyaodong/Documents/congtie-api`
- Branch: `main`
- HEAD: `cdb8003984be5a9b9ae4a6a5aad5ff5ad24bb97b`
- origin/main: `cdb8003984be5a9b9ae4a6a5aad5ff5ad24bb97b`
- Initial staging: empty

## 3. Actual Execution Date

All new C40.1 artifacts use the actual execution date `2026-08-25`. No artifact was backdated and no date exception was used.

## 4. Original C40 Date-Block Record

Original Step5-C40 required `2026-08-24`, while the actual date was `2026-08-25`. It stopped at its precondition with:

`STEP5-C40 BLOCKED — REPOSITORY OR DATE BASELINE MOVED`

## 5. Blocked C40 No-Artifact Confirmation

Before C40.1 began, both old-date authorization and review-packet paths were absent. The blocked C40 attempt created no artifact, changed no code, and performed no staging, commit, or push.

## 6. C33 Mixed-Profile Governance Lineage

~~~text
Path: agent/knowledge_seed_v0/registry_first_wave_pilot_a_source_verified_transition_plan_founder_approval_2026_08_24.v0.1.md
SHA-256: d3d90474ef17233bd8dbe0b7cc39409db061c1b0ee30a45a0e088fe9dac2f0c8
~~~

C33 requires independent source validation for every Profile at `source_verified`, `human_reviewed`, or `active`, including when the parent concept remains `proposed`.

## 7. C39 Registry State

At the C40.1 baseline:

~~~text
Height RegistryConcept/Profile = source_verified
Body Weight RegistryConcept/Profile = source_verified
Creatinine RegistryConcept/Profile = source_verified

Heart Rate RegistryConcept = proposed
heart_rate.spot_clinical = proposed
heart_rate.wearable_ppg_time_series_estimate = proposed

Human-reviewed lifecycle records = 0
Active/runtime/retrieval/published records = 0
~~~

## 8. Validator SHA Before

~~~text
SHA-256: 52ab54488fe8d018d008de3b45a46d16019445c20f36fa0641465c80ef867ff9
Lines: 1376
Snapshot: /tmp/c40_1-validator-before.py
Snapshot parity: PASS
~~~

## 9. Validator SHA After

~~~text
SHA-256: baf2de87085b697ed2c4a990546f2e29b4c938aec36005ce6d3a3348933bddb2
Lines: 1432
Temporary/repository byte parity: PASS
~~~

The hardened Validator remains local and uncommitted.

## 10. Current-Gap Reproduction

The immutable before-snapshot reproduced all four required baseline cases. The baseline self-test also matched exactly `5` valid and `12` invalid fixtures.

| Fixture | Before Semantic | Before Schema | Required baseline reproduced |
| --- | --- | --- | --- |
| Empty Profile source list | ACCEPT, 0 errors | REJECT | yes |
| Resolving pending Profile source | ACCEPT, 0 errors | ACCEPT | yes |
| Dangling Profile source | REJECT by global source-key resolution | ACCEPT | yes |
| Valid mixed Profile with content-verified source | ACCEPT | ACCEPT | yes |

## 11. Empty-Source Result Before and After

~~~text
Before semantic result = ACCEPT
Before Schema result = REJECT

After semantic result = REJECT
After Schema result = REJECT
After semantic diagnostic count = 1
~~~

The new semantic diagnostic is attached to `profiles[0].source_reference_keys` and requires at least one source key for a governed Profile.

## 12. Pending-Source Result Before and After

~~~text
Before semantic result = ACCEPT
Before Schema result = ACCEPT

After semantic result = REJECT
After Schema result = ACCEPT
After semantic diagnostic count = 1
~~~

This closes the primary mixed-Profile governance gap without changing Schema structure.

## 13. Dangling-Source Result Before and After

~~~text
Before semantic result = REJECT
After semantic result = REJECT
Diagnostic authority = existing global source-key resolution
Equivalent duplicate diagnostics after hardening = 0
~~~

`_check_source_statuses()` continues to skip unresolved sources, so the new helper does not duplicate the dangling-key diagnostic.

## 14. Valid Mixed-Profile Result Before and After

~~~text
Parent RegistryConcept lifecycle = proposed
Profile status = source_verified
Profile source = content_verified

Before semantic / Schema = PASS / PASS
After semantic / Schema = PASS / PASS
Parent lifecycle mutation = 0
Profile lifecycle mutation = 0
~~~

## 15. Exact Implementation Summary

The Validator diff is limited to:

1. `PROFILE_SOURCE_GOVERNED_STATUSES` with `source_verified`, `human_reviewed`, and `active`;
2. `_check_profile_source_lifecycle()`;
3. an unconditional helper call from `_check_source_lifecycle()`;
4. removal of the old parent-lifecycle-dependent direct Profile checks;
5. one valid and five invalid mixed-Profile fixtures; and
6. explicit Schema expectations for the new empty-source and pending-source fixtures.

No CLI, exit code, Schema, Ledger, namespace, unit, computation-contract, claim, mapping, runtime, network, file-write, or Heart Rate-specific logic changed.

## 16. Parent-Lifecycle Independence

The helper iterates every Profile and applies its Gate solely from `profile_status`. It executes before parent concept lifecycle branches. Therefore `source_verified`, `human_reviewed`, and `active` Profiles are checked even when the parent concept is `proposed`.

The Validator does not mutate either lifecycle value.

## 17. Duplicate-Diagnostic Avoidance

Direct Profile source keys were removed from `_reviewed_source_sections()`, and the previous direct Profile loop under parent `source_verified` was removed. Definition, ReferenceContext, mapping, claim, computation, and system-relation checks remain in their existing owners.

Verification result:

~~~text
Pending direct-Profile diagnostics = 1
Duplicate equivalent diagnostics = 0
Unexpected Validator function changes = 0
~~~

## 18. Source-Status Policy Non-Change

The following sets are byte-stable:

~~~python
VERIFIED_SOURCE_STATUSES = {"metadata_verified", "content_verified"}
REVIEWED_SOURCE_STATUSES = {"metadata_verified", "content_verified"}
CONTENT_VERIFIED = {"content_verified"}
~~~

The helper calls the existing `_check_source_statuses()` function. C40.1 does not require every direct Profile source to be `content_verified` and does not change SourceReference enums.

## 19. Self-Test Fixture Matrix

| New fixture | Expected semantic result | Expected Schema result | Actual |
| --- | --- | --- | --- |
| Valid proposed concept with source-verified Profile | PASS | PASS | PASS |
| Source-verified Profile without sources | REJECT | REJECT | PASS |
| Source-verified Profile with dangling source | REJECT | not separately required | PASS |
| Source-verified Profile with pending source | REJECT | PASS | PASS |
| Human-reviewed Profile with pending source | REJECT | not separately required | PASS |
| Active Profile with pending source | REJECT | not separately required | PASS |

The active child fixture verifies only the source Gate and does not approve that lifecycle combination as a product governance state.

## 20. Self-Test Counts Before and After

~~~text
Before valid / invalid = 5 / 12

SELF_TEST_VALID_TOTAL=6
SELF_TEST_VALID_PASSED=6
SELF_TEST_VALID_FAILED=0
SELF_TEST_INVALID_TOTAL=17
SELF_TEST_INVALID_REJECTED=17
SELF_TEST_INVALID_ACCEPTED=0
~~~

## 21. Schema-Backed Result

~~~text
SEMANTIC_SELF_TEST=PASS
SCHEMA_BACKED_SELF_TEST=PASS
DRAFT_2020_12_ENGINE=available
Python = 3.9.6
jsonschema = 4.25.1
~~~

The valid mixed Profile passed Schema validation. The empty-source fixture was rejected by Schema, while the resolving pending-source fixture remained structurally valid and was rejected by semantic governance.

## 22. Four-Record Regression Result

| Record | Validator result | Exit | SHA changed |
| --- | --- | ---: | --- |
| Height | VALID | 0 | no |
| Body Weight | VALID | 0 | no |
| Creatinine | VALID | 0 | no |
| Heart Rate | VALID | 0 | no |

Warnings: `0`. Errors: `0`.

## 23. Candidate and Migration Ledger Result

~~~text
Candidate Ledger + Migration Ledger = VALID
Exit = 0
Core candidates = 53
First Wave = 12
Migration rows = 169
First-Wave blockers = 0
~~~

Neither Ledger was modified.

## 24. Schema Integrity

~~~text
Draft 2020-12 Registry Schema = VALID
Schema SHA-256 = a376b02e8cf50e95392287a8924919e57c6df6e37fa957830d4f1a60d1557aa7
Modified = no
~~~

## 25. Dependency Integrity

~~~text
requirements-dev.txt SHA-256 = b362c00c5eab2a8795c02ea136e5773af55e9c845176547f778fa833ed755448
Modified = no
Runtime dependency change = no
~~~

## 26. CI Integrity

~~~text
.github/workflows/ci.yml SHA-256 = 91adf2136a2bf48dd67d4de595e0920c9c32d2413c64fe3aa8e096eccd778b6d
Modified = no
~~~

The existing Registry authoring job already executes compilation, Schema validation, semantic and Schema-backed self-tests, and Ledger validation. No CI change is required.

## 27. Record SHA Integrity

| Record | SHA-256 | Unchanged |
| --- | --- | --- |
| Height | `96434a7232da7f4fe3b91bb299e086ee5ba550378e9524a5bd81d6f202f465a1` | yes |
| Body Weight | `3065394413200d62f2395c761d209f5b8a38ac1e3840bc472b30c103d2d2649b` | yes |
| Creatinine | `396661e7b187beaab9717b042a991dc185a62857f3f1b01a3aa1b4d9d3b51e01` | yes |
| Heart Rate | `1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e` | yes |

## 28. Heart Rate Non-Change

~~~text
Heart Rate RegistryConcept lifecycle = proposed
heart_rate.spot_clinical = proposed
heart_rate.wearable_ppg_time_series_estimate = proposed
Heart Rate source/Profile/mapping changes = 0
Heart Rate S3 executed = no
~~~

## 29. Runtime and Product Non-Authorization

This local Validator hardening does not authorize runtime, retrieval, publication, database, API, loader, index, Observation processing, user-health storage, Service Panel, diagnosis, treatment, personal targets, automatic action, or other product behavior.

## 30. Founder Decision Sheet

| # | Decision | Founder Decision |
| ---: | --- | --- |
| 1 | Approve mixed-Profile lifecycle Validator implementation | Pending |
| 2 | Approve exact 6-valid / 17-invalid self-test result | Pending |
| 3 | Confirm Schema, CI, dependencies and all four Registry records remain unchanged | Pending |
| 4 | Authorize a later controlled commit/push of the exact hardened Validator, execution authorization, review packet and exact-SHA Founder approval closeout | Pending |

~~~text
Founder approvals = 0
Founder pending decisions = 4
Accidental approvals = 0
~~~

## 31. Recommended Next Gate

`Step5-C41: Final Founder Approval + Controlled Commit/Push - Mixed-Profile Lifecycle Validator Hardening`

C41 may submit only the exact hardened Validator, this execution authorization, this review packet, and an exact-SHA Founder approval closeout. It must not modify Heart Rate, execute S3, or change Schema, CI, dependencies, or Registry records.
