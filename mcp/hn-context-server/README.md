# HN Context MCP Server

Minimal MCP-compatible server that connects to a real external API (Hacker News public API) and exposes one tool:

- `get_hn_top_story`: fetches current top story metadata

## Why this exists

This artifact completes the roadmap requirement to ship an MCP server wired to a live API while keeping the implementation small and auditable.

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
