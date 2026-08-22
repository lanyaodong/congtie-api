# Registry Seed 001 Founder Review Packet v0.1

Version: v0.1
Status: Draft / Founder Review Pending
Prepared: 2026-08-21
Source baseline: `registry_seed_001_asset_reconciliation_and_seed_definition.v0.1.md`
Source SHA-256: `4eac755441d96bd3113ceda302f049ddfa6d405eaa96989a7a59744ac80930cc`

This packet prepares Founder decisions. It does not approve C22, freeze a Registry ID, create an active Registry item, or authorize production implementation.

## 1. Executive Summary

C22 is directionally sound: Knowledge Entry, Registry Item, User Observation, and Service Panel remain separate; IDs do not encode a body system; system mappings are many-to-many; and reference intervals, decision limits, risk thresholds, alert values, and personal targets remain distinct.

Four issues remain before record production:

1. The legacy directory has 107 exact unique text labels, not 107 deduplicated measurement concepts.
2. Of 48 current candidates, 21 need revision and 6 should move out of Core Seed.
3. Nine high-value concepts should be added, producing a recommended 51 concepts.
4. Numeric IDs should wait until split/merge review, semantic deduplication, and schema approval.

AI review recommends retaining the architecture, revising the Core Seed to 51, and freezing only the `BM` / `ME` / `SC` / `QS` namespaces. Every Founder Decision in this packet remains `Pending`.

```text
legacy != low value
new != automatically canonical
candidate != active record
proposed ID != permanent ID
Registry item != Knowledge Entry
Registry item != User Observation
Registry item != Service Panel
```

## 2. Asset Migration Review

### 2.1 Reconciliation decisions

| Asset / Family | Current C22 Decision | AI Review Recommendation | Founder Decision |
| --- | --- | --- | --- |
| Registry MVP Spec | `retain_as_governance` | Retain as conceptual authority. | Pending |
| Evidence Contract | `retain_as_governance` | Retain; evidence binds to claim and intended use. | Pending |
| B2-A knowledge entries | `retain_as_governance` | Retain as terminology/boundary sources; do not convert prose mechanically. | Pending |
| 12-item biomarker JSON | `partially_migrate` | Retain labels/aliases after type, method, unit, and source review. | Pending |
| 23-item Xiaoge registry | `partially_migrate` | Treat old codes as aliases, not Registry IDs. | Pending |
| Approx. 120-item legacy directory | `reference_only` | Change to concept-level `partially_migrate`, then supersede old representations. | Pending |
| Six-System Minimum Set | `reference_only` | Migrate candidate discovery and historical grouping only; reject worst-marker semantics. | Pending |
| System map v0.1 | `supersede` | Preserve history; do not migrate repeated placeholders. | Pending |
| System map v0.2 | `partially_migrate` | Split grouped rows and review each relation. | Pending |
| v0.2 acceptance/context trail | `reference_only` | Retain migration rationale and unresolved ownership. | Pending |
| v0.2 validator/tests | `keep_prototype` | Keep for old-format audit only. | Pending |
| System Registry | `partially_migrate` | Reconcile product IDs with T03; reject state scoring. | Pending |
| Observation examples/model/OpenAPI | mixed | Retain value/time/source ideas; defer enum/runtime reconciliation. | Pending |
| Freshness/accuracy assets | `partially_migrate` | Reuse vocabulary, not fixed windows or evidence-grade shortcuts. | Pending |
| System-state/DMIE assets | `reference_only` | Keep separate; Registry membership must not activate scoring or action. | Pending |
| Unknown observation DDL | `needs_founder_review` | Locate before any persistence migration. | Pending |

### 2.2 Migration rule

```text
legacy asset
-> semantic inventory
-> extract unique concepts
-> retain useful metadata
-> normalize aliases
-> split compound rows
-> deduplicate
-> migrate canonical meaning
-> Founder review
-> supersede old representation
```

No asset is deleted or rewritten by this packet.

## 3. Legacy Unique Concepts Missing From Core Seed

The legacy directory contains 138 label occurrences, 107 exact unique text labels, and 23 exact duplicate label names. After alias, repeated-system, procedure, compound-row, and representation normalization, the estimated semantic count is approximately 85-95. This estimate is not a canonical count.

