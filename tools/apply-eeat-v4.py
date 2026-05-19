#!/usr/bin/env python3
"""AdSense 4th pass: factual E-E-A-T — top author-meta, personal-note, keep bottom disclaimer."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"

AUTHOR_TOP = {
    "en": """  <motion class="author-meta" style="border-bottom:1px solid #2a2724;padding:10px 0;margin-bottom:20px;">
  <p style="margin:0;">By <strong>Changyong Lee</strong> | FITME Founder, Ansan, South Korea</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">Research-based guide. Sources: <a href="https://en.wikipedia.org/wiki/Kibbe_body_types" target="_blank" rel="noopener" style="color:#d4a84b;">Kibbe</a>, <a href="https://www.iso.org/standard/69080.html" target="_blank" rel="noopener" style="color:#d4a84b;">ISO 8559</a> | Last Updated: 2026.05.19</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">Contact: <a href="mailto:lcy861013@gmail.com" style="color:#d4a84b;">lcy861013@gmail.com</a></p>
</div>
""".replace("<motion class=", "<motion class=").replace(
        '<motion class="author-meta"', '<div class="author-meta"'
    ),
    "ko": """  <div class="author-meta" style="border-bottom:1px solid #2a2724;padding:10px 0;margin-bottom:20px;">
  <p style="margin:0;">글쓴이: <strong>이창용</strong> | FITME 대표, 안산</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">연구 기반 가이드. 출처: <a href="https://en.wikipedia.org/wiki/Kibbe_body_types" target="_blank" rel="noopener" style="color:#d4a84b;">키비 바디타입</a>, <a href="https://www.iso.org/standard/69080.html" target="_blank" rel="noopener" style="color:#d4a84b;">ISO 8559</a> | 최종 업데이트: 2026.05.19</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">문의: <a href="mailto:lcy861013@gmail.com" style="color:#d4a84b;">lcy861013@gmail.com</a></p>
</div>
""",
    "ja": """  <div class="author-meta" style="border-bottom:1px solid #2a2724;padding:10px 0;margin-bottom:20px;">
  <p style="margin:0;">著者: <strong>李昌龍</strong> | FITME代表、安山</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">研究ガイド。出典: <a href="https://en.wikipedia.org/wiki/Kibbe_body_types" target="_blank" rel="noopener" style="color:#d4a84b;">Kibbe</a>, <a href="https://www.iso.org/standard/69080.html" target="_blank" rel="noopener" style="color:#d4a84b;">ISO 8559</a> | 更新: 2026.05.19</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">連絡: <a href="mailto:lcy861013@gmail.com" style="color:#d4a84b;">lcy861013@gmail.com</a></p>
</div>
""",
    "pt": """  <div class="author-meta" style="border-bottom:1px solid #2a2724;padding:10px 0;margin-bottom:20px;">
  <p style="margin:0;">Por <strong>Changyong Lee</strong> | Fundador FITME, Ansan</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">Guia baseado em pesquisa. Fontes: <a href="https://en.wikipedia.org/wiki/Kibbe_body_types" target="_blank" rel="noopener" style="color:#d4a84b;">Kibbe</a>, <a href="https://www.iso.org/standard/69080.html" target="_blank" rel="noopener" style="color:#d4a84b;">ISO 8559</a> | Atualizado: 2026.05.19</p>
  <p style="margin:0;font-size:14px;color:#8b8178;">Contato: <a href="mailto:lcy861013@gmail.com" style="color:#d4a84b;">lcy861013@gmail.com</a></p>
</div>
""",
}

PERSONAL = {
    "en": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>My Research Note:</strong> Standard size charts failed me because they don't account for torso-to-leg ratio. I studied anthropometric data and fit systems to build this framework. This guide reflects that research and is for educational purposes only, not medical advice.
</div>
""",
    "ko": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>작성자 경험:</strong> 표준 사이즈표는 몸통-다리 비율을 반영하지 않아 저에게 맞지 않았습니다. 인체측정 데이터와 핏 시스템을 연구해 이 프레임워크를 만들었습니다. 본 가이드는 그 연구 결과이며 의학적 조언이 아닙니다.
</div>
""",
    "ja": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>研究メモ:</strong> 標準サイズは胴と脚の比率を反映しないため、私には合いませんでした。人体データとフィット理論を調べてまとめました。医学的助言ではありません。
</div>
""",
    "pt": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Nota de pesquisa:</strong> Tabelas de tamanho padrão ignoram a proporção tronco-perna. Estudei dados antropométricos e sistemas de caimento — não é conselho médico.
