#!/usr/bin/env python3
"""Single-language contact pages for 15 locales + English-only root /contact.html."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://perfectfitme.com"

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
footer{{text-align:center;padding:24px;font-size:12px;color:var(--muted);border-top:1px solid var(--border);}}
footer a{{color:var(--muted);}}
</style>
<link rel="stylesheet" href="/assets/satellite-pages-theme.css?v=7">
"""


def _load_about_module():
    path = ROOT / "tools" / "build-locale-about-15lang.py"
    spec = importlib.util.spec_from_file_location("about15", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


about = _load_about_module()
LANGS = about.LANGS
META = about.META
NAV = about.LOCALES

CONTACT: dict[str, dict[str, str]] = {
    "en": {
        "title": "Contact FITME",
        "desc": "Contact FITME by email. Ansan, South Korea. Reply within 72 hours.",
        "h1": "Contact FITME",
        "op": "FITME is operated by solo founder <strong>Changyong Lee</strong> (Ansan, South Korea).",
        "intro": "For questions, feedback, or partnership inquiries:",
        "email_l": "Email:",
        "location_l": "Location:",
        "location": "Ansan, South Korea",
        "reply": "We aim to reply within 72 hours.",
    },
    "ko": {
        "title": "문의하기 — FITME",
        "desc": "FITME 문의: 이메일 lcy861013@gmail.com · 안산 · 72시간 내 답변 목표.",
        "h1": "문의하기",
        "op": "FITME는 1인 창업가 <strong>이창용</strong>이 운영합니다.",
        "intro": "질문, 피드백, 제휴 문의:",
        "email_l": "이메일:",
        "location_l": "위치:",
        "location": "대한민국 안산",
        "reply": "72시간 이내 답변을 목표로 합니다.",
    },
    "ja": {
        "title": "お問い合わせ — FITME",
        "desc": "FITMEへの連絡先。安山（韓国）。72時間以内の返信を目標。",
        "h1": "お問い合わせ",
        "op": "FITMEは<strong>李昌龍</strong>が一人で運営しています。",
        "intro": "ご質問・フィードバック・提携のお問い合わせ:",
        "email_l": "メール:",
        "location_l": "所在地:",
        "location": "韓国・安山",
        "reply": "72時間以内の返信を目標としています。",
    },
    "pt": {
        "title": "Contato — FITME",
        "desc": "Contato FITME por e-mail. Ansan, Coreia do Sul. Resposta em até 72 horas.",
        "h1": "Contato FITME",
        "op": "A FITME é operada pelo fundador solo <strong>Changyong Lee</strong>.",
        "intro": "Dúvidas, feedback ou parcerias:",
        "email_l": "E-mail:",
        "location_l": "Local:",
        "location": "Ansan, Coreia do Sul",
        "reply": "Respondemos em até 72 horas.",
    },
    "es": {
        "title": "Contacto — FITME",
        "desc": "Contacto FITME por correo. Ansan, Corea del Sur. Respuesta en 72 horas.",
        "h1": "Contacto FITME",
        "op": "FITME la opera el fundador en solitario <strong>Changyong Lee</strong>.",
        "intro": "Preguntas, comentarios o colaboraciones:",
        "email_l": "Correo:",
        "location_l": "Ubicación:",
        "location": "Ansan, Corea del Sur",
        "reply": "Respondemos en un plazo de 72 horas.",
    },
    "zh": {
        "title": "联系 FITME",
        "desc": "通过邮件联系 FITME。韩国安山。目标 72 小时内回复。",
        "h1": "联系 FITME",
        "op": "FITME 由独立创始人 <strong>Changyong Lee</strong> 运营。",
        "intro": "问题、反馈或合作咨询:",
        "email_l": "邮箱:",
        "location_l": "地点:",
        "location": "韩国安山",
        "reply": "我们将在 72 小时内回复。",
    },
    "fr": {
        "title": "Contact — FITME",
        "desc": "Contactez FITME par e-mail. Ansan, Corée du Sud. Réponse sous 72 h.",
        "h1": "Contact FITME",
        "op": "FITME est exploité par le fondateur solo <strong>Changyong Lee</strong>.",
        "intro": "Questions, retours ou partenariats :",
        "email_l": "E-mail :",
        "location_l": "Lieu :",
        "location": "Ansan, Corée du Sud",
        "reply": "Réponse visée sous 72 heures.",
    },
    "de": {
        "title": "Kontakt — FITME",
        "desc": "FITME per E-Mail kontaktieren. Ansan, Südkorea. Antwort innerhalb von 72 Stunden.",
        "h1": "Kontakt FITME",
        "op": "FITME wird von Solo-Gründer <strong>Changyong Lee</strong> betrieben.",
        "intro": "Fragen, Feedback oder Partnerschaften:",
        "email_l": "E-Mail:",
        "location_l": "Standort:",
        "location": "Ansan, Südkorea",
        "reply": "Antwort innerhalb von 72 Stunden angestrebt.",
    },
    "it": {
        "title": "Contatti — FITME",
        "desc": "Contatta FITME via e-mail. Ansan, Corea del Sud. Risposta entro 72 ore.",
        "h1": "Contatti FITME",
        "op": "FITME è gestito dal fondatore unico <strong>Changyong Lee</strong>.",
        "intro": "Domande, feedback o partnership:",
        "email_l": "E-mail:",
        "location_l": "Sede:",
        "location": "Ansan, Corea del Sud",
        "reply": "Rispondiamo entro 72 ore.",
    },
    "ru": {
        "title": "Контакты — FITME",
        "desc": "Связь с FITME по e-mail. Ансан, Южная Корея. Ответ в течение 72 часов.",
        "h1": "Контакты FITME",
        "op": "FITME ведёт основатель-одиночка <strong>Changyong Lee</strong>.",
        "intro": "Вопросы, отзывы или сотрудничество:",
        "email_l": "E-mail:",
        "location_l": "Местоположение:",
        "location": "Ансан, Южная Корея",
        "reply": "Отвечаем в течение 72 часов.",
    },
    "ar": {
        "title": "تواصل — FITME",
        "desc": "تواصل مع FITME عبر البريد. أنسان، كوريا الجنوبية. رد خلال 72 ساعة.",
        "h1": "تواصل FITME",
        "op": "يُشغّل FITME المؤسس المنفرد <strong>Changyong Lee</strong>.",
        "intro": "أسئلة أو ملاحظات أو شراكات:",
        "email_l": "البريد:",
        "location_l": "الموقع:",
        "location": "أنسان، كوريا الجنوبية",
        "reply": "نهدف للرد خلال 72 ساعة.",
    },
    "hi": {
        "title": "संपर्क — FITME",
        "desc": "FITME से ईमेल पर संपर्क करें। अंसान, दक्षिण कोरिया। 72 घंटे में जवाब।",
        "h1": "संपर्क FITME",
        "op": "FITME को स्वतंत्र संस्थापक <strong>Changyong Lee</strong> चलाते हैं।",
        "intro": "प्रश्न, प्रतिक्रिया या साझेदारी:",
        "email_l": "ईमेल:",
        "location_l": "स्थान:",
        "location": "अंसान, दक्षिण कोरिया",
        "reply": "72 घंटे के भीतर जवाब देने का लक्ष्य।",
    },
    "th": {
        "title": "ติดต่อ — FITME",
        "desc": "ติดต่อ FITME ทางอีเมล อันซาน เกาหลีใต้ ตอบภายใน 72 ชั่วโมง",
        "h1": "ติดต่อ FITME",
        "op": "FITME ดำเนินการโดยผู้ก่อตั้งเดี่ยว <strong>Changyong Lee</strong>",
        "intro": "คำถาม ข้อเสนอแนะ หรือความร่วมมือ:",
        "email_l": "อีเมล:",
        "location_l": "ที่ตั้ง:",
        "location": "อันซาน เกาหลีใต้",
        "reply": "ตอบกลับภายใน 72 ชั่วโมง",
    },
    "id": {
        "title": "Kontak — FITME",
        "desc": "Hubungi FITME via email. Ansan, Korea Selatan. Balasan dalam 72 jam.",
        "h1": "Kontak FITME",
        "op": "FITME dioperasikan oleh pendiri solo <strong>Changyong Lee</strong>.",
        "intro": "Pertanyaan, masukan, atau kemitraan:",
        "email_l": "Email:",
        "location_l": "Lokasi:",
        "location": "Ansan, Korea Selatan",
        "reply": "Kami membalas dalam 72 jam.",
    },
    "vi": {
        "title": "Liên hệ — FITME",
        "desc": "Liên hệ FITME qua email. Ansan, Hàn Quốc. Phản hồi trong 72 giờ.",
        "h1": "Liên hệ FITME",
        "op": "FITME do nhà sáng lập độc lập <strong>Changyong Lee</strong> vận hành.",
        "intro": "Câu hỏi, góp ý hoặc hợp tác:",
        "email_l": "Email:",
        "location_l": "Địa điểm:",
        "location": "Ansan, Hàn Quốc",
        "reply": "Chúng tôi phản hồi trong 72 giờ.",
    },
}


def hreflang_contact() -> str:
    lines = [f'<link rel="alternate" hreflang="en" href="{SITE}/contact.html">']
    for loc in LANGS:
        if loc == "en":
            continue
        lines.append(
            f'<link rel="alternate" hreflang="{loc}" href="{SITE}/{loc}/contact.html">'
        )
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}/contact.html">')
    return "\n".join(lines)


