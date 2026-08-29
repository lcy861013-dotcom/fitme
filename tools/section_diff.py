# -*- coding: utf-8 -*-
"""Print KO vs EN section headings side by side for a post pair."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"

MAIN = re.compile(r"<main\b[^>]*>(.*?)</main>", re.S | re.I)
SCRIPT = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.S | re.I)
TAG = re.compile(r"<[^>]+>")
SEC = re.compile(r"<h([23])\b[^>]*>(.*?)</h\1>(.*?)(?=<h[23]\b|\Z)", re.S | re.I)


def sections(path: Path):
    raw = path.read_text(encoding="utf-8", errors="replace")
    m = MAIN.search(raw)
    chunk = SCRIPT.sub(" ", m.group(1) if m else raw)
    out = []
    for level, head, bodytext in SEC.findall(chunk):
        title = " ".join(TAG.sub(" ", head).split())
        words = len(" ".join(TAG.sub(" ", bodytext).split()))
        out.append((level, title, words))
    return out


for slug in sys.argv[1:]:
    ko = sections(BLOG / f"{slug}.html")
    en = sections(BLOG / f"{slug}-en.html")
    print("=" * 96)
    print(f"{slug}   KO sections: {len(ko)}   EN sections: {len(en)}")
    print("-" * 96)
    for i in range(max(len(ko), len(en))):
        k = f"h{ko[i][0]} {ko[i][1][:40]} ({ko[i][2]}c)" if i < len(ko) else ""
        e = f"h{en[i][0]} {en[i][1][:40]} ({en[i][2]}c)" if i < len(en) else ""
        print(f"  {k:<52} | {e}")
