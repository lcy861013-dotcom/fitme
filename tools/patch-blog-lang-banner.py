#!/usr/bin/env python3
"""Add KO/EN language switch banner to blog posts (blog1–25 pairs)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"
CSS_LINK = '<link rel="stylesheet" href="/assets/blog-lang-banner.css?v=1">\n'
MARKER = "blog-lang-banner"

PAIRS = [(f"blog{i}.html", f"blog{i}-en.html") for i in range(1, 26)]


def banner_ko(en_slug: str) -> str:
    return f"""  <nav class="blog-lang-banner" aria-label="Article language">
    <span class="blog-lang-banner__label">🌐 이 글: <strong>한국어</strong></span>
    <a class="blog-lang-banner__link" href="/blog/{en_slug}" hreflang="en" rel="alternate">Read in English →</a>
  </nav>

"""


def banner_en(ko_slug: str) -> str:
    return f"""  <nav class="blog-lang-banner" aria-label="Article language">
    <span class="blog-lang-banner__label">🌐 This article: <strong>English</strong></span>
    <a class="blog-lang-banner__link" href="/blog/{ko_slug}" hreflang="ko" rel="alternate">한국어로 읽기 →</a>
  </nav>

"""


def add_css_link(text: str) -> str:
    if "blog-lang-banner.css" in text:
        return text
    if 'href="/assets/satellite-pages-theme.css' in text:
        return text.replace(
            '<link rel="stylesheet" href="/assets/satellite-pages-theme.css',
            CSS_LINK + '  <link rel="stylesheet" href="/assets/satellite-pages-theme.css',
            1,
        )
    return text


def insert_after_meta(text: str, banner: str) -> str:
    if MARKER in text:
        return text
    m = re.search(r"  <div class=\"meta\">.*?</div>\n", text, flags=re.DOTALL)
    if not m:
        return text
    pos = m.end()
    return text[:pos] + banner + text[pos:]


def patch_file(path: Path, banner: str) -> bool:
    text = path.read_text(encoding="utf-8")
    new = add_css_link(text)
    new = insert_after_meta(new, banner)
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    n = 0
    for ko, en in PAIRS:
        if patch_file(BLOG / ko, banner_ko(en)):
            print(f"  {ko}")
            n += 1
        if patch_file(BLOG / en, banner_en(ko)):
            print(f"  {en}")
            n += 1
    print(f"done ({n} files)")


if __name__ == "__main__":
    main()
