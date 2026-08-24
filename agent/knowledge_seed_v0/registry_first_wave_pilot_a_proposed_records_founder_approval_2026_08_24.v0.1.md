# Registry First Wave Pilot A Proposed Records Founder Approval 2026-08-24 v0.1

- Status: Founder Approved for Version Control / Lifecycle Remains Proposed / Runtime and Retrieval Not Authorized
- Founder: 蓝耀栋
- Approval date: 2026-08-24

## 1. Purpose

This closeout records Founder approval of the exact SHA-identified Pilot A Registry records for version control after final human review and one authorized Heart Rate editorial clarification. It does not authorize any Registry lifecycle promotion or product capability.

## 2. Repository Baseline

```text
Repository: /Users/lanyaodong/Documents/congtie-api
Branch: main
Approval-task initial HEAD: 1a7015d1c0c6cf6c04b3d00747dc4631247b150a
Approval-task initial origin/main: 1a7015d1c0c6cf6c04b3d00747dc4631247b150a
Initial staging: empty
```

## 3. Effective ID Reservations

The following committed reservations remain effective, permanent, non-semantic, and non-reusable:

| Candidate | Registry ID | Intended and Approved Record Path |
|---|---|---|
| Height | `ME-000018` | `agent/biomarker_measurement_registry/records/ME-000018.height.json` |
| Body Weight | `ME-000019` | `agent/biomarker_measurement_registry/records/ME-000019.body_weight.json` |
| Creatinine | `BM-000023` | `agent/biomarker_measurement_registry/records/BM-000023.creatinine.json` |
| Heart Rate | `ME-000020` | `agent/biomarker_measurement_registry/records/ME-000020.heart_rate.json` |

## 4. Exact Approved Record Manifest

| Record | SHA-256 |
|---|---|
| `agent/biomarker_measurement_registry/records/ME-000018.height.json` | `6e03ad4435dafb5205212377f1cfb24568be47104769321ac34bd7aba74ee504` |
| `agent/biomarker_measurement_registry/records/ME-000019.body_weight.json` | `1f533cd61110d63585589f2c54faccd4366a83862c59506a73570831d1505bcc` |
| `agent/biomarker_measurement_registry/records/BM-000023.creatinine.json` | `fa6b2ad250c6c1f8f2e4df6428970eebd5e6497061533f110dabe99c0549cbab` |
| `agent/biomarker_measurement_registry/records/ME-000020.heart_rate.json` | `1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e` |

## 5. Review Packet

```text
Path: agent/knowledge_seed_v0/registry_first_wave_pilot_a_proposed_records_review_packet_2026_08_23.v0.1.md
SHA-256: 03766e3d20ddea6e29da46b5bcf73c78efa7124ea0984452bb7b1469e3c86580
Founder decisions: 5/5 Approved
Founder pending decisions: 0
```

## 6. Authoring Manifest Lineage

The approved Pilot A schema-exact authoring manifest SHA is `951b98de45dbf3de2085041d1e729a2319808858632c97121bd08ab27ce1c757`. It was the initial materialization authority for all four records. Effective numeric IDs and controlled record dates were injected as governed dynamic fields. The corrected Heart Rate record additionally contains the single Founder-authorized editorial clarification recorded below.

## 7. Founder-Authorized Editorial Correction

```text
Record: ME-000020.heart_rate.json
JSON path: profiles[profile_key=heart_rate.wearable_ppg_time_series_estimate].profile_limitations
Original: Motion wear signal sampling and artifact handling matter.
Corrected: Motion, wear, signal sampling, and artifact handling matter.
Classification: Founder-authorized editorial clarification only
Medical-content change: No
Evidence/source change: No
Profile/permission/lifecycle change: No
```

## 8. Schema and Validator Results

```text
JSON syntax: 4/4 PASS
Draft 2020-12 Schema: 4/4 PASS
Permanent Semantic Validator: 4/4 PASS
Cross-record checks: 25/25 PASS
Warnings: 0
Errors: 0
```

## 9. Record Lifecycle State

All four records retain `lifecycle_status: proposed`. Founder approval for version control is not a Registry lifecycle transition and does not establish `source_verified`, `human_reviewed`, or `active` status.

## 10. Profile Lifecycle State

All five embedded Measurement Profiles retain `profile_status: proposed`. No Profile was added, removed, promoted, or otherwise changed by this approval task.

## 11. Source, Mapping, and Unit Boundaries

The approved source pools, source roles, LOINC mappings, UCUM units, conversion rules, method-comparability boundaries, and profile limitations remain as validated in the exact record SHAs. No claim, reference context, threshold, system relation, lifecycle relation, or device mapping was added.

## 12. Agent Permission Boundaries

Height and Body Weight retain `action_authorization: none`. Creatinine and Heart Rate retain `action_authorization: separately_gated`. No record authorizes diagnosis, treatment, personal risk scoring, personal target generation, unverified conversion, automatic action, or method-independent normalization.

## 13. Founder Approval Decision

> Founder approves the exact SHA-identified Height, Body Weight, Creatinine and corrected Heart Rate Registry records for version control with `lifecycle_status: proposed`. This approval does not change the records to `human_reviewed`, `source_verified` or `active`, and does not authorize runtime, retrieval, publication, database, API, Observation processing, user-health storage, diagnosis, treatment, personal targets or automatic action.

## 14. Exact State

```text
Effective numeric-ID reservations = 4
Registry records = 4
Proposed records = 4
Source-verified records = 0
Human-reviewed lifecycle records = 0
Active records = 0
Runtime-enabled records = 0
Retrieval-enabled records = 0
Published records = 0
User observations = 0
```

## 15. Explicit Non-Authorizations

This approval does not authorize lifecycle promotion; runtime or retrieval; publication; database, API, loader, or index work; Observation processing; user-health storage; Service Panel creation; public thresholds or critical values; personal targets; diagnosis; treatment; or automatic action.

## 16. Git Commit Plan

1. Commit the four exact proposed Registry records with message `feat: add Pilot A proposed Registry records`.
2. Commit the updated Review Packet and this approval closeout with message `docs: approve Pilot A proposed Registry records`.
3. Push once to `origin/main` only after confirming the remote baseline remains unchanged.

## 17. Next Lifecycle Gate

The next recommended task is a Pilot A Source-Verified Transition Plan. Before any lifecycle change, it must separately review definition sources, Profile method sources, mapping sources, source completeness and freshness, Heart Rate spot-clinical method authority, wearable time-series Observation granularity, and future Profile or claim additions. No transition is automatic.
