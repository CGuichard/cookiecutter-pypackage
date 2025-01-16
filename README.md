# Cookiecutter - Python Package

> The last thing one knows in constructing a work is what to put first.
>
> \- Blaise Pascal

Creating a new project from scratch is always frustrating because you
have to setup for the hundredth time the same structure, often by copy
pasting another project and renaming things.

This cookiecutter is here to help you lay a base structure for all of your python
packages projects.

This template target is a **GitHub Open Source Python library/CLI**. I believe
with a few tweaks you could adapt it for other uses, and if asked it may be
included in the template depending on the maintenance workload implied.

## Features

- Python >= 3.10
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

## How to use it

### Install cookiecutter

I recommend using [uv](https://docs.astral.sh/uv/).

```bash
uv tool install cookiecutter
```

You could also use [pipx](https://pipx.pypa.io/).

```bash
pipx install cookiecutter
```

### Generate you project

Go to the parent directory of where you want to create your project and run:

```bash
cookiecutter <this-cookiecutter-path>
```

You may want to generate the project at another location:

```bash
cookiecutter <this-cookiecutter-path> -o <project-parent-dir>
```

The generator (cookiecutter) will ask you for some inputs.

The input variables, with their default values (some auto generated) are:

- `project_name`: name of the project
- `project_slug`: slug of the project, lower-case and hyphen-style
- `pkg_name`: python-friendly name of the package. By default, based on the project name
- `python_min`: minimum version of Python required, by default "3.10"
- `description`: project single-line description
- `author`: author firstname and lastname
- `email`: author email
- `version`: base version for the package, by default "0.0.0"
- `copyright_year`: year of the copyright, current year by default
- `license`: choice of open source license
- `development_status`: status of development for your project, for PyPI topic
- `cli`: whether to create CLI or not
- `precommit_push_ope`: Add pre-push checks in pre-commit.
- `git_user`: Git username
- `git_branch`: Git default branch (Examples: main, master)
- `git_init`: Whether to init the git repository or not

## License

Cookiecutter - Python Package is licensed under the MIT license.
A copy of this license is provided in the [LICENSE](LICENSE) file.
