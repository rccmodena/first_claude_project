# Initial project setup (from scratch)

Do this **once**, in order. Each step has a reason; do not skip step 6 (branch protection).

## 1. Create the GitHub repository

```bash
gh repo create first_claude_project --private --clone
cd first_claude_project
```

In *Settings → General*, enable **Automatically delete head branches**. Under Pull Requests, enable **Squash merge** and **Merge commit** (see `docs/pull-requests.md`).

## 2. Copy the starter kit and rename the project

Copy the kit contents into the repository root. It already contains the `src/` layout, `pyproject.toml`, tests, docs and `.github/`.

Rename the placeholder names (`first_claude_project` for the distribution, `first_claude_project` for the Python package):

```bash
git mv src/first_claude_project src/your_package
grep -rl "first_claude_project\|first_claude_project" . --exclude-dir=.git | xargs sed -i 's/first_claude_project/your_package/g; s/first_claude_project/your-project/g'
```

Tools used (modern and fast):

| Purpose | Tool |
|---|---|
| Environment and dependencies | [uv](https://docs.astral.sh/uv/) |
| Lint + formatting | [ruff](https://docs.astral.sh/ruff/) |
| Tests | pytest + pytest-cov |
| Typing | mypy (strict) |
| Local hooks | pre-commit |

Install and verify:

```bash
uv sync
uv run pytest
uv run ruff check . && uv run ruff format --check .
uv run mypy
```

## 3. Pre-commit hooks (including commit message validation)

The kit ships a `.pre-commit-config.yaml` with ruff and `conventional-pre-commit`. Install the hooks:

```bash
uv run pre-commit install --hook-type pre-commit --hook-type commit-msg
```

> Check the latest `rev` of each hook (`uv run pre-commit autoupdate`) before pinning.

## 4. First commit and Git Flow branches

```bash
git add .
git commit -m "chore: initial project structure"
git push -u origin main

git switch -c develop
git push -u origin develop
```

Set `develop` as the **default branch** in *Settings → Branches → Default branch*. That way PRs and issues target `develop` by default and `Closes #N` works.

## 5. Labels and milestones

```bash
gh label create "type: feature"  --color 0E8A16 --force
gh label create "type: bug"      --color D73A4A --force
gh label create "type: chore"    --color C5DEF5 --force
gh label create "type: docs"     --color 0075CA --force
gh label create "priority: high" --color B60205 --force
gh label create "priority: low"  --color FEF2C0 --force
gh label create "status: blocked" --color 000000 --force
gh label create "good first issue" --color 7057FF --force

gh api repos/:owner/:repo/milestones -f title="v0.1.0" -f description="First release"
```

## 6. Branch protection (rulesets)

In *Settings → Rules → Rulesets* (or *Branches → Branch protection rules*), for `main` **and** `develop`:

- [x] Require a pull request before merging (1 approval)
- [x] Require status checks to pass (`test`, `pr-title`)
- [x] Require branches to be up to date before merging
- [x] Block force pushes
- [x] Restrict deletions

This guarantees that **nobody (not even Claude Code) can push directly** to `main`/`develop`.

> Status checks only appear in the picker after the CI workflow has run at least once. Open a throwaway PR first if needed.

## 7. First real issue

Create an issue "Set up CI and first module" and follow `docs/gitflow.md` to deliver it. The first PR validates the whole process.
