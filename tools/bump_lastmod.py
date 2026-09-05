# -*- coding: utf-8 -*-
from __future__ import annotations
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
SITEMAP = ROOT / "sitemap.xml"
DATE = "2026-09-05"
SLUGS = [
    "/", "/size-check", "/ko/size-check", "/blog/",
    "/blog/blog2", "/blog/blog3", "/blog/blog3-en",
    "/blog/blog14", "/blog/blog14-en",
    "/blog/blog20", "/blog/blog20-en",
    "/blog/blog27", "/blog/blog29", "/blog/blog29-en",
    "/blog/blog30",
]
text = SITEMAP.read_text(encoding="utf-8")
n = 0
for slug in SLUGS:
    loc = f"https://perfectfitme.com{slug}"
    pattern = re.compile(
        r"(<loc>" + re.escape(loc) + r"</loc>\s*<lastmod>)(\d{4}-\d{2}-\d{2})(</lastmod>)"
    )
    m = pattern.search(text)
    if not m:
        print("MISS", loc)
        continue
    if m.group(2) != DATE:
        text = pattern.sub(lambda x: x.group(1) + DATE + x.group(3), text, count=1)
        n += 1
        print("bump", slug, m.group(2), "->", DATE)
SITEMAP.write_text(text, encoding="utf-8")
print(n, "updated")