| Legacy Concept / Family | Core Coverage | AI Recommendation | Reason / Required Treatment |
| --- | --- | --- | --- |
| Hematocrit | Missing | Add Core | Basic CBC foundation. |
| Red Blood Cell Count | Missing | Add Core | Basic CBC foundation. |
| BUN / urea | Missing | Add Core, revise name | Common renal/chemistry result; identity and units vary. |
| ALP | Missing | Add Core | Common liver/bone-related analyte. |
| Bilirubin | Missing | Add total bilirubin | Common liver-related panel item. |
| Sodium | Missing from C22 and legacy | Add Core | High-frequency chemistry/report ingestion. |
| Potassium | Missing from C22 and legacy | Add Core | High-frequency chemistry/report ingestion. |
| Non-HDL cholesterol | Missing | Add Core as SC | Stable vendor-neutral derived lipid measure. |
| Time in Bed | Missing | Add Core, namespace review | Needed for sleep-efficiency context. |
| Blood Lactate | Missing | Extended | Performance/acute context. |
| Creatine Kinase | Missing | Extended | Exercise confounding and context sensitivity. |
| Basal Metabolic Rate | Missing | Extended, split | Measured and estimated constructs differ. |
| HOMA-IR | Missing | Extended | Equation/input/intended-use dependent. |
| C-Peptide | Missing | Extended | Lower first-wave priority. |
| Triglyceride/HDL Ratio | Missing | Extended | Derived use needs evidence review. |
| ApoA1 | Missing | Extended | Useful but lower priority than ApoB. |
| Uric Acid | Missing | Extended | Common but not essential to first wave. |
| Leptin / Adiponectin | Missing | Extended, separate records | Specialized, method-sensitive analytes. |
| Visceral Fat | Missing | Extended | Imaging/device method required. |
| Fibrinogen / Homocysteine | Missing | Extended, separate records | Intended use needs review. |
| NT-proBNP / hs-troponin | Missing | Extended, separate records | Clinically sensitive and assay-specific. |
| LDL Particle Number / Small Dense LDL | Missing | Extended, separate records | Platform/definition varies. |
| Carotid IMT | Missing | Extended | Imaging procedure and interpretation required. |
| CAC Score | Missing | Extended | Imaging-derived and clinically sensitive. |
| Pulse Wave Velocity | Missing | Extended | Protocol/device required. |
| Lean Body Mass / Skeletal Muscle Mass | Missing | Extended, separate records | Related but not aliases; method required. |
| Bone Mineral Density | Missing | Extended | Site/modality/result type required. |
| DEXA Body Composition | Missing | Representation | Procedure/platform, not one universal result. |
| Chair Stand Test | Missing | Extended | Named protocol/result required. |
| Sleep Quality | Missing | Extended, split type | Could be self-report, scale, or proprietary score. |
| Deep Sleep Time / REM Sleep | Missing | Extended, separate records | PSG classification and device estimate differ. |
| Reaction Time | Missing | Extended | Task/procedure required. |
| Cognitive Score | Missing | Extended | Instrument-specific, not one generic score. |
| Cortisol morning/evening | Missing | Extended, one analyte plus context | Time and specimen must be explicit. |
| BDNF | Missing | Research only | Method/specimen/utility unstable. |
| Neutrophils / Lymphocytes / Monocytes | Missing | Extended, separate records | Absolute/relative value type required. |
| NLR Ratio | Missing | Extended | Derived index with context-sensitive evidence. |
| IL-6 / TNF-alpha | Missing | Research/Extended | Specialized method/use. |
| Testosterone / Free Testosterone | Missing | Extended, separate records | Total, direct-free, and calculated-free differ. |
| SHBG / Estradiol / DHEA-S | Missing | Extended, separate records | Endocrine/reproductive context required. |
| Free T3 / IGF-1 / Prolactin | Missing | Extended, separate records | Lower first-wave priority. |
| Vitamin B12 / Folate | Missing | Extended, separate records | Specimen/method required. |
| Magnesium / Zinc | Missing | Extended, separate records | Preanalytical/specimen constraints. |
| Omega-3 Index / Omega-6:3 Ratio | Missing | Extended, separate records | Method and input definitions matter. |
| Biological / Epigenetic / Glycan Age | Missing | Research only, separate model records | Model/version cannot be omitted. |
| Telomere Length / AGE family | Missing | Research only | Tissue/method/construct limitations. |
| Carotid Ultrasound | Missing | Representation | Procedure producing multiple measures. |
| DEXA Bone Density | Missing | Representation | Procedure plus site-specific results. |
| VO2max Lab Test | Partial | Representation | Procedure differs from capability/result/estimate. |

