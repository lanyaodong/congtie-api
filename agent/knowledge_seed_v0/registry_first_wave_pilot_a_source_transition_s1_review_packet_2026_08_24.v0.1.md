# Registry First Wave Pilot A - Source Transition S1 Review Packet 2026-08-24 v0.1

Status: Founder Approved for Version Control / Height and Body Weight Source-Verified / Runtime and Retrieval Not Authorized

Founder reviewer: 蓝耀栋

Founder review date: `2026-08-24`

## 1. Purpose

This packet presents the locally executed, uncommitted Source Transition S1 for Founder review. It covers only Height and Body Weight. It records source re-verification, exact authorized diffs, validation evidence and protected boundaries without authorizing commit, push, runtime or a later lifecycle.

## 2. Repository Baseline

| Field | State |
| --- | --- |
| Repository | `/Users/lanyaodong/Documents/congtie-api` |
| Branch | `main` |
| HEAD | `674b62b08abc16f56d0508bf4b03940c37dbda75` |
| `origin/main` | `674b62b08abc16f56d0508bf4b03940c37dbda75` |
| Staging | empty |
| Execution date | `2026-08-24` |

## 3. C33 Plan and Approval Lineage

| Artifact | SHA-256 | Role |
| --- | --- | --- |
| `registry_first_wave_pilot_a_c32_post_commit_clarification_2026_08_24.v0.1.md` | `63cf0317dd0e4355794dbd387310663b156b026866889e8f12ce2d630ef2067c` | approved historical-state clarification; byte-identical |
| `registry_first_wave_pilot_a_source_verified_transition_plan_2026_08_24.v0.1.md` | `dd627b31e887553b85179da78f47a504ef7da5df8113b6154bbcee4ec5f70121` | exact approved source-transition plan; byte-identical |
| `registry_first_wave_pilot_a_source_verified_transition_plan_founder_approval_2026_08_24.v0.1.md` | `d3d90474ef17233bd8dbe0b7cc39409db061c1b0ee30a45a0e088fe9dac2f0c8` | authoritative S1 authorization; S2/S3 gated |

## 4. Height SHA Before and After

| Field | Value |
| --- | --- |
| Path | `agent/biomarker_measurement_registry/records/ME-000018.height.json` |
| SHA before | `6e03ad4435dafb5205212377f1cfb24568be47104769321ac34bd7aba74ee504` |
| SHA after | `96434a7232da7f4fe3b91bb299e086ee5ba550378e9524a5bd81d6f202f465a1` |
| Temporary/repository parity | PASS |

## 5. Body Weight SHA Before and After

| Field | Value |
| --- | --- |
| Path | `agent/biomarker_measurement_registry/records/ME-000019.body_weight.json` |
| SHA before | `1f533cd61110d63585589f2c54faccd4366a83862c59506a73570831d1505bcc` |
| SHA after | `3065394413200d62f2395c761d209f5b8a38ac1e3840bc472b30c103d2d2649b` |
| Temporary/repository parity | PASS |

## 6. Exact Permitted Diff

Each record has exactly nine changed leaf values and no key, array-order or structural change:

1. `lifecycle_status`;
2. the one eligible `profiles[0].profile_status`;
3. four existing `source_references[*].access_date` values;
4. `governance_metadata.last_modified_date`;
5. `governance_metadata.last_source_check_date`;
6. `governance_metadata.status_note`.

Unauthorized changed leaf values: `0`.

## 7. Sources Reopened

Five unique source objects were actually reopened on `2026-08-24`. The WHO and WS/T source objects were each checked through their official landing page and relevant content or PDF, and the shared WHO, WS/T and UCUM source objects were applied to both record scopes.

| Source | Record scope | Access result | Support still valid | Superseded or withdrawn? |
| --- | --- | --- | --- | --- |
| `src-loinc-height` | Height | official LOINC `8302-2` page opened; term Active | Height construct identity and concept mapping | No |
| `src-loinc-weight` | Body Weight | official LOINC `29463-7` page opened; term Active | Body Weight construct identity and concept mapping | No |
| `src-who-steps` | both | official WHO manuals page and Part 3 Section 5 PDF opened | standing-height and measured-weight protocols | No notice found |
| `src-wst424` | both | official NHC landing page and WS/T 424-2013 text checked | China standing-height and measured-weight methods | No withdrawal or replacement found |
| `src-ucum` | both | official UCUM specification opened | `cm`, `m`, `[in_i]`, `kg`, `[lb_av]` syntax and physical conversions | No notice found |

LOINC remains terminology/mapping authority, WHO and WS/T remain measurement-method sources, and UCUM remains unit-syntax authority only. None is expanded beyond its recorded support scope.

## 8. Source Access Results

- LOINC `8302-2` and `29463-7` remain Active and have no Method component; they do not replace Profile method sources.
- WHO STEPS still specifies firm-surface/device setup, footwear context, body positioning and device recording for the scoped physical measurements.
- WS/T 424-2013 remains available from the official NHC source and supports its China population-monitoring measurement scope.
- UCUM still supports exact unit syntax and physical conversion, not protocol or device comparability.
- Existing source titles, organizations, roles, URLs, identifiers, support arrays, limitation arrays, verification statuses and notes were not changed.

