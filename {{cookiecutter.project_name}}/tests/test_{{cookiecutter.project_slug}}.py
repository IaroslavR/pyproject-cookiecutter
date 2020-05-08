"""Test cases for the main module."""

from "{{ cookiecutter.project_slug }}" import __version__


def test_version() -> None:
    """Version test."""
    assert __version__ == "{{ cookiecutter.version }}"
