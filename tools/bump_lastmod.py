# -*- coding: utf-8 -*-
"""Set <lastmod> for specific sitemap <loc> entries."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
SITEMAP = ROOT / "sitemap.xml"

DATE = "2026-09-05"
SLUGS = [
    "/size-check",
    "/ko/size-check",
    "/blog/",
    "/blog/blog4-en",
    "/blog/blog5-en",
    "/blog/blog7-en",
    "/blog/blog8-en",
    "/blog/blog9-en",
    "/blog/blog10-en",
    "/blog/blog13",
    "/blog/blog14",
    "/blog/blog19",
    "/blog/blog20",
    "/blog/blog20-en",
    "/blog/blog21",
    "/blog/blog21-en",
    "/blog/blog22",
    "/blog/blog22-en",
    "/blog/blog23",
    "/blog/blog23-en",
    "/blog/blog24",
    "/blog/blog24-en",
    "/blog/blog26-en",
    # wall-of-text cleanup on EN flagships
    "/blog/blog2-en",
    "/blog/blog3-en",
    "/blog/blog6-en",
    "/blog/blog11-en",
    "/blog/blog12-en",
    "/blog/blog13-en",
    "/blog/blog14-en",
    "/blog/blog15-en",
    "/blog/blog16-en",
    "/blog/blog18-en",
    "/blog/blog19-en",
]

text = SITEMAP.read_text(encoding="utf-8")
changed = []
missed = []

for slug in SLUGS:
    loc = f"https://perfectfitme.com{slug}"
    pattern = re.compile(
        r"(<loc>" + re.escape(loc) + r"</loc>\s*<lastmod>)(\d{4}-\d{2}-\d{2})(</lastmod>)"
    )
    match = pattern.search(text)
    if not match:
        missed.append(loc)
        continue
    if match.group(2) == DATE:
        continue
    text = pattern.sub(lambda m: m.group(1) + DATE + m.group(3), text, count=1)
    changed.append((slug, match.group(2)))

SITEMAP.write_text(text, encoding="utf-8")
for slug, old in changed:
    print(f"  bump  {slug}: {old} -> {DATE}")
for loc in missed:
    print(f"  MISS  {loc}")
print(f"\n{len(changed)} entries updated, {len(missed)} not found")
