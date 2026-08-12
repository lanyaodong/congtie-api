# Congtie Git Hygiene Preparation Review v0.1

Version: v0.1
Project: Congtie
Status: Draft
Owner: Founder
Review Date: 2026-08-11
Review Mode: Read-only preparation

---

## 1. Purpose

This document reviews Git hygiene for the first major atomic commit sequence in `congtie-api`.

It defines:

- what may enter Git;
- what should be ignored as generated or local-only state;
- what requires Founder approval;
- how nested repository ownership should be protected;
- how the known case-sensitivity mismatch should be handled;
- how to stage the first commit sequence safely.

This review does not modify `.gitignore`, source files, schemas, knowledge entries, runtime, API, database, frontend, deployment, or biomarker JSON. It does not move, rename, delete, stage, commit, push, change remote, or change branch.

---

## 2. Current Repository State

Repository identity:

```text
root: /Users/lanyaodong/Documents/congtie-api
branch: main
HEAD: 71f3c2fde58f1655d5c3b86656b063b8784f76c8
remote: git@github.com:lanyaodong/congtie-api.git
upstream display: main...origin/main
```

Audit-time status counts from `git status --porcelain=v1 -uall`:

| Category | Count |
|---|---:|
| Staged paths | 0 |
| Modified tracked paths | 16 |
| Deleted tracked paths | 1 |
| Untracked files | 1056 |
| Other tracked status | 0 |

High-level status includes:

- tracked changes to root configuration, application, scripts, specifications, tests, and a database schema snapshot;
- one tracked deletion at `app/__init__.py`;
- many untracked governance, knowledge, runtime, API, test, artifact, schema, and frontend paths;
- a root `.pnpm-store/` package-manager cache;
- a nested independent repository at `frontend/official-preview`;
- no staged paths.

Audit-time status path fingerprint:

```text
7175fa2d9de6542d375464c7698430f988e9f4143331aa4a670a94fa1bf90602
```

The fingerprint identifies the sorted path/status inventory, not file content and not an approved release.

No staging, commit, push, branch, remote, cleanup, move, rename, or deletion operation was executed by this review.

---

## 3. Git Hygiene Principles

Congtie uses:

```text
explicit staging
+ atomic commits
+ human approval
```

Principles:

1. Never use `git add .` for the first large commit.
2. Stage exact approved paths only.
3. One commit must represent one understandable and reversible change.
4. Generated files are not source assets by default.
5. Secrets and local private files never enter Git.
6. Nested repositories require explicit ownership and parent protection.
7. Global or machine-local ignore behavior is not a substitute for repository `.gitignore` governance.
8. Runtime, API, database, deployment, safety, and persistent user-data changes require separate review.
9. Historical artifacts are not deleted or ignored blindly merely because they look generated.
10. Staged diffs must be reviewed independently from working-tree diffs.
11. Human approves the staging boundary; AI executes only within that boundary.
12. Founder-gated ambiguity is excluded rather than guessed.

---

## 4. Current `.gitignore` Audit

Current repository `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
.DS_Store
```

### 4.1 Already Protected by Repository Rules

| Pattern | Coverage | Classification | Note |
|---|---|---|---|
| `.env` | Root/local environment file | Already covered | Keep protected; never stage secret values |
| `.venv/` | Python virtual environment | Already covered | Current local copy is generated |
| `__pycache__/` | Python bytecode cache directories | Already covered | Portable repository rule |
| `*.pyc` | Python bytecode files | Already covered | Portable repository rule |
| `.DS_Store` | macOS metadata | Already covered | Portable repository rule |

`.pytest_cache/` currently contains its own generated `.gitignore`, but the root repository does not explicitly protect it. No user-level global excludes file is configured. Repository protection should be explicit and portable.

### 4.2 Recommended Additions

This table is a proposal only. No rule is added by this review.

