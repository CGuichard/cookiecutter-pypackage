# Changelog

All notable changes to this project will be documented in this file.

Versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html) (`<major>.<minor>.<patch>`).

## 3.0.1 (2025-11-23)

### Bug fixes

- Fix pre-commit ruff-check files selection, also run on tests

## 3.0.0 (2025-11-21)

This release reduces reliance on `tox` by moving the **lint** and **docs** tasks to standard
virtual-environment installation and command execution. The usage of `tox` in `pre-commit` has
been replaced with `uv`. The integration of `uv` has been expanded and is now used throughout
the Makefile.

### BREAKING CHANGES

- Upgrade dependencies and migrate project tasks management from tox to uv
- Rework dev dependencies, merge install-all into install-dev
- Docs: update CONTRIBUTING.md with tox removal and install-dev changes

### Enhancements

- CI: upgrade uv to 0.9.X
- CI: upgrade actions checkout, upload-artifact, download-artifact, insightsengineering/coverage-action, sigstore/gh-action-sigstore-python
- Format script watch.py

### Bug fixes

- CI: update lint dependencies with all extras (project.optional-dependencies)
- Tox: remove unused gh-actions table

## 2.2.1 (2025-10-06)

### Bug fixes

- Invalid syntax in check github workflow

## 2.2.0 (2025-10-06)

### Enhancements

- CI: add SBOM in check and release workflows

### Bug fixes

- CI: rename build artifact from 'py-dist' to 'build'
- CI: correct test execution and report
- CI: correct pip-audit and libyear calls

## 2.1.1 (2025-09-24)

### Bug fixes

- Remove lint ignore rules for '_cli.py' if no CLI generated
- Make: clean target remove .coverage

## 2.1.0 (2025-09-11)

### Enhancements

- Update dev dependencies
- Rename script get_latest_release_notes.py option --tag-msg as --plain-text
- Add choice between resolving project version from git tag or pyproject.toml field
- More explicit pyproject.toml commitizen version scheme
- More explicit pyproject.toml ruff ignore path
- Lint: change docstring style for multi-line summary
- Test: move pytest reporting from config to call command in tox
- Make: move docs-live target, add clean to pipeline

### Bug fixes

- Docs: update uv recommended version in CONTRIBUTING.md
- Make: remove test-report Makefile target

### Internal

- Change cookiecutter vars order

## 2.0.1 (2025-06-13)

### Bug fixes

- Remove markdown bold in git tag message by make release

## 2.0.0 (2025-06-09)

### BREAKING CHANGES

- Remove rich for CLI
- Remove cookiecutter development_status variable

### Enhancements

- Update click version
- Update development dependencies
- Move project.scripts in pyproject.toml
- Makefile: re-organize targets
- Makefile: add --all-extras to uv sync in install and install-dev
- Makefile: remove pre-commit-install, merge in setup
- CI: update GitHub Actions

### Bug fixes

- Project metadata name use project_slug instead of pkg_name
- Project metadata use license SPDX and license-files
- Clean pyproject.toml keywords and classifiers
- Update lint ignored rules for tests after updates
- Tests: update test_cli after click update
- Tests: add annotations
- Docs: fix help.md missing sentence end
- Docs: update mkdocs config

## 1.4.0 (2025-04-25)

### Enhancements

- Update dependencies
- Rename dependency group 'tests' to 'test'
- Lint use force-exclude, exit non-zero on format
- Ruff and mypy exclude scripts
- CI: rename test coverage branch and html dir

### Reverted

- Remove test dependencies from dev

## 1.3.1 (2025-03-19)

### Bug fixes

- Config mkdocstrings-python filters for members

## 1.3.0 (2025-03-18)

### Enhancements

- Update dependencies
- Update ruff ignore list for tests
- CI: update setup-uv actions

### Bug fixes

- Typo in CONTRIBUTING section 'Working on issues'
- Remove tox skip_missing_interpreters unneeded by usage of tox-uv
- CI: use requirements hashes to avoid pip resolution in audit job of check workflow

### Documentation

- Remove dropped input variable from README

### Internal

- Compute variables in cookiecutter.json for git repo path and origin
- Change git questions order

## 1.2.1 (2025-01-17)

### Bug fixes

- Remove CLI reference in mkdocs site if no CLI

## 1.2.0 (2025-01-17)

### Enhancements

- Quote pre-commit hooks rev
- Make email optional
- Make CLI creation optional
- Include group tests in group dev
- Separate precommit_push_ope as precommit_push_test and precommit_push_docs
- Update lint rules ignore for tests
- Update README.md license section
- Update CONTRIBUTING.md and remove git ignore section

### Documentation

- Fix input variables inconsistent style in README.md

### Internal

- Remove git_repo unused prompt from cookiecutter.json

## 1.1.0 (2025-01-01)

### Enhancements

- Remove cookiecutter version field
- Remove bpython for Makefile 'shell'
- Remove lint dependencies from dev dependency group
- Update coverage exclude lines config
- Use ruff instead of black for docs api reference code formatting
- Pin mypy version in lint dependencies

### Documentation

- Add comments on optional dependencies

## 1.0.0 (2024-12-24)

### Enhancements

- Simple package with `click` CLI
- `uv` package manager
- Build-backend with `hatchling`, resolve version with VCS tags
- Code linting and formatting with `ruff`
- Type checking with `mypy`
- Testing with `pytest` and `tox`
- Docs with **Material for MkDocs**, versioned with `mike`
- Git hooks with `pre-commit`
- Makefile to easily manage the project's lifecycle
- GitHub issue/merge requests templates
- GitHub action for docs, test, and release workflows
- Contributing guidelines, Code of Conduct.

### Documentation

- Add template README.md and LICENSE
