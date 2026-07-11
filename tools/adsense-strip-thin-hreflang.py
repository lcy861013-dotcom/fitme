#!/usr/bin/env python3
"""Remove hreflang to thin JA/PT URLs from KO/EN surfaces + sitemap."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HREFLANG = re.compile(
    r'\n?<link rel="alternate" hreflang="(?:ja|pt|pt-BR)" '
    r'href="https://perfectfitme\.com/(?:ja|pt|blog/ja|blog/pt)[^"]*">\n?'
)
XHTML = re.compile(
    r'\n?\s*<xhtml:link rel="alternate" hreflang="(?:ja|pt|pt-BR)" '
    r'href="https://perfectfitme\.com/(?:ja|pt|blog/ja|blog/pt)[^"]*"/>\n?'
)


def main() -> None:
    files: list[Path] = []
    files.extend(ROOT.glob("*.html"))
    files.extend((ROOT / "blog").glob("*.html"))
    files.extend((ROOT / "ko").rglob("*.html"))
    files.extend((ROOT / "en").rglob("*.html"))

    changed = 0
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = f.read_text(encoding="utf-8", errors="replace")
            print(f"warn encoding {f.relative_to(ROOT)}")
        new = HREFLANG.sub("\n", text)
        if new != text:
            f.write_text(new, encoding="utf-8")
            changed += 1
            print(f"hreflang {f.relative_to(ROOT)}")

    sm = ROOT / "sitemap.xml"
    s = sm.read_text(encoding="utf-8")
    s2 = XHTML.sub("\n", s)
    if s2 != s:
        sm.write_text(s2, encoding="utf-8")
        print("sitemap xhtml cleaned")

    left = re.findall(r"perfectfitme\.com/(?:ja|pt)/", sm.read_text(encoding="utf-8"))
    print(f"hreflang_files={changed}")
    print(f"sitemap_left={left}")


if __name__ == "__main__":
    main()
