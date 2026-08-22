# -*- coding: utf-8 -*-
"""Estimate how a reviewer sees the blog corpus: length, template reuse, duplicate locales."""
from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"

MAIN = re.compile(r"<main\b[^>]*>(.*?)</main>", re.S | re.I)
TAG = re.compile(r"<[^>]+>")
SCRIPT = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.S | re.I)
H2 = re.compile(r"<h2\b[^>]*>(.*?)</h2>", re.S | re.I)


def body_text(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="replace")
    main = MAIN.search(raw)
    chunk = main.group(1) if main else raw
    chunk = SCRIPT.sub(" ", chunk)
    return " ".join(TAG.sub(" ", chunk).split())


def headings(path: Path) -> list[str]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    out = []
    for h in H2.findall(raw):
        text = " ".join(TAG.sub(" ", h).split())
        text = re.sub(r"^\d+[.)]\s*", "", text)
        out.append(text)
    return out


def word_count(text: str, korean: bool) -> int:
    if korean:
        # rough: Korean posts counted by characters / 2 to compare with English words
        return len(re.sub(r"\s+", "", text)) // 2
    return len(text.split())


def main() -> None:
    posts = sorted(BLOG.glob("blog*.html"))
    rows = []
    skeletons: dict[tuple, list[str]] = collections.defaultdict(list)

    for path in posts:
        rel = path.name
        korean = not rel.endswith("-en.html")
        text = body_text(path)
        wc = word_count(text, korean)
        hs = headings(path)
        rows.append((wc, rel, len(hs)))
        # normalized skeleton: generic section labels only
        norm = tuple(
            "faq" if ("자주 묻는" in h or "FAQ" in h) else
            "toc" if ("목차" in h or "Contents" in h) else
            "checklist" if ("체크리스트" in h or "hecklist" in h) else
            "other"
            for h in hs
        )
        skeletons[norm].append(rel)

    rows.sort()
    print(f"posts: {len(posts)}")
    print("\n--- thinnest 12 (approx word-equivalents) ---")
    for wc, rel, nh in rows[:12]:
        print(f"  {wc:>5}  h2={nh:<3} {rel}")
    print("\n--- longest 5 ---")
    for wc, rel, nh in rows[-5:]:
        print(f"  {wc:>5}  h2={nh:<3} {rel}")

    lengths = [wc for wc, _, _ in rows]
    print(f"\nmedian length: {sorted(lengths)[len(lengths)//2]}")
    print(f"under 600: {sum(1 for l in lengths if l < 600)} posts")
    print(f"under 900: {sum(1 for l in lengths if l < 900)} posts")

    print("\n--- shared section skeletons (template reuse) ---")
    for norm, files in sorted(skeletons.items(), key=lambda kv: -len(kv[1]))[:6]:
        if len(files) > 1:
            print(f"  {len(files)} posts share pattern {norm}")
            print(f"    {', '.join(files[:8])}{' ...' if len(files) > 8 else ''}")

    print("\n--- other language editions ---")
    for sub in sorted(p for p in BLOG.iterdir() if p.is_dir() and p.name != "img"):
        pages = list(sub.glob("*.html"))
        print(f"  /blog/{sub.name}/: {len(pages)} pages")

    ko = [r for _, r, _ in rows if not r.endswith("-en.html")]
    en = [r for _, r, _ in rows if r.endswith("-en.html")]
    print(f"\nKO posts: {len(ko)}  EN posts: {len(en)}  (paired translations = duplicate-topic risk)")


if __name__ == "__main__":
    main()
