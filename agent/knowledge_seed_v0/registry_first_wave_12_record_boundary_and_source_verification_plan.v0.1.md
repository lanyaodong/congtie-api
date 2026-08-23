# Registry First Wave 12 Record Boundary and Source Verification Plan v0.1

- Status: Founder Approved / Pilot A Proposed-Record Creation and Numeric ID Assignment Not Authorized
- Prepared date: 2026-08-22
- Founder reviewer: 蓝耀栋
- Founder review date: 2026-08-22
- Repository anchor: `9fdd4a16b8430e3553ff53d08a55ab4c05edea47`
- Owner: Congtie Registry governance
- Scope: planning only; no Registry records, profiles, numeric IDs, lifecycle transitions, runtime, retrieval, database, API, Observation storage, or Service Panel are authorized

## 1. Purpose

This document records Founder approval of the frozen Registry First Wave 12 boundary, profile, source, unit, computation, mapping, threshold, system-relation, Agent-permission, production-order, and numeric-ID policies. Approval applies to this planning baseline only.

It does not create any `RegistryConcept`, `MeasurementProfile`, mapping, evidence claim, system relation, computation, or active Registry artifact. Terms such as `READY_FOR_PROPOSED_RECORD` are planning conclusions only and are not lifecycle values written to the Candidate Ledger.

## 2. Governance Baseline

The approved architecture remains:

```text
Longevity Knowledge Entry
= explains concepts and general evidence

Registry Concept
= defines a stable measurement construct

Measurement Profile
= defines a specimen, method, protocol, device, algorithm, equation, or reporting representation

User Observation
= records what happened to one user at one time

Service Panel
= selects Registry concepts for a service
```

Therefore:

```text
Registry Concept
!= Measurement Procedure
!= User Observation
!= Service Panel
!= Knowledge Entry
```

The approved namespace-only freeze remains in force:

- `BM`: laboratory or molecular biomarker concept;
- `ME`: physiological or functional measurement concept;
- `SC`: derived score or index;
- `QS`: validated questionnaire or scale;
- numeric Registry IDs: not assigned;
- active Registry records: zero;
- First Wave production authorization: false.

## 3. First Wave 12 Frozen Set

| Order | Candidate Key | Canonical Name ZH | Canonical Name EN | Namespace | Current Review Class | First Wave |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `apolipoprotein_b` | 载脂蛋白B | Apolipoprotein B | BM | GREEN | proposed only |
| 2 | `lipoprotein_a` | 脂蛋白(a) | Lipoprotein(a) | BM | YELLOW | proposed only |
| 3 | `hba1c` | 糖化血红蛋白 | Hemoglobin A1c | BM | GREEN | proposed only |
| 4 | `creatinine` | 肌酐 | Creatinine | BM | GREEN | proposed only |
| 5 | `estimated_glomerular_filtration_rate` | 估算肾小球滤过率 | Estimated Glomerular Filtration Rate | SC | YELLOW | proposed only |
| 6 | `systolic_blood_pressure` | 收缩压 | Systolic Blood Pressure | ME | GREEN | proposed only |
| 7 | `diastolic_blood_pressure` | 舒张压 | Diastolic Blood Pressure | ME | GREEN | proposed only |
| 8 | `height` | 身高 | Height | ME | GREEN | proposed only |
| 9 | `body_weight` | 体重 | Body Weight | ME | GREEN | proposed only |
| 10 | `heart_rate` | 心率 | Heart Rate | ME | YELLOW | proposed only |
| 11 | `sleep_total_time` | 总睡眠时间 | Total Sleep Time | ME | YELLOW | proposed only |
| 12 | `body_mass_index` | 体重指数 | Body Mass Index | SC | GREEN | proposed only |

Frozen-set audit: `12/12` Candidate Ledger keys resolve; GREEN = 8; YELLOW = 4; non-null `registry_id` = 0.

## 4. Cross-Candidate Architecture Rules

### 4.1 Concept and profile separation

One stable measurand or construct should remain one concept even when laboratories, devices, collection settings, or time windows differ. Differences that affect method, comparability, specimen, reporting, or interpretation belong in profiles unless the result semantics themselves differ.

The initial design pattern is:

```text
One Registry Concept
-> zero or more Measurement Profiles
-> zero or more External or Device Mappings
-> zero or more Use-Evidence Claims
-> zero or more Six-System Relations
```

### 4.2 Splitting rule

Split before record creation only when two candidates represent different measurands, constructs, or result meanings. Do not split only because of a different vendor, laboratory, time window, equation version, unit representation, or jurisdiction. Conversely, do not hide semantically distinct outputs inside one profile merely because they share a familiar label.

### 4.3 Observation and event context

Measurement time, source organization, original value and unit, original report interval, specimen, body site, posture, device, assay, algorithm version, verification state, and user permission belong to the Observation or event layer. The Registry defines which of those fields are required to interpret and compare the concept; it does not store real user values.

### 4.4 Method and platform breakpoints

Assay, platform, device, firmware, algorithm, protocol, or equation changes can be longitudinal breakpoints. No generic assay-equivalence factor is assumed. Cross-platform conversion is allowed only when the conversion is mathematically and semantically valid, source-verified, and method comparability is separately addressed.

### 4.5 Evidence and action boundary

Definition authority, method validation, clinical utility, and personal interpretation are separate claims. E1-E5 attaches to a claim, use context, population, method/profile, and source scope, not permanently to a Registry concept.

Knowledge availability does not authorize retrieval, personalization, action, diagnosis, treatment, measurement frequency, or personal targets. For all First Wave concepts, `action_authorization` remains `none` or `separately_gated`.

## 5. Source-Verification Method

Sources were opened and checked on 2026-08-22. Status means:

- `content_verified`: the relevant source content was opened and checked against the planned statement;
- `metadata_verified`: title, organization/journal, DOI, PMID, code identity, or other metadata was checked, but the relevant full content was not fully reviewed;
- `pending`: the source or mapping remains unverified and cannot support a source-verified record;
- `superseded`: the source remains historically useful but must not support current output.

Primary source roles:

- authoritative definition or terminology;
- method, assay, device, protocol, equation, or standardization;
- code and unit mapping;
- clinical decision or risk use context;
- China-specific standard or reporting context.

Commercial pages may support a vendor's own metric name or algorithm description only. They cannot serve as definition authority, decision-threshold authority, or clinical-utility proof.

### 5.1 Shared source catalog

