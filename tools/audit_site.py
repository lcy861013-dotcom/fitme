# -*- coding: utf-8 -*-
"""Local consistency audit: sitemap/feed XML, JSON-LD, hreflang, internal links."""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"
SITE = "https://perfectfitme.com"

JSONLD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
HREF = re.compile(r'href="(/[^"#?]*)"')
CANON = re.compile(r'<link rel="canonical" href="([^"]+)"')
ALT = re.compile(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"')


def check_xml() -> None:
    for name in ("sitemap.xml", "feed.xml"):
        try:
            tree = ET.parse(ROOT / name)
            print(f"{name}: XML OK, top-level children = {len(list(tree.getroot()))}")
        except Exception as exc:  # noqa: BLE001
            print(f"{name}: XML ERROR -> {exc}")


def sitemap_locs() -> list[str]:
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    tree = ET.parse(ROOT / "sitemap.xml")
    return [e.text.strip() for e in tree.getroot().findall(".//s:loc", ns) if e.text]


def url_to_path(url: str) -> Path | None:
    if not url.startswith(SITE):
        return None
    rel = url[len(SITE):].strip("/")
    if rel == "":
        return ROOT / "index.html"
    candidates = [ROOT / rel, ROOT / f"{rel}.html", ROOT / rel / "index.html"]
    for c in candidates:
        if c.exists():
            return c
    return None


def check_sitemap_targets() -> None:
    missing = [u for u in sitemap_locs() if url_to_path(u) is None]
    print(f"sitemap entries missing local file: {len(missing)}")
    for u in missing:
        print("  MISSING:", u)


def check_pages() -> None:
    names = ["blog27", "blog28", "blog29", "blog27-en", "blog28-en", "blog29-en"]
    smap = set(sitemap_locs())
    for name in names:
        path = BLOG / f"{name}.html"
        text = path.read_text(encoding="utf-8")
        issues: list[str] = []

        for block in JSONLD.findall(text):
            try:
                json.loads(block.strip())
            except Exception as exc:  # noqa: BLE001
                issues.append(f"invalid JSON-LD: {exc}")

        if "noindex" in text:
            issues.append("noindex present")

        canon = CANON.findall(text)
        if len(canon) != 1:
            issues.append(f"canonical count={len(canon)}")
        elif canon[0] not in smap:
            issues.append(f"canonical not in sitemap: {canon[0]}")

        alts = dict(ALT.findall(text))
        for lang in ("ko", "en", "x-default"):
            if lang not in alts:
                issues.append(f"missing hreflang {lang}")

        for target in alts.values():
            if url_to_path(target) is None:
                issues.append(f"hreflang target missing: {target}")

        for link in set(HREF.findall(text)):
            if link.startswith(("/assets/", "/blog/img/")) or link in {
                "/favicon-32x32.png",
                "/consent-init.js",
                "/cookie-consent.js",
            }:
                continue
            if url_to_path(SITE + link) is None:
                issues.append(f"internal link unresolved: {link}")

        if "google-adsense-account" not in text:
            issues.append("missing adsense meta")

        print(f"{name}: {'OK' if not issues else issues}")


def check_ads_flag() -> None:
    ads = (ROOT / "assets" / "fitme-ads.js").read_text(encoding="utf-8")
    m = re.search(r"LIVE\s*[:=]\s*(true|false)", ads)
    print("fitme-ads.js LIVE =", m.group(1) if m else "not found")


if __name__ == "__main__":
    check_xml()
    check_sitemap_targets()
    check_pages()
    check_ads_flag()
