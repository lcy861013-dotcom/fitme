#!/usr/bin/env python3
"""Generate Atom feed.xml from blog/*.html (run from repo root: python tools/generate-feed.py)."""

import re
import xml.sax.saxutils as xmap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"
OUT = ROOT / "feed.xml"

MONTHS = {
    "jan": "01",
    "feb": "02",
    "mar": "03",
    "apr": "04",
    "may": "05",
    "jun": "06",
    "jul": "07",
    "aug": "08",
    "sep": "09",
    "oct": "10",
    "nov": "11",
    "dec": "12",
}


def parse_meta_date(html):
    m = re.search(r'<div class="meta">([^<]+)</div>', html)
    if not m:
        return None
    raw = m.group(1).strip().split("·")[0].strip()
    dots = re.match(r"(\d{4})\.(\d{2})\.(\d{2})", raw)
    if dots:
        return f"{dots.group(1)}-{dots.group(2)}-{dots.group(3)}T12:00:00Z"
    eng = re.match(r"([A-Za-z]+)\s+(\d+),\s+(\d{4})", raw)
    if eng:
        mo = MONTHS.get(eng.group(1).lower()[:3])
        if mo:
            day = int(eng.group(2))
            y = eng.group(3)
            return f"{y}-{mo}-{day:02d}T12:00:00Z"
    return None


def main():
    entries = []
    for path in sorted(BLOG.glob("*.html")):
        if path.name == "index.html":
            continue
        html = path.read_text(encoding="utf-8")
        mt = re.search(r"<title>([^<]+)</title>", html)
        md = re.search(r'<meta name="description" content="([^"]*)"', html)
        if not mt:
            continue
        title = mt.group(1).replace(" | FITME", "").strip()
        desc = md.group(1) if md else ""
        slug = path.stem
        url = f"https://perfectfitme.com/blog/{slug}"
        updated = parse_meta_date(html) or "2026-05-11T12:00:00Z"
        entries.append((updated, url, title, desc, slug))

    entries.sort(key=lambda x: x[0], reverse=True)
    now = "2026-05-12T12:00:00Z"

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom">',
        "  <title>FITME — Style &amp; Fit Blog</title>",
        "  <link href=\"https://perfectfitme.com/blog/\" rel=\"alternate\"/>",
        "  <link href=\"https://perfectfitme.com/feed.xml\" rel=\"self\"/>",
        "  <id>https://perfectfitme.com/blog/</id>",
        f"  <updated>{now}</updated>",
        "  <subtitle>Body proportion guides, fit tips, and measurement how-tos.</subtitle>",
        "  <author><name>FITME</name><uri>https://perfectfitme.com/</uri></author>",
    ]
    for updated, url, title, desc, slug in entries[:80]:
        lines.append("  <entry>")
        lines.append(f"    <title>{xmap.escape(title)}</title>")
        lines.append(f"    <link href=\"{xmap.escape(url)}\"/>")
        lines.append(f"    <id>{xmap.escape(url)}</id>")
        lines.append(f"    <updated>{updated}</updated>")
        lines.append(f"    <summary>{xmap.escape(desc)}</summary>")
        lines.append("  </entry>")
    lines.append("</feed>")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({len(entries)} entries)")


if __name__ == "__main__":
    main()