| Source Key | Source | Organization / Journal | Role | Verification | URL / Identifier |
| --- | --- | --- | --- | --- | --- |
| `SRC-BEST-RESOURCE` | BEST (Biomarkers, EndpointS, and other Tools) Resource | FDA-NIH / NCBI Bookshelf | biomarker terminology and Context of Use | content_verified | https://www.ncbi.nlm.nih.gov/books/NBK326791/ |
| `SRC-BEST-DESCRIPTION` | Contents of a Biomarker Description | FDA-NIH / NCBI Bookshelf | identity, source, type, method, units | content_verified | https://www.ncbi.nlm.nih.gov/books/NBK566059/ |
| `SRC-UCUM` | UCUM Specification | Regenstrief Institute | machine-readable unit syntax | content_verified | https://ucum.org/ucum |
| `SRC-LOINC-APOB` | LOINC 1884-6, Apolipoprotein B [Mass/volume] in Serum or Plasma | Regenstrief / LOINC | profile code and units | content_verified | https://loinc.org/1884-6 |
| `SRC-APOB-STD` | International Federation of Clinical Chemistry standardization project for measurements of apolipoproteins A-I and B | Clin Chem | ApoB standardization history | metadata_verified | PMID 8149615 |
| `SRC-APO-RM` | Reference materials for the standardization of apolipoproteins A-I and B, and lipoprotein(a) | Clin Chem Lab Med | reference-material context | metadata_verified | PMID 30416418; PMCID PMC6222398 |
| `SRC-AHA-DYSLIPID-2026-GUIDELINE` | 2026 ACC/AHA/AACVPR/ABC/ACPM/ADA/AGS/APhA/ASPC/NLA/PCNA Guideline on the Management of Dyslipidemia | ACC / AHA / Circulation | guideline recommendation; primary US ApoB and Lp(a) use-context authority | content_verified | DOI 10.1161/CIR.0000000000001423; https://professional.heart.org/en/guidelines-statements/2026-accahaaacvprabcacpmadaagsaphaaspcnlapcna-guideline-on-the-management-ofcir0000000000001423 |
| `SRC-AHA-DYSLIPID-2026-SUMMARY` | 2026 Guideline on the Management of Dyslipidemia: Top Things to Know | AHA Professional Heart Daily | professional education and guideline summary; does not independently support precise clinical claims | content_verified | https://professional.heart.org/en/science-news/2026-guideline-on-the-management-of-dyslipidemia/top-things-to-know |
| `SRC-LOINC-LPA-MASS` | LOINC 10835-7, Lipoprotein(a) [Mass/volume] in Serum or Plasma | Regenstrief / LOINC | mass-concentration profile code | content_verified | https://loinc.org/10835-7 |
| `SRC-LOINC-LPA-MOLAR` | LOINC 43583-4, Lipoprotein(a) [Moles/volume] in Serum or Plasma | Regenstrief / LOINC | molar-concentration profile code | content_verified | https://loinc.org/43583-4 |
| `SRC-EAS-LPA-2022` | Lipoprotein(a) in atherosclerotic cardiovascular disease and aortic stenosis | European Atherosclerosis Society / Eur Heart J | construct, assay limits, risk-use context | content_verified | DOI 10.1093/eurheartj/ehac361; PMID 36036785; PMCID PMC9639807 |
| `SRC-ESC-EAS-2025` | 2025 Focused Update of the 2019 ESC/EAS Guidelines for the management of dyslipidaemias | ESC / EAS / Eur Heart J | corrected European guideline and jurisdiction-scoped threshold context | content_verified | DOI 10.1093/eurheartj/ehaf190; https://academic.oup.com/eurheartj/article/46/42/4359/8234482 |
| `SRC-ESC-EAS-2025-CORRECTION` | Correction to: 2025 Focused Update of the 2019 ESC/EAS Guidelines for the management of dyslipidaemias | Eur Heart J | correction notice reviewed with the main document; not a standalone guideline | content_verified | DOI 10.1093/eurheartj/ehaf1036; https://academic.oup.com/eurheartj/article/47/6/697/8384289 |
| `SRC-LOINC-HBA1C-NGSP` | LOINC 4548-4, Hemoglobin A1c/Hemoglobin.total in Blood | Regenstrief / LOINC | NGSP/DCCT-style representation | content_verified | https://loinc.org/4548-4 |
| `SRC-LOINC-HBA1C-IFCC` | LOINC 59261-8, HbA1c standardized per IFCC-RMP in Blood | Regenstrief / LOINC | IFCC representation | content_verified | https://loinc.org/59261-8 |
| `SRC-NGSP-IFCC` | IFCC Standardization: IFCC and NGSP | NGSP | reporting relationship and master equation | content_verified | https://ngsp.org/ifcc.asp |
| `SRC-NGSP-FACTORS` | Factors that Interfere with HbA1c Test Results | NGSP | assay and interpretation limitations | content_verified | https://ngsp.org/factors.asp |
| `SRC-NIDDK-A1C` | The A1C Test and Diabetes | NIDDK | construct, use, and red-cell/variant limitations | content_verified | https://www.niddk.nih.gov/health-information/diagnostic-tests/a1c-test |
| `SRC-ADA-DIAGNOSIS-2026` | Diagnosis and Classification of Diabetes: Standards of Care in Diabetes 2026 | American Diabetes Association / Diabetes Care | diagnostic decision context and confirmation | content_verified | https://diabetesjournals.org/care/article/49/Supplement_1/S27/163926/2-Diagnosis-and-Classification-of-Diabetes |
| `SRC-LOINC-CREAT-MASS` | LOINC 2160-0, Creatinine [Mass/volume] in Serum or Plasma | Regenstrief / LOINC | mass-concentration profile code | content_verified | https://loinc.org/2160-0 |
| `SRC-LOINC-CREAT-MOLAR` | LOINC 14682-9, Creatinine [Moles/volume] in Serum or Plasma | Regenstrief / LOINC | molar-concentration profile code | content_verified | https://loinc.org/14682-9 |
| `SRC-NIST-CREAT` | Development of Reference Measurement Procedures and Reference Materials for Creatinine | NIST | IDMS traceability and reference material | content_verified | https://www.nist.gov/programs-projects/development-reference-measurement-procedures-and-reference-materials-creatinine |
| `SRC-CREAT-METHOD-2020` | Clinical and Analytical Impact of Moving from Jaffe to Enzymatic Serum Creatinine Methodology | J Appl Lab Med | method comparability and interference | content_verified | DOI 10.1093/jalm/jfaa053; PMID 32447368 |
| `SRC-WST4045` | WS/T 404.5-2015, Clinical common biochemical test reference intervals, Part 5: serum urea and creatinine | National Health Commission of China | China adult interval and method applicability | content_verified | https://www.nhc.gov.cn/ewebeditor/uploadfile/2015/05/20150504152412571.pdf |
| `SRC-NIDDK-EGFR` | eGFR Equations for Adults | NIDDK | equation formula, inputs, units, limitations | content_verified | https://www.niddk.nih.gov/research-funding/research-programs/kidney-clinical-research-epidemiology/laboratory/glomerular-filtration-rate-equations/adults |
| `SRC-INKER-2021` | New Creatinine- and Cystatin C-Based Equations to Estimate GFR without Race | N Engl J Med | equation development and validation | content_verified | DOI 10.1056/NEJMoa2102953; PMID 34554658; PMCID PMC8822996 |
| `SRC-LOINC-EGFR-2021` | LOINC 98979-8, eGFR by CKD-EPI 2021 creatinine equation | Regenstrief / LOINC | equation-specific profile mapping | content_verified | https://loinc.org/98979-8 |
| `SRC-KDIGO-CKD-2024` | KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of CKD | KDIGO | eGFR clinical context and confirmation boundary | content_verified | https://kdigo.org/guidelines/ckd-evaluation-and-management/ |
| `SRC-LOINC-SBP` | LOINC 8480-6, Systolic blood pressure | Regenstrief / LOINC | concept/profile mapping and UCUM unit | content_verified | https://loinc.org/8480-6 |
| `SRC-LOINC-DBP` | LOINC 8462-4, Diastolic blood pressure | Regenstrief / LOINC | concept/profile mapping and UCUM unit | content_verified | https://loinc.org/8462-4 |
| `SRC-AHA-BP-MEAS` | Measurement of Blood Pressure in Humans | American Heart Association / Hypertension | office, home, ambulatory methods | content_verified | DOI 10.1161/HYP.0000000000000087; PMID 30827125; PMCID PMC11409525 |
| `SRC-AHA-BP-2025` | 2025 AHA/ACC/AANP/AAPA/ABC/ACCP/ACPM/AGS/AMA/ASPC/NMA/PCNA Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults | ACC / AHA / Circulation | corrected US adult decision limits and use context | content_verified | DOI 10.1161/CIR.0000000000001356; https://www.ahajournals.org/doi/10.1161/CIR.0000000000001356 |
| `SRC-AHA-BP-2025-CORR-1396` | Correction to the 2025 High Blood Pressure Guideline | Circulation | correction notice reviewed 2026-08-22; use with main guideline only | content_verified | DOI 10.1161/CIR.0000000000001396; PMID 41212942 |
| `SRC-AHA-BP-2025-CORR-1436` | Correction to the 2025 High Blood Pressure Guideline | Circulation | correction notice reviewed 2026-08-22; use with main guideline only | content_verified | DOI 10.1161/CIR.0000000000001436; PMID 41973840 |
| `SRC-AHA-BP-2025-CORR-1448` | Correction to the 2025 High Blood Pressure Guideline | Circulation | correction notice reviewed 2026-08-22; use with main guideline only | content_verified | DOI 10.1161/CIR.0000000000001448; PMID 42189957 |
| `SRC-WST872-2025` | WS/T 872—2025 基层医疗卫生机构高血压防治管理标准 | National Health Commission of China | China measurement and management context; not a global threshold authority | content_verified | published 2025-09-19; effective 2026-03-01; canonical landing https://www.nhc.gov.cn/wjw/c100309/202509/b601cb822b25461f92f7aa66c03495a8.shtml; PDF attachment https://www.nhc.gov.cn/fzs/c100048/202509/2f3f7cce449145f8b361e70b3ed4ae9a/files/WS%20T%20872%E2%80%942025-20250930105429913.pdf |
| `SRC-LOINC-HEIGHT` | LOINC 8302-2, Body height | Regenstrief / LOINC | concept mapping and units | content_verified | https://loinc.org/8302-2 |
| `SRC-LOINC-WEIGHT` | LOINC 29463-7, Body weight | Regenstrief / LOINC | concept mapping and units | content_verified | https://loinc.org/29463-7 |
| `SRC-WHO-STEPS` | WHO STEPwise Approach to NCD Risk Factor Surveillance manuals | WHO | standardized anthropometry and BP protocol | content_verified | https://www.who.int/teams/noncommunicable-diseases/surveillance/systems-tools/steps/manuals |
| `SRC-WST424` | WS/T 424-2013, Anthropometric methods in population health monitoring | National Health Commission of China | China height and weight protocol | content_verified | https://www.nhc.gov.cn/wjw/yingyang/201308/1f27caef0b22493e93a1da8aec2cd63a.shtml |
| `SRC-LOINC-HR` | LOINC 8867-4, Heart rate | Regenstrief / LOINC | concept mapping and unit | content_verified | https://loinc.org/8867-4 |
| `SRC-HR-PPG-2020` | Validity of wrist-worn photoplethysmography devices to measure heart rate | J Sports Sci | wearable profile validation and activity dependence | content_verified | DOI 10.1080/02640414.2020.1767348; PMID 32552580 |
| `SRC-INTERLIVE-HR` | Recommendations for determining the validity of consumer wearable heart rate devices | INTERLIVE Network / Br J Sports Med | device validation framework | content_verified | PMID 33397674 |
| `SRC-NHC-LITERACY-2024` | Chinese Citizens' Health Literacy: Basic Knowledge and Skills 2024 | National Health Commission of China | general China public-health context only; not heart-rate definition, method, PPG validation, or device-comparability authority | content_verified | https://www.nhc.gov.cn/xcs/c100123/202405/73a4927142f34152abed875634a3c13b.shtml |
| `SRC-AASM-ACTIGRAPHY` | Use of Actigraphy for the Evaluation of Sleep Disorders | AASM / J Clin Sleep Med | actigraphy-estimated TST and limits | content_verified | DOI 10.5664/jcsm.7230; PMID 29991437; PMCID PMC6040807 |
| `SRC-CONSENSUS-DIARY` | The Consensus Sleep Diary | Sleep | diary-based sleep interval reporting | content_verified | DOI 10.5665/sleep.1642; PMID 22294820; PMCID PMC3250369 |
| `SRC-LOINC-SLEEP-PART` | LOINC Part LP412115-0, Sleep duration | Regenstrief / LOINC | terminology part only, not a final profile code | content_verified | https://loinc.org/LP412115-0 |
| `SRC-AASM-SCORING` | AASM Manual for the Scoring of Sleep and Associated Events | AASM | PSG TST definition and scoring profile | pending | exact accessible edition/version and licensed content review pending |
| `SRC-LOINC-BMI` | LOINC 39156-5, Body mass index | Regenstrief / LOINC | construct, formula, mapping, unit | content_verified | https://loinc.org/39156-5 |
| `SRC-WHO-BMI` | Obesity and overweight fact sheet | WHO | adult BMI definition and population classification | content_verified | https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight |
| `SRC-WST428` | WS/T 428-2013, Criteria of Weight for Adults | National Health Commission of China | China adult BMI decision context | content_verified | https://www.nhc.gov.cn/ewebeditor/uploadfile/2013/08/20130808135715967.pdf |

