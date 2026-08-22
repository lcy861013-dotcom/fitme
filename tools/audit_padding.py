# -*- coding: utf-8 -*-
"""Find padding artifacts across blog posts: near-duplicate paragraphs, wall-of-text
sections, and stray Latin words inside Korean prose."""
from __future__ import annotations

import re
import sys
from itertools import combinations
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"

MAIN = re.compile(r"<main\b[^>]*>(.*?)</main>", re.S | re.I)
SCRIPT = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.S | re.I)
TAG = re.compile(r"<[^>]+>")
PARA = re.compile(r"<p\b[^>]*>(.*?)</p>", re.S | re.I)
SECTION = re.compile(r"<h2\b[^>]*>(.*?)</h2>(.*?)(?=<h2\b|\Z)", re.S | re.I)

# Latin word sitting inside Korean text (AI-generation leftovers).
STRAY = re.compile(r"[가-힣][^<>\n]{0,12}?[·,、]?\s*\b([a-z]{5,})\b\s*[가-힣]")
ALLOW = {
    "fitme", "adsense", "google", "asos", "amazon", "uniqlo", "musinsa", "kibbe",
    "https", "email", "style", "sizes", "guide", "hover", "index", "print",
}


def clean(fragment: str) -> str:
    fragment = SCRIPT.sub(" ", fragment)
    return " ".join(TAG.sub(" ", fragment).split())


def tokens(text: str) -> set:
    text = re.sub(r"[^0-9A-Za-z가-힣 ]", " ", text)
    return {t for t in text.split() if len(t) > 1}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def main() -> None:
    dup_hits = []
    wall_hits = []
    stray_hits = []

    for path in sorted(BLOG.glob("blog*.html")):
        raw = path.read_text(encoding="utf-8", errors="replace")
        main_m = MAIN.search(raw)
        body = main_m.group(1) if main_m else raw

        paras = [clean(p) for p in PARA.findall(body)]
        paras = [p for p in paras if len(p) > 120]
        for (i, a), (j, b) in combinations(list(enumerate(paras)), 2):
            score = jaccard(tokens(a), tokens(b))
            if score >= 0.45:
                dup_hits.append((score, path.name, a[:90], b[:90]))

        for title, chunk in SECTION.findall(body):
            text = clean(chunk)
            n_para = len(PARA.findall(chunk))
            if len(text) > 420 and n_para <= 1 and "<ul" not in chunk and "<table" not in chunk:
                wall_hits.append((len(text), path.name, clean(title)))

        for m in STRAY.finditer(clean(body)):
            word = m.group(1).lower()
            if word not in ALLOW:
                stray_hits.append((path.name, m.group(0).strip()))

    print("=== near-duplicate paragraphs within same post (>=0.45 overlap) ===")
    for score, name, a, b in sorted(dup_hits, reverse=True):
        print(f"[{score:.2f}] {name}")
        print(f"   A: {a}")
        print(f"   B: {b}")
    if not dup_hits:
        print("  none")

    print("\n=== wall-of-text sections (single long paragraph, no list/table) ===")
    for length, name, title in sorted(wall_hits, reverse=True):
        print(f"  {length:>5} chars  {name}  <- {title}")
    if not wall_hits:
        print("  none")

    print("\n=== stray Latin words inside Korean prose ===")
    for name, ctx in stray_hits:
        print(f"  {name}: ...{ctx}...")
    if not stray_hits:
        print("  none")


if __name__ == "__main__":
    main()
