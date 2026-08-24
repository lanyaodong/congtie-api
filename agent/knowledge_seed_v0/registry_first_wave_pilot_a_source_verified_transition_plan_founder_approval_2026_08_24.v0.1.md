# Registry First Wave Pilot A - Source-Verified Transition Plan Founder Approval 2026-08-24 v0.1

Status: Founder Approved / Source Transition S1 Authorized / S2 and S3 Separately Gated

Founder: 蓝耀栋

Approval date: `2026-08-24`

## 1. Purpose

This closeout records Founder approval of the exact C33 post-commit clarification and source-verified transition plan. It authorizes only Source Transition S1 for the Height and Body Weight RegistryConcepts and their initial embedded Profiles. It does not authorize S2, S3, a human-reviewed or active lifecycle, or any product use.

## 2. Repository Baseline

| Field | Approved baseline |
| --- | --- |
| Repository | `/Users/lanyaodong/Documents/congtie-api` |
| Branch | `main` |
| HEAD | `674b62b08abc16f56d0508bf4b03940c37dbda75` |
| `origin/main` | `674b62b08abc16f56d0508bf4b03940c37dbda75` |
| Staging | empty |

## 3. Exact C33 Documents

| Document | Path | SHA-256 |
| --- | --- | --- |
| C32 post-commit clarification | `agent/knowledge_seed_v0/registry_first_wave_pilot_a_c32_post_commit_clarification_2026_08_24.v0.1.md` | `63cf0317dd0e4355794dbd387310663b156b026866889e8f12ce2d630ef2067c` |
| C33 source-verified transition plan | `agent/knowledge_seed_v0/registry_first_wave_pilot_a_source_verified_transition_plan_2026_08_24.v0.1.md` | `dd627b31e887553b85179da78f47a504ef7da5df8113b6154bbcee4ec5f70121` |

These exact reviewed documents retain their embedded review-time status. This closeout is the authoritative approval record and does not rewrite those bytes.

## 4. Exact Four-Record Manifest at Authorization

| Candidate | Registry ID | Path | Pre-transition SHA-256 | Authorized transition |
| --- | --- | --- | --- | --- |
| Height | `ME-000018` | `agent/biomarker_measurement_registry/records/ME-000018.height.json` | `6e03ad4435dafb5205212377f1cfb24568be47104769321ac34bd7aba74ee504` | S1 concept and `height.standing.stadiometer` Profile |
| Body Weight | `ME-000019` | `agent/biomarker_measurement_registry/records/ME-000019.body_weight.json` | `1f533cd61110d63585589f2c54faccd4366a83862c59506a73570831d1505bcc` | S1 concept and `body_weight.scale_measured` Profile |
| Creatinine | `BM-000023` | `agent/biomarker_measurement_registry/records/BM-000023.creatinine.json` | `fa6b2ad250c6c1f8f2e4df6428970eebd5e6497061533f110dabe99c0549cbab` | none; protected |
| Heart Rate | `ME-000020` | `agent/biomarker_measurement_registry/records/ME-000020.heart_rate.json` | `1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e` | none; protected |

## 5. Ten Founder Decisions

1. Height concept and its initial Profile are ready for S1 source verification.
2. Body Weight concept and its initial Profile are ready for S1 source verification.
3. Creatinine must not enter S2 before the NIDDK `88.4` conversion source is added and reviewed under a separate content-revision gate.
4. The Heart Rate wearable PPG Profile has source readiness.
5. The Heart Rate spot Profile remains `proposed`.
6. The Heart Rate RegistryConcept remains `proposed`.
7. Mixed-Profile lifecycle status is permitted in principle, but S3 requires independent Profile lifecycle Validator hardening first.
8. A source `access_date` is refreshed only when that source is actually reopened and checked.
9. A source-verification lifecycle and source-check metadata transition keeps `version: v0.1` when concept and Profile content are unchanged.
10. S1, S2 and S3 require separate authorization; this task authorizes S1 only.

