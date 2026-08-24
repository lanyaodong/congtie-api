# Registry First Wave Pilot A - Source-Verified Transition Plan 2026-08-24 v0.1

Status: Draft / Founder Review Pending / No Lifecycle Transition Authorized

## 1. Purpose

This document independently re-audits the existing sources in the four committed Pilot A Registry records and defines a reviewable plan for possible future `source_verified` transitions. It does not modify a Registry record or execute a lifecycle transition.

The audit applies these boundaries:

```text
definition authority != method validation
method validation != clinical utility
source verification != human review
Git versioning != lifecycle promotion
Registry record != user observation
```

## 2. Repository Baseline

| Field | Verified state |
| --- | --- |
| Repository | `/Users/lanyaodong/Documents/congtie-api` |
| Branch | `main` |
| HEAD | `674b62b08abc16f56d0508bf4b03940c37dbda75` |
| `origin/main` | `674b62b08abc16f56d0508bf4b03940c37dbda75` |
| Staging | empty |
| Audit date | `2026-08-24` |

## 3. Exact Record Manifest

| Record | Candidate | SHA-256 | Current concept lifecycle | Profiles |
| --- | --- | --- | --- | --- |
| `agent/biomarker_measurement_registry/records/ME-000018.height.json` | `height` | `6e03ad4435dafb5205212377f1cfb24568be47104769321ac34bd7aba74ee504` | `proposed` | `height.standing.stadiometer` = `proposed` |
| `agent/biomarker_measurement_registry/records/ME-000019.body_weight.json` | `body_weight` | `1f533cd61110d63585589f2c54faccd4366a83862c59506a73570831d1505bcc` | `proposed` | `body_weight.scale_measured` = `proposed` |
| `agent/biomarker_measurement_registry/records/BM-000023.creatinine.json` | `creatinine` | `fa6b2ad250c6c1f8f2e4df6428970eebd5e6497061533f110dabe99c0549cbab` | `proposed` | `creatinine.serum_or_plasma.enzymatic` = `proposed` |
| `agent/biomarker_measurement_registry/records/ME-000020.heart_rate.json` | `heart_rate` | `1f0e1c65923c69296e2da8791585ad39752f2039b760c4a2fe5aca6e84d58c3e` | `proposed` | `heart_rate.spot_clinical` = `proposed`; `heart_rate.wearable_ppg_time_series_estimate` = `proposed` |

Current operational state remains:

```text
Registry records = 4
Proposed records = 4
Source-verified records = 0
Human-reviewed lifecycle records = 0
Active records = 0
Runtime-enabled records = 0
Retrieval-enabled records = 0
Published records = 0
```

## 4. Source-Verified Semantics

### 4.1 Concept `source_verified`

A concept-level `source_verified` status means:

- canonical construct definition sources have been checked against their actual content;
- definition source keys resolve;
- at least one embedded Profile has reached `source_verified` or a later reviewed status;
- relevant source keys resolve to permitted verification statuses;
- source role and scope fit the statements they support.

It does not mean every Profile is source-verified, clinical utility is established, a threshold exists, a human lifecycle review is complete, or the record can be used by runtime or retrieval.

### 4.2 Profile `source_verified`

A Profile-level `source_verified` status means its nonempty method source set has been opened and the scoped method, modality, protocol, mapping and limitation statements are supported. It does not establish equivalence across devices, platforms, assays or vendors, and it does not authorize personal interpretation or action.

### 4.3 Schema and Validator rule

The current Schema and permanent Validator permit a `source_verified` concept only when at least one embedded Profile is `source_verified`, `human_reviewed` or `active` and has source references. Definition sources must be verified; content-level verification is preferred for definition authority. A Profile promoted to `source_verified` must have nonempty, resolving source keys with permitted verification status.

## 5. Verification Methodology

Every source was reopened on `2026-08-24`. Search snippets alone were not used as verification. The audit used official terminology pages, official standards pages and PDFs, official public-health or metrology pages, PubMed metadata and abstracts, and an open-access repository where available.

Verification status in this plan means:

- `content_verified`: the actual official page, standard text, specification content, abstract or open article was read and supports the narrowly stated scope;
- `metadata_verified`: identifying metadata was checked, but supporting content was not available;
- `pending`: the source could not be checked sufficiently;
- `superseded`: the source itself was replaced and is not current for the stated role.

