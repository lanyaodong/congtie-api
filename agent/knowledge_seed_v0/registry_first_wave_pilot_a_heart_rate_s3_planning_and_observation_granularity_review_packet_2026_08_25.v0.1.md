# Registry First Wave Pilot A Heart Rate S3 Planning and Observation-Granularity Review Packet 2026-08-25 v0.1

Status: Draft / Founder Review Pending / Heart Rate S3 Not Authorized / Heart Rate Record Unchanged

Prepared date: 2026-08-25

## 1. Purpose

This read-only packet rechecks the four current Heart Rate sources, reviews 2020-2026 wearable PPG evidence, fixes the intended wearable Profile boundary, defines future Observation-granularity and Profile-aware output acceptance rules, and records an exact six-leaf Profile-only S3 plan. It does not modify the Heart Rate record, execute S3, create user data, or authorize runtime or retrieval.

## 2. Repository Baseline

- Repository: `/Users/lanyaodong/Documents/congtie-api`
- Branch: `main`
- HEAD: `bdbcbeb766101755beaf152c09bb4ef72f6b1937`
- origin/main: `bdbcbeb766101755beaf152c09bb4ef72f6b1937`
- Execution date: `2026-08-25`
- Initial staging: empty
- Baseline result: PASS

The unrelated dirty and untracked working tree was inventoried before the task and left untouched.

## 3. C33 and C41 Lineage

| Artifact | SHA-256 | Role |
| --- | --- | --- |
| C33 Transition Plan | `dd627b31e887553b85179da78f47a504ef7da5df8113b6154bbcee4ec5f70121` | Approved transition plan |
| C33 Founder Approval | `d3d90474ef17233bd8dbe0b7cc39409db061c1b0ee30a45a0e088fe9dac2f0c8` | Mixed-Profile prerequisite |
| C40.1 Execution Authorization | `906f73627dbc693bdb4f7ce65cd7eb36c9ca2ec1aaa45c2ca6b8839e9b25f07a` | Validator scope authorization |
| C40.1 Review Packet | `78827062fe98e85a8230c30f07f97e34fbf02a85e5706b1fbf3063d452d5a052` | Hardening evidence |
| C41 Founder Approval | `d9c03ad141f4cbc646eece2847fede1bfe6ecef62f0e3a8cad76ff1ab8b8ca98` | Committed hardening approval |

C41 closed the independent Profile source-lifecycle Validator prerequisite. It did not authorize Heart Rate S3.

## 4. Current Heart Rate SHA

~~~text
Path: agent/biomarker_measurement_registry/records/ME-000020.heart_rate.json
SHA-256: 1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e
Lines: 322
Read-only parity after C42: PASS
~~~

## 5. Current Record and Profile State

~~~text
registry_id = ME-000020
candidate_key = heart_rate
namespace = ME
version = v0.1
RegistryConcept.lifecycle_status = proposed

heart_rate.spot_clinical.profile_status = proposed
heart_rate.spot_clinical.source_reference_keys = []

heart_rate.wearable_ppg_time_series_estimate.profile_status = proposed
heart_rate.wearable_ppg_time_series_estimate.source_reference_keys =
  [src-hr-ppg-2020, src-interlive-hr]

SourceReference objects = 4
Duplicate source keys = 0
~~~

No current record field was changed.

## 6. Hardened Validator Prerequisite

Permanent Validator SHA `baf2de87085b697ed2c4a990546f2e29b4c938aec36005ce6d3a3348933bddb2` independently validates direct sources for every Profile at `source_verified`, `human_reviewed`, or `active`, even when the parent RegistryConcept remains `proposed`.

~~~text
Valid fixtures = 6/6 PASS
Invalid fixtures rejected = 17/17 PASS
Semantic self-test = PASS
Schema-backed self-test = PASS
~~~

The prerequisite is satisfied for authoring validation only. It creates no lifecycle or runtime authorization.

## 7. Four-Source Inventory

| Source key | Identity | Role | Status | Current access date | Scope |
| --- | --- | --- | --- | --- | --- |
| `src-loinc-hr` | LOINC `8867-4` | `other_reviewed_role` | `content_verified` | 2026-08-22 | concept identity/mapping |
| `src-hr-ppg-2020` | DOI `10.1080/02640414.2020.1767348`; PMID `32552580` | `validation_evidence` | `content_verified` | 2026-08-22 | wearable PPG Profile |
| `src-interlive-hr` | PMID `33397674`; verified DOI `10.1136/bjsports-2020-103148` | `validation_evidence` | `content_verified` | 2026-08-22 | wearable validation framework |
| `src-ucum` | UCUM Specification | `other_reviewed_role` | `content_verified` | 2026-08-22 | unit syntax only |

