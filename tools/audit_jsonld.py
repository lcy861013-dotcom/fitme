# -*- coding: utf-8 -*-
"""Validate every JSON-LD block on the site."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
BLOCK = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def main() -> None:
    bad = 0
    blocks = 0
    for path in sorted(ROOT.rglob("*.html")):
        if any(part in {".git", "node_modules", "tools"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw in BLOCK.findall(text):
            blocks += 1
            try:
                json.loads(raw.strip())
            except Exception as exc:  # noqa: BLE001
                bad += 1
                print(f"BAD: {path.relative_to(ROOT)} -> {exc}")
    print(f"checked {blocks} JSON-LD blocks, invalid: {bad}")


if __name__ == "__main__":
    main()