Abstract-level verification is explicitly identified. It is sufficient only where the record's support statement is directly present in the abstract. Publisher full text was not copied or persisted.

## 6. Source Inventory

### 6.1 Counts

```text
Unique existing source keys = 13
Independently content_verified for stated scope = 13
Metadata_verified only = 0
Pending = 0
Superseded source objects = 0
Inaccessible source objects = 0
Publisher full texts not used = 2
Proposed new SourceReference objects = 1
Proposed cross-record source linkage = 1
```

The proposed new SourceReference is an NIDDK conversion authority for creatinine. The proposed cross-record linkage reuses the already existing WHO STEPS source only if the spot Heart Rate Profile is narrowed through a separately approved content revision.

### 6.2 Existing source audit

| Source key | Exact audited title and organization/journal | URL / DOI / PMID | Access result and independent status | Source role confirmed? | Supports | Does not support | Correction or supersession | Legal/access note | Transition blocker? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `src-loinc-height` | `LOINC 8302-2, Body height`; Regenstrief Institute / LOINC | `https://loinc.org/8302-2` | Official term page opened; Active; `content_verified` | Yes, terminology and mapping authority | body-height identity; concept mapping | standing protocol; self-report equivalence; pediatric interpretation; targets | No deprecation or replacement shown | Public LOINC page; LOINC license applies | No |
| `src-loinc-weight` | `LOINC 29463-7, Body weight`; Regenstrief Institute / LOINC | `https://loinc.org/29463-7` | Official term page opened; Active; `content_verified` | Yes, terminology and mapping authority | body-weight identity; concept mapping | scale protocol; body composition; change attribution | No deprecation or replacement shown | Public LOINC page; LOINC license applies | No |
| `src-loinc-creat-mass` | `LOINC 2160-0, Creatinine [Mass/volume] in Serum or Plasma`; Regenstrief Institute / LOINC | `https://loinc.org/2160-0` | Official term page opened; Active; `content_verified` | Yes, terminology and profile mapping authority | serum/plasma mass-concentration representation | enzymatic method; assay equivalence; kidney-function equivalence | No deprecation or replacement shown | Public LOINC page; LOINC license applies | No |
| `src-loinc-creat-molar` | `LOINC 14682-9, Creatinine [Moles/volume] in Serum or Plasma`; Regenstrief Institute / LOINC | `https://loinc.org/14682-9` | Official term page opened; Active; `content_verified` | Yes, terminology and profile mapping authority | serum/plasma molar-concentration representation | enzymatic method; assay equivalence; kidney-function equivalence | No deprecation or replacement shown | Public LOINC page; LOINC license applies | No |
| `src-loinc-hr` | `LOINC 8867-4, Heart rate`; Regenstrief Institute / LOINC | `https://loinc.org/8867-4` | Official term page opened; Active in LOINC 2.82; `content_verified` | Yes, terminology and mapping authority | heart-rate identity; concept mapping; example unit context | spot method; PPG validation; ECG equivalence; rhythm diagnosis | No deprecation or replacement shown | Public LOINC page; LOINC license applies | No for concept identity; cannot verify either Profile method |
| `src-who-steps` | `WHO STEPwise Approach to NCD Risk Factor Surveillance, Part 3 Section 5: Collecting Step 2 data - Physical Measurements`; World Health Organization | `https://www.who.int/teams/noncommunicable-diseases/surveillance/systems-tools/steps/manuals`; official section PDF `https://cdn.who.int/media/docs/default-source/ncds/ncd-surveillance/steps/part3-section5.pdf?sfvrsn=a46653c7_2` | Official manuals page and PDF opened; section PDF last updated `2017-01-26`; `content_verified` | Yes, measurement method | standing height with measuring board/stadiometer context; footwear/head position; scale-based weight, zeroing, device context; a narrow automatic BP-monitor-displayed spot heart-rate procedure | every instrument; every clinical HR device; universal fasting requirement; cross-device equivalence | No supersession notice found on current official page | Public WHO material | No for Height/Weight; usable for Heart Rate only after separately approved narrowing/linkage |
| `src-wst424` | `人群健康监测人体测量方法 (WS/T 424-2013)`; National Health Commission of China | Landing `https://www.nhc.gov.cn/wjw/yingyang/201308/1f27caef0b22493e93a1da8aec2cd63a.shtml`; PDF `https://www.nhc.gov.cn/ewebeditor/uploadfile/2013/08/20130808141055922.pdf` | Official landing page and standard PDF opened; published `2013-04-18`; effective `2013-10-01`; `content_verified` | Yes, China measurement method | standing-height construct/protocol; measured weight; certified scale, calibration/zeroing, clothing/footwear and defined survey context | global thresholds; self-report equivalence; making the standard's fasting/time protocol universal outside its scope | No official withdrawal or replacement marker found | Public NHC standard PDF | No |
| `src-ucum` | `The Unified Code for Units of Measure`; Regenstrief Institute | `https://ucum.org/ucum` | Official specification opened; `content_verified` | Yes, unit syntax authority only | `cm`, `m`, `[in_i]`, `kg`, `[lb_av]`, `umol/L`, `mg/dL`, `/min` syntax and exact physical unit relationships where defined | clinical interpretation; method equivalence; assay comparability | No supersession notice found on current specification page | Public specification | No; it does not by itself explicitly state the record's creatinine `88.4` rule |
| `src-nist-creat` | `Development of Reference Measurement Procedures and Reference Materials for Creatinine`; NIST | `https://www.nist.gov/programs-projects/development-reference-measurement-procedures-and-reference-materials-creatinine` | Official page opened; updated `2025-03-26`; `content_verified` | Yes, reference measurement and traceability | isotope-dilution GC-MS/LC-MS reference procedures; serum reference materials; higher-order traceability | equivalence of all commercial enzymatic assays; clinical diagnosis; exact `88.4` conversion | Historical SRM 967 was superseded by SRM 967a; the project page remains current and also identifies current materials | Public US government page | No for traceability; yes if incorrectly used as conversion authority |
| `src-creat-method-2020` | `Clinical and Analytical Impact of Moving from Jaffe to Enzymatic Serum Creatinine Methodology`; The Journal of Applied Laboratory Medicine | DOI `10.1093/jalm/jfaa053`; PMID `32447368` | PubMed metadata and abstract opened; abstract-level `content_verified` | Yes, validation evidence | paired-method differences; glucose/hemolysis interference; continuity risk when moving methods | universal continuity; equivalence of every platform; diagnosis; exact `88.4` conversion | No correction, retraction or supersession found in checked metadata | PubMed abstract used; publisher full text not copied or persisted | No for stated method limitations |
| `src-wst4045` | `临床常用生化检验项目参考区间 第5部分：血清尿素、肌酐 (WS/T 404.5-2015)`; National Health Commission of China | `https://www.nhc.gov.cn/ewebeditor/uploadfile/2015/05/20150504152412571.pdf` | Official standard PDF opened; `content_verified` | Yes, China reference-interval and method context | China adult serum creatinine interval context; ID-MS-traceable enzymatic/Jaffe method context; μmol/L reporting; interference and system caveats | universal interval; kidney-function equivalence; all-assay equivalence; personal target | No official withdrawal or replacement marker found | Public NHC standard PDF | No; no numeric ReferenceContext is created in the current record |
| `src-hr-ppg-2020` | `Validity of wrist-worn photoplethysmography devices to measure heart rate: A systematic review and meta-analysis`; Journal of Sports Sciences | DOI `10.1080/02640414.2020.1767348`; PMID `32552580` | PubMed metadata and abstract opened; abstract-level `content_verified` | Yes, validation evidence | wrist PPG validity limitations; activity dependence; device/test heterogeneity | ECG equivalence; every device; rhythm diagnosis; universal normalization | No correction, retraction or supersession found in checked metadata | PubMed abstract used; publisher full text not copied or persisted | No for the wearable Profile's narrow limitations |
| `src-interlive-hr` | `Recommendations for determining the validity of consumer wearable heart rate devices: expert statement and checklist of the INTERLIVE Network`; British Journal of Sports Medicine | DOI `10.1136/bjsports-2020-103148`; PMID `33397674`; PMCID `PMC8273688` | PubMed metadata/abstract and open-access repository record checked; `content_verified` | Yes, validation framework | validation domains for population, criterion, index device, testing conditions, processing and analysis | device/firmware/algorithm equivalence; diagnosis; universal normalization | No correction, retraction or supersession found in checked metadata | Open-access article available; no commercial text persisted | No |

