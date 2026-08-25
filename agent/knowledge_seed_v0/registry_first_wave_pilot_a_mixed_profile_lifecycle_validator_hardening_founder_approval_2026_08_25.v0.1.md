# Registry First Wave Pilot A Mixed-Profile Lifecycle Validator Hardening Founder Approval 2026-08-25 v0.1

Status: Founder Approved for Version Control / Permanent Validator Hardened / Heart Rate S3 Not Yet Authorized

Founder: 蓝耀栋

Approval date: 2026-08-25

## 1. Purpose

This closeout records Founder approval of the exact C40.1 execution authorization, hardened Permanent Registry Validator, and review packet. It authorizes their controlled three-commit versioning and push while preserving all Registry records and product authorization boundaries.

## 2. Repository Baseline

- Repository: `/Users/lanyaodong/Documents/congtie-api`
- Branch: `main`
- Initial HEAD: `cdb8003984be5a9b9ae4a6a5aad5ff5ad24bb97b`
- Initial origin/main: `cdb8003984be5a9b9ae4a6a5aad5ff5ad24bb97b`
- Approval date: `2026-08-25`
- Initial staging: empty

## 3. Original C40 Date-Block History

Original Step5-C40 required `2026-08-24`, while its actual execution date was `2026-08-25`. It stopped at the date precondition with:

`STEP5-C40 BLOCKED — REPOSITORY OR DATE BASELINE MOVED`

That blocked attempt created no authorization document, review packet, or code change and performed no staging, commit, or push. Step5-C40.1 supplied the correctly dated local execution authorization and did not backdate any artifact.

## 4. Exact C40.1 Execution Authorization

~~~text
Path: agent/knowledge_seed_v0/registry_first_wave_pilot_a_mixed_profile_lifecycle_validator_hardening_execution_authorization_2026_08_25.v0.1.md
SHA-256: 906f73627dbc693bdb4f7ce65cd7eb36c9ca2ec1aaa45c2ca6b8839e9b25f07a
Lines: 131
~~~

The embedded `Final Version-Control Approval Pending` wording is retained as reviewed historical state. This closeout is the authoritative final approval record.

## 5. Exact Validator SHA Before

~~~text
Path: agent/knowledge_seed_v0/scripts/validate_biomarker_measurement_registry.py
SHA-256: 52ab54488fe8d018d008de3b45a46d16019445c20f36fa0641465c80ef867ff9
Lines: 1376
~~~

## 6. Exact Validator SHA After

~~~text
Path: agent/knowledge_seed_v0/scripts/validate_biomarker_measurement_registry.py
SHA-256: baf2de87085b697ed2c4a990546f2e29b4c938aec36005ce6d3a3348933bddb2
Lines: 1432
Diff: 69 insertions, 13 deletions
~~~

## 7. Exact C40.1 Review Packet

~~~text
Path: agent/knowledge_seed_v0/registry_first_wave_pilot_a_mixed_profile_lifecycle_validator_hardening_review_packet_2026_08_25.v0.1.md
SHA-256: 78827062fe98e85a8230c30f07f97e34fbf02a85e5706b1fbf3063d452d5a052
Lines: 311
~~~

The packet's embedded `Draft / Founder Review Pending` status and four pending decisions are retained as reviewed historical bytes. This closeout resolves all four decisions.

## 8. Pre-Hardening Gap Reproduction

The immutable Validator-before snapshot reproduced the governed mixed-Profile gap:

| Fixture | Before Semantic | Before Schema |
| --- | --- | --- |
| Source-verified Profile with empty source list | ACCEPT | REJECT |
| Source-verified Profile with resolving pending source | ACCEPT | ACCEPT |
| Source-verified Profile with dangling source | REJECT by global source-key resolution | ACCEPT |
| Proposed concept with source-verified Profile and content-verified source | PASS | PASS |

The baseline self-test was exactly `5` valid and `12` invalid fixtures.

## 9. Exact Implementation Scope

The approved implementation is limited to:

1. `PROFILE_SOURCE_GOVERNED_STATUSES` for `source_verified`, `human_reviewed`, and `active`;
2. `_check_profile_source_lifecycle()`;
3. unconditional helper wiring in `_check_source_lifecycle()`;
4. removal of superseded duplicate direct-Profile checks from `_reviewed_source_sections()` and the parent-lifecycle branch;
5. one valid and five invalid mixed-Profile fixtures; and
6. Schema-backed assertions for the empty-source and pending-source fixtures.