| Candidate | Current Root Coverage | Classification | Recommendation |
|---|---|---|---|
| `node_modules/` | Not covered | Add recommended | Standard dependency output; nested frontend already ignores its own copy |
| `.pnpm-store/` | Not covered | Add recommended | Root-local package store and database files |
| `.vinext/` | Not covered | Add recommended | Generated frontend build/cache state |
| `.next/` | Not covered | Add recommended | Generated Next.js output |
| `.pytest_cache/` | Not covered by root | Add recommended | Do not rely on cache-generated self-ignore |
| `.ruff_cache/` | Not covered | Add recommended | Generated lint cache |
| `.mypy_cache/` | Not covered | Add recommended | Generated type-check cache |
| `.tox/` and `.nox/` | Not covered | Add recommended | Generated test environments |
| `.coverage` | Not covered | Add recommended | Generated coverage data |
| `coverage/` | Not covered | Add recommended | Generated coverage output |
| `htmlcov/` | Not covered | Add recommended | Generated HTML coverage output |
| `.wrangler/` | Not covered | Add recommended | Local Cloudflare/Miniflare state |
| `.idea/` | Not covered | Add recommended | Machine-local IDE state |
| `*.swp`, `*.swo`, `*~` | Not covered | Add recommended | Temporary editor files |
| `.vscode/` | Not covered | Founder decision required | Some teams commit shared tasks/settings; do not ignore blindly |
| `.env.*` with `!.env.example` | Not covered | Add recommended with exception | Protect local variants while preserving reviewed templates |
| `*.log` or `logs/` | Not covered | Founder decision required | Blanket rule could hide governed validation logs under artifact directories |
| `*.db`, `*.sqlite`, `*.sqlite3` | Not covered | Founder decision required | Use scoped local/cache patterns; do not hide governed fixtures or approved databases blindly |
| `dist/` | Not covered | Founder decision required | Root `dist/` contains an external trial package that may be a governed release artifact |
| `build/` | Not covered | Founder decision required | Some build directories may contain source-side hosting plugins or governed output |
| `frontend/official-preview/` | Not covered | Add recommended after GH-004 confirmation | Protect independent nested repository from parent staging |

### 4.3 Do Not Ignore by Default

| Path or category | Classification | Reason |
|---|---|---|
| `.env.example` | Do not ignore | Candidate source-controlled configuration template after value review |
| `.github/` | Do not ignore | Repository workflow and governance source |
| `agent/longevity_knowledge_base/entries/**` | Do not ignore | Canonical knowledge source |
| `agent/longevity_knowledge_base/schemas/**` | Do not ignore | Governed evidence/schema documentation |
| `.openai/hosting.json` inside the independent frontend repo | Do not ignore there | Hosting source configuration, not generated output |
| `agent/artifacts/**` | Founder decision required | Contains QA evidence and historical trial records, not one homogeneous cache |
| `artifacts/**` | Founder decision required | Historical scenario evidence; preserve until exact-list review |
| `spec/*.sql` | Founder decision required | Database/schema snapshots require separate review, not blanket ignore |

---

## 5. Generated Files Analysis

### 5.1 Inventory

| Category | Location | Approximate Size | File Count | Recommendation | Reason |
|---|---|---:|---:|---|---|
| Python virtual environment | `.venv/` | 31M | 1509 | `IGNORE_GENERATED` | Already protected by root `.gitignore` |
| pnpm store | `.pnpm-store/` | 48K | 3 | `IGNORE_GENERATED` | Contains local package-store database, SHM, and WAL files |
| pytest cache | `.pytest_cache/` | 48K | 7 | `IGNORE_GENERATED` | Test cache; add portable root rule |
| Root distribution package | `dist/` | 312K | 24 | `FOUNDER_GATE` | Contains `first_external_trial_package` and zip; may be governed release output |
| QA/review artifacts | `agent/artifacts/` | 4.9M | 102 | `FOUNDER_GATE` | Screenshots, trial records, logs, and review evidence require an artifact policy |
| Historical root artifacts | `artifacts/` | 16K | 3 | `FOUNDER_GATE` | Historical XSB evidence; preserve pending classification |
| Frontend dependencies | `frontend/official-preview/node_modules/` | 464M | 20665 | `IGNORE_GENERATED` | Protected by nested repo `.gitignore`; never enter parent Git |
| Frontend Vinext cache | `frontend/official-preview/.vinext/` | 172K | 13 | `IGNORE_GENERATED` | Protected by nested repo `.gitignore` |
| Frontend Next cache | `frontend/official-preview/.next/` | 4K | 1 | `IGNORE_GENERATED` | Protected by nested repo `.gitignore` |
| Wrangler local state | `frontend/official-preview/.wrangler/` | 52K | 4 | `IGNORE_GENERATED` | Includes generated local SQLite metadata; protected by nested repo |
| Frontend build directory | `frontend/official-preview/build/` | 4K | 1 | `KEEP` | Contains a tracked source-side hosting plugin file, not a disposable build tree |
| Frontend distribution output | `frontend/official-preview/dist/` | 3.4M | 71 | `FOUNDER_GATE` | Ignored by nested repo; hosting artifact policy still needs documentation |

