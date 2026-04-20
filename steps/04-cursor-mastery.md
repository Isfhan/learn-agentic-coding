# Step 04 · Cursor Mastery

> **⏱️ Time:** ~3 hours · **Prereq:** Step 03, Cursor installed

We'll go from *"I use Tab + Chat"* to *"I configure agents, rules, skills, hooks, and MCP servers in Cursor."*

---

## 🎯 What you'll learn

- Every mode Cursor ships: **Tab**, **Cmd-K**, **Chat**, **Agent**, **Plan**, **Ask**, **Debug**.
- How to use **Rules**, **Skills**, **Hooks**, **Subagents**, and **MCP** inside Cursor.
- Which keyboard shortcuts are worth memorizing.
- How to make Cursor 2x faster for *your* codebase specifically.

---

## 1. The modes — know the right tool for the job

| Mode | Trigger | Use for |
|------|---------|---------|
| **Tab** | Just type | Autocomplete next line / block |
| **Cmd-K** | ⌘K / Ctrl-K in file | Inline edit / generate a snippet |
| **Chat** | ⌘L | Quick Q&A about a file (no file edits) |
| **Agent** | ⌘I (mode: Agent) | The full agent loop — plans, reads, edits, runs shell |
| **Plan mode** | Mode switcher | Read-only, helps you *design* before touching files |
| **Ask mode** | Mode switcher | Read-only, for code comprehension |
| **Debug mode** | Mode switcher | Systematic bug investigation with runtime evidence |

**Practical rule:**
- Use **Tab** 80% of the time.
- Use **Cmd-K** for surgical inline edits.
- Use **Agent** for anything that spans multiple files.
- Use **Plan** when the task is fuzzy / has trade-offs.

---

## 2. Rules — the secret sauce

Rules are persistent instructions that ride along with every request. Set them once and Cursor will stop suggesting wrong-framework code forever.

### Where rules live

| Scope | Location | Use for |
|-------|----------|---------|
| **Project** | `.cursor/rules/*.mdc` | Tech stack, code style, testing conventions (version-controlled) |
| **User** | Cursor Settings → Rules | Personal preferences (e.g., "I prefer tabs, no semicolons") |
| **Team** | Team dashboard | Shared policies |

### Rule types

```yaml
---
description: "Apply when editing React components"
globs: ["**/*.tsx", "**/*.jsx"]
alwaysApply: false
---
- Use function components with hooks (no classes).
- Prefer `useState` + `useReducer` over external state mgmt unless >3 useStates exist.
- Co-locate tests as `Component.test.tsx`.
```

The 4 types:
1. **Always** — in every session
2. **Agent decides** — included when description matches task
3. **Globs** — auto-included for matching files
4. **Manual** — @-mentioned in chat only

### 🔧 Build your first rule file

Create `.cursor/rules/project.mdc`:

```markdown
---
description: "Project-wide rules"
alwaysApply: true
---
# Project: MyApp
- Stack: TypeScript, Node 20, Fastify, Prisma/Postgres, Vitest.
- Every new endpoint lives in `src/routes/` and is registered in `src/app.ts`.
- Errors use `AppError` from `src/errors.ts`, never raw `throw`.
- Tests: Vitest, one test file per source file, `describe`-per-function.
- Do not install new dependencies without asking.
```

**Keep rules under ~500 lines.** More than that and the model starts ignoring half of them.

---

## 3. Skills (in Cursor) — reusable capabilities

Skills are **packaged expertise** your agent can load on demand. Think of each skill as a mini-guide the model consults when relevant.

Example skills you might ship in a project:
- `create-migration` — how to author a Prisma migration safely
- `write-pr-description` — your team's PR-description template
- `run-release` — the exact steps of your release process

Skills live in `.cursor/skills/<name>/SKILL.md` (and may include scripts/files).

> We'll go deep on Skills in [Step 08 · Skills](./08-skills.md). For now: know they exist and that Cursor supports them.

---

## 4. Hooks — automate the agent loop

Hooks run before/after agent events. Example uses:

- Run `prettier --write` after every edit → never see bad formatting again.
- Block edits to `package.json` unless explicit approval.
- Inject `git diff` at session start so the agent knows what's changed.

### Example: `/.cursor/hooks.json`

