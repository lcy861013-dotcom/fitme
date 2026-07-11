#!/usr/bin/env python3
"""Batch fixes from deep site audit: ads cache bust, short KO noindex."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHORT_KO = ("blog14", "blog20", "blog26")


def bump_ads_refs() -> int:
    n = 0
    for f in ROOT.rglob("*.html"):
        if "node_modules" in f.parts:
            continue
        raw = f.read_bytes()
        new = raw.replace(b"fitme-ads.js?v=9", b"fitme-ads.js?v=10")
        new = new.replace(b"fitme-ads.css?v=9", b"fitme-ads.css?v=10")
        new = new.replace(b"cookie-consent.js?v=9", b"cookie-consent.js?v=12")
        new = new.replace(b"cookie-consent.js?v=10", b"cookie-consent.js?v=12")
        new = new.replace(b"cookie-consent.js?v=11", b"cookie-consent.js?v=12")
        if new != raw:
            f.write_bytes(new)
            n += 1
    return n


def noindex_short_ko() -> None:
    for slug in SHORT_KO:
        f = ROOT / "blog" / f"{slug}.html"
        if not f.exists():
            continue
        raw = f.read_bytes()
        if b'name="robots"' in raw:
            raw2 = re.sub(
                br'<meta name="robots" content="[^"]*">',
                b'<meta name="robots" content="noindex, follow">',
                raw,
                count=1,
            )
        else:
            raw2 = raw.replace(
                b"<meta charset=",
                b'<meta name="robots" content="noindex, follow">\n<meta charset=',
                1,
            )
            if raw2 == raw:
                raw2 = raw.replace(
                    b"<head>",
                    b'<head>\n<meta name="robots" content="noindex, follow">',
                    1,
                )
        # also strip ad slots from short KO during review
        raw2 = re.sub(
            br'\r?\n\s*<div class="fitme-ad-slot"[^>]*>.*?</div>',
            b"",
            raw2,
            flags=re.DOTALL,
        )
        if raw2 != raw:
            f.write_bytes(raw2)
            print(f"noindex+strip-ads {f.name}")


def clean_sitemap() -> None:
    sm = ROOT / "sitemap.xml"
    text = sm.read_text(encoding="utf-8")
    for slug in SHORT_KO:
        text = re.sub(
            rf"\n\s*<url>\s*\n\s*<loc>https://perfectfitme\.com/blog/{slug}</loc>.*?</url>\s*",
            "\n",
            text,
            flags=re.DOTALL,
        )
        # remove ko hreflang pointing at short posts from remaining entries
        text = re.sub(
            rf'\n\s*<xhtml:link rel="alternate" hreflang="ko" href="https://perfectfitme\.com/blog/{slug}"/>',
            "",
            text,
        )
    sm.write_text(text, encoding="utf-8")
    print("sitemap cleaned for short KO")


def strip_ko_hreflang_on_en() -> None:
    for slug in SHORT_KO:
        f = ROOT / "blog" / f"{slug}-en.html"
        if not f.exists():
            continue
        raw = f.read_bytes()
        new = re.sub(
            rf'\r?\n<link rel="alternate" hreflang="ko" href="https://perfectfitme\.com/blog/{slug}">'.encode(),
            b"",
            raw,
        )
        if new != raw:
            f.write_bytes(new)
            print(f"strip ko hreflang {f.name}")


def main() -> None:
    print("bumped html refs", bump_ads_refs())
    noindex_short_ko()
    clean_sitemap()
    strip_ko_hreflang_on_en()


if __name__ == "__main__":
    main()
