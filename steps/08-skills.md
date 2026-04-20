# Step 08 · Skills

> **⏱️ Time:** ~2 hours · **Prereq:** Step 07

Skills are **the 2026 breakout feature** for agentic coding. If rules are "how to be," skills are "how to *do*."

---

## 🎯 What you'll learn

- What a skill *is* and what it isn't.
- The two skill archetypes: **capability uplift** vs. **encoded preference**.
- How to **write, test, and ship** your first skill.
- Where to find great community skills.

---

## 1. The 30-second definition

A **skill** is a folder containing a `SKILL.md` (plus optional scripts/files). The `SKILL.md` starts with a **description**. Only the description sits in the agent's context permanently. When the agent decides a task matches, it reads the full skill — *progressive disclosure*.

```
.claude/skills/
└── write-migration/
    ├── SKILL.md          ← always loaded (just the description)
    ├── template.sql      ← loaded on demand
    └── example.sql       ← loaded on demand
```

**Why this is genius:** you can have 50 skills installed. Only their one-line descriptions cost context tokens. The full detail arrives exactly when needed.

---

## 2. The two archetypes

Anthropic (who formalized skills) names two types:

### a) Capability uplift
Teaches the model *something it doesn't know how to do*.

Examples:
- How to use your proprietary CLI tool.
- How to read a specific internal logfile format.
- How to navigate your custom domain-specific language.

### b) Encoded preference
Teaches the model *how your team does a thing* that it could plausibly guess, but you want done your way.

Examples:
- PR description format.
- Commit message conventions.
- Release runbook.
- Bug report triage flow.

**Both are valuable.** The second is usually where to start — encoding team preferences gives immediate ROI.

---

## 3. Anatomy of a great SKILL.md

```markdown
---
name: write-pr
description: |
  Use when the user asks you to "write a PR", "draft a pull request",
  "create PR description", or "summarize my changes for review".
  This skill produces a PR body in our team's exact format.
---

# Write PR

## When this applies
You've just completed a change and need to produce a pull request body
that follows our team's conventions.

## Steps
1. Run `git diff origin/main...HEAD --stat` to get scope.
2. Run `git log origin/main..HEAD --oneline` to list commits.
3. Read any updated `CHANGELOG.md` if present.
4. Produce a body using `template.md` in this skill's folder.

## Output format
- ## Summary (1-3 bullets, user-facing)
- ## Why (what user/business problem this solves)
- ## Changes (grouped headings: Backend / Frontend / Infra / Docs)
- ## Screenshots / Videos (only if UI changed)
- ## Test plan (checkboxes)
- ## Risks & rollback

## Don'ts
- No emojis.
- No "This PR …" prefix.
- No marketing language ("We're thrilled to…").
- No unchecked boxes shipping in the final version.

## Example
See `example.md` in this folder for a real, good PR body.
```

### Things that make skills great

✅ **Crisp description** — the agent decides whether to load you based on this one string. Make it specific.

✅ **Numbered steps** — agents execute steps better than prose.

✅ **Explicit don'ts** — just like rules.

✅ **Reference files** — keep examples, templates, and scripts alongside.

✅ **Concrete trigger phrases** — list exact words the user would say.

❌ **Don't** stuff rules into skills. Rules are always-on; skills are on-demand.

❌ **Don't** write 2000-line skills. If it's that complex, it's a plugin — multiple skills + commands + hooks.

---

## 4. Where skills live (2026)

| Tool | Location |
|------|----------|
| **Claude Code** | `.claude/skills/<name>/SKILL.md` or `~/.claude/skills/…` |
| **Cursor** | `.cursor/skills/<name>/SKILL.md` |
| **Plugins** | Bundle multiple skills into one installable |
| **Claude.ai** | Settings → Skills (for the consumer web app) |

All follow the same "folder with a `SKILL.md`" format. Write once, copy to both `.claude/skills/` and `.cursor/skills/`.

---

## 5. Walkthrough: build your first skill in 15 minutes

We'll build a **`review-pr`** skill.

### Step 1 — Decide the trigger phrases

> "Review this PR", "do a code review", "critique my change"

### Step 2 — Write SKILL.md