Exact duplicate labels include ApoA1, ApoB, Body Fat Percentage, Creatinine, DEXA Body Composition, Fasting Glucose, Ferritin, Grip Strength, HbA1c, HDL, HRV, hsCRP, Lp(a), Reaction Time, Resting Heart Rate, Sleep Duration, Sleep Efficiency, Sleep Quality, Triglycerides, Vitamin D, VO2max, Waist Circumference, and White Blood Cell Count.

Compound v0.2 rows include glucose/HbA1c, fasting insulin/HOMA-IR/CGM, ApoB/LDL-C, hsCRP/ESR, CBC/WBC, B12/folate, liver/kidney, resting HR/HRV, stress/mood, body composition/lean mass, DXA/bone density, symptoms/safety, weight/BMI, and gait speed/mobility. Each requires semantic splitting.

## 4. Core Seed 48 - Founder Decision Table

`GREEN` = keep. `YELLOW` = keep but revise. `RED` = move to Extended or another mapping layer, not delete. All IDs below are proposed review coordinates and are not active.

| Current Candidate | Proposed ID | Current Type | Recommendation | Class | Reason | Required Change | Legacy Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total cholesterol / 总胆固醇 | `BM-000001` proposed | laboratory biomarker | Keep | GREEN | Stable, high-frequency analyte. | Verify specimen/unit/method. | LEGACY120, MAP2 |
| LDL-C / 低密度脂蛋白胆固醇 | `BM-000002` proposed | laboratory biomarker | Keep/revise | YELLOW | Direct and calculated results may differ. | Model method/equation breakpoint. | LEGACY120, MAP2 |
| HDL-C / 高密度脂蛋白胆固醇 | `BM-000003` proposed | laboratory biomarker | Keep | GREEN | Stable, high-frequency analyte. | Verify method metadata. | BR23, LEGACY120, MIN6, MAP2 |
| Triglycerides / 甘油三酯 | `BM-000004` proposed | laboratory biomarker | Keep | GREEN | Stable analyte. | Record fasting context where relevant. | BR23, LEGACY120, MIN6, MAP2 |
| ApoB / 载脂蛋白B | `BM-000005` proposed | laboratory biomarker | Keep | GREEN | Stable, high-value analyte. | Separate intended-use claims. | BR23, BS12, LEGACY120, MIN6, MAP2 |
| Lp(a) / 脂蛋白(a) | `BM-000006` proposed | laboratory biomarker | Keep/revise | YELLOW | Mass/molar units are not generically convertible. | Require unit/method; prohibit unvalidated conversion. | BR23, LEGACY120, MIN6, MAP2 |
| Fasting plasma glucose / 空腹血糖 | `BM-000007` proposed | laboratory biomarker | Keep/revise | YELLOW | Fasting and specimen/source matter. | Tighten identity and preanalytical context. | BR23, BS12, LEGACY120, MIN6, MAP2 |
| HbA1c / 糖化血红蛋白 | `BM-000008` proposed | laboratory biomarker | Keep | GREEN | Stable common measure. | Method/standardization metadata. | BR23, BS12, LEGACY120, MIN6, MAP2 |
| Fasting insulin / 空腹胰岛素 | `BM-000009` proposed | laboratory biomarker | Keep/revise | YELLOW | Assay and fasting context matter. | Require method/fasting context. | LEGACY120, MIN6, MAP2 |
| Creatinine / 肌酐 | `BM-000010` proposed | laboratory biomarker | Keep | GREEN | High-frequency analyte. | Do not force one system owner. | LEGACY120, MAP2 |
| ALT / 丙氨酸氨基转移酶 | `BM-000011` proposed | laboratory biomarker | Keep | GREEN | Stable common analyte. | Verify source/unit. | LEGACY120, MAP2 |
| AST / 天门冬氨酸氨基转移酶 | `BM-000012` proposed | laboratory biomarker | Keep | GREEN | Stable multi-tissue analyte. | Preserve limitations/multi-system relations. | LEGACY120, MAP2 |
| GGT / γ-谷氨酰转移酶 | `BM-000013` proposed | laboratory biomarker | Keep | GREEN | Stable common analyte. | Verify method/unit. | LEGACY120, MAP2 |
| Albumin / 白蛋白 | `BM-000014` proposed | laboratory biomarker | Keep | GREEN | Stable common analyte. | Avoid single nutrition interpretation. | LEGACY120, MAP2 |
| Hemoglobin / 血红蛋白 | `BM-000015` proposed | laboratory biomarker | Keep | GREEN | Basic CBC foundation. | Preserve population/context intervals. | LEGACY120, MIN6 |
| WBC count / 白细胞计数 | `BM-000016` proposed | laboratory biomarker | Keep | GREEN | Basic CBC foundation. | Distinguish count from differential. | BR23, LEGACY120, MIN6, MAP2 |
| Platelet count / 血小板计数 | `BM-000017` proposed | laboratory biomarker | Keep | GREEN | Basic CBC foundation. | Verify exact source/provenance. | MAP2/CBC family |
| hsCRP / 高敏C反应蛋白 | `BM-000018` proposed | laboratory biomarker | Keep | GREEN | Common inflammation-related measure. | Keep acute/intended-use limits. | BR23, BS12, LEGACY120, MIN6, MAP2 |
| TSH / 促甲状腺激素 | `BM-000019` proposed | laboratory biomarker | Keep | GREEN | High-frequency thyroid foundation. | Method/context metadata. | LEGACY120, MAP2 |
| Free T4 / 游离甲状腺素 | `BM-000020` proposed | laboratory biomarker | Keep | GREEN | Common thyroid foundation. | Method/interval provenance. | LEGACY120, MAP2 |
| Ferritin / 铁蛋白 | `BM-000021` proposed | laboratory biomarker | Keep/revise | YELLOW | Multiple intended uses/confounders. | Narrow use records and limits. | LEGACY120, MIN6, MAP2 |
| 25-hydroxyvitamin D / 25-羟维生素D | `BM-000022` proposed | laboratory biomarker | Keep/revise | YELLOW | Total/components and assay comparability matter. | Specify construct/method. | BR23, LEGACY120, MIN6, MAP2 |
| Systolic BP / 收缩压 | `ME-000001` proposed | physiological measurement | Keep | GREEN | Stable, high-frequency construct. | Preserve protocol/posture/device. | BR23, BS12, LEGACY120, MIN6, MAP2 |
| Diastolic BP / 舒张压 | `ME-000002` proposed | physiological measurement | Keep | GREEN | Stable, high-frequency construct. | Preserve protocol/posture/device. | BR23, BS12, LEGACY120, MIN6, MAP2 |
| Heart rate / 心率 | `ME-000003` proposed | physiological measurement | Keep/revise | YELLOW | Resting/sleeping/activity are contexts. | Base concept plus context/window. | BR23, BS12, LEGACY120, MAP2 |
| HRV / 心率变异性 | `ME-000004` proposed | physiological measurement or device estimate | Keep/revise | YELLOW | RMSSD/SDNN/window/artifacts/source differ. | Decide metric records vs profiles. | BR23, BS12, LEGACY120, MIN6, MAP2, B2A |
| Body weight / 体重 | `ME-000005` proposed | physiological measurement | Keep | GREEN | Stable, high-frequency measure. | Preserve timing/scale context. | LEGACY120, MAP2 |
| Waist circumference / 腰围 | `ME-000006` proposed | physiological measurement | Keep/revise | YELLOW | Landmark/protocol affect comparison. | Require protocol/landmark. | BR23, LEGACY120, MIN6, MAP2 |
| Body fat percentage / 体脂率 | `ME-000007` proposed | measurement or device estimate | Keep/revise | YELLOW | DXA/BIA/device are not equivalent. | Method profiles/cross-platform limits. | LEGACY120, MAP2 |
| Body temperature / 体温 | `ME-000008` proposed | physiological measurement | Keep | GREEN | Stable if site/method captured. | Require site/method. | New C22 candidate |
| Skin temperature signal / 皮肤温度信号 | `ME-000009` proposed | device signal | Keep/revise | YELLOW | Not core temperature; site/device dependent. | Separate signal from inference. | B2A, Registry Spec |
| Respiratory rate / 呼吸频率 | `ME-000010` proposed | measurement or device estimate | Keep/revise | YELLOW | Clinical count and estimate differ. | Add measurement nature/source profile. | LEGACY120, B2A |
| Oxygen saturation / 血氧饱和度 | `ME-000011` proposed | measurement or device estimate | Keep/revise | YELLOW | Method/conditions differ. | Specify method/device/context. | LEGACY120, B2A |
| Sleep duration / 睡眠时长 | `ME-000012` proposed | measurement or device estimate | Keep/revise | YELLOW | Total/main/24h representations differ. | Define total sleep time and source. | BR23, LEGACY120, MIN6, MAP2, B2A |
| Sleep latency / 入睡潜伏期 | `ME-000013` proposed | measurement or device estimate | Keep/revise | YELLOW | Event boundaries/source differ. | Define start/end and source nature. | B2A |
| WASO / 入睡后清醒时间 | `ME-000014` proposed | measurement or device estimate | Keep/revise | YELLOW | Sleep-onset boundary/source required. | Define events and algorithm. | B2A |
| Cardiorespiratory fitness / VO2max-related result | `ME-000015` proposed | functional/performance measurement | Keep/revise | YELLOW | Capability/procedure/result/estimate differ. | Split construct before production. | BR23, BS12, LEGACY120, MIN6, MAP2 |
| Grip strength / 握力 | `ME-000016` proposed | functional/performance measurement | Keep/revise | YELLOW | Side/device/position/attempts matter. | Define protocol/result metadata. | BR23, LEGACY120, MIN6, MAP2 |
| Gait speed / 步速 | `ME-000017` proposed | functional/performance measurement | Keep/revise | YELLOW | Distance/start/aids/instruction matter. | Define named protocol/profile. | BR23, LEGACY120, MAP2 |
| Balance test measure / 平衡测试测量 | `ME-000018` proposed | functional/performance measurement | Move out | RED | No single generic balance measure. | Add named tests later. | LEGACY120 |
| eGFR / 估算肾小球滤过率 | `SC-000001` proposed | derived score/index | Keep/revise | YELLOW | Equation/version/inputs are inseparable. | Require formula/input lineage. | LEGACY120, MAP2 |
| BMI / 体重指数 | `SC-000002` proposed | derived score/index | Keep | GREEN | Stable vendor-neutral index. | Preserve input provenance/limits. | MAP2 |
| Sleep efficiency / 睡眠效率 | `SC-000003` proposed | derived score/index | Keep/revise | YELLOW | Denominator/time boundaries vary. | Require formula/denominator/source. | LEGACY120, B2A |
| Sleep regularity index / 睡眠规律指数 | `SC-000004` proposed | derived score/index | Move out | RED | Multiple non-equivalent formulas. | Retain formula-specific candidates later. | B2A |
| Sleep score / 睡眠评分 | `SC-000005` proposed | derived score/index | Move out | RED | Usually proprietary/vendor-specific. | Device metric mapping layer. | BR23, MIN6, B2A |
| Recovery score / 恢复评分 | `SC-000006` proposed | derived score/index | Move out | RED | Proprietary composite. | Device metric mapping layer. | B2A |
| Readiness score / 准备度评分 | `SC-000007` proposed | derived score/index | Move out | RED | Proprietary composite. | Device metric mapping layer. | B2A |
| Device stress estimate / 设备压力估算 | `SC-000008` proposed | derived score/index | Move out | RED | Algorithmic proxy, not universal construct. | Device-specific proxy mapping. | B2A |

