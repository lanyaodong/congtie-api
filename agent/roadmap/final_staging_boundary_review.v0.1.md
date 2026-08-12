# Congtie Final Staging Boundary Review v0.1

Version: v0.1
Project: Congtie
Status: Founder Review Pending
Owner: Founder
Review Date: 2026-08-11
Review Mode: Documentation-only staging boundary review

---

## 1. Purpose

This document is the final Founder approval packet before the first controlled staging operation in `congtie-api`.

It defines:

- the exact proposed file boundary for Commit 001;
- the isolated boundary for Commit 002;
- later engineering and repository groups;
- files and directories that must remain unstaged;
- tracked modifications and deletion risks;
- Founder decisions required before any `git add` command.

This review does not stage, commit, push, modify, move, rename, restore, or delete any file other than creating this review document itself.

---

## 2. Current Repository State

Audit-time state before creation of this review document:

```text
repository_root: /Users/lanyaodong/Documents/congtie-api
branch: main
HEAD: 71f3c2fde58f1655d5c3b86656b063b8784f76c8
remote_fetch: git@github.com:lanyaodong/congtie-api.git
remote_push: git@github.com:lanyaodong/congtie-api.git
staged_count: 0
modified_tracked_count: 17
deleted_tracked_count: 1
untracked_file_count: 1054
```

The branch status was:

```text
## main...origin/main
```

No staged path existed. No commit or push was performed by this review. The current HEAD remained unchanged throughout the read-only audit.

The working tree is intentionally not clean. Existing application, specification, test, documentation, artifact, frontend, and database changes must not be interpreted as approved merely because they are present.

---

## 3. Staging Principles

Congtie first-commit staging follows:

```text
explicit paths
+ atomic commits
+ Founder approval
```

Rules:

1. Never use `git add .`.
2. Never stage an entire broad directory merely because some child files are approved.
3. Never stage unknown generated files, dependency caches, or local tooling state.
4. Never include secrets or private environment values.
5. Never mix governance and knowledge infrastructure with risky application, API, runtime, database, deployment, or safety changes.
6. Never stage a nested repository accidentally.
7. Each commit must have one understandable purpose and an exact manifest.
8. Review the staged diff independently from the working-tree diff.
9. A file being visible in `git status` does not grant staging approval.
10. A content approval does not automatically grant runtime, retrieval, publication, deployment, or push approval.

---

## 4. Commit 001 Boundary Proposal

Proposed purpose:

```text
Congtie Foundation Governance and Knowledge Infrastructure
```

Proposed commit message:

```text
docs: establish Congtie governance and knowledge infrastructure
```

### 4.1 Exact Proposed Manifest

Commit 001 proposes exactly 21 files.

#### Repository Governance

```text
.gitignore
agent/roadmap/congtie_repository_ownership_map.v0.1.md
agent/roadmap/post_rename_repository_simplification_audit_and_atomic_commit_plan_2026_08_11.v0.1.md
agent/roadmap/git_hygiene_preparation_review.v0.1.md
agent/roadmap/gitignore_exact_patch_review.v0.1.md
agent/roadmap/final_staging_boundary_review.v0.1.md
```

#### Longevity Information Library Foundation

```text
agent/longevity_knowledge_base/README.md
agent/longevity_knowledge_base/templates/longevity_knowledge_item_template.v0.1.md
agent/longevity_knowledge_base/schemas/evidence_source_type_enum.v0.1.md
agent/longevity_knowledge_base/schemas/evidence_source_type_alignment_notes.v0.1.md
agent/longevity_knowledge_base/scripts/validate_longevity_knowledge_item.py
agent/longevity_knowledge_item_schema.v0.1.md
agent/knowledge_seed_v0/longevity_information_library_architecture.v0.1.md
agent/knowledge_seed_v0/longevity_information_library_architecture_patch_for_taxonomy.v0.1.md
agent/knowledge_seed_v0/longevity_topic_taxonomy.v0.1.md
agent/knowledge_seed_v0/evidence_grading_framework.v0.1.md
```

The final four `agent/knowledge_seed_v0/` files are included to make the proposed infrastructure dependency-complete:

