#!/usr/bin/env python3
"""
1. Append JP & PT blog URLs to sitemap.xml (with proper hreflang chains).
2. Append JP & PT blog INDEX URLs (/blog/ja/ and /blog/pt/).
3. Add <xhtml:link rel="alternate" hreflang="ja" / "pt-BR"> to the EXISTING
   ko/en blog post entries in sitemap that have a JP/PT counterpart (blog1, 3, 13, 18, 25).

Mapping between EN blogN and the JP/PT slugs:
  blog1  -> ja/pants-fit-guide,            pt/guia-modelagem-calcas
  blog3  -> ja/golden-ratio-fuku,          pt/(no match)
  blog10 -> pt/como-parecer-mais-alta      (ja/no match)
  blog12 -> ja/find-body-type-data         (pt/no match)
  blog13 -> ja/taikei-fuku-erabikata,      pt/como-se-vestir-tipo-de-corpo
  blog18 -> ja/pear-styling,               pt/corpo-pera-como-vestir
  blog25 -> pt/whr-065-significado         (ja/no match)
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://perfectfitme.com"
SITEMAP = ROOT / "sitemap.xml"

# Mapping: en_blog_num -> { 'ja': slug_or_none, 'pt': slug_or_none }
MAP = {
    1:  {"ja": "pants-fit-guide",       "pt": "guia-modelagem-calcas"},
    3:  {"ja": "golden-ratio-fuku",     "pt": None},
    10: {"ja": None,                    "pt": "como-parecer-mais-alta"},
    12: {"ja": "find-body-type-data",   "pt": None},
    13: {"ja": "taikei-fuku-erabikata", "pt": "como-se-vestir-tipo-de-corpo"},
    18: {"ja": "pear-styling",          "pt": "corpo-pera-como-vestir"},
    25: {"ja": None,                    "pt": "whr-065-significado"},
}

JP_SLUGS = ["taikei-fuku-erabikata", "find-body-type-data", "pear-styling",
            "pants-fit-guide", "golden-ratio-fuku"]
PT_SLUGS = ["como-se-vestir-tipo-de-corpo", "corpo-pera-como-vestir",
            "whr-065-significado", "guia-modelagem-calcas", "como-parecer-mais-alta"]


def build_url(url: str, alts: dict[str, str], lastmod: str = "2026-05-16",
              changefreq: str = "monthly", priority: str = "0.7") -> str:
    alt_lines = "\n".join(
        f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{href}"/>'
        for lang, href in alts.items()
    )
    return (
        "  <url>\n"
        f"    <loc>{url}</loc>\n"
        f"    <lastmod>{lastmod}</lastmod>\n"
        f"    <changefreq>{changefreq}</changefreq>\n"
        f"    <priority>{priority}</priority>\n"
        f"{alt_lines}\n"
        "  </url>"
    )


def main():
    raw = SITEMAP.read_text(encoding="utf-8")

    # ---- 1. Inject hreflang ja/pt into EXISTING ko & en blog entries for mapped posts.
    for n, langs in MAP.items():
        for variant in (f"blog{n}", f"blog{n}-en"):
            # find the <url>...</url> block whose <loc> ends with /blog/{variant}
            pattern = re.compile(
                r'(<url>\s*<loc>https://perfectfitme\.com/blog/'
                + re.escape(variant)
                + r'</loc>.*?</url>)',
                re.DOTALL,
            )
            m = pattern.search(raw)
            if not m:
                continue
            block = m.group(1)
            new_block = block
            if langs["ja"] and "hreflang=\"ja\"" not in new_block:
                ja_url = f"{SITE}/blog/ja/{langs['ja']}"
                ins = f'\n    <xhtml:link rel="alternate" hreflang="ja" href="{ja_url}"/>'
                # insert before </url>
                new_block = new_block.replace("</url>", ins + "\n  </url>")
            if langs["pt"] and "hreflang=\"pt-BR\"" not in new_block:
                pt_url = f"{SITE}/blog/pt/{langs['pt']}"
                ins = f'\n    <xhtml:link rel="alternate" hreflang="pt-BR" href="{pt_url}"/>'
                new_block = new_block.replace("</url>", ins + "\n  </url>")
            if new_block != block:
                raw = raw.replace(block, new_block, 1)

    # ---- 2. Append JP/PT blog index URLs (if not already present)
    for index_url in [f"{SITE}/blog/ja/", f"{SITE}/blog/pt/"]:
        if index_url in raw:
            continue
        alts_idx = {
            "ko": f"{SITE}/blog/",
            "en": f"{SITE}/blog/",
            "ja": f"{SITE}/blog/ja/",
            "pt-BR": f"{SITE}/blog/pt/",
            "x-default": f"{SITE}/blog/",
        }
        block = build_url(index_url, alts_idx, lastmod="2026-05-16",
                          changefreq="weekly", priority="0.85")
        raw = raw.replace("</urlset>", block + "\n</urlset>")

    # ---- 3. Append JP blog post URLs
    for slug in JP_SLUGS:
        url = f"{SITE}/blog/ja/{slug}"
        if url in raw:
            continue
        # build hreflang chain
        en_num = None
        for n, langs in MAP.items():
            if langs["ja"] == slug:
                en_num = n
                break
        alts = {"ja": url}
        if en_num:
            alts["ko"] = f"{SITE}/blog/blog{en_num}"
            alts["en"] = f"{SITE}/blog/blog{en_num}-en"
            if MAP[en_num]["pt"]:
                alts["pt-BR"] = f"{SITE}/blog/pt/{MAP[en_num]['pt']}"
            alts["x-default"] = f"{SITE}/blog/blog{en_num}-en"
        block = build_url(url, alts, lastmod="2026-05-16",
                          changefreq="monthly", priority="0.7")
        raw = raw.replace("</urlset>", block + "\n</urlset>")

    # ---- 4. Append PT blog post URLs
    for slug in PT_SLUGS:
        url = f"{SITE}/blog/pt/{slug}"
        if url in raw:
            continue
        en_num = None
        for n, langs in MAP.items():
            if langs["pt"] == slug:
                en_num = n
                break
        alts = {"pt-BR": url}
        if en_num:
            alts["ko"] = f"{SITE}/blog/blog{en_num}"
            alts["en"] = f"{SITE}/blog/blog{en_num}-en"
            if MAP[en_num]["ja"]:
                alts["ja"] = f"{SITE}/blog/ja/{MAP[en_num]['ja']}"
            alts["x-default"] = f"{SITE}/blog/blog{en_num}-en"
        block = build_url(url, alts, lastmod="2026-05-16",
                          changefreq="monthly", priority="0.7")
        raw = raw.replace("</urlset>", block + "\n</urlset>")

    SITEMAP.write_text(raw, encoding="utf-8")

    n_ja = sum(1 for s in JP_SLUGS if f"{SITE}/blog/ja/{s}" in raw)
    n_pt = sum(1 for s in PT_SLUGS if f"{SITE}/blog/pt/{s}" in raw)
    print(f"sitemap.xml updated.")
    print(f"  Total <url> entries now: {raw.count('<url>')}")
    print(f"  JP posts in sitemap: {n_ja}/5")
    print(f"  PT posts in sitemap: {n_pt}/5")


if __name__ == "__main__":
    main()