Unique source inventory: 51 total; `content_verified` = 48; `metadata_verified` = 2; `pending` = 1; `superseded` = 0. These statuses apply only to this planning review and do not transition any Registry lifecycle.

### 5.2 Candidate-level source support boundaries

| Candidate | Source Key(s) | Supports | Does Not Support |
|---|---|---|---|
| ApoB | `SRC-BEST-DESCRIPTION`; `SRC-LOINC-APOB`; `SRC-APOB-STD`; `SRC-APO-RM`; `SRC-AHA-DYSLIPID-2026-GUIDELINE`; `SRC-AHA-DYSLIPID-2026-SUMMARY` | construct, profile mapping, standardization context, guideline-scoped use; summary is education support only | universal target, diagnosis, treatment, unverified assay equivalence, precise claims from summary alone |
| Lp(a) | `SRC-EAS-LPA-2022`; `SRC-LOINC-LPA-MASS`; `SRC-LOINC-LPA-MOLAR`; `SRC-ESC-EAS-2025`; `SRC-ESC-EAS-2025-CORRECTION` | construct, non-interconvertible mass/molar properties, assay caveats, corrected jurisdictional risk context | fixed unit conversion, universal target, personal action |
| HbA1c | `SRC-NGSP-IFCC`; `SRC-NGSP-FACTORS`; `SRC-LOINC-HBA1C-NGSP`; `SRC-LOINC-HBA1C-IFCC`; `SRC-NIDDK-A1C`; `SRC-ADA-DIAGNOSIS-2026` | standardized representations, limitations, scoped diagnostic/monitoring claims | automatic diagnosis, method-independent equivalence, personal target |
| Creatinine | `SRC-LOINC-CREAT-MASS`; `SRC-LOINC-CREAT-MOLAR`; `SRC-NIST-CREAT`; `SRC-CREAT-METHOD-2020`; `SRC-WST4045` | serum/plasma profiles, units, traceability, method and China interval context | kidney function equivalence, universal threshold, cross-method continuity |
| eGFR | `SRC-NIDDK-EGFR`; `SRC-INKER-2021`; `SRC-LOINC-EGFR-2021`; `SRC-KDIGO-CKD-2024` | CKD-EPI 2021 creatinine contract, inputs, validation, mapping, scoped use | measured GFR equivalence, other equations, diagnosis from one result |
| Systolic BP | `SRC-LOINC-SBP`; `SRC-AHA-BP-MEAS`; `SRC-AHA-BP-2025`; `SRC-AHA-BP-2025-CORR-1396`; `SRC-AHA-BP-2025-CORR-1436`; `SRC-AHA-BP-2025-CORR-1448`; `SRC-WST872-2025` | construct, protocol profiles, corrected jurisdictional limits | global target, context interchangeability, cuffless validation |
| Diastolic BP | `SRC-LOINC-DBP`; `SRC-AHA-BP-MEAS`; `SRC-AHA-BP-2025`; `SRC-AHA-BP-2025-CORR-1396`; `SRC-AHA-BP-2025-CORR-1436`; `SRC-AHA-BP-2025-CORR-1448`; `SRC-WST872-2025` | construct, protocol profiles, corrected jurisdictional limits | global target, context interchangeability, missing paired value inference |
| Height | `SRC-LOINC-HEIGHT`; `SRC-WHO-STEPS`; `SRC-WST424` | construct, units, standing measurement protocol | pediatric growth assessment, self-report equivalence |
| Body Weight | `SRC-LOINC-WEIGHT`; `SRC-WHO-STEPS`; `SRC-WST424` | construct, units, scale measurement protocol | body composition, change attribution, self-report equivalence |
| Heart Rate | `SRC-LOINC-HR`; `SRC-HR-PPG-2020`; `SRC-INTERLIVE-HR` | construct, unit, wearable validation limits | rhythm diagnosis, modality/window interchangeability |
| Total Sleep Time | `SRC-AASM-ACTIGRAPHY`; `SRC-CONSENSUS-DIARY`; `SRC-LOINC-SLEEP-PART`; `SRC-AASM-SCORING` | actigraphy/diary construct planning and terminology; PSG source remains pending | sleep quality, sleep score, cross-device equivalence, source-verified PSG profile |
| BMI | `SRC-LOINC-BMI`; `SRC-WHO-BMI`; `SRC-WST428` | construct, formula, unit, adult population contexts | body-fat measurement, diagnosis, pediatric interpretation, personal target |

## 6. Evidence and Reference Rules

### 6.1 Claim-specific evidence

Each planned claim must identify population, jurisdiction, method/profile, intended use, source role, supports, does not support, and uncertainty. A source that defines a construct does not automatically validate a method, establish a risk threshold, or authorize personal action.

### 6.2 Six reference and target layers

The following remain distinct:

1. laboratory-reported reference interval metadata;
2. population reference interval;
3. guideline clinical decision limit;
4. risk-associated threshold;
5. critical or alert value;
6. personalized-target support only.

No field named or treated as a universal `normal_range` is planned. A concrete personal target belongs to a future user/protocol layer, not the public Registry item.

### 6.3 Original report preservation

Future observations must preserve the original value, original unit, original interval, original flag, source organization, method/platform, and report document. Canonicalization never deletes the original report context.

### 6.4 Jurisdiction and minimum-profile policy

Definition and method sources prioritize authoritative international or standards sources. China standards and guidance are recorded in distinct China contexts. US, European, and China thresholds remain separate claim/reference contexts; a second international jurisdiction enters v0.1 only when a material difference, common China-user question, or explanatory benefit justifies it. No global normal range is created.

A first proposed record includes only profiles needed for the near-term user path or to validate Registry architecture, and only where the source boundary is sufficiently clear. Other profiles remain explicit future work rather than being added for completeness.

## 7. China Context Rules


- Preserve Chinese report names and aliases without claiming that one local label is globally canonical.
- Store China-common units and international units as reviewed representations; conversion does not imply method equivalence.
- Apply Chinese reference intervals and decision limits only to their stated population, age, method, specimen, and jurisdiction.
- Keep laboratory-local and future partner codes in a mapping layer; no partnership is claimed.
- `WS/T` or other standards are source-versioned; later amendments require review.
- No Service Panel, laboratory integration, sampling provider, courier arrangement, or confirmed partner is created by this plan.

## 8. Twelve Candidate Planning Packets

### 8.1 `apolipoprotein_b`

**Identity.** `载脂蛋白B / Apolipoprotein B`; abbreviation `ApoB` or `apoB`; aliases include `Apolipoprotein B-100` only where a source or report uses that label. Namespace `BM`; information type `laboratory_biomarker`; construct type `analyte`; value type `number`; current review class `GREEN`; `first_wave_proposed = true`.

**Boundary Decision: `retain_with_profiles`.** One concept represents the clinically reported ApoB mass concentration. It excludes ApoA-I, an ApoB/ApoA-I ratio, LDL-C, non-HDL-C, particle number, and atherosclerotic risk itself. Routine clinical assays predominantly reflect ApoB-100-containing particles, but the concept remains ApoB unless a method explicitly distinguishes an isoform. Serum and plasma are profile attributes.

