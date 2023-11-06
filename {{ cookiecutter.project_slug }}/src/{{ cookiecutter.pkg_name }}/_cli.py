"""Command-line interface."""

from importlib.metadata import metadata

import click
from rich import print as rprint
from rich import traceback


@click.group()
def main() -> None:
    """{{ cookiecutter.project_name }} CLI."""
    traceback.install(show_locals=True, suppress=[click])


@main.command()
def version() -> None:
    """Print version and exit."""
    m = metadata(__package__)
    pkg_name = m["Name"]
    pkg_version = m["Version"]
    pkg_summary = m["Summary"]
    rprint(f"[blue]{pkg_name}[/blue]: '{pkg_version}'")
    rprint(f"{pkg_summary}")
