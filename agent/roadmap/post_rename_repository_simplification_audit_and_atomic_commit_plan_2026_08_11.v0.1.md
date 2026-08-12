# Post-Rename Repository Simplification Audit and Atomic Commit Plan

Version: v0.1
Project: Congtie
Status: Draft
Owner: Congtie Agent Team
Audit Date: 2026-08-11
Repository: `/Users/lanyaodong/Documents/congtie-api`
Baseline HEAD: `71f3c2fde58f1655d5c3b86656b063b8784f76c8`

---

## 1. Executive Summary

本审计在仓库和 GitHub 项目完成 `xiaoge-api` 到 `congtie-api` 的名称迁移后执行。它只记录现状、保留策略、Founder Gate 和未来原子提交计划，不执行清理、移动、暂存、提交或推送。

基线确认：

```text
branch: main
HEAD: 71f3c2fde58f1655d5c3b86656b063b8784f76c8
origin: git@github.com:lanyaodong/congtie-api.git
staged: 0
tracked modified: 16
deleted: 1
renamed: 0
untracked: 1052
ignored status entries: 1535
status manifest SHA-256: cf4db8af74336c0c8554e10afdd9fd894f17bf71706c9635b4b17435f8ad47c2
```

Founder-approved knowledge entry remains the protected canonical asset:

```text
agent/longevity_knowledge_base/entries/knowledge/KN-T0101-0001.healthspan-definition.md
SHA-256: 5d5562e24109bea582de67fb52cb1aa76f8319ee35d5ff239c300762ff0f63c9
status: approved
runtime_enabled: false
retrieval_enabled: false
```

Highest-risk findings:

1. The working tree is mostly untracked work: only 26 paths are tracked in HEAD, while 1,052 status entries are untracked.
2. Tracked changes include API/runtime integration, tool contracts, state semantics, a database snapshot rewrite, and test behavior. They are not a rename-only change set.
3. `frontend/official-preview/` is a clean nested Git repository with no remote. A parent `git add` would risk recording an unconfigured embedded repository/gitlink.
4. `app/__init__.py` is deleted. It was empty, but its package-marker role still requires an explicit decision.
5. Root `.gitignore` is too small for the current Python/Node/Cloudflare worktree.
6. `.env` is correctly ignored and no obvious private-key/token signature was found in the filename/content-signature scan, but local deployment state and a public founder contact asset still require handling decisions.
7. Process-document volume is high. Immediate deletion is intentionally limited to 68 conservative candidates after external backup and reference checks.

This plan recommends 15 future atomic commits. No commit in the plan combines cleanup with API, database, clinical/safety, knowledge-content, or deployment changes.

---

## 2. Repository State

### 2.1 Git identity and operation state

```text
repository root: /Users/lanyaodong/Documents/congtie-api
branch: main
HEAD: 71f3c2fde58f1655d5c3b86656b063b8784f76c8
origin fetch/push: git@github.com:lanyaodong/congtie-api.git
worktrees: one
merge: none
rebase: none
cherry-pick: none
revert: none
bisect: none
sequencer: none
detached HEAD: false
```

The pre-audit manifest matched the post-rename manifest exactly. All existing changes predate this audit document.

### 2.2 Parent repository status inventory

The classification count below uses parent-repository audit entries: 26 tracked paths, 1,052 untracked entries, and 1,535 ignored entries. Homogeneous dependency/build trees are counted as status entries or directory groups rather than pretending every dependency file is a project asset.

| Classification | Parent audit entries | Basis |
|---|---:|---|
| KEEP_ACTIVE | 568 | Clean tracked assets, bounded current docs, tests, frontend source, roadmap and knowledge assets |
| ARCHIVE_REPO | 109 | 101 milestone/artifact entries plus 8 brand-migration records |
| CONSOLIDATE_THEN_ARCHIVE | 152 | 68 day closeouts, 64 historical M4/M5 files, 20 prompt/review-chain files |
| BACKUP_THEN_DELETE | 68 | 66 day plans, one completed scaffold prompt, one exact duplicate contract |
| IGNORE_GENERATED | 1560 | 1,534 ignored generated entries plus 26 untracked cache/package-output entries |
| LOCAL_PRIVATE | 1 | `.env` |
| FOUNDER_GATE | 150 | API/runtime/schema/spec/deployment/biomarker/nested-repo decisions |
| UNRESOLVED | 5 | Empty placeholder files with unclear intended ownership |
| **Total** | **2613** | 26 + 1052 + 1535 |

Nested `frontend/official-preview/` is represented by one parent entry above. Its own generated tree is audited separately and is not double-counted: `node_modules` 20,665 files, `dist` 71, `.vinext` 13, `.wrangler` 4, and `.next` 1.

---

## 3. Audit Method

The audit used read-only Git and filesystem inspection:

1. Verified root, branch, HEAD, origin, worktree count, operation state, and status manifest.
2. Recomputed the protected knowledge-entry SHA-256 before any write.
3. Read `AGENTS.md`, root `README.md`, `.gitignore`, current release plan/backlog, Batch 001 plan, knowledge-base README/template/schema/governance/validator, user-health documents, and active migration/runbook documents.
4. Read every tracked diff, including the deleted file from HEAD.
5. Enumerated every tracked, untracked, and ignored parent status entry.
6. Enumerated nested Git repositories and inspected nested HEAD/status/remote/hosting configuration without outputting resource values.
7. Grouped generated/cache/dependency files by exact directory.
8. Scanned filenames for environment, credential, key, certificate, token, database, and local-state indicators; scanned for common secret signatures while reporting paths only.
9. Hashed non-generated files to identify byte-identical duplicates.
10. Checked zero-length files, large files, binary assets, process-document naming families, and cross-references.

No build or test that writes to the working tree was run.

---

## 4. Retention Policy

The required labels are applied as follows:

| Label | Decision rule for this repository |
|---|---|
| KEEP_ACTIVE | Current source, tests, canonical governance, roadmap, runbook, knowledge assets, reproducibility inputs |
| ARCHIVE_REPO | Durable historical evidence or decision record that should remain in Git but outside default active context |
| CONSOLIDATE_THEN_ARCHIVE | Repetitive process chain with unique facts that must first be summarized and reference-checked |
| BACKUP_THEN_DELETE | One-time or exact duplicate content whose durable conclusions already have a canonical home |
| IGNORE_GENERATED | Dependencies, caches, build output, coverage, logs, local generated hosting state |
| LOCAL_PRIVATE | Local settings or confidential material that must not enter Git |
| FOUNDER_GATE | API, safety, clinical, DB, runtime identifiers, deployment, biomarker, nested-repo, or referenced compatibility decision |
| UNRESOLVED | Intent cannot be established reliably from content and references |

Conservative rule: because most work has never entered Git history, uncertain substantive documents stay active or gated. Age, length, `draft`, or a lower version number alone never justifies deletion.

---

## 5. Top-Level Inventory

