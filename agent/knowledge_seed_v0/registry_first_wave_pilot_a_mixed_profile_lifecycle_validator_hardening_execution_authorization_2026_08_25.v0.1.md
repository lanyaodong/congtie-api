# Registry First Wave Pilot A Mixed-Profile Lifecycle Validator Hardening Execution Authorization 2026-08-25 v0.1

Status: Founder Authorized for Local Permanent Validator Hardening / Final Version-Control Approval Pending / Heart Rate S3 Not Authorized

Founder: 蓝耀栋

Authorization date: 2026-08-25

## 1. Purpose

This document authorizes a local, Validator-only hardening task for independently checking source lifecycle requirements on governed Measurement Profiles. It does not authorize any Registry record or product behavior change.

## 2. Repository Baseline

- Repository: `/Users/lanyaodong/Documents/congtie-api`
- Branch: `main`
- HEAD: `cdb8003984be5a9b9ae4a6a5aad5ff5ad24bb97b`
- origin/main: `cdb8003984be5a9b9ae4a6a5aad5ff5ad24bb97b`
- Initial staging: empty

## 3. Actual Execution Date

The authorized execution date is `2026-08-25`. New C40.1 artifacts must use this date and must not be backdated.

## 4. Original C40 Date Block

Original Step5-C40 required `2026-08-24`, while the actual execution date was `2026-08-25`. It stopped at the repository/date precondition with:

`STEP5-C40 BLOCKED — REPOSITORY OR DATE BASELINE MOVED`

This reauthorization does not treat that blocked attempt as an executed Validator revision.

## 5. Original C40 No-Change Confirmation

The blocked C40 attempt created no authorization document, no review packet, and no code change. It did not use `git add`, commit, or push. Both old-date C40 artifact paths were confirmed absent before this authorization was created.

## 6. Exact Validator-Before SHA

~~~text
Path: agent/knowledge_seed_v0/scripts/validate_biomarker_measurement_registry.py
SHA-256: 52ab54488fe8d018d008de3b45a46d16019445c20f36fa0641465c80ef867ff9
Lines: 1376
~~~

## 7. Exact Schema and Record SHAs

| Artifact | SHA-256 |
| --- | --- |
| Registry Schema | `a376b02e8cf50e95392287a8924919e57c6df6e37fa957830d4f1a60d1557aa7` |
| Height | `96434a7232da7f4fe3b91bb299e086ee5ba550378e9524a5bd81d6f202f465a1` |
| Body Weight | `3065394413200d62f2395c761d209f5b8a38ac1e3840bc472b30c103d2d2649b` |
| Creatinine | `396661e7b187beaab9717b042a991dc185a62857f3f1b01a3aa1b4d9d3b51e01` |
| Heart Rate | `1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e` |

The Candidate and Migration Ledgers, authoring dependency, and CI workflow also passed their exact SHA gates.

## 8. C33 Mixed-Profile Gate Lineage

The governing approval is:

~~~text
Path: agent/knowledge_seed_v0/registry_first_wave_pilot_a_source_verified_transition_plan_founder_approval_2026_08_24.v0.1.md
SHA-256: d3d90474ef17233bd8dbe0b7cc39409db061c1b0ee30a45a0e088fe9dac2f0c8
~~~

It requires independent validation of every governed Profile source lifecycle before any Profile-only transition under a parent concept that remains `proposed`.

## 9. Current Semantic-Validation Gap

The current Permanent Validator ties direct Profile source-status validation to parent RegistryConcept lifecycle. A governed Profile under a `proposed` parent can therefore semantically accept an empty direct source list or a resolving `pending` source, even though the mixed-Profile governance requires independent enforcement. Existing global source-key resolution already rejects dangling source keys and must remain intact.

## 10. Exact Authorized Implementation Scope

Only the Permanent Validator may be modified. The authorized code scope is:

1. a governed Profile-status constant for `source_verified`, `human_reviewed`, and `active`;
2. one independent Profile source-lifecycle helper;
3. unconditional wiring of that helper into semantic record validation;
4. removal or refactoring of the old duplicate direct-Profile source check; and
5. the exact mixed-Profile self-test fixture additions.

The implementation must reuse existing source-status policy and `_check_source_statuses()` logic, preserve global dangling-key resolution, and avoid duplicate diagnostics.

## 11. Exact Self-Test Requirements

The baseline is `5` valid and `12` invalid fixtures. The authorized additions are:

- one valid proposed-concept/source-verified-Profile fixture with a resolving `content_verified` source;
- invalid fixtures for empty sources, dangling source, pending source, human-reviewed Profile with pending source, and active Profile with pending source.

The target is exactly `6` valid and `17` invalid fixtures, all passing their expected semantic and Schema-backed outcomes.

## 12. Schema Non-Change

The Registry Schema must remain byte-identical at SHA `a376b02e8cf50e95392287a8924919e57c6df6e37fa957830d4f1a60d1557aa7`. C40.1 supplements semantic enforcement and does not revise Schema structure or enums.

## 13. CI Non-Change

`.github/workflows/ci.yml` must remain byte-identical at SHA `91adf2136a2bf48dd67d4de595e0920c9c32d2413c64fe3aa8e096eccd778b6d`. Existing authoring-validation commands already cover compilation, Schema validation, self-tests, and Ledger validation.

## 14. Record Non-Change

Height, Body Weight, Creatinine, and Heart Rate records must remain byte-identical. No lifecycle, Profile, source, mapping, unit, claim, threshold, relation, permission, or governance metadata may change.

## 15. Heart Rate S3 Non-Authorization

Heart Rate must remain exactly:

~~~text
RegistryConcept.lifecycle_status = proposed
heart_rate.spot_clinical.profile_status = proposed
heart_rate.wearable_ppg_time_series_estimate.profile_status = proposed
~~~

This authorization is only an S3 prerequisite. It does not execute S3 or approve a Heart Rate lifecycle transition.

## 16. Runtime and Product Non-Authorization

This task does not authorize runtime, retrieval, publication, database, API, loader, index, Observation processing, user-health storage, Service Panel, diagnosis, treatment, personal targets, automatic action, or other product logic.

## 17. Final Founder-Review Requirement

The hardened Validator, exact before/after SHA and diff, gap reproduction, self-test matrix, regression results, execution authorization, and review packet require a later exact-SHA Founder approval before any version-control action.

## 18. Git Boundary

This local task must not use `git add`, commit, push, clean, restore, stash, reset, rebase, amend, pull, or merge. Staging must remain empty and unrelated working-tree content must remain untouched.

## Exact Authorization Language

Founder authorizes local Permanent Validator hardening on `2026-08-25` against the exact SHA-identified Validator baseline. The original C40 stopped solely because its required date was `2026-08-24`; it created no artifact and changed no code. This authorization permits only independent source-lifecycle validation for governed Measurement Profiles and the exact associated self-tests. It does not authorize any Registry record change, lifecycle transition, Heart Rate S3, runtime, retrieval or product behavior.
