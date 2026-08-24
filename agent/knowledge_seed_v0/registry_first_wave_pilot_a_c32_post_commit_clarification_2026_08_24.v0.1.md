# Registry First Wave Pilot A - C32 Post-Commit Clarification 2026-08-24 v0.1

Status: Governance Clarification / No Record or Lifecycle Change

## 1. Purpose

This clarification preserves the exact-SHA approval chain while resolving a time-specific statement in the final C32 review packet.

The final review packet at SHA-256 `03766e3d20ddea6e29da46b5bcf73c78efa7124ea0984452bb7b1469e3c86580` states:

> The files exist in the repository working tree for review but are not committed, active, published, runtime-enabled, or retrieval-enabled.

That sentence accurately described the repository state when the packet was created. It is historical review-time context, not a current operational assertion.

Step5-C32.1 subsequently created and pushed two controlled commits:

- `b1b71532ded423763ec0f38062fb1346e26b8f92` - `feat: add Pilot A proposed Registry records`
- `674b62b08abc16f56d0508bf4b03940c37dbda75` - `docs: approve Pilot A proposed Registry records`

The review packet is not rewritten because Founder approval applies to its exact reviewed bytes and SHA.

## 2. Current Operational Clarification

After Step5-C32.1, the four Registry records are committed and versioned in Git. They remain `proposed`, inactive, unpublished, runtime-disabled and retrieval-disabled. Git versioning does not constitute Registry lifecycle promotion or product authorization.

Current bounded state:

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
```

## 3. Exact Record Manifest

| Registry ID | Candidate | Path | SHA-256 | Lifecycle |
| --- | --- | --- | --- | --- |
| `ME-000018` | `height` | `agent/biomarker_measurement_registry/records/ME-000018.height.json` | `6e03ad4435dafb5205212377f1cfb24568be47104769321ac34bd7aba74ee504` | `proposed` |
| `ME-000019` | `body_weight` | `agent/biomarker_measurement_registry/records/ME-000019.body_weight.json` | `1f533cd61110d63585589f2c54faccd4366a83862c59506a73570831d1505bcc` | `proposed` |
| `BM-000023` | `creatinine` | `agent/biomarker_measurement_registry/records/BM-000023.creatinine.json` | `fa6b2ad250c6c1f8f2e4df6428970eebd5e6497061533f110dabe99c0549cbab` | `proposed` |
| `ME-000020` | `heart_rate` | `agent/biomarker_measurement_registry/records/ME-000020.heart_rate.json` | `1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e` | `proposed` |

## 4. No Changes

```text
Record content change = 0
Record SHA change = 0
Lifecycle change = 0
Source change = 0
Runtime/retrieval change = 0
```

This clarification creates no Registry record, Profile, source, mapping, claim, threshold, system relation, observation, runtime behavior, retrieval behavior, API behavior or user-health storage.

