# Landing Page

A single-file, zero-build, modern landing page for **The Agentic Coding Roadmap**.

- **File:** `index.html` (everything inline: Tailwind via CDN, fonts, styles, JS)
- **No build step.** No `node_modules`. No bundler. Just open the file.
- **No tracking, no analytics, no external calls** beyond Google Fonts and `cdn.tailwindcss.com`.

## Preview locally

Any static server works. Examples:

```bash
# Python 3
python -m http.server --directory site 8080
# then open http://localhost:8080

# Node (no install needed if you have npx)
npx serve site

# Or just double-click site/index.html
```

## Deploy

### GitHub Pages (recommended — free, one-click)

1. Go to **Settings → Pages** in your GitHub repo.
2. Under **Build and deployment → Source**, choose **Deploy from a branch**.
3. Branch: `main` · Folder: `/site`. Save.
4. In ~60 seconds, your site is live at `https://<user>.github.io/<repo>/`.

### Cloudflare Pages / Netlify / Vercel

- **Build command:** *(leave empty)*
- **Output directory:** `site`

## What's inside

- **Hero** with animated orbs, grid background, and a live-looking `agent_loop.py` code card
- **Tools marquee** (Cursor, Claude Code, Qwen, MCP servers, Spec Kit, OpenSpec, …)
- **The big picture** — six thesis cards
- **Four phases** (Explorer · Operator · Extender · Architect) color-coded
- **All 20 steps** rendered from a single JS array — easy to update
- **3-week plan** timeline
- **What you'll build** — portfolio outputs
- **Differentiators + final CTA + footer**

All links point to real files in this repo (`../steps/...`, `../ROADMAP.md`, etc.), so the page works both locally and once deployed.

## Updating content

Almost everything is declarative. To update the step list, edit the `steps` array near the bottom of `index.html`:

```js
const steps = [
  { n: "00", title: "…", focus: "…", time: "30 min", href: "../steps/00-introduction.md", tone: "violet" },
  // …
];
```

Tones control the phase colors: `violet` → Explorer, `cyan` → Operator, `pink` → Extender, `amber` → Architect.