Coverage: current candidates 48/48; duplicate candidate rows 0.

## 5. Missing Candidates

| Proposed Concept | Proposed Type | Why Missing | Priority | Source / Rationale | Founder Decision |
| --- | --- | --- | --- | --- | --- |
| Hematocrit / 红细胞压积 | `BM` | Basic CBC item. | P0-A | LEGACY120 | Pending |
| Red blood cell count / 红细胞计数 | `BM` | Basic CBC item. | P0-A | LEGACY120 | Pending |
| Urea/BUN construct / 尿素或尿素氮 | `BM` | Common renal/chemistry report item. | P0-A | LEGACY120 | Pending |
| Alkaline phosphatase / 碱性磷酸酶 | `BM` | Common liver/bone-related item. | P0-A | LEGACY120 | Pending |
| Total bilirubin / 总胆红素 | `BM` | Common liver-related item. | P0-A | LEGACY120 | Pending |
| Sodium / 钠 | `BM` | High-frequency chemistry item omitted by old assets. | P0-A | Product-path audit | Pending |
| Potassium / 钾 | `BM` | High-frequency chemistry item omitted by old assets. | P0-A | Product-path audit | Pending |
| Non-HDL cholesterol / 非高密度脂蛋白胆固醇 | `SC` | Vendor-neutral derived lipid measure. | P0-A | Standard reporting rationale | Pending |
| Time in bed / 卧床时间 | namespace pending | Needed for sleep efficiency; not total sleep time. | P0-C | KN-T0501-0001 | Pending |

