#!/usr/bin/env python3
"""Remove unverifiable credentials; replace with factual E-E-A-T copy."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"

AUTHOR_META_CSS = """
.author-meta{margin:40px 0 16px;padding:18px 20px;background:var(--card,#1c1a18);border:1px solid var(--border,#2a2724);border-radius:12px;font-size:14px;line-height:1.85;color:#ccc;}
.author-meta p{margin:0 0 8px;}
.author-meta p:last-child{margin-bottom:0;}
.personal-note{margin:24px 0;padding:16px 18px;border-left:3px solid var(--accent,#d4a84b);background:rgba(212,168,75,0.08);font-size:14px;line-height:1.8;color:#ccc;}
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

PERSONAL_NOTES = {
    "en": (
        '  <div class="personal-note">\n'
        "<strong>From My Research:</strong> Standard size charts failed me because they "
        "ignore torso-to-leg ratio. I studied fit systems and anthropometric data to build "
        "this framework. This guide reflects that research, not medical advice.\n"
        "  </div>\n"
    ),
    "ko": (
        '  <div class="personal-note">\n'
        "<strong>연구 메모:</strong> 표준 사이즈표는 상체·다리 비율을 반영하지 못해 저에게 맞지 "
        "않았습니다. 핏 시스템과 인체 비율 자료를 바탕으로 이 가이드를 정리했으며, "
        "의학적 조언이 아닙니다.\n"
        "  </div>\n"
    ),
    "ja": (
        '  <div class="personal-note">\n'
        "<strong>研究メモ:</strong> 標準サイズ表は胴と脚の比率を無視するため、"
        "私の体型には合いませんでした。フィット理論と人体データを調べてこの枠組みを"
        "まとめました。医学的助言ではありません。\n"
        "  </div>\n"
    ),
    "pt": (
        '  <div class="personal-note">\n'
        "<strong>Da minha pesquisa:</strong> Tabelas de tamanho padrão ignoram "
        "a proporção tronco-perna. Estudei sistemas de caimento e dados "
        "antropométricos para montar este guia — não é conselho médico.\n"
        "  </div>\n"
    ),
}

AUTHOR_BOX_RE = re.compile(
    r'[ \t]*<div class="author-box">.*?</div>\s*',
    re.DOTALL,
)


def lang_for(path: Path) -> str:
    if "ja" in path.parts:
        return "ja"
    if "pt" in path.parts:
        return "pt"
    if path.name.endswith("-en.html"):
        return "en"
    return "ko"


def patch_css(text: str) -> str:
    if ".author-meta{" in text and ".personal-note{" in text:
        return text
    text = re.sub(r"\.author-box\{[^}]+\}\s*", "", text)
    text = re.sub(r"\.author-box p\{[^}]+\}\s*", "", text)
    text = re.sub(r"\.author-box p:last-child\{[^}]+\}\s*", "", text)
    if "</style>" in text:
        text = text.replace("</style>", AUTHOR_META_CSS + "</style>", 1)
    return text


def patch_blog_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if 'class="author-box"' not in text:
        return False
    lang = lang_for(path)
    new_text, n = AUTHOR_BOX_RE.subn(BLOCKS[lang], text, count=1)
    if n == 0:
        return False
    new_text = patch_css(new_text)
    if 'class="personal-note"' not in new_text:
        m = re.search(r"(<h2>[^<]+</h2>\s*<p>.*?</p>)", new_text, re.DOTALL)
        if m:
            new_text = new_text.replace(
                m.group(1), m.group(1) + "\n" + PERSONAL_NOTES[lang], 1
            )
    path.write_text(new_text, encoding="utf-8")
    return True


def patch_about() -> None:
    p = ROOT / "about.html"
    t = p.read_text(encoding="utf-8")
    t = t.replace('"jobTitle": "Fashion merchandiser",', '"jobTitle": "Founder",')
    t = t.replace('"foundingDate": "2025",', '"foundingDate": "2026-03",')
    old = (
        "  <p>FITME is independently built and maintained by <strong>Changyong Lee</strong>, "
        "a fashion merchandiser with 7+ years of experience in apparel fit analysis and "
        "proportion consulting. Based in South Korea. The project goal is to reduce "
        "“size-only” shopping mistakes by making proportion literacy accessible in Korean, "
        "English, Japanese, and Portuguese.</p>"
    )
    new = (
        "  <p>FITME is independently built and maintained by <strong>Changyong Lee</strong>, "
        "a solo founder based in South Korea.</p>\n"
        "  <p>I created FITME after struggling to find clothes that fit my proportions. "
        "This project translates research from systems like Kibbe Body Types and ISO 8559 "
        "garment standards into practical tools. Started March 2026.</p>\n"
        "  <p>The project goal is to reduce “size-only” shopping mistakes by making "
        "proportion literacy accessible in Korean, English, Japanese, and Portuguese.</p>"
    )
    if old in t:
        t = t.replace(old, new)
    p.write_text(t, encoding="utf-8")


def main() -> None:
    patch_about()
    n = 0
    for path in BLOG.rglob("*.html"):
        if path.name == "index.html":
            continue
        if patch_blog_file(path):
            n += 1
    print(f"Patched {n} blog files + about.html")


if __name__ == "__main__":
    main()
