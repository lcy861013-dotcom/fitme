# -*- coding: utf-8 -*-
"""Find posts competing for the same query: title/keyword overlap plus body similarity."""
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
TITLE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
DESC = re.compile(r'<meta name="description" content="([^"]*)"', re.I)

STOP = {
    "the", "and", "for", "you", "your", "with", "that", "this", "from", "how",
    "what", "are", "not", "但", "fitme", "guide", "body", "not", "why", "when",
    "지금", "그리고", "하는", "위한", "가장", "이렇게", "합니다", "있습니다",
}


def text_of(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="replace")
    m = MAIN.search(raw)
    chunk = m.group(1) if m else raw
    chunk = SCRIPT.sub(" ", chunk)
    return " ".join(TAG.sub(" ", chunk).split())


def meta_of(path: Path) -> tuple[str, str]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    t = TITLE.search(raw)
    d = DESC.search(raw)
    return (
        " ".join(TAG.sub(" ", t.group(1)).split()) if t else "",
        d.group(1) if d else "",
    )


def keywords(text: str) -> set:
    text = re.sub(r"[^0-9A-Za-z가-힣 ]", " ", text.lower())
    return {w for w in text.split() if len(w) > 2 and w not in STOP}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def main() -> None:
    posts = {}
    for path in sorted(BLOG.glob("blog*.html")):
        title, desc = meta_of(path)
        posts[path.name] = {
            "title": title,
            "title_kw": keywords(title + " " + desc),
            "body_kw": keywords(text_of(path)),
            "lang": "en" if path.name.endswith("-en.html") else "ko",
        }

    pairs = []
    for a, b in combinations(posts, 2):
        pa, pb = posts[a], posts[b]
        if pa["lang"] != pb["lang"]:
            continue  # KO/EN pairs are intentional translations
        t = jaccard(pa["title_kw"], pb["title_kw"])
        y = jaccard(pa["body_kw"], pb["body_kw"])
        if t >= 0.22 or y >= 0.52:
            pairs.append((t, y, a, b))

    pairs.sort(key=lambda r: -(r[0] * 2 + r[1]))
    print("=== posts likely competing for the same query ===")
    print("(title-overlap / body-overlap)\n")
    for t, y, a, b in pairs:
        print(f"[title {t:.2f} | body {y:.2f}]")
        print(f"   {a}: {posts[a]['title'][:78]}")
        print(f"   {b}: {posts[b]['title'][:78]}")
    if not pairs:
        print("  none")
    print(f"\n{len(pairs)} overlapping pairs")


if __name__ == "__main__":
    main()
