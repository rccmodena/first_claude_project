# Git Flow

## Permanent branches

| Branch | Purpose | Who writes to it |
|---|---|---|
| `main` | Production code. Every commit is a release (tagged). | Only merges from `release/*` and `hotfix/*` |
| `develop` | Integration. The next version under construction. | Only merges from `feature/*`, `fix/*` and `chore/*` via PR |

**Never** commit directly to `main` or `develop`.

## Temporary branches

| Prefix | Branches from | Merges into | Use |
|---|---|---|---|
| `feature/` | `develop` | `develop` | New functionality |
| `fix/` | `develop` | `develop` | Non-urgent bug fix |
| `chore/` / `docs/` / `refactor/` | `develop` | `develop` | Maintenance, documentation, refactoring |
| `release/` | `develop` | `main` **and** `develop` | Prepare a version (final tweaks, changelog) |
| `hotfix/` | `main` | `main` **and** `develop` | Urgent production fix |

### Naming convention

```text
<type>/<issue-number>-<short-description-in-kebab-case>
```

Examples:

```text
feature/42-login-with-oauth
fix/57-csv-parsing-error
hotfix/63-token-leak
release/1.2.0
```

Always include the issue number (except for `release/`). This links branch, PR and issue automatically.

## Daily flow: feature

```bash
git switch develop && git pull
git switch -c feature/42-login-with-oauth

# ... work, small commits following Conventional Commits ...
git push -u origin feature/42-login-with-oauth

gh pr create --base develop --fill
```

After approval and green CI: **squash merge** into `develop`; the branch is deleted.

Keep your branch up to date with `develop` (prefer rebase while nobody else uses your branch):

```bash
git fetch origin
git rebase origin/develop
git push --force-with-lease
```

## Release flow

```bash
git switch develop && git pull
git switch -c release/1.2.0
# only: version bump, CHANGELOG, small fixes — no new features
git push -u origin release/1.2.0
gh pr create --base main --title "chore(release): 1.2.0"
```

After merging into `main` (use a **merge commit**, not squash):

```bash
git switch main && git pull
git tag -a v1.2.0 -m "v1.2.0"
git push origin v1.2.0

# bring the release changes back into develop
git switch develop && git pull
git merge --no-ff main
git push
```

> `develop` is protected, so the back-merge itself should go through a PR (`main` → `develop`) rather than a direct push.

## Hotfix flow

```bash
git switch main && git pull
git switch -c hotfix/63-token-leak
# fix it, with a test that reproduces the bug
gh pr create --base main
```

After merging into `main`: tag the patch (`v1.2.1`) and merge `main` into `develop` (same as the end of the release flow).

## Versioning

[SemVer](https://semver.org/): `MAJOR.MINOR.PATCH`

- `PATCH`: backward-compatible fixes (`fix`)
- `MINOR`: backward-compatible features (`feat`)
- `MAJOR`: breaking changes (`feat!` / `BREAKING CHANGE`)

The single source of truth for the version is `version` in `pyproject.toml`.

## Visual summary

```text
main      ●───────────────●─────────●  (tags v1.0.0, v1.1.0, v1.1.1)
           \             / \       /
hotfix      \           /   ●─────●
             \         /
release       \   ●───●
               \ /     \
develop  ●──●───●───●───●──●
            \  /
feature      ●
```

## Golden rules

1. One branch = one issue = one PR.
2. Branches live a few days. If it goes past a week, split the issue.
3. Never `push --force` on `main`/`develop`; on your own branch, use `--force-with-lease`.
4. `release/*` and `hotfix/*` always come back into `develop`.
