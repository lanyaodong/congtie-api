# Congtie .gitignore Exact Patch Review v0.1

Version: v0.1
Project: Congtie
Status: Founder Review Pending
Owner: Founder
Review Date: 2026-08-11
Review Mode: Documentation-only exact patch review

---

## 1. Purpose

This document is the Founder review packet for a proposed update to the root `.gitignore` before the first large staging operation in `congtie-api`.

It records the current file exactly, proposes a line-level patch, explains the impact of each candidate, and separates low-risk additions from unresolved or high-risk choices.

This document does not apply the patch. It does not modify `.gitignore`, source code, knowledge entries, schemas, validators, runtime, API, frontend, database, deployment, or biomarker JSON. It does not stage, commit, push, move, rename, or delete any file.

---

## 2. Current `.gitignore` State

Repository-relative path:

```text
.gitignore
```

Absolute path:

```text
/Users/lanyaodong/Documents/congtie-api/.gitignore
```

Observed file metadata:

```text
size_bytes: 41
last_modified: 2026-02-11 16:37:42 +0800
sha256: 59429504f47d366d1fce795f11bc33a3a5c9ce301981b15c5f92185e4f0b6f71
```

Current rules, reproduced in full and in current order:

```gitignore
.env
.venv/
__pycache__/
*.pyc
.DS_Store
```

Read-only Git checks found no working-tree or staged diff for `.gitignore` at review time.

---

## 3. Git Hygiene Principles

1. Ignore reproducible dependencies, caches, build state, and machine-local files.
2. Keep source code, specifications, schemas, knowledge assets, validators, and reviewed documentation visible to Git.
3. Do not use broad patterns when a path may contain governed evidence, release material, source-side build logic, or historical records.
4. Do not treat `.gitignore` as a secret scanner. Every staged blob still requires review before push.
5. Preserve independent repository history and make nested repository ownership explicit.
6. Prefer exact staging over `git add .` during the first commit sequence.
7. Do not hide Founder-gated material merely to simplify `git status`.
8. Apply only lines explicitly approved by the Founder.

---

## 4. Existing Ignore Rules Analysis

| Existing rule | What it protects | Remains correct | Risk or limitation |
|---|---|---|---|
| `.env` | Files named exactly `.env` at repository levels | Yes | Does not protect `.env.local`, `.env.production`, or other `.env.*` variants |
| `.venv/` | Python virtual environment directories | Yes | Low risk; generated dependencies should remain outside Git |
| `__pycache__/` | Python bytecode cache directories | Yes | Low risk; caches are reproducible |
| `*.pyc` | Compiled Python bytecode files | Yes | Low risk; generated from Python source |
| `.DS_Store` | macOS Finder metadata | Yes | Low risk; machine-local metadata |

No existing rule is proposed for removal.

The current root rules do not explicitly protect `.pnpm-store/`, `.pytest_cache/`, `node_modules/`, `.vinext/`, `.next/`, `coverage/`, `.wrangler/`, environment variants, root distribution output, or the nested frontend repository boundary.

---

## 5. Proposed Exact Patch

### 5.1 Recommended Base Patch

The following is the exact proposed patch for Founder review. It is not applied by this document.

```diff
diff --git a/.gitignore b/.gitignore
--- a/.gitignore
+++ b/.gitignore
@@
 .env
+.env.*
+!.env.example
 .venv/
+.pnpm-store/
 __pycache__/
 *.pyc
+.pytest_cache/
+node_modules/
+.vinext/
+.next/
+coverage/
 .DS_Store
```

No removals proposed.

If approved exactly as shown, the resulting file would be:

```gitignore
.env
.env.*
!.env.example
.venv/
.pnpm-store/
__pycache__/
*.pyc
.pytest_cache/
node_modules/
.vinext/
.next/
coverage/
.DS_Store
```

### 5.2 Explicitly Excluded From the Base Patch

The following rules are not included because they require separate decisions:

```gitignore
logs/
.wrangler/
dist/
agent/artifacts/
frontend/official-preview/
```

No blanket key, certificate, database, log-file, build-directory, or artifact rule is proposed in the base patch.

---

## 6. Ignore Candidate Classification

Classification meanings:

```text
ADD
= recommended for the exact base patch, pending Founder approval

KEEP_VISIBLE
= do not ignore now; keep visible to review and exact staging

FOUNDER_GATE
= do not add until the stated ownership or content decision is approved
```

### 6.1 Candidate A: `.pnpm-store/`

Recommendation: `ADD`.

Observed state:

- The root `.pnpm-store/` exists.
- It contains package-manager database state, including database sidecar files.
- It is generated dependency cache, not source code.

Impact: prevents local pnpm store state from entering a parent repository commit.

### 6.2 Candidate B: `.pytest_cache/`

Recommendation: `ADD`.

Observed state:

- The root `.pytest_cache/` exists.
- It currently relies partly on a cache-generated internal `.gitignore`.
- The cache is reproducible from test execution.

Impact: makes protection explicit and portable at repository level.

