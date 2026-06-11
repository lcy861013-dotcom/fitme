#!/usr/bin/env python3
"""Point internal links and trust-page canonicals at extensionless URLs (Cloudflare 308)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = [
    ("https://perfectfitme.com/privacy.html", "https://perfectfitme.com/privacy"),
    ("https://perfectfitme.com/terms.html", "https://perfectfitme.com/terms"),
    ("https://perfectfitme.com/contact.html", "https://perfectfitme.com/contact"),
    ("https://perfectfitme.com/about.html", "https://perfectfitme.com/about"),
    (
        "https://perfectfitme.com/editorial-standards.html",
        "https://perfectfitme.com/editorial-standards",
    ),
    ("https://perfectfitme.com/how-it-works.html", "https://perfectfitme.com/how-it-works"),
    ('href="/privacy.html"', 'href="/privacy"'),
    ('href="/terms.html"', 'href="/terms"'),
    ('href="/contact.html"', 'href="/contact"'),
    ('href="/about.html"', 'href="/about"'),
    ('href="/editorial-standards.html"', 'href="/editorial-standards"'),
    ('href="/how-it-works.html"', 'href="/how-it-works"'),
    ("https://perfectfitme.com/demo-video.html", "https://perfectfitme.com/demo-video"),
    ('href="/demo-video.html"', 'href="/demo-video"'),
    ('href="/ko/privacy.html"', 'href="/ko/privacy"'),
    ('href="/ko/terms.html"', 'href="/ko/terms"'),
    ('href="/ko/how-it-works.html"', 'href="/ko/how-it-works"'),
    ('href="/ko/editorial-standards.html"', 'href="/ko/editorial-standards"'),
    ('href="/ko/about.html"', 'href="/ko/about"'),
    ('href="/ko/contact.html"', 'href="/ko/contact"'),
    ('href="/ja/about.html"', 'href="/ja/about"'),
    ('href="/ja/contact.html"', 'href="/ja/contact"'),
    ('href="/pt/about.html"', 'href="/pt/about"'),
    ('href="/pt/contact.html"', 'href="/pt/contact"'),
]

SKIP_DIRS = {".git", "__pycache__", "node_modules", ".cursor"}
GLOBS = ("**/*.html", "**/*.js", "**/*.txt", "**/*.xml")


def should_touch(path: Path) -> bool:
    parts = set(path.parts)
    return not parts & SKIP_DIRS


def main() -> None:
    changed: list[str] = []
    for pattern in GLOBS:
        for path in ROOT.glob(pattern):
            if not should_touch(path):
                continue
            text = path.read_text(encoding="utf-8")
            original = text
            for old, new in REPLACEMENTS:
                text = text.replace(old, new)
            if text != original:
                path.write_text(text, encoding="utf-8")
                changed.append(str(path.relative_to(ROOT)))
    print(f"Updated {len(changed)} files")
    for rel in sorted(changed)[:30]:
        print(f"  {rel}")
    if len(changed) > 30:
        print(f"  ... and {len(changed) - 30} more")


if __name__ == "__main__":
    main()