</div>
""",
}

BOTTOM_AUTHOR_RE = re.compile(
    r"\n[ \t]*<div class=\"author-meta\">(?!.*border-bottom).*?</div>\s*\n",
    re.DOTALL,
)
TOP_AUTHOR_RE = re.compile(
    r"\n[ \t]*<div class=\"author-meta\" style=\"border-bottom.*?</motion>\s*\n"
    r"|\n[ \t]*<div class=\"author-meta\" style=\"border-bottom.*?</motion>\s*\n",
    re.DOTALL,
)
TOP_AUTHOR_RE = re.compile(
    r"\n[ \t]*<div class=\"author-meta\" style=\"border-bottom.*?</div>\s*\n",
    re.DOTALL,
)
OLD_PERSONAL_RE = re.compile(
    r"\n[ \t]*<div class=\"personal-note\"[^>]*>.*?</div>\s*\n",
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


def insert_top_author(text: str, lang: str) -> str:
    block = AUTHOR_TOP[lang]
    text = TOP_AUTHOR_RE.sub("\n", text)
    if 'author-meta" style="border-bottom' in text:
        return text
    m = re.search(r"(<h1>[^<]+</h1>\s*<div class=\"meta\">[^<]*</div>\s*)", text)
    if m:
        return text[: m.end()] + block + text[m.end() :]
    m2 = re.search(r"(<h1>[^<]+</h1>\s*)", text)
    if m2:
        return text[: m2.end()] + block + text[m2.end() :]
    return text


def insert_personal(text: str, lang: str) -> str:
    block = PERSONAL[lang]
    text = OLD_PERSONAL_RE.sub("\n", text)
    if "My Research Note" in text or "작성자 경험" in text:
        if 'style="background:#1c1a18' in text:
            return text
    for pat in (
        r"(<h2>Introduction[^<]*</h2>\s*<p>.*?</p>)",
        r"(<h2>Why Generic[^<]*</h2>\s*<p>.*?</p>)",
        r"(<h2>[^<]*소개[^<]*</h2>\s*<p>.*?</p>)",
    ):
        m = re.search(pat, text, re.DOTALL | re.IGNORECASE)
        if m:
            return text.replace(m.group(1), m.group(1) + "\n" + block, 1)
    m = re.search(r"(<h2>[^<]+</h2>\s*<p>.*?</p>)", text, re.DOTALL)
    if m:
        return text.replace(m.group(1), m.group(1) + "\n" + block, 1)
    return text


def patch_blog(path: Path) -> bool:
    if path.name == "index.html":
        return False
    lang = lang_for(path)
    text = path.read_text(encoding="utf-8")
    orig = text
    text = BOTTOM_AUTHOR_RE.sub("\n", text)
    text = insert_top_author(text, lang)
    text = insert_personal(text, lang)
    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def patch_about() -> None:
    p = ROOT / "about.html"
    raw = p.read_text(encoding="utf-8")
    head = raw.split("<main>")[0]
    foot = """</main>
