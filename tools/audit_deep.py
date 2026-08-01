# -*- coding: utf-8 -*-
"""Wider site audit: encoding leftovers, head tags, duplicates, alt text, asset weight."""
from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "node_modules", "tools", "canvases"}

TITLE = re.compile(r"<title>(.*?)</title>", re.S)
DESC = re.compile(r'<meta name="description" content="(.*?)"', re.S)
CANON = re.compile(r'<link rel="canonical"')
ALT_RE = re.compile(r"<img\b[^>]*>", re.I)
H1 = re.compile(r"<h1\b", re.I)
LANG = re.compile(r'<html[^>]*\blang="([^"]+)"')
MOJIBAKE = re.compile(r"â€|Â[ °]|ì„|ë‹|ã…|\ufffd|ï¿½")


def pages() -> list[Path]:
    out = []
    for path in sorted(ROOT.rglob("*.html")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        out.append(path)
    return out


def main() -> None:
    titles: dict[str, list[str]] = collections.defaultdict(list)
    descs: dict[str, list[str]] = collections.defaultdict(list)
    problems: list[str] = []

    for path in pages():
        rel = str(path.relative_to(ROOT)).replace("\\", "/")
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            problems.append(f"[encoding] {rel}: not valid UTF-8")
            text = raw.decode("utf-8", "replace")

        if MOJIBAKE.search(text):
            problems.append(f"[mojibake] {rel}")
        if "??" in re.sub(r"<script[\s\S]*?</script>", "", text):
            problems.append(f"[?? left] {rel}")

        title_match = TITLE.search(text)
        if not title_match:
            problems.append(f"[no title] {rel}")
        else:
            title = " ".join(title_match.group(1).split())
            titles[title].append(rel)
            if len(title) > 65:
                problems.append(f"[title {len(title)} chars] {rel}: {title[:70]}")

        desc_match = DESC.search(text)
        if not desc_match:
            problems.append(f"[no description] {rel}")
        else:
            desc = " ".join(desc_match.group(1).split())
            descs[desc].append(rel)
            if len(desc) > 165:
                problems.append(f"[description {len(desc)} chars] {rel}")
            elif len(desc) < 60:
                problems.append(f"[description short {len(desc)}] {rel}")

        if not CANON.search(text):
            problems.append(f"[no canonical] {rel}")

        h1_count = len(H1.findall(text))
        if h1_count != 1:
            problems.append(f"[h1 count {h1_count}] {rel}")

        if not LANG.search(text):
            problems.append(f"[no html lang] {rel}")

        for tag in ALT_RE.findall(text):
            if "alt=" not in tag:
                problems.append(f"[img without alt] {rel}: {tag[:70]}")
            elif 'alt=""' in tag and "decorative" not in tag:
                problems.append(f"[img empty alt] {rel}")

    for title, files in titles.items():
        if len(files) > 1:
            problems.append(f"[duplicate title] {title[:55]} -> {', '.join(files)}")
    for desc, files in descs.items():
        if len(files) > 1:
            problems.append(f"[duplicate description] {desc[:45]} -> {', '.join(files)}")

    heavy = []
    for path in sorted(ROOT.rglob("*")):
        if path.is_dir() or any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".mp4", ".svg", ".js", ".css"}:
            size = path.stat().st_size
            if size > 250 * 1024:
                heavy.append((size, str(path.relative_to(ROOT)).replace("\\", "/")))

    print(f"pages checked: {len(pages())}")
    print(f"problems: {len(problems)}")
    for line in problems:
        print("  " + line)
    print("\nassets over 250 KB:")
    for size, rel in sorted(heavy, reverse=True):
        print(f"  {size // 1024} KB  {rel}")


if __name__ == "__main__":
    main()