**Profile and unit plan.** Initial profile: `apob.serum_or_plasma.immunochemical_mass`, laboratory measured, serum/plasma, immunochemical method with recognized reference-material traceability. It records platform, calibration, interference, report unit, comparability, and method-change breakpoint. Recommended unit policy is `single_canonical` with `g/L` (`g/L`) canonical and `mg/dL` a reviewed representation (`1 g/L = 100 mg/dL`). Conversion does not establish assay equivalence.

**Sources, mappings, and claim plan.** `SRC-BEST-DESCRIPTION` supports definition; `SRC-LOINC-APOB` supports profile mapping LOINC `1884-6`; `SRC-APOB-STD` and `SRC-APO-RM` support standardization context; the full `SRC-AHA-DYSLIPID-2026-GUIDELINE` supports a jurisdiction-scoped cardiovascular use claim. `SRC-AHA-DYSLIPID-2026-SUMMARY` is professional education support and does not independently support precise clinical claims. They do not support a universal personal target, diagnosis, or treatment action. Keep guideline limits separate from laboratory intervals and individualized targets.

**Reference, system, Agent, and gate.** No universal Registry threshold is recommended. Biological relationships: `T03.02` and `T03.03`; product grouping may emphasize cardiometabolic health. Agent may explain report/method context and longitudinal caveats; it may not diagnose, calculate personal risk or targets, normalize unverified assays, or recommend treatment. Action authorization: `separately_gated`. Verify initial LOINC version, China reporting conventions, and traceability wording. Readiness: `READY_WITH_NAMED_CONDITIONS`; target lifecycle `proposed`; numeric ID only after boundary/profile approval.

### 8.2 `lipoprotein_a`

**Identity.** `脂蛋白(a) / Lipoprotein(a)`; abbreviation `Lp(a)`; namespace `BM`; information type `laboratory_biomarker`; construct type `analyte`; value type `number`; current review class `YELLOW`; `first_wave_proposed = true`.

**Boundary Decision: `retain_with_profiles`.** Founder approved one Lp(a) concept with two non-interconvertible measurement-property profiles. Mass concentration and molar/particle concentration are different measurement properties, not display-unit variants. It excludes apo(a) isoform size, oxidized phospholipids, LDL-C, and Lp(a)-corrected LDL calculations. Apo(a) isoform size requires a future independent-concept or child-concept review.

**Profile and unit plan.** Initial profiles are `lpa.serum_or_plasma.mass_concentration` and `lpa.serum_or_plasma.molar_concentration`, with assay identity, calibration, isoform sensitivity, unit, method limitations, and breakpoint metadata. Unit policy is `non_convertible_representations`: `mg/dL` for mass concentration and `nmol/L` for molar concentration. No fixed universal `mg/dL` to `nmol/L` conversion is permitted; the original report unit is retained.

**Sources, mappings, and claim plan.** `SRC-EAS-LPA-2022` supports construct, assay caveats, and risk context; `SRC-LOINC-LPA-MASS` (`10835-7`) and `SRC-LOINC-LPA-MOLAR` (`43583-4`) support profile mappings; `SRC-ESC-EAS-2025` and `SRC-ESC-EAS-2025-CORRECTION` support corrected, jurisdiction-scoped claim planning. A once-in-adulthood or risk-enhancing recommendation, if retained, is a use-evidence claim, not a definition, and does not authorize personal action.

**Reference, system, Agent, and gate.** Plan profile-specific risk-threshold contexts; do not recast them as reference intervals. No universal Registry threshold or critical value is recommended. Biological relationships: `T03.02` and `T03.03`. Agent may explain unit/profile differences; it may not convert mg/dL to nmol/L, infer treatment, or set a target. Action authorization: `separately_gated`. Readiness: `READY_WITH_NAMED_CONDITIONS`; the boundary is approved, while numeric ID remains gated by an exact proposed-record authoring manifest.

### 8.3 `hba1c`

**Identity.** `糖化血红蛋白 / Hemoglobin A1c`; abbreviation `HbA1c`; aliases `A1C` and `glycated hemoglobin A1c`; namespace `BM`; information type `laboratory_biomarker`; construct type `analyte`; value type `number`; current review class `GREEN`; `first_wave_proposed = true`.

**Boundary Decision: `retain_with_profiles`.** One HbA1c concept supports NGSP/DCCT percent and IFCC mmol/mol representations of the same standardized construct. It excludes total glycated hemoglobin, estimated average glucose, point-in-time glucose, and a diabetes diagnosis. Whole blood is a profile property.

**Profile and unit plan.** Initial profile: `hba1c.whole_blood.standardized`, recording platform, NGSP certification or IFCC traceability, variant handling, red-cell turnover limitations, representation, and comparability. Recommended `single_canonical` uses IFCC `mmol/mol` with NGSP `%` as a verified representation, subject to the sourced master equation and rounding rules. LOINC `59261-8` and `4548-4` remain representation/profile mappings.

**Sources, mappings, and claim plan.** `SRC-NGSP-IFCC` and `SRC-NGSP-FACTORS` support standardization and representation; `SRC-LOINC-HBA1C-NGSP` and `SRC-LOINC-HBA1C-IFCC` support mappings; `SRC-NIDDK-A1C` supports limitations; `SRC-ADA-DIAGNOSIS-2026` supports claim-scoped diagnostic and monitoring contexts. Separate screening/diagnostic limits from monitoring claims. A single value never automatically creates a diagnosis.

**Reference, system, Agent, and gate.** Laboratory interval, decision limit, monitoring use, and risk association remain distinct. Biological relationship: `T03.02`, with secondary `T03.01`. Agent may explain representations and limitations; it may not diagnose, substitute an untraceable method, or set a personal target. Action authorization: `separately_gated`. Verify conversion implementation, rounding, mappings, and China source. Readiness: `READY_WITH_NAMED_CONDITIONS`; lifecycle target `proposed`.

### 8.4 `creatinine`

**Identity.** `肌酐 / Creatinine`; abbreviation `Cr` only as a potentially ambiguous alias; namespace `BM`; information type `laboratory_biomarker`; construct type `analyte`; value type `number`; current review class `GREEN`; `first_wave_proposed = true`.

**Boundary Decision: `retain_with_profiles`.** The concept covers serum/plasma creatinine concentration. It excludes urine creatinine, creatinine clearance, eGFR, cystatin C, and kidney function as a broader construct. Enzymatic and Jaffe procedures are profiles but can create trend breakpoints.

**Profile and unit plan.** The v0.1 initial profile is `creatinine.serum_or_plasma.enzymatic`, recording IDMS traceability, specimen, platform, interference, unit, and comparability. `creatinine.serum_or_plasma.jaffe` is deferred because its interference and comparability boundaries deserve a separately reviewed profile. Recommended `single_canonical` uses `umol/L` with `mg/dL` as a reviewed representation (`mg/dL x 88.4 = umol/L`). Conversion does not resolve method differences.

**Sources, mappings, and claim plan.** `SRC-LOINC-CREAT-MASS` (`2160-0`) and `SRC-LOINC-CREAT-MOLAR` (`14682-9`) support profile mappings; `SRC-NIST-CREAT` and `SRC-CREAT-METHOD-2020` support traceability and method limits; `SRC-WST4045` supports a China-specific reference context. Plan an eGFR-input claim and a kidney-assessment context claim, not a concept-wide kidney-function assertion.

**Reference, system, Agent, and gate.** Preserve report intervals and source-specific China interval metadata; no universal concept threshold is planned. Biological relationship: `T03.02`. Agent may explain unit/method context and eGFR lineage; it may not diagnose kidney disease, equate creatinine with kidney function, or compare unreviewed methods. Action authorization: `separately_gated`. Readiness: `READY_WITH_NAMED_CONDITIONS`; lifecycle target `proposed`; ID after initial profile order approval.


### 8.5 `estimated_glomerular_filtration_rate`

**Identity.** `估算肾小球滤过率 / Estimated Glomerular Filtration Rate`; abbreviation `eGFR`; namespace `SC`; information type `derived_score_index`; construct type `derived_index`; value type `number`; current review class `YELLOW`; `first_wave_proposed = true`.

**Boundary Decision: `retain_with_profiles`.** Use one eGFR concept with equation-specific profiles. The first profile is `egfr.ckd_epi_2021_creatinine`. Future cystatin-C-only and creatinine-plus-cystatin-C equations require distinct profiles and reviewed computation contracts. Measured GFR, creatinine clearance, and raw creatinine are separate concepts. Equation-specific child concepts are not required unless later evidence shows that profile separation cannot preserve semantics.

**Profile and computation plan.** Founder approved one eGFR concept with equation-specific profiles. The initial `egfr.ckd_epi_2021_creatinine` profile is derived and limited to adults age 18+, standardized serum creatinine, age, and the equation's female/male sex category; it uses no race coefficient and records equation name/version, rounding/capping behavior, limitations, and source. Inputs are registry concept `creatinine`, user-context `age_years`, and governed categorical user-context `sex_at_birth`; these are equation parameters, not BM/ME concepts. `sex_at_birth` is currently the governed user-context source for resolving the binary sex category required by this equation. It is not a general gender-identity inference and does not authorize broader clinical conclusions. Unit policy is `single_canonical` with `mL/min/{1.73_m2}`; no unindexed mL/min conversion is allowed without body-surface-area inputs and separate governance.