| Path/group | Observed files/status | Classification | Audit result |
|---|---:|---|---|
| `.github/` | 1 tracked workflow + ignored OS file | KEEP_ACTIVE / IGNORE_GENERATED | CI workflow retained; `.DS_Store` ignored |
| `.gitignore` | 1 clean tracked | KEEP_ACTIVE, FOUNDER_GATE for update | Current rules are incomplete |
| `.env` | 1 ignored | LOCAL_PRIVATE | Do not read, print, back up into cleanup package, or commit |
| `.env.example` | 1 untracked | KEEP_ACTIVE | Contains variable names for active and legacy aliases; values were not reported |
| `.venv/` | 1,510 ignored status entries | IGNORE_GENERATED | Local Python environment |
| `.pnpm-store/` | 4 untracked entries | IGNORE_GENERATED | Local package-store metadata |
| `.pytest_cache/` | 7 self-ignored entries | IGNORE_GENERATED | Add explicit root ignore |
| `AGENTS.md` | 1 untracked | KEEP_ACTIVE | Current repo operating and Founder Gate policy |
| `Makefile` | 1 tracked modified | KEEP_ACTIVE | Functional M2 test-target addition; not rename-only |
| `README.md` | 1 tracked modified | KEEP_ACTIVE | Path rename plus public-brand text; malformed fences and deprecated display spelling need a separate correction |
| `requirements.txt` | 1 clean tracked | KEEP_ACTIVE | Python reproducibility input |
| `pytest.ini` | 1 untracked | KEEP_ACTIVE | Marker policy support |
| `agent/` | 811 untracked + 2 ignored OS files | Mixed | 437 conservative active, 109 archive, 152 consolidate, 68 backup/delete, 44 gated, 1 unresolved |
| `app/` | 1 modified, 1 deleted, 64 untracked, 4 ignored | FOUNDER_GATE / UNRESOLVED | Current source is valuable but initial API/runtime commit requires gates |
| `artifacts/` | 3 untracked | FOUNDER_GATE | XSB001 copies differ from `agent/artifacts/`; preserve until provenance decision |
| `dist/` | 22 untracked + 2 ignored OS files | IGNORE_GENERATED | Generated external-trial package; verify reproducibility before cleanup |
| `frontend/` | 70 parent-untracked + 1 ignored OS file | KEEP_ACTIVE / FOUNDER_GATE | `local-app` active; `official-preview` nested-repo gate |
| `schemas/` | 4 untracked + 1 ignored OS file | FOUNDER_GATE | Runtime/tool contracts; exact duplicate exists under `agent/` |
| `scripts/` | 2 modified + 8 untracked | KEEP_ACTIVE / FOUNDER_GATE / UNRESOLVED | Active helpers; identifier changes gated; one empty placeholder |
| `spec/` | 9 modified + 24 untracked + 6 clean examples + 1 ignored OS file | FOUNDER_GATE | Contract, clinical/safety and DB implications; one case-only path mismatch |
| `tests/` | 2 modified + 39 untracked + ignored OS files | KEEP_ACTIVE | Current M1/M2/M3, boundary, fixture and compatibility coverage |

Binary/large observations:

- `frontend/official-preview/public/og.png` is 1,979,005 bytes; its `dist/client/og.png` copy is generated.
- `frontend/official-preview/public/founder-wechat-qr.jpeg` is 115,716 bytes; publishing it requires explicit consent.
- QA screenshots under `agent/artifacts/` range above 100 KB and should be privacy-reviewed before archival commit.

---

## 6. Canonical Active Assets

### 6.1 Repository and roadmap

```text
AGENTS.md
README.md
.github/workflows/ci.yml
.gitignore
Makefile
requirements.txt
.env.example
pytest.ini
agent/roadmap/v0_release_plan_2026_09.md
agent/roadmap/v0_release_task_backlog_2026_09.md
agent/roadmap/longevity_knowledge_batch_001_plan.v0.1.md
```

`AGENTS.md` is the current operating-policy source. The release plan and backlog are the current schedule/work-decomposition sources. Daily plans do not supersede them.

### 6.2 Longevity Information Library

```text
agent/longevity_knowledge_base/README.md
agent/longevity_knowledge_base/templates/longevity_knowledge_item_template.v0.1.md
agent/longevity_knowledge_item_schema.v0.1.md
agent/longevity_knowledge_base/schemas/evidence_source_type_enum.v0.1.md
agent/longevity_knowledge_base/schemas/evidence_source_type_alignment_notes.v0.1.md
agent/longevity_knowledge_base/scripts/validate_longevity_knowledge_item.py
agent/knowledge_seed_v0/longevity_information_library_architecture.v0.1.md
agent/knowledge_seed_v0/longevity_information_library_architecture_patch_for_taxonomy.v0.1.md
agent/knowledge_seed_v0/longevity_topic_taxonomy.v0.1.md
agent/longevity_knowledge_base/entries/knowledge/KN-T0101-0001.healthspan-definition.md
```

The approved entry must be committed alone after its framework dependencies. It remains disabled for runtime and retrieval.

### 6.3 User health information

```text
agent/user_health_information_library_mvp_spec.v0.1.md
agent/user_health_context_schema.v0.1.md
```

These are complementary, not byte/content duplicates: one is the MVP product boundary, the other the conceptual context schema. Neither authorizes persistence or runtime integration.

### 6.4 Active internal-alpha assets

```text
agent/knowledge_seed/minimum_longevity_knowledge_seed.v0.1.md
agent/knowledge_seed/knowledge_seed_index.v0.1.json
agent/internal_alpha_scenarios_2026_08_XX/
agent/m3_internal_alpha_trial_handoff_package_2026_08_XX/
agent/m3_internal_alpha_local_runbook_2026_08_XX.v0.1.md
frontend/local-app/
tests/
```

The small `agent/knowledge_seed/` remains referenced by M3 tests and runbooks. It is not superseded merely because `agent/knowledge_seed_v0/` exists.

### 6.5 Runbooks requiring bounded refresh

```text
agent/agent_release_runbook.v0.1.md
agent/demo_runbook.v0.1.md
agent/m1_api_alpha_external_smoke_runbook_2026_08_XX.v0.1.md
agent/m3_internal_alpha_local_runbook_2026_08_XX.v0.1.md
```

They remain active because they carry operating procedures, but legacy branding, environment aliases, and stale path statements must be reviewed in their own commit.

---

## 7. Process Document Review

### 7.1 Daily plans

Sixty-six one-day plans are proposed as BACKUP_THEN_DELETE only after an external backup, reference report, and Founder approval. Their durable planning role is now served by the release plan/backlog; some closeouts still cite them, so reference reconciliation is mandatory.

Exact paths are listed in Appendix A.

### 7.2 Daily closeouts

Sixty-eight daily closeouts retain execution facts. They should first be consolidated into milestone-level closeouts, then moved to archive. Exact paths are listed in Appendix B.

### 7.3 M4/M5 chains

- 64 dated M4/M5 approval/status/report/config files from 2026-05-14 through 2026-05-16 are CONSOLIDATE_THEN_ARCHIVE. Exact paths are in Appendix C.
- 23 M4 files marked `2026_08_XX` plus two operator-packet directories remain FOUNDER_GATE because they describe current deployment, host, TLS, service and rollback behavior. Exact paths are in Section 13 and the Founder table.

### 7.4 Prompt/review chains

Twenty biomarker/minimal-JSON execution prompt and Founder-review files are CONSOLIDATE_THEN_ARCHIVE. They contain safety decisions that must be preserved in a single reviewed closeout before originals leave active context. Exact paths are in Appendix D.

The following remain active:

```text
agent/codex_daily_execution_prompt_template_2026_06_10.v0.1.md
agent/prompt_engineering_guide.v0.1.md
```

The completed `agent/m1_backend_scaffold_prompt.v0.1.md` is a BACKUP_THEN_DELETE candidate because current source, AGENTS rules, M1 specs and tests carry the durable result.

### 7.5 Conservative remainder

The other 437 `agent/` status entries are KEEP_ACTIVE in this audit. This is deliberate: many contain unique safety decisions, runtime contracts, validator outcomes or current knowledge assets, and no Git history yet protects them. Future per-domain consolidation may reduce them, but a broad delete is not justified now.

---

## 8. Duplicate and Superseded Documents