### 5.2 Categories Not Found at Parent Root

No parent-root `node_modules/`, `.vinext/`, `.next/`, `coverage/`, `htmlcov/`, `.wrangler/`, `logs/`, or generic `build/` directory was found during this audit.

Their absence does not remove the need for portable ignore rules where the toolchain can generate them later.

### 5.3 Artifact Boundary

Do not apply one blanket ignore rule to all artifact-like paths.

Use this distinction:

```text
reproducible dependency/cache output
→ IGNORE_GENERATED

review evidence, release packages, screenshots, trial records
→ FOUNDER_GATE

source or hosting configuration
→ KEEP
```

No generated directory or artifact is deleted by this review.

---

## 6. Local Private Files Analysis

Only filenames and risk categories were inspected. Secret values were not reported.

| Filename or path | Location | Risk Type | Classification | Git Recommendation |
|---|---|---|---|---|
| `.env` | Repository root | Local secrets, URLs, credentials, database configuration | `LOCAL_PRIVATE` | Already ignored; never stage |
| `.env.example` | Repository root | Configuration template that could accidentally contain real values | Review candidate | Keep only after value-by-value secret and naming review |
| `index.db`, `index.db-shm`, `index.db-wal` | `.pnpm-store/v11/` | Local package-store database state | `LOCAL_PRIVATE` / generated | Ignore `.pnpm-store/`; never stage |
| `metadata.sqlite` | `frontend/official-preview/.wrangler/.../` | Local emulator/cache database | `LOCAL_PRIVATE` / generated | Already ignored by nested repository; never stage |
| `xiaoge_v0_schema_snapshot.sql` | `spec/` | Database schema snapshot, not a local secret file | `FOUNDER_GATE` | Separate independent database review before staging |

No private-key, certificate, PKCS archive, credential-named, or standalone token-named file was found outside excluded dependency/cache directories by the filename scan.

`.env.example` exposes configuration key names and includes non-empty local/example settings. No value is reproduced here. It should be reviewed independently before entering the first commit and should remain excluded from staging until that review is complete.

Security rule:

```text
Ignoring a secret file is necessary but not sufficient.
The staged blob set must still be scanned before every push.
```

---

## 7. Nested Repository Protection

Target:

```text
frontend/official-preview
```

Audit result:

```text
exists: true
independent .git: true
branch: main
HEAD: 9dafa395e9e0366ee8e15f825a17268f6f95a73c
remote: none configured
working tree: clean
hosting config: .openai/hosting.json
built hosting copy: dist/.openai/hosting.json
```

The nested repository has its own `.gitignore`, including protections for:

```text
node_modules
coverage
.next
.vinext
dist
.wrangler
environment files
debug logs
```

### 7.1 Options

#### Option A: Keep Independent Repository

Pros:

- Preserves independent Git history.
- Keeps frontend and hosting lifecycle separate.
- Avoids parent repository ownership ambiguity.

Cons:

- Requires a future remote, owner, deployment policy, and versioned API contract.
- Physical nesting remains operationally delicate.

Current assessment:

```text
Recommended and already approved for the current phase.
```

#### Option B: Convert to Submodule

Possible only after a remote and submodule workflow are approved.

Current assessment:

```text
Do not perform now.
```

#### Option C: Monorepo Merge

Would require explicit history migration, deployment consolidation, and ownership review.

Current assessment:

```text
Do not perform now.
```

### 7.2 Parent Protection Recommendation

