SHELL := /bin/bash

# ---- Config (you can override on CLI) ----
DB_CONTAINER ?= xiaoge-postgres
DB_USER ?= postgres
DB_PASS ?= postgres
DB_NAME ?= xiaoge
DB_PORT ?= 5432

API_HOST ?= 127.0.0.1
API_PORT ?= 8000

SCHEMA_FILE ?= spec/xiaoge_v0_schema_snapshot.sql
VENV_ACTIVATE ?= .venv/bin/activate

DATABASE_URL ?= postgresql://$(DB_USER):$(DB_PASS)@$(API_HOST):$(DB_PORT)/$(DB_NAME)

.PHONY: help db-up db-wait schema api-up api-down test test-no-api db-down clean

help:
	@echo ""
	@echo "Targets:"
	@echo "  make db-up       # start postgres container"
	@echo "  make schema      # apply schema snapshot"
	@echo "  make api-up      # start uvicorn in background"
	@echo "  make api-down    # stop uvicorn"
	@echo "  make test        # db-up -> schema -> api-up -> pytest -> api-down"
	@echo "  make db-down     # stop/remove postgres container"
	@echo "  make clean       # remove temp pid/log"
	@echo ""
	@echo "Override example:"
	@echo "  make test API_PORT=8001"
	@echo ""

db-up:
	@echo "[db] starting container $(DB_CONTAINER) ..."
	@docker rm -f $(DB_CONTAINER) >/dev/null 2>&1 || true
	@docker run -d --name $(DB_CONTAINER) \
		-e POSTGRES_PASSWORD=$(DB_PASS) \
		-e POSTGRES_DB=$(DB_NAME) \
		-p $(DB_PORT):5432 \
		postgres:16 >/dev/null
	@$(MAKE) db-wait

db-wait:
	@echo "[db] waiting for postgres to be ready..."
	@for i in $$(seq 1 60); do \
		if docker exec $(DB_CONTAINER) pg_isready -U $(DB_USER) -d $(DB_NAME) >/dev/null 2>&1; then \
			echo "[db] ready"; exit 0; \
		fi; \
		sleep 1; \
	done; \
	echo "[db] NOT ready after 60s"; exit 1

schema:
	@test -f $(SCHEMA_FILE)
	@echo "[schema] applying $(SCHEMA_FILE)"
	@docker exec -i $(DB_CONTAINER) psql -U $(DB_USER) -d $(DB_NAME) -v ON_ERROR_STOP=1 < $(SCHEMA_FILE)
	@echo "[schema] done"

api-up:
	@echo "[api] starting uvicorn on http://$(API_HOST):$(API_PORT)"
	@. $(VENV_ACTIVATE) && \
		export DATABASE_URL="$(DATABASE_URL)" && \
		python3 -m uvicorn app.main:app --host $(API_HOST) --port $(API_PORT) \
		> /tmp/xiaoge-api-uvicorn.log 2>&1 & echo $$! > /tmp/xiaoge-api-uvicorn.pid
	@sleep 1
	@echo "[api] pid=$$(cat /tmp/xiaoge-api-uvicorn.pid) log=/tmp/xiaoge-api-uvicorn.log"

api-down:
	@if [ -f /tmp/xiaoge-api-uvicorn.pid ]; then \
		PID=$$(cat /tmp/xiaoge-api-uvicorn.pid); \
		echo "[api] stopping uvicorn pid=$$PID"; \
		kill $$PID >/dev/null 2>&1 || true; \
		rm -f /tmp/xiaoge-api-uvicorn.pid; \
	else \
		echo "[api] no pid file, skip"; \
	fi

test-no-api:
	@. $(VENV_ACTIVATE) && \
		export DATABASE_URL="$(DATABASE_URL)" && \
		python -m pytest -q

test: db-up schema api-up
	@set -e; \
	trap '$(MAKE) api-down' EXIT; \
	echo "[test] running pytest..."; \
	. $(VENV_ACTIVATE) && export DATABASE_URL="$(DATABASE_URL)" && python -m pytest -q; \
	echo "[test] OK"

db-down:
	@echo "[db] stopping/removing container $(DB_CONTAINER)"
	@docker rm -f $(DB_CONTAINER) >/dev/null 2>&1 || true

clean:
	@rm -f /tmp/xiaoge-api-uvicorn.pid /tmp/xiaoge-api-uvicorn.log
