# Step 09 · MCP — The Model Context Protocol

> **⏱️ Time:** ~2 hours · **Prereq:** Step 08

This is the single most important piece of plumbing in the entire AI stack. Getting MCP is like getting HTTP in 1995. Everything else starts to make sense.

---

## 🎯 What you'll learn

- Why MCP exists and what problem it solves.
- The **host / client / server** architecture.
- The difference between **tools, resources, and prompts**.
- How to install and use your first MCP servers.

---

## 1. The problem MCP solves

Before MCP, every AI app reinvented the wheel:

```
Cursor  ⇄  GitHub API (custom integration)
Cursor  ⇄  Postgres    (custom integration)
Cursor  ⇄  Slack       (custom integration)

Claude  ⇄  GitHub API (different custom integration)
Claude  ⇄  Postgres    (different custom integration)
Claude  ⇄  Slack       (different custom integration)

Copilot ⇄  GitHub API (yet another custom integration)
...
```

N agents × M tools = N×M integrations. Chaos.

## 2. The MCP solution

One protocol. Any client. Any server.

```
       Cursor ─┐
       Claude ─┼──  MCP (JSON-RPC)  ──┬─ GitHub MCP server
       Copilot─┘                       ├─ Postgres MCP server
                                       └─ Slack MCP server
```

N + M integrations. Sanity.

> 🧠 **The analogy everyone uses:** MCP is the **USB-C of AI**. One port (protocol), many devices (data sources). **JSON-RPC** means the client and server send JSON messages that say “call this method with these arguments.”

Anthropic open-sourced MCP in late 2024. By 2026, OpenAI, Google, GitHub, and most AI tool vendors support it.

---

## 3. The architecture (3 parts)

```mermaid
flowchart LR
    subgraph Host["🏠 Host (your IDE / CLI)"]
        direction TB
        LLM[LLM]
        MC[MCP Client<br/>1 per server]
    end

    subgraph Servers["🔌 MCP Servers (processes)"]
        direction TB
        S1[github server]
        S2[postgres server]
        S3[filesystem server]
        S4[your-company server]
    end

    LLM <--> MC
    MC <-->|JSON-RPC| S1
    MC <-->|JSON-RPC| S2
    MC <-->|JSON-RPC| S3
    MC <-->|JSON-RPC| S4

    style Host fill:#dbeafe,stroke:#3b82f6
    style Servers fill:#dcfce7,stroke:#16a34a
```

| Component | What it is |
|-----------|-----------|
| **Host** | The application the user interacts with (Cursor, Claude Code, Copilot). |
| **Client** | The piece of the host that speaks MCP. One per connected server. |
| **Server** | A separate process exposing tools/resources/prompts over MCP. |

### Transports

An MCP server talks to its client over:
- **stdio** (standard input/output) — server is a local subprocess that reads and writes text streams. Most common.
- **HTTP+SSE** (HTTP plus server-sent events) — server is remote and can push updates over a web connection. Used for hosted MCP servers.

---

## 4. The 3 primitives (what servers expose)

| Primitive | Who invokes it | Think of it as |
|-----------|----------------|----------------|
| **Tools** | The **model** (agent decides to call) | API endpoints, functions |
| **Resources** | The **user/client** (explicit attach) | Files, rows, documents |
| **Prompts** | The **user** (explicit insert) | Pre-built prompt templates |

### Tools example
A `github` server might expose tools:
- `create_issue(repo, title, body)`
- `list_prs(repo, state)`
- `merge_pr(repo, number)`

The agent decides *when* to call them.

### Resources example
A `filesystem` server exposes:
- `file:///home/me/project/src/` — your project dir, readable as resources.

You (or the agent) attach a resource to the conversation explicitly.

### Prompts example
A `sql-helper` server exposes a prompt called `optimize-query` that takes a SQL string and expands into a full "analyze-this-query" prompt.

> Most people think "MCP" == "tools". Tools are the most common and useful primitive, but don't forget resources and prompts.

---

## 5. Using MCP servers today (no coding yet)

