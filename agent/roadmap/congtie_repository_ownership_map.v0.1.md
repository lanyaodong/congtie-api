# Congtie Repository Ownership Map v0.1

Version: v0.1  
Project: Congtie  
Status: Draft  
Owner: Founder  
Last Updated: 2026-08-11

---

## 1. Purpose

This document defines the initial repository ownership map for the Congtie AI-native development ecosystem.

It records:

- known repositories and local project boundaries;
- repository purpose and responsibility;
- lifecycle and ownership status;
- dependencies between deployable components;
- Git and deployment governance principles;
- future migration options;
- decisions reserved for the Founder.

This document does not merge, rename, move, delete, initialize, commit, push, or deploy any repository. It does not change Git remotes, `.gitignore`, code, API behavior, runtime behavior, databases, frontend implementation, hosting configuration, or biomarker JSON.

---

## 2. Congtie Repository Philosophy

Congtie follows an:

```text
AI-native multi-repository architecture
```

The working principles are:

1. Keep the core product independent from external adapters.
2. Keep deployment ownership clear for every deployable component.
3. Avoid premature monorepo consolidation.
4. Preserve Git history and repository provenance.
5. Prefer explicit contracts and boundaries over hidden coupling.
6. Keep secrets, generated dependencies, and environment-specific artifacts out of source control.
7. Treat nested repositories explicitly rather than staging them accidentally.
8. Use atomic commits with one reviewed purpose.
9. Human decides ownership; AI executes within approved boundaries.

Multi-repository architecture is not a requirement to create many repositories. A new repository should exist only when it has a clear owner, independent lifecycle, meaningful security or deployment boundary, and a stable relationship with the rest of the system.

---

## 3. Current Repository Map

| Repository | Location | GitHub URL | Purpose | Lifecycle | Ownership | Current Status | Decision Needed |
|---|---|---|---|---|---|---|---|
| `congtie-api` | `/Users/lanyaodong/Documents/congtie-api` | `git@github.com:lanyaodong/congtie-api.git` | Canonical core Congtie product platform | `active` | Core product, Founder-owned | Active development; canonical core repository | First large staging and push governance |
| `congtie-im-connector` | `/Users/lanyaodong/Documents/congtie-im-connector` | Current remote: `git@github.com:lanyaodong/xiaoge-im-connector.git` | External IM transport and connector layer | `prototype` | Recommended independent connector repository | Founder Gate; inactive historical prototype | Rename, API contract, identity, security, deployment |
| `frontend/official-preview` | `/Users/lanyaodong/Documents/congtie-api/frontend/official-preview` | No remote configured | Web/H5 preview and hosting-oriented frontend | `prototype` | Independent frontend/hosting component | `active-preview`; independent clean Git history; nested locally | Remote, deployment owner, long-term repository location |

Audit-time Git identity:

| Repository | Branch | HEAD | Remote Status |
|---|---|---|---|
| `congtie-api` | `main` | `71f3c2fde58f1655d5c3b86656b063b8784f76c8` | `origin` points to `congtie-api` |
| `congtie-im-connector` | `main` | `cd1b529eacdaecd4cf77288bc261c1604c1a03e6` | `origin` still points to historical repository name |
| `frontend/official-preview` | `main` | `9dafa395e9e0366ee8e15f825a17268f6f95a73c` | No remote configured |

These values describe the repositories at the time of this document. They are not release tags or approval states.

---

## 4. Repository Responsibility Definition

### 4.1 `congtie-api`

Purpose:

```text
Core Congtie product platform
```

Primary responsibilities:

- Congtie Agent runtime and harness.
- Longevity Information Library.
- User Health Information Library concepts and approved future implementation.
- Core API services and response contracts.
- Core product and orchestration logic.
- Safety and non-clinical boundaries.
- Knowledge retrieval foundation.
- Core schemas, validation, and integration contracts where approved.
- Core backend tests and release evidence.

Governance:

```text
Canonical core repository
```

The repository should define stable contracts for external adapters. It should not absorb every channel-specific SDK, credential, hosting concern, or experimental project by default.

Current status:

```text
active development
```

### 4.2 `congtie-im-connector`

Current repository identity:

```text
local folder: congtie-im-connector
GitHub remote: xiaoge-im-connector
```

Purpose:

```text
External IM connector layer
```

