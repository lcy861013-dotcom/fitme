# -*- coding: utf-8 -*-
"""Set <lastmod> for specific sitemap <loc> entries."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
SITEMAP = ROOT / "sitemap.xml"

DATE = "2026-08-29"

# Posts that gained new prose or had their FAQ schema corrected.
POSTS = [
    "blog1", "blog7", "blog8", "blog9", "blog11", "blog14", "blog19", "blog20",
    "blog21", "blog22", "blog23", "blog24", "blog25", "blog26", "blog27",
    "blog28", "blog29", "blog30",
]
SLUGS = [f"/blog/{p}" for p in POSTS] + [f"/blog/{p}-en" for p in POSTS if p != "blog14" and p != "blog19"]
SLUGS += ["/blog/", "/"]

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