**Sources, mappings, and claim plan.** `SRC-NIDDK-EGFR` supports the equation contract and applicability; `SRC-INKER-2021` supports derivation/validation metadata (DOI `10.1056/NEJMoa2102953`, PMID `34554658`); `SRC-LOINC-EGFR-2021` supports profile mapping LOINC `98979-8`; `SRC-KDIGO-CKD-2024` supports claim-scoped kidney-disease interpretation. These do not support measured-GFR equivalence, use outside the stated population, or diagnosis from one result.

**Reference, system, Agent, and gate.** Laboratory-reported intervals/flags are preserved, while guideline decision categories are separate claim contexts. No universal critical value or personal target is planned. Biological relationship: `T03.02`. Agent may explain equation lineage, inputs, applicability, and method breakpoints; it may not fabricate missing age/sex, substitute an equation silently, diagnose, or compare incompatible equations as one continuous trend. Action authorization: `separately_gated`. Readiness: `READY_WITH_NAMED_CONDITIONS`; the concept/equation-profile policy and adult initial scope are approved, while record production and ID allocation await Pilot B authorization.

### 8.6 `systolic_blood_pressure`

**Identity.** `收缩压 / Systolic Blood Pressure`; abbreviation `SBP`; namespace `ME`; information type `physiological_measurement`; construct type `physiological_measurement`; value type `number`; current review class `GREEN`; `first_wave_proposed = true`.

**Boundary Decision: `retain_with_profiles`.** SBP is a separate concept from DBP but both reference the same blood-pressure measurement event when acquired together. Office, home, and ambulatory contexts are profiles. Central aortic pressure, invasive arterial pressure, pulmonary pressure, and unvalidated cuffless estimates are excluded.

**Profile and unit plan.** The v0.1 profiles are `bp.office.upper_arm` and `bp.home.upper_arm`; `bp.ambulatory.upper_arm` is deferred, and cuffless estimates are excluded from v0.1. Each initial profile records body site, posture, rest, cuff size, repeated-reading protocol, validated device, oscillometric/manual method, timestamp, and averaging window. Unit policy is `single_canonical` with UCUM `mm[Hg]`. Context or method changes are explicit breakpoints.

**Sources, mappings, and claim plan.** `SRC-LOINC-SBP` supports LOINC `8480-6`; `SRC-AHA-BP-MEAS` supports protocol/method planning; `SRC-AHA-BP-2025` plus its three reviewed correction notices and `SRC-WST872-2025` support separate, corrected jurisdictional decision contexts. They do not establish one global target or make office, home, and ambulatory values interchangeable.

**Reference, system, Agent, and gate.** Separate source-specific decision limits from report metadata, risk thresholds, and alert governance. Do not encode `120/80` as a universal personal target. Biological relationship: `T03.03`, with product grouping in cardiopulmonary/cardiometabolic review. Agent may explain protocol and paired-event context; it may not diagnose hypertension, average incompatible contexts, or prescribe action. Action authorization: `separately_gated`. Readiness: `READY_WITH_NAMED_CONDITIONS`; office/home scope is approved, while exact source selection and Pilot B record authorization remain gated.

### 8.7 `diastolic_blood_pressure`

**Identity.** `舒张压 / Diastolic Blood Pressure`; abbreviation `DBP`; namespace `ME`; information type `physiological_measurement`; construct type `physiological_measurement`; value type `number`; current review class `GREEN`; `first_wave_proposed = true`.

**Boundary Decision: `retain_with_profiles`.** DBP remains distinct from SBP, pulse pressure, mean arterial pressure, and a combined `blood pressure` record. A future observation links SBP and DBP to the same event without merging their Registry identities. Office, home, and ambulatory contexts are profiles.

**Profile and unit plan.** Mirror the SBP profile keys and protocol metadata so paired values remain aligned: upper-arm site, posture, rest, cuff, repeat protocol, method, device validation, and averaging window. Unit policy is `single_canonical` with `mm[Hg]`. Pairing metadata must not imply that a missing SBP/DBP value is normal.

**Sources, mappings, and claim plan.** `SRC-LOINC-DBP` supports LOINC `8462-4`; method and jurisdiction sources are `SRC-AHA-BP-MEAS`, `SRC-AHA-BP-2025` plus its three reviewed correction notices, and `SRC-WST872-2025`. Claim evidence is profile- and jurisdiction-scoped and does not authorize one global personal target.

**Reference, system, Agent, and gate.** Use the same separated reference/decision/risk/alert model as SBP. Biological relationship: `T03.03`. Agent may explain paired-event and protocol context but may not diagnose, fill a missing paired value, or combine incompatible windows. Action authorization: `separately_gated`. Readiness: `READY_WITH_NAMED_CONDITIONS`; produce SBP and DBP records in the same review batch after paired-event governance is accepted.

### 8.8 `height`

**Identity.** `身高 / Height`; aliases include `standing height` only for the measured profile. Namespace `ME`; information type `physiological_measurement`; construct type `anthropometric_measurement`; value type `number`; current review class `GREEN`; `first_wave_proposed = true`.

**Boundary Decision: `retain_with_profiles`.** One concept covers human height, with standing measured height as the first profile. Recumbent length, segmental height, arm span, and stature estimate are separate future concepts or profiles only after boundary review. Adult and pediatric interpretation differ, but the measured construct need not split. Self-report is a lower-confidence later profile.

**Profile and unit plan.** Initial profile `height.standing.stadiometer` records stadiometer, shoes/no shoes, posture, surface, protocol, and measurement precision. A `height.self_reported` profile is deferred. Recommended `single_canonical` uses `cm`; reviewed representations may include `m` and `[in_i]`. Conversion is mathematical; measurement quality remains profile-specific. Height is an input to BMI.

**Sources, mappings, and claim plan.** `SRC-LOINC-HEIGHT` supports LOINC `8302-2`; `SRC-WHO-STEPS` and `SRC-WST424` support measurement protocol. These do not support pediatric growth interpretation without age/sex/reference data or validate self-report as equivalent to measured height.

**Reference, system, Agent, and gate.** No universal threshold is recommended. Pediatric percentiles are future use-context resources, not a concept-level normal range. Biological relationship: `T03.04`, with product grouping in anthropometry/body capability context. Agent may explain protocol, unit, and BMI lineage; it may not infer height, diagnose growth disorders, or treat self-report as measured. Action authorization: `none`. Readiness: `READY_FOR_PROPOSED_RECORD`; lifecycle target `proposed`; ID only at approved proposed-record creation.

### 8.9 `body_weight`

**Identity.** `体重 / Body Weight`; alias `weight` only when human body context is explicit; namespace `ME`; information type `physiological_measurement`; construct type `anthropometric_measurement`; value type `number`; current review class `GREEN`; `first_wave_proposed = true`.

**Boundary Decision: `retain_with_profiles`.** One concept covers human body weight. It excludes body composition, fat mass, lean mass, fluid status, and weight-change rate. Measured and self-reported values are separate profiles, not interchangeable evidence.

**Profile and unit plan.** Initial profile `body_weight.scale_measured` records scale/device, calibration, clothing, time of day, and optional fasting/post-void context for trend interpretation. A `body_weight.self_reported` profile is deferred or explicitly lower confidence. Recommended `single_canonical` uses `kg`; `[lb_av]` is a reviewed representation. Device changes can be trend breakpoints. Body weight is an input to BMI.

**Sources, mappings, and claim plan.** `SRC-LOINC-WEIGHT` supports LOINC `29463-7`; `SRC-WHO-STEPS` and `SRC-WST424` support measurement protocol. These do not establish body composition, validate every consumer scale, or support interpreting short-term change as fat or muscle change.

**Reference, system, Agent, and gate.** No universal concept threshold is recommended. Biological relationships: `T03.01`, `T03.02`, and `T03.04`; product grouping is anthropometry. Agent may explain protocol, unit, context, and BMI lineage; it may not infer composition, diagnose, moralize weight, or set a target. Action authorization: `none`. Readiness: `READY_FOR_PROPOSED_RECORD`; lifecycle target `proposed`; ID only at approved proposed-record creation.

### 8.10 `heart_rate`

**Identity.** `心率 / Heart Rate`; abbreviation `HR`; aliases include `pulse rate` only in a source/profile that establishes equivalence. Namespace `ME`; information type `physiological_measurement`; construct type `physiological_measurement`; value type `number`; current review class `YELLOW`; `first_wave_proposed = true`.

**Boundary Decision: `retain_with_profiles`.** Follow Founder direction: one heart-rate concept with explicit contexts/windows. Resting, sleeping, spot clinical, and activity/exercise values are profiles or observation contexts, not separate concepts. Atrial/ventricular rate distinctions, rhythm diagnosis, heart-rate recovery, and proprietary zone scores are separate constructs.

**Profile and unit plan.** The v0.1 initial profiles are `heart_rate.spot_clinical` and `heart_rate.wearable_ppg_time_series_estimate`. The spot profile records clinical device, ECG or pulse-count method as applicable, body state, posture, rest, measurement window, and provenance. The wearable profile is explicitly estimated and records PPG device, firmware, algorithm, sampling, aggregation, artifact handling, and quality. Resting, sleeping, and activity/exercise summaries, heart-rate zones, and heart-rate recovery are deferred because each needs distinct aggregation, window, or algorithm semantics. Recommended `single_canonical` uses UCUM `/min` (display may be bpm; `{beats}/min` only if the mapping source requires it). Context and algorithm changes are breakpoints.

