#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
old = (
    '<footer><p>© 2026 FITME. 모든 권리 보유. · '
    '<a href="/privacy" style="color:var(--muted);">개인정보처리방침</a></p></footer>'
)
new = (
    '<footer><p>© 2026 FITME. 모든 권리 보유. · '
    '<a href="/privacy" style="color:var(--muted);">개인정보처리방침</a> · '
    '<a href="/terms" style="color:var(--muted);">이용약관</a> · '
    '<a href="/contact" style="color:var(--muted);">문의</a> · '
    '<a href="/about" style="color:var(--muted);">소개</a></p></footer>'
)
n = 0
for p in (ROOT / "blog").glob("blog*.html"):
    if p.name.endswith("-en.html"):
        continue
    text = p.read_text(encoding="utf-8")
    if old in text:
        p.write_text(text.replace(old, new), encoding="utf-8")
        n += 1
print(f"Updated {n} Korean blog footers")