No numeric ID is assigned to these proposals.

## 6. Revised Core Seed Count

| Measure | Count |
| --- | ---: |
| Current candidates | 48 |
| GREEN | 21 |
| YELLOW | 21 |
| RED / move or postpone | 6 |
| MISSING / proposed additions | 9 |
| Recommended Core Seed | 51 |

The recommendation is `48 - 6 + 9 = 51`; it is not a Founder-approved quota.

## 7. BM Audit

| Result | Count | Main Issue |
| --- | ---: | --- |
| Current | 22 | Six need method/unit/use-context refinement. |
| GREEN | 16 | Stable high-frequency analytes. |
| YELLOW | 6 | LDL-C, Lp(a), fasting glucose/insulin, ferritin, 25-OH vitamin D. |
| RED | 0 | None. |
| Add | 7 | CBC, chemistry, liver-related foundations. |
| Recommended | 29 | Pending review. |

Key rules: no compound panel rows; direct/calculated LDL-C needs a method breakpoint; Lp(a) has no generic mass/molar conversion; fasting is context; ferritin needs intended-use separation; urea/BUN needs naming/unit governance; no analyte receives a universal range or evidence grade.

## 8. ME Audit

| Result | Count | Main Issue |
| --- | ---: | --- |
| Current | 18 | Thirteen need construct/protocol/source refinement. |
| GREEN | 4 | Systolic BP, diastolic BP, body weight, body temperature. |
| YELLOW | 13 | Context, method, source nature, or procedure unresolved. |
| RED | 1 | Generic balance-test row. |
| Add | 1 | Time in bed, namespace pending. |
| Recommended family count | 18 | Seventeen retained plus one addition if classified ME. |

