# -*- coding: utf-8 -*-
"""Regenerate FAQPage mainEntity from the visible FAQ block so schema matches the page.

Google treats structured data that doesn't match visible content as invalid, so the
visible <div class="faq-block"> is the single source of truth here.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"

FB = re.compile(r'<div class="faq-block">(.*?)</div>', re.S)
LD = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)
ENTITY = re.compile(r"&(?:nbsp|amp|lt|gt|quot|#39);")
ENT_MAP = {"&nbsp;": " ", "&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": '"', "&#39;": "'"}
QA = re.compile(r"<h3\b[^>]*>(.*?)</h3>(.*?)(?=<h3\b|\Z)", re.S | re.I)

# Inline tags sit mid-word, so dropping them must not leave a space behind —
# Korean has no word spaces, and "<strong>단면</strong>입니다" would become "단면 입니다".
INLINE = re.compile(r"</?(?:a|strong|em|b|i|span|code|small|u|s|mark|sup|sub)\b[^>]*>", re.I)
BLOCK = re.compile(r"<[^>]+>")


def plain(fragment: str) -> str:
    text = INLINE.sub("", fragment)
    text = BLOCK.sub(" ", text)
    text = ENTITY.sub(lambda m: ENT_MAP.get(m.group(0), " "), text)
    return " ".join(text.split())


def visible_faq(raw: str) -> list[dict]:
    block = FB.search(raw)
    if not block:
        return []
    out = []
    for question, answer in QA.findall(block.group(1)):
        q, a = plain(question), plain(answer)
        if q and a:
            out.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            })
    return out


def sync(path: Path) -> str | None:
    raw = path.read_text(encoding="utf-8")
    faq = visible_faq(raw)
    if not faq:
        return None

    changed = None

    def repl(m: re.Match) -> str:
        nonlocal changed
        if changed:
            return m.group(0)
        try:
            data = json.loads(m.group(2))
        except json.JSONDecodeError:
            return m.group(0)

        nodes = data.get("@graph") if isinstance(data, dict) and "@graph" in data else \
            ([data] if isinstance(data, dict) else None)
        if not nodes:
            return m.group(0)

        target = next((n for n in nodes if isinstance(n, dict) and n.get("@type") == "FAQPage"), None)
        if target is None:
            return m.group(0)

        old = target.get("mainEntity", [])
        old_pairs = [(q.get("name"), q.get("acceptedAnswer", {}).get("text")) for q in old]
        new_pairs = [(q["name"], q["acceptedAnswer"]["text"]) for q in faq]
        if old_pairs == new_pairs:
            return m.group(0)

        target["mainEntity"] = faq
        changed = f"{len(old)} -> {len(faq)} questions"
        return m.group(1) + "\n  " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n  " + m.group(3)

    updated = LD.sub(repl, raw)
    if changed:
        path.write_text(updated, encoding="utf-8")
    return changed


count = 0
for path in sorted(BLOG.glob("blog*.html")):
    result = sync(path)
    if result:
        count += 1
        print(f"  synced {path.name}: {result}")

print(f"\n{count} posts updated")