No CLI, exit-code, Schema, Ledger, namespace, unit, computation-contract, claim, mapping, runtime, network, repository-write, lifecycle-mutation, or Heart Rate-specific logic changed.

## 10. Parent-Lifecycle Independence

Every Measurement Profile whose `profile_status` is `source_verified`, `human_reviewed`, or `active` now receives direct source-lifecycle validation independently of the parent RegistryConcept lifecycle. The helper executes before the parent lifecycle branches and does not mutate either lifecycle field.

## 11. Duplicate-Diagnostic Avoidance

Direct Profile source checks have one semantic owner. Existing global source-key resolution remains the sole owner of dangling-source diagnostics, while the new helper skips unresolved sources after that resolution check.

~~~text
Pending direct-Profile diagnostics = 1
Dangling direct-Profile diagnostics = 1 global-resolution diagnostic
Duplicate equivalent diagnostics = 0
Unexpected Validator function changes = 0
~~~

## 12. Source-Status Policy Non-Change

The approved change reuses `_check_source_statuses()` and leaves these policies unchanged:

~~~python
VERIFIED_SOURCE_STATUSES = {"metadata_verified", "content_verified"}
REVIEWED_SOURCE_STATUSES = {"metadata_verified", "content_verified"}
CONTENT_VERIFIED = {"content_verified"}
~~~

No SourceReference enum or source-role policy changed.

## 13. Self-Test Fixture Matrix

| New fixture | Semantic result | Schema result | Approved result |
| --- | --- | --- | --- |
| Proposed concept + source-verified Profile + content-verified source | PASS | PASS | PASS |
| Source-verified Profile without sources | REJECT, one diagnostic | REJECT | PASS |
| Source-verified Profile with dangling source | REJECT, one global diagnostic | structural PASS | PASS |
| Source-verified Profile with pending source | REJECT, one diagnostic | PASS | PASS |
| Human-reviewed Profile with pending source | REJECT | structural PASS | PASS |
| Active Profile with pending source | REJECT | structural PASS | PASS |

## 14. Exact 6-Valid / 17-Invalid Results

~~~text
SELF_TEST_VALID_TOTAL=6
SELF_TEST_VALID_PASSED=6
SELF_TEST_VALID_FAILED=0
SELF_TEST_INVALID_TOTAL=17
SELF_TEST_INVALID_REJECTED=17
SELF_TEST_INVALID_ACCEPTED=0
SEMANTIC_SELF_TEST=PASS
~~~

Founder approval binds to these exact fixture totals and results.

## 15. Schema-Backed Result

~~~text
SCHEMA_BACKED_SELF_TEST=PASS
DRAFT_2020_12_ENGINE=available
Python=3.9.6
jsonschema=4.25.1
~~~

The valid mixed Profile passes Schema validation. The empty-source fixture is structurally rejected, while the pending-source fixture remains structurally valid and is rejected by semantic governance.

## 16. Four-Record Regression

| Record | Result | Exit | SHA unchanged |
| --- | --- | ---: | --- |
| Height | VALID | 0 | yes |
| Body Weight | VALID | 0 | yes |
| Creatinine | VALID | 0 | yes |
| Heart Rate | VALID | 0 | yes |

Warnings: `0`. Errors: `0`.

## 17. Candidate and Migration Ledger Result

~~~text
Candidate Ledger + Migration Ledger = VALID
Exit = 0
Core candidates = 53
First Wave = 12
Migration rows = 169
First-Wave blockers = 0
~~~

Both Ledgers remain byte-identical.

## 18. Schema Integrity

~~~text
Registry Schema SHA-256: a376b02e8cf50e95392287a8924919e57c6df6e37fa957830d4f1a60d1557aa7
Draft 2020-12 definition result: VALID
Modified: no
~~~

## 19. Dependency Integrity

~~~text
requirements-dev.txt SHA-256: b362c00c5eab2a8795c02ea136e5773af55e9c845176547f778fa833ed755448
jsonschema[format]: 4.25.1
Runtime dependency change: no
Modified: no
~~~

## 20. CI Integrity