<footer><p>© 2026 FITME. All rights reserved. · <a href="/privacy.html" style="color:var(--muted);">Privacy Policy</a> · <a href="/terms.html" style="color:var(--muted);">Terms</a> · <a href="/contact.html" style="color:var(--muted);">Contact</a> · <a href="/editorial-standards.html" style="color:var(--muted);">Editorial</a> · <a href="/how-it-works.html" style="color:var(--muted);">How it works</a></p></footer>
<script defer src="/cookie-consent.js?v=7"></script>
</body>
</html>
"""
    main = """<main>
  <section lang="en">
  <h1>About FITME</h1>
  <p>FITME is independently built and maintained by <strong>Changyong Lee</strong>, a solo founder based in Ansan, South Korea.</p>
  <p><strong>Why I Built FITME:</strong> I struggled to find clothes that fit my proportions. Standard S/M/L sizes ignored my torso-to-leg ratio and shoulder width. After researching fit systems like <a href="https://en.wikipedia.org/wiki/Kibbe_body_types" target="_blank" rel="noopener" style="color:var(--accent);">Kibbe Body Types</a> and <a href="https://www.iso.org/standard/69080.html" target="_blank" rel="noopener" style="color:var(--accent);">ISO 8559 garment standards</a>, I built this tool to share what I learned.</p>
  <p><strong>Project Started:</strong> March 2026</p>
  <p><strong>Contact:</strong> <a href="/contact.html" style="color:var(--accent);">Contact page</a> · <a href="mailto:lcy861013@gmail.com" style="color:var(--accent);">lcy861013@gmail.com</a></p>
  </section>
  <hr class="divider" style="margin:40px 0;">
  <section lang="ko">
  <h1>About FITME</h1>
  <p>FITME는 안산에 거주하는 1인 창업가 <strong>이창용</strong>이 직접 만들고 운영합니다.</p>
  <p><strong>제작 계기:</strong> 제 사이즈에 맞는 옷을 사도 체형 비율이 맞지 않아 실패를 반복했습니다. 어깨-힙 비율, 몸통-다리 비율을 무시한 S/M/L 사이즈의 한계를 느끼고 <a href="https://en.wikipedia.org/wiki/Kibbe_body_types" target="_blank" rel="noopener" style="color:var(--accent);">키비 바디타입</a>, <a href="https://www.iso.org/standard/69080.html" target="_blank" rel="noopener" style="color:var(--accent);">ISO 8559 의류 표준</a>을 연구해 이 도구를 만들었습니다.</p>
  <p><strong>프로젝트 시작:</strong> 2026년 3월</p>
  <p><strong>문의:</strong> <a href="/contact.html" style="color:var(--accent);">문의 페이지</a> · <a href="mailto:lcy861013@gmail.com" style="color:var(--accent);">lcy861013@gmail.com</a></p>
  </section>
  <motion class="cta" style="margin-top:48px;padding:32px;background:var(--card);border-radius:16px;border:1px solid var(--border);text-align:center;">
    <div style="font-weight:700;font-size:18px;margin-bottom:8px;">Free proportion analysis</div>
    <div style="font-size:14px;color:var(--muted);">Height, weight, waist — runs in your browser</motion>
    <a href="/?utm_source=about&utm_medium=cta&utm_campaign=analysis#analysis" class="cta-btn">Analyze My Body Type Free →</a>
  </div>
"""
    main = main.replace('<motion class="cta"', '<div class="cta"').replace(
        "browser</motion>", "browser</motion>"
    ).replace("browser</motion>", "browser</div>")
    p.write_text(head + main + foot, encoding="utf-8")
    # fix dateModified
    p.write_text(
        p.read_text(encoding="utf-8").replace(
            '"dateModified": "2026-05-18"', '"dateModified": "2026-05-19"'
        ),
        encoding="utf-8",
    )


def patch_contact() -> None:
    p = ROOT / "contact.html"
    t = p.read_text(encoding="utf-8")
    new_main = """<main>
  <h1>Contact FITME</h1>
  <p>For questions, feedback, or partnership inquiries:</p>
  <p><strong>Email:</strong> <a href="mailto:lcy861013@gmail.com" style="color:var(--accent);">lcy861013@gmail.com</a></p>
  <p><strong>Location:</strong> Ansan, South Korea</p>
  <p>We aim to reply within 72 hours.</p>
  <section lang="ko" style="margin-top:40px;padding-top:32px;border-top:1px solid var(--border);">
  <h1 style="font-size:clamp(28px,6vw,40px);">문의하기</h1>
  <p>질문, 피드백, 제휴 문의:</p>
  <p><strong>이메일:</strong> <a href="mailto:lcy861013@gmail.com" style="color:var(--accent);">lcy861013@gmail.com</a></p>
  <p><strong>위치:</strong> 대한민국 안산</p>
  <p>72시간 이내 답변을 목표로 합니다.</p>
  </section>
</main>"""
    t = re.sub(r"<main>.*?</main>", new_main, t, count=1, flags=re.DOTALL)
    foot = '<footer><p>© 2026 FITME. All rights reserved. · <a href="/privacy.html" style="color:var(--muted);">Privacy Policy</a> · <a href="/terms.html" style="color:var(--muted);">Terms</a> · <a href="/about.html" style="color:var(--muted);">About</a> · <a href="/contact.html" style="color:var(--muted);">Contact</a></p></footer>'
    t = re.sub(r"<footer>.*?</footer>", foot, t, count=1, flags=re.DOTALL)
    if '/contact.html">Contact</a>' not in t.split("<nav>")[1].split("</nav>")[0]:
        t = t.replace(
            '<a href="/privacy.html">Privacy</a>',
            '<a href="/contact.html">Contact</a>\n    <a href="/privacy.html">Privacy</a>',
        )
    p.write_text(t, encoding="utf-8")


def main() -> None:
    patch_about()
    patch_contact()
    n = sum(1 for f in BLOG.rglob("*.html") if patch_blog(f))
    print(f"Done: about + contact + {n} blog files")


if __name__ == "__main__":
    main()
