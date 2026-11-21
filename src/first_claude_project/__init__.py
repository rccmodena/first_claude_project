"""My Project: short description of what the project does."""

from importlib.metadata import PackageNotFoundError, version

from first_claude_project.core import greet

try:
    __version__ = version("first_claude_project")
except PackageNotFoundError:  # running from a source tree that is not installed
    __version__ = "0.0.0+unknown"

__all__ = ["__version__", "greet"]