### 6.3 Proposed source changes for later approval

| Proposed action | Exact source | Role and source-key proposal | Why needed | Current task action |
| --- | --- | --- | --- | --- |
| Add one SourceReference to Creatinine and reference it from the enzymatic Profile | `eGFR Equations for Adults`; National Institute of Diabetes and Digestive and Kidney Diseases; `https://www.niddk.nih.gov/research-funding/research-programs/kidney-clinical-research-epidemiology/laboratory/glomerular-filtration-rate-equations/adults`; last reviewed May 2025 | Proposed key `src-niddk-creatinine-conversion`; `source_role = other_reviewed_role`; note `unit conversion authority` | Official NIDDK content explicitly states serum creatinine μmol/L to mg/dL is divided by `88.4`, which is algebraically equivalent to `mg/dL × 88.4 = μmol/L` | Plan only; source addition not authorized |
| Reuse existing WHO STEPS SourceReference for a narrowed Heart Rate spot Profile | Existing key `src-who-steps`; official physical-measurements section | Add key to the spot Profile only if Profile scope is narrowed to the specific automatic BP-monitor-displayed pulse procedure and protocol | Current broad `device-based spot heart-rate measurement` is not fully supported by one source; WHO STEPS supports a narrower modality/protocol | Plan only; source linkage and Profile change not authorized |

