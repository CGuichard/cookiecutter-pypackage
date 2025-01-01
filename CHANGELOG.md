# Changelog

All notable changes to this project will be documented in this file.

Versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html) (`<major>.<minor>.<patch>`).

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
