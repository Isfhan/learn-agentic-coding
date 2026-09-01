# HN Context MCP Server

Minimal MCP-compatible server (protocol `2026-07-28`, stateless) that connects to a real external API (Hacker News public API) and exposes one tool:

- `get_hn_top_story`: fetches current top story metadata

## Protocol notes (2026-07-28)

- **Stateless:** the `initialize` handshake and `Mcp-Session-Id` are gone. Protocol version, client info, and capabilities travel in a `_meta` field on each request; the server reports its identity in `_meta` on each reply.
- **Tool list caching:** `tools/list` results carry `ttlMs` and `cacheScope` so clients know how long the list stays fresh.
- **Stateful apps:** this server is read-only and stateless by design. If you add an app that needs state across calls, use the explicit-handle pattern (a tool mints an id and returns it; the model passes it back as an ordinary argument) instead of hidden session state.
- **SDKs:** the official TypeScript SDK v2 (`@modelcontextprotocol/server` + `client`, stable `2.0.0+`) and Python SDK v2 (stable `mcp` 2.0.0) implement the new spec. Older clients (spec `2025-11-25`) that begin with `initialize` will not work with this server; it no longer answers the handshake.

## Why this exists

This artifact completes the roadmap requirement to ship an MCP server wired to a live API while keeping the implementation small and auditable.

## Security and permissions

- **Auth:** No API key is required because the Hacker News API is public.
- **Least privilege:** The server is read-only. It cannot write files, mutate Hacker News, post comments, or call private APIs.
- **Tool boundary:** The only exposed tool is `get_hn_top_story`. Keep the tool list small so agents do not receive unnecessary power or context.
- **Fallback behavior:** Network calls time out after 5 seconds. Bad ranks, empty API responses, and failed fetches return MCP tool errors instead of crashing the process.
- **HITL (human-in-the-loop):** If you extend this into a write-capable MCP server, add explicit human approval before posting, deleting, deploying, or changing external systems.

## Run

```bash
node mcp/hn-context-server/server.js
```

## Cursor config snippet

```json
{
  "mcpServers": {
    "hn-context": {
      "command": "node",
      "args": ["mcp/hn-context-server/server.js"]
    }
  }
}
```

## Tool contract

- Input:
  - `rank` (integer, optional, default `0`) — position in top stories list.
- Output:
  - JSON text containing id, title, url, score, by, and timestamp.

## Extension exercise

Turn this read-only server into a safer write-capable design on paper first:

1. Add a proposed write tool, such as `draft_hn_comment`.
2. Define the exact input schema and output shape.
3. Add a HITL approval step before any real post is made.
4. Document the auth token scope and where the token is stored.
5. Add evals that confirm the agent refuses to post secrets, spam, or destructive content.
