# Step 03 · The AI Coding Tool Landscape (2026)

> **⏱️ Time:** ~1 hour · **Prereq:** Step 02 · **Best for:** every track

You do **not** need to master every tool. You need to know the *categories*, pick 1–2 daily drivers, and be comfortable switching.

---

## 🎯 What you'll learn

- The 4 categories of agentic coding tools.
- The tradeoffs between **IDE-native** and **CLI-native**.
- Which tool fits which kind of task.
- How to make a "primary + sidekick" setup.

---

## The 4 categories

```mermaid
flowchart TD
    A[Agentic Coding<br/>Tools] --> B[IDE-native<br/>in your editor]
    A --> C[CLI-native<br/>in your terminal]
    A --> D[OSS frameworks<br/>open-source tools]
    A --> E[Cloud agents<br/>remote PR builders]
```

### 1. IDE-native (the "in-editor" experience)

Built into (or deeply integrated with) your code editor.

| Tool | Strength | Weakness | Pricing |
|------|----------|----------|---------|
| **Cursor** | Best-in-class agent (3.x Agents Window), Marketplace plugins, async subagents, worktrees, rules/skills/hooks | Forks VS Code (not VS Code itself) | ~$20/mo |
| **GitHub Copilot (Agent Mode + coding agent)** | Universal, works in VS Code / JetBrains / Xcode; deep GitHub integration; MCP support; AI Credits billing since June 2026 | Less bleeding-edge than Cursor for some agent workflows | Free–$39/mo (Max $100) |
| **Windsurf** | Cascade "flow" feels very natural | Smaller ecosystem | ~$15/mo |
| **Google Antigravity** | Gemini 3.7 Flash-native agent IDE; strong multimodal + Google Cloud integration | Newer; Google-ecosystem focused | Plan-based |

### 2. CLI-native (the "agent in a terminal" experience)

Run in your shell, see your files, execute commands directly.

| Tool | Strength | Weakness | Pricing |
|------|----------|----------|---------|
| **Claude Code** | Most agent-native workflow; dynamic workflows, effort control, Skills, hooks, subagents, plugins | Tied to Anthropic | Usage-based (~$5/$25 per M tokens for Opus 5); Pro from $20/mo |
| **OpenAI Codex CLI** | GPT-5.6 default (ChatGPT sign-in); `gpt-5.6` family (Sol/Terra/Luna) for API-key workflows; open-source Rust CLI; strong Terminal-Bench scores | Tied to OpenAI | Usage-based |
| **Gemini CLI → Antigravity CLI** | Gemini 3.7 Flash / 3.1 Pro access; 1M context; Google Search grounding built in | Gemini CLI sunset June 18, 2026 for consumer tiers; Antigravity CLI is Go-based with async multi-agent workflows | Usage-based / plan-based |
| **Qwen Code** | Fully open; Qwen3-Coder family; can run local or self-host | Infra required for best perf | Free (model costs) |
| **Aider** | Token-efficient repo-map; git-native auto-commits | Terminal-only UX | Free (model costs) |
| **OpenCode** | Model-agnostic (75+ providers, bring-your-own-model); large OSS community (~200k stars); MCP + skills + hooks support | Moved to the anomalyco org; Claude OAuth blocked Jan 2026 (removed Feb 2026) — bring API keys for Claude | Free (model costs) |
| **Muse Code** (Meta, Aug 2026) | Fail-closed OS sandbox by default; cheap tokens ($1.25/$4.25 per M); async background agents with an audit event log | Brand new (shipped Aug 5, 2026); smaller ecosystem | Usage-based |

### 3. OSS extensions for VS Code / JetBrains

| Tool | Strength | Weakness |
|------|----------|----------|
| **Cline** | Autonomous with step approval; many model providers | UI still evolving |
| **Continue** | Most flexible config; VS Code + JetBrains | Less "agentic" by default |
| **Roo Code** | Cline fork with deep role-based modes | Smaller community |

### 4. Cloud agents (work happens on a remote sandbox)

You assign a task, they return a PR.

| Tool | Strength | Weakness |
|------|----------|----------|
| **Devin** | Full autonomous "employee" UX | Expensive; mixed reviews |
| **OpenHands** (formerly OpenDevin) | Open-source autonomous coding agent | Self-hosted infra required |
| **GitHub Copilot coding agent** | Tight GitHub issue → PR loop; good governance fit for GitHub teams | GitHub-only |
| **Cursor Cloud Agents** | Spawn agents from phone/web; worktree isolation | Still maturing |
| **OpenAI Codex (Cloud)** | Parallel multi-task execution; GPT-5.6 in Codex | Newer |
| **Gemini Enterprise Agent Platform** | Strong if your team lives in Google Cloud or Workspace | Product surface changes quickly |

---

## How to choose: decision tree