```json
{
  "version": 1,
  "hooks": {
    "afterFileEdit": [
      { "command": "pnpm prettier --write \"$CURSOR_EDITED_FILE\"" }
    ],
    "sessionStart": [
      { "command": "git status --porcelain" }
    ]
  }
}
```

We'll build more in [Step 11 · Hooks & Automation](./11-hooks-automation.md).

---

## 5. Subagents — delegate for parallelism & context isolation

Cursor ships built-in subagents:
- **Explore** — searches and analyzes codebases (read-only, safe)
- **Bash** — runs shell command sequences
- **Browser** — controls a browser via MCP

You invoke them by asking the agent to use them, e.g., *"Use the Explore subagent to find every place we call `/api/users` across frontend + backend, then summarize."*

**Why this is huge:** the subagent has its *own* context window. Its messy exploration doesn't pollute your main session.

More in [Step 12 · Subagents & Orchestration](./12-subagents-orchestration.md).

---

## 6. MCP in Cursor — plug in anything

Cursor supports MCP servers out of the box. Add them at `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgres://localhost/mydb"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxx" }
    }
  }
}
```

Now the agent can query your DB and GitHub. We'll cover MCP properly in [Step 09](./09-mcp-introduction.md) and [Step 10](./10-mcp-building-servers.md).

---

## 7. Keyboard shortcuts worth learning

| Shortcut (Mac / Win) | Action |
|----------------------|--------|
| `⌘ K` / `Ctrl K` | Inline edit in current file |
| `⌘ L` / `Ctrl L` | Open Chat |
| `⌘ I` / `Ctrl I` | Open Agent (or quick toggle) |
| `⌘ .` / `Ctrl .` | Quick fix |
| `⌘ N` / `Ctrl N` | New chat (clean context!) |
| `@` in chat | Reference file / folder / symbol / docs |
| `⌘ ⇧ L` / `Ctrl ⇧ L` | Add selection to chat |

> 🔑 **`@` is the most powerful feature most users underuse.** `@file`, `@folder`, `@docs`, `@web`, `@git`, `@code` — explore them.

---

## 🎥 Watch

- **[Official Cursor tutorials](https://cursor.com/learn)** — Cursor's own onboarding.
- **["Cursor rules, commands, skills, and hooks: a complete guide"](https://theodoroskokosioulis.com/blog/cursor-rules-commands-skills-hooks-guide/)** — one of the best deep dives.
- **["12 Hidden Settings To Enable In Your Cursor/Claude Setup" — AI LABS](https://www.youtube.com/watch?v=pDoBe4qbFPE)** — optimization tips.
- **YouTube search:** [`"Cursor AI tutorial 2026"`](https://www.youtube.com/results?search_query=cursor+ai+tutorial+2026) — this space refreshes monthly, prefer recent vids.

## 📚 Read

- 📘 [**cursor.com/docs**](https://cursor.com/docs) — official docs. Actually good.
- 📘 [**cursor.com/docs/agent/third-party-hooks**](https://cursor.com/docs/agent/third-party-hooks) — hooks reference.
- 📘 [**cursor.com/docs/subagents**](https://cursor.com/docs/subagents) — subagents reference.
- 📘 [**PatrickJS/awesome-cursorrules**](https://github.com/PatrickJS/awesome-cursorrules) — community rule examples. Steal liberally.

---

## ✍️ Exercise (1 hour)

Pick a project you own (or fork any OSS repo).

1. Create `.cursor/rules/project.mdc` describing the stack, conventions, and "don'ts."
2. Create `.cursor/rules/tests.mdc` with `globs: ["**/*.test.ts"]` and test-writing rules.
3. Add a `hooks.json` that runs your formatter after edits.
4. Open the Agent and ask: *"Add a new endpoint `GET /health` that returns `{ok: true, uptime: seconds}`. Follow project conventions."*
5. Notice: did the agent follow the rules without being told?
6. Screenshot the diff. Push to GitHub. Tweet it. That's portfolio content.

---

## ✅ Self-check

1. What's the difference between a rule, a skill, and a hook in Cursor?
2. When would you use **Plan mode** vs **Agent mode**?
3. How do you add an MCP server to Cursor?

---

## 🧭 Next

→ [Step 05 · Claude Code Mastery](./05-claude-code-mastery.md)