- the knowledge base README references the architecture, architecture patch, and taxonomy;
- the conceptual knowledge item schema references the architecture, taxonomy, and evidence framework;
- the validator resolves the taxonomy from `agent/knowledge_seed_v0/longevity_topic_taxonomy.v0.1.md` when no root-level taxonomy exists.

Without these dependencies, Commit 001 would contain active documentation and validator references to files absent from an independent checkout of that commit.

#### User Health Information Foundation

```text
agent/user_health_information_library_mvp_spec.v0.1.md
agent/user_health_context_schema.v0.1.md
```

These are conceptual documentation only. They do not create a database, API, persistence model, or production user data flow.

#### Release Planning

```text
agent/roadmap/v0_release_plan_2026_09.md
agent/roadmap/v0_release_task_backlog_2026_09.md
agent/roadmap/longevity_knowledge_batch_001_plan.v0.1.md
```

### 4.2 Explicitly Not Included in Commit 001

Commit 001 does not include:

- the first official knowledge entry;
- `.env.example`;
- root `README.md` or `Makefile`;
- any other file under `agent/` or `agent/roadmap/`;
- any `.gitkeep` file;
- any application, API, runtime, test, database, schema implementation, frontend, deployment, connector, artifact, or distribution file;
- any existing tracked modification except `.gitignore`.

The exact manifest must be used. Directory-wide staging such as `git add agent/` is prohibited.

---

## 5. Commit 002 Boundary Proposal

Proposed purpose:

```text
First Official Knowledge Asset
```

Proposed commit message:

```text
docs: add approved healthspan knowledge entry
```

Exact proposed manifest:

```text
agent/longevity_knowledge_base/entries/knowledge/KN-T0101-0001.healthspan-definition.md
```

Verified gate state:

```yaml
entry_id: KN-T0101-0001
status: approved
runtime_enabled: false
retrieval_enabled: false
```

Additional verification:

```text
validator_result: VALID
validator_exit_code: 0
sha256: 5d5562e24109bea582de67fb52cb1aa76f8319ee35d5ff239c300762ff0f63c9
```

Commit 002 must contain only this entry. Content approval does not enable publication, runtime use, or retrieval.

---

## 6. Later Commit Boundary Proposal

### 6.1 Application Engineering

Separate later review and commit groups should cover:

```text
Makefile
app/
app/agent_runtime/
app/api/
app/core/
app/middleware/
app/schemas/
app/services/
pytest.ini
scripts used by runtime or tests
tests/
```

These changes affect imports, API routing, middleware, configuration, runtime behavior, test execution, and compatibility. They require an engineering diff review and focused test plan before staging.

### 6.2 API, Tool, Protocol, and Safety Specifications

Separate later review should cover:

```text
spec/Agent_Integration_Pack.v0.1.md
spec/agent_tools.v0.1.json
spec/api_behavior_spec.v0.1.md
spec/im_connector_min_spec.v0.1.md
spec/openai_tools.v0.1.json
spec/openapi.v0.1.yaml
spec/system_rules.v0.1.md
spec/xiaoge_agent_protocol.v0.1.md
other untracked spec files
```

The current tracked diffs materially change endpoints, schemas, system states, recommendations, tool contracts, connector behavior, and safety semantics. They must not be bundled into a documentation-foundation commit.

### 6.3 Database

Separate database review should cover:

```text
spec/xiaoge_v0_schema_snapshot.sql
database migrations
database-backed tests
persistent model changes
```

The current SQL snapshot is a substantial schema replacement, not a documentation-only rename.

### 6.4 Frontend

Separate frontend ownership and deployment review should cover:

```text
frontend/local-app/
frontend/shared-state-support/
frontend/official-preview/
frontend-related tests and Makefile targets
```

`frontend/official-preview` is an independent nested Git repository. It is currently clean on branch `main`, has no configured remote, and must not be staged by the parent repository.

### 6.5 Deployment

Separate deployment review should cover:

```text
hosting configuration
cloud configuration
service files
Nginx configuration
environment templates
deployment scripts and reports
```

