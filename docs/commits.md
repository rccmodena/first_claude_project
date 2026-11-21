# Commit message standard

We use [Conventional Commits 1.0](https://www.conventionalcommits.org/en/v1.0.0/). This enables automatic validation, changelog generation and version decisions (SemVer).

## Format

```text
<type>(<optional scope>): <description in imperative mood, lowercase, no trailing period>

[optional body: WHAT changed and WHY, lines up to 72 characters]

[optional footer: Closes #42 / BREAKING CHANGE: ...]
```

First line: **at most 72 characters**.

## Types

| Type | When to use | SemVer effect |
|---|---|---|
| `feat` | New feature | MINOR |
| `fix` | Bug fix | PATCH |
| `docs` | Documentation only | — |
| `style` | Formatting, no logic change | — |
| `refactor` | Restructuring without behavior change | — |
| `perf` | Performance improvement | PATCH |
| `test` | Adding/adjusting tests | — |
| `build` | Build, dependencies, packaging | — |
| `ci` | CI pipelines | — |
| `chore` | Maintenance that fits nowhere else | — |
| `revert` | Reverts a previous commit | — |

## Examples

Good:

```text
feat(auth): add Google OAuth login
fix(parser): handle empty lines when reading CSV
docs: explain release flow in gitflow
refactor(db): extract session creation into its own function
chore(deps): bump ruff to 0.8.0
```

With body and footer:

```text
fix(api): avoid timeout on large queries

The query loaded all records into memory. It now uses cursor
pagination with pages of 500 items.

Closes #57
```

Breaking change:

```text
feat(api)!: remove /v1/users endpoint

BREAKING CHANGE: use /v2/users. The response format changed.
```

Bad (don't):

```text
tweaks
fix bug
WIP
feat: Add Things.
updating files
```

## Suggested scopes

Keep a short list aligned with the modules in `src/` (e.g. `api`, `db`, `cli`, `auth`, `deps`). Scope is optional; don't invent one per commit. The CI title check accepts lowercase letters, digits, `_` and `-`.

## Best practices

- **Atomic commits**: one logical change per commit, and it passes the tests.
- Write the description so it completes the sentence "If applied, this commit will…" (`add`, `fix`, `remove`).
- Reference the issue in the footer: `Closes #42` (closes it when merged into the default branch), `Refs #42` (only links).
- `WIP` commits stay on your local branch; clean up with `git rebase -i` before the PR, or let the squash take care of it.
- Language: **English** for description and body, as well as types and scopes.

## Automatic validation

- Locally: the `conventional-pre-commit` hook (see `docs/initial-setup.md`).
- On GitHub: the `pr-title` CI job validates the **PR title**, which becomes the squash commit message.

> Note: `Closes #N` only closes the issue automatically when the merge lands on the repository's **default** branch. Since `develop` is the default, it works on feature PRs.
