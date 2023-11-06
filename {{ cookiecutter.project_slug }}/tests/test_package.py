"""Basic package test."""


def test_package_import():
    """Import package."""
    import {{ cookiecutter.pkg_name }}  # noqa: F401


def test_package_version_is_defined():
    """Check imported package have __version__ defined."""
    import {{ cookiecutter.pkg_name }}

    assert {{ cookiecutter.pkg_name }}.__version__ != "undefined"
