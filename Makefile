HOST := 127.0.0.1
PORT := 5000
MODULE := main
CALLABLE := app

PYTHON := python
LINTER := flake8
TEST_RUNNER := pytest

SERVER := uvicorn
SERVER_FLAGS := --host $(HOST) --port $(PORT) --reload --header server:sharify

RM := rm -rf
TEMP_FILES := instance htmlcov .coverage .pytest_cache, *.egg-info

all: test lint run
run:
	APP_DEBUG=True $(SERVER) $(MODULE):$(CALLABLE) $(SERVER_FLAGS)

lint: lint-app lint-test
lint-app:
	$(LINTER) app --show-source --statistics
lint-test:
	$(LINTER) tests --show-source --statistics

test:
	$(PYTHON) -m $(TEST_RUNNER) -v

coverage:
	coverage run --source app -m $(TEST_RUNNER)
	coverage html
	coverage report

clean:
	$(RM) $(TEMP_FILES)
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

