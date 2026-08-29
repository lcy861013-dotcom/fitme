# -*- coding: utf-8 -*-
"""Compare each KO post against its EN counterpart to find versions left thinner.

Length is a weak signal across these two languages: any character-to-word divisor
you pick is arbitrary enough to flag healthy posts. Section count and FAQ count are
structural, so a missing <h2> is real evidence that one version dropped content
while a length ratio of 0.7 usually is not. Treat the section columns as the finding
and the size columns as context only.
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
    # Rough only: Korean packs about 2.8 characters into an English word's worth of meaning.
    size = len(re.sub(r"\s+", "", text)) / 2.8 if korean else len(text.split())
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

rows.sort(key=lambda r: r[3]["h2"] - r[2]["h2"])

print("Section gap is the real signal. Size columns are indicative only.")
print(f"{'post':<10} {'h2 ko/en':>9} {'gap':>5} {'faq ko/en':>10}  {'KO~':>6} {'EN~':>6}  note")
print("-" * 78)
for ratio, slug, ko, en in rows:
    gap = en["h2"] - ko["h2"]
    if gap <= -2:
        note = f"EN missing {-gap} sections"
    elif gap >= 2:
        note = f"KO missing {gap} sections"
    elif ko["faq"] != en["faq"]:
        note = "FAQ count differs"
    else:
        note = ""
    print(f"{slug:<10} {ko['h2']:>4}/{en['h2']:<4} {gap:>+5} {ko['faq']:>5}/{en['faq']:<4}  "
          f"{ko['size']:>6} {en['size']:>6}  {note}")

en_missing = [r for r in rows if r[3]["h2"] - r[2]["h2"] <= -2]
ko_missing = [r for r in rows if r[3]["h2"] - r[2]["h2"] >= 2]
faq_gap = [r for r in rows if r[2]["faq"] != r[3]["faq"]]

print(f"\nEN missing 2+ sections ({len(en_missing)}): "
      f"{', '.join(f'{r[1]} ({r[2]['h2']}->{r[3]['h2']})' for r in en_missing) or 'none'}")
print(f"KO missing 2+ sections ({len(ko_missing)}): "
      f"{', '.join(f'{r[1]} ({r[2]['h2']}->{r[3]['h2']})' for r in ko_missing) or 'none'}")
print(f"FAQ count differs ({len(faq_gap)}): "
      f"{', '.join(f'{r[1]}({r[2]['faq']}/{r[3]['faq']})' for r in faq_gap) or 'none'}")
print("\nRun tools/_section_diff.py <slug> to see which sections are absent.")
