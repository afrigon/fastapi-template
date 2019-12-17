HOST := 127.0.0.1
PORT := 5000
MODULE := main
CALLABLE := app
LINTER := flake8
TEST_RUNNER := pytest

SERVER := uvicorn
SERVER_FLAGS := --host $(HOST) --port $(PORT) --reload --header server:sharify

RM := rm -rf
TEMP_FILES := instance htmlcov .coverage .pytest_cache

all: test lint run
run:
	APP_DEBUG=True $(SERVER) $(MODULE):$(CALLABLE) $(SERVER_FLAGS)

lint: lint-app lint-test
lint-app:
	$(LINTER) app
lint-test:
	$(LINTER) tests

test:
	python -m $(TEST_RUNNER) -v

coverage:
	coverage run -m $(TEST_RUNNER)
	coverage html
	coverage report

clean:
	$(RM) $(TEMP_FILES)
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