~~~text
.github/workflows/ci.yml SHA-256: 91adf2136a2bf48dd67d4de595e0920c9c32d2413c64fe3aa8e096eccd778b6d
Modified: no
~~~

The existing authoring-validation job already runs compilation, Schema validation, semantic and Schema-backed self-tests, and Ledger validation.

## 21. Registry-Record SHA Integrity

| Record | SHA-256 | Unchanged |
| --- | --- | --- |
| Height | `96434a7232da7f4fe3b91bb299e086ee5ba550378e9524a5bd81d6f202f465a1` | yes |
| Body Weight | `3065394413200d62f2395c761d209f5b8a38ac1e3840bc472b30c103d2d2649b` | yes |
| Creatinine | `396661e7b187beaab9717b042a991dc185a62857f3f1b01a3aa1b4d9d3b51e01` | yes |
| Heart Rate | `1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e` | yes |

Registry record changes in C41: `0`. Registry lifecycle changes in C41: `0`.

## 22. Parent-Child Lifecycle Scope Clarification

C40.1 hardens direct Profile source-lifecycle validation only. It does not approve every possible parent/child lifecycle combination. In particular, the active-child self-test verifies only that an `active` Profile cannot rely on a pending source; it does not establish that a `proposed` parent with an `active` child is an approved product-governance state.

Heart Rate S3 concerns only a `proposed` parent with a `source_verified` wearable Profile. Parent-child consistency for `human_reviewed` or `active` states, if later needed, requires a separate governance Gate. C41 adds no such rule.

## 23. Heart Rate S3 Non-Authorization

~~~text
Heart Rate RegistryConcept.lifecycle_status = proposed
heart_rate.spot_clinical.profile_status = proposed
heart_rate.wearable_ppg_time_series_estimate.profile_status = proposed
Heart Rate S3 executed = no
Heart Rate record modified = no
~~~

This Validator hardening is an S3 prerequisite only. It does not approve or execute any Heart Rate transition.

## 24. Runtime and Product Non-Authorization

This approval does not authorize runtime, retrieval, publication, database, API, loader, index, Observation processing, user-health storage, Service Panel, diagnosis, treatment, personal targets, automatic action, or other product behavior. It creates no Registry record and changes no source, Profile, mapping, claim, threshold, relation, permission, or action boundary.

## 25. Founder Decisions and Exact Approval

| # | Decision | Founder Decision |
| ---: | --- | --- |
| 1 | Mixed-Profile lifecycle Validator implementation | Approved |
| 2 | Exact 6-valid / 17-invalid self-test result | Approved |
| 3 | Schema, Candidate Ledger, Migration Ledger, dependencies, CI, and all four Registry records unchanged | Confirmed |
| 4 | Controlled three-commit push | Approved |

~~~text
Founder decisions approved = 4/4
Founder pending decisions = 0
Heart Rate S3 = Not authorized
Registry lifecycle changes = 0
Runtime/retrieval/product behavior changes = 0
~~~

Founder approves the exact SHA-identified hardened Permanent Registry Validator for version control. The approved implementation independently enforces source lifecycle requirements for every Measurement Profile at `source_verified`, `human_reviewed`, or `active`, regardless of the parent RegistryConcept lifecycle. Approval binds to the exact `6/6` valid and `17/17` invalid self-test results. It does not modify any Registry record, execute Heart Rate S3, promote any lifecycle, or authorize runtime, retrieval, publication, database, API, Observation processing, user-health storage or product action.

## 26. Git Commit Plan

The approved history is three strictly separated commits followed by one non-force push to `origin/main`:

1. `docs: authorize mixed-profile lifecycle validator hardening`
   - C40.1 Execution Authorization only.
2. `fix: harden Registry mixed-profile source lifecycle validation`
   - Hardened Permanent Validator only.
3. `docs: approve mixed-profile lifecycle validator hardening`
   - C40.1 Review Packet and this C41 Founder Approval Closeout only.

No amend, squash, rebase, force push, tag push, or other-branch push is authorized.

## 27. Next Gate

After controlled versioning and post-push verification, the only recommended next task is:

`Step5-C42: Heart Rate S3 Planning - Wearable PPG Profile Source Reverification + Observation-Granularity Acceptance + Exact Profile-Only Transition Plan`

C42 must begin with planning and source review. It must not automatically modify Heart Rate or execute S3.
