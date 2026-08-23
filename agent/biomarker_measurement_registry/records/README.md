# Registry Records

Status: Founder Approved Storage and Naming Convention / Record Creation Not Authorized

This is the canonical directory for machine-readable `RegistryConcept` records. The directory is flat in v0.1.

Canonical filename pattern:

```text
<REGISTRY_ID>.<candidate_key>.json
```

The Registry ID uses an uppercase namespace and six digits; the candidate key uses lowercase snake_case. Filenames must not include schema version, record version, lifecycle, Pilot, body system, priority, or product grouping.

Each JSON file stores exactly one `RegistryConcept`; its profiles are embedded in `RegistryConcept.profiles[]`. Namespace, lifecycle, body-system, Pilot, and product-grouping subdirectories are prohibited.

This README does not authorize record creation.

This README does not hard-code a mutable record count. The canonical JSON files actually present in this directory are the authoritative record inventory.
