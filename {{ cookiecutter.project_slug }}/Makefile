##@ Project's Makefile, with utility commands for the project development lifecycle.

MAKEFLAGS += --no-print-directory

UV=uv
PYTHON=$(UV) run python
TOX=$(UV) run tox -qq
PRE_COMMIT=$(UV) run pre-commit
COMMITIZEN=$(UV) run cz

.PHONY: default help pipeline setup clean pre-commit
.PHONY: release shell build install install-dev install-all
.PHONY: lint lint-watch test test-report docs docs-live docs-serve

# ======================================================= #

default: help

pipeline: build lint test docs ## Run build, lint, test, docs.

setup: install-dev ## Run 'install-dev' and install pre-commit hooks.
	@$(PRE_COMMIT) install --install-hooks

clean: ## Clean temporary files, like python '__pycache__', dist build, docs output, tests reports.
	@find src tests -regex "^.*\(__pycache__\|\.py[co]\)$$" -delete
	@rm -rf dist tests-reports docs/build .*_cache

pre-commit: ## Run all pre-commit hooks.
	@$(PRE_COMMIT) run --all-files
	@$(PRE_COMMIT) run --hook-stage pre-push --all-files

release: ## Bump version, create tag and update 'CHANGELOG.md'.
	@$(COMMITIZEN) bump --yes --changelog
	@./scripts/update_latest_tag_msg.sh

shell: ## Open Python shell.
	@$(PYTHON)

build: ## Build wheel and tar.gz in 'dist/'.
	@$(UV) build

install: ## Install in the python venv.
	@$(UV) sync --all-extras --no-dev --no-editable

install-dev: ## Install in editable mode inside the python venv with dev group dependencies.
	@$(UV) sync --all-extras

install-all: ## Install in editable mode inside the python venv with all extras and groups dependencies.
	@$(UV) sync --all-extras --all-groups

lint: ## Lint python source code.
	@$(TOX) -e lint

lint-watch: ## Watch for src Python files changes and run `make lint`.
	@$(UV) run --script scripts/watch.py --clear --filter "*.py" src "make lint"

test: ## Invoke tox to run automated tests.
	@$(TOX)

test-report: ## Start http server to serve the test report and coverage.
	@printf "Test report: http://localhost:9000\n"
	@printf "Coverage report: http://localhost:9000/coverage-html\n"
	@$(PYTHON) -m http.server -b 0.0.0.0 -d tests-reports 9000 > /dev/null

docs: ## Build the docs.
	@$(TOX) -e docs

docs-live: ## Live-edition of the docs.
	@$(TOX) -e docs -- serve

docs-serve: docs ## Start http server to serve the docs.
	@printf "Docs: http://localhost:8000\n"
	@$(PYTHON) -m http.server -b 0.0.0.0 -d docs/build/html 8000 > /dev/null

# ======================================================= #

HELP_COLUMN=11
help: ## Show this help.
	@printf "\033[1m################\n#     Help     #\n################\033[0m\n"
	@awk 'BEGIN {FS = ":.*##@"; printf "\n"} /^##@/ { printf "%s\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n\n  make \033[36m<target>\033[0m\n\n"} /^[$$()% a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-$(HELP_COLUMN)s\033[0m %s\n", $$1, $$2 } ' $(MAKEFILE_LIST)
	@printf "\n"
