#!/usr/bin/env python3
"""Lightweight documentation checks for local links and Mermaid fences."""

from __future__ import annotations

import re
import sys
from argparse import ArgumentParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def iter_markdown_files() -> list[Path]:
    ignored_parts = {".git", ".cursor"}
    return [
        path
        for path in ROOT.rglob("*.md")
        if not any(part in ignored_parts for part in path.relative_to(ROOT).parts)
    ]


def strip_anchor(target: str) -> str:
    return target.split("#", 1)[0]


def is_external(target: str) -> bool:
    parsed = urlparse(target)
    return bool(parsed.scheme and parsed.scheme not in {"file"})


def strip_fenced_code_blocks(text: str) -> str:
    lines: list[str] = []
    inside_fence = False

    for line in text.splitlines():
        if line.strip().startswith("```"):
            inside_fence = not inside_fence
            lines.append("")
            continue

        lines.append("" if inside_fence else line)

    return "\n".join(lines)


def check_links(path: Path) -> list[str]:
    errors: list[str] = []
    text = strip_fenced_code_blocks(path.read_text(encoding="utf-8"))

    for match in MARKDOWN_LINK.finditer(text):
        target = strip_anchor(match.group(1).strip())
        if not target or is_external(target) or target.startswith("mailto:"):
            continue

        # Ignore intentionally templated examples.
        if "<" in target or ">" in target:
            continue

        local_target = unquote(target)
        resolved = (path.parent / local_target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)} links outside repo: {target}")
            continue

        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)} has broken local link: {target}")

    return errors


def check_mermaid_fences(path: Path) -> list[str]:
    errors: list[str] = []
    inside_mermaid = False
    start_line = 0

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if stripped == "```mermaid":
            if inside_mermaid:
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_number} starts nested Mermaid fence"
                )
            inside_mermaid = True
            start_line = line_number
        elif stripped == "```" and inside_mermaid:
            inside_mermaid = False

    if inside_mermaid:
        errors.append(
            f"{path.relative_to(ROOT)}:{start_line} has an unclosed Mermaid fence"
        )

    return errors


def list_mermaid_fences() -> list[tuple[Path, int]]:
    fences: list[tuple[Path, int]] = []

    for path in iter_markdown_files():
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), 1
        ):
            if line.strip() == "```mermaid":
                fences.append((path, line_number))

    return fences


def main() -> int:
    parser = ArgumentParser(
        description="Check roadmap documentation links and Mermaid fences."
    )
    parser.add_argument(
        "--list-mermaid",
        action="store_true",
        help="List every Mermaid diagram source location for visual review.",
    )
    args = parser.parse_args()

    if args.list_mermaid:
        fences = list_mermaid_fences()
        if not fences:
            print("No Mermaid diagrams found.")
            return 0

        print("Mermaid diagrams:")
        for path, line_number in fences:
            print(f"- {path.relative_to(ROOT)}:{line_number}")
        return 0

    errors: list[str] = []
    for path in iter_markdown_files():
        errors.extend(check_links(path))
        errors.extend(check_mermaid_fences(path))

    if errors:
        print("Documentation checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Documentation checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