**Sources, mappings, and claim plan.** `SRC-LOINC-HR` supports LOINC `8867-4`; `SRC-HR-PPG-2020` and `SRC-INTERLIVE-HR` support device/profile limitations. `SRC-NHC-LITERACY-2024` supplies general China public-health context only and does not support the heart-rate definition, measurement method, PPG validity, or device comparability; a China-specific method/profile source remains pending. These sources do not make PPG, ECG, resting, sleeping, and exercise values interchangeable or authorize rhythm diagnosis.

**Reference, system, Agent, and gate.** No universal Registry threshold is recommended; clinical alerts require separate service governance. Biological relationship: `T03.03`, with secondary `T03.01`. Agent may explain window, modality, artifact, and comparability; it may not diagnose arrhythmia, erase context, or use a device score to dismiss symptoms. Action authorization: `separately_gated`. Readiness: `READY_WITH_NAMED_CONDITIONS`; the one-concept model and two-profile v0.1 set are approved, while the exact Pilot A authoring manifest and numeric-ID gate remain pending.

### 8.11 `sleep_total_time`

**Identity.** `总睡眠时间 / Total Sleep Time`; abbreviation `TST`; legacy alias `sleep duration` is accepted only when source semantics are verified. Namespace `ME`; information type `physiological_measurement`; construct type `sleep_interval_measurement`; value type `duration`; current review class `YELLOW`; `first_wave_proposed = true`.

**Boundary Decision: `retain_with_profiles`.** One concept represents total time classified or reported as sleep within a defined sleep event/window. It excludes time in bed, sleep opportunity, sleep latency, WASO, sleep efficiency, sleep quality, sleep score, and sleep stages. Main-sleep TST and 24-hour TST remain one concept only when observation context explicitly records window and nap inclusion. Legacy `Sleep Duration` ambiguity does not block a clean TST record.

**Profile and unit plan.** The v0.1 initial profiles are `tst.user_report`, `tst.sleep_diary`, and `tst.wearable_estimate`. Each records the defined sleep event/window, main sleep versus total 24-hour sleep, nap inclusion, source modality, algorithm/scoring version where applicable, uncertainty, and aggregation. `tst.psg` and `tst.clinical_actigraphy` are deferred. Recommended `single_canonical` uses minutes (`min`); hours (`h`) are a reviewed mathematical representation. Profiles are not method-equivalent.

**Sources, mappings, and claim plan.** `SRC-LOINC-SLEEP-PART` supports terminology only; final profile-level LOINC mappings remain `pending`. `SRC-AASM-ACTIGRAPHY` supports future clinical-actigraphy planning; `SRC-CONSENSUS-DIARY` supports diary constructs; `SRC-AASM-SCORING` remains pending for an accessible, exact-version, legally usable, content-reviewed PSG scoring authority. The pending PSG authority does not block the clean TST concept or the three initial profiles. These sources do not validate consumer algorithms across brands or equate TST with sleep quality.

**Reference, system, Agent, and gate.** Population duration guidance, risk associations, and personal sleep need are separate claim contexts; no universal Registry threshold or critical value is recommended. Biological relationships: `T03.05`, `T03.01`, and `T03.06`; product grouping is sleep/recovery. Agent may explain event/window, modality, uncertainty, and device breakpoints; it may not diagnose a sleep disorder, merge TST with time in bed, or compare proprietary algorithms without validation. Action authorization: `separately_gated`. Readiness: `READY_WITH_NAMED_CONDITIONS`; the initial profile set is approved, and PSG remains a non-blocking deferred profile with its own source gate.

### 8.12 `body_mass_index`

**Identity.** `体重指数 / Body Mass Index`; abbreviation `BMI`; aliases include `身体质量指数` and `体质指数` where used by a source or report. Namespace `SC`; information type `derived_score_index`; construct type `derived_index`; value type `number`; current review class `GREEN`; `first_wave_proposed = true`.

**Boundary Decision: `retain_with_profiles`.** BMI is one derived concept calculated from height and body weight. It is not body-fat percentage, body composition, adiposity diagnosis, disease diagnosis, or a personal target. The measured construct and formula do not split by age; v0.1 interpretation is adult-only, while pediatric growth percentiles and age-sex reference contexts are deferred.

**Profile and computation plan.** Initial computation profile `bmi.metric.standard` uses registry concepts `height` and `body_weight`: weight in kilograms divided by squared height in metres. Record source observations, unit normalization status, formula version, and limitations. Recommended `single_canonical` uses UCUM `kg/m2`. Do not compute from estimated height or weight without preserving their lower-confidence profiles.

**Sources, mappings, and claim plan.** `SRC-LOINC-BMI` supports LOINC `39156-5`, formula, and unit; `SRC-WHO-BMI` supports adult population interpretation; `SRC-WST428` supports China adult decision context. These do not make BMI a direct body-composition measure, support pediatric interpretation without age/sex growth references, or authorize diagnosis.

**Reference, system, Agent, and gate.** WHO and China adult categories are separate jurisdiction/context resources; pediatric percentiles are deferred. No critical value or personal target belongs in the concept. Biological relationships: `T03.02` and `T03.04`, with product grouping in anthropometry. Agent may explain formula, inputs, units, and limitations; it may not diagnose, infer body fat, moralize weight, or create a personal target. Action authorization: `none`. Readiness: `READY_FOR_PROPOSED_RECORD`; produce after height and body-weight candidate lineage is approved; lifecycle target `proposed`; ID assigned only at approved creation.

## 9. Cross-Candidate Dependency Graph

```text
height + body_weight
  -> body_mass_index

creatinine + age_years + sex_at_birth
  -> estimated_glomerular_filtration_rate
     [egfr.ckd_epi_2021_creatinine]

systolic_blood_pressure + diastolic_blood_pressure
  -> same future measurement-event reference
     (two Registry concepts, no merged value)

heart_rate
  -> spot clinical / wearable PPG time-series estimate
     (resting / sleeping / activity summaries, zones, and recovery deferred)

sleep_total_time
  -> user report / sleep diary / wearable estimate
     (PSG and clinical actigraphy deferred)
```

Derived records must resolve Registry-concept inputs to the approved candidate ledger. User-context inputs are formula parameters, not Registry concepts or user observations in this document.

### 9.1 Boundary Matrix

| Candidate | Boundary Decision | Profiles Planned | Split Needed? | First Record Readiness |
|---|---|---:|---|---|
| Apolipoprotein B | retain_with_profiles | 1 initial lab profile | No | READY_WITH_NAMED_CONDITIONS |
| Lipoprotein(a) | retain_with_profiles | 2 non-interconvertible measurement-property profiles | No; apo(a) isoform later | READY_WITH_NAMED_CONDITIONS |
| HbA1c | retain_with_profiles | 1 standardized profile, two representations | No | READY_WITH_NAMED_CONDITIONS |
| Creatinine | retain_with_profiles | enzymatic first; Jaffe deferred | No | READY_WITH_NAMED_CONDITIONS |
| eGFR | retain_with_profiles | equation-specific | No now; revisit if profile semantics fail | READY_WITH_NAMED_CONDITIONS |
| Systolic BP | retain_with_profiles | office + home; ambulatory later | No | READY_WITH_NAMED_CONDITIONS |
| Diastolic BP | retain_with_profiles | office + home; ambulatory later | No | READY_WITH_NAMED_CONDITIONS |
| Height | retain_with_profiles | standing measured; self-report later | No | READY_FOR_PROPOSED_RECORD |
| Body Weight | retain_with_profiles | scale measured; self-report later | No | READY_FOR_PROPOSED_RECORD |
| Heart Rate | retain_with_profiles | spot clinical + wearable PPG estimate; summaries deferred | No; minimal set approved | READY_WITH_NAMED_CONDITIONS |
| Total Sleep Time | retain_with_profiles | report/diary/wearable; PSG/clinical actigraphy deferred | No; event/window required | READY_WITH_NAMED_CONDITIONS |
| BMI | retain_with_profiles | metric formula + interpretation contexts | No | READY_FOR_PROPOSED_RECORD |

## 10. Recommended Production Subwaves

### Pilot A - foundational inputs and direct measurements

1. Height
2. Body Weight
3. Creatinine
4. Heart Rate

This group tests ME/BM identity, profile metadata, protocol context, unit handling, device/method breakpoints, and source mappings without first requiring a derived-record chain.

### Pilot B - derived and paired concepts

5. BMI
6. eGFR
7. Systolic Blood Pressure
8. Diastolic Blood Pressure

BMI follows approved height/weight lineage; eGFR follows creatinine and its equation contract. SBP/DBP are produced together to test two concepts linked to one measurement event.

### Pilot C - complex laboratory and sleep concepts

9. Apolipoprotein B
10. Lipoprotein(a)
11. HbA1c
12. Total Sleep Time