## 7. Height Audit

Record: `ME-000018.height.json`

### 7.1 Definition and mapping

LOINC `8302-2` is Active and identifies Body height. It supports the canonical construct and concept-level mapping. It does not define standing protocol, device quality or interpretation.

### 7.2 Profile method

The WHO STEPS physical-measurements guide supports standing height measured with a measuring board/stadiometer-type instrument on a firm surface, removal of footwear/headgear, defined body/head positioning and centimetre recording. WS/T 424-2013 independently supports standing height, a vertical height instrument, posture/head-position checks and 0.1 cm recording in its population-monitoring scope.

### 7.3 Units and freshness

UCUM supports `cm`, `m` and international inch `[in_i]`; the exact `m × 100 = cm` and `[in_i] × 2.54 = cm` conversions are mathematical unit conversions, not protocol comparability. LOINC is Active, WHO's official PDF is current on its manuals page, and the NHC landing page does not mark WS/T 424-2013 as withdrawn.

### 7.4 Readiness

```text
Concept: READY_FOR_SOURCE_VERIFIED
Profile height.standing.stadiometer: READY_FOR_SOURCE_VERIFIED
Blocking issues: none
```

Pediatric interpretation remains deferred; that limitation does not block source verification of the measured construct or adult-oriented initial Profile.

## 8. Body Weight Audit

Record: `ME-000019.body_weight.json`

### 8.1 Definition and mapping

LOINC `29463-7` is Active and identifies Body weight. It supports concept identity and mapping, not body composition or the measurement protocol.

### 8.2 Profile method

WHO STEPS supports measured body weight with a scale placed on a firm flat surface, zeroing, footwear/heavy-item removal, centered standing, kg recording and device identification. WS/T 424-2013 supports a certified scale, calibration with a standard mass, stable placement/zeroing, standing position and clothing/footwear conditions. The record's `calibrated scale` language is therefore within the combined source scope.

WS/T 424-2013 also gives a survey-specific morning, fasting and post-void context for people over age two. The Registry Profile correctly keeps fasting status `unknown` and says it must never be assumed; the standard's context is not generalized to every observation.

Clothing, footwear, time of day and scale identity are protocol/context metadata. They do not establish cause for short-term change. Exact `[lb_av] × 0.45359237 = kg` conversion does not establish cross-scale comparability.

### 8.3 Readiness

```text
Concept: READY_FOR_SOURCE_VERIFIED
Profile body_weight.scale_measured: READY_FOR_SOURCE_VERIFIED
Blocking issues: none
```

## 9. Creatinine Audit

Record: `BM-000023.creatinine.json`

### 9.1 Definition and mapping