After GH-004 approval, add this exact parent exclusion candidate:

```gitignore
frontend/official-preview/
```

Do not ignore the entire parent `frontend/` directory because it contains other candidate source and review assets.

Before each parent commit:

1. Confirm the nested Git root remains `frontend/official-preview`.
2. Confirm its own status separately.
3. Confirm no parent staged path points inside it.
4. Do not stage `frontend/` recursively.
5. Treat future submodule or monorepo conversion as a separate Founder-approved migration.

This review does not add the ignore rule or change either repository.

---

## 8. Case Sensitivity Issues

Affected integration-pack path:

```text
filesystem:
spec/agent_Integration_pack.v0.1.md

Git index:
spec/Agent_Integration_Pack.v0.1.md
```

Audit evidence:

```text
working-tree blob: fb6a8c312633e4f4fceed9caef17cf7ea197c905
index blob:        339c71cec52d263052098d5d1ba9771a94878abc
content numstat:   484 additions / 34 deletions
```

This is not currently a pure case-only rename. The working file also contains a substantial content change relative to the index.

Risks:

- macOS case-insensitive behavior can hide the index/filesystem mismatch;
- a direct stage may combine content changes with the rename;
- Linux and CI may resolve the path differently;
- references may drift between both spellings;
- calling the operation case-only would conceal a large semantic diff.

### 8.1 Recommended Two-phase Plan

Phase 1: Content decision

1. Review the `484/34` content diff independently.
2. Classify it under the appropriate specification/API integration commit.
3. Founder decides whether to accept, revise, or reject the content change.
4. Do not restore or discard content without explicit permission.

Phase 2: Case-only rename

1. Begin only after the content state is clean and approved.
2. Use a temporary intermediate filename on the case-insensitive filesystem.
3. Rename from the indexed historical spelling to the approved canonical spelling.
4. Verify Git records a rename rather than deletion plus unrelated addition.
5. Search and update active references in the same narrowly reviewed rename task if required.
6. Confirm file content hash is unchanged by the case-only phase.

Proposed canonical target:

```text
spec/agent_Integration_pack.v0.1.md
```

The exact temporary path and commands must be included in a separate execution review. No rename is executed here.

---

## 9. Staging Boundary Proposal

### 9.1 Immediate First Staging Candidate

The first staging operation should be C006 Repository Hygiene, only after GH-001, GH-004, GH-005, and GH-007 decisions are recorded.

Recommended initial C006 scope:

```text
.gitignore
agent/roadmap/git_hygiene_preparation_review.v0.1.md
```

The Integration Pack case rename should not enter this first staging unless its content diff has first been resolved. If unresolved, exclude it from C006.

Recommended first commit purpose:

```text
chore(repo): establish Git hygiene boundaries
```

This is a governance/hygiene commit and must precede experimental application changes.

### 9.2 Include in First Atomic Staging Cycle

After C006, the following are eligible for exact-manifest review in separate commits.

#### Repository Governance Foundation

```text
AGENTS.md
agent/roadmap/congtie_repository_ownership_map.v0.1.md
agent/roadmap/congtie_im_connector_audit_v0.1.md
agent/roadmap/post_rename_repository_simplification_audit_and_atomic_commit_plan_2026_08_11.v0.1.md
agent/roadmap/congtie_atomic_git_commit_plan.v0.1.md
agent/roadmap/git_hygiene_preparation_review.v0.1.md
```

#### Knowledge Library Foundation

```text
agent/longevity_knowledge_base/README.md
agent/longevity_knowledge_base/templates/longevity_knowledge_item_template.v0.1.md
agent/longevity_knowledge_base/schemas/evidence_source_type_enum.v0.1.md
agent/longevity_knowledge_base/schemas/evidence_source_type_alignment_notes.v0.1.md
agent/longevity_knowledge_base/scripts/validate_longevity_knowledge_item.py
agent/longevity_knowledge_item_schema.v0.1.md
agent/evidence_grading_framework.v0.1.md
agent/knowledge_seed_v0/longevity_information_library_architecture.v0.1.md
agent/knowledge_seed_v0/longevity_information_library_architecture_patch_for_taxonomy.v0.1.md
agent/knowledge_seed_v0/longevity_topic_taxonomy.v0.1.md
```

