# 🗒 Cheatsheets — quick reference

> Bookmark this page. Everything you need on one screen.

---

## 🧠 The agent loop (memorize)

```
while not done:
    llm.see(context)
    tool, args = llm.pick()
    result = run(tool, args)
    context += result
```

---

## 🔤 Vocab in 12 lines

| Term | One-line |
|------|---------|
| **LLM** | The brain (GPT / Claude / Gemini / Qwen / Llama). |
| **Token** | ~¾ of a word. You pay per token. |
| **Context window** | Max tokens the LLM can see in a turn. |
| **System prompt** | Hidden setup instructions the tool provides. |
| **Tool / Function call** | LLM requests an action from the agent runner. |
| **Agent** | LLM + tools + loop. |
| **MCP** | Open protocol that standardizes tools across clients. |
| **Skill** | On-demand "how to" package for an agent. |
| **Rule** | Always-on instruction for an agent in a project. |
| **Hook** | Script that runs around agent events (pre/post). |
| **Subagent** | Child agent with its own context window. |
| **Eval** | A test case for an AI system. |

---

## 🎯 Prompt recipe template

```
ROLE: You are a <specific role>.
GOAL: <outcome you want>.
CONTEXT: <relevant info; point to files>.
CONSTRAINTS: <hard dos and don'ts>.
FORMAT: <exact output shape>.
```

---

## 📜 AGENTS.md starter (one file, every tool)

```markdown
# Project X
## Stack: <lang/framework/db/test>
## Structure
- `src/…` …
## Conventions
- <2-5 rules>
## Commands
- pnpm test · pnpm typecheck · pnpm lint
## Before "done"
pnpm typecheck && pnpm test && pnpm lint
## Don'ts
- <3-5 hard don'ts>
## Workflow
1. Plan 2. Approve 3. Edit small 4. Verify
```

---

## ⚙️ MCP config snippet (Cursor / Claude both)

```json
{
  "mcpServers": {
    "github":     { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-github"],    "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "$GH_PAT" } },
    "postgres":   { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-postgres", "$DATABASE_URL"] },
    "filesystem": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/abs/path"] },
    "fetch":      { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-fetch"] }
  }
}
```

---

## 🧩 Skill skeleton

```markdown
---
name: <short-name>
description: |
  Use when the user says "<phrase 1>", "<phrase 2>", or "<phrase 3>".
  This skill produces <outcome> in our format.
---

# <Skill title>
## Steps
1. ...
## Output format
- ...
## Don'ts
- ...
## Example
See `example.md`.
```

---

## 🛡 Hook skeleton

```json
{
  "hooks": {
    "sessionStart": [{ "command": "git status --porcelain" }],
    "afterFileEdit": [{ "command": "pnpm prettier --write \"$EDITED_FILE\" 2>/dev/null || true" }],
    "beforeShellExecution": [{
      "prompt": "Block: rm -rf, force push, DROP TABLE, curl | sh, edits outside repo. Allow otherwise."
    }]
  }
}
```

---

## 🔐 Security 6-point check

- [ ] No secrets in committed `mcp.json`.
- [ ] `.env*`, keys, `.ssh/*` in agent ignore.
- [ ] Shell hook blocks destructive commands.
- [ ] MCP servers audited (official or well-starred).
- [ ] Audit log hook writing `~/.agent-audit.log`.
- [ ] Principle of least privilege on all tokens.

---

## 🧪 Eval starter (`promptfooconfig.yaml`)

```yaml
prompts:
  - 'Write {{language}} code to {{task}}. Return code only.'
providers:
  - anthropic:claude-sonnet-4.5
  - openai:gpt-5.1
tests:
  - vars: { language: Python, task: "reverse a string" }
    assert:
      - type: contains
        value: "def "
      - type: llm-rubric
        value: "Valid Python, correctly reverses a string, no explanation text."
```

---

## ⌨️ Cursor hotkeys

| Keys | Action |
|------|--------|
| `⌘K` / `Ctrl K` | Inline edit |
| `⌘L` / `Ctrl L` | Chat |
| `⌘I` / `Ctrl I` | Agent |
| `⌘N` / `Ctrl N` | New chat (clear context!) |
| `@` | Reference file/folder/docs/web/git |

---

## 💻 Claude Code slash commands

| Command | Purpose |
|---------|---------|
| `/init` | Scaffold `CLAUDE.md` |
| `/clear` | Reset context |
| `/compact` | Summarize context |
| `/model` | Switch model mid-session |
| `/plugin` | Manage plugins |
| `/review` (custom) | Example of your own command |

---

## 📞 Patterns — 30-sec picker

| Situation | Use |
|-----------|-----|
| Fixed steps | Prompt chaining |
| Clear categories | Routing |
| Independent pieces | Parallelization |
| Unpredictable decomposition | Orchestrator-workers |
| Need quality + can iterate | Evaluator-optimizer |
| Safety-critical | Debate + HITL |
| Single LLM call works | Just prompt |

---

## ✅ "Am I ready to ship an agent?" checklist

- [ ] `AGENTS.md` + rules in place.
- [ ] At least 10 evals passing.
- [ ] MCP config committed, secrets in env.
- [ ] Hooks block dangerous commands.
- [ ] Audit log enabled.
- [ ] Clear list of tools exposed (minimal).
- [ ] HITL checkpoints for destructive actions.
- [ ] README explains how to run + debug.
- [ ] Documented how to **disable** the agent.

---

[⬅ Back to resources index](./)  · [Top of README](../README.md)