Physiological measurement, functional measurement, device signal, and device estimate remain distinct information types even if they later share the `ME` namespace.

## 9. SC Audit

| Result | Count | Main Issue |
| --- | ---: | --- |
| Current | 8 | Five are unstable/proprietary generic score families. |
| GREEN | 1 | BMI. |
| YELLOW | 2 | eGFR and sleep efficiency. |
| RED | 5 | Sleep regularity, sleep, recovery, readiness, stress estimates. |
| Add | 1 | Non-HDL cholesterol. |
| Recommended | 4 | eGFR, BMI, sleep efficiency, non-HDL-C. |

| SC Candidate | Vendor Neutral? | Core Recommendation | Future Placement |
| --- | --- | --- | --- |
| eGFR | Yes, equation-specific | Keep/revise | Formula/version/input lineage. |
| BMI | Yes | Keep | Input provenance and limits. |
| Sleep efficiency | Yes, denominator-specific | Keep/revise | Formula/source profile. |
| Sleep regularity index | Not as one generic formula | Move | Extended formula-specific concepts. |
| Sleep score | Usually no | Move | Device metric mapping. |
| Recovery score | Usually no | Move | Device metric mapping. |
| Readiness score | Usually no | Move | Device metric mapping. |
| Device stress estimate | Usually no | Move | Device proxy mapping. |

## 10. Wearable / Sleep Concept Audit

| Concept Family | Recommendation |
| --- | --- |
| Heart rate / resting / sleeping HR | One base construct plus context/window profiles by default. |
| HRV / nocturnal HRV | Named metric, window, artifacts, source, and algorithm; nocturnal is usually context. |
| Body/core vs skin temperature | Separate concepts. |
| Respiratory rate / SpO2 | Base construct plus measured/estimated source profile. |
| Sleep duration | Define total sleep time; preserve main-sleep/24h/source representations. |
| Sleep opportunity | Separate contextual interval. |
| Time in bed | Add separate interval concept. |
| Sleep latency / WASO | Keep after event/source definitions. |
| Awakening count | Extended. |
| Bedtime / wake time / midpoint | Coordinate with User Health Event / Timeline. |
| Sleep regularity | Extended until formula selected. |
| Sleep-stage estimate | Extended; never equivalent to PSG classification. |
| Device composite scores | Device mapping layer. |

Sleeping HR and nocturnal HRV do not automatically receive separate IDs. Skin temperature is not an alias for body temperature. Device metric name, device, firmware, algorithm version, and measured/estimated/inferred nature remain in provenance.

## 11. Fitness Concept Audit

```text
capability concept != procedure != result != device estimate
```

| Family | Recommendation |
| --- | --- |
| Cardiorespiratory fitness / VO2max | Keep a direct result construct; separate capability, test procedure, and device estimate. |
| Grip strength | Keep with side, device, position, attempts, and protocol. |
| Gait speed | Keep with distance, start, aid, and pace protocol. |
| Balance | Move generic row; add named tests later. |
| Body composition | Keep body-fat percentage with method profiles; lean mass and DXA results remain Extended. |

