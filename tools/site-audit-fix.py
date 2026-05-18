#!/usr/bin/env python3
"""One-off fixes from site audit: OG image path, blog footers, 404, llms.txt, feed date."""
from __future__ import annotations

import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_OG = "/assets/og-image-en.png"
TODAY = date.today().isoformat()

FOOTER_OLD = re.compile(
    r'(<footer><p>© 2026 FITME[^<]*</p></footer>)',
    re.I,
)

FOOTER_NEW = (
    '<footer><p>© 2026 FITME. All rights reserved. · '
    '<a href="/privacy.html" style="color:var(--muted);">Privacy</a> · '
    '<a href="/terms.html" style="color:var(--muted);">Terms</a> · '
    '<a href="/contact.html" style="color:var(--muted);">Contact</a> · '
    '<a href="/about.html" style="color:var(--muted);">About</a></p></footer>'
)

FOOTER_PRIVACY_ONLY = re.compile(
    r'<footer><p>© 2026 FITME\. All rights reserved\. · '
    r'<a href="/privacy\.html" style="color:var\(--muted\);">Privacy Policy</a></p></footer>'
)


def copy_og_image() -> None:
    src = ROOT / "assets" / "og-image-en.png"
    dst = ROOT / "og-image.png"
    if src.exists():
        shutil.copy2(src, dst)
        print(f"Copied {src.name} -> og-image.png")


def replace_og_urls() -> int:
    n = 0
    for path in ROOT.rglob("*"):
        if path.suffix not in {".html", ".js", ".xml"}:
            continue
        if "node_modules" in path.parts or ".git" in path.parts:
            continue
        raw = path.read_text(encoding="utf-8")
        new = raw.replace("https://perfectfitme.com/og-image.png", f"https://perfectfitme.com{SITE_OG}")
        new = new.replace("/og-image.png", SITE_OG)
        if new != raw:
            path.write_text(new, encoding="utf-8")
            n += 1
    return n


def fix_blog_footers() -> int:
    n = 0
    for path in (ROOT / "blog").rglob("blog*.html"):
        raw = path.read_text(encoding="utf-8")
        if "href=\"/terms.html\"" in raw:
            continue
        new = FOOTER_PRIVACY_ONLY.sub(FOOTER_NEW, raw)
        if new == raw and "<footer>" in raw:
            new = FOOTER_OLD.sub(FOOTER_NEW, raw, count=1)
        if new != raw:
            path.write_text(new, encoding="utf-8")
            n += 1
    return n


def fix_404() -> None:
    path = ROOT / "404.html"
    raw = path.read_text(encoding="utf-8")
    new = raw.replace(
        '<meta property="og:url" content="https://perfectfitme.com/404">',
        '<meta property="og:url" content="https://perfectfitme.com/404.html">',
    )
    new = new.replace(
        '<link rel="canonical" href="https://perfectfitme.com/">',
        '<link rel="canonical" href="https://perfectfitme.com/404.html">\n'
        '  <meta name="robots" content="noindex, follow">',
    )
    if new != raw:
        path.write_text(new, encoding="utf-8")
        print("Updated 404.html")


def fix_llms() -> None:
    path = ROOT / "llms.txt"
    raw = path.read_text(encoding="utf-8")
    new = raw.replace(
        "https://perfectfitme.com/blog/index-en.html",
        "https://perfectfitme.com/blog/?lang=en",
    )
    new = new.replace(f"Last updated\n2026-05-18", f"Last updated\n{TODAY}")
    if "index-en.html" in new:
        new = new.replace("- English blog index: https://perfectfitme.com/blog/index-en.html\n", "")
    if new != raw:
        path.write_text(new, encoding="utf-8")
        print("Updated llms.txt")


def fix_feed() -> None:
    path = ROOT / "feed.xml"
    raw = path.read_text(encoding="utf-8")
    new = re.sub(r"<updated>[^<]+</updated>", f"<updated>{TODAY}T12:00:00Z</updated>", raw, count=1)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        print("Updated feed.xml")


def fix_blog_index_footer() -> None:
    path = ROOT / "blog" / "index.html"
    raw = path.read_text(encoding="utf-8")
    if 'href="/terms.html"' in raw:
        return
    new = raw.replace(
        '<a href="/privacy.html" style="color:var(--muted);">Privacy Policy</a>',
        '<a href="/privacy.html" style="color:var(--muted);">Privacy</a> · '
        '<a href="/terms.html" style="color:var(--muted);">Terms</a> · '
        '<a href="/contact.html" style="color:var(--muted);">Contact</a> · '
        '<a href="/about.html" style="color:var(--muted);">About</a>',
    )
    if new != raw:
        path.write_text(new, encoding="utf-8")
        print("Updated blog/index.html footer")


def fix_webmanifest() -> None:
    path = ROOT / "site.webmanifest"
    raw = path.read_text(encoding="utf-8")
    icons = [
        {"src": "/assets/og-image-en.png", "sizes": "512x512", "type": "image/png"},
        {"src": "/favicon-32x32.png", "sizes": "32x32", "type": "image/png"},
    ]
    import json

    data = json.loads(raw)
    data["icons"] = icons
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print("Updated site.webmanifest icons")


def main() -> None:
    copy_og_image()
    og_files = replace_og_urls()
    footers = fix_blog_footers()
    fix_404()
    fix_llms()
    fix_feed()
    fix_blog_index_footer()
    fix_webmanifest()
    print(f"OG paths updated in {og_files} files; blog footers: {footers}")


if __name__ == "__main__":
    main()