```mermaid
flowchart TD
    Q1{Where do you<br/>spend most<br/>of your time?}
    Q1 -->|VS Code / JetBrains| Q2{Willing to use<br/>a VS Code fork?}
    Q1 -->|Terminal| Q3{Do you want<br/>Anthropic models<br/>as default?}
    Q1 -->|GitHub PRs| GH[GitHub Copilot Agent<br/>+ coding agent]

    Q2 -->|Yes, best-in-class| CUR[Cursor]
    Q2 -->|No, stay on VS Code| CL[Cline or<br/>Copilot Agent]

    Q3 -->|Yes| CC[Claude Code]
    Q3 -->|No / want open-source| Q4{Need local<br/>models?}
    Q4 -->|Yes| QW[Qwen Code]
    Q4 -->|No| AI[Aider]

    style CUR fill:#EF4444,color:#fff
    style CC fill:#DC2626,color:#fff
    style GH fill:#0A0A0A,color:#fff
    style CL fill:#E5E5E5,color:#0A0A0A
    style QW fill:#D4D4D4,color:#0A0A0A
    style AI fill:#B91C1C,color:#fff
```

---

## My recommended "primary + sidekick" setups

Pick a **primary** (your daily driver) and a **sidekick** (for when the primary is stuck or the task is specialized).

| Primary | Sidekick | Best for |
|---------|----------|----------|
| **Cursor** | **Claude Code** | Full-time engineers who want the best GUI + a CLI fallback for multi-step refactors |
| **Claude Code** | **Cursor** | Power users who live in the terminal but want an IDE for browsing |
| **GitHub Copilot** | **Aider** | GitHub-heavy teams wanting governance + a free terminal fallback |
| **Copilot coding agent** | **Codex CLI** | GitHub-first teams that want issue-to-PR automation plus a terminal backup |
| **Antigravity CLI** | **Cursor or Claude Code** | Learners who want large-context exploration (Gemini 3.7 Flash) plus a familiar editor agent |
| **Cline** | **Qwen Code** | Privacy-focused / self-hosted / no-cloud environments |

> Going through this roadmap, **we'll use both Cursor (Step 04) and Claude Code (Step 05)**. If you can, install both. They're complementary.

---

## Vendor-neutral comparison checklist

Use this checklist when a new tool appears. Tool names change fast; capabilities matter more than hype.

- **Context strategy:** Can it read the right files without dumping the whole repo into context?
- **Tool boundaries:** Can you approve shell, file, browser, MCP, and deploy actions separately?
- **MCP support:** Can it connect to your tools through MCP, and can you limit server permissions?
- **Review workflow:** Does it produce a diff or PR that a human can review before merge?
- **Eval fit:** Can you measure whether the tool improved your task quality, speed, or safety?
- **Fallback:** If the tool fails, can you continue in another agent without losing the task state?

---

## 🎥 Watch

- **[Every AI Coding Tool Compared (2026) — Matt Pocock](https://www.youtube.com/results?search_query=ai+coding+tools+comparison+2026+matt+pocock)** (search — this genre updates fast)
- **[Fireship — AI coding tool showdown](https://www.youtube.com/@Fireship)** (search his channel; short, funny, current)
- **[Cline vs Cursor vs Claude Code — honest comparison](https://www.youtube.com/results?search_query=cline+cursor+claude+code+comparison+2026)**

## 📚 Read

- 📘 [**caramaschiHG/awesome-ai-agents-2026**](https://github.com/caramaschiHG/awesome-ai-agents-2026) — curated list of agent tools across 20+ categories; bookmark it.
- 📄 [**Ry Walker — AI Coding Assistants Compared**](https://rywalker.com/research/ai-coding-assistants) — honest research.
- 📄 [**State of AI Report 2025/26**](https://www.stateof.ai/) — yearly industry pulse.

---

## ✍️ Exercise (30 min)

1. Install **two** tools from different categories — e.g., Cursor (IDE) + Claude Code (CLI), Copilot Agent + Codex CLI, Antigravity CLI + Cursor, or VS Code + Cline + Aider.
2. Give them **the same small task** (e.g., "add input validation to the /login endpoint of my demo repo").
3. Fill in this table in your learning log:

| Tool | How many turns? | Quality 1–5 | Safety controls | What I liked | What frustrated me |
|------|-----------------|-------------|-----------------|--------------|---------------------|
| (Tool 1) | | | | | |
| (Tool 2) | | | | | |

This 20-minute exercise will teach you more about tool differences than any blog post.

---

## ✅ Self-check

1. Name one tool from each of the 4 categories.
2. When would you pick a **cloud agent** over an IDE agent?
3. What's the benefit of having a CLI sidekick to an IDE primary?

---

## 🧭 Next

→ [Step 04 · Cursor Mastery](./04-cursor-mastery.md)