LOINC `2160-0` and `14682-9` are Active serum/plasma creatinine terms that distinguish mass and molar concentration properties. Their Method field is not enzymatic. They support the two Profile-level mappings and property representations, but do not validate enzymatic provenance.

### 9.2 Method and traceability

NIST supports higher-order isotope-dilution reference procedures and reference-material traceability. It does not prove that every commercial enzymatic assay is equivalent. The 2020 JALM abstract supports material Jaffe-versus-enzymatic differences and interference/continuity limitations. WS/T 404.5-2015 supports China-specific serum creatinine method/reference context, μmol/L reporting, ID-MS traceability context and the need to account for method/system interference. It is not a global interval authority.

### 9.3 Conversion authority

The current Profile states:

```text
value_mg/dL * 88.4 = value_umol/L
conversion_verified = true
```

The existing source pool defines both units and provides creatinine terminology/property context, but no existing SourceReference explicitly states the exact `88.4` factor. Mathematical derivation from molecular mass and UCUM is not treated as equivalent to a reviewed source declaration.

The NIDDK `eGFR Equations for Adults` page explicitly states that serum creatinine in μmol/L is converted to mg/dL by dividing by `88.4`. This is an authoritative exact source for the inverse record rule, but it is not present in the current record source pool.

### 9.4 Readiness

```text
Definition/mapping readiness: READY_FOR_SOURCE_VERIFIED
Profile creatinine.serum_or_plasma.enzymatic: READY_WITH_SOURCE_ADDITION_REQUIRED
Concept lifecycle readiness: READY_WITH_SOURCE_ADDITION_REQUIRED
Blocking issue: add and review the exact NIDDK conversion SourceReference before transition
```

The source addition must be an independently approved content revision. Unit conversion must continue to remain separate from assay/platform comparability.

## 10. Heart Rate Concept Audit

Record: `ME-000020.heart_rate.json`

LOINC `8867-4` is Active and supports the Heart rate construct, concept mapping and number-rate representation. Its Method is unspecified and it does not support a spot clinical procedure, wearable PPG validation, ECG equivalence or rhythm diagnosis.

Concept definition readiness in isolation is `READY_FOR_SOURCE_VERIFIED`. The recommended record-level lifecycle remains `proposed`, however, because one initial Profile is not ready and mixed-Profile output/filtering semantics are not yet governed. A concept-level `source_verified` label could otherwise be misread as applying to both initial Profiles.

Schema technically permits a `source_verified` concept when at least one Profile is source-verified. This plan does not recommend that path until mixed-Profile output semantics and filtering are explicitly governed.

Founder Decision: Pending.

## 11. Heart Rate Profile Audits

### 11.1 Wearable PPG time-series estimate

The wrist-worn PPG systematic review/meta-analysis supports activity-dependent accuracy limits and device/test heterogeneity. The INTERLIVE statement supplies a structured validation framework covering population, criterion measure, index device, test conditions, data processing and statistical analysis. Together they support the Profile's PPG estimate boundary, activity/sampling/artifact caveats and prohibition on silent cross-platform normalization.

They do not support ECG equivalence, every device/firmware/algorithm, rhythm diagnosis, or universal cross-device normalization.

```text
Profile heart_rate.wearable_ppg_time_series_estimate:
READY_FOR_SOURCE_VERIFIED
```

### 11.2 Spot clinical

The current Profile is broad:

```text
method = device-based spot heart-rate measurement
instrument_or_device = clinical heart-rate device
source_reference_keys = []
```

LOINC is not a method authority. The wearable PPG sources do not validate a general clinical spot method. General public-health material is not a substitute.

WHO STEPS provides an authoritative but narrower path: a pulse rate displayed by a digital automatic blood-pressure monitor after a defined rest and repeated-measurement protocol. It does not validate every ECG monitor, pulse oximeter or generic clinical heart-rate device.

```text
Profile heart_rate.spot_clinical:
NOT_READY_FOR_SOURCE_VERIFIED
```

Future refinement requires one of two separately approved paths:

1. Narrow this Profile to the WHO STEPS automatic BP-monitor-displayed pulse modality and add `src-who-steps` to its source keys.
2. Define a specific device modality such as ECG-derived spot rate or pulse-oximeter pulse rate and add an authority that directly covers that modality.

