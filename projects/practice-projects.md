# 🛠 Practice Projects — build your portfolio

> Reading won't make you a pro. Shipping will. Pick 3–5 of these. Put each in its own repo. Tweet each one.

---

## 🥉 Bronze — beginner (finish in an afternoon each)

### B1 · "Commit-coach" slash command
Build a Claude Code / Cursor slash command `/commit` that:
- Reads `git diff --staged`.
- Writes a conventional-commit message that matches your team's style.
- Copies it to clipboard (use `pbcopy` / `clip.exe`).

**You'll learn:** custom commands, reading git state.

### B2 · Your first AGENTS.md
In one of your real repos, write a high-quality `AGENTS.md`. Commit it. See if the agent follows it without prompting.

**You'll learn:** what rules actually move the needle. Skill: Step 07.

### B3 · Personal "daily" skill
A skill `/daily` that:
- Reads today's calendar-events file or notes.
- Outputs a 5-bullet plan for the day.

**You'll learn:** skill authoring, progressive disclosure.

### B4 · Hook-harden a project
Take any project. Add 3 hooks: format-after-edit, block-dangerous-shell, log-audit. PR it to your own repo with a clear README.

**You'll learn:** hook patterns.

### B5 · Eval 10 of your own prompts
Pick 3 prompts you use weekly. Write 10 promptfoo evals. Run against 2 models. Publish results as a blog post or README.

**You'll learn:** evals mindset. Skill: Step 14.

---

## 🥈 Silver — intermediate (1–2 days each)

### S1 · Ship an MCP server — **⭐ crowd favorite**
Build a real MCP server that exposes something *you* use daily:
- Your Obsidian vault
- A personal timer
- Your company's internal API (if safe)
- A CSV/SQLite "mini-DB"

**Requirements:**
- TypeScript or Python.
- ≥ 3 tools.
- Tested with the MCP Inspector.
- Clean README + demo GIF.
- Publishable via `npx` / `uvx`.

**You'll learn:** the most shareable thing in this roadmap. This gets upvotes on Twitter.

### S2 · Self-built mini-agent
Finish the Step 16 capstone. Extend with:
- Conversation save/load.
- `AGENTS.md` loader.
- MCP client (so your agent can use any MCP server).

**You'll learn:** agents stop being magic.

### S3 · Multi-agent swarm for a real task
Pick something embarrassingly parallel (scan 50 files for dead code; audit 20 repos for stale deps). Build a driver script that fans out subagent calls.

**You'll learn:** orchestration mechanics.

### S4 · Code-review bot plugin
Bundle a skill (`review-pr`) + a slash-command (`/review`) + a hook (auto-run on PR-branch) into a plugin. Publish to GitHub with installation instructions.

**You'll learn:** plugin architecture.

### S5 · Local-only coding assistant
Set up Ollama + a coding model + Aider (or Cline) running fully offline. Benchmark: what tasks it can do well, what it can't.

**You'll learn:** local-LLM realities; privacy tradeoffs.

### S6 · Eval harness for YOUR agent
A promptfoo project + GitHub Action that runs on any PR touching your rules/skills/hooks. Post a badge to your repo README.

**You'll learn:** making evals part of CI. This is what pros do.

---

## 🥇 Gold — ambitious (weekend–week projects that go viral)

### G1 · "Agent OS for my laptop"
Combine:
- A personal `AGENTS.md` across all your projects.
- 5 custom skills (commit, review, release, triage, daily).
- 3 hooks (format, block-destructive, audit-log).
- 3 MCP servers (notes, calendar, internal-API).
- 1 top-level CLI that wraps Claude Code or a custom agent.

Document the whole setup as a blog post: *"How I turned my Mac into an AI-native dev environment."*

**The viral angle:** people love "setup" posts. This is shareable for years.

### G2 · Open-source "portable agent config"
A git repo called `dotagents` (like `dotfiles`) with everyone's rules + skills + hooks, installable via one command. Make it so community members can fork and remix.

**The viral angle:** create a *convention*. If it catches, you become the author of it.

### G3 · Best-of-N agent runner
A CLI that spawns N agents in parallel on the same task (using different models or temps), then a judge agent picks the best answer. Publish to npm/PyPI.

**Reference:** a similar technique powers Devin-like systems.

### G4 · MCP server for a niche domain
Examples that have worked for others:
- Accounting → QuickBooks MCP
- Music → Spotify playlist curator MCP
- Home → Home Assistant MCP
- 3D printing → OctoPrint MCP
- Tabletop → D&D rules MCP

If your domain doesn't have one, *you* make it. Instant niche audience.

### G5 · Agent-first SaaS idea
Build an agent-centric micro-SaaS:
- A Slack bot that reviews PRs via MCP → GitHub.
- A terminal tool that writes release notes across N repos.
- A "meeting → tickets" pipeline.

Dogfood it for 2 weeks. Open-source the non-secret parts.

### G6 · Teach: publish an agentic-coding course / playlist
Take 5 steps of this roadmap and make 5 YouTube videos (5–10 min each) in your own voice. Link back here. Build an audience.

**Viral angle:** educators get hired. Full stop.

---

## 📣 How to share (get that GitHub star / Twitter follow)

When you publish, include:

1. **A 30-second demo GIF** at the top of the README (use `asciinema`, `ttygif`, or just screen-record). *Most important item.*
2. **One-line elevator pitch** in the repo description.
3. **"Why it exists" paragraph** at the top of the README.
4. **Install in one command** (`npx mything` or `uvx mything`).
5. **Screenshots** in the README of the tool in action.
6. **A tweet** announcing it with: problem → video → link → ask for feedback.
7. **Cross-post** to r/LocalLLaMA (if local), r/ClaudeAI (if Claude-adjacent), r/cursor (if Cursor-adjacent), dev.to.

---

## 🎯 Ship 3 of these, and you have:

- A GitHub profile that stands out.
- Proof of agentic-coding skill for any job.
- Twitter/X content that builds your audience.
- Deep understanding that reading alone can't give.

[Commit.](https://github.com/new)

---

[⬅ Back to README](../README.md) · [Roadmap](../ROADMAP.md) · [Resources](../resources/)
