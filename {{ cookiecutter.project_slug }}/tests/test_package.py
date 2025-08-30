"""Basic package test."""


def test_package_import() -> None:
    """Import package."""
    import {{ cookiecutter.pkg_name }}  # noqa: F401, PLC0415


def test_package_version_is_defined() -> None:
    """Check imported package have __version__ defined."""
    import {{ cookiecutter.pkg_name }}  # noqa: PLC0415

    assert {{ cookiecutter.pkg_name }}.__version__ != "undefined"
