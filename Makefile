SHELL := /bin/bash

# ---- Config (override on CLI) ----
DB_CONTAINER ?= xiaoge-postgres
DB_IMAGE ?= postgres:16
DB_USER ?= postgres
DB_PASS ?= postgres
DB_NAME ?= xiaoge
DB_PORT ?= 5432

API_HOST ?= 127.0.0.1
API_PORT ?= 8000

SCHEMA_FILE ?= spec/xiaoge_v0_schema_snapshot.sql
VENV_ACTIVATE ?= .venv/bin/activate

DATABASE_URL ?= postgresql://$(DB_USER):$(DB_PASS)@$(API_HOST):$(DB_PORT)/$(DB_NAME)

UVICORN_PID ?= /tmp/xiaoge-api-uvicorn.pid
UVICORN_LOG ?= /tmp/xiaoge-api-uvicorn.log

.PHONY: help db-up db-wait schema api-up api-down test test-no-api db-down clean dev nuke

# -------------------------
# Help
# -------------------------
help:
	@echo ""
	@echo "Targets:"
	@echo "  make test      # Full CI-equivalent run"
	@echo "  make dev       # Start DB + API (keep running)"
	@echo "  make db-up"
	@echo "  make schema"
	@echo "  make api-up"
	@echo "  make api-down"
	@echo "  make db-down"
	@echo "  make clean"
	@echo "  make nuke      # api-down + db-down + clean"
	@echo ""

# -------------------------
# Database
# -------------------------
db-up:
	@echo "[db] starting $(DB_CONTAINER)"
	@docker rm -f $(DB_CONTAINER) >/dev/null 2>&1 || true
	@docker run -d --name $(DB_CONTAINER) \
		-e POSTGRES_PASSWORD=$(DB_PASS) \
		-e POSTGRES_DB=$(DB_NAME) \
		-p $(DB_PORT):5432 \
		$(DB_IMAGE) >/dev/null
	@$(MAKE) db-wait

db-wait:
	@echo "[db] waiting..."
	@for i in $$(seq 1 60); do \
		if docker exec $(DB_CONTAINER) pg_isready -U $(DB_USER) -d $(DB_NAME) >/dev/null 2>&1; then \
			echo "[db] ready"; exit 0; \
		fi; \
		sleep 1; \
	done; \
	echo "[db] timeout"; exit 1

db-down:
	@docker rm -f $(DB_CONTAINER) >/dev/null 2>&1 || true
	@echo "[db] stopped"

# -------------------------
# Schema
# -------------------------
schema:
	@test -f $(SCHEMA_FILE)
	@echo "[schema] applying..."
	@docker exec -i $(DB_CONTAINER) psql -U $(DB_USER) -d $(DB_NAME) -v ON_ERROR_STOP=1 < $(SCHEMA_FILE)
	@echo "[schema] done"

# -------------------------
# API
# -------------------------
api-up:
	@echo "[api] starting..."
	@rm -f $(UVICORN_PID) $(UVICORN_LOG)
	@. $(VENV_ACTIVATE) && \
	export DATABASE_URL="$(DATABASE_URL)" && \
	python3 -m uvicorn app.main:app --host $(API_HOST) --port $(API_PORT) \
	> $(UVICORN_LOG) 2>&1 & echo $$! > $(UVICORN_PID)
	@for i in $$(seq 1 30); do \
		if curl -sf http://$(API_HOST):$(API_PORT)/health >/dev/null 2>&1; then \
			echo "[api] ready pid=$$(cat $(UVICORN_PID))"; exit 0; \
		fi; \
		sleep 1; \
	done; \
	echo "[api] failed to start"; exit 1

api-down:
	@if [ -f $(UVICORN_PID) ]; then \
		PID=$$(cat $(UVICORN_PID)); \
		kill $$PID >/dev/null 2>&1 || true; \
		rm -f $(UVICORN_PID); \
		echo "[api] stopped"; \
	else \
		echo "[api] no pid file"; \
	fi

# -------------------------
# Test
# -------------------------
test: db-up schema api-up
	@set -e; \
	trap '$(MAKE) api-down' EXIT; \
	echo "[test] running..."; \
	. $(VENV_ACTIVATE) && export DATABASE_URL="$(DATABASE_URL)" && python -m pytest -q; \
	echo "[test] OK"

test-no-api:
	@. $(VENV_ACTIVATE) && export DATABASE_URL="$(DATABASE_URL)" && python -m pytest -q

# -------------------------
# Dev
# -------------------------
dev: db-up schema api-up
	@echo ""
	@echo "[dev] API is up at http://$(API_HOST):$(API_PORT)"
	@echo "[dev] health:    curl -s http://$(API_HOST):$(API_PORT)/health && echo"
	@echo "[dev] health/db: curl -s http://$(API_HOST):$(API_PORT)/health/db && echo"
	@echo ""
	@echo "[dev] Stop API:  make api-down"
	@echo "[dev] Stop DB:   make db-down"

# -------------------------
# Cleanup
# -------------------------
clean:
	@rm -f $(UVICORN_PID) $(UVICORN_LOG)

nuke: api-down db-down clean
	@echo "[nuke] complete"

