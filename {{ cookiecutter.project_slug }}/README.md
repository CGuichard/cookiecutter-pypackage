# {{ cookiecutter.project_name }}

<!-- --8<-- [start:badges] -->

[![Language](https://img.shields.io/badge/language-python≥{{ cookiecutter.python_min }}-3776ab?style=flat-square)](https://www.python.org/)
![License](https://img.shields.io/badge/license-{{ cookiecutter.license.replace('-', '--') }}-yellow?style=flat-square)
[![Documentation](https://img.shields.io/badge/documentation-Material%20for%20MkDdocs-0a507a?style=flat-square)](https://{{ cookiecutter.git_user }}.github.io/{{ cookiecutter.project_slug }}/)
![Style](https://img.shields.io/badge/style-ruff-9a9a9a?style=flat-square)
![Lint](https://img.shields.io/badge/lint-ruff,%20mypy-brightgreen?style=flat-square)
![Security](https://img.shields.io/badge/security-bandit,%20pip--audit-purple?style=flat-square)
[![PyPI - Version](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}?style=flat-square)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![Tests](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.git_user }}/{{ cookiecutter.project_slug }}/check.yml?branch={{ cookiecutter.git_branch }}&label=Test)]({{ cookiecutter.__git_repo }}/actions/workflows/check.yml)
[![Coverage](https://raw.githubusercontent.com/{{ cookiecutter.git_user }}/{{ cookiecutter.project_slug }}/refs/heads/gh-tests-coverages/data/{{ cookiecutter.git_branch }}/badge.svg)](https://github.com/{{ cookiecutter.git_user }}/{{ cookiecutter.project_slug }}/actions/workflows/check.yml)

[Pull Request]({{ cookiecutter.__git_repo }}/pulls) **·**
[Bug Report]({{ cookiecutter.__git_repo }}/issues/new?template=bug_report.md) **·**
[Feature Request]({{ cookiecutter.__git_repo }}/issues/new?template=feature_request.md)

<!-- --8<-- [end:badges] -->

<!-- --8<-- [start:introduction] -->

Summary of the package purpose.

<!-- --8<-- [end:introduction] -->

## Table of Contents

- [Getting started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Getting started

### Installation

Install `{{ cookiecutter.project_slug }}` with pip:

```bash
pip install {{ cookiecutter.project_slug }}
```

Install `{{ cookiecutter.project_slug }}` with pip from source:

```bash
pip install git+{{ cookiecutter.__git_repo }}.git
# pip install git+{{ cookiecutter.__git_repo }}.git@<tag>
```

### Usage

<!-- --8<-- [start:usage] -->

Describe the usage of your package.

<!-- --8<-- [end:usage] -->

## Contributing

If you want to contribute to this project please check [CONTRIBUTING.md](CONTRIBUTING.md).

Everyone contributing to this project is expected to treat other people with respect,
and more generally to follow the guidelines articulated by our [Code of Conduct](./CODE_OF_CONDUCT.md).

## License

Copyright &copy; {{ cookiecutter.copyright_year }}, {{ cookiecutter.author }}

{{ cookiecutter.project_name }} is licensed under the {{ cookiecutter.license }} license. A copy of this license is provided in the [LICENSE](./LICENSE) file.

## Acknowledgements

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
from the project template [CGuichard/cookiecutter-pypackage](https://github.com/CGuichard/cookiecutter-pypackage).