### 6.3 Candidate C: `node_modules/`

Recommendation: `ADD`.

Observed state:

- No parent-root `node_modules/` was found.
- The independent `frontend/official-preview` repository has its own `node_modules/` and already ignores it locally.
- The parent repository contains frontend-related work and may encounter Node dependencies in future tasks.

Impact: protects generated dependency trees wherever they appear in the parent repository. It does not, by itself, resolve ownership of the whole nested frontend repository.

### 6.4 Candidate D: `.vinext/`

Recommendation: `ADD`.

Observed state:

- No parent-root `.vinext/` was found.
- A generated `.vinext/` exists in the independent frontend repository and is already ignored there.

Impact: provides portable protection if the parent repository later runs compatible frontend tooling.

### 6.5 Candidate E: `.next/`

Recommendation: `ADD`.

Observed state:

- No parent-root `.next/` was found.
- A generated `.next/` exists in the independent frontend repository and is already ignored there.

Impact: prevents generated Next.js build/cache state from being staged in the parent repository.

### 6.6 Candidate F: `coverage/`

Recommendation: `ADD`.

Observed state:

- No parent-root `coverage/` directory was found.
- The independent frontend repository already ignores its local coverage output.

Impact: excludes reproducible test coverage output while leaving source and tests visible.

### 6.7 Candidate G: `logs/`

Recommendation: `FOUNDER_GATE`; not in the base patch.

Observed state:

- No application-level parent `logs/` directory was found.
- Historical validation and execution evidence includes log files under governed artifact paths.

Risk: a broad directory rule may hide future logs that are intended as review evidence. If runtime logs later need protection, prefer a scoped local-runtime path over a blanket repository-wide rule.

### 6.8 Candidate H: `.wrangler/`

Recommendation: `FOUNDER_GATE`; not in the base patch.

Observed state:

- No parent-root `.wrangler/` was found.
- The independent frontend repository has local Cloudflare tooling state under `.wrangler/` and already ignores it.

Risk: the generated local state should not be committed, but Cloudflare hosting configuration is separate source material and must remain visible in the frontend repository. Add a parent rule only if parent-owned Cloudflare tooling is confirmed.

### 6.9 Candidate I: `dist/`

Recommendation: `KEEP_VISIBLE` behind `FOUNDER_GATE`; do not ignore automatically.

Observed state:

- Root `dist/` exists.
- It contains `first_external_trial_package`, documentation, reference material, a mock runner, scenario/contract JSON, and a zip package.
- The independent frontend repository also has generated hosting output under its own `dist/`, already ignored by its own rules.

Risk: a blanket `dist/` rule would combine two different categories: a potentially governed root release/trial package and reproducible frontend output. The root package requires an explicit keep, archive, regenerate, or exclude decision before any ignore rule.

Classification: `FOUNDER_GATE`, with current treatment `KEEP_VISIBLE`.

### 6.10 Candidate J: `agent/artifacts/`

Recommendation: `KEEP_VISIBLE` behind `FOUNDER_GATE`; do not ignore automatically.

Observed content includes:

- frontend browser and submit-flow screenshots;
- internal alpha and Founder trial evidence;
- staging dry-run material;
- historical XSB request, response, caller-path, and validation records.

Risk: these are not one homogeneous generated cache. A blanket ignore rule could hide validation evidence and historical records that repository policy requires preserving.

Classification: `FOUNDER_GATE`, with future options `KEEP`, `ARCHIVE`, or an exact-list artifact policy.

### 6.11 Candidate K: `frontend/official-preview/`

Recommendation: `FOUNDER_GATE`; not in the base patch.

Observed state:

```text
independent Git repository: true
branch: main
HEAD: 9dafa395e9e0366ee8e15f825a17268f6f95a73c
working tree: clean
remote: none configured
parent status: untracked frontend/official-preview/
```

The current ownership direction is to keep this frontend as an independent repository, not a submodule or monorepo component. The exact parent exclusion line remains a separate approval item.

Benefits of adding the rule later:

- prevents accidental staging of the nested repository from the parent;
- preserves independent history and lifecycle;
- keeps parent staging boundaries clear.

Risks:

- the parent status would no longer remind reviewers that the nested repository exists;
- frontend changes could be missed unless the workflow always checks the nested repository separately;
- no remote or final deployment owner is configured yet.

Classification: `FOUNDER_GATE` for the exact ignore line, despite the independent-repository ownership direction already being approved.

### 6.12 Candidate L: `.env.example` Handling

Recommendation: add `.env.*` together with `!.env.example` in the base patch, pending Founder approval and a separate content review before staging `.env.example`.

Observed state:

- Root `.env` exists and is ignored.
- Root `.env.example` exists and is currently untracked.
- No values are reproduced in this review.

Impact:

- `.env.*` protects common local environment variants.
- `!.env.example` keeps the template visible to Git.
- The exception does not approve or stage `.env.example`; its contents must be reviewed before inclusion in a commit.

---

## 7. Risk Analysis

