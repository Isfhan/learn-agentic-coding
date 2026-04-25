# Landing Page

A single-file, zero-build, modern landing page for **The Agentic Coding Roadmap**.

- **File:** `index.html` (everything inline: Tailwind via CDN, fonts, styles, JS)
- **No build step.** No `node_modules`. No bundler. Just open the file.
- **No tracking, no analytics, no external calls** beyond Google Fonts and `cdn.tailwindcss.com`.

## Preview locally

Serve the **repo root** (not the `docs/` folder) so that `steps/` and other content directories are reachable alongside the HTML files:

```bash
# Python 3 — serve from the repo root
python -m http.server 8080
# then open http://localhost:8080/docs/

# Node (no install needed if you have npx)
npx serve .
# then open http://localhost:3000/docs/
```

## Deploy

### GitHub Pages via GitHub Actions (recommended)

The included workflow (`.github/workflows/deploy-pages.yml`) assembles the HTML files together with `steps/`, `ROADMAP.md`, and other referenced content into a single `_site/` output and deploys it automatically on every push to `main`.

**One-time setup:**

1. Go to **Settings → Pages** in your GitHub repo.
2. Under **Build and deployment → Source**, choose **GitHub Actions**.
3. Push any commit to `main` — the workflow runs and your site is live at `https://<user>.github.io/<repo>/`.
   Example: [https://isfhan.github.io/learn-agentic-coding/](https://isfhan.github.io/learn-agentic-coding/)

### Cloudflare Pages / Netlify / Vercel

Run the same build step manually:

```bash
mkdir -p _site
cp docs/index.html docs/read.html _site/
cp -r steps ROADMAP.md CONTRIBUTING.md learning-log.template.md LICENSE _site/
cp -r projects resources _site/ 2>/dev/null; true
```

Then set the **publish directory** to `_site`.

## What's inside

- **Hero** with animated orbs, grid background, and a live-looking `agent_loop.py` code card
- **Tools marquee** (Cursor, Claude Code, Qwen, MCP servers, Spec Kit, OpenSpec, …)
- **The big picture** — six thesis cards
- **Four phases** (Foundations · Operator · Extender · Architect) color-coded
- **All 20 steps** rendered from a single JS array — easy to update
- **3-week plan** timeline
- **What you'll build** — portfolio outputs
- **Differentiators + final CTA + footer**

All reader links use paths relative to `read.html` (e.g. `steps/00-introduction.md`), which work correctly once the build step has placed the HTML files and content at the same level.

## Updating content

Almost everything is declarative. To update the step list, edit the `steps` array near the bottom of `index.html`:

```js
const steps = [
  { n: "00", title: "…", focus: "…", time: "30 min", href: "steps/00-introduction.md", tone: "violet" },
  // …
];
```

Tones control the phase colors: `violet` → Foundations, `cyan` → Operator, `pink` → Extender, `amber` → Architect.