Potential responsibilities:

- Feishu connector.
- Telegram connector.
- Future WeChat connector.
- Message receiving and transport acknowledgment.
- Platform authentication and webhook verification.
- Message normalization.
- Stable identity handoff under an approved identity strategy.
- Retry, replay, idempotency, and outbound reply adapter behavior.
- Versioned communication with `congtie-api`.

Important boundary:

The connector should not contain:

- health reasoning;
- diagnosis or treatment logic;
- medication or dosage logic;
- longevity or disease scoring;
- disease risk calculation or prediction;
- user health interpretation;
- personalized supplement or medical protocols;
- bypasses around `congtie-api` safety and tool contracts.

Current status:

```text
prototype / Founder review required / inactive
```

Recommended initial ownership:

```text
Independent repository
```

Open decisions:

```text
xiaoge-im-connector
→ possible future rename to congtie-im-connector

versioned API contract with congtie-api
identity mapping strategy
platform security requirements
deployment ownership
```

No rename or runtime approval is implied by this map.

### 4.3 `frontend/official-preview`

Current state:

- Nested physically under `congtie-api/frontend/official-preview`.
- Has its own `.git` history and repository root.
- Current working tree is clean.
- No Git remote is configured.
- Contains `.openai/hosting.json` and a corresponding built copy under `dist/.openai/hosting.json`.
- Contains frontend package and hosting-related files.

Purpose:

```text
Frontend, H5, web preview, and hosting layer
```

Responsibility candidates:

- User-facing web/H5 preview.
- Frontend application shell and assets.
- Frontend-to-API binding.
- Hosting configuration and deployment artifacts.
- Preview-specific validation and release evidence.

Ownership options:

#### Option A: Keep Independent Repository

Pros:

- Preserves current independent history.
- Supports a separate frontend release and deployment lifecycle.
- Keeps hosting configuration ownership explicit.

Cons:

- Requires a remote, owner, release process, and documented API contract.
- Its physical nesting must be handled carefully by the parent repository.

#### Option B: Convert to Submodule

Pros:

- Makes the nested independent dependency explicit in the parent repository.
- Pins a reviewed frontend commit.

Cons:

- Adds submodule workflow and tooling complexity.
- Requires a stable remote first.

#### Option C: Merge into `congtie-api` Monorepo

Pros:

- Simpler atomic API/frontend changes.
- One repository workflow for a small team.

Cons:

- Loses the current independent boundary unless history migration is carefully designed.
- Couples frontend hosting and backend release lifecycles.
- Expands the already large core repository.

Current Founder-approved posture:

```text
Keep frontend/official-preview as an independent repository.
Do not convert it to a submodule or monorepo currently.
Review future deployment and ownership strategy separately.
```

Before the first parent repository push, generated folders must be excluded and hosting configuration must be documented. This document records that requirement but does not modify `.gitignore` or hosting files.

---

## 5. Ownership Model

### 5.1 Founder Ownership

The Founder is responsible for:

- repository boundaries;
- architecture and service boundaries;
- repository ownership assignments;
- repository creation, rename, merge, archive, or deletion decisions;
- remote and GitHub organization decisions;
- deployment ownership and production environment decisions;
- persistent identity and user-health data boundaries;
- production safety and clinical-boundary approval;
- final approval of cross-repository contracts.

### 5.2 AI Agent Responsibility

AI agents may perform approved work such as:

- implementation inside a defined repository boundary;
- documentation and architecture records;
- validation and test execution;
- maintenance and bounded migrations;
- repository audits;
- atomic commit preparation;
- contract compatibility checks;
- generating review packets for Founder decisions.

AI agents cannot, without explicit Founder approval:

- merge or split repositories;
- rename a repository or change a remote;
- change repository ownership;
- convert a nested repository into a submodule or monorepo component;
- alter deployment boundaries or production hosting;
- initialize a new production repository;
- delete or archive a repository;
- rewrite or discard Git history;
- introduce persistent identity, health-data, or clinical behavior;
- push unreviewed changes.

### 5.3 Component Ownership Principle

Every component must have one clearly identified primary owner even when several repositories contribute to one user flow.

```text
One user journey may cross repositories.
One responsibility must not have hidden owners.
```

---

## 6. Lifecycle Status

Allowed lifecycle values:

```text
active
prototype
experimental
archive_candidate
archived
```

Initial assignments:

| Repository | Lifecycle | Operational Note |
|---|---|---|
| `congtie-api` | `active` | Canonical core repository under active development |
| `congtie-im-connector` | `prototype` | Inactive pending Founder-gated engineering, safety, identity, and repository review |
| `frontend/official-preview` | `prototype` | Used as an active preview, but not yet assigned a final production ownership/deployment model |

`active-preview` is an operational description, not an additional lifecycle enum.

Lifecycle changes require an explicit review. A repository must not become an archive or deletion candidate merely because it is currently inactive.

---

## 7. Dependency Relationship

Conceptual ecosystem:

```text
                   Congtie Product Ecosystem

                              User
                               |
                  Frontend / IM Connectors
                               |
                          congtie-api
                               |
             ---------------------------------
             |                               |
 Longevity Information              User Health Context
        Library                           Library
```

Dependency direction:

```text
frontend/official-preview
→ versioned public API contract
→ congtie-api

congtie-im-connector
→ versioned connector/tool/API contract
→ congtie-api
```

Boundary rules:

1. External connectors communicate with core services through reviewed contracts.
2. External connectors do not own health reasoning or clinical behavior.
3. Frontend components render bounded API states and do not recreate backend safety logic.
4. `congtie-api` does not import channel credentials or hosting-specific state from adapters.
5. Libraries and user-private context remain logically distinct even when combined under approved runtime permissions.
6. Cross-repository changes require contract-version and compatibility review.

No repository should depend on another repository's unversioned internal file paths.

---

## 8. Git Governance Rules

### 8.1 Before First Push

Before the first large commit and push, each repository must have:

- a clear owner and purpose;
- a confirmed Git root;
- a reviewed remote destination;
- generated files and dependency caches excluded;
- secrets and local environment files excluded;
- nested repositories explicitly handled;
- hosting and deployment configuration documented;
- atomic commit boundaries;
- a reviewed working tree inventory;
- relevant tests or documentation validations recorded.

### 8.2 History Preservation

- Preserve independent Git histories.
- Do not copy a nested repository into the parent as ordinary files by accident.
- Do not rewrite history merely to simplify appearance.
- Use explicit migration plans for rename, split, merge, or submodule operations.
- Record old and new remotes during an approved migration.
- Do not force-push or discard unreviewed local work.

### 8.3 Atomic Commit Rules

Each commit should:

- have one clear purpose;
- avoid mixing cleanup, rename, runtime, frontend, deployment, and database work;
- exclude generated dependencies and unrelated artifacts;
- state tests or checks performed;
- preserve Founder-gated files until separately reviewed.

Repository ownership documentation should remain separate from implementation and deployment commits.

### 8.4 Prohibited Ungoverned Actions

Do not:

- blindly create a monorepo;
- merge experimental projects into the core repository;
- commit generated dependency folders;
- commit `.env`, credentials, tokens, keys, or certificates;
- stage through nested `.git` boundaries without an explicit decision;
- change remotes as part of unrelated cleanup;
- interpret a local folder name as proof of GitHub migration;
- treat an independent repository as an ordinary untracked parent directory.

---

## 9. Deployment Ownership

Every deployable component should have:

```yaml
owner:
repository:
environment:
domain:
deployment_method:
secret_owner:
rollback_owner:
release_approval:
```

Initial deployment map:

| Component | Repository | Current Deployment State | Ownership Decision |
|---|---|---|---|
| Core API and Agent services | `congtie-api` | Active development; production ownership not established by this document | Founder must approve environment and deployment owner |
| IM connector service | `congtie-im-connector` | Inactive prototype; not approved for deployment | Separate security, identity, API-contract, and operations review |
| Official web/H5 preview | `frontend/official-preview` | Hosting configuration exists; independent deployment model remains under review | Assign frontend/hosting owner, remote, environment, and domain |

Repositories must not be assumed to share one deployment lifecycle merely because they participate in the same product.

Production deployment configuration changes remain Founder-gated.

---

## 10. Future Repository Evolution

The following are possibilities, not approved repository creation tasks.

### 10.1 `congtie-api`

May remain the canonical core repository for Agent runtime, API, knowledge foundations, safety contracts, and approved user-context services.

It should remain focused enough that external platform SDKs and unrelated deployment concerns do not blur its ownership.