No fitness item authorizes a threshold, score, diagnosis, training target, or personalized action.

## 12. Namespace and ID Freeze Decision

```text
BM = biomarker / laboratory or molecular biomarker
ME = physiological or functional measurement
SC = derived score / index
QS = validated questionnaire / scale
```

An estimate does not automatically enter `SC`. An estimate of the same construct may remain in its concept family if units and semantics are compatible and `measurement_nature` identifies it as estimated. A proprietary composite belongs in `SC` or a device mapping layer. This packet adds no namespace.

| Option | Decision | Advantage | Risk | Founder Decision |
| --- | --- | --- | --- | --- |
| A | Freeze numeric IDs now | Immediate references. | Split/merge and dedup may force renumbering. | Pending |
| B | Freeze namespace only | Allows schema/dedup before final numbering. | Planning uses candidate labels temporarily. | Pending |
| C | Temporary `CAND-*` IDs | Clear candidate/active separation. | Adds a conversion/mapping lifecycle. | Pending |

AI recommendation: **Option B**. Freeze namespaces only; assign numbers after scope, schema, semantic deduplication, and record boundaries are approved. C22 numbers remain review coordinates.

## 13. Required / Conditional / Optional Field Review

| Field / Group | C22 Tier | AI Recommendation |
| --- | --- | --- |
| Proposed/stable ID | Required | Required; final number only during approved record creation. |
| Canonical zh/en names | Required | Keep Required. |
| Aliases | Required | Keep Required; empty list allowed. |
| Information type | Required | Keep Required. |
| Measurement nature | Not explicit | Add Required: measured/estimated/derived/reported/classified. |
| Construct definition | Not explicit | Add Required: capability/procedure/result/score/context. |
| Value type | Required | Keep Required. |
| Canonical unit or N/A | Required | Keep Required. |
| Accepted units/conversion | Conditional | Keep Conditional; verification required. |
| Specimen | Broadly Required | Conditional by type; Required for lab items. |
| Source/modality | Required | Keep Required. |
| Method/platform requirement status | Required | Keep Required. |
| Method/platform detail | Required broadly | Conditional at proposed stage. |
| Intended use / use context | Required | Required before active; unresolved allowed while proposed. |
| Definition source | Within sources | Add Required. |
| Evidence level/scope | Broadly Required | Conditional per use claim; required for active claims. |
| Interpretation limitation | Required | Required before active. |
| Safety boundary | Required | Required before active when applicable. |
| Agent allowed/disallowed use | Required | Required before active. |
| Six-system mapping | Required | Conditional while proposed; reviewed before product use. |
| Mapping rationale/source/confidence | Required group | Conditional per relation. |
| LOINC / UCUM | Conditional | Keep Conditional. |
| Reference/threshold model | Conditional | Keep Conditional. |
| Method comparability status | Conditional | Add Required status; details Conditional. |
| Biological variation / RCV | Optional | Keep Optional. |
| China interval enrichment | Optional | Required only for a claim that needs it. |

## 14. Migration Metadata Review

Migration work should not turn the permanent Registry schema into a legacy-specific worksheet.

| Field | Recommended Placement | Tier |
| --- | --- | --- |
| `source_asset` | Record-creation provenance / migration ledger | Required for migrated Seed records; general provenance remains permanent. |
| `migration_status` | Migration ledger | Required during Seed migration. |
| `migration_note` | Migration ledger/audit log | Optional. |
| `supersedes` | Permanent lifecycle relation | Conditional. |
| `superseded_by` | Permanent lifecycle relation | Conditional. |
| `duplicate_of` | Permanent identity relation | Conditional. |

The machine-readable Registry should preserve durable provenance and lifecycle relations. Project-only extraction status and working notes can live in a separate migration ledger.

## 15. Reference / Threshold Review

Keep six concepts separate:

1. laboratory-reported reference interval;
2. population reference interval;
3. guideline/clinical decision limit;
4. risk-associated threshold;
5. critical/alert value;
6. personalized target.

AI recommendation: the public Registry may define whether an item supports a target concept and what method/unit/context prerequisites apply. A user's target value, rationale, effective dates, source, revision history, and action linkage belong in the User Health Information Library / Personalized Longevity Protocol layer, not in the public Registry definition.

Every observation must preserve the original laboratory interval and flag. A Registry interval must never overwrite it. `normal_range` must not collapse the six concepts.

## 16. Six-System Mapping Issues

Required governance before production:

