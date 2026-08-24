# Registry First Wave Pilot A - Source Transition S1 Founder Approval 2026-08-24 v0.1

Status: Founder Approved for Version Control / Height and Body Weight Source-Verified / Human Review, Active, Runtime and Retrieval Not Authorized

Founder: 蓝耀栋

Approval date: `2026-08-24`

## 1. Purpose

This closeout is the authoritative Founder approval for Source Transition S1. It approves the exact SHA-identified Height and Body Weight Registry records, their single embedded source-verified Profiles, the corrected S1 Review Packet, and the controlled three-commit version-control plan. It does not authorize S2, S3, a later lifecycle, or product use.

## 2. Repository Baseline

| Field | Approved state |
| --- | --- |
| Repository | `/Users/lanyaodong/Documents/congtie-api` |
| Branch | `main` |
| Initial HEAD | `674b62b08abc16f56d0508bf4b03940c37dbda75` |
| Initial `origin/main` | `674b62b08abc16f56d0508bf4b03940c37dbda75` |
| Initial staging | empty |
| Approval date | `2026-08-24` |

## 3. Exact C33 Lineage

| Artifact | Path | SHA-256 |
| --- | --- | --- |
| C32 post-commit clarification | `agent/knowledge_seed_v0/registry_first_wave_pilot_a_c32_post_commit_clarification_2026_08_24.v0.1.md` | `63cf0317dd0e4355794dbd387310663b156b026866889e8f12ce2d630ef2067c` |
| C33 source-verified transition plan | `agent/knowledge_seed_v0/registry_first_wave_pilot_a_source_verified_transition_plan_2026_08_24.v0.1.md` | `dd627b31e887553b85179da78f47a504ef7da5df8113b6154bbcee4ec5f70121` |
| C33 Founder approval closeout | `agent/knowledge_seed_v0/registry_first_wave_pilot_a_source_verified_transition_plan_founder_approval_2026_08_24.v0.1.md` | `d3d90474ef17233bd8dbe0b7cc39409db061c1b0ee30a45a0e088fe9dac2f0c8` |

The exact C33 documents remain byte-identical. Their embedded review-time statuses are preserved.

## 4. Exact C33 Approval SHA

The authoritative C33 planning approval is:

```text
Path:
agent/knowledge_seed_v0/registry_first_wave_pilot_a_source_verified_transition_plan_founder_approval_2026_08_24.v0.1.md

SHA-256:
d3d90474ef17233bd8dbe0b7cc39409db061c1b0ee30a45a0e088fe9dac2f0c8
```

It authorizes S1 only and separately gates S2 and S3.

## 5. Exact Final S1 Review Packet

```text
Path:
agent/knowledge_seed_v0/registry_first_wave_pilot_a_source_transition_s1_review_packet_2026_08_24.v0.1.md

SHA-256:
0ab06764555e9261f27dfd9c832d800385c1bb830530d72451b8e2377bdfc932
```

The packet records Founder decisions approved `3/3`, pending decisions `0`, and accidental approvals `0`.

## 6. Height SHA Before and After

```text
Path:
agent/biomarker_measurement_registry/records/ME-000018.height.json

Before:
6e03ad4435dafb5205212377f1cfb24568be47104769321ac34bd7aba74ee504

After and approved:
96434a7232da7f4fe3b91bb299e086ee5ba550378e9524a5bd81d6f202f465a1
```

## 7. Body Weight SHA Before and After

```text
Path:
agent/biomarker_measurement_registry/records/ME-000019.body_weight.json

Before:
1f533cd61110d63585589f2c54faccd4366a83862c59506a73570831d1505bcc

After and approved:
3065394413200d62f2395c761d209f5b8a38ac1e3840bc472b30c103d2d2649b
```

## 8. Exact Permitted Nine-Leaf Diff

Each approved record differs from current HEAD at exactly nine leaf values:

1. `lifecycle_status`;
2. its single eligible `Profile.profile_status`;
3. four existing `source_references[*].access_date` values;
4. `governance_metadata.last_modified_date`;
5. `governance_metadata.last_source_check_date`;
6. `governance_metadata.status_note`.

For both records:

```text
Changed leaves = 9
Authorized leaves = 9
Unauthorized leaves = 0
Added keys = 0
Removed keys = 0
Array reordering = 0
```

No source, Profile, unit, mapping, permission, claim, threshold, reference context, system relation or device mapping content changed.

