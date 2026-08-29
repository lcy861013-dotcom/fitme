# -*- coding: utf-8 -*-
"""Add FAQPage schema to Korean posts that show FAQ prose but declare no schema.

These posts write their FAQ as <p><strong>Q. …</strong> — answer</p> instead of the
<div class="faq-block"> markup used elsewhere, so sync_faq_schema.py cannot see them.
Their English counterparts already carry FAQPage, so the Korean pages were losing
the same rich-result eligibility for no reason.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"

SLUGS = ["blog21", "blog22", "blog23", "blog24", "blog25"]

FAQ_SECTION = re.compile(
    r"<h2\b[^>]*>[^<]*FAQ[^<]*</h2>(.*?)(?=<h2\b|<div class=\"nav-links\"|\Z)", re.S | re.I
)
QA = re.compile(r"<p>\s*<strong>\s*Q[.。]?\s*(.*?)</strong>\s*(?:&mdash;|—|-)?\s*(.*?)</p>", re.S | re.I)
INLINE = re.compile(r"</?(?:a|strong|em|b|i|span|code|small|u|s|mark|sup|sub)\b[^>]*>", re.I)
BLOCK = re.compile(r"<[^>]+>")
ENTITY = re.compile(r"&(?:nbsp|amp|lt|gt|quot|#39|mdash|ndash);")
ENT_MAP = {
    "&nbsp;": " ", "&amp;": "&", "&lt;": "<", "&gt;": ">",
    "&quot;": '"', "&#39;": "'", "&mdash;": "—", "&ndash;": "–",
}


def plain(fragment: str) -> str:
    text = INLINE.sub("", fragment)
    text = BLOCK.sub(" ", text)
    text = ENTITY.sub(lambda m: ENT_MAP.get(m.group(0), " "), text)
    return " ".join(text.split())


updated = 0
for slug in SLUGS:
    path = BLOG / f"{slug}.html"
    raw = path.read_text(encoding="utf-8")

    if "FAQPage" in raw:
        print(f"  skip  {slug} (already has FAQPage)")
        continue

    section = FAQ_SECTION.search(raw)
    if not section:
        print(f"  WARN  {slug}: no FAQ section found")
        continue

    entities = []
    for question, answer in QA.findall(section.group(1)):
        q, a = plain(question), plain(answer)
        if not q or not a:
            continue
        entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        })

    if not entities:
        print(f"  WARN  {slug}: FAQ section had no Q/A pairs")
        continue

    payload = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}
    block = ('<script type="application/ld+json">\n  '
             + json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
             + "\n  </script>\n")

    idx = raw.rindex("</head>")
    raw = raw[:idx] + block + raw[idx:]
    path.write_text(raw, encoding="utf-8")
    updated += 1
    print(f"  added {slug}: {len(entities)} questions")
    for e in entities:
        print(f"           Q: {e['name'][:64]}")

print(f"\n{updated} posts updated")