```markdown
---
name: review-pr
description: |
  Use when the user says "review this PR", "review my changes",
  "code review", or "critique what I just did". Produces a structured
  senior-engineer review of the current git diff.
---

# Review PR

## Steps
1. Run `git diff origin/main...HEAD` and read the full diff.
2. Identify: correctness bugs, security risks, test gaps, style violations, over-engineering.
3. Output markdown with sections in this order:
   - ## Overall (1-line verdict: Ship / Nits-then-ship / Block)
   - ## Bugs (bullet list of correctness issues, each with file:line)
   - ## Security (bullet list or "none found")
   - ## Test gaps (what isn't covered that should be)
   - ## Style nits (minor; don't block merge)
   - ## Suggestions (improvements that aren't blockers)

## Tone
- Direct, specific, no praise-sandwiching.
- Cite `file:line` for every point.
- If you can't find anything wrong, say so honestly. Don't invent issues.

## Don'ts
- Don't rewrite the code.
- Don't summarize the changes (diff is already there).
- Don't be vague ("consider improving readability" ← bad).
```

### Step 3 — Test the trigger

Open a new session in your repo. Make a code change. Then say *"review my changes"*. Did the skill load?

### Step 4 — Iterate on the description

If the skill isn't triggering when it should, add trigger phrases to the `description`. If it triggers when it shouldn't, make it more specific.

### Step 5 — Add an example file

Put `example-output.md` in the skill folder with a perfect example review. The model will imitate.

---

## 6. Great community skills to steal

- **[anthropics/skills](https://github.com/anthropics/skills)** — Anthropic's official examples.
- **[awesome-claude-skills](https://github.com/topics/claude-skills)** — community registry on GitHub.
- **[Cursor plugin/skill marketplace](https://cursor.com/plugins)** — browse installable plugins.

Great skills to install *immediately*:
- **Create tests** — generate unit tests in your framework.
- **Write commit message** — for your conventional-commits style.
- **Review PR** — like the one we just built.
- **Generate migration** — for your ORM.
- **Update changelog** — parse commits into user-facing release notes.

---

## 7. Skills vs. plugins (for reference)

A **plugin** bundles multiple skills + slash-commands + hooks + MCP servers into one installable package with a manifest. Think of it as a "VS Code extension" for your agent.

When your skills + commands + hooks pile up, it's time to turn them into a plugin you can share across your team or the community. Details vary per tool; see each tool's docs.

---

## 🎥 Watch

- **["Claude Code Skills Just Got a MASSIVE Upgrade" — Chase AI](https://www.youtube.com/watch?v=UxfeF4bSBYI)** — covers the Skill Creator tool.
- **["Claude Plugins & Skills Tutorial" — Ansh Mehra (26 min)](https://www.youtube.com/watch?v=6EFOT6hjvAU)** — most comprehensive free video.
- **[Official Anthropic Skill tutorial](https://claude.com/resources/tutorials/creating-your-first-skill)**

## 📚 Read

- 📘 [**Anthropic docs: Skills**](https://docs.claude.com/en/docs/claude-code/skills) — canonical reference.
- 📘 [**Blake Crosley — Building Custom Skills for Claude Code**](https://blakecrosley.com/blog/building-custom-skills) — excellent walkthrough.
- 📘 [**anthropics/skills** (GitHub)](https://github.com/anthropics/skills) — examples to remix.

---

## ✍️ Exercise (1 hour)

1. Build a skill for a **real pain point** you have. Suggestions:
   - `write-conventional-commit`
   - `generate-jest-test` (or your framework)
   - `explain-sql-query` (runs EXPLAIN and interprets)
   - `bump-version` (updates all the places your app's version lives)
2. Test it by triggering it via natural language — does the description work?
3. Iterate 3 times. Each iteration, note what went wrong.
4. Publish the skill as a gist or GitHub repo. Tweet it with `#AgenticCoding`.

---

## ✅ Self-check

1. What's "progressive disclosure" and why does it matter?
2. Give an example of a "capability uplift" skill and an "encoded preference" skill.
3. When would you turn skills into a plugin?

---

## 🧭 Next

→ [Step 09 · MCP — Introduction](./09-mcp-introduction.md)
