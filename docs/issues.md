# GitHub Issues

Every change starts with an issue. No issue, no branch.

## Types

Use the forms in `.github/ISSUE_TEMPLATE/`:

- **Bug**: something doesn't work as expected (steps to reproduce, expected vs. actual, version/environment).
- **Feature**: new functionality or improvement (problem, proposal, acceptance criteria).
- Open questions and ideas → *Discussions*, not Issues.

## How to write a good issue

- **Title**: short and specific: `Error parsing CSV with empty line`, not `Parser bug`.
- **Context**: which user/business problem does this solve?
- **Acceptance criteria**: a verifiable list (`- [ ]`) of what "done" means.
- **Small scope**: if it doesn't fit in ~3 days, split it into sub-issues.
- No secrets, tokens or personal data in text or logs.

## Labels

| Group | Labels |
|---|---|
| Type | `type: feature`, `type: bug`, `type: chore`, `type: docs` |
| Priority | `priority: high`, `priority: low` |
| State | `status: blocked` |
| Community | `good first issue` |

Every issue has **exactly one** `type:` label.

## Milestones

One milestone per version (`v0.1.0`, `v0.2.0`...). Issues for the next release go into the milestone; when all are closed, open the `release/*` branch.

## Lifecycle

1. **Open** → triage: type label, priority, milestone, assignee.
2. **In progress** → someone creates the `feature/<n>-...` branch and opens a Draft PR.
3. **Closed** → automatically by `Closes #N` when the PR is merged.

Tip: use a **GitHub Project** (board) with columns `Backlog → Ready → In progress → In review → Done` to visualize the flow.

## Creating a branch from the issue

```bash
gh issue develop 42 --checkout --base develop
# or manually:
git switch -c feature/42-login-with-oauth develop
```

## Useful commands

```bash
gh issue create
gh issue list --label "type: bug" --state open
gh issue view 42
gh issue close 42 --reason completed
```