### 10.2 `congtie-im-connector`

Possible future roles:

- official connector service;
- multi-channel messaging gateway;
- MCP gateway, if separately designed and approved;
- A2A gateway, if separately designed and approved.

These roles should not be combined automatically. A gateway role requires its own contract, security model, and lifecycle review.

### 10.3 Frontend Repositories

Possible future direction:

```text
congtie-web
congtie-app
```

The existing `frontend/official-preview` history may inform a future migration, but no repository should be created or renamed until product, ownership, hosting, and deployment requirements are approved.

### 10.4 Other Possible Repositories

Potential future repositories may include:

```text
congtie-docs
congtie-research
congtie-sdk
```

They should be created only if ownership and lifecycle boundaries justify them. This document does not create or approve them.

---

## 11. Founder Decision Items

| Decision ID | Topic | Current State | Options | Recommendation | Founder Decision | Founder Notes |
|---|---|---|---|---|---|---|
| R001 | `congtie-im-connector` rename | Local folder uses Congtie name; remote uses historical name | Keep current remote temporarily; rename remote repository to `congtie-im-connector` | Rename later through a separate case-only migration after security and ownership review | Pending | Do not change remote in cleanup commits |
| R002 | `frontend/official-preview` ownership | Independent nested Git repository; no remote; hosting config exists | Independent repo; submodule; monorepo | Keep independent until product and deployment needs justify change | Approved: independent repository for current phase | Do not convert to submodule or monorepo currently |
| R003 | Future repository strategy | Three current repository/project boundaries | Multi-repo; monorepo | Continue AI-native multi-repository architecture with a high bar for new repos | Pending confirmation | Avoid premature consolidation |
| R004 | Connector API contract ownership | Historical connector calls old API naming and write path | Connector-owned contract; core-owned contract; jointly versioned contract | `congtie-api` owns the stable core contract; connector implements a pinned version | Pending | Include identity, error, replay, safety, and compatibility rules |
| R005 | Deployment ownership model | Components have different maturity and hosting state | Shared deployment owner; owner per component; external managed ownership | Assign owner per deployable component with Founder release approval | Pending | Record environment, domain, secrets, rollback, and release owner |
| R006 | `frontend/official-preview` remote | No remote configured | Create dedicated remote; keep local only temporarily; later migrate | Decide before production deployment, not through parent cleanup | Pending | Preserve current independent history |
| R007 | Nested repository handling in parent | Physically nested under `congtie-api` | Explicit exclusion; submodule; relocation; monorepo merge | Keep independent and explicitly exclude generated/nested contents before parent push | Partially approved | `.gitignore` change belongs to a separate task |
| R008 | Connector lifecycle activation | Prototype with known security and data-integrity gaps | Keep inactive; active remediation; archive | Keep inactive, then run separate engineering and safety review | Pending | No deployment or real-data testing before approval |

Blank or pending Founder decisions must not be inferred from recommendations.

---

## 12. Acceptance Criteria

This ownership map is acceptable when:

- all currently known repositories and project boundaries are listed;
- `congtie-api` is identified as the canonical core repository;
- `congtie-im-connector` is identified as an independent prototype and external adapter boundary;
- `frontend/official-preview` is identified as an independent nested repository with hosting concerns;
- repository responsibility and non-responsibility boundaries are explicit;
- lifecycle states are assigned consistently;
- dependency direction is documented;
- Git history preservation and nested repository handling are explicit;
- generated files and secrets are excluded by governance principle;
- deployment ownership is separated by component;
- Founder decisions are distinct from AI recommendations;
- AI agents cannot merge, rename, re-own, delete, archive, or redeploy repositories without Founder approval;
- no repository merge, rename, remote change, file move, deletion, commit, push, deployment, runtime, API, database, frontend, `.gitignore`, or biomarker JSON change is performed by this documentation task.

---

## 13. Current Recommendation

Use this initial ownership model:

```text
congtie-api
= canonical core repository

congtie-im-connector
= independent inactive prototype behind Founder Gate

frontend/official-preview
= independent frontend/hosting repository retained in its current phase
```

Before the first large parent repository staging operation, perform a separate `.gitignore` and nested-repository preparation task. That task should exclude generated folders, preserve independent histories, and document hosting ownership without merging repositories.
