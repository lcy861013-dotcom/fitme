#!/usr/bin/env python3
"""Align trust page canonical/hreflang/nav URLs with Cloudflare extensionless paths."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://perfectfitme.com"
LANGS = ("ko", "en", "ja", "pt", "es", "zh", "fr", "de", "it", "ru", "ar", "hi", "th", "id", "vi")


def fix_text(text: str) -> str:
    text = text.replace(f"{SITE}/about.html", f"{SITE}/about")
    text = text.replace(f"{SITE}/contact.html", f"{SITE}/contact")
    for loc in LANGS:
        text = text.replace(f"{SITE}/{loc}/about.html", f"{SITE}/{loc}/about")
        text = text.replace(f"{SITE}/{loc}/contact.html", f"{SITE}/{loc}/contact")
    text = text.replace('href="/about.html"', 'href="/about"')
    text = text.replace('href="/contact.html"', 'href="/contact"')
    for loc in LANGS:
        text = text.replace(f'href="/{loc}/about.html"', f'href="/{loc}/about"')
        text = text.replace(f'href="/{loc}/contact.html"', f'href="/{loc}/contact"')
    return text


def main() -> None:
    paths: list[Path] = [ROOT / "about.html", ROOT / "contact.html"]
    for loc in LANGS:
        paths.extend(
            [
                ROOT / loc / "about.html",
                ROOT / loc / "contact.html",
                ROOT / loc / "index.html",
            ]
        )
    for path in paths:
        if not path.is_file():
            continue
        original = path.read_text(encoding="utf-8")
        updated = fix_text(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print("fixed", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