All keys resolve. No source was added, removed, reordered, or edited. The null DOI in the current INTERLIVE object is a metadata-completeness observation, not a resolution blocker, because the existing PMID resolves to the exact reviewed document.

## 8. LOINC Audit

- Source: `src-loinc-hr`
- URL: `https://loinc.org/8867-4`
- Access: official page opened on 2026-08-25.
- Status: active; displayed release `2.82`.
- Identity: `Heart rate:NRat:Pt:XXX:Qn:`.
- Method: not specified.
- Unit context: `/MIN`; `bpm` may appear as display text.
- Deprecation/replacement affecting the mapping: none found.

It supports construct identity and concept-level mapping. It does not support spot method, wearable validation, PPG-ECG equivalence, rhythm diagnosis, or device/algorithm equivalence.

Result: identity and scope stable.

## 9. PPG Systematic-Review Audit

~~~text
Source key: src-hr-ppg-2020
Title: Validity of Wrist-Worn photoplethysmography devices to measure heart rate: A systematic review and meta-analysis
Journal: Journal of Sports Sciences
DOI: 10.1080/02640414.2020.1767348
PMID: 32552580
Access: PubMed record and abstract opened on 2026-08-25
~~~

The review synthesized 44 articles, 738 effects, and 15 brands. Reported performance varies by testing context, supporting the record's activity, device/test, wear, sampling, and artifact limitations.

It supports wrist-worn PPG Heart Rate validity limits, activity dependence, device/test heterogeneity, and provenance retention. It does not support ECG equivalence, every device or version, universal normalization, rhythm diagnosis, or automatic interpretation.

Correction, retraction, expression of concern, or formal supersession: none found.

## 10. INTERLIVE Audit

~~~text
Source key: src-interlive-hr
Title: Recommendations for determining the validity of consumer wearable heart rate devices: expert statement and checklist of the INTERLIVE Network
Organization/journal: INTERLIVE Network / British Journal of Sports Medicine
DOI: 10.1136/bjsports-2020-103148
PMID: 33397674
PMCID: PMC8273688
Access: PubMed record and lawful open-access PMC full text opened on 2026-08-25
~~~

The source addresses target population, criterion measure, index measure/device placement, testing conditions, data processing, and statistical analysis. It supports explicit treatment of population, wear location, motion artifact, time alignment, resampling, missingness, and firmware/software changes.

It does not support device/firmware/algorithm equivalence, diagnosis, cross-platform normalization, transfer to the spot Profile, or automatic validation of summaries.

Correction, retraction, expression of concern, or formal supersession: none found. The current record's null DOI was observed but not edited.

## 11. UCUM Audit

- Source: `src-ucum`
- URL: `https://ucum.org/ucum`
- Access: official specification opened on 2026-08-25.
- `/min` remains valid UCUM rate syntax.
- `bpm` remains a UI display label, not a second canonical unit code.
- Replacement or withdrawal affecting `/min`: none found.

UCUM supports unit syntax only. It does not support PPG validation, method equivalence, clinical interpretation, or personal targets.

## 12. Corrections, Retractions, and Supersession Audit

| Source | Correction | Retraction/concern | Supersession | Result |
| --- | --- | --- | --- | --- |
| LOINC `8867-4` | not applicable | no deprecation found | no affecting replacement | stable |
| PMID `32552580` | none found | none found | no formal supersession | stable |
| PMID `33397674` | none found | none found | no formal supersession | stable |
| UCUM | none affecting `/min` | none found | none found | stable |

The newer 2025 INTERLIVE free-living activity-profile paper, PMID `39893599`, has a linked correction, PMID `41131415`, DOI `10.1007/s40279-025-02329-9`. That correction does not apply to current source PMID `33397674`.

## 13. Updated 2020-2026 Evidence Search

Search date: `2026-08-25`.

Queries:

1. `wrist-worn photoplethysmography heart rate systematic review meta-analysis`
2. `consumer wearable heart rate validation systematic review`
3. `wearable PPG heart rate consensus validation`
4. `INTERLIVE heart rate update`
5. `2020-2026 wearable PPG heart rate accuracy review`

