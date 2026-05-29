#!/usr/bin/env python3
"""Point Korean blog HTML footers at /ko/ trust pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "blog"
REPL = [
    ('href="/contact"', 'href="/ko/contact"'),
    ('href="/about"', 'href="/ko/about"'),
    ('href="/privacy"', 'href="/ko/privacy"'),
    ('href="/terms"', 'href="/ko/terms"'),
    ('href="/editorial-standards"', 'href="/ko/editorial-standards"'),
    ('href="/how-it-works"', 'href="/ko/how-it-works"'),
]


def main() -> None:
    n = 0
    for f in ROOT.rglob("*.html"):
        if "-en" in f.name or f.parent.name in ("ja", "pt"):
            continue
        text = f.read_text(encoding="utf-8")
        orig = text
        for old, new in REPL:
            text = text.replace(old, new)
        if text != orig:
            f.write_text(text, encoding="utf-8")
            n += 1
    print(f"updated {n} files")


if __name__ == "__main__":
    main()