1. Model system mappings as relation records, not one owner field.
2. Separate `biological_relationship` from `product_grouping`.
3. Make product primary grouping optional and explicitly non-medical.
4. Give each relation its own rationale, source, evidence scope, and confidence.
5. Do not derive diagnosis, system state, score, or action from mapping alone.

Examples needing review:

| Candidate | Legacy Conflict / Risk | Recommendation |
| --- | --- | --- |
| ApoB / LDL-C | Metabolic vs cardiopulmonary ownership | Multiple biological relations; optional product group. |
| VO2max | Energy vs cardiopulmonary | Capability/result relations without exclusive ownership. |
| Vitamin D | Repair/immune vs musculoskeletal | Multi-system relations with use-specific rationale. |
| HRV | Energy, cardiopulmonary, neurocognitive | No forced single primary biological system. |
| Creatinine | Kidney/organ not represented as one T03 owner | Keep system mapping pending rather than arbitrary. |
| Ferritin | Hematology, immune/inflammation, nutrition context | Intended-use-specific relationships. |

Current `P:` labels in C22 are provisional product grouping proposals only. Founder need not approve all item mappings now, but should approve this governance principle.

## 17. Extended Pool

Extended Pool status:

- 107 exact unique legacy text labels do not equal 107 semantic measurement concepts.
- Obvious aliases and repeated-system placements must be normalized.
- Compound rows must be split before candidate comparison.
- Procedures, observations, derived indices, device metrics, and analytes must be separated.
- Brand/vendor metrics remain a mapping layer unless a reusable canonical construct is demonstrated.
- Imaging, advanced omics, aging clocks, genetics, microbiome, full questionnaires, disease-specific calculators, and experimental longevity scores remain deferred by default.

The Extended Pool does not require full source verification in this review step. It requires a deduplicated candidate ledger before promotion.

## 18. Production Readiness

**READY WITH CONDITIONS**

Conditions:

1. Founder approves final Core scope and GREEN/YELLOW/RED adjustments.
2. Founder approves namespace/ID policy.
3. Machine-readable schema distinguishes concept, procedure, result, estimate, and device metric mapping.
4. Field requirements become lifecycle-aware.
5. Migration ledger is separated from durable Registry identity/lifecycle fields.
6. Personalized target values are placed in the user/protocol layer.
7. Six-system relation governance is approved.
8. First production wave is limited to 8-12 records with source verification, standards mapping, AI review, and Founder review.

Meeting these conditions authorizes a proposal for schema and first-record production, not active status, runtime use, Service Panel use, or user-data storage.

## 19. Explicit Non-Authorizations

This packet creates:

- active Registry records: 0;
- frozen numeric IDs: 0;
- databases/APIs/runtime changes: 0;
- user-health storage changes: 0;
- Service Panels: 0;
- laboratory integrations: 0.

It does not authorize production storage, consent, clinical escalation, panel launch, lab/provider partnership, report ingestion, or automated action. No candidate ecosystem organization is represented as a confirmed partner.

## 20. Founder Decision Sheet

| # | Decision | Current C22 Position | AI Review Recommendation | Founder Decision |
| ---: | --- | --- | --- | --- |
| 1 | C22 architecture direction | Draft | Retain core object boundaries and governance. | Pending |
| 2 | Legacy directory migration | `reference_only` | Concept-level partial migration plus supersession. | Pending |
| 3 | Core Seed scope | 48 candidates | 51: 21 GREEN, 21 revised YELLOW, remove/postpone 6, add 9. | Pending |
| 4 | RED candidates | Included in Core | Move generic balance and five unstable/proprietary SC rows out of Core. | Pending |
| 5 | Missing candidates | Not in Core | Add seven BM foundations, non-HDL-C, and time in bed. | Pending |
| 6 | ID freeze | Proposed numbers shown | Option B: freeze namespaces only. | Pending |
| 7 | Field tiers | C22 broad tiers | Add measurement nature/construct; lifecycle-aware requirements. | Pending |
| 8 | Migration metadata | In Registry planning | Separate migration ledger from durable relations/provenance. | Pending |
| 9 | Personalized targets | One of six modeled concepts | Keep target capability metadata public; actual targets private/user-protocol. | Pending |
| 10 | Production entry gate | Not authorized | READY WITH CONDITIONS; first wave 8-12 only after decisions above. | Pending |

Recommended next step: Founder + ChatGPT review this packet and decide final Core scope, candidate classifications, missing candidates, ID policy, field tiers, and production readiness. Do not modify C22 or create Registry records automatically.