| PMID | DOI | Evidence | Relevance | Correction |
| --- | --- | --- | --- | --- |
| `35060915` | `10.2196/30791` | wrist-wearable accuracy/acceptability systematic review | broad supporting context | none found |
| `36376641` | `10.1007/s40615-022-01446-9` | skin-tone accuracy systematic review | reinforces population/skin-tone caveats | none found |
| `37204639` | `10.1007/s11357-023-00815-4` | cardiovascular remote-monitoring systematic review | broad context, not a replacement | none found |
| `39893599` | `10.1007/s40279-024-02159-1` | INTERLIVE free-living HR activity-profile review | supports separate summary semantics | PMID `41131415` |
| `41131415` | `10.1007/s40279-025-02329-9` | correction to PMID `39893599` | correction-chain governance | correction record |
| `40909206` | `10.1038/s44325-025-00082-6` | guide to consumer wearables in cardiovascular care | broader context, not a replacement | none found |

No current-source retraction, identity failure, or materially adverse evidence was found. Newer evidence emphasizes population/skin-tone scope, activity/motion effects, firmware/algorithm drift, device heterogeneity, processing, and summary separation.

No new source is required before the narrow S3 transition. Any future source addition requires a separate content-revision Gate.

## 14. Materially New Evidence Classification

Classification: `Class B - Useful but nonblocking`.

The two existing PPG sources still support the narrow wearable estimate Profile. Newer evidence reinforces limitations and provenance requirements but does not widen or invalidate it. The 2025 free-living evidence supports future separate summary Profiles.

Source-content revision prerequisite before S3: none.

## 15. Current PPG Profile Scope

Proposed Founder decision:

> Device-produced, time-stamped Heart Rate estimates derived from wearable photoplethysmography, with explicit device, time-window and provenance context.

Allowed scope is estimated points from a wearable PPG series or an ordered estimated Heart Rate time series. It does not establish device equivalence or clinical utility.

Excluded: raw PPG waveform, ECG, rhythm classification, atrial/ventricular rate, clinical spot Heart Rate, manual pulse, resting/sleeping/daily/activity summaries, zones, recovery, and proprietary readiness or recovery scores.

Founder Decision: Pending.

## 16. Raw PPG Waveform Exclusion

~~~text
wearable PPG Heart Rate estimate != raw PPG waveform
~~~

The current Profile describes derived or estimated Heart Rate values, not optical sensor waveforms. A future raw-waveform concept requires separate sensor, wavelength, sampling, filtering, signal-quality, artifact, privacy, and legal governance.

No raw-signal concept, Profile, schema, or record is created.

Founder Decision: Pending.

## 17. Spot Profile Hold

`heart_rate.spot_clinical` remains `proposed` with an empty source list. Wearable sources do not transfer to it, and LOINC/UCUM do not supply the missing spot-method authority. Manual pulse count remains excluded.

A later spot transition requires an independently reviewed method source and, if needed, a narrower modality boundary. S3 plans no spot changes.

## 18. Observation Representation Contract

Allowed future representations:

~~~text
wearable_hr_estimate_point_from_series
wearable_hr_estimate_time_series
~~~

Point-from-series means one timestamped wearable-derived Heart Rate estimate whose provenance identifies the wearable PPG series. It is not a spot clinical measurement.

Time-series means an ordered set of timestamped estimates preserving covered interval, source output behavior, and missingness.

Reject or route to future Profiles:

~~~text
daily_average_heart_rate
resting_heart_rate_summary
sleeping_heart_rate_summary
activity_heart_rate_summary
exercise_heart_rate_summary
heart_rate_zone
heart_rate_recovery
raw_ppg_waveform
ecg_derived_heart_rate
clinical_spot_heart_rate
manual_pulse_rate
rhythm_or_arrhythmia_label
~~~

A `context_tag` cannot convert those distinct semantics into this Profile.

Founder Decision: Pending.

## 19. Required Provenance

Future interpretation requires:

~~~text
Registry ID or candidate key
Profile key
observation representation
measurement nature = estimated
original metric name
original value/unit or ordered point series
timestamp or interval start/end
time zone or explicit unknown
device manufacturer or source organization
device model/family or explicit unknown
source app/file/API/export identifier
~~~

These are planning requirements only, not fields added by C42.

## 20. Conditional Provenance

Record when available or material:

~~~text
firmware version
software/app version
algorithm version
sampling cadence
device output cadence
aggregation window
wear location/body site
activity/context
artifact handling
missingness
signal-quality indicator
data completeness
wear-time completeness
~~~