def locale_contact_html(loc: str) -> str:
    c = CONTACT[loc]
    n = NAV[loc]
    html_lang, extra = META[loc]
    canon = f"{SITE}/{loc}/contact.html"
    body = f"""  <h1>{c['h1']}</h1>
  <p>{c['op']}</p>
  <p>{c['intro']}</p>
  <p><strong>{c['email_l']}</strong> <a href="mailto:lcy861013@gmail.com" style="color:var(--accent);">lcy861013@gmail.com</a></p>
  <p><strong>{c['location_l']}</strong> {c['location']}</p>
  <p>{c['reply']}</p>
"""
    return f"""<!DOCTYPE html>
<html lang="{html_lang}"{extra}>
<head>
  <script src="/consent-init.js?v=7"></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-JW0DB4GXG3"></script>
  <script>gtag('js', new Date()); gtag('config', 'G-JW0DB4GXG3');</script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{c['title']}</title>
  <meta name="description" content="{c['desc']}">
  <meta property="og:title" content="{c['title']}">
  <meta property="og:description" content="{c['desc']}">
  <meta property="og:image" content="{SITE}/assets/og-image-en.png">
  <meta property="og:url" content="{canon}">
  <link rel="canonical" href="{canon}">
{hreflang_contact()}
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
    <a href="/#analysis">{n['nav_analysis']}</a>
    <a href="/blog/">{n['nav_blog']}</a>
    <a href="/{loc}/about.html">{n['nav_about']}</a>
    <a href="/{loc}/contact.html" style="color:var(--accent);">{n['nav_contact']}</a>
    <a href="/privacy.html">{n['nav_privacy']}</a>
  </nav>
</header>
<main>
{body}
</main>
<footer><p>{n['footer_copy']} · <a href="/privacy.html">{n['footer_privacy']}</a> · <a href="/terms.html">{n['footer_terms']}</a> · <a href="/{loc}/contact.html">{n['footer_contact']}</a> · <a href="/{loc}/about.html">{n['footer_about']}</a></p></footer>
<script defer src="/cookie-consent.js?v=7"></script>
</body>
</html>
"""