No deployment lifecycle is implied by Commit 001 or Commit 002.

### 6.6 Experimental Projects and Connectors

Separate repository and architecture review should cover:

```text
congtie-im-connector
IM connector implementations
MCP/A2A gateway experiments
prototypes and experimental integrations
```

External connectors must not be merged into the core staging boundary without an explicit repository and API contract decision.

---

## 7. Excluded Files and Reasons

### 7.1 Generated and Dependency State

The following are excluded from all proposed commits:

```text
.pnpm-store/
.pytest_cache/
node_modules/
.vinext/
.next/
coverage/
```

They are dependency caches, test caches, generated build state, or generated output. Current `.gitignore` rules protect them. No generated file is deleted by this policy.

### 7.2 Local Private Files

Excluded:

```text
.env
.env.*
```

The current ignore exception makes `.env.example` visible, but visibility is not content approval. `.env.example` remains outside Commit 001 pending a value-safe template review and explicit Founder staging decision. No secret value was output during this audit.

### 7.3 Nested Repository

Excluded:

```text
frontend/official-preview/
```

Reason:

- independent Git history;
- separate ownership and deployment lifecycle;
- no current remote;
- parent staging could create an accidental gitlink or ambiguous ownership state.

### 7.4 Ambiguous Artifacts

Keep visible but exclude pending Founder decision:

```text
dist/
agent/artifacts/
artifacts/
```

`dist/` contains an external trial package, reference material, validation logs, JSON contracts, a mock runner, and a zip package. `agent/artifacts/` contains screenshots, QA evidence, trial records, debug records, and historical XSB artifacts. These are not homogeneous caches.

Possible future decisions:

```text
KEEP in a governed artifact commit
ARCHIVE with an exact manifest
REGENERATE from source
EXCLUDE selected generated copies
```

No blanket ignore, deletion, or staging decision is granted by this review.

### 7.5 Other Untracked Files

All untracked files outside the 21-file Commit 001 manifest and the one-file Commit 002 manifest remain excluded. This includes `AGENTS.md`, other `agent/` documents, new application modules, runtime files, schemas, scripts, specifications, tests, frontend files, deployment files, and artifacts.

---

## 8. Modified Tracked Files Review

Current tracked modifications are individually classified below.

| Path | Observed change summary | Proposed commit | Risk | Founder Gate |
|---|---|---|---|---|
| `.gitignore` | Adds eight approved environment, cache, dependency, frontend-build, and coverage rules | Commit 001 | Low | Already approved; final manifest approval still required |
| `Makefile` | Adds an M2 frontend contract-test target and updates help/phony targets | Later application/frontend engineering | Medium | Yes |
| `README.md` | Changes project branding and local repository paths; current diff includes noncanonical display spelling | Later repository identity/documentation cleanup | Medium | Yes |
| `app/main.py` | Moves configuration to settings, installs middleware/router, and removes the inline health route | Later API/runtime engineering | High | Yes |
| `scripts/agent_playbook_v0_1.py` | Adds environment-variable alias behavior | Later compatibility tooling | Medium | Yes |
| `scripts/agent_smoke_v0_1.py` | Adds environment aliases and changes diagnostic output | Later compatibility/testing tooling | Medium | Yes |
| `spec/Agent_Integration_Pack.v0.1.md` | Large integration-pack rewrite, 484 additions and 34 deletions; known case-path/content review remains | Later contract documentation | High | Yes |
| `spec/agent_tools.v0.1.json` | Large external tool-contract rewrite, including schema and enum changes | Later tool-contract commit | High | Yes |
| `spec/api_behavior_spec.v0.1.md` | Rewrites endpoint, state, recommendation, and agent behavior semantics | Later API/safety specification | High | Yes |
| `spec/im_connector_min_spec.v0.1.md` | Large connector architecture and identity/delivery behavior rewrite | Later connector specification | High | Yes |
| `spec/openai_tools.v0.1.json` | Reshapes OpenAI-compatible tool definitions and required inputs | Later tool-contract commit | High | Yes |
| `spec/openapi.v0.1.yaml` | Changes server, auth, endpoint, schema, state, and API contract definitions | Later API contract commit | High | Yes |
| `spec/system_rules.v0.1.md` | Rewrites state enums, core biomarker logic, placeholders, and recommendation behavior | Later safety/system-rules review | High | Yes |
| `spec/xiaoge_agent_protocol.v0.1.md` | Rewrites agent capabilities, contract hierarchy, and integration behavior | Later protocol review | High | Yes |
| `spec/xiaoge_v0_schema_snapshot.sql` | Replaces enum, table, and seed-data structures | Separate database commit | Critical | Independent database review required |
| `tests/test_e2e_metabolic.py` | Adds external-server/database/e2e markers and environment-gated skipping | Later test-infrastructure commit | Medium | Yes |
| `tests/test_smoke_health.py` | Adds environment aliases, markers, and external-server/database gating | Later test-infrastructure commit | Medium | Yes |

