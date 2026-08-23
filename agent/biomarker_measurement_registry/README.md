# Biomarker and Measurement Registry

Status: Founder Approved Storage and Naming Convention / Record Creation Not Authorized

## Purpose

This directory is the canonical home for long-lived, machine-readable public Biomarker and Measurement Registry operational assets. It is separate from the Longevity Knowledge Base, User Health Information Library, user Observation storage, runtime indexes, databases, and Service Panels.

Historical Registry Seed governance and review documents remain in `agent/knowledge_seed_v0/` and are not migrated here.

## Object Boundaries

```text
RegistryConcept != MeasurementProfile != UserObservation != ServicePanel != KnowledgeEntry
```

One `RegistryConcept` is stored in one JSON file. Its `MeasurementProfile` objects remain embedded in `RegistryConcept.profiles[]`. Separate profile, source, mapping, or threshold files are not authorized without a later Schema and governance Gate.

## Directory Tree

```text
agent/biomarker_measurement_registry/
|-- README.md
|-- records/
|   `-- README.md
`-- id_allocations/
    `-- README.md
```

`records/` is a flat directory in v0.1. Namespace, lifecycle, body-system, Pilot, and product-grouping subdirectories are prohibited. Any future sharding requires a separate Founder governance Gate.

## Record Filename Pattern

Canonical record files use:

```text
<REGISTRY_ID>.<candidate_key>.json
```

- `REGISTRY_ID` is an uppercase namespace plus six digits.
- `candidate_key` is lowercase snake_case.
- The extension is `.json`.
- Both the Registry ID and candidate key are required.
- Schema version, record version, lifecycle, Pilot, body system, priority, and product grouping are prohibited in filenames.

## Version and Lifecycle

Record version is expressed by the JSON `version` field. Lifecycle is expressed by the JSON `lifecycle_status` field. Git preserves history. A concept keeps the same canonical path when its version or lifecycle changes.

## Numeric IDs

Numeric IDs are namespace-level, monotonic, non-semantic, and never reused. They do not encode body system, Pilot, priority, dependency, clinical meaning, lifecycle, or product grouping.

## Allocation Ledgers

Allocation ledgers live in `id_allocations/` and remain separate from Candidate Ledger planning. A proposed reservation becomes effective only after Founder approval of its exact SHA and a controlled Git commit. Candidate Ledger entries remain unchanged by allocation.

Legacy review coordinates are collision-reserved strings, not formal Registry IDs or effective reservations, and must not be reused as future formal IDs.

## Data and Runtime Boundary

This Registry stores public definitions only. It must not contain personal user data or observations. This convention does not authorize Registry record creation, publication, runtime or retrieval indexing, database/API work, Service Panels, Observation processing, or user-health storage.

## Operational State Source of Truth

Mutable operational counts are not hard-coded in this README.

- Registry record existence and count are derived from the canonical JSON files present in `records/`.
- Effective numeric-ID reservations are derived from committed allocation ledgers whose exact SHA is Founder-approved in a committed approval closeout.
- Active Registry records are derived from each canonical record's `lifecycle_status`.
- An allocation proposal, approval closeout, or README never creates a Registry record.
