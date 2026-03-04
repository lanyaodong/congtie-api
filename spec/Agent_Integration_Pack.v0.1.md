
# Agent Integration Pack v0.1 (Xiaoge API)


This pack makes Xiaoge callable by other Agents (ChatGPT / Qwen / Doubao / etc.).
The only stable contract in v0.1 is:
- API endpoints
- `spec/agent_tools.v0.1.json` (tool surface)

## Quickstart (30 seconds)

### 1) Start local dev environment
```bash
make dev


2) Verify health

curl -s http://127.0.0.1:8000/health && echo
curl -s http://127.0.0.1:8000/health/db && echo


3) Run the agent smoke script

export XIAOGE_API_BASE_URL="http://127.0.0.1:8000"
python3 scripts/agent_smoke_v0_1.py



How an Agent should call Xiaoge


Tool spec location:

spec/agent_tools.v0.1.json


Required environment variables:

XIAOGE_API_BASE_URL (default http://127.0.0.1:8000)


Minimal call flow (recommended):

1.health_check

2.db_health_check

3.create_observation (one or more)

4.If 422: print body, fix payload, retry

5.If 500: run db_health_check and stop (infra issue)


Compatibility & Contract Rules:

1.Agents MUST NOT access database directly

2.Agents MUST NOT rely on DB schema as an external contract

3.Agents MUST ONLY call endpoints declared in spec/agent_tools.v0.1.json

4.If new endpoints are added, bump tool spec version (v0.2, v0.3...)


Notes

v0.1 has no auth. Add auth later (e.g., X-API-Key header).

measured_at should be RFC3339 with Z, e.g. 2026-03-03T06:32:46Z

