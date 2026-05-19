#!/usr/bin/env python3
"""Create /ko|en|ja|pt/about.html and contact.html for GitHub Pages."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://perfectfitme.com"

HREFLANG = """<link rel="alternate" hreflang="ko" href="{SITE}/ko/about.html">
<link rel="alternate" hreflang="en" href="{SITE}/en/about.html">
<link rel="alternate" hreflang="ja" href="{SITE}/ja/about.html">
<link rel="alternate" hreflang="pt" href="{SITE}/pt/about.html">
<link rel="alternate" hreflang="x-default" href="{SITE}/en/about.html">"""

HREFLANG_CONTACT = HREFLANG.replace("/about.html", "/contact.html")

HEAD_EXTRA = """
<style>
:root{{--bg:#0f0e0d;--surface:#161412;--card:#1c1a18;--accent:#d4a84b;--text:#e0dcd8;--muted:#8b8178;--border:#2a2724;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:var(--bg);color:var(--text);font-family:'DM Sans',sans-serif;line-height:1.7;}}
header{{padding:16px 24px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;background:rgba(10,10,10,0.95);backdrop-filter:blur(15px);z-index:100;}}
.logo{{font-family:'Bebas Neue',sans-serif;font-size:24px;color:var(--accent);text-decoration:none;letter-spacing:2px;}}
.logo span{{color:var(--text);}}
nav{{display:flex;gap:20px;align-items:center;flex-wrap:wrap;}}
nav a{{color:var(--muted);font-size:13px;text-decoration:none;letter-spacing:1px;}}
nav a:hover{{color:var(--accent);}}
main{{max-width:720px;margin:0 auto;padding:60px 20px 80px;}}
h1{{font-family:'Bebas Neue',sans-serif;font-size:clamp(32px,7vw,52px);line-height:1.1;margin-bottom:16px;letter-spacing:1px;color:var(--accent);}}
p{{font-size:15px;line-height:1.9;color:#d0d0d0;margin-bottom:18px;}}
.cta{{margin-top:48px;padding:32px;background:var(--card);border-radius:16px;border:1px solid var(--border);text-align:center;}}
.cta-btn{{display:inline-block;background:var(--accent);color:#0f0e0d;padding:14px 36px;border-radius:50px;font-weight:700;font-size:16px;text-decoration:none;margin-top:14px;}}
footer{{text-align:center;padding:24px;font-size:12px;color:var(--muted);border-top:1px solid var(--border);}}
footer a{{color:var(--muted);}}
</style>
<link rel="stylesheet" href="/assets/satellite-pages-theme.css?v=7">
"""

ABOUT = {
    "en": {
        "lang": "en",
        "title": "About FITME — Solo Founder",
        "desc": "FITME is built by Changyong Lee, a solo founder in Ansan, South Korea. Research-based proportion tools.",
        "main": """  <h1>About FITME</h1>
  <p>FITME is independently built and maintained by <strong>Changyong Lee</strong>, a solo founder based in Ansan, South Korea.</p>
  <p><strong>Why I Built FITME:</strong> I struggled to find clothes that fit my proportions. Standard S/M/L sizes ignored my torso-to-leg ratio and shoulder width. After researching fit systems like <a href="https://en.wikipedia.org/wiki/Dressing_by_body_type_in_women" target="_blank" rel="noopener" style="color:var(--accent);">Kibbe Body Types</a> and <a href="https://www.iso.org/standard/69080.html" target="_blank" rel="noopener" style="color:var(--accent);">ISO 8559 garment standards</a>, I built this tool to share what I learned.</p>
  <p><strong>Project Started:</strong> March 2026</p>
  <p><strong>Contact:</strong> <a href="/en/contact.html" style="color:var(--accent);">Contact page</a> · <a href="mailto:lcy861013@gmail.com" style="color:var(--accent);">lcy861013@gmail.com</a></p>
""",
        "cta": "Analyze My Body Type Free →",
        "cta_sub": "Height, weight, waist — runs in your browser",
    },
    "ko": {
        "lang": "ko",
        "title": "About FITME — 1인 창업가",
        "desc": "FITME는 안산의 1인 창업가 이창용이 운영하는 체형 비율·핏 가이드 사이트입니다.",
        "main": """  <h1>About FITME</h1>
  <p>FITME는 안산에 거주하는 1인 창업가 <strong>이창용</strong>이 직접 만들고 운영합니다.</p>
  <p><strong>제작 계기:</strong> 제 사이즈에 맞는 옷을 사도 체형 비율이 맞지 않아 실패를 반복했습니다. 어깨-힙 비율, 몸통-다리 비율을 무시한 S/M/L 사이즈의 한계를 느끼고 <a href="https://en.wikipedia.org/wiki/Dressing_by_body_type_in_women" target="_blank" rel="noopener" style="color:var(--accent);">키비 바디타입</a>, <a href="https://www.iso.org/standard/69080.html" target="_blank" rel="noopener" style="color:var(--accent);">ISO 8559 의류 표준</a>을 연구해 이 도구를 만들었습니다.</p>
  <p><strong>프로젝트 시작:</strong> 2026년 3월</p>
  <p><strong>문의:</strong> <a href="/ko/contact.html" style="color:var(--accent);">문의 페이지</a> · <a href="mailto:lcy861013@gmail.com" style="color:var(--accent);">lcy861013@gmail.com</a></p>
""",
        "cta": "무료 체형 분석하기 →",
        "cta_sub": "키·몸무게·허리 — 브라우저에서만 처리",
    },
    "ja": {
        "lang": "ja",
        "title": "FITMEについて — 運営者",
        "desc": "FITMEは韓国安山の李昌龍が運営する、体型比率の教育ツールです。",
        "main": """  <h1>About FITME</h1>
  <p>FITMEは韓国安山を拠点とする<strong>李昌龍</strong>が一人で開発・運営しています。</p>
  <p><strong>制作のきっかけ:</strong> 標準サイズでは胴と脚の比率が合わず、服選びに苦労しました。<a href="https://en.wikipedia.org/wiki/Dressing_by_body_type_in_women" target="_blank" rel="noopener" style="color:var(--accent);">Kibbe</a>や<a href="https://www.iso.org/standard/69080.html" target="_blank" rel="noopener" style="color:var(--accent);">ISO 8559</a>などの研究をもとに、このツールを公開しました。</p>
  <p><strong>開始:</strong> 2026年3月</p>
  <p><strong>連絡:</strong> <a href="/ja/contact.html" style="color:var(--accent);">お問い合わせ</a> · <a href="mailto:lcy861013@gmail.com" style="color:var(--accent);">lcy861013@gmail.com</a></p>
""",
        "cta": "無料で体型分析 →",
        "cta_sub": "身長・体重・ウエスト — ブラウザ内で処理",
    },
    "pt": {
        "lang": "pt-BR",
        "title": "Sobre a FITME — Fundador",
        "desc": "FITME é operada por Changyong Lee, fundador solo em Ansan, Coreia do Sul.",
        "main": """  <h1>About FITME</h1>
  <p>A FITME é criada e mantida por <strong>Changyong Lee</strong>, fundador solo em Ansan, Coreia do Sul.</p>
  <p><strong>Por que criei a FITME:</strong> Tamanhos S/M/L ignoravam minhas proporções. Pesquisei sistemas como <a href="https://en.wikipedia.org/wiki/Dressing_by_body_type_in_women" target="_blank" rel="noopener" style="color:var(--accent);">Kibbe</a> e <a href="https://www.iso.org/standard/69080.html" target="_blank" rel="noopener" style="color:var(--accent);">ISO 8559</a> e transformei isso em uma ferramenta prática.</p>
  <p><strong>Início do projeto:</strong> março de 2026</p>
  <p><strong>Contato:</strong> <a href="/pt/contact.html" style="color:var(--accent);">Página de contato</a> · <a href="mailto:lcy861013@gmail.com" style="color:var(--accent);">lcy861013@gmail.com</a></p>
""",
        "cta": "Analisar proporções grátis →",
        "cta_sub": "Altura, peso, cintura — no navegador",
    },
}

CONTACT = {
    "en": {
        "lang": "en",
        "title": "Contact FITME",
        "desc": "Contact FITME by email. Ansan, South Korea. Reply within 72 hours.",
        "main": """  <h1>Contact FITME</h1>
  <p>FITME is operated by solo founder <strong>Changyong Lee</strong>.</p>
  <p>For questions, feedback, or partnership inquiries:</p>
  <p><strong>Email:</strong> <a href="mailto:lcy861013@gmail.com" style="color:var(--accent);">lcy861013@gmail.com</a></p>
  <p><strong>Location:</strong> Ansan, South Korea</p>
  <p>We aim to reply within 72 hours.</p>
""",
    },
    "ko": {
        "lang": "ko",
        "title": "문의하기 — FITME",
        "desc": "FITME 문의: 이메일 lcy861013@gmail.com · 안산 · 72시간 내 답변 목표.",
        "main": """  <h1>문의하기</h1>
  <p>FITME는 1인 창업가 <strong>이창용</strong>이 운영합니다.</p>
  <p>질문, 피드백, 제휴 문의:</p>
  <p><strong>이메일:</strong> <a href="mailto:lcy861013@gmail.com" style="color:var(--accent);">lcy861013@gmail.com</a></p>
  <p><strong>위치:</strong> 대한민국 안산</p>
  <p>72시간 이내 답변을 목표로 합니다.</p>
""",
    },
    "ja": {
        "lang": "ja",
        "title": "お問い合わせ — FITME",
        "desc": "FITMEへの連絡先。安山（韓国）。72時間以内の返信を目標。",
        "main": """  <h1>お問い合わせ</h1>
  <p>FITMEは<strong>李昌龍</strong>が一人で運営しています（solo founder）。</p>
  <p>ご質問・フィードバック・提携のお問い合わせ:</p>
  <p><strong>メール:</strong> <a href="mailto:lcy861013@gmail.com" style="color:var(--accent);">lcy861013@gmail.com</a></p>
  <p><strong>所在地:</strong> 韓国・安山</p>
  <p>72時間以内の返信を目標としています。</p>
""",
    },
    "pt": {
        "lang": "pt-BR",
        "title": "Contato — FITME",
        "desc": "Contato FITME por e-mail. Ansan, Coreia do Sul. Resposta em até 72 horas.",
        "main": """  <h1>Contato FITME</h1>
  <p>A FITME é operada pelo fundador solo <strong>Changyong Lee</strong>.</p>
  <p>Dúvidas, feedback ou parcerias:</p>
  <p><strong>E-mail:</strong> <a href="mailto:lcy861013@gmail.com" style="color:var(--accent);">lcy861013@gmail.com</a></p>
  <p><strong>Local:</strong> Ansan, Coreia do Sul</p>
  <p>Respondemos em até 72 horas.</p>
""",
    },
}


def page_html(locale: str, kind: str, data: dict) -> str:
    path = f"/{locale}/{kind}.html"
    canon = f"{SITE}{path}"
    hreflang = HREFLANG_CONTACT if kind == "contact" else HREFLANG
    hreflang = hreflang.format(SITE=SITE)
    about_active = ' style="color:var(--accent);"' if kind == "about" else ""
    contact_active = ' style="color:var(--accent);"' if kind == "contact" else ""
    cta_block = ""
    if kind == "about":
        cta_block = f"""
  <div class="cta">
    <motion style="font-weight:700;font-size:18px;margin-bottom:8px;">{data.get('cta_sub','')}</div>
    <a href="/?utm_source=about&utm_medium=cta&utm_campaign=analysis#analysis" class="cta-btn">{data.get('cta','')}</a>
  </motion>"""
        cta_block = cta_block.replace("<motion", "<div").replace("</motion>", "</div>")
        cta_block = f"""
  <div class="cta">
    <motion style="font-weight:700;font-size:18px;margin-bottom:8px;">{data['cta_sub']}</div>
    <a href="/?utm_source=about&utm_medium=cta&utm_campaign=analysis#analysis" class="cta-btn">{data['cta']}</a>
  </div>""".replace("<motion", "<div").replace("</motion>", "</div>")
    return f"""<!DOCTYPE html>
<html lang="{data['lang']}">
<head>
  <script src="/consent-init.js?v=7"></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-JW0DB4GXG3"></script>
  <script>gtag('js', new Date()); gtag('config', 'G-JW0DB4GXG3');</script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data['title']}</title>
  <meta name="description" content="{data['desc']}">
  <meta property="og:title" content="{data['title']}">
  <meta property="og:description" content="{data['desc']}">
  <meta property="og:image" content="{SITE}/assets/og-image-en.png">
  <meta property="og:url" content="{canon}">
  <link rel="canonical" href="{canon}">
{hreflang}
  <link rel="icon" href="/favicon-32x32.png">
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <meta name="google-adsense-account" content="ca-pub-6377720400458954">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6377720400458954" crossorigin="anonymous"></script>
{HEAD_EXTRA}
</head>
<body>
<header>
  <a href="/" class="logo">FIT<span>ME</span></a>
  <nav>
    <a href="/#analysis">Analysis</a>
    <a href="/blog/">Blog</a>
    <a href="/{locale}/about.html"{about_active}>About</a>
    <a href="/{locale}/contact.html"{contact_active}>Contact</a>
    <a href="/privacy.html">Privacy</a>
  </nav>
</header>
<main>
{data['main']}{cta_block}
</main>
<footer><p>© 2026 FITME · <a href="/privacy.html">Privacy</a> · <a href="/terms.html">Terms</a> · <a href="/{locale}/contact.html">Contact</a> · <a href="/{locale}/about.html">About</a></p></footer>
<script defer src="/cookie-consent.js?v=7"></script>
</body>
</html>
"""


def patch_root_hreflang() -> None:
    block_about = HREFLANG.format(SITE=SITE) + "\n"
    block_contact = HREFLANG_CONTACT.format(SITE=SITE) + "\n"
    for name, block in (("about.html", block_about), ("contact.html", block_contact)):
        p = ROOT / name
        text = p.read_text(encoding="utf-8")
        import re
        text = re.sub(
            r"\n*<link rel=\"alternate\" hreflang=\"[^\"]+\"[^>]*>\s*",
            "\n",
            text,
        )
        m = re.search(r"(<link rel=\"canonical\"[^>]*>\s*)", text, re.I)
        if m:
            text = text[: m.end()] + "\n" + block + text[m.end() :]
        p.write_text(text, encoding="utf-8")


def main() -> None:
    for loc in ("ko", "en", "ja", "pt"):
        (ROOT / loc).mkdir(exist_ok=True)
        for kind, data in (("about", ABOUT[loc]), ("contact", CONTACT[loc])):
            out = ROOT / loc / f"{kind}.html"
            out.write_text(page_html(loc, kind, data), encoding="utf-8")
            print("wrote", out.relative_to(ROOT))
    patch_root_hreflang()
    print("updated root hreflang")


if __name__ == "__main__":
    main()