| Group | Canonical source | Other copy/history | Recommendation | Reference status |
|---|---|---|---|---|
| A2A contract | `schemas/agent/a2a_contract.v0.1.json` | `agent/a2a_contract.v0.1.json` | Exact-byte duplicate; update two doc references, external backup, then delete duplicate | Runtime loader and validator use `schemas/agent`; demo/onboarding docs still mention `agent/` |
| Frontend deploy snapshot | `frontend/local-app/` | `agent/artifacts/m4_staging_deploy_dry_run_2026_08_XX/frontend_static_preview/` | Archive snapshot | 44 files identical; 5 runtime files differ and preserve deploy evidence |
| Official preview build | `frontend/official-preview/public/` and source | `frontend/official-preview/dist/` | Ignore generated `dist` | `og.png` and QR image are duplicated in build output |
| Knowledge entry location | Approved entry under `entries/knowledge/` | Empty top-level `knowledge/` with `.gitkeep` | FOUNDER_GATE | KB README says `entries/` is staging and `knowledge/` canonical, but actual approved path uses `entries/knowledge/` |
| Agent integration pack casing | Git index path `spec/Agent_Integration_Pack.v0.1.md` | Filesystem spelling `spec/agent_Integration_pack.v0.1.md` | FOUNDER_GATE; normalize through an explicit case-only rename | Case-insensitive macOS hides a Linux portability problem |
| Internal-alpha seed vs formal seed | `agent/knowledge_seed/` for M3 runtime fixtures; `agent/knowledge_seed_v0/` for formal seed | Both | Keep both until runtime migration | Tests and runbooks directly reference the smaller M3 seed |
| User health docs | MVP spec + conceptual schema | Two files | Keep both | Different responsibilities; cross-link later |
| Brand migration chain | Current `AGENTS.md`, current roadmap and this audit | Eight brand/alias documents | Archive history | Historical alias and identifier reasoning is not fully recoverable from current docs |

The root `README.md` is not currently a clean canonical public document: it contains malformed/unclosed fenced blocks and deprecated display-brand spelling. Correct it separately from the rename-path commit.

---

## 9. Archive Candidates

### 9.1 Milestone evidence

Exact directory:

```text
agent/artifacts/
```

Classification: ARCHIVE_REPO. It contains 101 untracked evidence entries plus ignored OS metadata. Preserve XSB artifacts as required by `AGENTS.md`; remove `.DS_Store` only through ignore/cleanup. Review screenshots for personal information before commit.

### 9.2 Brand and identifier migration history

```text
agent/agent:atie_brand_rename_execution_plan.v0.1.md
agent/brand_migration_to_congtie_2026_05_31.v0.1.md
agent/brand_rename_alias_compatibility_atie_2026_04_28.v0.1.md
agent/brand_rename_alias_verification_atie_2026_04_28.v0.1.md
agent/brand_rename_audit_atie_2026_04_28.v0.1.md
agent/brand_rename_closure_atie_2026_04_28.v0.1.md
agent/brand_rename_identifier_decision_atie_2026_04_28.v0.1.md
agent/brand_rename_text_replacement_atie_2026_04_28.v0.1.md
```

Classification: ARCHIVE_REPO. The unusual colon in the first filename is portable-risk metadata and should be normalized only during an approved archive move.

---

## 10. Backup-and-Delete Candidates

### 10.1 Candidate groups

| Candidate | Count | Replacement | References | Risk |
|---|---:|---|---|---|
| Daily plans in Appendix A | 66 | Current release plan/backlog plus retained milestone closeouts | Some daily closeouts and reviews cite day plans | Medium; reconcile links first |
| `agent/m1_backend_scaffold_prompt.v0.1.md` | 1 | `AGENTS.md`, current app source, M1 specs/tests/status | No current runtime reference found | Low/medium; preserve prompt constraints in M1 closeout |
| `agent/a2a_contract.v0.1.json` | 1 | `schemas/agent/a2a_contract.v0.1.json` | Two docs still point to old location | Low after reference update; files are byte-identical |

### 10.2 External backup procedure

Future approved execution should use this repository-external destination:

```text
/Users/lanyaodong/Documents/congtie-api_cleanup_backup_2026-08-11/
```

Required procedure:

1. Copy only Founder-approved deletion candidates while preserving relative paths.
2. Exclude `.env`, secrets, caches, dependencies and generated output.
3. Generate a SHA-256 manifest for copied files.
4. Verify source/backup count and every hash.
5. Record the manifest and Founder decision outside the repository.
6. Delete only after verification; never add the backup directory to Git.

This audit did not create that backup.

---

## 11. Generated and Ignored Content

### 11.1 Parent repository

```text
.venv/
.pnpm-store/
.pytest_cache/
**/__pycache__/
**/*.pyc
dist/
**/.DS_Store
```

Classification: IGNORE_GENERATED. Parent status reports 1,534 ignored generated entries and 26 untracked `.pnpm-store`/`dist` entries.

### 11.2 Nested official preview

```text
frontend/official-preview/node_modules/
frontend/official-preview/.vinext/
frontend/official-preview/.next/
frontend/official-preview/.wrangler/
frontend/official-preview/dist/
```

Classification: IGNORE_GENERATED inside whichever repository ownership option is approved. Logical disk use is dominated by `node_modules` (approximately 1.7 GB when followed). The nested `.gitignore` already covers these paths.

### 11.3 Generated package caution

`dist/first_external_trial_package/` is generated, but it includes trial artifacts and references. Before deletion, prove that `agent/build_first_external_trial_package.sh` reproduces it and decide whether a release artifact should live outside Git. Do not commit generated output merely because it contains useful copies.

---

## 12. Local and Sensitive Content

| Exact path | Classification | Risk/handling |
|---|---|---|
| `.env` | LOCAL_PRIVATE | Ignored; never output values or commit |
| `.env.example` | KEEP_ACTIVE with FOUNDER review | Contains variable names for active/legacy identifiers; keep placeholder-only |
| `agent/m4_staging_env_final_template_2026_05_15.env.example` | CONSOLIDATE_THEN_ARCHIVE | Historical staging template; verify placeholders before archive |
| `agent/m4_staging_manual_deploy_operator_packet_2026_08_XX/02_ENV_FILE_TEMPLATE.md` | FOUNDER_GATE | Current deployment template; secret-safe review required |
| `frontend/official-preview/.openai/hosting.json` | FOUNDER_GATE | Contains hosting resource identifiers/bindings; values not printed |
| `frontend/official-preview/.wrangler/` | IGNORE_GENERATED | Local Cloudflare state, including SQLite/WAL files |
| `frontend/official-preview/public/founder-wechat-qr.jpeg` | FOUNDER_GATE | Public contact/identity asset; require publication consent |

No common private-key, GitHub token, AWS access-key or OpenAI-style secret signature was found outside excluded dependency/build trees. This is not a substitute for a dedicated secret scanner before first push.

---

## 13. Nested Repository Gate

### 13.1 Current facts

```text
path: frontend/official-preview
has .git: true
branch: main
HEAD: 9dafa395e9e0366ee8e15f825a17268f6f95a73c
status: clean
commits: 2
remote: none
hosting config: .openai/hosting.json
hosting keys observed: project_id, d1, r2
parent status: ?? frontend/official-preview/
```

If the parent runs `git add -A`, Git is likely to warn about an embedded repository and stage a gitlink-like entry without `.gitmodules` or a usable remote. Another clone would not receive its contents reliably.

### 13.2 Options

| Option | Benefits | Costs/risks | Preconditions |
|---|---|---|---|
| A. Independent repository | Preserves two-commit history and hosting isolation; simplest immediate containment | Two release flows; parent must explicitly ignore/document it; currently no remote | Create/verify its GitHub remote; backup hosting metadata; update parent ignore/docs |
| B. Formal submodule | Parent pins exact preview commit; preserves independent history | Operational complexity; contributors must initialize/update; CI/hosting must support submodules | Publish nested remote first; add `.gitmodules`; document CI/deploy flow |
| C. Monorepo directory | Simplest single-repo contributor workflow; source commits atomically with API | Removing nested `.git` can lose independent history/hosting provenance; large generated trees must stay ignored | Export/bundle history, verify hosting source, remove nested Git only in an approved destructive task |

