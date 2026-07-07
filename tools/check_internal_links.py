#!/usr/bin/env python3
"""Scan repo HTML/XML for internal href/src paths and report missing targets."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#", "javascript:")
HREF_RE = re.compile(r"""(?:href|src)=["']([^"']+)["']""", re.I)


def resolve(path: str) -> Path | None:
    if path.startswith(SKIP_PREFIXES):
        return None
    if path.startswith("//"):
        return None
    clean = path.split("?")[0].split("#")[0]
    if not clean or clean == "/":
        return ROOT / "index.html"
    if clean.endswith("/"):
        # directory index
        for name in ("index.html", "index-en.html"):
            candidate = ROOT / clean.lstrip("/") / name
            if candidate.is_file():
                return candidate
        return ROOT / clean.lstrip("/") / "index.html"
    rel = clean.lstrip("/")
    direct = ROOT / rel
    if direct.is_file():
        return direct
    if direct.with_suffix(".html").is_file():
        return direct.with_suffix(".html")
    # extensionless blog/page slug
    if (ROOT / f"{rel}.html").is_file():
        return ROOT / f"{rel}.html"
    return direct


def main() -> int:
    broken: list[tuple[str, str, str]] = []
    checked = 0
    for file in ROOT.rglob("*"):
        if file.suffix.lower() not in {".html", ".xml", ".js"}:
            continue
        if "node_modules" in file.parts:
            continue
        text = file.read_text(encoding="utf-8", errors="ignore")
        for match in HREF_RE.finditer(text):
            raw = match.group(1)
            if not raw.startswith("/"):
                continue
            target = resolve(raw)
            if target is None:
                continue
            checked += 1
            if not target.is_file():
                broken.append((str(file.relative_to(ROOT)), raw, str(target.relative_to(ROOT))))

    print(f"Checked {checked} internal paths")
    if not broken:
        print("No broken internal links found in repo.")
        return 0

    print(f"\nBroken links ({len(broken)}):")
    seen = set()
    for src, href, _ in sorted(broken):
        key = (href, src)
        if key in seen:
            continue
        seen.add(key)
        print(f"  {href}")
        print(f"    in {src}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
