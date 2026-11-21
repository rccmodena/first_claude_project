# My Project

> Short description of what the project does.

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
