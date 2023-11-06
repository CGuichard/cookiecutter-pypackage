# Installation

:material-arrow-right-circle: Python ≥ {{ cookiecutter.python_min }} is required.

{{ cookiecutter.project_name }} is available as `{{ cookiecutter.project_slug }}` on PyPI.

## Pip from PyPI

You can install `{{ cookiecutter.project_slug }}` easily with `pip`:

<!-- termynal -->

```bash
$ pip install {{ cookiecutter.project_slug }}
---> 100%
Installed!
```

!!! tip
    The use of a virtual environment is greatly recommended :material-shield-check:.

## Pip from source

You can install from the code source with the repository:

<!-- termynal -->

```bash
$ pip install git+{{ cookiecutter.__git_repo }}.git@main
---> 100%
Installed from source!
```
