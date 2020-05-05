"""Test cases for the main module."""

from pyproject_cookiecutter_test import __version__


def test_version() -> None:
    """Version test."""
    assert __version__ == "{{ cookiecutter.version }}"
