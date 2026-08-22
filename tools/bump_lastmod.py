# -*- coding: utf-8 -*-
"""Set <lastmod> for specific sitemap <loc> entries."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
SITEMAP = ROOT / "sitemap.xml"

DATE = "2026-08-22"
SLUGS = [
    "/blog/",
    "/blog/blog20",
    "/blog/blog19-en",
    "/blog/blog18-en",
    "/blog/blog13-en",
    "/blog/blog6-en",
    "/blog/blog3-en",
    "/blog/blog8-en",
    "/blog/blog29-en",
]

text = SITEMAP.read_text(encoding="utf-8")
changed = []

for slug in SLUGS:
    loc = f"https://perfectfitme.com{slug}"
    pattern = re.compile(
        r"(<loc>" + re.escape(loc) + r"</loc>\s*<lastmod>)(\d{4}-\d{2}-\d{2})(</lastmod>)"
    )
    match = pattern.search(text)
    if not match:
        print(f"  MISS  {loc}")
        continue
    if match.group(2) == DATE:
        print(f"  same  {loc}")
        continue
    text = pattern.sub(lambda m: m.group(1) + DATE + m.group(3), text, count=1)
    changed.append((slug, match.group(2)))

SITEMAP.write_text(text, encoding="utf-8")
for slug, old in changed:
    print(f"  bump  {slug}: {old} -> {DATE}")
print(f"\n{len(changed)} entries updated")