## 9. Lifecycle Changes

```text
Height RegistryConcept: proposed -> source_verified
Body Weight RegistryConcept: proposed -> source_verified
```

No other RegistryConcept lifecycle changed.

## 10. Profile Changes

```text
height.standing.stadiometer: proposed -> source_verified
body_weight.scale_measured: proposed -> source_verified
```

No Profile was added, removed or rewritten.

## 11. Date Changes

For both records:

```text
four reopened source access_date values: 2026-08-22 -> 2026-08-24
governance_metadata.last_modified_date: 2026-08-23 -> 2026-08-24
governance_metadata.last_source_check_date: 2026-08-22 -> 2026-08-24
```

`created_date`, `reviewed_by`, `reviewed_date` and `version` remain unchanged.

## 12. Status-Note Changes

Height exact note:

> Source verification completed for the canonical Height definition and height.standing.stadiometer Profile. RegistryConcept and Profile are source_verified only; no human review, active status, publication, runtime, retrieval, clinical claim, threshold or action authorization.

Body Weight exact note:

> Source verification completed for the canonical Body Weight definition and body_weight.scale_measured Profile. RegistryConcept and Profile are source_verified only; no human review, active status, publication, runtime, retrieval, clinical claim, threshold or action authorization.

## 13. Schema Result

The two temporary records and the two byte-identical repository copies parse as JSON and pass the Draft 2020-12 Registry Schema using Python `3.9.6` and `jsonschema 4.25.1`.

```text
Height: PASS
Body Weight: PASS
Total: 2/2
```

## 14. Permanent Validator Result

Both records pass the permanent authoring Validator with the final Candidate Ledger supplied for lineage resolution.

```text
Height: VALID
Body Weight: VALID
Warnings: 0
Errors: 0
```

## 15. Cross-Record Checks

| Check | Result |
| --- | --- |
| Concept/Profile lifecycle values match S1 | PASS |
| Definition and Profile source keys resolve | PASS |
| Relevant sources remain `content_verified` | PASS |
| Source set, roles and support scope unchanged | PASS |
| Claims, thresholds, relations and mappings unchanged | PASS |
| Unit, method, protocol, limitations and Agent permissions unchanged | PASS |
| `version: v0.1`, `reviewed_by: []`, `reviewed_date: null` retained | PASS |
| Creatinine and Heart Rate protected SHAs unchanged | PASS |
| Candidate Ledger SHA and null Registry IDs unchanged | PASS |
| Runtime and retrieval state unchanged | PASS |

Programmatic detailed checks: `20/20 PASS`.

## 16. Protected Record Integrity

| Protected record | Required SHA-256 | Result |
| --- | --- | --- |
| Creatinine `BM-000023` | `fa6b2ad250c6c1f8f2e4df6428970eebd5e6497061533f110dabe99c0549cbab` | unchanged |
| Heart Rate `ME-000020` | `1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e` | unchanged |

The Registry Schema, Candidate Ledger, Migration Ledger, permanent Validator, allocation assets and prior governance artifacts remain unchanged.

## 17. Registry State

```text
Effective numeric-ID reservations = 4
Registry records = 4

Height concept = source_verified
height.standing.stadiometer = source_verified
Body Weight concept = source_verified
body_weight.scale_measured = source_verified
Creatinine concept and Profile = proposed
Heart Rate concept and both Profiles = proposed

Human-reviewed lifecycle records = 0
Active records = 0
Runtime-enabled records = 0
Retrieval-enabled records = 0
Published records = 0
```

These are local, uncommitted record modifications until a separately authorized controlled commit/push.

## 18. Explicit Non-Authorizations

This packet does not authorize S2, S3, Creatinine or Heart Rate changes, source additions, Profile additions, mappings, claims, thresholds, reference contexts, system relations, device mappings, human review, active status, publication, runtime, retrieval, database/API/loader/index behavior, Observation processing, Service Panel behavior, user-health storage, diagnosis, treatment, targets or action.

## 19. Founder Decision Sheet

| Decision | Founder Decision |
| --- | --- |
| Approve final Height `source_verified` record at SHA `96434a7232da7f4fe3b91bb299e086ee5ba550378e9524a5bd81d6f202f465a1` | Approved |
| Approve final Body Weight `source_verified` record at SHA `3065394413200d62f2395c761d209f5b8a38ac1e3840bc472b30c103d2d2649b` | Approved |
| Authorize controlled commit/push of the C33 documents, two S1 records, this packet and the exact-SHA S1 Founder approval closeout | Approved |

```text
Founder decisions approved = 3/3
Founder pending decisions = 0
Accidental approvals = 0
```

## 20. Recommended Next Gate

S1 controlled commit and push are authorized. Creatinine S2 remains gated on adding and reviewing the exact NIDDK conversion source. Heart Rate S3 remains gated on independent mixed-Profile lifecycle Validator hardening. Do not execute S2 or S3 automatically. `source_verified` does not mean `human_reviewed`, `active`, runtime-enabled or retrieval-enabled.