## 6. Height Readiness Approval

The Height construct and LOINC mapping are supported by `src-loinc-height`. The standing-height method scope is supported by `src-who-steps` and `src-wst424`, and unit syntax is supported by `src-ucum`. The authorized transition is limited to the concept and `height.standing.stadiometer` Profile.

## 7. Body Weight Readiness Approval

The Body Weight construct and LOINC mapping are supported by `src-loinc-weight`. The measured-scale method scope is supported by `src-who-steps` and `src-wst424`, and unit syntax is supported by `src-ucum`. The authorized transition is limited to the concept and `body_weight.scale_measured` Profile.

## 8. Creatinine NIDDK Source-Addition Gate

S2 is not authorized. The exact `mg/dL x 88.4 = umol/L` conversion requires an added, content-reviewed NIDDK source. That source addition and any record diff require a separate Founder-approved content-revision task before a Creatinine source-verification transition.

## 9. Heart Rate Wearable Readiness

The wearable PPG source audit is approved as readiness planning. It does not execute a Profile status change and does not authorize device equivalence, ECG equivalence, rhythm diagnosis, output, runtime or retrieval.

## 10. Heart Rate Spot and Concept Hold

`heart_rate.spot_clinical` and the parent Heart Rate RegistryConcept remain `proposed`. The current broad spot method has no nonempty authoritative Profile source set. Neither LOINC nor wearable PPG evidence may be substituted as a spot-clinical method authority.

## 11. Mixed-Profile Validator Gate

Before S3, the Permanent Validator must independently validate every Profile whose `profile_status` is `source_verified`, `human_reviewed` or `active`, regardless of parent lifecycle. The future hardening must include:

- a valid `proposed` concept with one source-verified Profile and nonempty resolving content-verified source keys;
- rejection of a source-verified Profile with empty source keys;
- rejection of a source-verified Profile with a dangling source key;
- rejection of a source-verified Profile whose source remains `pending`;
- no runtime or Registry lifecycle promotion as a side effect.

The Validator is not modified by S1.

## 12. Source-Date Refresh Rule

Only source objects actually reopened on the transition date may receive that date in `access_date`. A shared source opened once may be refreshed in each record whose source object was within the verified S1 scope. Source titles, organizations, roles, identifiers, support scope and verification status remain byte-stable.

## 13. Version Decision

S1 keeps `version: v0.1`. The authorized change is a lifecycle/source-check metadata transition, not a new construct, method, Profile, unit, mapping or permission revision. Git remains the change history.

## 14. S1 Authorization

Founder authorizes the exact, bounded transition of:

```text
ME-000018 Height: RegistryConcept proposed -> source_verified
height.standing.stadiometer: proposed -> source_verified

ME-000019 Body Weight: RegistryConcept proposed -> source_verified
body_weight.scale_measured: proposed -> source_verified
```

The only additional permitted changes are the access dates of actually reopened S1 source objects, `last_modified_date`, `last_source_check_date`, and the exact transition status notes specified in Step5-C34.

## 15. S2 and S3 Non-Authorization

S2 and S3 are not authorized. Creatinine and Heart Rate record bytes must remain unchanged. No source, Profile, mapping, claim, threshold, reference context, system relation or device mapping may be added or removed in S1.

## 16. Runtime and Retrieval Non-Authorization

Source verification does not authorize human review, active status, publication, runtime, retrieval, database/API integration, loader/index creation, Observation processing, Service Panel behavior, user-health storage, diagnosis, treatment, target generation or action.

## 17. Next Founder Gate

After local S1 execution and validation, Founder reviews the exact Height and Body Weight record SHAs, the exact permitted diff, reopened-source evidence, and the S1 Review Packet. A later task may prepare an exact-SHA S1 Founder approval closeout and a controlled commit/push. No commit or push is authorized here.
