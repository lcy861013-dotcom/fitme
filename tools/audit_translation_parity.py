# -*- coding: utf-8 -*-
"""Compare each KO post against its EN counterpart to find versions left thinner.

Korean is far denser per character than English, so raw length is meaningless.
Section count (h2/h3) and FAQ count are structural and comparable across languages.
"""
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
H2 = re.compile(r"<h2\b[^>]*>", re.I)
H3 = re.compile(r"<h3\b[^>]*>", re.I)
LI = re.compile(r"<li\b[^>]*>", re.I)
TABLE = re.compile(r"<table\b", re.I)
FB = re.compile(r'<div class="faq-block">(.*?)</div>', re.S)


def body(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="replace")
    m = MAIN.search(raw)
    chunk = SCRIPT.sub(" ", m.group(1) if m else raw)
    return chunk


def stats(path: Path) -> dict:
    chunk = body(path)
    text = " ".join(TAG.sub(" ", chunk).split())
    korean = not path.name.endswith("-en.html")
    # Korean: characters / 2.2 approximates English word equivalents
    size = len(re.sub(r"\s+", "", text)) // 2.2 if korean else len(text.split())
    fb = FB.search(chunk)
    return {
        "size": int(size),
        "h2": len(H2.findall(chunk)),
        "h3": len(H3.findall(chunk)),
        "li": len(LI.findall(chunk)),
        "tables": len(TABLE.findall(chunk)),
        "faq": len(re.findall(r"<h3\b", fb.group(1), re.I)) if fb else 0,
    }


rows = []
for ko_path in sorted(BLOG.glob("blog*.html")):
    if ko_path.name.endswith("-en.html"):
        continue
    en_path = BLOG / ko_path.name.replace(".html", "-en.html")
    if not en_path.exists():
        print(f"  no EN counterpart: {ko_path.name}")
        continue
    ko, en = stats(ko_path), stats(en_path)
    ratio = en["size"] / ko["size"] if ko["size"] else 0
    rows.append((ratio, ko_path.stem, ko, en))

rows.sort()

print("EN size / KO size — below 0.75 means the English version lost content")
print(f"{'post':<10} {'ratio':>6} {'KO':>6} {'EN':>6}   {'h2 ko/en':>9} {'faq ko/en':>10} {'li ko/en':>9}")
print("-" * 74)
for ratio, slug, ko, en in rows:
    flag = "  <-- thin" if ratio < 0.75 else ("  <-- KO thin" if ratio > 1.4 else "")
    print(f"{slug:<10} {ratio:>6.2f} {ko['size']:>6} {en['size']:>6}   "
          f"{ko['h2']:>4}/{en['h2']:<4} {ko['faq']:>5}/{en['faq']:<4} {ko['li']:>4}/{en['li']:<4}{flag}")

thin = [r for r in rows if r[0] < 0.75]
ko_thin = [r for r in rows if r[0] > 1.4]
faq_gap = [r for r in rows if r[2]["faq"] != r[3]["faq"]]
h2_gap = [r for r in rows if abs(r[2]["h2"] - r[3]["h2"]) >= 2]

print(f"\nEN thinner than KO (<0.75): {len(thin)} — {', '.join(r[1] for r in thin) or 'none'}")
print(f"KO thinner than EN (>1.40): {len(ko_thin)} — {', '.join(r[1] for r in ko_thin) or 'none'}")
print(f"FAQ count differs: {len(faq_gap)} — {', '.join(f'{r[1]}({r[2]['faq']}/{r[3]['faq']})' for r in faq_gap) or 'none'}")
print(f"section count differs by 2+: {len(h2_gap)} — {', '.join(f'{r[1]}({r[2]['h2']}/{r[3]['h2']})' for r in h2_gap) or 'none'}")