### In Cursor — `.cursor/mcp.json`

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxxx" }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres",
               "postgresql://user:pass@localhost/db"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem",
               "/Users/me/projects"]
    }
  }
}
```

Restart Cursor. Ask your agent: *"Find every open PR on the `myorg/myrepo` repo and summarize them."* — it now has a `github` tool available.

**Security note:** Do not commit real tokens in `.cursor/mcp.json`. Put secrets in environment variables, use read-only tokens when possible, and give every MCP server the smallest permission set it needs.

### In Claude Code

```bash
claude mcp add github npx -y @modelcontextprotocol/server-github
claude mcp list
```

Or edit `~/.claude/mcp.json` directly. Same format as Cursor's file.

---

## 6. Battle-tested MCP servers (2026)

Official servers from [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers):

- **filesystem** — read/write local files
- **github** — issues, PRs, code search
- **gitlab**, **bitbucket**
- **postgres**, **sqlite**, **mysql**
- **brave-search**, **fetch** (web fetch)
- **slack**, **notion**, **google-drive**
- **puppeteer**, **playwright** (browser control)
- **aws**, **gcp**, **cloudflare**
- **memory** — long-term memory server
- **sequential-thinking** — structured reasoning helper

Community-maintained registry: **[mcp.so](https://mcp.so/)** — hundreds of servers, many niche.

---

## 7. When to add an MCP server

✅ **Add when:**
- You repeatedly ask the agent to do something it can't (query prod DB, check Jira).
- You have an internal API the agent keeps hallucinating about.
- You want the agent to take actions in an external system (create a ticket, post a Slack message).

🚫 **Don't add when:**
- You just need to *read* local files (the agent can already do that).
- A skill + shell access can do the job (skills are cheaper and simpler).
- You can solve it with `curl` in a shell command.

---

## 🎥 Watch

- **[Anthropic — Intro to Model Context Protocol (official)](https://www.youtube.com/results?search_query=anthropic+model+context+protocol+intro)**
- **[Matt Pocock — "What is MCP?"](https://www.youtube.com/results?search_query=matt+pocock+mcp)** — clear dev-focused explanation.
- **[AI Engineer conference — MCP talks](https://www.youtube.com/results?search_query=model+context+protocol+AI+engineer+conference)** — go deeper.

## 📚 Read

- 📘 [**modelcontextprotocol.io**](https://modelcontextprotocol.io/) — official spec + docs. Start here.
- 📘 [**modelcontextprotocol/servers** (GitHub)](https://github.com/modelcontextprotocol/servers) — official servers to learn from.
- 📘 [**mcp.so**](https://mcp.so/) — community registry of 100s of servers.
- 📄 [**SynapseWire — MCP Practical Guide 2026**](https://synapsewire.com/en/posts/mcp-agentic-ai-practical-guide-2026/) — excellent overview.
- 📄 [**GitHub Docs — Enhancing Copilot agent with MCP**](https://docs.github.com/copilot/tutorials/enhancing-copilot-agent-mode-with-mcp)

---

## ✍️ Exercise (45 min)

1. Add the **filesystem**, **github**, and **fetch** servers to your Cursor (or Claude Code) config.
2. Restart. Verify they show up (`claude mcp list` or Cursor Settings → MCP).
3. Give the agent these tasks, one per new chat:
   - *"Summarize the top 5 open issues in `modelcontextprotocol/servers`."* (tests `github`)
   - *"Fetch https://modelcontextprotocol.io and tell me the headline."* (tests `fetch`)
   - *"What's the largest file in `~/Downloads` by size?"* (tests `filesystem`)
4. In your log, note: for each task, which tool(s) did it use? How many calls? Any surprises?

---

## ✅ Self-check

1. What are the 3 primitives an MCP server can expose?
2. What's the difference between a **host** and a **client** in MCP?
3. Why doesn't MCP replace REST APIs or gRPC?

---

## 🧭 Next

→ [Step 10 · Building MCP Servers](./10-mcp-building-servers.md) — *ship your own.*