def patch_root_contact() -> None:
    c = CONTACT["en"]
    p = ROOT / "contact.html"
    text = p.read_text(encoding="utf-8")
    text = re.sub(
        r'\s*<section lang="ko"[^>]*>.*?</section>\s*',
        "\n",
        text,
        flags=re.S,
    )
    text = re.sub(
        r"<p>FITME is operated by[^<]*</p>\s*",
        f"  <p>{c['op']}</p>\n",
        text,
        count=1,
    )
    text = re.sub(
        r"\n*<link rel=\"alternate\" hreflang=\"[^\"]+\"[^>]*>\s*",
        "\n",
        text,
    )
    m = re.search(r"(<link rel=\"canonical\"[^>]*>\s*)", text, re.I)
    if m:
        text = text[: m.end()] + "\n" + hreflang_contact() + "\n" + text[m.end() :]
    p.write_text(text, encoding="utf-8")
    print("patched root contact.html")


def strip_non_english_from_legal(name: str) -> None:
    p = ROOT / name
    if not p.exists():
        return
    text = p.read_text(encoding="utf-8")
    orig = text
    text = re.sub(r'\s*<section lang="ko">.*?</section>\s*', "\n", text, flags=re.S)
    text = re.sub(r'\s*<hr[^>]*>\s*(?=<section)', "\n", text)
    if text != orig:
        p.write_text(text, encoding="utf-8")
        print(f"cleaned {name}")


def main() -> None:
    for loc in LANGS:
        (ROOT / loc).mkdir(exist_ok=True)
        out = ROOT / loc / "contact.html"
        out.write_text(locale_contact_html(loc), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))
    patch_root_contact()
    for legal in ("privacy.html", "terms.html"):
        strip_non_english_from_legal(legal)


if __name__ == "__main__":
    main()
