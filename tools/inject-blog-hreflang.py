#!/usr/bin/env python3
"""Add ja / pt-BR hreflang links to KO+EN blog posts that have JP/PT counterparts."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"
SITE = "https://perfectfitme.com"

MAP: dict[int, dict[str, str | None]] = {
    1: {"ja": "pants-fit-guide", "pt": "guia-modelagem-calcas"},
    3: {"ja": "golden-ratio-fuku", "pt": None},
    10: {"ja": None, "pt": "como-parecer-mais-alta"},
    12: {"ja": "find-body-type-data", "pt": None},
    13: {"ja": "taikei-fuku-erabikata", "pt": "como-se-vestir-tipo-de-corpo"},
    18: {"ja": "pear-styling", "pt": "corpo-pera-como-vestir"},
    25: {"ja": None, "pt": "whr-065-significado"},
}


def hreflang_lines(n: int) -> list[str]:
    entry = MAP.get(n)
    if not entry:
        return []
    lines: list[str] = []
    if entry.get("ja"):
        lines.append(
            f'  <link rel="alternate" hreflang="ja" '
            f'href="{SITE}/blog/ja/{entry["ja"]}">'
        )
    if entry.get("pt"):
        lines.append(
            f'  <link rel="alternate" hreflang="pt-BR" '
            f'href="{SITE}/blog/pt/{entry["pt"]}">'
        )
    return lines


def inject(path: Path) -> bool:
    m = re.match(r"blog(\d+)(?:-en)?\.html$", path.name)
    if not m:
        return False
    n = int(m.group(1))
    raw = path.read_text(encoding="utf-8")
    to_add: list[str] = []
    entry = MAP.get(n)
    if not entry:
        return False
    if entry.get("ja") and 'hreflang="ja"' not in raw:
        to_add.append(
            f'  <link rel="alternate" hreflang="ja" '
            f'href="{SITE}/blog/ja/{entry["ja"]}">'
        )
    if entry.get("pt") and 'hreflang="pt-BR"' not in raw:
        to_add.append(
            f'  <link rel="alternate" hreflang="pt-BR" '
            f'href="{SITE}/blog/pt/{entry["pt"]}">'
        )
    if not to_add:
        return False
    anchor = re.search(r'(<link rel="alternate" hreflang="en"[^>]+>\s*)', raw)
    if not anchor:
        anchor = re.search(r'(<link rel="canonical"[^>]+>\s*)', raw)
    if not anchor:
        return False
    block = "\n".join(to_add) + "\n"
    new = raw[: anchor.end()] + block + raw[anchor.end() :]
    path.write_text(new, encoding="utf-8")
    return True


def main() -> None:
    touched = []
    for path in sorted(BLOG.glob("blog*.html")):
        if inject(path):
            touched.append(path.name)
    print(f"Updated {len(touched)} files: {', '.join(touched)}")


if __name__ == "__main__":
    main()
