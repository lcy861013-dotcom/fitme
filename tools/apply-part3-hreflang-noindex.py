#!/usr/bin/env python3
"""Part 3: normalize hreflang clusters, index blog listing pages, verify source URLs."""
from __future__ import annotations

import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"
SITE = "https://perfectfitme.com"

# blog number -> ja/pt slug (None if no edition)
CLUSTER: dict[int, dict[str, str | None]] = {
    1: {"ja": "pants-fit-guide", "pt": "guia-modelagem-calcas"},
    3: {"ja": "golden-ratio-fuku", "pt": None},
    6: {"ja": "capsule-5-basics", "pt": "guarda-roupa-capsula-5-pecas"},
    7: {"ja": "proportion-not-weight", "pt": "proporcao-importa-mais-que-peso"},
    8: {"ja": "whr-clothing-fit", "pt": "whr-e-caimento"},
    9: {"ja": "shoulder-fit-guide", "pt": "ombro-e-caimento"},
    10: {"ja": None, "pt": "como-parecer-mais-alta"},
    12: {"ja": "find-body-type-data", "pt": None},
    13: {"ja": "taikei-fuku-erabikata", "pt": "como-se-vestir-tipo-de-corpo"},
    18: {"ja": "pear-styling", "pt": "corpo-pera-como-vestir"},
    25: {"ja": None, "pt": "whr-065-significado"},
}

SOURCE_LINKS = (
    "https://en.wikipedia.org/wiki/Dressing_by_body_type_in_women",
    "https://www.iso.org/standard/69080.html",
)

HREFLANG_RE = re.compile(
    r'\n?\s*<link rel="alternate" hreflang="[^"]+"[^>]*>\s*',
    re.IGNORECASE,
)
ROBOTS_INDEX = '<meta name="robots" content="index, follow">'
ROBOTS_NOINDEX = '<meta name="robots" content="noindex, follow">'

# Reverse lookup for ja/pt article paths
JA_TO_N = {v["ja"]: k for k, v in CLUSTER.items() if v.get("ja")}
PT_TO_N = {v["pt"]: k for k, v in CLUSTER.items() if v.get("pt")}


def cluster_urls(n: int) -> dict[str, str]:
    urls = {
        "ko": f"{SITE}/blog/blog{n}",
        "en": f"{SITE}/blog/blog{n}-en",
    }
    extra = CLUSTER.get(n, {})
    if extra.get("ja"):
        urls["ja"] = f"{SITE}/blog/ja/{extra['ja']}"
    if extra.get("pt"):
        urls["pt"] = f"{SITE}/blog/pt/{extra['pt']}"
    return urls


def hreflang_block(urls: dict[str, str]) -> str:
    lines: list[str] = []
    for lang in ("ko", "en", "ja", "pt"):
        if lang in urls:
            lines.append(
                f'<link rel="alternate" hreflang="{lang}" href="{urls[lang]}">'
            )
    default = urls.get("en", next(iter(urls.values())))
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{default}">')
    return "\n".join(lines) + "\n"


def replace_hreflang(html: str, block: str) -> str:
    stripped = HREFLANG_RE.sub("\n", html)
    m = re.search(r"(<link rel=\"canonical\"[^>]*>\s*)", stripped, re.I)
    if m:
        return stripped[: m.end()] + block + stripped[m.end() :]
    m = re.search(r"(<meta charset[^>]*>\s*)", stripped, re.I)
    if m:
        return stripped[: m.end()] + block + stripped[m.end() :]
    return stripped


def ensure_robots_meta(html: str, content: str) -> str:
    if re.search(r'<meta name="robots"[^>]*>', html, re.I):
        return re.sub(
            r'<meta name="robots"[^>]*>',
            f'<meta name="robots" content="{content}">',
            html,
            count=1,
            flags=re.I,
        )
    m = re.search(r"(<meta name=\"viewport\"[^>]*>\s*)", html, re.I)
    if m:
        return html[: m.end()] + f'<meta name="robots" content="{content}">\n' + html[m.end() :]
    m = re.search(r"(<meta charset[^>]*>\s*)", html, re.I)
    if m:
        return html[: m.end()] + f'<meta name="robots" content="{content}">\n' + html[m.end() :]
    return html


def ensure_index(html: str) -> str:
    return ensure_robots_meta(html, "index, follow")


