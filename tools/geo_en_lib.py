#!/usr/bin/env python3
"""Shared GEO injection helpers for English blog posts."""
from __future__ import annotations

import json
import re
from pathlib import Path

GEO_CSS = (
    ".lead-answer{font-size:16px;line-height:1.85;color:var(--text);margin-bottom:28px;"
    "padding:16px 18px;background:rgba(212,168,75,0.06);border-left:3px solid var(--accent);"
    "border-radius:0 8px 8px 0;}"
    ".faq-block{margin:36px 0 8px;}"
    ".faq-block h3{font-family:'DM Sans',sans-serif;font-size:16px;font-weight:700;"
    "margin:22px 0 8px;color:var(--text);}"
    ".faq-block p{font-size:15px;line-height:1.85;color:#d0d0d0;margin-bottom:14px;}"
)

FAQ_SECTION_OLD = re.compile(
    r"  <h2>FAQ[^<]*</h2>\s*(?:<p><strong>Q\..*?</p>\s*)+",
    re.DOTALL,
)

RELATED_BLOCK = re.compile(r"\n    <div class=\"related\">")


def faq_html_block(title: str, faqs: list[tuple[str, str]]) -> str:
    lines = [f"  <h2>{title}</h2>", '  <div class="faq-block">']
    for q, a in faqs:
        lines.append(f"    <h3>{q}</h3>")
        lines.append(f"    <p>{a}</p>")
    lines.append("  </div>")
    return "\n".join(lines)


def faq_schema(canonical: str, faqs: list[tuple[str, str]]) -> str:
    entities = [
        {
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for q, a in faqs
    ]
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities,
        "url": canonical,
    }
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(data, ensure_ascii=False, indent=2)
        + "\n</script>"
    )


def inject_css(raw: str) -> str:
    if ".lead-answer" in raw:
        return raw
    needle = ".guide-img{width:100%;border-radius:12px;margin:28px 0;border:1px solid var(--border);}"
    if needle not in raw:
        return raw
    return raw.replace(needle, needle + "\n" + GEO_CSS, 1)


def inject_lead(raw: str, lead: str) -> str:
    if 'class="lead-answer"' in raw:
        return raw
    m = re.search(r'(<img[^>]*class="guide-img"[^>]*>\s*)', raw, re.I)
    if not m:
        return raw
    return raw[: m.end()] + lead + "\n\n" + raw[m.end() :]


def inject_faq_schema(raw: str, schema: str) -> str:
    if '"@type": "FAQPage"' in raw:
        return raw
    return raw.replace(
        "</script>\n  <link rel=\"stylesheet\" href=\"/assets/satellite-pages-theme.css",
        "</script>\n" + schema + "\n  <link rel=\"stylesheet\" href=\"/assets/satellite-pages-theme.css",
        1,
    )


def inject_faq_body(raw: str, title: str, meta: dict) -> str:
    if 'class="faq-block"' in raw:
        return raw
    new_block = faq_html_block(title, meta["faqs"])
    m = meta.get("faq_old")
    if m and (hit := m.search(raw)):
        return raw[: hit.start()] + new_block + "\n\n" + raw[hit.end() :]
    before = meta.get("faq_insert_before")
    if before and (hit := before.search(raw)):
        return raw[: hit.start()] + "\n\n" + new_block + "\n" + raw[hit.start() :]
    return raw


def bump_modified(raw: str, modified: str) -> str:
    if '"dateModified"' not in raw:
        return raw
    return re.sub(
        r'"dateModified":\s*"[^"]*"',
        f'"dateModified": "{modified}"',
        raw,
        count=1,
    )


def process_file(path: Path, meta: dict, faq_title: str, modified: str) -> bool:
    raw = path.read_text(encoding="utf-8")
    new = raw
    new = inject_css(new)
    new = inject_lead(new, meta["lead"])
    new = inject_faq_body(new, faq_title, meta)
    new = inject_faq_schema(new, faq_schema(meta["canonical"], meta["faqs"]))
    new = bump_modified(new, modified)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False
