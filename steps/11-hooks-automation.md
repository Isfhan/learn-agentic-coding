# Step 11 · Hooks & Automation

> **⏱️ Time:** ~2 hours · **Prereq:** Step 10

Hooks are tiny scripts (or prompt-based checks) that run around the agent's actions. They're how you turn "the agent mostly follows my rules" into "the agent *cannot* violate my rules."

---

## 🎯 What you'll learn

- What hooks are and which events you can hook into.
- The two flavors: **command** hooks vs. **prompt** hooks.
- Five battle-tested hook recipes to copy-paste.
- When hooks beat rules.

---

## 1. The big picture

An agent session is a timeline. Hooks run at specific points:

```
sessionStart ──► preToolUse ──► [tool runs] ──► postToolUse ──► ... ──► sessionEnd
                    │                                 │
                    ▼                                 ▼
               "validate!"                       "format! lint!"
```

Every agentic tool (Cursor, Claude Code) fires the same general set of events. The names differ slightly; the idea is identical.

### Common hook events

| Event | Fires when | Typical use |
|-------|-----------|-------------|
| `sessionStart` | Session begins | Inject status, set up env |
| `sessionEnd` | Session ends | Summary email, cleanup |
| `preToolUse` | Before any tool | Validate, block unsafe calls |
| `postToolUse` | After any tool | Log, format |
| `beforeShellExecution` | Before `bash` tool | Block `rm -rf /`, `force-push` |
| `afterFileEdit` | After an edit | `prettier`, update index |
| `beforeMCPExecution` | Before MCP call | Scan args for secrets |
| `subagentStart` / `subagentStop` | Sub-agent boundaries | Attribute cost, swap rules |

---

## 2. Two flavors: command vs. prompt

### a) Command hooks — deterministic

A shell command, fed JSON on stdin, expected to emit JSON on stdout (or exit 0/non-zero to allow/block).

```json
{
  "hooks": {
    "afterFileEdit": [
      { "command": "pnpm prettier --write \"$CURSOR_EDITED_FILE\"" }
    ]
  }
}
```

Fast, deterministic, zero extra LLM cost. **Prefer these when the rule is mechanical.**

### b) Prompt hooks — LLM-evaluated

Instead of a shell command, you write a prompt. A small model evaluates it and returns allow/block.

```json
{
  "hooks": {
    "beforeShellExecution": [
      {
        "prompt": "Is this command safe to run in our repo? Block: rm -rf, force push to main, DROP TABLE without WHERE, secrets being echoed. Allow otherwise."
      }
    ]
  }
}
```

Slower + costs tokens, but **great for nuanced policies** no regex can catch.

---

## 3. Five must-have hook recipes

### Recipe 1: Format after every edit (command)

```json
"afterFileEdit": [
  { "command": "pnpm prettier --write \"$EDITED_FILE\" 2>/dev/null || true" }
]
```

You will never see badly formatted agent output again.

### Recipe 2: Block dangerous shells (prompt)

```json
"beforeShellExecution": [
  {
    "prompt": "Reject this command if it: (1) uses `rm -rf` or deletes without backup, (2) force-pushes, (3) drops/truncates a DB in production, (4) uses `curl | sh`, (5) writes outside the repo. Otherwise allow."
  }
]
```

### Recipe 3: Inject git status at session start (command)

```json
"sessionStart": [
  { "command": "bash -c 'git status --porcelain && git log -3 --oneline'" }
]
```

The agent sees what's changed and what you've been working on. Saves 3 clarifying questions.

### Recipe 4: Auto-run typecheck after bulk edits (command)

```json
"postToolUse": [
  {
    "matcher": { "tool": "edit_file" },
    "command": "pnpm typecheck --pretty false 2>&1 | head -50"
  }
]
```

The agent sees type errors immediately — self-corrects without you asking.

### Recipe 5: Scan MCP tool args for secrets (command)

```json
"beforeMCPExecution": [
  {
    "command": "bash -c 'grep -E \"(sk-|ghp_|-----BEGIN)\" <<< \"$MCP_ARGS\" && echo BLOCKED || echo OK'"
  }
]
```

Catches accidental secret leakage to third-party MCP servers.

---

## 4. Hook config locations

| Tool | Project | User |
|------|---------|------|
| Cursor | `.cursor/hooks.json` | `~/.cursor/hooks.json` |
| Claude Code | `.claude/hooks.json` | `~/.claude/hooks.json` |

Project-level beats user-level. Commit project hooks to git.

---

## 5. Hooks vs. Rules — when each wins

| Scenario | Better solution |
|----------|-----------------|
| "Always use tabs" | **Rule** (informs behavior) + **Hook** that runs `prettier` (enforces) |
| "Never run `git push --force`" | **Hook** (a rule can be ignored; a hook *blocks*) |
| "Prefer named exports" | **Rule** — a hook that rejects default exports would be too rigid |
| "Never log passwords" | **Hook** that greps edited files for `password\s*:`  |

**Rule of thumb:** Rules inform. Hooks enforce.

---

## 6. Debugging hooks

When a hook misbehaves, you need visibility. Tips:

- Log to a file: `"command": "bash -c 'echo $EDITED_FILE >> ~/hooks.log && prettier --write $EDITED_FILE'"`.
- Start with `exit 0` — confirm the hook *fires* before adding real logic.
- Keep hook commands fast (<500ms). Slow hooks make the agent feel broken.
- For prompt hooks, err on the side of allowing — false blocks are worse than false allows during development.

---

## 🎥 Watch

- **[Cursor Docs: Hooks (official)](https://cursor.com/docs/hooks)** — canonical reference.
- **[Claude Code hooks walkthrough](https://www.youtube.com/results?search_query=claude+code+hooks+tutorial)** — search recent.
- **["Cursor rules, commands, skills, hooks: complete guide"](https://theodoroskokosioulis.com/blog/cursor-rules-commands-skills-hooks-guide/)**

## 📚 Read

- 📘 [**Cursor Docs — Hooks**](https://cursor.com/docs/hooks)
- 📘 [**Cursor Docs — Third-party hooks**](https://cursor.com/docs/agent/third-party-hooks)
- 📘 [**Claude Code docs — Hooks**](https://docs.claude.com/en/docs/claude-code/hooks)

---

## ✍️ Exercise (45 min)

In one of your projects:

1. Create `.cursor/hooks.json` (or `.claude/hooks.json`) with:
   - A **`sessionStart`** command that prints `git status`.
   - An **`afterFileEdit`** command that runs your formatter.
   - A **`beforeShellExecution`** prompt that blocks dangerous commands.
2. Deliberately try to get the agent to run `rm -rf .` or `git push --force main`. Does your hook catch it?
3. Log: Which hook surprised you most by firing? Which one did you need to refine?

---

## ✅ Self-check

1. When would you use a prompt-based hook vs. a command-based hook?
2. What's the difference between `preToolUse` and `beforeShellExecution`?
3. Should "format on save" be a rule or a hook? Why?

---

## 🧭 Next

→ [Step 12 · Subagents & Orchestration](./12-subagents-orchestration.md)