This group exercises standardization, method-sensitive interpretation, non-convertible units, jurisdictional thresholds, and multi-modality sleep estimates. Founder approved the Pilot A to Pilot B to Pilot C planning order; this does not authorize production.

## 11. Numeric ID Assignment Options

| Option | Timing | Benefit | Risk |
|---|---|---|---|
| A | At draft/proposed-record authoring start | Simple references during drafting | Wastes or destabilizes IDs if a boundary splits or merges |
| B | After Founder approves boundary and exact proposed-record manifest, immediately before record creation | Preserves stable references while avoiding premature allocation | Requires a small controlled allocation gate |
| C | After human review of the completed proposed record | Minimizes abandoned IDs | Draft lineage needs temporary keys longer and cross-record validation is harder |

**Founder decision: Option B approved.** Keep namespaces frozen and allocate monotonic, non-semantic numeric IDs only after the boundary and exact proposed-record authoring manifest are approved, in a controlled allocation manifest immediately before separately authorized proposed-record creation. The order must not encode clinical priority, body system, dependency, or Pilot rank. A split/merge question must be closed before allocation. Derived dependencies affect production order, not ID meaning or sequence.

No numeric Registry ID is assigned in this plan.

## 12. Lifecycle Recommendation

Founder approved `proposed` as the only permitted first lifecycle target for a future machine-readable record. A profile or external mapping may be marked mapped only after its code, version, source, and scope are verified under the Schema. Transition to `source_verified` requires all definition/profile/computation/claim sources used by that record to satisfy the permanent Validator and an explicit review. `human_reviewed` and `active` remain later Founder gates.

| Candidate group | Recommended first target | Next possible gate | Direct human_reviewed/active? |
|---|---|---|---|
| Pilot A | proposed | mapped or source_verified after source review | No |
| Pilot B | proposed | source_verified after dependency/equation review | No |
| Pilot C | proposed | mapped/source_verified after method and threshold review | No |

## 13. Source Coverage Matrix

| Candidate | Definition Source | Method Source | Claim Source | China Source | Verification Status |
|---|---|---|---|---|---|
| ApoB | BEST; LOINC | WHO-IFCC standardization sources | full AHA/ACC 2026 guideline; AHA summary supporting only | China-specific profile source pending | content_verified plus metadata_verified |
| Lp(a) | EAS 2022; LOINC | EAS assay discussion | corrected ESC/EAS 2025 update | China-specific source pending | content_verified |
| HbA1c | NGSP; LOINC | NGSP/IFCC | ADA 2026; NIDDK limitations | China-specific source pending | content_verified |
| Creatinine | LOINC | NIST; method review | NIDDK/KDIGO through eGFR use | WS/T 404.5 | content_verified |
| eGFR | NIDDK; LOINC | Inker 2021 equation | KDIGO 2024 | China-specific equation guidance pending | content_verified |
| Systolic BP | LOINC | AHA measurement statement | AHA 2025 plus three reviewed corrections | WS/T 872—2025 official landing and attachment | content_verified |
| Diastolic BP | LOINC | AHA measurement statement | AHA 2025 plus three reviewed corrections | WS/T 872—2025 official landing and attachment | content_verified |
| Height | LOINC | WHO STEPS | use claim deferred | WS/T 424 | content_verified |
| Body Weight | LOINC | WHO STEPS | use claim deferred | WS/T 424 | content_verified |
| Heart Rate | LOINC | PPG review; INTERLIVE | use claim deferred | NHC literacy general context only; China method source pending | content_verified plus metadata_verified |
| Total Sleep Time | LOINC terminology part | sleep diary; wearable sources; PSG scoring pending | population-use claim deferred | China-specific source pending | content_verified plus pending |
| BMI | LOINC | formula in LOINC/WHO | WHO adult context | WS/T 428 | content_verified |

Shared inventory: 51 unique sources, 48 `content_verified`, 2 `metadata_verified`, 1 `pending`, and 0 `superseded`. The pending AASM scoring source prevents a source-verified PSG profile but does not block the TST concept or its user-report, sleep-diary, and wearable-estimate initial profiles. No DOI, PMID, URL, code, or title is promoted beyond the verification status recorded in section 5.

## 14. Units, Computations, and External Mappings

### 14.1 Units / Computation Matrix

| Candidate | Unit Policy | Units | Conversion | Computation Inputs | Formula / Version |
|---|---|---|---|---|---|
| ApoB | single_canonical proposed | g/L; mg/dL | 1 g/L = 100 mg/dL | none | not applicable |
| Lp(a) | non_convertible_representations | mg/dL; nmol/L | fixed conversion prohibited | none | not applicable |
| HbA1c | single_canonical proposed | mmol/mol; % | NGSP/IFCC master equation, reviewed rounding | none | NGSP/IFCC current reviewed relationship |
| Creatinine | single_canonical proposed | umol/L; mg/dL | creatinine-specific factor 88.4 | none | not applicable |
| eGFR | single_canonical | mL/min/{1.73_m2} | unindexing prohibited without governed inputs | creatinine; age_years; sex_at_birth | CKD-EPI 2021 creatinine |
| Systolic BP | single_canonical | mm[Hg] | none | none | not applicable |
| Diastolic BP | single_canonical | mm[Hg] | none | none | not applicable |
| Height | single_canonical | cm; m; [in_i] | reviewed length conversion | none | not applicable |
| Body Weight | single_canonical | kg; [lb_av] | reviewed mass conversion | none | not applicable |
| Heart Rate | single_canonical | /min; display bpm | representation only | none | profile/window algorithm where estimated |
| Total Sleep Time | single_canonical | min; h | 60 min = 1 h | none | scoring/algorithm is profile-specific |
| BMI | single_canonical | kg/m2 | input normalization required | height; body_weight | kg / m2 |

### 14.2 LOINC / UCUM / China Mapping Matrix

| Candidate | Concept Mapping | Profile Mapping | LOINC Status | UCUM Status | China Mapping Status |
|---|---|---|---|---|---|
| ApoB | canonical analyte | serum/plasma mass | `1884-6` reviewed | g/L, mg/dL reviewed | local/standard mapping pending |
| Lp(a) | canonical analyte | mass and molar separate | `10835-7`, `43583-4` reviewed | mg/dL, nmol/L reviewed; no conversion | pending |
| HbA1c | standardized fraction | NGSP % and IFCC molar | `4548-4`, `59261-8` reviewed | %, mmol/mol reviewed | standard/code mapping pending |
| Creatinine | serum/plasma analyte | mass and molar; method metadata | `2160-0`, `14682-9` reviewed | mg/dL, umol/L reviewed | WS/T reference context; local code pending |
| eGFR | derived construct | CKD-EPI 2021 creatinine | `98979-8` reviewed | mL/min/{1.73_m2} reviewed | equation/code mapping pending |
| Systolic BP | pressure concept | office/home first; ambulatory deferred | `8480-6` reviewed | mm[Hg] reviewed | WS/T protocol context; local code pending |
| Diastolic BP | pressure concept | office/home first; ambulatory deferred | `8462-4` reviewed | mm[Hg] reviewed | WS/T protocol context; local code pending |
| Height | anthropometric concept | standing measured | `8302-2` reviewed | cm/m/[in_i] reviewed | WS/T 424 context |
| Body Weight | anthropometric concept | scale measured | `29463-7` reviewed | kg/[lb_av] reviewed | WS/T 424 context |
| Heart Rate | rate concept | spot clinical and wearable PPG time-series estimate | `8867-4` reviewed | /min reviewed | local/device mapping pending |
| Total Sleep Time | sleep-duration construct | source-specific codes unresolved | final code pending; LP412115-0 terminology only | min/h reviewed | pending |
| BMI | derived index | metric formula | `39156-5` reviewed | kg/m2 reviewed | WS/T 428 context |

LOINC mappings are not forced onto a concept when specimen, method, time aspect, or representation belongs to a profile. Laboratory-local and device-vendor codes remain future mapping-layer records. No code is guessed.

## 15. Reference / Threshold Matrix

| Candidate | Lab Interval | Clinical Limit | Risk Threshold | Critical Value | Personalized Target Placement |
|---|---|---|---|---|---|
| ApoB | Preserve reported interval | guideline/jurisdiction claim only | claim-specific | none at concept level | future governed protocol |
| Lp(a) | Preserve reported interval | not treated as generic interval | profile/jurisdiction-specific | none recommended | future governed protocol |
| HbA1c | Preserve reported interval | diagnostic/monitoring claim, population scoped | separate association claim | none at concept level | future clinical/protocol layer |
| Creatinine | Preserve reported interval; WS/T context when applicable | none universal | none universal | service-specific lab alert only | future governed protocol |
| eGFR | Preserve report flag/context | KDIGO context, equation/population scoped | separate prognosis claim | service-specific escalation only | future governed protocol |
| Systolic BP | not a laboratory interval | guideline and measurement-context specific | separate risk claim | separate clinical escalation governance | future governed protocol |
| Diastolic BP | not a laboratory interval | guideline and measurement-context specific | separate risk claim | separate clinical escalation governance | future governed protocol |
| Height | not generally applicable | pediatric growth context only | none | none | future user layer if justified |
| Body Weight | not generally applicable | none universal | separate population association only | none | future user layer if justified |
| Heart Rate | source/device report context | context-specific only | separate claim | separate symptom/service governance | future governed protocol |
| Total Sleep Time | not generally applicable | population guidance is not a lab limit | separate population association only | none | future user/protocol layer |
| BMI | not a laboratory interval | adult jurisdiction categories; pediatric percentiles separate | separate association claim | none | future user/protocol layer |

