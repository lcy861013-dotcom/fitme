#!/usr/bin/env python3
"""Inject top author-meta + bottom ymyl disclaimer (factual E-E-A-T only)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"

AUTHOR_TOP = {
    "en": """  <div class="author-meta" style="border-bottom:1px solid #2a2724;padding:10px 0;margin-bottom:20px;">
  <p style="margin:0;">By <strong>Changyong Lee</strong> | FITME Founder, Ansan, South Korea</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">Research-based guide. Sources: <a href="https://en.wikipedia.org/wiki/Dressing_by_body_type_in_women" target="_blank" rel="noopener" style="color:#d4a84b;">Kibbe</a>, <a href="https://www.iso.org/standard/69080.html" target="_blank" rel="noopener" style="color:#d4a84b;">ISO 8559</a> | Last Updated: 2026.05.19</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">Contact: <a href="mailto:lcy861013@gmail.com" style="color:#d4a84b;">lcy861013@gmail.com</a></p>
</div>
""",
    "ko": """  <div class="author-meta" style="border-bottom:1px solid #2a2724;padding:10px 0;margin-bottom:20px;">
  <p style="margin:0;">글쓴이: <strong>이창용</strong> | FITME 대표, 안산</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">연구 기반 가이드. 출처: <a href="https://en.wikipedia.org/wiki/Dressing_by_body_type_in_women" target="_blank" rel="noopener" style="color:#d4a84b;">키비 바디타입</a>, <a href="https://www.iso.org/standard/69080.html" target="_blank" rel="noopener" style="color:#d4a84b;">ISO 8559</a> | 최종 업데이트: 2026.05.19</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">문의: <a href="mailto:lcy861013@gmail.com" style="color:#d4a84b;">lcy861013@gmail.com</a></p>
</div>
""",
    "ja": """  <div class="author-meta" style="border-bottom:1px solid #2a2724;padding:10px 0;margin-bottom:20px;">
  <p style="margin:0;">著者: <strong>李昌龍</strong> | FITME代表、安山</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">研究ガイド。出典: <a href="https://en.wikipedia.org/wiki/Dressing_by_body_type_in_women" target="_blank" rel="noopener" style="color:#d4a84b;">Kibbe</a>, <a href="https://www.iso.org/standard/69080.html" target="_blank" rel="noopener" style="color:#d4a84b;">ISO 8559</a> | 更新: 2026.05.19</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">連絡: <a href="mailto:lcy861013@gmail.com" style="color:#d4a84b;">lcy861013@gmail.com</a></p>
</div>
""",
    "pt": """  <div class="author-meta" style="border-bottom:1px solid #2a2724;padding:10px 0;margin-bottom:20px;">
  <p style="margin:0;">Por <strong>Changyong Lee</strong> | Fundador FITME, Ansan</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">Guia baseado em pesquisa. Fontes: <a href="https://en.wikipedia.org/wiki/Dressing_by_body_type_in_women" target="_blank" rel="noopener" style="color:#d4a84b;">Kibbe</a>, <a href="https://www.iso.org/standard/69080.html" target="_blank" rel="noopener" style="color:#d4a84b;">ISO 8559</a> | Atualizado: 2026.05.19</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">Contato: <a href="mailto:lcy861013@gmail.com" style="color:#d4a84b;">lcy861013@gmail.com</a></p>
</div>
""",
}

DISCLAIMER = {
    "en": '  <p class="ymyl-disclaimer"><strong>Disclaimer:</strong> For education and style only; not medical or health advice.</p>\n',
    "ko": '  <p class="ymyl-disclaimer"><strong>면책조항:</strong> 스타일 교육 목적이며, 의학·건강 조언이 아닙니다.</p>\n',
    "ja": '  <p class="ymyl-disclaimer"><strong>免責:</strong> スタイル教育目的。医学的助言ではありません。</p>\n',
    "pt": '  <p class="ymyl-disclaimer"><strong>Aviso:</strong> Conteúdo educacional; não é aconselhamento médico.</p>\n',
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
    if 'author-meta" style="border-bottom' in text:
        return False
    lang = lang_for(path)
    block = AUTHOR_TOP[lang]
    if '  <div class="related">' in text:
        if "ymyl-disclaimer" not in text:
            text = text.replace('  <div class="related">', DISCLAIMER[lang] + '  <div class="related">', 1)
        import re
        m = re.search(r"(<h1>[^<]+</h1>\s*<div class=\"meta\">[^<]*</div>\s*)", text)
        if m:
            text = text[: m.end()] + block + text[m.end() :]
            path.write_text(text, encoding="utf-8")
            return True
    return False


def main() -> None:
    n = sum(1 for f in BLOG.rglob("*.html") if f.name != "index.html" and inject_file(f))
    print(f"Done. Updated {n} blog files.")


if __name__ == "__main__":
    main()
