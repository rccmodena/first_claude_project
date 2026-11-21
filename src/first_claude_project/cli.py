"""Command-line interface."""

import argparse
import sys
from collections.abc import Sequence

from first_claude_project import __version__
from first_claude_project.core import greet


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="first_claude_project", description="Example CLI.")
    parser.add_argument("--name", default="world", help="who to greet (default: %(default)s)")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI and return a process exit code."""
    args = build_parser().parse_args(argv)
    try:
        print(greet(args.name))
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
