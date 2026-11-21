# Pull Requests

## Rules

1. **All code enters through a PR.** `main` and `develop` are protected.
2. PRs from `feature/*`, `fix/*`, `chore/*`, `docs/*` → base **`develop`**.
3. PRs from `release/*` and `hotfix/*` → base **`main`** (then sync `develop`).
4. Every PR references an issue (`Closes #N`).
5. At least **1 approval**. Authors do not approve their own PR.
6. Green CI (lint, types, tests, PR title).
7. All conversations resolved before merging.
8. Ideal size: up to ~400 changed lines. Larger than that, split it.

## Title

Follows Conventional Commits, since it becomes the squash message:

```text
feat(auth): add Google OAuth login
```

## Merge strategy

| From → to | Merge | Reason |
|---|---|---|
| `feature/*`, `fix/*`, etc. → `develop` | **Squash and merge** | Linear history, one commit per delivery |
| `release/*` → `main` | **Merge commit** | Preserves the release milestone |
| `hotfix/*` → `main` | **Merge commit** | Same |
| `main` → `develop` (sync) | **Merge commit** | Do not rewrite history |

## PR lifecycle

1. Open as **Draft** as soon as you have something to discuss (`gh pr create --draft`).
2. Fill in the template (what, why, how to test).
3. Mark *Ready for review* when CI is green and you have reviewed your own diff.
4. Answer comments with new commits (don't rewrite history during review).
5. The **author** merges after approval.
6. The branch is deleted automatically.

## Reviewer checklist

- Does the change solve the issue, and only the issue?
- Are there tests for the new behavior and for the error case?
- Are names, types and error messages clear?
- Any secret, personal data or debug `print` left behind?
- Is a breaking change flagged (`!` / `BREAKING CHANGE`)?
- Are docs/CHANGELOG updated, if needed?

Useful comment prefixes: `nit:` (optional), `question:`, `blocking:`.

## Useful commands

```bash
gh pr create --base develop --fill
gh pr checks --watch
gh pr view --web
gh pr merge --squash --delete-branch
```