Missing material provenance may prevent comparison or interpretation. It never authorizes an inferred value or cross-device normalization.

## 21. Missing-Data Semantics

Future handling must distinguish:

~~~text
known
unknown
not supplied
not available from device
not applicable
~~~

The system must not infer firmware, algorithm, sampling cadence, activity context, or artifact handling from absence. `Unknown` is not `not applicable` and is not a verified default.

## 22. Summary-Output Separation

The current Profile does not authorize resting, sleeping, daily, activity/exercise, zone, or recovery summaries. Each requires a future Profile with an explicit window, inclusion/exclusion rules, state semantics, aggregation algorithm, missingness handling, provenance, and validation scope.

A derived summary must not masquerade as a point or raw time series. The 2025 INTERLIVE free-living evidence reinforces this separation.

Founder Decision: Pending.

## 23. User-Data Boundary

~~~text
RegistryConcept/Profile = public definition
User Observation = private user event or value
~~~

The Registry record stores no user identifier, observed Heart Rate, time series, device account, consent, symptom, diagnosis, target, or action. C42 creates no Observation.

Future Observation handling still requires authorization, purpose limitation, provenance, privacy-safe rendering, and deletion/withdrawal handling.

## 24. Profile-Aware Retrieval and Output Contract

If separately authorized after S3, output may state only:

~~~text
heart_rate.wearable_ppg_time_series_estimate = source_verified
~~~

It must not state:

~~~text
Heart Rate record = source_verified
heart_rate.spot_clinical = source_verified
~~~

A generic Heart Rate answer must disclose that only the wearable PPG time-series estimate Profile is source-verified while the parent concept and spot Profile remain `proposed`.

Wearable evidence must not transfer to spot output or generate rhythm diagnosis, ECG equivalence, personal targets, risk scores, or actions. Runtime/retrieval remains disabled.

Founder Decision: Pending.

## 25. Record-Level Source-Date Semantics

For S3, `governance_metadata.last_source_check_date` means:

> The latest governed source check relevant to the modified wearable PPG Profile.

It does not claim that all four record sources were reopened on that date. SourceReference-level `access_date` indicates which source was actually opened.

The future S3 diff may refresh only `src-hr-ppg-2020.access_date` and `src-interlive-hr.access_date`. C42 found no conflict with this scoped meaning in the C33 governance, Schema, or Validator.

Founder Decision: Pending.

## 26. Exact Future S3 Diff

For transition date `2026-08-25`, the only planned changes are:

~~~text
1. wearable Profile profile_status: proposed -> source_verified
2. src-hr-ppg-2020.access_date: 2026-08-22 -> 2026-08-25
3. src-interlive-hr.access_date: 2026-08-22 -> 2026-08-25
4. governance_metadata.last_modified_date: 2026-08-23 -> 2026-08-25
5. governance_metadata.last_source_check_date: 2026-08-22 -> 2026-08-25
6. governance_metadata.status_note -> exact text below
~~~

Exact status note:

~~~text
Source verification completed for heart_rate.wearable_ppg_time_series_estimate only. The Heart Rate RegistryConcept and heart_rate.spot_clinical Profile remain proposed. No human review, active status, publication, runtime, retrieval, rhythm diagnosis, clinical claim, threshold or action authorization.
~~~

Expected diff:

~~~text
Changed existing scalar leaves = 6
Authorized leaves = 6
Unauthorized leaves = 0
Added keys = 0
Removed keys = 0
SourceReference/Profile additions or removals = 0
Array reordering = 0
~~~

Parent lifecycle, spot status, source content, definition keys, methods, units, mappings, limitations, permissions, claims, thresholds, relations, `reviewed_by`, and `reviewed_date` remain unchanged.

Founder Decision: Pending.

## 27. Version Decision

Recommendation: `version = v0.1`, unchanged.

The planned change is Profile lifecycle and source-check metadata only. Construct, Profile identity, method, unit, source content, mapping, limitations, and permissions remain stable. Git preserves history.

## 28. Dry-Run Result

~~~text
Path: /tmp/congtie-heart-rate-c42-s3-dry-run/ME-000020.heart_rate.json
SHA-256: b1a110d51112414ec12c40fe5418280013884fa8940acb3c6000d71bda26519f
Serialization: UTF-8, LF, two spaces, ensure_ascii=false,
               preserved order, one final newline