Manual pulse count remains excluded from the initial Profile.

## 12. Wearable Time-Series Observation Granularity Plan

This is planning only and creates no Observation field or storage.

Future Observation governance must distinguish:

1. raw or time-stamped point series;
2. device-produced sampled series;
3. window summary;
4. resting summary;
5. sleeping summary;
6. activity summary.

Future Observation provenance must preserve:

- device and model;
- firmware;
- algorithm/version;
- source metric name;
- sampling cadence;
- aggregation window;
- activity/context;
- artifact handling and missingness;
- original timestamps;
- time zone.

A point value, time series, daily average, sleeping Heart Rate and resting Heart Rate must not be silently stored as the same Observation representation.

## 13. Source-Role Matrix

| Record/Profile scope | Definition or terminology | Method/protocol | Validation | Reference/China context | Unit syntax | Scope boundary |
| --- | --- | --- | --- | --- | --- | --- |
| Height concept | `src-loinc-height` | none | none | none | `src-ucum` | LOINC/UCUM do not validate standing protocol |
| `height.standing.stadiometer` | none | `src-who-steps`, `src-wst424` | none | `src-wst424` also supplies China context | inherited `src-ucum` | adult/pediatric interpretation remains separate |
| Body Weight concept | `src-loinc-weight` | none | none | none | `src-ucum` | Body weight is not body composition |
| `body_weight.scale_measured` | none | `src-who-steps`, `src-wst424` | none | `src-wst424` also supplies China context | inherited `src-ucum` | fasting/time context is not universalized |
| Creatinine concept/property mappings | `src-loinc-creat-mass`, `src-loinc-creat-molar` | none | none | none | `src-ucum` | LOINC Method is not enzymatic |
| `creatinine.serum_or_plasma.enzymatic` | none | `src-nist-creat` | `src-creat-method-2020` | `src-wst4045` | inherited `src-ucum`; proposed NIDDK conversion source | no assay equivalence or universal interval |
| Heart Rate concept | `src-loinc-hr` | none | none | none | `src-ucum` | no modality/rhythm support |
| `heart_rate.spot_clinical` | none | none currently | none | none | inherited `src-ucum` | not ready; source keys empty |
| `heart_rate.wearable_ppg_time_series_estimate` | none | PPG modality encoded in Profile | `src-hr-ppg-2020`, `src-interlive-hr` | none | inherited `src-ucum` | no ECG/device equivalence or rhythm diagnosis |

## 14. Source Freshness Matrix

| Source group | Checked 2026-08-24 | Freshness/correction result | Future refresh trigger |
| --- | --- | --- | --- |
| LOINC 8302-2, 29463-7, 2160-0, 14682-9, 8867-4 | Yes | All displayed Active; no deprecation found | LOINC release/status change or mapping review |
| WHO STEPS physical-measurements guide | Yes | Official manual and section PDF available; section PDF dated 2017-01-26 | WHO manual revision or Profile protocol change |
| WS/T 424-2013 | Yes | Official landing/PDF available; no withdrawal/replacement marker found | NHC replacement/withdrawal or China protocol revision |
| UCUM | Yes | Official specification available; no relevant supersession found | UCUM syntax/version change affecting used codes |
| NIST creatinine project | Yes | Current project page updated 2025-03-26; older SRM 967 superseded by 967a, while the project page remains current | NIST reference-material or method update |
| JALM creatinine-method paper | Yes | DOI/PMID/abstract match; no correction/retraction found | correction, retraction or method-policy revision |
| WS/T 404.5-2015 | Yes | Official PDF available; no withdrawal/replacement marker found | NHC interval/method standard revision |
| PPG systematic review | Yes | DOI/PMID/abstract match; no correction/retraction found | correction, retraction or materially newer review for the Profile |
| INTERLIVE statement | Yes | DOI/PMID/PMCID match; open-access record available; no correction/retraction found | checklist revision or superseding consensus |
| Proposed NIDDK conversion source | Yes | Official page last reviewed May 2025; exact factor present | source addition review and later source check |

## 15. Transition-Readiness Matrix