Recommendation: Option A as the lowest-risk immediate decision because it preserves history and hosting isolation. Re-evaluate Option C after the preview remote/history and hosting source are backed up and the product decides that one release cadence is desirable. Do not choose B unless pinning an independently released preview is a real requirement.

### 13.3 Current M4 deployment Founder Gate paths

```text
agent/m4_fastapi_systemd_service_draft_2026_08_XX.service
agent/m4_nginx_ecs_static_frontend_topology_2026_08_XX.v0.1.md
agent/m4_nginx_ecs_static_frontend_topology_status_2026_08_XX.v0.1.md
agent/m4_nginx_staging_congtie_draft_2026_08_XX.conf
agent/m4_nginx_staging_congtie_draft_after_founder_decisions_2026_08_XX.conf
agent/m4_staging_deploy_dry_run_report_2026_08_XX.v0.1.md
agent/m4_staging_deploy_dry_run_status_2026_08_XX.v0.1.md
agent/m4_staging_deploy_execution_checklist_2026_08_XX.v0.1.md
agent/m4_staging_deploy_execution_checklist_status_2026_08_XX.v0.1.md
agent/m4_staging_env_var_and_config_plan_2026_08_XX.v0.1.md
agent/m4_staging_founder_decisions_update_2026_08_XX.v0.1.md
agent/m4_staging_founder_operator_decision_closeout_2026_08_XX.v0.1.md
agent/m4_staging_founder_operator_decision_closeout_status_2026_08_XX.v0.1.md
agent/m4_staging_host_inputs_collection_2026_08_XX.v0.1.md
agent/m4_staging_host_inputs_collection_status_2026_08_XX.v0.1.md
agent/m4_staging_host_inputs_founder_response_closeout_2026_08_XX.v0.1.md
agent/m4_staging_host_inputs_founder_response_closeout_status_2026_08_XX.v0.1.md
agent/m4_staging_host_specific_preflight_packet_status_2026_08_XX.v0.1.md
agent/m4_staging_manual_deploy_operator_packet_status_2026_08_XX.v0.1.md
agent/m4_staging_prelaunch_checklist_2026_08_XX.v0.1.md
agent/m4_staging_prelaunch_checklist_draft_2026_08_XX.v0.1.md
agent/m4_staging_prelaunch_checklist_status_2026_08_XX.v0.1.md
agent/m4_staging_ssh_dns_fix_checklist_2026_08_XX.v0.1.md
agent/m4_staging_host_specific_preflight_packet_2026_08_XX/
agent/m4_staging_manual_deploy_operator_packet_2026_08_XX/
```

---

## 14. Tracked Modified Files

All rows below existed before this audit. Only the README path substitutions are confirmed rename work; the origin of the other diff hunks cannot be proven from Git because they were never committed separately.

| Path | Change summary | Rename-only? | Impact | Classification / future commit | Validation | Gate |
|---|---|---|---|---|---|---|
| `Makefile` | Adds `test-m2-frontend` and JS/Python checks | No | Test workflow | KEEP_ACTIVE / C07 | `make test-m2-frontend` | No, after source review |
| `README.md` | Public name edits and two repo-path edits | No; mixed | Docs/onboarding | KEEP_ACTIVE / C01 then correction | fenced-block check, path search | Brand compatibility review |
| `app/main.py` | Uses settings, operational middleware and API router; removes inline health route | No | API/runtime | FOUNDER_GATE / C03 | focused M1/API tests | Yes |
| `scripts/agent_playbook_v0_1.py` | Adds active/legacy base URL alias | No | Runtime identifier | FOUNDER_GATE / C06 | smoke script dry configuration | Yes |
| `scripts/agent_smoke_v0_1.py` | Adds alias helper and output label | No | Runtime identifier/test | FOUNDER_GATE / C06 | external smoke when server approved | Yes |
| `spec/Agent_Integration_Pack.v0.1.md` | Large write-oriented contract rewrite | No | Agent/API contract | FOUNDER_GATE / C04 | cross-contract review | Yes |
| `spec/agent_tools.v0.1.json` | Replaces tool surface and enums | No | Tool contract | FOUNDER_GATE / C04 | JSON parse + contract tests | Yes |
| `spec/api_behavior_spec.v0.1.md` | Replaces prior behavior rules; adds state/color, confidence and recommendation concepts | No | API/safety/clinical boundary | FOUNDER_GATE / C04 | contract/safety review | Yes |
| `spec/im_connector_min_spec.v0.1.md` | Large connector/identity/security rewrite | No | Integration/deployment | FOUNDER_GATE / C04 | connector contract review | Yes |
| `spec/openai_tools.v0.1.json` | Replaces OpenAI tool definitions | No | Tool contract | FOUNDER_GATE / C04 | JSON parse + contract tests | Yes |
| `spec/openapi.v0.1.yaml` | Replaces endpoints, auth, states and schemas | No | Top-level API contract | FOUNDER_GATE / C04 | OpenAPI validation + API tests | Yes |
| `spec/system_rules.v0.1.md` | Rewrites system state/biomarker/recommendation rules | No | Safety/clinical semantics | FOUNDER_GATE / C04 | safety and boundary suite | Yes |
| `spec/xiaoge_agent_protocol.v0.1.md` | Rewrites protocol and future capabilities | No | Agent/runtime contract | FOUNDER_GATE / C04 | contract/reference review | Yes |
| `spec/xiaoge_v0_schema_snapshot.sql` | Replaces observation/assessment tables with systems/state/strategy tables | No | Database/persistence | FOUNDER_GATE / C05 | isolated schema/DB tests | Yes |
| `tests/test_e2e_metabolic.py` | Adds external-server/DB/e2e markers and skip gate | No | Test execution only | KEEP_ACTIVE / C03 | marker selection + DB E2E when approved | No |
| `tests/test_smoke_health.py` | Adds aliases and external/DB skip gates | No | Test execution/identifier | KEEP_ACTIVE / C03 | focused smoke marker checks | Alias policy review |
| `app/__init__.py` | Deleted empty file | No | Package discovery/import | FOUNDER_GATE / isolated in C03 or restore | import, uvicorn, pytest collection | Yes |

`spec/api_behavior_spec.v0.1.md` and `spec/system_rules.v0.1.md` currently have pre-existing end-of-file whitespace findings. Do not hide those inside unrelated commits.

---

## 15. Deleted File Review

Target:

```text
app/__init__.py
```

Facts:

- The HEAD blob is empty (`e69de29...`).
- No business code is deleted.
- Python 3 namespace packages may allow imports without it, but packaging, discovery, older tools, static analyzers and deployment conventions can differ.
- New subpackages retain their own `__init__.py` files.
- Git history provides no separate explanatory commit for the deletion.

Recommendation: FOUNDER_GATE. Prefer restoring the empty package marker unless focused import, uvicorn, pytest collection and packaging checks establish an intentional namespace-package decision. If deletion is retained, commit it explicitly with that rationale; do not bundle it with cleanup.

---

## 16. `.gitignore` Gaps

### 16.1 Correctly covered now

```text
.env
.venv/
__pycache__/
*.pyc
.DS_Store
```

### 16.2 Recommended additions

```text
.pytest_cache/
.mypy_cache/
.ruff_cache/
.coverage
coverage/
htmlcov/
node_modules/
.pnpm-store/
.next/
.vinext/
.wrangler/
dist/
build/
out/
*.log
*.pid
*.sqlite
*.sqlite-shm
*.sqlite-wal
*.db
.idea/
.vscode/
*.swp
.env.*
!.env.example
!*.env.example
```

### 16.3 Risks and exceptions