JSON syntax = PASS
Programmatic checks = 18/18 PASS
Repository copy-back = not performed
~~~

The dry-run has parent `proposed`, spot `proposed`, wearable `source_verified`, exact two content-verified wearable sources, unchanged LOINC/UCUM dates, `version = v0.1`, no user data, and the exact six-leaf diff.

It is not an approved Registry record and does not execute S3.

## 29. Schema Result

~~~text
Draft 2020-12 instance validation = PASS
Schema errors = 0
~~~

The mixed parent/Profile lifecycle combination is structurally valid under Schema v0.1.

## 30. Hardened Validator Result

~~~text
Result = VALID: Registry concept record
Exit code = 0
Warnings = 0
Errors = 0
Mixed-Profile source Gate = PASS
Candidate Ledger lineage = PASS
~~~

The hardened Validator independently resolved both wearable Profile source keys. It did not mutate any record.

## 31. Protected Integrity

| Artifact | Required SHA-256 | Result |
| --- | --- | --- |
| Height | `96434a7232da7f4fe3b91bb299e086ee5ba550378e9524a5bd81d6f202f465a1` | unchanged |
| Body Weight | `3065394413200d62f2395c761d209f5b8a38ac1e3840bc472b30c103d2d2649b` | unchanged |
| Creatinine | `396661e7b187beaab9717b042a991dc185a62857f3f1b01a3aa1b4d9d3b51e01` | unchanged |
| Heart Rate | `1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e` | unchanged |
| Permanent Validator | `baf2de87085b697ed2c4a990546f2e29b4c938aec36005ce6d3a3348933bddb2` | unchanged |
| Registry Schema | `a376b02e8cf50e95392287a8924919e57c6df6e37fa957830d4f1a60d1557aa7` | unchanged |
| Candidate Ledger | `b97f4b0e0aeaa4fae6e728c561e88019d3c9e0b34ce353c1cc2b27f5cd09bbe5` | unchanged |
| Migration Ledger | `592408206315e2a404740c0fe5ca1f1ad574d407401d9df9c7f2062a45ad1a56` | unchanged |
| requirements-dev | `b362c00c5eab2a8795c02ea136e5773af55e9c845176547f778fa833ed755448` | unchanged |
| CI | `91adf2136a2bf48dd67d4de595e0920c9c32d2413c64fe3aa8e096eccd778b6d` | unchanged |

C33-C41 governance artifacts, allocations, Registry READMEs, Evidence Contract, Registry MVP Spec, knowledge entries, UHIL, Observation assets, and runtime/application assets were not modified.

## 32. Explicit Non-Authorizations

C42 does not authorize Heart Rate changes; S3; any lifecycle change; parent or spot verification; source/Profile/mapping/unit/claim/threshold/relation edits; Observation schema or data; user-health storage; runtime/retrieval; publication; database/API/loader/index/Service Panel; diagnosis, personal target, treatment, or action; staging, commit, or push.

## 33. Founder Decision Sheet

| # | Decision | Founder Decision |
| ---: | --- | --- |
| 1 | Existing two PPG sources remain sufficient for the narrow wearable Profile, or a separate source-content revision is required | Pending |
| 2 | Approve wearable PPG Profile scope and raw-waveform exclusion | Pending |
| 3 | Approve Observation representation contract for point-from-series and time-series only | Pending |
| 4 | Approve separation of resting, sleeping, daily, activity, zone and recovery summaries into future Profiles | Pending |
| 5 | Approve Profile-aware retrieval/output contract | Pending |
| 6 | Approve exact six-leaf Profile-only S3 transition plan | Pending |
| 7 | Approve parent concept and spot Profile remaining `proposed`, with version remaining `v0.1` | Pending |
| 8 | Authorize a later, separately controlled local S3 execution task after exact-SHA Founder approval of this packet | Pending |

~~~text
Founder approvals = 0
Founder pending decisions = 8
Accidental approvals = 0
~~~

## 34. Recommended Next Gate

If the Founder approves all eight decisions at this packet's exact SHA, the next separately controlled task is:

~~~text
Step5-C43: Founder Approval + Execute Heart Rate S3 Locally - Wearable PPG Profile Only
~~~

That task may execute only the approved six-leaf Profile-only transition. It must keep the parent Heart Rate RegistryConcept and spot Profile `proposed`, keep `version: v0.1`, validate with the final Schema and hardened Validator, and remain outside runtime and retrieval.

No next Gate is executed automatically.