None of these tracked modifications, other than `.gitignore`, belongs in Commit 001 or Commit 002.

---

## 9. Deleted File Review

Actual deleted tracked path:

```text
app/__init__.py
```

The task brief referred to `app/init.py`; the repository status shows the double-underscore package file `app/__init__.py`.

Observed state:

```text
working_tree_status: deleted
HEAD_blob_size: 0 bytes
staged: false
```

Although the tracked file was empty, accepting its deletion may affect package discovery, import behavior, tooling compatibility, and deployment assumptions.

Recommendation:

1. Exclude the deletion from Commit 001 and Commit 002.
2. Review package/import behavior independently.
3. Run focused application and packaging tests.
4. Decide explicitly whether to restore the package marker or accept its deletion in a later engineering commit.

This review neither restores nor accepts the deletion.

---

## 10. Founder Gate Items

Founder approval is required before:

- staging the Commit 001 exact manifest;
- staging the Commit 002 knowledge asset;
- handling `.env.example` as a source-controlled template;
- staging any application, API, runtime, specification, test, or database change;
- accepting or restoring `app/__init__.py` deletion;
- staging any frontend or nested repository path;
- deciding whether `dist/`, `agent/artifacts/`, or `artifacts/` should be kept, archived, regenerated, or excluded;
- executing the first commit or push.

---

## 11. Staging Safety Checklist

Before the first `git add`:

- [ ] Founder approves STAGE-001 through STAGE-008 decisions.
- [ ] Commit 001 manifest contains exactly the approved paths.
- [ ] No directory-wide `git add` command is used.
- [ ] Staged count is zero before execution.
- [ ] `.env` and environment variants remain ignored.
- [ ] `.env.example` remains unstaged unless separately approved.
- [ ] Generated caches and dependency directories remain ignored.
- [ ] `frontend/official-preview` remains unstaged and is checked separately.
- [ ] `dist/`, `agent/artifacts/`, and `artifacts/` remain unstaged.
- [ ] Application, API, runtime, database, test, deployment, and biomarker files remain unstaged.
- [ ] `app/__init__.py` deletion remains unstaged.
- [ ] `git diff --cached --name-status` exactly matches the approved manifest.
- [ ] `git diff --cached --check` reports no whitespace errors.
- [ ] Staged content is scanned for secrets and private values.
- [ ] Founder reviews the full staged diff before commit.

---

## 12. Proposed Git Commands

The following commands document a possible future process. They are not executed by this task.

### 12.1 Commit 001 Staging