def ensure_source_links(html: str) -> str:
    ok = all(u in html for u in SOURCE_LINKS)
    if ok:
        return html
    snippet = (
        '  <p style="font-size:13px;color:#8b8178;margin:12px 0 0;">Sources: '
        '<a href="https://en.wikipedia.org/wiki/Dressing_by_body_type_in_women" target="_blank" '
        'rel="noopener" style="color:#d4a84b;">Kibbe Body Types</a> · '
        '<a href="https://www.iso.org/standard/69080.html" target="_blank" '
        'rel="noopener" style="color:#d4a84b;">ISO 8559</a></p>\n'
    )
    if 'class="ymyl-disclaimer"' in html:
        return html.replace(
            '  <p class="ymyl-disclaimer"',
            snippet + '  <p class="ymyl-disclaimer"',
            1,
        )
    if '  <motion class="related">' in html:
        return html.replace('  <div class="related">', snippet + '  <div class="related">', 1)
    return html


def patch_blog_number(n: int) -> int:
    urls = cluster_urls(n)
    block = hreflang_block(urls)
    count = 0
    for name in (f"blog{n}.html", f"blog{n}-en.html"):
        path = BLOG / name
        if not path.exists():
            continue
        text = replace_hreflang(path.read_text(encoding="utf-8"), block)
        text = ensure_source_links(text)
        path.write_text(text, encoding="utf-8")
        count += 1
    extra = CLUSTER.get(n, {})
    if extra.get("ja"):
        p = BLOG / "ja" / f"{extra['ja']}.html"
        if p.exists():
            text = replace_hreflang(p.read_text(encoding="utf-8"), block)
            text = ensure_source_links(text)
            p.write_text(text, encoding="utf-8")
            count += 1
    if extra.get("pt"):
        p = BLOG / "pt" / f"{extra['pt']}.html"
        if p.exists():
            text = replace_hreflang(p.read_text(encoding="utf-8"), block)
            text = ensure_source_links(text)
            p.write_text(text, encoding="utf-8")
            count += 1
    return count


def patch_listing_index(path: Path, hreflang_block_html: str) -> None:
    text = path.read_text(encoding="utf-8")
    text = replace_hreflang(text, hreflang_block_html)
    text = ensure_index(text)
    path.write_text(text, encoding="utf-8")


def patch_trust_pages() -> None:
    hub = hreflang_block(
        {
            "en": f"{SITE}/about.html",
            "ko": f"{SITE}/about.html",
            "ja": f"{SITE}/blog/ja/",
            "pt": f"{SITE}/blog/pt/",
        }
    )
    for name in ("about.html", "contact.html"):
        p = ROOT / name
        if p.exists():
            text = replace_hreflang(p.read_text(encoding="utf-8"), hub)
            p.write_text(text, encoding="utf-8")


def verify_urls() -> list[str]:
    bad: list[str] = []
    for url in SOURCE_LINKS:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (FITME-check/1.0)"})
            with urllib.request.urlopen(req, timeout=20) as resp:
                if resp.status >= 400:
                    bad.append(f"{url} -> HTTP {resp.status}")
        except Exception as e:
            bad.append(f"{url} -> {e}")
    return bad


def main() -> None:
    total = 0
    for n in range(1, 26):
        total += patch_blog_number(n)
    listing_hreflang = hreflang_block(
        {
            "ko": f"{SITE}/blog/",
            "en": f"{SITE}/blog/",
            "ja": f"{SITE}/blog/ja/",
            "pt": f"{SITE}/blog/pt/",
        }
    )
    for rel in ("index.html", "ja/index.html", "pt/index.html"):
        p = BLOG / rel
        if p.exists():
            patch_listing_index(p, listing_hreflang)
            total += 1
    patch_trust_pages()
    missing = []
    for path in BLOG.rglob("*.html"):
        if path.name == "index.html":
            continue
        raw = path.read_text(encoding="utf-8")
        if not all(u in raw for u in SOURCE_LINKS):
            missing.append(str(path.relative_to(ROOT)))
    bad = verify_urls()
    print(f"Patched hreflang/index on {total}+ listing/trust pages")
    if missing:
        print(f"Missing source links ({len(missing)}):", ", ".join(missing[:10]), "...")
    else:
        print("All blog articles include Kibbe + ISO 8559 links.")
    if bad:
        print("URL check failures:", bad)
    else:
        print("External URLs OK:", ", ".join(SOURCE_LINKS))


if __name__ == "__main__":
    main()