| Record | Concept readiness | Profile | Profile readiness | Blocking issue | AI recommendation |
| --- | --- | --- | --- | --- | --- |
| `ME-000018.height.json` | `READY_FOR_SOURCE_VERIFIED` | `height.standing.stadiometer` | `READY_FOR_SOURCE_VERIFIED` | none | S1 concept + Profile transition after Founder authorization |
| `ME-000019.body_weight.json` | `READY_FOR_SOURCE_VERIFIED` | `body_weight.scale_measured` | `READY_FOR_SOURCE_VERIFIED` | none | S1 concept + Profile transition after Founder authorization |
| `BM-000023.creatinine.json` | `READY_WITH_SOURCE_ADDITION_REQUIRED` | `creatinine.serum_or_plasma.enzymatic` | `READY_WITH_SOURCE_ADDITION_REQUIRED` | exact `88.4` authority absent from current source pool | First approve source addition, revalidate, then S2 concept + Profile transition |
| `ME-000020.heart_rate.json` | definition ready, lifecycle held at `proposed` | `heart_rate.spot_clinical` | `NOT_READY_FOR_SOURCE_VERIFIED` | empty source keys and over-broad method scope | keep Profile proposed; approve a later narrowing/source revision |
| `ME-000020.heart_rate.json` | definition ready, lifecycle held at `proposed` | `heart_rate.wearable_ppg_time_series_estimate` | `READY_FOR_SOURCE_VERIFIED` | mixed-Profile output semantics not governed | S3 Profile-only transition after Founder authorization and Observation-granularity acceptance |

## 16. Exact Future Diff Plan

No diff in this section is authorized by this document.

### 16.1 Height and Body Weight S1

For each ready record, the only lifecycle-transition changes are:

```text
RegistryConcept.lifecycle_status:
proposed -> source_verified

eligible Profile.profile_status:
proposed -> source_verified

source_references[*].access_date:
2026-08-22 -> actual transition verification date
only for sources actually reopened in the transition task

governance_metadata.last_modified_date:
2026-08-23 -> actual transition date

governance_metadata.last_source_check_date:
2026-08-22 -> actual transition date
```

Exact Height status note:

```text
Source verification completed for the canonical Height definition and height.standing.stadiometer Profile. RegistryConcept and Profile are source_verified only; no human review, active status, publication, runtime, retrieval, clinical claim, threshold or action authorization.
```

Exact Body Weight status note:

```text
Source verification completed for the canonical Body Weight definition and body_weight.scale_measured Profile. RegistryConcept and Profile are source_verified only; no human review, active status, publication, runtime, retrieval, clinical claim, threshold or action authorization.
```

### 16.2 Creatinine content-revision prerequisite

Before any Creatinine lifecycle transition, a separate approved content revision must:

1. add a `SourceReference` with proposed key `src-niddk-creatinine-conversion`, exact title and official NIDDK URL listed in Section 6.3;
2. set `source_role = other_reviewed_role` and a note identifying unit-conversion authority;
3. state that it supports only the exact serum-creatinine conversion factor and standardized-creatinine/eGFR input context;
4. state that it does not support assay equivalence, a reference interval, diagnosis or personal action;
5. add the new key to `creatinine.serum_or_plasma.enzymatic.source_reference_keys`;
6. refresh only the newly checked source's access date;
7. pass Schema and permanent semantic validation.

After that content revision is approved and committed, the S2 lifecycle diff may use the same lifecycle/date fields as S1 and this exact status note:

```text
Source verification completed for the canonical Creatinine definition and creatinine.serum_or_plasma.enzymatic Profile after exact unit-conversion authority was added. RegistryConcept and Profile are source_verified only; no assay equivalence, human review, active status, publication, runtime, retrieval, clinical claim, threshold or action authorization.
```

### 16.3 Heart Rate mixed-Profile plan

If the conservative mixed-Profile plan is authorized:

```text
RegistryConcept.lifecycle_status = proposed
heart_rate.spot_clinical.profile_status = proposed
heart_rate.wearable_ppg_time_series_estimate.profile_status:
proposed -> source_verified
```

Refresh `access_date` only for `src-hr-ppg-2020` and `src-interlive-hr` if actually reopened in the transition task. Update `last_modified_date` and `last_source_check_date` to the actual transition date.

Exact Heart Rate status note:

