#!/usr/bin/env python3
"""Append missing JA/PT blog loc entries + locale trust pages to sitemap.xml."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITEMAP = ROOT / "sitemap.xml"
SITE = "https://perfectfitme.com"
LASTMOD = "2026-05-29"

JA_MISSING = [
    (
        "capsule-5-basics",
        [
            ("ko", f"{SITE}/blog/blog6"),
            ("en", f"{SITE}/blog/blog6-en"),
            ("ja", f"{SITE}/blog/ja/capsule-5-basics"),
            ("pt-BR", f"{SITE}/blog/pt/guarda-roupa-capsula-5-pecas"),
            ("x-default", f"{SITE}/blog/blog6-en"),
        ],
    ),
    (
        "proportion-not-weight",
        [
            ("ko", f"{SITE}/blog/blog7"),
            ("en", f"{SITE}/blog/blog7-en"),
            ("ja", f"{SITE}/blog/ja/proportion-not-weight"),
            ("pt-BR", f"{SITE}/blog/pt/proporcao-importa-mais-que-peso"),
            ("x-default", f"{SITE}/blog/blog7-en"),
        ],
    ),
    (
        "whr-clothing-fit",
        [
            ("ko", f"{SITE}/blog/blog8"),
            ("en", f"{SITE}/blog/blog8-en"),
            ("ja", f"{SITE}/blog/ja/whr-clothing-fit"),
            ("pt-BR", f"{SITE}/blog/pt/whr-e-caimento"),
            ("x-default", f"{SITE}/blog/blog8-en"),
        ],
    ),
    (
        "shoulder-fit-guide",
        [
            ("ko", f"{SITE}/blog/blog9"),
            ("en", f"{SITE}/blog/blog9-en"),
            ("ja", f"{SITE}/blog/ja/shoulder-fit-guide"),
            ("pt-BR", f"{SITE}/blog/pt/ombro-e-caimento"),
            ("x-default", f"{SITE}/blog/blog9-en"),
        ],
    ),
]

PT_MISSING = [
    (
        "guarda-roupa-capsula-5-pecas",
        [
            ("ko", f"{SITE}/blog/blog6"),
            ("en", f"{SITE}/blog/blog6-en"),
            ("ja", f"{SITE}/blog/ja/capsule-5-basics"),
            ("pt-BR", f"{SITE}/blog/pt/guarda-roupa-capsula-5-pecas"),
            ("x-default", f"{SITE}/blog/blog6-en"),
        ],
    ),
    (
        "proporcao-importa-mais-que-peso",
        [
            ("ko", f"{SITE}/blog/blog7"),
            ("en", f"{SITE}/blog/blog7-en"),
            ("ja", f"{SITE}/blog/ja/proportion-not-weight"),
            ("pt-BR", f"{SITE}/blog/pt/proporcao-importa-mais-que-peso"),
            ("x-default", f"{SITE}/blog/blog7-en"),
        ],
    ),
    (
        "whr-e-caimento",
        [
            ("ko", f"{SITE}/blog/blog8"),
            ("en", f"{SITE}/blog/blog8-en"),
            ("ja", f"{SITE}/blog/ja/whr-clothing-fit"),
            ("pt-BR", f"{SITE}/blog/pt/whr-e-caimento"),
            ("x-default", f"{SITE}/blog/blog8-en"),
        ],
    ),
    (
        "ombro-e-caimento",
        [
            ("ko", f"{SITE}/blog/blog9"),
            ("en", f"{SITE}/blog/blog9-en"),
            ("ja", f"{SITE}/blog/ja/shoulder-fit-guide"),
            ("pt-BR", f"{SITE}/blog/pt/ombro-e-caimento"),
            ("x-default", f"{SITE}/blog/blog9-en"),
        ],
    ),
]

TRUST_PAGES = [
    (
        f"{SITE}/ja/about",
        [
            ("en", f"{SITE}/about"),
            ("ja", f"{SITE}/ja/about"),
            ("pt-BR", f"{SITE}/pt/about"),
            ("x-default", f"{SITE}/about"),
        ],
        "0.55",
    ),
    (
        f"{SITE}/ja/contact",
        [
            ("en", f"{SITE}/contact"),
            ("ja", f"{SITE}/ja/contact"),
            ("pt-BR", f"{SITE}/pt/contact"),
            ("x-default", f"{SITE}/contact"),
        ],
        "0.45",
    ),
    (
        f"{SITE}/pt/about",
        [
            ("en", f"{SITE}/about"),
            ("ja", f"{SITE}/ja/about"),
            ("pt-BR", f"{SITE}/pt/about"),
            ("x-default", f"{SITE}/about"),
        ],
        "0.55",
    ),
    (
        f"{SITE}/pt/contact",
        [
            ("en", f"{SITE}/contact"),
            ("ja", f"{SITE}/ja/contact"),
            ("pt-BR", f"{SITE}/pt/contact"),
            ("x-default", f"{SITE}/contact"),
        ],
        "0.45",
    ),
]


def url_block(loc: str, alts: list[tuple[str, str]], priority: str = "0.8") -> str:
    lines = [
        "  <url>",
        f"    <loc>{loc}</loc>",
        f"    <lastmod>{LASTMOD}</lastmod>",
        "    <changefreq>monthly</changefreq>",
        f"    <priority>{priority}</priority>",
    ]
    for lang, href in alts:
        lines.append(f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{href}"/>')
    lines.append("  </url>")
    return "\n".join(lines)


def has_loc(raw: str, loc: str) -> bool:
    return f"<loc>{loc}</loc>" in raw


def main():
    raw = SITEMAP.read_text(encoding="utf-8")
    insert = []

    for slug, alts in JA_MISSING:
        loc = f"{SITE}/blog/ja/{slug}"
        if not has_loc(raw, loc):
            insert.append(url_block(loc, alts))

    for slug, alts in PT_MISSING:
        loc = f"{SITE}/blog/pt/{slug}"
        if not has_loc(raw, loc):
            insert.append(url_block(loc, alts))

    for loc, alts, pri in TRUST_PAGES:
        if not has_loc(raw, loc):
            insert.append(url_block(loc, alts, pri))

    if not insert:
        print("sitemap: nothing to add")
        return

    marker = "  <url>\n    <loc>https://perfectfitme.com/feed.xml</loc>"
    block = "\n\n  <!-- Added: JA/PT blog loc + locale trust (2026-05-29) -->\n" + "\n".join(insert) + "\n\n"
    if marker not in raw:
        raise SystemExit("feed.xml marker not found")
    raw = raw.replace(marker, block + marker, 1)
    SITEMAP.write_text(raw, encoding="utf-8")
    print(f"sitemap: added {len(insert)} url blocks")


if __name__ == "__main__":
    main()
