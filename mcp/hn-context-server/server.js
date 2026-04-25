#!/usr/bin/env node
"use strict";

const readline = require("node:readline");
const { stdin, stdout, stderr } = require("node:process");

const API_TOP_STORIES = "https://hacker-news.firebaseio.com/v0/topstories.json";
const API_ITEM = "https://hacker-news.firebaseio.com/v0/item";
const FETCH_TIMEOUT_MS = 5000;

function writeMessage(message) {
  stdout.write(`${JSON.stringify(message)}\n`);
}

function writeError(message) {
  stderr.write(`[hn-context-server] ${message}\n`);
}

async function fetchJson(url) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);

  try {
    const res = await fetch(url, { signal: controller.signal });
    if (!res.ok) {
      throw new Error(`HTTP ${res.status} for ${url}`);
    }
    return res.json();
  } catch (err) {
    if (err.name === "AbortError") {
      throw new Error(`Timed out after ${FETCH_TIMEOUT_MS}ms for ${url}`);
    }
    throw err;
  } finally {
    clearTimeout(timeout);
  }
}

async function getTopStory(rank = 0) {
  const requestedRank = Number(rank);
  if (!Number.isInteger(requestedRank) || requestedRank < 0) {
    throw new Error("rank must be a non-negative integer.");
  }

  const ids = await fetchJson(API_TOP_STORIES);
  if (!Array.isArray(ids) || ids.length === 0) {
    throw new Error("No top stories returned by API.");
  }

  const normalizedRank = Math.min(requestedRank, ids.length - 1);
  const id = ids[normalizedRank];
  const item = await fetchJson(`${API_ITEM}/${id}.json`);

  if (!item || typeof item !== "object") {
    throw new Error(`Story ${id} was not returned by API.`);
  }

  return {
    rank: normalizedRank,
    id: item.id,
    title: item.title,
    url: item.url || `https://news.ycombinator.com/item?id=${item.id}`,
    score: item.score,
    by: item.by,
    time: item.time
  };
}

async function handleCallTool(params) {
  const name = params?.name;
  const args = params?.arguments || {};

  if (name !== "get_hn_top_story") {
    return {
      isError: true,
      content: [{ type: "text", text: `Unknown tool: ${name}` }]
    };
  }

  try {
    const story = await getTopStory(args.rank);
    return {
      content: [{ type: "text", text: JSON.stringify(story, null, 2) }]
    };
  } catch (err) {
    return {
      isError: true,
      content: [{ type: "text", text: `Tool failed: ${err.message}` }]
    };
  }
}

async function routeRequest(msg) {
  switch (msg.method) {
    case "initialize":
      return {
        protocolVersion: "2024-11-05",
        capabilities: {
          tools: {}
        },
        serverInfo: {
          name: "hn-context-server",
          version: "0.1.0"
        }
      };

    case "tools/list":
      return {
        tools: [
          {
            name: "get_hn_top_story",
            description: "Read-only tool. Return metadata for a top Hacker News story by rank.",
            inputSchema: {
              type: "object",
              properties: {
                rank: {
                  type: "integer",
                  minimum: 0,
                  description: "Top story rank to fetch. 0 = current top story."
                }
              }
            }
          }
        ]
      };

    case "tools/call":
      return handleCallTool(msg.params);

    case "notifications/initialized":
      return null;

    default:
      throw new Error(`Unsupported method: ${msg.method}`);
  }
}

const rl = readline.createInterface({ input: stdin, crlfDelay: Infinity });

rl.on("line", async (line) => {
  if (!line.trim()) return;

  let msg;
  try {
    msg = JSON.parse(line);
  } catch (err) {
    writeError(`Invalid JSON input: ${err.message}`);
    return;
  }

  if (!Object.prototype.hasOwnProperty.call(msg, "id")) {
    return;
  }

  try {
    const result = await routeRequest(msg);
    if (result !== null) {
      writeMessage({ jsonrpc: "2.0", id: msg.id, result });
    }
  } catch (err) {
    writeMessage({
      jsonrpc: "2.0",
      id: msg.id,
      error: { code: -32000, message: err.message }
    });
  }
});

rl.on("close", () => {
  writeError("stdin closed");
});
