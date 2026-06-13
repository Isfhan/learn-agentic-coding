# Step 05 · Claude Code Mastery

> **⏱️ Time:** ~3 hours · **Prereq:** Step 04 · Claude Code installed (`npm i -g @anthropic-ai/claude-code`)

Claude Code is a terminal-native agent. Pair it with Cursor and you become dangerous.

---

## 🎯 What you'll learn

- The full Claude Code surface area: **commands, slash-commands, plugins, skills, subagents, hooks, MCP.**
- How to scope it to a project with `CLAUDE.md` / `AGENTS.md`.
- How to use it for workflows Cursor isn't great at: **long-running refactors**, **unattended tasks**, **multi-repo work**.

---

## 1. Getting started in 60 seconds

```bash
# Install
npm i -g @anthropic-ai/claude-code

# Authenticate
claude login

# Run in your repo
cd my-project
claude
```

You're in. The prompt is just a chat. Everything else is layered on.

---

## 2. The CLAUDE.md / AGENTS.md file

Like `.cursor/rules`, but one file at the repo root. Claude Code (and many other agents) reads it automatically.

```markdown
# Project: MyApp

## Stack
TypeScript 5, Node 20, Fastify, Prisma + Postgres, Vitest.

## Conventions
- Functions over classes. Pure functions when possible.
- Errors via `AppError` from `src/errors.ts`.
- Lint: `pnpm lint`. Test: `pnpm test`. Typecheck: `pnpm typecheck`.
- Before claiming done: run all three.

## Don'ts
- Never add a new dependency without asking.
- Never touch `prisma/migrations/`.
- Never push to `main` directly.

## Workflow
1. Plan first with a numbered list.
2. Wait for approval before editing.
3. After edits, run typecheck + tests before claiming done.
```

> 🧠 The `AGENTS.md` convention is becoming cross-tool: Claude Code, Codex, and Cursor all read it natively. Some OSS tools (Aider, Cline) can be configured to include it — check each tool's docs.

---

## 3. Slash commands — your shortcut arsenal

Claude Code has built-in `/commands` for common jobs. Use `/help` in-session.

