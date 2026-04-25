# Step 10 · Building MCP Servers

> **⏱️ Time:** ~4 hours · **Prereq:** Step 09

Installing MCP servers is cool. Building one is a superpower. By the end of this step you will have **your own MCP server running** that Cursor and Claude Code can both use.

---

## 🎯 What you'll learn

- The MCP SDK in **TypeScript** and **Python**.
- How to expose **tools, resources, and prompts**.
- How to test with the **MCP Inspector**.
- How to publish to npm / PyPI so others can install with `npx`/`uvx`.

---

## 1. The shortest possible server (TypeScript)

Let's build a server that exposes one tool: `roll_dice(sides, count)`.

### Setup

```bash
mkdir mcp-dice && cd mcp-dice
npm init -y
npm i @modelcontextprotocol/sdk zod
npm i -D typescript @types/node tsx
npx tsc --init
```

### `src/index.ts`

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({
  name: "dice",
  version: "1.0.0",
});

server.tool(
  "roll_dice",
  "Roll N dice with S sides each. Returns the individual rolls and the sum.",
  {
    sides: z.number().int().min(2).max(1000).describe("Sides per die"),
    count: z.number().int().min(1).max(100).describe("Number of dice"),
  },
  async ({ sides, count }) => {
    const rolls = Array.from({ length: count }, () =>
      Math.floor(Math.random() * sides) + 1
    );
    const sum = rolls.reduce((a, b) => a + b, 0);
    return {
      content: [
        { type: "text", text: JSON.stringify({ rolls, sum }, null, 2) },
      ],
    };
  }
);

const transport = new StdioServerTransport();
await server.connect(transport);
```

### Run it in dev

```bash
npx tsx src/index.ts
```

The server is now listening on **stdio**. It does nothing until a client speaks to it.

---

## 2. Test with the MCP Inspector

Anthropic ships an official inspector — a web UI to poke any MCP server.

```bash
npx @modelcontextprotocol/inspector npx tsx src/index.ts
```

Open the URL it prints. You'll see:
- Tools tab → `roll_dice` listed. Click it, enter args, hit **Call**.
- Resources tab → empty (we haven't added any yet).
- Prompts tab → empty.

🎉 You just built and tested your first MCP server.

---

## 3. Connect it to Cursor / Claude Code

Bundle and install it globally (simple path while developing):

Add to `.cursor/mcp.json` (or Claude's config):

```json
{
  "mcpServers": {
    "dice": {
      "command": "npx",
      "args": ["tsx", "/absolute/path/to/mcp-dice/src/index.ts"]
    }
  }
}
```

Restart. Ask the agent: *"Roll 3d6 for me."* Watch it invoke your tool.

---

## 4. Adding resources

Resources are read-only data the user or client can attach. Example: expose local markdown files.

```typescript
server.resource(
  "notes",
  "notes://local",
  async () => {
    const files = await fs.readdir("./notes");
    return {
      contents: files.map((f) => ({
        uri: `notes://local/${f}`,
        name: f,
        mimeType: "text/markdown",
      })),
    };
  }
);
```

---

## 5. Adding prompts

Prompts are pre-built templates users can insert.

```typescript
server.prompt(
  "summarize-notes",
  "Summarize today's notes into a daily brief.",
  { date: z.string().describe("YYYY-MM-DD") },
  async ({ date }) => ({
    messages: [{
      role: "user",
      content: {
        type: "text",
        text: `Read @notes://local/${date}.md and produce a 5-bullet daily brief.`,
      },
    }],
  })
);
```

---

## 6. Python version (identical architecture)

```bash
pip install mcp
```

### `server.py`

```python
from mcp.server.fastmcp import FastMCP
import random

mcp = FastMCP("dice")

@mcp.tool()
def roll_dice(sides: int, count: int) -> dict:
    """Roll N dice with S sides. Returns rolls + sum."""
    rolls = [random.randint(1, sides) for _ in range(count)]
    return {"rolls": rolls, "sum": sum(rolls)}

if __name__ == "__main__":
    mcp.run()
