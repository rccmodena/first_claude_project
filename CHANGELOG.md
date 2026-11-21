# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- This changelog. (#5)

## [0.2.0] - 2026-11-21

### Added

- `--greet` CLI option to customize the greeting word (default `Hello`). (#1)
- `greeting` parameter on `core.greet()`; empty or whitespace-only greetings
  raise `ValueError`, and the CLI exits with code 2.

## [0.1.0] - 2026-11-20

### Added

- Initial project structure: `src/` layout, example CLI with `--name`,
  tests, CI, and process documentation.

[Unreleased]: https://github.com/rccmodena/first_claude_project/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/rccmodena/first_claude_project/releases/tag/v0.2.0
[0.1.0]: https://github.com/rccmodena/first_claude_project/commit/39ffad5
