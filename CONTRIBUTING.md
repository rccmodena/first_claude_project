# Contributing

One-page summary. Details live in [`docs/`](docs/).

1. **Open (or pick) an issue.** → [docs/issues.md](docs/issues.md)
2. **Create a branch from `develop`**: `feature/<n>-description`. → [docs/gitflow.md](docs/gitflow.md)
3. **Make small commits following Conventional Commits**: `feat(api): add X`. → [docs/commits.md](docs/commits.md)
4. **Run locally before pushing:**
   ```bash
   uv run ruff check . && uv run ruff format --check .
   uv run mypy
   uv run pytest
   ```
5. **Open a PR to `develop`**, fill in the template and reference the issue (`Closes #N`). → [docs/pull-requests.md](docs/pull-requests.md)
6. **Wait for green CI and 1 approval**, then squash merge.

## Never do

- Commit directly to `main` or `develop`.
- `git push --force` on a shared branch.
- Push secrets (`.env`, keys, tokens).
- Mix several issues in one PR.
