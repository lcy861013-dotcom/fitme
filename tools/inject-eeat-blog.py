#!/usr/bin/env python3
"""Inject factual author meta + YMYL disclaimer into blog HTML (EN/KO/JA/PT)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"

META_CSS = """
.author-meta{margin:40px 0 16px;padding:18px 20px;background:var(--card,#1c1a18);border:1px solid var(--border,#2a2724);border-radius:12px;font-size:14px;line-height:1.85;color:#ccc;}
.author-meta p{margin:0 0 8px;}
.author-meta p:last-child{margin-bottom:0;}
.ymyl-disclaimer{font-size:13px;color:var(--muted,#8b8178);margin:0 0 24px;line-height:1.7;}
"""

BLOCKS = {
    "en": (
        '  <div class="author-meta">\n'
        "    <p>By <strong>Changyong Lee</strong> | FITME Founder</p>\n"
        "    <p>Research-based guide using Kibbe Body Types and ISO 8559. "
        "Last Updated: 2026.05.19</p>\n"
        "  </div>\n"
        '  <p class="ymyl-disclaimer"><strong>Disclaimer:</strong> For education and style '
        "only; not medical or health advice.</p>\n"
    ),
    "ko": (
        '  <div class="author-meta">\n'
        "    <p><strong>이창용</strong> | FITME 대표</p>\n"
        "    <p>Kibbe 체형·ISO 8559 기반 연구 가이드. 최종 수정: 2026.05.19</p>\n"
        "  </div>\n"
        '  <p class="ymyl-disclaimer"><strong>면책조항:</strong> 스타일 교육 목적이며, '
        "의학·건강 조언이 아닙니다.</p>\n"
    ),
    "ja": (
        '  <div class="author-meta">\n'
        "    <p><strong>李昌龍</strong> | FITME代表</p>\n"
        "    <p>Kibbe・ISO 8559に基づく研究ガイド。最終更新: 2026.05.19</p>\n"
        "  </div>\n"
        '  <p class="ymyl-disclaimer"><strong>免責:</strong> スタイル教育目的。'
        "医学的助言ではありません。</p>\n"
    ),
    "pt": (
        '  <div class="author-meta">\n'
        "    <p><strong>Changyong Lee</strong> | Fundador FITME</p>\n"
        "    <p>Guia com base em Kibbe e ISO 8559. Atualizado: 2026.05.19</p>\n"
        "  </div>\n"
        '  <p class="ymyl-disclaimer"><strong>Aviso:</strong> Conteúdo educacional; '
        "não é aconselhamento médico.</p>\n"
    ),
}


def lang_for(path: Path) -> str:
    if "ja" in path.parts:
        return "ja"
    if "pt" in path.parts:
        return "pt"
    if path.name.endswith("-en.html"):
        return "en"
    return "ko"


def inject_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if 'class="author-meta"' in text or 'class="author-box"' in text:
        return False
    block = BLOCKS[lang_for(path)]
    if '  <div class="related">' in text:
        text = text.replace('  <div class="related">', block + '  <div class="related">', 1)
    elif '  <div class="cta">' in text:
        text = text.replace('  <div class="cta">', block + '  <div class="cta">', 1)
    else:
        return False
    if ".author-meta{" not in text and "</style>" in text:
        text = text.replace("</style>", META_CSS + "</style>", 1)
    path.write_text(text, encoding="utf-8")
    return True


def main() -> None:
    n = 0
    for path in BLOG.rglob("*.html"):
        if path.name == "index.html":
            continue
        if inject_file(path):
            n += 1
    print(f"Done. Updated {n} blog files.")


if __name__ == "__main__":
    main()