- Do not add `dist/` until the external trial package is proven reproducible or moved to release storage.
- Broad DB patterns can hide deliberate test fixtures; scope them if database fixtures become canonical.
- Keep `.openai/hosting.json` governed rather than broadly ignoring `.openai/`.
- Keep `package-lock.json`, source `public/` assets, schemas, fixtures and `.gitkeep` files trackable.
- `.pytest_cache` currently self-ignores through its own `.gitignore`; root policy should still be explicit.

Classification of the future `.gitignore` change: FOUNDER_GATE because it affects what the first large commit can see.

---

## 17. Proposed Target Structure

No directory is created or moved in this task. Proposed future structure:

```text
agent/
├── roadmap/
├── specs/
├── runbooks/
├── governance/
├── longevity_knowledge_base/
│   ├── entries/
│   ├── templates/
│   ├── schemas/
│   ├── indexes/
│   ├── review_logs/
│   └── scripts/
├── user_health_information/
├── knowledge_seed/
├── knowledge_seed_v0/
├── closeouts/
├── artifacts/
└── archive/
    ├── brand_and_repository_migrations/
    ├── milestone_closeouts/
    ├── deployment_history/
    └── prompt_review_history/
```

Rules:

1. Active source/spec/runbook paths must be updated before any move.
2. Formal knowledge and process records must not share the same directory.
3. `agent/artifacts/` remains the historical artifact home; root `artifacts/` requires provenance resolution.
4. Founder must resolve whether canonical knowledge entries live under `entries/<layer>/` or top-level layer directories.
5. Archive moves happen only after consolidation, hash manifest and reference update.

---

## 18. Atomic Commit Plan

| # | Suggested commit message | Exact scope | Depends on | Gate | Validation | Independent push / rollback |
|---:|---|---|---|---|---|---|
| C01 | `chore(repo): align active paths with congtie-api` | `README.md`; ten 2026-08-11-touched agent docs: `agent/agent_decision_trace_spec.v0.1.md`, `agent/agent_evidence_closure_spec.v0.1.md`, `agent/agent_observability_spec.v0.1.md`, `agent/agent_registry_loading_spec.v0.1.md`, `agent/agent_release_runbook.v0.1.md`, `agent/agent_runtime_checklist.notes.zh.v0.1.md`, `agent/agent_runtime_checklist.v0.1.md`, `agent/agent_test_scenarios.notes.zh.v0.1.md`, `agent/agent_test_scenarios.v0.1.md`, `agent/demo_runbook.v0.1.md` | Founder confirms brand compatibility wording | Identifier/brand | targeted old-path search; whitespace | Yes; documentation-only rollback |
| C02 | `chore(repo): establish ignore and local config hygiene` | `.gitignore`, `.env.example`, `pytest.ini` | D014 | Ignore policy | `git check-ignore -v` samples; secret scan | Yes; easy rollback |
| C03 | `feat(api-alpha): add bounded API scaffold and operational middleware` | `app/main.py`, `app/api/`, `app/core/`, `app/middleware/`, `app/schemas/`, `app/services/`, selected M1 API tests; resolve `app/__init__.py` explicitly | C02; D008/D009 | API/runtime/safety | focused M1 API Alpha suite | No until gate; code rollback may affect startup |
| C04 | `docs(api): align current API and agent contracts` | All non-example `spec/` Markdown/JSON/YAML except SQL; normalize integration-pack casing | C03 contract shape; D009/D010 | API/tool/safety/clinical | JSON/OpenAPI parse, focused API and boundary tests | No until contract gate |
| C05 | `db(schema): review v0 schema snapshot separately` | `spec/xiaoge_v0_schema_snapshot.sql` only | Approved DB model | Database/persistence | isolated schema apply and DB tests | No; high rollback impact |
| C06 | `feat(agent-runtime): add bounded runtime registry and boundary harness` | `app/agent_runtime/`, `schemas/agent/`, active agent runtime specs, `scripts/agent_*`, `scripts/validate_agent_registry.sh`, `scripts/run_boundary_suite.sh`, `tests/agent_boundary/`, M1 CLI/runtime tests | C02, C04; D011/D012/D016 | Runtime/tool identifier/safety | boundary suite, CLI contract, fixture compatibility | No until gate |
| C07 | `feat(frontend): add local Web/H5 trial shell` | `frontend/local-app/`, shared support dirs, M2/M3 frontend tests, Makefile M2 target | C03 stable envelope | Frontend contract | `make test-m2-frontend` | Yes after API contract; medium rollback |
| C08 | `docs(roadmap): add v0 release plan and backlog` | `agent/roadmap/v0_release_plan_2026_09.md`, `agent/roadmap/v0_release_task_backlog_2026_09.md` | C01 | None | whitespace/link checks | Yes |
| C09 | `docs(knowledge-seed): add governed v0 seed and action resources` | `agent/knowledge_seed_v0/` only | Evidence/safety review | Knowledge safety | all existing knowledge-seed/action-resource/topic validators and loaders | Yes after validation |
| C10 | `docs(knowledge-base): add entry framework and evidence governance` | KB README/templates/schemas/scripts plus `agent/longevity_knowledge_item_schema.v0.1.md` | C09 taxonomy references; D013 | Schema is conceptual only | knowledge-item validator on approved entry | Yes |
| C11 | `docs(user-health): add private context conceptual specifications` | `agent/user_health_information_library_mvp_spec.v0.1.md`, `agent/user_health_context_schema.v0.1.md` | C10 terminology | User data architecture; no implementation | scope/naming/whitespace review | Yes, docs only |
| C12 | `docs(roadmap): add longevity knowledge Batch 001 plan` | `agent/roadmap/longevity_knowledge_batch_001_plan.v0.1.md` | C09-C10 | None | taxonomy/schema references | Yes |
| C13 | `docs(knowledge): add approved healthspan definition` | `agent/longevity_knowledge_base/entries/knowledge/KN-T0101-0001.healthspan-definition.md` only | C10-C12; D018 | Human approval already exists; publication still separate | validator + exact protected SHA-256 | Yes; isolated content rollback |
| C14 | `docs(archive): consolidate and archive approved historical records` | Only Founder-approved Appendix B/C/D summaries and archive moves; never deletion candidates in same commit | D001-D005 | Cleanup/archive | source/target hash manifest, reference scan | Yes after backup; easy path rollback if history retained |
| C15 | `chore(frontend-preview): apply approved repository ownership model` | `frontend/official-preview/` according to Option A/B/C | D007 | Nested repo/deployment/resources | nested status, build/test in chosen repo, clone reproduction | No until gate; potentially destructive |

Deletion itself should be a separate future commit after C14 and external backup, not included in C14. C05 and C15 must never be folded into a broad initial import.

---

## 19. Founder Decision Table