Frequently used:
- `/init` — scaffold a `CLAUDE.md`.
- `/clear` — reset context (start fresh — you'll do this often).
- `/compact` — summarize & compress context when it's getting full.
- `/edit` — enter edit mode on a file.
- `/model` — switch between Haiku / Sonnet / Opus mid-session (e.g., `claude-sonnet-4-6`, `claude-opus-4-8`).
- `/plugin` — manage plugins.

### Custom slash commands

Create `.claude/commands/fix-tests.md`:

```markdown
---
description: Run tests and fix failures
---
Run `pnpm test`. If any tests fail:
1. For each failing test, read the test and the source.
2. Propose a minimal fix.
3. Apply it, re-run.
4. Repeat until green. Then show a summary diff.
```

Now you can type `/fix-tests` in any session. Boom — a reusable workflow.

---

## 4. Skills — Anthropic's killer feature

A **skill** is a folder with a `SKILL.md` that teaches Claude how to do something well. Skills are **progressive-disclosure**: only the description loads initially; full contents load only when relevant.

Example: `.claude/skills/write-pr/SKILL.md`

```markdown
---
description: Generate a PR description in our team's format
---
# Skill: Write PR

When asked to draft a PR description:

1. Run `git diff origin/main...HEAD --stat` to understand scope.
2. Run `git log origin/main..HEAD --oneline` for commits.
3. Produce a PR body with these sections:
   - ## Summary (1-3 bullets)
   - ## Why (the user-facing reason)
   - ## Changes (grouped by area)
   - ## Test plan (checklist)
4. Do NOT include: emojis, marketing speak, "This PR does X" prefixes.
```

Skills can include helper scripts, templates, and example outputs.

> We'll build a skill from scratch in [Step 08 · Skills](./08-skills.md).

**Two types** (per Anthropic's guidance):
- **Capability uplift** — teaches a skill the model doesn't have (e.g., using your internal linter).
- **Encoded preference** — teaches *how your team* does a thing.

---

## 5. Subagents in Claude Code

Spin up child agents for scoped tasks.

```
> Can you use the explore subagent to map every call to /api/users
  across the repo and summarize the patterns?
```

Built-ins mirror Cursor's:
- `explore` — read-only codebase search
- `shell` — bash specialist
- `generalPurpose` — full-power sub-agent
- `browser-use` — web automation via MCP

Why use them?
- **Context isolation** — their noisy exploration doesn't clog your main session.
- **Parallelism** — spawn several in the background.
- **Specialization** — route UI tasks to one, infra tasks to another.

More in [Step 12](./12-subagents-orchestration.md).

---

## 6. Hooks

Like Cursor's, but config lives at `.claude/hooks.json` (project) or `~/.claude/hooks.json` (user).

```json
{
  "version": 1,
  "hooks": {
    "afterFileEdit": [
      { "command": "pnpm prettier --write \"$CLAUDE_EDITED_FILE\"" }
    ],
    "beforeShellExecution": [
      {
        "prompt": "Is this command safe to run? Block `rm -rf /`, `git push --force`, `DROP TABLE`, any command that deletes data without confirmation."
      }
    ]
  }
}
```

Hooks can be **command-based** (shell scripts) or **prompt-based** (LLM evaluates & decides). Both are powerful.

---

## 7. MCP in Claude Code

```bash
claude mcp add github npx -y @modelcontextprotocol/server-github
claude mcp list
```

Or edit `~/.claude/mcp.json` directly. Same servers work in Claude Code, Cursor, and Copilot — that's the whole point of MCP.

---

## 8. Plugins

Claude Code plugins bundle **commands + skills + hooks + MCP** into one installable unit. Think of them as the "VS Code extensions" of agents.

```bash
claude plugin add https://github.com/anthropics/skills
```

Browse the growing plugin ecosystem on GitHub under [`claude-plugins`](https://github.com/topics/claude-plugins).

---

## 9. Three workflows Claude Code excels at

### 🌙 The unattended overnight refactor
```bash
claude --headless "Add TypeScript strict mode. For every new error, either
fix the type or add a narrow @ts-expect-error with a comment explaining why.
Commit in batches of 20 files with meaningful messages."
```
Come back in the morning. Review the commits. Ship it.

### 🔍 Multi-repo triage
Open Claude Code at a parent folder containing 5 repos. Ask: *"In each subdirectory that's a git repo, find every usage of our deprecated `getUserData` function and open a PR replacing it with `fetchUser`."*

### 📚 Documentation generation
*"Walk the `src/` directory. For each module, generate a one-page `README.md` documenting its exports, public API, and a usage example. Do not touch existing READMEs — only create missing ones."*

---

## 🎥 Watch

- **[Official Claude Code tutorials](https://claude.com/resources/tutorials)** — Anthropic's own.
- **["Claude Code Skills Just Got a MASSIVE Upgrade"](https://www.youtube.com/watch?v=UxfeF4bSBYI)** — Chase AI, the skill creator tool.
- **["Claude Plugins & Skills Tutorial (All Updates Combined)"](https://www.youtube.com/watch?v=6EFOT6hjvAU)** — Ansh Mehra, 26-min deep dive.
- **["12 Hidden Settings To Enable In Your Claude Code Setup"](https://www.youtube.com/watch?v=pDoBe4qbFPE)** — AI LABS, optimization tips.

## 📚 Read

- 📘 [**docs.claude.com/claude-code**](https://docs.claude.com/en/docs/claude-code/overview) — official docs.
- 📘 [**anthropics/claude-code** (GitHub)](https://github.com/anthropics/claude-code) — source + issues.
- 📘 [**Blake Crosley — Building Custom Skills for Claude Code**](https://blakecrosley.com/blog/building-custom-skills) — great hands-on guide.
- 📘 [**Anthropic: Creating your first skill**](https://claude.com/resources/tutorials/creating-your-first-skill) — official walkthrough.

---

## ✍️ Exercise (1 hour)

In any repo:

1. Run `/init` to generate a starter `CLAUDE.md`. Edit it to match your project.
2. Create `.claude/commands/review.md` — a slash-command that does a self-review of the last commit.
3. Create `.claude/commands/write-commit.md` — a slash-command that teaches Claude your team's commit-message format (use a command, not a skill, so `/write-commit` works).
4. Run `/review` on a recent commit. Stage a change and run `/write-commit`.
5. In your learning log, write: *"What did Claude Code do better than Cursor for this task? What did it do worse?"*

---

## ✅ Self-check

1. What's the point of the `CLAUDE.md` / `AGENTS.md` file?
2. When would you use `/clear` vs `/compact`?
3. What's the difference between a slash-command, a skill, and a plugin?

---

## 🧭 Next

→ [Step 06 · Open-Source Coding Agents](./06-open-source-tools.md)
