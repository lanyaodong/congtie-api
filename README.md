

# Xiaoge v0 API

Xiaoge API is designed for:

- Direct human use (FastAPI Swagger UI)
- Agent-to-Agent integration
- Machine-readable contract consumption

---

## 🚀 30-Second Quickstart

### Prerequisites
- Docker Desktop
- Python 3.9+
- `make`

### Run full local test (CI-equivalent)

```bash
cd ~/Documents/xiaoge-api
source .venv/bin/activate
make test


What happens:

1.Start local Postgres container

2.Apply schema snapshot

3.Start API (uvicorn)

4.Run pytest

5.Stop API automatically


Run development mode
make dev

Open:

Health: http://127.0.0.1:8000/health

DB Health: http://127.0.0.1:8000/health/db

Swagger Docs: http://127.0.0.1:8000/docs

OpenAPI JSON: http://127.0.0.1:8000/openapi.json

Stop:

make nuke


🔒 Architecture Rules (Agent Contract)

1.Agents MUST call tools defined in:

spec/agent_tools.v0.1.json

2.Direct database access is forbidden.

3.Business logic must flow through OpenAPI endpoints.

4.Database schema is NOT an external contract.

5.External integration contract:

/openapi.json

spec/agent_tools.v0.1.json


Breaking these rules breaks system integrity.


🤖 Agent-to-Agent Integration

Xiaoge exposes:

OpenAPI contract → /openapi.json

Swagger UI → /docs

Tool spec → spec/agent_tools.v0.1.json


Design goals:

Stable input/output schemas

Deterministic responses

No implicit DB coupling

Idempotent-safe operations

Versioned tool definitions


Future versioning pattern:
代码

v0.1
v0.2
v1.0


🧪 Agent Playbook

Prerequisites:

API running

Valid DATABASE_URL


Run:

pip install -r requirements.txt
python3 scripts/agent_playbook_v0_1.py


⚠️ Notes

macOS may show LibreSSL warning from urllib3 — safe to ignore.

Default DB URL:
代码

postgresql://postgres:postgres@127.0.0.1:5432/xiaoge


代码
---

# ✅ 三、验收步骤

复制执行：

```bash
cd ~/Documents/xiaoge-api
git status

make help
make test

make dev
# 另开终端：
curl -s http://127.0.0.1:8000/health && echo
curl -s http://127.0.0.1:8000/health/db && echo

make nuke