```bash
git status --short

git add -- \
  .gitignore \
  agent/roadmap/congtie_repository_ownership_map.v0.1.md \
  agent/roadmap/post_rename_repository_simplification_audit_and_atomic_commit_plan_2026_08_11.v0.1.md \
  agent/roadmap/git_hygiene_preparation_review.v0.1.md \
  agent/roadmap/gitignore_exact_patch_review.v0.1.md \
  agent/roadmap/final_staging_boundary_review.v0.1.md \
  agent/longevity_knowledge_base/README.md \
  agent/longevity_knowledge_base/templates/longevity_knowledge_item_template.v0.1.md \
  agent/longevity_knowledge_base/schemas/evidence_source_type_enum.v0.1.md \
  agent/longevity_knowledge_base/schemas/evidence_source_type_alignment_notes.v0.1.md \
  agent/longevity_knowledge_base/scripts/validate_longevity_knowledge_item.py \
  agent/longevity_knowledge_item_schema.v0.1.md \
  agent/knowledge_seed_v0/longevity_information_library_architecture.v0.1.md \
  agent/knowledge_seed_v0/longevity_information_library_architecture_patch_for_taxonomy.v0.1.md \
  agent/knowledge_seed_v0/longevity_topic_taxonomy.v0.1.md \
  agent/knowledge_seed_v0/evidence_grading_framework.v0.1.md \
  agent/user_health_information_library_mvp_spec.v0.1.md \
  agent/user_health_context_schema.v0.1.md \
  agent/roadmap/v0_release_plan_2026_09.md \
  agent/roadmap/v0_release_task_backlog_2026_09.md \
  agent/roadmap/longevity_knowledge_batch_001_plan.v0.1.md

git diff --cached --name-status
git diff --cached --check
git diff --cached
```

Only after Founder staged-diff approval:

```bash
git commit -m "docs: establish Congtie governance and knowledge infrastructure"
git status --short
```

### 12.2 Commit 002 Staging

```bash
python3 agent/longevity_knowledge_base/scripts/validate_longevity_knowledge_item.py \
  agent/longevity_knowledge_base/entries/knowledge/KN-T0101-0001.healthspan-definition.md

git add -- \
  agent/longevity_knowledge_base/entries/knowledge/KN-T0101-0001.healthspan-definition.md

git diff --cached --name-status
git diff --cached --check
git diff --cached
```

Only after Founder staged-diff approval:

```bash
git commit -m "docs: add approved healthspan knowledge entry"
git status --short
```

### 12.3 Push

Only after separate Founder push approval:

```bash
git push origin main
```

No command in Sections 12.1 through 12.3 is executed by this review task.

---

## 13. Founder Decision Table

| ID | Decision | Recommendation | Founder Decision | Notes |
|---|---|---|---|---|
| STAGE-001 | Approve Commit 001 exact 21-file scope | Approve only after reviewing the dependency-complete manifest | Pending | No directory-wide staging |
| STAGE-002 | Approve Commit 002 one-file knowledge asset scope | Keep isolated; preserve `approved`, runtime off, retrieval off | Pending | Validator currently returns `VALID` |
| STAGE-003 | Exclude nested `frontend/official-preview` | Exclude from parent Commit 001 and Commit 002 | Pending | Independent clean repository; no remote |
| STAGE-004 | Exclude API/runtime/database changes | Exclude and require separate engineering/database reviews | Pending | Includes contracts, safety semantics, and SQL |
| STAGE-005 | Handle `dist/` | Keep visible and unstaged pending exact artifact decision | Pending | Contains trial/release package material |
| STAGE-006 | Handle `agent/artifacts/` and root `artifacts/` | Keep visible and unstaged pending keep/archive policy | Pending | Historical and QA evidence |
| STAGE-007 | Handle `app/__init__.py` deletion | Exclude; review import/package behavior separately | Pending | Empty HEAD blob does not eliminate compatibility risk |
| STAGE-008 | Approve first staging command execution | Approve only after all preceding boundaries are accepted | Pending | Approval to stage is not approval to commit or push |
| STAGE-009 | Handle `.env.example` | Keep unstaged until content-safe template review | Pending | Ignore exception is not content approval |

No pending cell is interpreted as approval.

---

## 14. Acceptance and Validation Conditions

This review is ready for Founder decision when:

- the review document exists and has no trailing whitespace;
- Commit 001 has an exact dependency-complete manifest;
- Commit 002 contains only the approved healthspan entry;
- all existing tracked modifications are individually classified;
- the deleted package file is explicitly excluded;
- generated, private, nested, ambiguous artifact, application, API, runtime, database, test, deployment, and frontend paths remain unstaged;
- no `git add`, commit, or push has occurred;
- staged count remains zero after document creation.