| decision_id | File/path/group | Current classification | Proposed action | Reason | Replacement canonical document | Reference status | Deletion risk | Recommended decision | Founder decision | Founder note |
|---|---|---|---|---|---|---|---|---|---|---|
| D001 | Appendix A: 66 day plans | BACKUP_THEN_DELETE | External backup, reconcile links, delete later | Superseded one-day execution plans | Release plan/backlog + milestone summaries | Referenced by some closeouts/reviews | Medium | Approve after reference report |  |  |
| D002 | Appendix B: 68 day closeouts | CONSOLIDATE_THEN_ARCHIVE | Create milestone summaries then archive | Unique execution facts amid repetition | Future milestone closeouts | Cross-references exist | Medium | Approve consolidation |  |  |
| D003 | Eight brand/identifier records in Section 9 | ARCHIVE_REPO | Move to migration archive | Durable compatibility rationale | `AGENTS.md`, current roadmap, this audit | Historical references possible | Low | Approve archive |  |  |
| D004 | `agent/artifacts/` | ARCHIVE_REPO | Track in historical artifact area after privacy scan | Reproducibility/audit evidence | Same path or future archive subtree | XSB explicitly protected | Medium | Approve archive retention |  |  |
| D005 | Appendix C/D historical M4/M5 and prompt chains | CONSOLIDATE_THEN_ARCHIVE | Summarize decisions, archive originals | High duplication, some unique gates | Current M4 packet, roadmap, biomarker draft/validator | Many references | Medium/high | Approve phased consolidation |  |  |
| D006 | Current M4 paths in Section 13 | FOUNDER_GATE | Keep active until deployment model is current | Production host/TLS/service/rollback identifiers | None fully replaces them | Current deployment references | High | Review before any archive/commit |  |  |
| D007 | `frontend/official-preview/` | FOUNDER_GATE | Choose A/B/C | Nested repo has no remote and parent cannot reproduce it | None | Parent sees one embedded repo | High | Choose A now; revisit C later |  |  |
| D008 | `app/__init__.py` | FOUNDER_GATE | Restore or retain deletion explicitly | Empty package marker may affect tools/imports | None | Package convention only | Medium | Restore unless namespace package is intentional |  |  |
| D009 | Tracked API/runtime/spec changes | FOUNDER_GATE | Review and split C03-C05 | Not rename-only; changes contracts, states and DB | Current approved API envelope/AGENTS rules | Code/tests/specs interdependent | High | Do not stage as one set |  |  |
| D010 | Integration-pack case mismatch | FOUNDER_GATE | Explicit case-only normalization | Linux portability and duplicate-path risk | Chosen canonical casing | Git index/disk differ | Medium | Normalize before first push |  |  |
| D011 | Two A2A contract copies | BACKUP_THEN_DELETE / FOUNDER_GATE | Keep `schemas/agent`, update docs, delete `agent` copy after backup | Byte-identical duplicate | `schemas/agent/a2a_contract.v0.1.json` | Two docs point to old path | Low after references | Approve canonical runtime path |  |  |
| D012 | Five empty paths in Section 20 | UNRESOLVED | Assign owner/purpose or delete after backup | Empty content cannot express intent | None | One is described as current fixture | Medium | Resolve individually |  |  |
| D013 | KB `entries/knowledge/` vs top-level `knowledge/` | FOUNDER_GATE | Select canonical directory convention and update README | Approved entry conflicts with README directory semantics | Founder-approved entry path or revised README | Future automation affected | High | Keep approved path unchanged until decision |  |  |
| D014 | `.gitignore` additions | FOUNDER_GATE | Apply reviewed ignore rules before bulk staging | Current worktree exposes generated content | Root ignore policy | Affects first import visibility | Medium | Approve with dist/DB exceptions |  |  |
| D015 | Root `artifacts/xsb001_*` | FOUNDER_GATE | Compare provenance; retain until resolved | Files differ from protected `agent/artifacts` copies | `agent/artifacts/` if confirmed | Historical XSB semantics protected | High | Do not delete yet |  |  |
| D016 | Active/legacy environment identifiers | FOUNDER_GATE | Approve compatibility horizon and public naming | App/scripts/examples expose both alias families | Future identifier migration decision | Tests/docs depend on aliases | High | Preserve aliases until explicit deprecation plan |  |  |
| D017 | Founder QR public asset | FOUNDER_GATE | Confirm consent and intended publication | Personal contact/identity asset | None | Used by preview source/build | High privacy | Require explicit approval |  |  |
| D018 | Approved knowledge entry | KEEP_ACTIVE | Commit alone, keep runtime/retrieval disabled | Human-approved canonical content | Itself | Validator and hash gate | High content integrity | Approve isolated C13 only |  |  |
| D019 | Existing spec whitespace findings | FOUNDER_GATE | Fix only in owning contract commit | Global diff check already fails in two specs | Owning spec files | Pre-existing | Low/medium | Keep separate from audit/rename |  |  |

---

## 20. Risks

### 20.1 Highest-risk findings

1. **Accidental embedded repository:** parent bulk staging may record an unusable nested gitlink.
2. **Contract drift:** OpenAPI, agent tools, API behavior and runtime source do not form a proven atomic change today.
3. **Clinical/safety drift:** modified specs introduce state/color, confidence, biomarker and recommendation language that requires Founder safety review and must not become production clinical logic.
4. **Database drift:** the SQL snapshot removes observation/assessment structures and adds systems/state/strategy structures; it needs an isolated DB gate.
5. **Identifier drift:** current public/runtime material mixes current brand, legacy names and alias environment variables.
6. **Case portability:** integration-pack index and disk casing differ.
7. **Knowledge path ambiguity:** approved entry placement and KB README semantics conflict.
8. **Local/private exposure:** `.env`, hosting bindings, local Wrangler DB state, screenshots and founder QR require differentiated handling.
9. **Process noise:** 329 cleanup/archive candidates are classified (68 backup/delete, 109 archive, 152 consolidate); broad deletion would destroy uncommitted history.
10. **Generated volume:** nested dependencies/build state greatly exceed source size.

### 20.2 Exact unresolved paths

All are zero length:

```text
agent/demo_requests/a2a_demo_hardstop_high_glucose.v0.1.json
app/agent_runtime/mocks/mock_metabolic_system.py
app/agent_runtime/prompts/response_guard_prompt.v0.1.md
app/agent_runtime/prompts/system_prompt.v0.1.md
scripts/generate_trace_report.py
```

The empty demo request is referenced by `agent/m1_api_alpha_runtime_fixture_inventory_2026_08_XX.v0.1.md` as current; the other four had no direct non-generated reference in this scan. Product/runtime owners must decide whether to populate, retain as explicit placeholders, or backup/delete them.

---

## 21. Execution Order

1. Founder fills every row in Section 19.
2. Freeze the worktree and regenerate status/secret/large-file manifests.
3. Resolve nested repository ownership before any parent bulk staging.
4. Resolve `.gitignore` exceptions and apply C02 first.
5. Create external backup for approved BACKUP_THEN_DELETE paths; verify hashes.
6. Resolve `app/__init__.py`, case-only spec path and empty placeholders.
7. Review and commit C01-C13 in dependency order, running each listed validation.
8. Produce milestone/decision summaries for approved consolidation groups.
9. Archive with hash/reference verification in C14.
10. Execute deletions in a separate, reviewable commit only after archive and backup.
11. Apply C15 only under the selected nested-repository option.
12. Push commits incrementally only after each gate and validation; never push an undifferentiated 1,052-file import.

---

## 22. Acceptance Criteria

This audit is complete when:

- the precondition and protected-entry hash are recorded;
- every parent tracked/untracked/ignored entry is assigned by exact path or homogeneous group;
- all deletion, archive, consolidation and unresolved candidates have exact path manifests;
- current canonical assets and duplicate relationships are identified;
- all 17 tracked dirty paths are individually reviewed;
- `app/__init__.py`, `.gitignore`, nested repo, API/runtime/DB/deployment and biomarker gates are explicit;
- local/private and large/binary risks are recorded without exposing secret values;
- the atomic plan separates cleanup, contracts, DB, runtime, frontend, knowledge, deployment and approved content;
- no existing file was modified, deleted, moved, renamed, staged, committed or pushed;
- the approved knowledge entry remains VALID with the expected SHA-256;
- the only audit-task change is this new Markdown file.

---

## Appendix A. Exact BACKUP_THEN_DELETE Daily Plan Candidates