The Registry may model support for a target concept, but a concrete user target is never stored as a public Registry threshold. Critical/alert values require the separate Critical Result / Clinical Escalation Governance dependency.

## 16. Six-System Relation Matrix

| Candidate | Biological Relationship | Product Grouping | Confidence / Source Plan | Non-Authorization |
|---|---|---|---|---|
| ApoB | T03.02, T03.03 | cardiometabolic | reviewed lipid/atherosclerosis source | no system score, diagnosis, frequency, or action |
| Lp(a) | T03.02, T03.03 | cardiometabolic | reviewed Lp(a) source | same |
| HbA1c | T03.02; secondary T03.01 | metabolic | standardized glycemia sources | same |
| Creatinine | T03.02 | kidney/metabolic | assay plus kidney-context source | same |
| eGFR | T03.02 | kidney/metabolic | equation plus KDIGO source | same |
| Systolic BP | T03.03 | cardiovascular | measurement/guideline sources | same |
| Diastolic BP | T03.03 | cardiovascular | measurement/guideline sources | same |
| Height | T03.04 | anthropometry/capability context | protocol source; biological relation conservative | same |
| Body Weight | T03.01, T03.02, T03.04 | anthropometry | protocol source; multi-system relation reviewed | same |
| Heart Rate | T03.03; secondary T03.01 | cardiovascular/fitness context | modality/profile sources | same |
| Total Sleep Time | T03.05, T03.01, T03.06 | sleep/recovery | sleep construct and modality sources | same |
| BMI | T03.02, T03.04 | anthropometry/metabolic | formula and population sources | same |

Many-to-many biological relationships and product groupings are stored as distinct relation kinds. A primary display group, if later chosen, does not override biological mapping.

## 17. Agent Permission Matrix

| Candidate | Permitted Planning Use | Prohibited Use | Action Authorization |
|---|---|---|---|
| ApoB | definition, units, method and trend caveats | diagnosis, personal risk/target, treatment | separately_gated |
| Lp(a) | explain profiles and no fixed conversion | conversion, diagnosis, personal treatment | separately_gated |
| HbA1c | explain representations and limitations | automatic diagnosis or personal target | separately_gated |
| Creatinine | explain assay/unit/eGFR lineage | equate with kidney function or diagnose | separately_gated |
| eGFR | explain equation, inputs, scope | fabricate inputs, silently change equation, diagnose | separately_gated |
| Systolic BP | explain protocol and paired event | diagnose, universal target, automatic action | separately_gated |
| Diastolic BP | explain protocol and paired event | diagnose, fill missing pair, automatic action | separately_gated |
| Height | explain method/unit/BMI lineage | infer value or diagnose growth status | none |
| Body Weight | explain context/unit/BMI lineage | infer composition, stigmatize, prescribe | none |
| Heart Rate | explain modality/window/artifact | diagnose rhythm or dismiss symptoms | separately_gated |
| Total Sleep Time | explain window/source/uncertainty | diagnose, equate with sleep quality, merge methods | separately_gated |
| BMI | explain formula/context/limitations | diagnose, infer body fat, set target | none |

Across all candidates, the Agent may ask minimal missing-context questions and provide source-aware interpretation context. It may not perform unverified conversion, method-independent normalization, personal treatment, automatic action, or personal target generation without separate governance.

## 18. Open Issues and Production Gates

### 18.1 Production Gate Matrix

| Candidate | GREEN/YELLOW | Blockers | Recommended Subwave | Target Lifecycle | ID Ready? |
|---|---|---|---|---|---|
| ApoB | GREEN | initial assay/profile and China source confirmation | C | proposed | After profile manifest approval |
| Lp(a) | YELLOW | assay source depth and exact Pilot C manifest | C | proposed | After manifest approval |
| HbA1c | GREEN | conversion/rounding and China source confirmation | C | proposed | After profile manifest approval |
| Creatinine | GREEN | initial method order and traceability wording | A | proposed | After profile manifest approval |
| eGFR | YELLOW | exact equation-profile source and Pilot B manifest | B | proposed | After manifest approval |
| Systolic BP | GREEN | initial office/home scope and jurisdiction | B | proposed | After paired-event approval |
| Diastolic BP | GREEN | same paired-event governance | B | proposed | After paired-event approval |
| Height | GREEN | exact initial profile manifest | A | proposed | At authorized creation gate |
| Body Weight | GREEN | exact initial profile manifest | A | proposed | At authorized creation gate |
| Heart Rate | YELLOW | exact Pilot A manifest; China method source remains non-blocking | A | proposed | After manifest approval |
| Total Sleep Time | YELLOW | wearable source depth; PSG source is deferred and non-blocking | C | proposed | After manifest approval |
| BMI | GREEN | approved height/weight lineage | B | proposed | After input records are manifested |

Counts: `GREEN = 8`, `YELLOW = 4`, `RED = 0`. No candidate is marked `split_required_before_record`; the four former concept/profile decisions are Founder-approved, while record-specific source and manifest conditions remain. This approved plan does not authorize record production.

### 18.2 Cross-cutting unresolved items

- Select the exact source versions and source keys that enter each v0.1 proposed record.
- Apply the approved jurisdiction rule: international method/definition authority first, China contexts separately, and a second international threshold jurisdiction only when differences or user needs justify it.
- Apply the approved minimal-profile rule; deferred profiles must not inflate the first record.
- Complete China-specific code/standard mapping where the current plan says pending.
- Define a future Observation event link for paired BP without modifying Observation assets in this task.
- Keep critical-result workflow, service ownership, and response times outside Registry items.
- Resolve an accessible, exact-version, legally usable, content-reviewed AASM scoring authority before any PSG TST profile can advance; this does not block the clean TST concept or its three initial profiles.

## 19. Founder Decision Sheet

| # | Decision | Final Approved Direction | Founder Decision |
|---:|---|---|---|
| 1 | Lp(a) concept structure | One concept; mass and molar are two non-interconvertible measurement-property profiles; apo(a) isoform later | Approved 2026-08-22 |
| 2 | eGFR structure | One concept with equation-specific profiles; CKD-EPI 2021 creatinine, adults 18+, first | Approved 2026-08-22 |
| 3 | Heart Rate structure | One concept; v0.1 spot clinical and wearable PPG time-series estimate only | Approved 2026-08-22 |
| 4 | Total Sleep Time scope | One concept; report, diary, and wearable first; PSG and clinical actigraphy deferred | Approved 2026-08-22 |
| 5 | BP v0.1 profiles | Office and home upper-arm first; ambulatory deferred; cuffless excluded; SBP/DBP share future event reference | Approved 2026-08-22 |
| 6 | Height/BMI age scope | Measured construct shared; adult interpretation first; pediatric context and self-reported height deferred | Approved 2026-08-22 |
| 7 | Numeric ID timing | Option B: boundary approval, manifest approval, controlled allocation, then separately authorized proposed-record creation | Approved 2026-08-22 |
| 8 | Production order | Pilot A, then Pilot B, then Pilot C | Approved 2026-08-22 |
| 9 | Initial lifecycle | First machine-readable records may be `proposed` only; later lifecycle states require separate review | Approved 2026-08-22 |
| 10 | Threshold jurisdictions | Source jurisdictions remain separate; no global normal range; personalized targets stay in the user/protocol layer | Approved 2026-08-22 |
| 11 | First-record profile breadth | Include only near-term or architecture-validating profiles with clear sources; defer the rest | Approved 2026-08-22 |
| 12 | TST PSG source | Accessible, exact-version, legally usable, content-reviewed AASM authority required before PSG source verification | Approved 2026-08-22 |

## 20. Explicit Non-Authorizations

This document does not authorize:

- creation of Registry concept, profile, computation, mapping, relation, or claim records;
- allocation of any numeric Registry ID;
- transition to `source_verified`, `human_reviewed`, `active`, or published;
- First Wave production;
- database, API, loader, index, runtime, retrieval, or Observation storage;
- Service Panel, laboratory integration, sampling operations, or critical-result workflow;
- user-health data persistence, processing, sharing, or model-context use;
- personalized targets, diagnosis, treatment, or action recommendations;
- modification of the Schema, Candidate Ledger, Migration Ledger, Validator, governance closeouts, knowledge entries, UHIL, Observation, CI, or requirements files.

Core 53 and First Wave 12 remain unchanged. Numeric IDs assigned = 0. Active Registry records = 0. Published Registry records = 0.

## 21. Recommended Next Step

Founder + ChatGPT should next review the separate Pilot A proposed-record authoring manifest for Height, Body Weight, Creatinine, and Heart Rate. Only after that manifest is approved may a new task prepare a controlled numeric-ID allocation manifest and request proposed-record creation authorization. This document does not itself authorize either step.