### 7.1 Secret and Private File Review

Only filenames and categories were inspected. Secret values were not output.

| Category | Current protection | Gap | Decision posture |
|---|---|---|---|
| `.env` | Protected by existing rule | None for exact `.env` name | Keep existing rule |
| `.env.*` variants | Not protected | Local variants could appear in status | Add `.env.*` if approved |
| `.env.example` | Visible and untracked | Could contain non-template values | Keep visible via exception; review contents before staging |
| Credential/token-named files | No blanket rule | Filename-only rules cannot guarantee safety | No matching filenames found outside pruned dependency/cache paths; staged-blob review still required |
| Private keys and certificates | No root blanket rule | Future files could be exposed | No matching key/certificate files found outside pruned dependency/cache paths; decide exact patterns separately |

`.gitignore` cannot protect secrets already tracked, stored under unexpected names, or embedded inside source files. A pre-push staged-content review remains mandatory.

### 7.2 Broad-pattern Risk

Rules such as `dist/`, `logs/`, `*.db`, `*.sqlite`, `build/`, or whole artifact trees can hide governed material. They should be scoped only after exact content ownership is known.

### 7.3 Nested-repository Risk

Leaving `frontend/official-preview/` visible creates accidental parent-staging risk. Ignoring it creates discoverability risk. If the exact exclusion is approved, the operating checklist must always run a separate status check inside the frontend repository.

### 7.4 First Commit Impact

After approval of the base patch, expected protected categories are:

```text
environment files and variants
Python virtual environments and bytecode
Python test cache
pnpm package-store cache
Node dependency trees
Vinext and Next.js generated state
coverage output
macOS metadata
```

Expected to remain visible and eligible for exact review:

```text
source code
specifications
schemas
canonical knowledge entries
validators and scripts
documentation
root dist trial/release material
agent artifacts and historical evidence
the nested frontend repository boundary
.env.example
```

Visible does not mean approved for staging.

---

## 8. Founder Decision Table

| ID | Rule | Recommendation | Risk | Founder Decision | Notes |
|---|---|---|---|---|---|
| GH-001-A | `.pnpm-store/` | ADD | Low; generated package cache | Pending | Present at root |
| GH-001-B | `.pytest_cache/` | ADD | Low; reproducible test cache | Pending | Root rule should not rely on cache self-ignore |
| GH-001-C | `node_modules/` | ADD | Low; generated dependencies | Pending | Nested frontend already has its own rule |
| GH-001-D | `.vinext/` | ADD | Low; generated frontend state | Pending | Currently observed only in nested frontend |
| GH-001-E | `.next/` | ADD | Low; generated frontend state | Pending | Currently observed only in nested frontend |
| GH-001-F | `coverage/` | ADD | Low; test output | Pending | No parent-root directory currently found |
| GH-001-G | `logs/` | FOUNDER_GATE | Medium; may hide governed evidence | Pending | Prefer scoped runtime log path if later needed |
| GH-001-H | `.wrangler/` | FOUNDER_GATE | Medium; local state and hosting ownership must remain distinct | Pending | Nested frontend already ignores local state |
| GH-001-I | `dist/` | KEEP_VISIBLE / FOUNDER_GATE | High; root trial package may be governed | Pending | Do not combine root release material with nested generated output |
| GH-001-J | `agent/artifacts/` | KEEP_VISIBLE / FOUNDER_GATE | High; includes historical and QA evidence | Pending | Requires exact keep/archive policy |
| GH-001-K | `frontend/official-preview/` | FOUNDER_GATE | High; affects independent repository visibility | Pending | Independent ownership approved; exact parent rule still pending |
| GH-001-L | `.env.*` plus `!.env.example` | ADD WITH CONTENT GATE | Medium; template must be reviewed before staging | Pending | Ignore variants, keep template visible |

Founder may approve the base patch as a whole or approve individual lines. No blank or pending decision is interpreted as approval.

---

## 9. Post-Approval Execution Plan

After explicit Founder approval:

1. Codex applies only the approved `.gitignore` lines as one narrow patch.
2. Run:

```bash
git diff -- .gitignore
```

3. Review:

```bash
git status --short
```

4. Probe representative paths with `git check-ignore -v` and confirm each ignored path maps to the intended rule.
5. Verify that source code, schemas, knowledge entries, validators, documentation, root release material, and governed artifacts have not disappeared unintentionally from status.
6. If `frontend/official-preview/` is approved for parent exclusion, run a separate status check inside that repository and document its hosting ownership.
7. Review `.env.example` contents without exposing values before considering it for staging.
8. Founder approves the exact staging boundary.

No automatic staging or commit follows approval of this review document.

---

## 10. Review Validation

Required checks for this documentation-only step:

```text
review document exists
review document has no trailing whitespace
.gitignore SHA-256 remains unchanged
.gitignore has no working-tree or staged diff
no staged paths were introduced
no git add, commit, or push was executed
```

This document remains a proposal until the Founder records decisions for GH-001-A through GH-001-L.

