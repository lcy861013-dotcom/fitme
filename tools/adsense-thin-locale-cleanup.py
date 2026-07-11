#!/usr/bin/env python3
"""AdSense prep: noindex thin JA/PT, strip their ads, clean sitemap."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def add_noindex(folder: Path) -> int:
    n = 0
    for f in folder.rglob("*.html"):
        text = f.read_text(encoding="utf-8")
        if 'name="robots"' in text or "name='robots'" in text:
            continue
        if '<meta charset="UTF-8">' in text:
            text = text.replace(
                '<meta charset="UTF-8">',
                '<meta charset="UTF-8">\n  <meta name="robots" content="noindex, follow">',
                1,
            )
        else:
            text = text.replace(
                "<head>",
                '<head>\n  <meta name="robots" content="noindex, follow">',
                1,
            )
        f.write_text(text, encoding="utf-8")
        n += 1
        print(f"noindex {f.relative_to(ROOT)}")
    return n


AD_PATTERNS = [
    re.compile(r'\n?<meta name="google-adsense-account" content="ca-pub-[^"]+">\n?'),
    re.compile(
        r'\n?\s*<div class="fitme-ad-slot"[^>]*>.*?</div>\n?',
        re.DOTALL,
    ),
    re.compile(r'\n?<link rel="stylesheet" href="/assets/fitme-ads\.css[^>]*>\n?'),
    re.compile(r'\n?<script defer src="/assets/fitme-ads\.js[^>]*></script>\n?'),
]


def strip_ads(folder: Path) -> int:
    n = 0
    for f in folder.rglob("*.html"):
        text = f.read_text(encoding="utf-8")
        orig = text
        for pat in AD_PATTERNS:
            text = pat.sub("\n", text)
        if text != orig:
            f.write_text(text, encoding="utf-8")
            n += 1
            print(f"strip ads {f.relative_to(ROOT)}")
    return n


def clean_sitemap() -> None:
    sm = ROOT / "sitemap.xml"
    s = sm.read_text(encoding="utf-8")
    s2 = re.sub(
        r"\n\s*<url>\s*\n\s*<loc>https://perfectfitme\.com/(?:ja|pt)/(?:about|contact)</loc>.*?</url>\s*",
        "\n",
        s,
        flags=re.DOTALL,
    )
    s2 = re.sub(
        r"\n\s*<!-- Added: JA/PT blog loc \+ locale trust \(2026-05-29\) -->\s*\n",
        "\n",
        s2,
    )
    sm.write_text(s2, encoding="utf-8")
    left = re.findall(
        r"perfectfitme\.com/(?:ja|pt)/(?:about|contact)",
        sm.read_text(encoding="utf-8"),
    )
    print(f"sitemap_ja_pt_left={left}")


def main() -> None:
    noindex_n = 0
    for name in ("ja", "pt"):
        noindex_n += add_noindex(ROOT / name)
    print(f"noindex_added={noindex_n}")

    strip_n = 0
    for folder in (
        ROOT / "blog" / "ja",
        ROOT / "blog" / "pt",
        ROOT / "ja",
        ROOT / "pt",
    ):
        strip_n += strip_ads(folder)
    print(f"stripped_files={strip_n}")

    clean_sitemap()


if __name__ == "__main__":
    main()
