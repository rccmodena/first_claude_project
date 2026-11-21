# FIRST CLAUDE PROJECT

> A small, typed Python CLI that prints a configurable greeting, built to practice a complete development workflow with Claude Code.

## About

FIRST CLAUDE PROJECT is a deliberately simple command-line tool: it greets someone by name,
with a greeting word you can choose. The code is small on purpose. The point of the project
is the process around it, used as a sandbox for working with [Claude Code](https://claude.com/claude-code):

- every change starts from a GitHub issue;
- work happens on gitflow branches (`feature/*`, `docs/*`, `release/*`) and lands through pull requests;
- commits and PR titles follow Conventional Commits;
- CI runs Ruff, mypy (strict) and pytest with a coverage threshold on every PR;
- releases are tagged, published on GitHub and recorded in the [changelog](CHANGELOG.md).

## Usage

```bash
uv run first_claude_project                        # Hello, world!
uv run first_claude_project --name Ada             # Hello, Ada!
uv run first_claude_project --name Ada --greet Hi  # Hi, Ada!
uv run first_claude_project --version              # first_claude_project 0.2.1
```

An empty or whitespace-only `--name` or `--greet` is rejected with an error and exit code 2.

## Documentation

| Document | Contents |
|---|---|
| [docs/initial-setup.md](docs/initial-setup.md) | Step-by-step guide to create the project from scratch (one time only) |
| [docs/gitflow.md](docs/gitflow.md) | Branches, naming, feature / release / hotfix flows |
| [docs/commits.md](docs/commits.md) | Commit message standard (Conventional Commits) |
| [docs/pull-requests.md](docs/pull-requests.md) | PR rules, review and merge |
| [docs/issues.md](docs/issues.md) | How to use Issues, labels and milestones |
| [docs/claude-code.md](docs/claude-code.md) | How to work with Claude Code in this project |
| [CONTRIBUTING.md](CONTRIBUTING.md) | One-page summary for contributors |
| [CHANGELOG.md](CHANGELOG.md) | Notable changes in each version |

## Quick start

```bash
git clone <repo-url>
cd <repo>
uv sync                      # installs dependencies (including dev group)
uv run pre-commit install --hook-type pre-commit --hook-type commit-msg
uv run pytest                # runs the tests
uv run first_claude_project --name Ada # runs the example CLI (Hello, Ada!)
uv run first_claude_project --name Ada --greet Hi # custom greeting (Hi, Ada!)
```

## Layout

```text
src/first_claude_project/   application code (src layout)
tests/            tests, mirroring src/
docs/             process documentation
.github/          issue/PR templates and CI workflow
```
