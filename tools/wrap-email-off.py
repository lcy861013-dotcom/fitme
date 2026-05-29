#!/usr/bin/env python3
"""Prevent Cloudflare from rewriting mailto links to /cdn-cgi/l/email-protection."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAILTO_ANCHOR = re.compile(
    r'(<a\s[^>]*href="mailto:lcy861013@gmail\.com"[^>]*>.*?</a>)',
    re.IGNORECASE | re.DOTALL,
)
SKIP = {".git", "__pycache__", "node_modules", ".cursor"}


def patch(text: str) -> str:
    if "<!--email_off-->" in text:
        return text

    def repl(m: re.Match[str]) -> str:
        block = m.group(1)
        if "<!--email_off-->" in block:
            return block
        return f"<!--email_off-->{block}<!--/email_off-->"

    return MAILTO_ANCHOR.sub(repl, text)


def main() -> None:
    changed: list[str] = []
    for path in ROOT.rglob("*.html"):
        if SKIP & set(path.parts):
            continue
        original = path.read_text(encoding="utf-8")
        updated = patch(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(str(path.relative_to(ROOT)))
    print(f"Wrapped mailto links in {len(changed)} files")
    for rel in sorted(changed)[:15]:
        print(f"  {rel}")
    if len(changed) > 15:
        print(f"  ... and {len(changed) - 15} more")


if __name__ == "__main__":
    main()
