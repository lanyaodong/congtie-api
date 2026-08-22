# Registry Seed 001 C26 Final Verification Manifest v0.1

Status: Founder Review Pending / No Record Production Authorized

Validation date: 2026-08-22

## 1. Purpose

This manifest records the isolated, Schema-backed verification of the final Registry Seed 001 C26 artifacts. It is an authoring-governance record only and does not activate Registry records, assign numeric IDs, authorize runtime use, or authorize First Wave production.

## 2. Repository Baseline

- Repository: `/Users/lanyaodong/Documents/congtie-api`
- Branch: `main`
- HEAD: `f7d59ab476eca343d276ca297be9d60ab97dceee`
- origin/main: `f7d59ab476eca343d276ca297be9d60ab97dceee`
- Staging at validation start: empty

## 3. Final Artifact Manifest

| Artifact | Path | SHA-256 |
|---|---|---|
| Registry Schema | `schemas/biomarker_measurement_registry_schema_v0.1.json` | `a376b02e8cf50e95392287a8924919e57c6df6e37fa957830d4f1a60d1557aa7` |
| Candidate Ledger | `agent/knowledge_seed_v0/registry_seed_001_candidate_ledger.v0.1.json` | `b97f4b0e0aeaa4fae6e728c561e88019d3c9e0b34ce353c1cc2b27f5cd09bbe5` |
| Migration Ledger | `agent/knowledge_seed_v0/registry_seed_001_migration_ledger.v0.1.json` | `592408206315e2a404740c0fe5ca1f1ad574d407401d9df9c7f2062a45ad1a56` |
| Permanent Registry Validator | `agent/knowledge_seed_v0/scripts/validate_biomarker_measurement_registry.py` | `52ab54488fe8d018d008de3b45a46d16019445c20f36fa0641465c80ef867ff9` |

## 4. Validation Environment

- Temporary environment: `/tmp/congtie-registry-authoring-venv`
- Python: `3.9.6`
- Platform: `macOS-26.5.2-arm64-arm-64bit`
- jsonschema: `4.25.1`
- `Draft202012Validator`: import PASS
- `FormatChecker`: import PASS
- Repository runtime environment modified: no

## 5. Dependency Placement

- Authoring dependency file: `requirements-dev.txt`
- Exact dependency: `jsonschema[format]==4.25.1`
- Classification: development / authoring-governance tooling
- Runtime `requirements.txt` modified: no
- Runtime application dependency added: no

## 6. CI Authoring Validation Placement

- Workflow: `.github/workflows/ci.yml`
- Job: `registry-authoring-validation`
- Python: `3.9`
- Installs: `requirements-dev.txt` only
- Compiles the permanent Validator
- Validates the Draft 2020-12 Schema definition
- Runs semantic and Schema-backed self-tests
- Validates Candidate and Migration Ledgers
- Starts application or database: no
- Reads user health data or external services: no

## 7. Commands and Exit Codes

### Python compilation

```bash
PYTHONPYCACHEPREFIX=/tmp/congtie-registry-authoring-pycache \
/tmp/congtie-registry-authoring-venv/bin/python -m py_compile \
  agent/knowledge_seed_v0/scripts/validate_biomarker_measurement_registry.py
```

Result: PASS / exit `0`

### Schema definition

```bash
/tmp/congtie-registry-authoring-venv/bin/python \
  agent/knowledge_seed_v0/scripts/validate_biomarker_measurement_registry.py \
  --schema schemas/biomarker_measurement_registry_schema_v0.1.json
```

Output: `VALID: Draft 2020-12 Registry Schema`

Result: PASS / exit `0`

### Semantic and Schema-backed self-test

```bash
/tmp/congtie-registry-authoring-venv/bin/python \
  agent/knowledge_seed_v0/scripts/validate_biomarker_measurement_registry.py \
  --schema schemas/biomarker_measurement_registry_schema_v0.1.json \
  --self-test
```

```text
SELF_TEST_VALID_TOTAL=5
SELF_TEST_VALID_PASSED=5
SELF_TEST_VALID_FAILED=0
SELF_TEST_INVALID_TOTAL=12
SELF_TEST_INVALID_REJECTED=12
SELF_TEST_INVALID_ACCEPTED=0
SEMANTIC_SELF_TEST=PASS
SCHEMA_BACKED_SELF_TEST=PASS
DRAFT_2020_12_ENGINE=available
```

Result: PASS / exit `0`

### Candidate and Migration Ledgers

```bash
/tmp/congtie-registry-authoring-venv/bin/python \
  agent/knowledge_seed_v0/scripts/validate_biomarker_measurement_registry.py \
  --candidate-ledger agent/knowledge_seed_v0/registry_seed_001_candidate_ledger.v0.1.json \
  --migration-ledger agent/knowledge_seed_v0/registry_seed_001_migration_ledger.v0.1.json
```

Output: `VALID: Candidate Ledger + Migration Ledger`

Result: PASS / exit `0`

## 8. Registry Seed 001 Verification Results

- Core candidates: `53`
- Namespace counts: `BM 29 / ME 20 / SC 4 / QS 0`
- First Wave candidates: `12`
- Numeric Registry IDs assigned: `0`
- Active Registry records: `0`
- Migration rows: `169`
- Migration rows requiring review: `53`
- First Wave migration blockers: `0`
- Silent migration loss: `0`

## 9. Explicit Non-Authorizations

This verification does not authorize:

- Registry record creation or activation
- Numeric Registry ID assignment
- First Wave record production
- Runtime or retrieval enablement
- Database, API, index, Service Panel, or user-health storage implementation
- User observation processing
- Clinical thresholds, diagnosis, treatment, or intervention behavior
- Publication, commit, or push

## 10. Next Founder Gate

Founder and external ChatGPT review must confirm:

1. The four exact artifact SHAs in this manifest.
2. The isolated Schema-backed validation results.
3. The authoring dependency and independent CI placement.
4. Whether to authorize a controlled commit and push.

No First Wave records may be created automatically after this review.