```text
agent/day_plan_2026_04_21.v0.1.md
agent/day_plan_2026_04_22.v0.1.md
agent/day_plan_2026_04_23.v0.1.md
agent/day_plan_2026_04_24.v0.1.md
agent/day_plan_2026_04_25.v0.1.md
agent/day_plan_2026_04_26.v0.1.md
agent/day_plan_2026_04_27.v0.1.md
agent/day_plan_2026_04_29.v0.1.md
agent/day_plan_2026_04_30.v0.1.md
agent/day_plan_2026_05_01.v0.1.md
agent/day_plan_2026_05_02.v0.1.md
agent/day_plan_2026_05_03.v0.1.md
agent/day_plan_2026_05_04.v0.1.md
agent/day_plan_2026_05_05.v0.1.md
agent/day_plan_2026_05_06.v0.1.md
agent/day_plan_2026_05_07.v0.1.md
agent/day_plan_2026_05_08.v0.1.md
agent/day_plan_2026_05_09.v0.1.md
agent/day_plan_2026_05_10.v0.1.md
agent/day_plan_2026_05_11.v0.1.md
agent/day_plan_2026_05_12.v0.1.md
agent/day_plan_2026_05_13.v0.1.md
agent/day_plan_2026_05_14.v0.1.md
agent/day_plan_2026_05_15.v0.1.md
agent/day_plan_2026_05_16.v0.1.md
agent/day_plan_2026_05_17.v0.1.md
agent/day_plan_2026_05_18.v0.1.md
agent/day_plan_2026_05_19.v0.1.md
agent/day_plan_2026_05_20.v0.1.md
agent/day_plan_2026_05_21.v0.1.md
agent/day_plan_2026_05_22.v0.1.md
agent/day_plan_2026_05_23.v0.1.md
agent/day_plan_2026_05_24.v0.1.md
agent/day_plan_2026_05_25.v0.1.md
agent/day_plan_2026_05_26.v0.1.md
agent/day_plan_2026_05_27.v0.1.md
agent/day_plan_2026_05_28.v0.1.md
agent/day_plan_2026_05_29.v0.1.md
agent/day_plan_2026_05_30.v0.1.md
agent/day_plan_2026_05_31.v0.1.md
agent/day_plan_2026_06_01.v0.1.md
agent/day_plan_2026_06_02.v0.1.md
agent/day_plan_2026_06_03.v0.1.md
agent/day_plan_2026_06_04.v0.1.md
agent/day_plan_2026_06_05.v0.1.md
agent/day_plan_2026_06_06.v0.1.md
agent/day_plan_2026_06_07.v0.1.md
agent/day_plan_2026_06_08.v0.1.md
agent/day_plan_2026_06_09.v0.1.md
agent/day_plan_2026_06_10.v0.1.md
agent/day_plan_2026_06_11.v0.1.md
agent/day_plan_2026_06_12.v0.1.md
agent/day_plan_2026_06_13.v0.1.md
agent/day_plan_2026_06_14.v0.1.md
agent/day_plan_2026_06_15.v0.1.md
agent/day_plan_2026_06_16.v0.1.md
agent/day_plan_2026_06_17.v0.1.md
agent/day_plan_2026_06_18.v0.1.md
agent/day_plan_2026_06_19.v0.1.md
agent/day_plan_2026_06_20.v0.1.md
agent/day_plan_2026_06_21.v0.1.md
agent/day_plan_2026_06_22.v0.1.md
agent/day_plan_2026_06_23.v0.1.md
agent/day_plan_2026_06_24.v0.1.md
agent/day_plan_2026_06_25.v0.1.md
agent/day_plan_2026_06_28.v0.1.md
```

## Appendix B. Exact CONSOLIDATE_THEN_ARCHIVE Daily Closeouts

```text
agent/day_closeout_2026_04_21.v0.1.md
agent/day_closeout_2026_04_22.v0.1.md
agent/day_closeout_2026_04_24.v0.1.md
agent/day_closeout_2026_04_25.v0.1.md
agent/day_closeout_2026_04_26.v0.1.md
agent/day_closeout_2026_04_27.v0.1.md
agent/day_closeout_2026_04_28.v0.1.md
agent/day_closeout_2026_04_29.v0.1.md
agent/day_closeout_2026_04_30.v0.1.md
agent/day_closeout_2026_05_01.v0.1.md
agent/day_closeout_2026_05_02.v0.1.md
agent/day_closeout_2026_05_03.v0.1.md
agent/day_closeout_2026_05_04.v0.1.md
agent/day_closeout_2026_05_05.v0.1.md
agent/day_closeout_2026_05_06.v0.1.md
agent/day_closeout_2026_05_07.v0.1.md
agent/day_closeout_2026_05_08.v0.1.md
agent/day_closeout_2026_05_09.v0.1.md
agent/day_closeout_2026_05_10.v0.1.md
agent/day_closeout_2026_05_11.v0.1.md
agent/day_closeout_2026_05_12.v0.1.md
agent/day_closeout_2026_05_13.v0.1.md
agent/day_closeout_2026_05_14.v0.1.md
agent/day_closeout_2026_05_15.v0.1.md
agent/day_closeout_2026_05_16.v0.1.md
agent/day_closeout_2026_05_17.v0.1.md
agent/day_closeout_2026_05_18.v0.1.md
agent/day_closeout_2026_05_19.v0.1.md
agent/day_closeout_2026_05_20.v0.1.md
agent/day_closeout_2026_05_21.v0.1.md
agent/day_closeout_2026_05_22.v0.1.md
agent/day_closeout_2026_05_23.v0.1.md
agent/day_closeout_2026_05_24.v0.1.md
agent/day_closeout_2026_05_25.v0.1.md
agent/day_closeout_2026_05_26.v0.1.md
agent/day_closeout_2026_05_27.v0.1.md
agent/day_closeout_2026_05_28.v0.1.md
agent/day_closeout_2026_05_29.v0.1.md
agent/day_closeout_2026_05_30.v0.1.md
agent/day_closeout_2026_05_31.v0.1.md
agent/day_closeout_2026_06_01.v0.1.md
agent/day_closeout_2026_06_02.v0.1.md
agent/day_closeout_2026_06_03.v0.1.md
agent/day_closeout_2026_06_04.v0.1.md
agent/day_closeout_2026_06_05.v0.1.md
agent/day_closeout_2026_06_06.v0.1.md
agent/day_closeout_2026_06_07.v0.1.md
agent/day_closeout_2026_06_08.v0.1.md
agent/day_closeout_2026_06_09.v0.1.md
agent/day_closeout_2026_06_10.v0.1.md
agent/day_closeout_2026_06_11.v0.1.md
agent/day_closeout_2026_06_12.v0.1.md
agent/day_closeout_2026_06_13.v0.1.md
agent/day_closeout_2026_06_14.v0.1.md
agent/day_closeout_2026_06_15.v0.1.md
agent/day_closeout_2026_06_16.v0.1.md
agent/day_closeout_2026_06_17.v0.1.md
agent/day_closeout_2026_06_18.v0.1.md
agent/day_closeout_2026_06_19.v0.1.md
agent/day_closeout_2026_06_20.v0.1.md
agent/day_closeout_2026_06_21.v0.1.md
agent/day_closeout_2026_06_22.v0.1.md
agent/day_closeout_2026_06_23.v0.1.md
agent/day_closeout_2026_06_24.v0.1.md
agent/day_closeout_2026_06_27.v0.1.md
agent/day_closeout_2026_06_30.v0.1.md
agent/day_closeout_2026_07_03.v0.1.md
agent/day_closeout_2026_07_06.v0.1.md
```

## Appendix C. Exact Historical M4/M5 CONSOLIDATE_THEN_ARCHIVE Paths

