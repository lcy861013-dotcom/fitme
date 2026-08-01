# -*- coding: utf-8 -*-
"""Scan every HTML file for internal links/images that do not resolve locally."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
REF = re.compile(r'(?:href|src)="(/[^"]*)"')
REDIRECT_PREFIXES = ("/wp-", "/xmlrpc", "/admin", "/phpmyadmin", "/administrator")


def resolve(ref: str) -> bool:
    clean = ref.split("#")[0].split("?")[0].strip()
    if clean in ("", "/"):
        return True
    if clean.startswith(REDIRECT_PREFIXES):
        return True
    rel = clean.lstrip("/")
    for candidate in (ROOT / rel, ROOT / f"{rel}.html", ROOT / rel / "index.html"):
        if candidate.exists():
            return True
    return False


def main() -> None:
    broken: dict[str, set[str]] = {}
    for path in ROOT.rglob("*.html"):
        if any(part in {".git", "node_modules", "tools"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for ref in set(REF.findall(text)):
            if not resolve(ref):
                broken.setdefault(ref, set()).add(str(path.relative_to(ROOT)))
    if not broken:
        print("no broken internal references")
        return
    print(f"broken references: {len(broken)}")
    for ref, files in sorted(broken.items()):
        sample = ", ".join(sorted(files)[:4])
        print(f"  {ref}  <- {len(files)} file(s): {sample}")


if __name__ == "__main__":
    main()
