# Contributing to the Agentic Coding Roadmap

Thanks for wanting to make this better! A roadmap for a space moving this fast only stays useful if the community maintains it. 🤝

---

## 🪴 Guiding principles

1. **Beginner-friendly.** A programmer with 6 months of experience should understand every page.
2. **High signal, low noise.** Every linked resource must be *genuinely the best of its kind*.
3. **Tool-agnostic.** We highlight multiple tools. No vendor lock-in.
4. **Recent.** Links older than ~12 months are flagged; tool docs older than ~6 months should be reviewed.
5. **Hands-on.** Every step must end with a doable exercise.
6. **Clear English.** Keep the real industry term, then explain it in plain words on first use: `MCP (Model Context Protocol: a standard way for AI tools to connect to tools and data)`.

---

## ✅ Good PR ideas

- 🔧 **Fix broken links.** Most common + most valuable.
- 🔄 **Replace outdated videos/articles** with newer, better ones.
- ➕ **Add a resource** that's strictly better than an existing one — with a 1-sentence justification.
- 🆕 **Add a new tool** to the comparison tables with honest pros/cons.
- ✍️ **Improve an exercise** with a clearer task or better expected outcome.
- 🌐 **Translate** any step to your language (new folder `steps-<lang>/`).
- 🐛 **Fix typos, grammar, rendering.**
- 📸 **Add diagrams.** Mermaid preferred (renders on GitHub), PNG accepted.

## ❌ PRs that will likely be declined

- Adding a resource without justification.
- Swapping a widely-cited resource (Karpathy, Willison, Anthropic, promptfoo, etc.) for a lesser-known one with no reason.
- Advertising your own tool without a clear fit.
- Rewrites that significantly expand word count without pedagogical gain.
- "Anti-X" content — we're here to teach, not to bash tools.

---

## ✏️ How to submit

1. Fork this repo.
2. Create a branch: `git checkout -b improve-step-09`.
3. Make your change. Keep it focused — one topic per PR is easier to merge.
4. Open a PR. Explain **what** you changed and **why** in the description.
5. If you're adding a resource, include: *"Better than X because Y"* in the PR body.

---

## 📐 Style guide

- **Headings:** Title Case for H1/H2, Sentence case for H3+.
- **Emoji:** keep modest; 1 per heading max; use them to aid scanning, not decorate.
- **Voice:** direct, slightly informal, 2nd person ("you'll…").
- **Language:** prefer short sentences, active voice, and concrete examples for non-native English readers.
- **Time estimates** on every step header.
- **"Watch / Read / Exercise"** subsections exist on every `steps/*.md` — preserve them.
- **Links:** full URLs (no markdown-reference style); prefer canonical sources (official docs > blog posts > tweets).
- **Code fences:** always specify language.
- **Tables:** for anything comparative; they render well on GitHub and phones.

---

## 🧪 Verify before submitting

- [ ] Run `python scripts/check_docs.py` for local Markdown links and Mermaid fence checks.
- [ ] Run `python scripts/check_docs.py --list-mermaid` to review every diagram location.
- [ ] Run `python -m py_compile agents/roadmap_agent.py scripts/check_docs.py`.
- [ ] Run `node --check mcp/hn-context-server/server.js`.
- [ ] All links resolve (you can use `lychee` CLI or any link checker).
- [ ] Mermaid diagrams render in GitHub or [mermaid.live](https://mermaid.live), and in the local reader at `docs/read.html`.
- [ ] Spell-check run (at least once).
- [ ] New buzzwords are explained with `term (plain-English meaning)` on first use.
- [ ] Step numbers and inter-step links still consistent.

---

## 💬 Ideas but not a PR yet?

Open an **Issue** with the `idea` label. We'll discuss before you invest time.

---

## 🙏 Acknowledging contributors

All PR authors are added to a `CONTRIBUTORS.md` we maintain over time. (Feel free to start one in your PR if it doesn't exist yet.)

---

## 💛 Code of conduct

Be kind. Assume good intent. Disagreements are welcome; personal attacks are not. We follow a standard [Contributor Covenant](https://www.contributor-covenant.org/) spirit.

---

Thanks again. Every improvement helps the next person learning this stuff. 🚀
