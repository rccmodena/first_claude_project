# CLAUDE.md

Python project (`src/` layout), managed with `uv`. Language for docs, code and commits: English.

## Commands

```bash
uv sync                                  # install dependencies
uv run pytest                            # tests (with coverage)
uv run ruff check . --fix                # lint
uv run ruff format .                     # format
uv run mypy                              # type check (strict)
```

Before saying a task is done, run lint, type check and tests, and make sure they pass.

## Structure

- `src/first_claude_project/` application code
- `tests/` tests (mirror the structure of `src/`)
- `docs/` process documentation

## Code conventions

- Python 3.14+, type hints on all functions (mypy runs in strict mode).
- Small functions, descriptive names, no `print` in library code (use `logging`).
- Every new behavior ships with a test; every bug fix ships with a test that reproduces it.
- Do not add dependencies without justifying it in the PR description.

## Git workflow (summary; details in docs/gitflow.md)

- NEVER commit or push directly to `main` or `develop`.
- Branches start from `develop`: `feature/<n>-description`, `fix/<n>-description`. Hotfixes start from `main`.
- Commits follow Conventional Commits (docs/commits.md): `feat(scope): description`.
- Atomic commits; never `git push --force` (use `--force-with-lease`, only on your own branch).
- PRs target `develop`, use the PR template, and include `Closes #<issue>`.
- Before creating a branch or commit on a non-trivial task, confirm the issue and the plan with me.

## Security

- Never read, print or commit `.env` files, keys or tokens.
- Do not run destructive commands (`rm -rf`, `git reset --hard`) without asking for confirmation.
