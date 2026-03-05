
# IM Connector Minimal Spec v0.1 (Xiaoge)


目标：让任意 IM 渠道（WeChat / Feishu / DingTalk / Telegram / Slack / WhatsApp…）通过一个“连接器服务”(IM Connector)接入 Xiaoge API，
实现“用户在 IM 里发一句话 -> Xiaoge 返回结果 -> 回写 IM”。

本 spec 只定义最小可用版本 (v0.1)：
- 不追求多模态/富交互/复杂权限
- 优先保证：可接入、可观测、可幂等、可扩展、可被其它 Agent 调用


---

## 0. Terms

- Channel: IM 平台（微信/飞书/钉钉/Telegram...）
- IM Connector: 你写/部署的连接器服务，接收 IM Webhook 事件并调用 Xiaoge API
- Xiaoge API: 你的 FastAPI 服务（OpenAPI + agent tools）
- Session: IM 中的“会话上下文”（群/私聊/线程）
- Turn: 一次用户输入（消息）+ Xiaoge 输出（回复）


---

## 1. High-level Flow

1) Channel -> IM Connector: incoming message event
2) IM Connector -> Xiaoge API: normalize + call
3) Xiaoge API -> IM Connector: response payload
4) IM Connector -> Channel: post reply message

关键原则：
- 幂等：同一条 IM 消息重复投递，不会创建重复 observation / 重复写入
- 可观测：每次请求都有 trace_id，可在日志里串起来
- 解耦：IM Connector 不直连数据库，只调用 Xiaoge API（符合你的“DB 非 contract”原则）


---

## 2. Security & Auth

### 2.1 Channel -> Connector (Inbound)
每个渠道有自己的签名校验方式。连接器必须支持：
- 签名验证（HMAC / RSA / platform token）
- 时间戳防重放（例如 5 分钟窗口）
- 原始 request body 保留用于验签
- 失败返回 401/403

### 2.2 Connector -> Xiaoge API (Outbound)
v0.1 最小要求（二选一，推荐 A）：

A) Static Bearer Token（最简单可用）
- Connector 请求头：`Authorization: Bearer <XIAOGE_CONNECTOR_TOKEN>`
- Xiaoge API 校验 token（env：`XIAOGE_CONNECTOR_TOKEN`）

B) mTLS（更安全，v0.2 再做）
- Connector 使用 client cert


---

## 3. Connector Responsibilities (MUST)

### 3.1 Normalize Input
把不同渠道的消息统一成标准结构 `NormalizedMessage`：

