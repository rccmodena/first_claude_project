# Working with Claude Code in this project

## Principles

1. **`CLAUDE.md` is the project's memory.** Claude Code reads it at the start of every session. Keep it short (commands, conventions, rules) and update it when something changes. Run `/init` to generate a draft, then edit by hand.
2. **One session per issue.** Start with a clean context (`/clear`) when switching tasks.
3. **Plan before coding.** For non-trivial tasks, use plan mode (Shift+Tab until *plan mode*), review the plan, and only then allow execution.
4. **Give it a way to verify.** Say which command proves the work is done (`uv run pytest`, `ruff`, `mypy`). Claude works best when it can run tests and correct itself.
5. **You are still the author.** Review the diff (`git diff`) before every commit and before opening the PR.

## Suggested flow per issue

```text
1. gh issue develop 42 --checkout --base develop            (you)
2. "Read issue #42 (gh issue view 42) and propose a plan"    (Claude, plan mode)
3. Approve the plan → Claude implements it with tests
4. "Run lint, types and tests and fix whatever fails"
5. "Make atomic commits following docs/commits.md"
6. "Open a draft PR to develop using the template, with Closes #42"
```

## Useful prompts

- `Read CLAUDE.md and docs/gitflow.md. Create the correct branch for issue #42 and tell me the plan before editing.`
- `Review my diff against develop looking for bugs, missing tests and violations of CLAUDE.md.`
- `Rewrite this branch's history into atomic Conventional Commits (show me the plan first).`

## Security and permissions

- Use `/permissions` (or a versioned `.claude/settings.json`) to **allow** safe, frequent commands: `uv run pytest`, `uv run ruff *`, `git status`, `git diff`, `gh issue view *`.
- Keep **blocked**/behind confirmation: `git push --force`, `git reset --hard`, `rm -rf`, pushes to `main`/`develop`.
- Never put secrets in the repository or in prompts. `.env` stays in `.gitignore`.
- GitHub branch protection is the last barrier: even if Claude tries, a direct push is rejected.

## Resources to grow into

- **Slash commands** in `.claude/commands/` for repeated routines (e.g. `/new-issue`, `/open-pr`).
- **Subagents** in `.claude/agents/` (e.g. a code reviewer with this project's checklist).
- **Hooks** to run `ruff format` automatically after edits.
- The **GitHub MCP server** or the `gh` CLI to read issues and PRs.

See the official documentation for up-to-date details: https://docs.claude.com/en/docs/claude-code
