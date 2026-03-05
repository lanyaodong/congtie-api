
Xiaoge Agent Protocol v0.1



Purpose

This protocol defines how external AI Agents integrate with the Xiaoge Longevity API.

Xiaoge is designed as a Longevity Intelligence Node that can be invoked by other Agents.

Supported integrations include:

OpenAI Agents

Claude Agents

Qwen Agents

Doubao Agents

Alipay Health Agents

any OpenAPI-compatible client



1 Agent Role Model

Agents interacting with Xiaoge must follow this architecture:

Agent
   │
   │ tool call
   ▼
Xiaoge API
   │
   │ database
   ▼
Longevity Knowledge + Biomarker Data


Agents never access the database directly.

All actions must go through the Xiaoge API.



2 Contract Hierarchy

The Xiaoge system defines strict integration contracts.

Order of authority:

1 OpenAPI Specification
spec/openapi.v0.1.yaml

2 Agent Tool Schema
spec/agent_tools.v0.1.json

3 Agent Protocol
spec/xiaoge_agent_protocol.v0.1.md


Agents must comply with all three.



3 Agent Capabilities

Agents may perform the following actions:

Capability	          Description
Create observation	  record biomarker or wearable data
Query observation	  retrieve historical biomarker data
Run analysis	          trigger longevity analysis
Query system state	  retrieve system health status

Agents must not:

modify schema
execute SQL
bypass API



4 Tool Invocation Model

Agents must use structured tool invocation.

Example:

tool: create_observation

payload:

{
  "user_id": "uuid",
  "biomarker_code": "rhr",
  "value_num": 58,
  "unit": "bpm",
  "measured_at": "2026-03-04T07:26:13Z"
}



5 Observation Data Model

Observation represents a single health measurement.

Core fields:

user_id
biomarker_code
value_num
value_text
value_json
unit
measured_at
observation_medium
accuracy_tier
freshness_state

Agents must supply:

user_id
biomarker_code
value
measured_at



6 Biomarker Code Registry

Biomarkers must be referenced by code, not free text.

Examples:

Code	          Meaning
rhr	          resting heart rate
hrv	          heart rate variability
vo2max	          aerobic capacity
glucose_fasting	  fasting glucose

Full registry defined in:

spec/biomarker_registry.v0.1.json



7 Error Handling

Agents must handle API errors.

Standard error format:

{
  "error": {
    "code": "invalid_request",
    "message": "biomarker_code not supported"
  }
}



8 Idempotency

Agents should avoid duplicate observation creation.

Recommended:

client_observation_id


Future API versions will support idempotent writes.




9 Security Model (v0.1)

Current version:

no authentication
local development

Future versions will support:

API Key
Agent Identity
Rate Limit




10 Recommended Agent Workflow

Example Agent workflow:

1 collect wearable data
2 call create_observation
3 store biomarker
4 request analysis
5 present insight to user




11 Future Protocol Extensions

Planned features:

agent authentication
agent identity registry
analysis execution
longevity scoring
multi-agent coordination




12 Philosophy

Xiaoge is designed as:

Longevity Intelligence Infrastructure

not just a standalone application.

Agents can:

read health state
write biomarker data
trigger longevity analysis

This allows Xiaoge to function as a shared longevity brain across the Agent ecosystem.