```json
{
  "channel": "feishu|dingtalk|wechat|telegram|slack|custom",
  "channel_message_id": "string",
  "channel_event_id": "string|null",
  "session": {
    "type": "dm|group|channel|thread",
    "session_id": "string",
    "thread_id": "string|null"
  },
  "sender": {
    "channel_user_id": "string",
    "display_name": "string|null"
  },
  "content": {
    "type": "text",
    "text": "string"
  },
  "timestamps": {
    "sent_at": "RFC3339 string",
    "received_at": "RFC3339 string"
  },
  "routing": {
    "tenant_id": "string|null",
    "app_id": "string|null"
  },
  "trace": {
    "trace_id": "uuid|string",
    "idempotency_key": "string"
  }
}


3.2 Idempotency

idempotency_key MUST stable for same message

推荐：<channel>:<channel_message_id>；若渠道只有 event_id，用 event_id

Connector 调用 Xiaoge API 时必须带：

Header Idempotency-Key: <idempotency_key>


3.3 Rate Limiting / Retry

渠道回调可能重试/并发；Connector 必须能重复处理而不重复写入

对 Xiaoge API 失败：

5xx / 网络错误：退避重试（例如 1s/2s/4s，最多 3 次）

4xx（除 429）：不重试，直接回写错误提示

429：按 Retry-After 重试（最多 3 次）


3.4 Observability

每次 Turn 必须记录（日志即可，v0.2 再接 tracing）：

trace_id

channel + session_id + channel_message_id

outbound request path + status

latency

error detail（不要打印 token / 密码）



4. Xiaoge API Contract for IM (v0.1)

IM Connector 不需要“理解长寿业务”，它只做转发。
因此 Xiaoge API 对 IM 最小只需要 1 个“统一入口”：


4.1 Endpoint: POST /im/turns

Purpose: 处理一次 IM Turn（用户一句话）

Auth: Bearer token

Idempotency: Header Idempotency-Key required

Request:
{
  "channel": "feishu",
  "session": {
    "type": "group",
    "session_id": "oc_123",
    "thread_id": null
  },
  "sender": {
    "channel_user_id": "u_456",
    "display_name": "Alice"
  },
  "input": {
    "text": "我今天静息心率 58，要不要记录？"
  },
  "context": {
    "locale": "zh-CN",
    "timezone": "Asia/Shanghai"
  },
  "trace": {
    "trace_id": "3f7b...",
    "channel_message_id": "m_789"
  }
}


Response (success):
{
  "trace_id": "3f7b...",
  "reply": {
    "type": "text",
    "text": "已记录：rhr=58 bpm（fresh / standard）。"
  },
  "actions": [
    {
      "type": "create_observation",
      "status": "ok",
      "observation_id": "uuid"
    }
  ]
}

Response (user-facing error):
{
  "trace_id": "3f7b...",
  "reply": {
    "type": "text",
    "text": "我这边数据库暂时不可用，请稍后再试。"
  },
  "error": {
    "code": "DB_UNAVAILABLE",
    "detail": "connection refused"
  }
}

注：如果你现在还没实现 /im/turns，v0.1 也可以先让 Connector 调 agent tool（例如“create_observation”等）；
但长远建议保留 /im/turns 作为“面向 IM 的稳定入口”，内部再路由到 agent tools。



5. Minimal Connector Output Types

v0.1 只要求支持：

text reply（纯文本）

可选（v0.2）：

markdown

cards（飞书卡片/钉钉卡片）

quick replies（按钮）

file/image



6. Mapping & Identity

6.1 User Mapping

Connector 必须提供一种“IM 用户 -> Xiaoge user_id”的映射方式。

v0.1 简化方案（二选一）：

A) Single shared demo user_id（最快跑通）

所有 IM 用户映射到同一个 user_id（开发阶段）

用 env：XIAOGE_DEMO_USER_ID

B) Deterministic mapping（无需存储）

user_id = UUIDv5(namespace, channel + ":" + channel_user_id)

namespace 固定写在 Connector 配置中

优点：可重复、无需 DB；缺点：无法合并不同渠道同一个人

真正的账号系统（OAuth/手机号绑定/企业 SSO）放 v0.2+。



7. Acceptance Checklist (v0.1)

7.1 Connector 验收

 能接收渠道 webhook（至少 1 个渠道）

 验签通过（或 dev 模式跳过，但必须可配置）

 同一条消息重复投递，Xiaoge 不会重复写入（幂等）

 Connector 日志能看到 trace_id 串联 inbound/outbound

 失败时能回写用户可读错误文本


7.2 Xiaoge API 验收

 /health OK

 /health/db OK

 /im/turns 返回 text reply（或替代路线：agent tool + smoke script）

 Idempotency-Key 生效（重复请求不重复 create）



8. Threat Model Notes (v0.1)

Token 泄漏：Connector token 必须只在 server-side env，不能在客户端

重放攻击：渠道验签 + timestamp window

PII：日志避免打印原文（可只打印 hash / length）

租户隔离：v0.1 可以不做，但结构预留 tenant_id



9. Next (v0.2+)

支持富消息（cards/buttons）

多租户、企业组织、权限

统一用户账号与跨渠道身份合并

端到端 tracing（OpenTelemetry）

Job queue（异步长任务）

Tool-call streaming / partial responses

