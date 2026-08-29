# -*- coding: utf-8 -*-
"""Post-edit validation: tag balance, JSON-LD parse, FAQ schema/visible parity, link targets."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]

LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
FAQ_BLOCK = re.compile(r'<div class="faq-block">(.*?)</div>', re.S)
H3 = re.compile(r"<h3\b[^>]*>", re.I)
HREF = re.compile(r'href="(/[^"#?]*)')

BALANCED = ("main", "div", "p", "ul", "ol", "li", "table", "h1", "h2", "h3", "a", "section", "fieldset")

pages = sorted(ROOT.glob("*.html")) + sorted((ROOT / "ko").glob("*.html")) \
    + sorted((ROOT / "blog").glob("*.html"))

problems = 0
for path in pages:
    rel = path.relative_to(ROOT).as_posix()
    raw = path.read_text(encoding="utf-8")
    issues = []

    for i, block in enumerate(LD.findall(raw)):
        try:
            data = json.loads(block)
        except json.JSONDecodeError as exc:
            issues.append(f"JSON-LD #{i + 1} invalid: {exc}")
            continue
        nodes = data.get("@graph", [data]) if isinstance(data, dict) else []
        for node in nodes:
            if isinstance(node, dict) and node.get("@type") == "FAQPage":
                schema_n = len(node.get("mainEntity", []))
                fb = FAQ_BLOCK.search(raw)
                if fb:
                    visible_n = len(H3.findall(fb.group(1)))
                    if schema_n != visible_n:
                        issues.append(f"FAQ mismatch: schema {schema_n} vs visible {visible_n}")

    for tag in BALANCED:
        opens = len(re.findall(rf"<{tag}\b", raw, re.I))
        closes = len(re.findall(rf"</{tag}>", raw, re.I))
        if opens != closes:
            issues.append(f"<{tag}> {opens} open / {closes} close")

    # internal links must resolve to a file or a known route
    for href in set(HREF.findall(raw)):
        if href.startswith(("/assets/", "/blog/img/", "/cdn-cgi/")):
            continue
        if href in ("/", "/blog/", "/ads.txt", "/feed.xml", "/sitemap.xml", "/llms.txt", "/robots.txt"):
            continue
        target = href.lstrip("/")
        if (ROOT / target).exists() or (ROOT / (target + ".html")).exists():
            continue
        if (ROOT / target / "index.html").exists():
            continue
        issues.append(f"dead internal link: {href}")

    if issues:
        problems += 1
        print(f"[FAIL] {rel}")
        for msg in sorted(set(issues)):
            print(f"        {msg}")

print(f"\nchecked {len(pages)} pages — {problems} with issues" if problems
      else f"\nchecked {len(pages)} pages — all clean")