The canonical path alignment must be included consistently. Legacy top-level directories must not be populated or deleted through this staging cycle.

#### User Health Context Foundation

```text
agent/user_health_information_library_mvp_spec.v0.1.md
agent/user_health_context_schema.v0.1.md
```

These are conceptual documents only. No database, schema implementation, API, runtime, or user data is included.

#### Release Planning

```text
agent/roadmap/v0_release_plan_2026_09.md
agent/roadmap/v0_release_task_backlog_2026_09.md
agent/roadmap/longevity_knowledge_batch_001_plan.v0.1.md
```

#### First Official Knowledge Asset

Dedicated one-file commit only:

```text
agent/longevity_knowledge_base/entries/knowledge/KN-T0101-0001.healthspan-definition.md
```

Required protected fields:

```yaml
status: "approved"
runtime_enabled: false
retrieval_enabled: false
```

### 9.3 Exclude From First Staging

```text
.env
.venv/
.pnpm-store/
.pytest_cache/
node_modules/
.next/
.vinext/
.wrangler/
coverage output
local databases and cache databases
temporary files
frontend/official-preview/**
```

Also exclude until separately classified:

```text
dist/**
agent/artifacts/**
artifacts/**
.env.example
spec/agent_Integration_pack.v0.1.md content change and rename
historical archive candidates
```

### 9.4 Founder Gate Required

The following must not enter the first governance/knowledge staging cycle:

```text
app/** runtime and service changes
app/__init__.py deletion and package/import behavior
API routes, middleware, envelopes, and contracts
spec/xiaoge_v0_schema_snapshot.sql
database or persistence changes
tests tied to unreviewed application behavior
parent-owned frontend implementation changes
deployment configuration
safety interruption semantic changes
biomarker JSON
ambiguous historical files
generated or release artifacts without an artifact policy
```

These require separate engineering manifests, tests, and Founder Gates.

### 9.5 Staging Procedure

For each atomic commit:

1. Review current `git status`.
2. Produce an exact include/exclude manifest.
3. Resolve the commit-specific Founder Gate.
4. Stage only approved paths.
5. Review staged name/status output.
6. Review the full staged diff.
7. Scan staged blobs for secrets.
8. Run commit-specific validation.
9. Commit only that approved unit.
10. Verify the resulting commit before starting the next unit.

Never use `git add .` for this initial repository capture.

---

## 10. Founder Decision Table

| Decision ID | Topic | Current State | Recommendation | Options | Founder Decision | Founder Notes |
|---|---|---|---|---|---|---|
| GH-001 | `.gitignore` additions | Only five basic patterns exist | Approve a line-by-line portable ignore patch | Approve proposed set; approve reduced set; revise | Pending | No `.gitignore` modification in this review |
| GH-002 | `node_modules` and generated folders | Nested frontend has 464M dependencies; root `.pnpm-store` is untracked | Ignore dependency/cache outputs explicitly | Ignore generated; selectively keep; defer | Pending | Do not delete through this task |
| GH-003 | `dist` and build output | Root trial package and nested hosting output have different governance value | Do not blanket-ignore; classify by repository and artifact purpose | Keep governed artifact; ignore reproducible output; archive separately | Pending | Root `dist` and `agent/artifacts` require exact-list review |
| GH-004 | `frontend/official-preview` nested repository | Independent, clean, no remote, hosting config exists | Keep independent and add parent exclusion | Independent; submodule; monorepo | Approved for current phase | Do not convert or merge currently; exact ignore line still needs approval |
| GH-005 | Integration Pack case rename | Filesystem/index casing differs and content diff is 484/34 | Resolve content first, then perform separate case-only rename | Accept content then rename; revise content then rename; defer | Approved in principle, execution blocked | Do not describe current state as pure rename |
| GH-006 | Local private files | Root `.env`, generated local DBs, unreviewed `.env.example` | Keep private files local; review template before staging | Approve template; revise template; exclude template | Pending | Never output or stage secret values |
| GH-007 | First staging boundary | No staged paths; 1056 untracked files | C006 exact hygiene commit first, then C001-C005 separately | Approve order; revise order; defer | Pending | Never use broad staging |
| GH-008 | API/runtime/database exclusions | 16 modified tracked paths, one deletion, and many new engineering files | Exclude from first governance/knowledge cycle | Separate engineering review; include selected reviewed subset; defer | Founder Gate remains active | Database, import, safety, API, and deployment each need independent review |