```

```bash
python server.py
# or from any MCP host:
# "command": "python", "args": ["/abs/path/server.py"]
```

---

## 7. Best-practice tool design

Anthropic has published guidance on this ([see this must-read](https://www.anthropic.com/engineering/writing-tools-for-agents)). The gist:

✅ **Do:**
- Give tools **clear, action-verb names** (`create_issue`, not `issues`).
- Write descriptions for an agent, not a human. Be explicit about inputs/outputs.
- Validate inputs with Zod / Pydantic. Reject with a helpful error message.
- Return **structured** content (JSON text) rather than prose.
- **Keep tool count low.** Fewer, more focused tools beat 50 overlapping ones.
- Add a `list_*` tool before a `get_*` tool — the agent needs to discover IDs first.

❌ **Don't:**
- Expose 47 tools that duplicate each other's functionality.
- Return giant blobs. Paginate.
- Mutate silently. If `delete_issue` is destructive, make it clear in the description.
- Name a tool generically ("action1"). Agents pick tools by name + description.

---

## 8. Security basics (we go deeper in Step 15)

- **Never trust tool inputs.** An LLM can be tricked into sending malicious args (prompt injection). Validate strictly.
- **Scope credentials minimally.** A "read-only GH" token > full PAT.
- **Sandbox shell-like tools.** If a tool runs commands, allowlist.
- **Log every invocation.** You'll want the audit trail.
- **Document auth.** Say exactly where tokens come from, what scopes they need, and what happens when they are missing.
- **Define fallback behavior.** Timeouts, rate limits, and failed APIs should return clear errors, not crash the server.
- **Use HITL for writes.** Any tool that posts, deletes, deploys, charges money, or changes production data should require human approval.

### Minimal MCP safety checklist

Before you connect a server to Cursor, Claude Code, Copilot, or any other host:

- [ ] Tool list is small and each tool has a clear action verb.
- [ ] Inputs are validated with Zod, Pydantic, or an equivalent schema.
- [ ] Secrets are loaded from environment variables, not committed config files.
- [ ] Permissions follow least privilege (only the access needed for this server).
- [ ] Read-only tools are clearly marked read-only.
- [ ] Write tools have HITL approval and audit logs.
- [ ] Network failures and rate limits have a clear fallback response.

---

## 9. Idea bank: MCP servers worth building

Real-world servers people love to build (and ship to mcp.so):

1. **`your-company-api`** — expose your internal CRM/ticketing for your agents.
2. **`log-search`** — query your Loki/ELK logs.
3. **`on-call`** — query PagerDuty, acknowledge pages.
4. **`obsidian`** — search and edit your personal notes.
5. **`home-assistant`** — control your smart home from an agent.
6. **`linear` / `jira`** — issue tracking (community ones exist; roll your own for niche setups).
7. **`your-deploy-tool`** — kick off deploys, query status.
8. **`design-tokens`** — expose your Figma/design-system tokens so UI agents pick correct colors.

---

## 🎥 Watch

- **[Official MCP SDK tutorial video](https://www.youtube.com/results?search_query=build+mcp+server+sdk+tutorial+2026)** — search recent.
- **[Matt Pocock — Build an MCP server in TS](https://www.youtube.com/results?search_query=matt+pocock+mcp+server)**
- **[Python MCP server walkthrough](https://www.youtube.com/results?search_query=python+mcp+server+fastmcp+tutorial)**

## 📚 Read

- 📘 [**modelcontextprotocol.io/docs**](https://modelcontextprotocol.io/docs) — official reference.
- 📘 [**modelcontextprotocol/typescript-sdk**](https://github.com/modelcontextprotocol/typescript-sdk)
- 📘 [**modelcontextprotocol/python-sdk**](https://github.com/modelcontextprotocol/python-sdk)
- 📘 [**modelcontextprotocol/servers**](https://github.com/modelcontextprotocol/servers) — read source of official servers.
- 📄 [**Anthropic: Writing tools for agents**](https://www.anthropic.com/engineering/writing-tools-for-agents) — required reading.

---

## ✍️ Exercise (2 hours) — **CAPSTONE FOR THIS PHASE**

Build a real MCP server for *your* life. Pick one:

- **Notes server** — exposes `search_notes(query)`, `create_note(title, body)` over your Obsidian/Markdown vault.
- **GitHub-lite** — just the 3 tools you actually use: `list_my_prs`, `open_pr_comments(number)`, `assign_reviewers(number, reviewers)`.
- **Time tracker** — `start_task(name)`, `stop_task()`, `daily_summary(date)` — backed by a SQLite file.

For your first version, prefer a read-only server. If you add write actions, include the safety checklist above in your README.

Requirements:
1. Written in TypeScript or Python.
2. At least 3 tools.
3. Tested with the MCP Inspector.
4. Connected to both Cursor *and* Claude Code.
5. Pushed to GitHub with a clean README.
6. Announce on Twitter/X with `#MCP #AgenticCoding` and a short video demo.

---

## ✅ Self-check

1. What transport do local MCP servers usually use?
2. What's the difference between a tool and a resource?
3. What should a tool description contain?

---

## 🧭 Next

→ [Step 11 · Hooks & Automation](./11-hooks-automation.md)