## 9. Sources Reopened

The S1 audit reopened these exact source keys on `2026-08-24`:

- `src-loinc-height`;
- `src-loinc-weight`;
- `src-who-steps`;
- `src-wst424`;
- `src-ucum`.

LOINC supports terminology and mapping, WHO and WS/T support scoped measurement methods, and UCUM supports unit syntax. No source role was expanded beyond its recorded scope.

## 10. Five Unique Source-Object Count

```text
Unique source keys in S1 scope = 5
Record-level SourceReference object instances = 8
```

The WHO and WS/T source objects were checked through their official landing pages and relevant content or PDFs. A landing page and its linked content are not counted as separate Registry source objects.

## 11. Height Lifecycle Approval

Founder approves:

```text
ME-000018 Height RegistryConcept = source_verified
height.standing.stadiometer Profile = source_verified
```

This approval is limited to source verification of the canonical definition and the one initial standing-stadiometer Profile.

## 12. Body Weight Lifecycle Approval

Founder approves:

```text
ME-000019 Body Weight RegistryConcept = source_verified
body_weight.scale_measured Profile = source_verified
```

This approval is limited to source verification of the canonical definition and the one initial measured-scale Profile.

## 13. Schema and Validator Result

Validation used Python `3.9.6`, `jsonschema[format] 4.25.1`, the final Draft 2020-12 Registry Schema, the Permanent Validator, and the final Candidate Ledger.

```text
Height JSON: PASS
Height Schema and Permanent Validator: VALID / exit 0
Body Weight JSON: PASS
Body Weight Schema and Permanent Validator: VALID / exit 0
Warnings = 0
Errors = 0
Cross-Registry checks = 25/25 PASS
```

## 14. Version Decision

Both records remain `version: v0.1`. S1 is a source-verification lifecycle and source-check metadata transition. It does not revise concept identity, Profile content, units, mappings, permissions or interpretation boundaries. Git preserves the change history.

## 15. Human-Review Lifecycle Boundary

Founder approves the following exact language:

> Founder approves the exact SHA-identified Height and Body Weight Registry records for version control at `lifecycle_status: source_verified`, together with their single embedded source-verified Profiles. This approval confirms source verification only. It does not establish Registry lifecycle `human_reviewed` or `active`, and does not authorize publication, runtime, retrieval, database, API, Observation processing, user-health storage, diagnosis, treatment, personal targets or automatic action.

Current human-reviewed lifecycle records remain `0`.

## 16. S2 Non-Authorization

Creatinine remains `proposed` at SHA `fa6b2ad250c6c1f8f2e4df6428970eebd5e6497061533f110dabe99c0549cbab`. S2 is not authorized until the exact NIDDK `88.4` conversion source is added, content-reviewed, and approved through a separate record-content revision gate.

## 17. S3 Validator Gate

Heart Rate remains `proposed` at SHA `1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e`. Before S3, the Permanent Validator must independently enforce source lifecycle requirements for a source-verified Profile under a parent concept that remains proposed. S3 is not authorized by this closeout.

## 18. Runtime, Retrieval and Publication Non-Authorization

After version control:

```text
Human-reviewed lifecycle records = 0
Active records = 0
Runtime-enabled records = 0
Retrieval-enabled records = 0
Published records = 0
Use-evidence claims added = 0
Thresholds added = 0
System relations added = 0
User observations = 0
```

No database, API, loader, index, Observation processing, Service Panel, user-health storage, diagnosis, treatment, personal target or automatic action is authorized.

## 19. Git Commit Plan

Founder authorizes exactly three commits followed by one non-force push to `origin/main` if the remote movement gate passes:

1. `docs: approve Pilot A source transition plan` containing only the three C33 governance documents.
2. `feat: source-verify Height and Body Weight Registry records` containing only the two approved S1 record files.
3. `docs: approve Pilot A source transition S1` containing only the corrected S1 Review Packet and this exact-SHA approval closeout.

No amend, squash, rebase, force push, tag push or unrelated staging is authorized.

## 20. Next Founder Gate

After the controlled push, the only recommended next task is:

```text
Creatinine S2 - Add Exact NIDDK Conversion Source + Content Revision Review
```

Heart Rate S3 remains gated on Permanent Validator mixed-Profile lifecycle hardening. Neither S2 nor S3 may execute automatically.