```text
Source verification completed for heart_rate.wearable_ppg_time_series_estimate only. The Heart Rate RegistryConcept and heart_rate.spot_clinical Profile remain proposed. No human review, active status, publication, runtime, retrieval, rhythm diagnosis, clinical claim, threshold or action authorization.
```

### 16.4 Fields held byte-stable during lifecycle-only transitions

Unless a separately approved content revision is named, do not change:

- `registry_id`;
- `candidate_key`;
- `version`;
- canonical names, aliases, definition or construct boundary;
- source title, role, support scope, DOI, PMID or URL;
- Profile method, modality, protocol or boundary;
- units, conversions, canonicalization or mappings;
- interpretation limitations;
- Agent permission boundary;
- claims, system relations or reference contexts;
- personalized-target boundary;
- `reviewed_by = []`;
- `reviewed_date = null`.

## 17. Version Recommendation

AI recommendation:

```text
version remains v0.1
```

A lifecycle/source-check metadata transition does not change stable concept identity or Profile semantics, and Git preserves the transition history. The Creatinine source addition and any Heart Rate spot narrowing are separate content revisions; their version treatment must be named in those future tasks and is not decided here.

Founder Decision: Pending.

## 18. Recommended Transition Subwaves

### Source Transition S1

- Height concept + `height.standing.stadiometer`
- Body Weight concept + `body_weight.scale_measured`

Gate: all sources reopened on the actual transition date, no source additions, exact lifecycle-only diff, Schema PASS and semantic Validator PASS.

### Source Transition S2

- Creatinine concept + `creatinine.serum_or_plasma.enzymatic`

Gate: separately approved NIDDK source addition, exact `88.4` support, source-role check, no unsupported interval claim, Schema PASS and semantic Validator PASS.

### Source Transition S3

- `heart_rate.wearable_ppg_time_series_estimate` Profile only

Gate: both PPG sources reopened, Observation-granularity plan accepted, mixed-Profile lifecycle semantics accepted, concept and spot Profile remain `proposed`, Schema PASS and semantic Validator PASS.

Heart Rate spot and concept remain proposed.

## 19. Founder Decision Sheet

| Decision | AI recommendation | Founder Decision |
| --- | --- | --- |
| 1. Height source-verification readiness | Approve concept + initial Profile for S1 | Pending |
| 2. Body Weight source-verification readiness | Approve concept + initial Profile for S1 | Pending |
| 3. Creatinine readiness | Require the named NIDDK source addition before S2 | Pending |
| 4. Heart Rate wearable Profile readiness | Approve Profile-only S3 readiness | Pending |
| 5. Heart Rate spot Profile | Keep `proposed`; do not promote with empty source keys | Pending |
| 6. Heart Rate concept lifecycle | Keep `proposed` until spot method scope/source and mixed-output governance are resolved | Pending |
| 7. Mixed Profile lifecycle semantics | Permit one Profile to be `source_verified` while concept/other Profile remain `proposed`, with explicit status note and no runtime use | Pending |
| 8. Source access-date refresh | Refresh only sources actually reopened in the authorized transition task | Pending |
| 9. Version | Keep `v0.1` for lifecycle-only transitions | Pending |
| 10. Execution authorization | Authorize later S1, S2 and S3 tasks separately; no combined automatic promotion | Pending |

Pending Founder decisions: `10`.

## 20. Explicit Non-Authorizations

This plan does not authorize:

- modification of any of the four Registry records;
- any concept or Profile lifecycle transition;
- source addition, removal or mutation;
- Profile addition, removal, split or narrowing;
- claim, threshold, system relation, mapping or reference-context change;
- human-reviewed or active status;
- runtime, retrieval, publication, loader, index, database or API behavior;
- Observation schema or storage changes;
- user-health data processing or storage;
- Service Panel creation;
- diagnosis, treatment, target or action generation;
- git add, commit or push.

## 21. Recommended Next Gate

Founder + ChatGPT reviews:

1. the 13 per-source verification results;
2. Height and Body Weight S1 readiness;
3. the exact Creatinine conversion-source addition Gate;
4. Heart Rate wearable-versus-spot readiness;
5. mixed-Profile lifecycle semantics and Observation granularity;
6. the exact future diff and no-version-bump recommendation;
7. separate authorization boundaries for S1, S2 and S3.

Do not transition records automatically.

