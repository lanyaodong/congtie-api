

#!/usr/bin/env python3
import os
import sys
import json
from datetime import datetime, timezone
import uuid

import requests


def die(msg: str, code: int = 1) -> None:
    print(msg, file=sys.stderr)
    sys.exit(code)


def pretty(x) -> str:
    try:
        return json.dumps(x, ensure_ascii=False, indent=2)
    except Exception:
        return str(x)


def main() -> int:
    base_url = os.getenv("XIAOGE_API_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
    print(f"[config] XIAOGE_API_BASE_URL={base_url}")

    # 1) /health
    r = requests.get(f"{base_url}/health", timeout=10)
    print(f"[health] status={r.status_code} body={r.text}")
    if r.status_code != 200:
        die("[health] failed")

    # 2) /health/db
    r = requests.get(f"{base_url}/health/db", timeout=10)
    try:
        data = r.json()
    except Exception:
        data = {"raw": r.text}
    print(f"[health/db] status={r.status_code}\n{pretty(data)}")
    if r.status_code != 200 or data.get("ok") is not True:
        die("[health/db] failed - DB not ready or DATABASE_URL misconfigured")

    # 3) POST /observations
    user_id = "11111111-1111-1111-1111-111111111111"  # same as your e2e tests
    now_z = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    payload = {
        "user_id": user_id,
        "biomarker_code": "rhr",
        "data_source_id": None,
        "observation_medium": "device",
        "sample_type": None,
        "sample_method": "wearable",
        "sampling_context": {"state": "resting"},
        "value_num": 58,
        "value_text": None,
        "value_json": {},
        "unit": "bpm",
        "measured_at": now_z,
        "freshness_state": "fresh",
        "accuracy_tier": "standard",
    }

    r = requests.post(f"{base_url}/observations", json=payload, timeout=10)
    try:
        body = r.json()
    except Exception:
        body = r.text

    print(f"[create_observation] status={r.status_code}\n{pretty(body)}")

    if r.status_code in (200, 201):
        print("[ok] agent smoke passed")
        return 0

    # Helpful diagnostics
    if r.status_code == 422:
        die("[create_observation] 422 validation error. Fix payload according to response body.")
    if r.status_code >= 500:
        die("[create_observation] server error. Check DB health and server logs.")
    die("[create_observation] unexpected status")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