Founder approval of a category does not approve every file within it. Each execution task must show the exact diff.

---

## 11. First Commit Safety Checklist

Before the first commit:

- [ ] Review `git status` and compare it with the approved baseline.
- [ ] Review the exact staging list.
- [ ] Confirm staged count was zero before starting.
- [ ] Verify `.env`, private keys, tokens, certificates, and local databases are absent from staging.
- [ ] Verify `.env.example` has completed value review if included.
- [ ] Verify `frontend/official-preview` remains an independent repository and no child path is staged by the parent.
- [ ] Verify generated dependencies and caches are absent.
- [ ] Verify Integration Pack content and case rename are not mixed accidentally.
- [ ] Verify no archive candidate or historical record was deleted.
- [ ] Run the validations required for that commit group.
- [ ] Review `git diff --cached --name-status`.
- [ ] Review the full `git diff --cached`.
- [ ] Confirm the commit message matches the staged scope.
- [ ] Commit only approved paths.
- [ ] Verify the resulting commit tree and validation result.
- [ ] Push only after separate Founder approval.

Recommended first commit:

```text
C006 Repository Hygiene
chore(repo): establish Git hygiene boundaries
```

If the exact `.gitignore` patch is not approved, stop. Do not compensate by staging broad directories manually.

After C006, prefer governance and knowledge foundation commits before any experimental application, runtime, API, database, frontend, or deployment change.

---

## 12. Risks

### 12.1 Broad Staging

`git add .` could include generated stores, private templates, nested repositories, experimental code, artifacts, and Founder-gated files.

Mitigation:

```text
explicit path staging only
```

### 12.2 Non-portable Ignore Behavior

Local or cache-generated ignore files may make this machine appear clean while another clone exposes generated files.

Mitigation:

```text
approved repository-level ignore rules
```

### 12.3 Nested Repository Capture

Recursive parent staging may create an unintended embedded-repository entry or blur ownership.

Mitigation:

```text
keep independent + parent exclusion + separate status check
```

### 12.4 Secret Leakage

An ignored `.env` does not protect secrets copied into templates, docs, fixtures, logs, screenshots, or staged blobs.

Mitigation:

```text
value review + staged blob scan + human approval
```

### 12.5 Case-only Rename Data Loss

The known case mismatch also includes a large content diff. Treating it as a pure rename may conceal or overwrite work.

Mitigation:

```text
content decision first + temporary-path rename second
```

### 12.6 Over-broad Artifact Ignore

Blanket `dist/`, `artifacts/`, or `*.log` rules may hide release packages, QA evidence, or historical validation records.

Mitigation:

```text
path-specific artifact policy and Founder classification
```

### 12.7 Mixing Foundations with Application Changes

Combining governance, knowledge, runtime, API, database, frontend, and deployment makes review and rollback unsafe.

Mitigation:

```text
C006 → C001 → C002 → C003 → C004 → C005 → C007+
```

### 12.8 Deleting Before Classification

Generated-looking files may include historical evidence or a release record.

Mitigation:

```text
no deletion; classify first; backup only after exact-list Founder review
```

---

## 13. Review Acceptance Criteria

This review is ready for Founder decision when:

- current Git counts and zero staged paths are recorded;
- current `.gitignore` coverage and portable gaps are explicit;
- generated, artifact, and private paths are classified without exposing secret values;
- nested frontend ownership and protection are explicit;
- the Integration Pack case mismatch is not misrepresented as a pure rename;
- include, exclude, and Founder Gate staging boundaries are separate;
- the first commit recommendation is governance/hygiene before application changes;
- no `.gitignore`, file, code, schema, entry, runtime, API, database, frontend, deployment, biomarker, Git index, branch, remote, or history change is performed by this review.
