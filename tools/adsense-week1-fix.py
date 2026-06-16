#!/usr/bin/env python3
"""Week 1 AdSense fixes: JA/PT noindex, author schema, sitemap cleanup."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
blog = ROOT / "blog"

PERSON_MULTILINE = """  "author": {
    "@type": "Person",
    "name": "Changyong Lee",
    "url": "https://perfectfitme.com/about"
  }"""

PERSON_INLINE = '{"@type": "Person", "name": "Changyong Lee", "url": "https://perfectfitme.com/about"}'

AUTHOR_PATTERNS = [
    (
        re.compile(
            r'"author":\s*\{\s*"@type":\s*"Organization",\s*"name":\s*"FITME",\s*"url":\s*"https://perfectfitme\.com"\s*\}',
            re.DOTALL,
        ),
        PERSON_MULTILINE,
    ),
    (
        re.compile(
            r'"author":\s*\{\s*"@type":\s*"Organization",\s*"name":\s*"FITME",\s*"url":\s*"https://perfectfitme\.com"\s*\}'
        ),
        PERSON_INLINE,
    ),
    (
        re.compile(
            r'"author":\s*\{\s*"@type":\s*"Organization",\s*"name":\s*"FITME",\s*"url":\s*"https://perfectfitme\.com"\s*\}'
        ),
        PERSON_INLINE,
    ),
    (
        re.compile(
            r'"author":\{"@type":"Organization","name":"FITME","url":"https://perfectfitme.com"\}'
        ),
        PERSON_INLINE,
    ),
]

NOINDEX_META = '<meta name="robots" content="noindex, follow">'
NOINDEX_RE = re.compile(r'<meta name="robots" content="[^"]*">', re.I)


def fix_author(text: str) -> str:
    for pat, repl in AUTHOR_PATTERNS:
        text = pat.sub(repl, text)
    return text


def add_noindex(text: str) -> str:
    if NOINDEX_RE.search(text):
        return NOINDEX_RE.sub(NOINDEX_META, text, count=1)
    if "<meta charset" in text:
        return text.replace(
            '<meta charset="UTF-8">', '<meta charset="UTF-8">\n' + NOINDEX_META, 1
        )
    return NOINDEX_META + "\n" + text


def main() -> None:
    for sub in ("ja", "pt"):
        d = blog / sub
        if not d.exists():
            continue
        for f in d.glob("*.html"):
            text = add_noindex(f.read_text(encoding="utf-8"))
            text = fix_author(text)
            f.write_text(text, encoding="utf-8", newline="\n")
            print("noindex", f.relative_to(ROOT))

    for f in blog.glob("blog*.html"):
        text = f.read_text(encoding="utf-8")
        fixed = fix_author(text)
        if fixed != text:
            f.write_text(fixed, encoding="utf-8", newline="\n")
            print("author", f.name)

    sm = ROOT / "sitemap.xml"
    xml = sm.read_text(encoding="utf-8")

    xml = re.sub(
        r"\s*<url>\s*<loc>https://perfectfitme\.com/blog/(?:ja|pt)/[^<]*</loc>.*?</url>",
        "",
        xml,
        flags=re.DOTALL,
    )
    xml = re.sub(
        r'\s*<xhtml:link rel="alternate" hreflang="(?:ja|pt-BR)" href="https://perfectfitme\.com/blog/(?:ja|pt)/[^"]*"/>',
        "",
        xml,
    )
    xml = re.sub(
        r'\s*<xhtml:link rel="alternate" hreflang="ja" href="https://perfectfitme\.com/blog/ja/"/>',
        "",
        xml,
    )
    xml = re.sub(
        r'\s*<xhtml:link rel="alternate" hreflang="pt-BR" href="https://perfectfitme\.com/blog/pt/"/>',
        "",
        xml,
    )

    ko_about = """  <url>
    <loc>https://perfectfitme.com/ko/about</loc>
    <lastmod>2026-06-16</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
    <xhtml:link rel="alternate" hreflang="ko" href="https://perfectfitme.com/ko/about"/>
    <xhtml:link rel="alternate" hreflang="en" href="https://perfectfitme.com/about"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://perfectfitme.com/about"/>
  </url>
"""
    if "https://perfectfitme.com/ko/about" not in xml:
        xml = xml.replace(
            "  <url>\n    <loc>https://perfectfitme.com/about</loc>",
            ko_about + "  <url>\n    <loc>https://perfectfitme.com/about</loc>",
            1,
        )
    else:
        xml = re.sub(
            r"(<loc>https://perfectfitme\.com/ko/about</loc>\s*<lastmod>)[^<]+(</lastmod>)",
            r"\g<1>2026-06-16\g<2>",
            xml,
        )

    xml = re.sub(
        r"(<loc>https://perfectfitme\.com/about</loc>\s*<lastmod>)[^<]+(</lastmod>)",
        r"\g<1>2026-06-16\g<2>",
        xml,
        count=1,
    )

    sm.write_text(xml, encoding="utf-8", newline="\n")
    print("sitemap done")


if __name__ == "__main__":
    main()
