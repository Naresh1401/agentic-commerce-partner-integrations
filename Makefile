.PHONY: setup run test

setup:
	@if [ -f backend/requirements.txt ]; then pip install -r backend/requirements.txt; fi
	@if [ -f mcp-server/requirements.txt ]; then pip install -r mcp-server/requirements.txt; fi
	@if [ -f agents/requirements.txt ]; then pip install -r agents/requirements.txt || true; fi
	@if [ -f frontend/package.json ]; then cd frontend && npm install; fi

run:
	cd partner-integrations && python3.11 retry_and_circuit_breaker_demo.py

test:
	python3.11 -m pytest tests