```text
agent/m4_fastapi_systemd_service_final_draft_2026_05_15.service
agent/m4_nginx_staging_congtie_final_draft_2026_05_15.conf
agent/m4_staging_cloud_ingress_80_verification_report_2026_05_15.v0.1.md
agent/m4_staging_cloud_ingress_80_verification_status_2026_05_15.v0.1.md
agent/m4_staging_dns_tls_access_decision_2026_05_14.v0.1.md
agent/m4_staging_dns_tls_access_decision_status_2026_05_14.v0.1.md
agent/m4_staging_env_final_template_2026_05_15.env.example
agent/m4_staging_founder_trial_ready_closeout_2026_05_15.v0.1.md
agent/m4_staging_founder_trial_ready_closeout_status_2026_05_15.v0.1.md
agent/m4_staging_level1_host_prep_approval_2026_05_15.v0.1.md
agent/m4_staging_level1_host_prep_approval_status_2026_05_15.v0.1.md
agent/m4_staging_level1_host_prep_writes_report_2026_05_15.v0.1.md
agent/m4_staging_level1_host_prep_writes_status_2026_05_15.v0.1.md
agent/m4_staging_level2_config_apply_approval_2026_05_15.v0.1.md
agent/m4_staging_level2_config_apply_approval_status_2026_05_15.v0.1.md
agent/m4_staging_level2_config_apply_checklist_2026_05_15.v0.1.md
agent/m4_staging_level2_config_apply_execution_report_2026_05_15.v0.1.md
agent/m4_staging_level2_config_apply_execution_status_2026_05_15.v0.1.md
agent/m4_staging_level2_config_draft_finalization_report_2026_05_15.v0.1.md
agent/m4_staging_level2_config_draft_finalization_status_2026_05_15.v0.1.md
agent/m4_staging_level3_app_static_deploy_approval_2026_05_15.v0.1.md
agent/m4_staging_level3_app_static_deploy_approval_status_2026_05_15.v0.1.md
agent/m4_staging_level3_app_static_deploy_execution_report_2026_05_15.v0.1.md
agent/m4_staging_level3_app_static_deploy_execution_status_2026_05_15.v0.1.md
agent/m4_staging_level4_service_start_http_smoke_approval_2026_05_15.v0.1.md
agent/m4_staging_level4_service_start_http_smoke_approval_status_2026_05_15.v0.1.md
agent/m4_staging_level4_service_start_http_smoke_execution_report_2026_05_15.v0.1.md
agent/m4_staging_level4_service_start_http_smoke_execution_status_2026_05_15.v0.1.md
agent/m4_staging_level5_tls_http_to_https_approval_2026_05_15.v0.1.md
agent/m4_staging_level5_tls_http_to_https_approval_status_2026_05_15.v0.1.md
agent/m4_staging_level5_tls_http_to_https_execution_report_2026_05_15.v0.1.md
agent/m4_staging_level5_tls_http_to_https_execution_status_2026_05_15.v0.1.md
agent/m4_staging_public_http_reachability_fix_and_rerun_report_2026_05_15.v0.1.md
agent/m4_staging_public_http_reachability_fix_and_rerun_status_2026_05_15.v0.1.md
agent/m4_staging_static_path_hygiene_hardening_approval_2026_05_15.v0.1.md
agent/m4_staging_static_path_hygiene_hardening_approval_status_2026_05_15.v0.1.md
agent/m4_staging_static_path_hygiene_hardening_execution_report_2026_05_15.v0.1.md
agent/m4_staging_static_path_hygiene_hardening_execution_status_2026_05_15.v0.1.md
agent/m4_staging_sudo_access_resolution_report_2026_05_15.v0.1.md
agent/m4_staging_sudo_access_resolution_rerun_report_2026_05_15.v0.1.md
agent/m4_staging_sudo_access_resolution_rerun_status_2026_05_15.v0.1.md
agent/m4_staging_sudo_access_resolution_status_2026_05_15.v0.1.md
agent/m4_staging_tls_hardening_and_founder_trial_readiness_report_2026_05_15.v0.1.md
agent/m4_staging_tls_hardening_and_founder_trial_readiness_status_2026_05_15.v0.1.md
agent/m5_founder_manual_trial_result_2026_05_16.v0.1.md
agent/m5_founder_manual_trial_result_capture_status_2026_05_16.v0.1.md
agent/m5_founder_only_trial_checklist_2026_05_16.v0.1.md
agent/m5_founder_only_trial_execution_approval_2026_05_16.v0.1.md
agent/m5_founder_only_trial_execution_status_2026_05_16.v0.1.md
agent/m5_founder_only_trial_feedback_template_2026_05_16.v0.1.md
agent/m5_founder_only_trial_plan_2026_05_16.v0.1.md
agent/m5_founder_only_trial_plan_status_2026_05_16.v0.1.md
agent/m5_founder_only_trial_technical_smoke_report_2026_05_16.v0.1.md
agent/m5_founder_trial_blank_shell_debug_and_fix_report_2026_05_16.v0.1.md
agent/m5_founder_trial_blank_shell_debug_and_fix_status_2026_05_16.v0.1.md
agent/m5_founder_trial_closeout_2026_05_16.v0.1.md
agent/m5_founder_trial_closeout_and_next_stage_plan_status_2026_05_16.v0.1.md
agent/m5_next_stage_plan_2026_05_16.v0.1.md
agent/m5_staging_frontend_default_chinese_localization_report_2026_05_16.v0.1.md
agent/m5_staging_frontend_default_chinese_localization_status_2026_05_16.v0.1.md
agent/m5_staging_frontend_nav_chinese_patch_report_2026_05_16.v0.1.md
agent/m5_staging_frontend_nav_chinese_patch_status_2026_05_16.v0.1.md
agent/m5_staging_frontend_remaining_chinese_polish_report_2026_05_16.v0.1.md
agent/m5_staging_frontend_remaining_chinese_polish_status_2026_05_16.v0.1.md
```

## Appendix D. Exact Prompt/Founder-Review CONSOLIDATE_THEN_ARCHIVE Paths

```text
agent/biomarker_system_map_v0.2_context_layer_spec_prompt_2026_08_11.v0.1.md
agent/biomarker_system_map_v0.2_context_layer_spec_prompt_founder_review_2026_08_11.v0.1.md
agent/biomarker_system_map_v0.2_marker_expansion_patch_execution_prompt_2026_07_31.v0.1.md
agent/biomarker_system_map_v0.2_marker_expansion_patch_execution_prompt_founder_review_2026_07_31.v0.1.md
agent/biomarker_system_map_v0.2_ownership_patch_execution_prompt_2026_07_21.v0.1.md
agent/biomarker_system_map_v0.2_ownership_patch_execution_prompt_founder_review_2026_07_21.v0.1.md
agent/biomarker_system_map_v0.2_source_doc_warning_cleanup_patch_execution_prompt_2026_08_03.v0.1.md
agent/biomarker_system_map_v0.2_source_doc_warning_cleanup_patch_execution_prompt_founder_review_2026_08_03.v0.1.md
agent/biomarker_system_map_v0.2_unresolved_ownership_note_patch_execution_prompt_2026_08_06.v0.1.md
agent/biomarker_system_map_v0.2_unresolved_ownership_note_patch_execution_prompt_founder_review_2026_08_06.v0.1.md
agent/biomarker_system_map_v0.2_validation_script_prompt_2026_07_24.v0.1.md
agent/biomarker_system_map_v0.2_validation_script_prompt_founder_review_2026_07_24.v0.1.md
agent/biomarker_system_map_v0.2_validation_test_fixtures_prompt_2026_07_27.v0.1.md
agent/biomarker_system_map_v0.2_validation_test_fixtures_prompt_founder_review_2026_07_27.v0.1.md
agent/biomarker_system_map_v0.2_validator_calibration_execution_prompt_2026_07_25.v0.1.md
agent/biomarker_system_map_v0.2_validator_calibration_execution_prompt_founder_review_2026_07_25.v0.1.md
agent/biomarker_system_map_v0.2_weight_term_validator_calibration_execution_prompt_2026_08_01.v0.1.md
agent/biomarker_system_map_v0.2_weight_term_validator_calibration_execution_prompt_founder_review_2026_08_01.v0.1.md
agent/minimal_json_execution_prompt_2026_07_17.v0.1.md
agent/minimal_json_execution_prompt_founder_review_2026_07_17.v0.1.md
```
