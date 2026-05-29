#!/usr/bin/env python3
"""Single-language about pages for 15 locales + English-only root /about.html."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://perfectfitme.com"

LANGS = ("ko", "en", "ja", "pt", "es", "zh", "fr", "de", "it", "ru", "ar", "hi", "th", "id", "vi")

# AdSense/GSC: index only full editorial locales; keep others as noindex doorways for UX only.
INDEXABLE_TRUST_LOCALES = frozenset({"ja", "pt"})

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

KIBBE = 'https://en.wikipedia.org/wiki/Dressing_by_body_type_in_women'
ISO = "https://www.iso.org/standard/69080.html"

# lang_code, html_lang, optional dir
META = {
    "ko": ("ko", ""),
    "en": ("en", ""),
    "ja": ("ja", ""),
    "pt": ("pt-BR", ""),
    "es": ("es", ""),
    "zh": ("zh-Hans", ""),
    "fr": ("fr", ""),
    "de": ("de", ""),
    "it": ("it", ""),
    "ru": ("ru", ""),
    "ar": ("ar", ' dir="rtl"'),
    "hi": ("hi", ""),
    "th": ("th", ""),
    "id": ("id", ""),
    "vi": ("vi", ""),
}

LOCALES: dict[str, dict[str, str]] = {
    "en": {
        "title": "About FITME — Solo Founder",
        "desc": "FITME is built by Changyong Lee, a solo founder in Ansan, South Korea. Research-based proportion tools.",
        "h1": "About FITME",
        "p1": "FITME is independently built and maintained by <strong>Changyong Lee</strong>, a solo founder based in Ansan, South Korea.",
        "why_l": "Why I built FITME:",
        "why": "I struggled to find clothes that fit my proportions. Standard S/M/L sizes ignored my torso-to-leg ratio and shoulder width. After researching fit systems like <a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a> and <a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559 garment standards</a>, I built this tool to share what I learned.",
        "started_l": "Project started:",
        "started": "March 2026",
        "contact_l": "Contact:",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">Contact page</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "Analysis",
        "nav_blog": "Blog",
        "nav_about": "About",
        "nav_contact": "Contact",
        "nav_privacy": "Privacy",
        "footer_privacy": "Privacy",
        "footer_terms": "Terms",
        "footer_contact": "Contact",
        "footer_about": "About",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "Height, weight, waist — runs in your browser",
        "cta": "Analyze My Body Type Free →",
    },
    "ko": {
        "title": "FITME 소개 — 1인 창업가",
        "desc": "FITME는 안산의 1인 창업가 이창용이 운영하는 체형 비율·핏 가이드 사이트입니다.",
        "h1": "FITME 소개",
        "p1": "FITME는 안산에 거주하는 1인 창업가 <strong>이창용</strong>이 직접 만들고 운영합니다.",
        "why_l": "제작 계기:",
        "why": "제 사이즈에 맞는 옷을 사도 체형 비율이 맞지 않아 실패를 반복했습니다. 어깨·힙·몸통·다리 비율을 무시한 S/M/L 사이즈의 한계를 느끼고 <a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a>와 <a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559</a> 의류 표준을 연구해 이 도구를 만들었습니다.",
        "started_l": "프로젝트 시작:",
        "started": "2026년 3월",
        "contact_l": "문의:",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">문의 페이지</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "비율 분석",
        "nav_blog": "블로그",
        "nav_about": "소개",
        "nav_contact": "문의",
        "nav_privacy": "개인정보",
        "footer_privacy": "개인정보처리방침",
        "footer_terms": "이용약관",
        "footer_contact": "문의",
        "footer_about": "소개",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "키·몸무게·허리 — 브라우저에서만 처리",
        "cta": "무료 체형 분석하기 →",
    },
    "ja": {
        "title": "FITMEについて — 運営者",
        "desc": "FITMEは韓国安山の李昌龍が運営する、体型比率の教育ツールです。",
        "h1": "FITMEについて",
        "p1": "FITMEは韓国安山を拠点とする<strong>李昌龍</strong>が一人で開発・運営しています。",
        "why_l": "制作のきっかけ:",
        "why": "標準サイズでは胴と脚の比率が合わず、服選びに苦労しました。<a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a>や<a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559</a>などの研究をもとに、このツールを公開しました。",
        "started_l": "開始:",
        "started": "2026年3月",
        "contact_l": "連絡:",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">お問い合わせ</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "体型分析",
        "nav_blog": "ブログ",
        "nav_about": "紹介",
        "nav_contact": "お問い合わせ",
        "nav_privacy": "プライバシー",
        "footer_privacy": "プライバシー",
        "footer_terms": "利用規約",
        "footer_contact": "お問い合わせ",
        "footer_about": "紹介",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "身長・体重・ウエスト — ブラウザ内で処理",
        "cta": "無料で体型分析 →",
    },
    "pt": {
        "title": "Sobre a FITME — Fundador",
        "desc": "A FITME é operada por Changyong Lee, fundador solo em Ansan, Coreia do Sul.",
        "h1": "Sobre a FITME",
        "p1": "A FITME é criada e mantida por <strong>Changyong Lee</strong>, fundador solo em Ansan, Coreia do Sul.",
        "why_l": "Por que criei a FITME:",
        "why": "Tamanhos S/M/L ignoravam minhas proporções. Pesquisei sistemas como <a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a> e <a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559</a> e transformei isso em uma ferramenta prática.",
        "started_l": "Início do projeto:",
        "started": "março de 2026",
        "contact_l": "Contato:",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">Página de contato</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "Análise",
        "nav_blog": "Blog",
        "nav_about": "Sobre",
        "nav_contact": "Contato",
        "nav_privacy": "Privacidade",
        "footer_privacy": "Privacidade",
        "footer_terms": "Termos",
        "footer_contact": "Contato",
        "footer_about": "Sobre",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "Altura, peso, cintura — no navegador",
        "cta": "Analisar proporções grátis →",
    },
    "es": {
        "title": "Sobre FITME — Fundador",
        "desc": "FITME la crea Changyong Lee, fundador en solitario en Ansan, Corea del Sur.",
        "h1": "Sobre FITME",
        "p1": "FITME la desarrolla y mantiene <strong>Changyong Lee</strong>, fundador en solitario con base en Ansan, Corea del Sur.",
        "why_l": "Por qué creé FITME:",
        "why": "Las tallas S/M/L no reflejaban mis proporciones. Investigué sistemas como <a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a> e <a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559</a> y convertí lo aprendido en esta herramienta.",
        "started_l": "Inicio del proyecto:",
        "started": "marzo de 2026",
        "contact_l": "Contacto:",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">Página de contacto</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "Análisis",
        "nav_blog": "Blog",
        "nav_about": "Sobre",
        "nav_contact": "Contacto",
        "nav_privacy": "Privacidad",
        "footer_privacy": "Privacidad",
        "footer_terms": "Términos",
        "footer_contact": "Contacto",
        "footer_about": "Sobre",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "Altura, peso, cintura — en el navegador",
        "cta": "Analizar proporciones gratis →",
    },
    "zh": {
        "title": "关于 FITME — 独立创始人",
        "desc": "FITME 由韩国安山的独立创始人 Changyong Lee 运营，提供体型比例教育工具。",
        "h1": "关于 FITME",
        "p1": "FITME 由居住在韩国安山的独立创始人 <strong>Changyong Lee</strong> 独立开发与运营。",
        "why_l": "创建原因：",
        "why": "标准 S/M/L 尺码无法反映我的肩腰与上下身比例。在研究 <a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a> 与 <a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559</a> 后，我将所学做成这一工具。",
        "started_l": "项目开始：",
        "started": "2026 年 3 月",
        "contact_l": "联系：",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">联系页面</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "比例分析",
        "nav_blog": "博客",
        "nav_about": "关于",
        "nav_contact": "联系",
        "nav_privacy": "隐私",
        "footer_privacy": "隐私政策",
        "footer_terms": "条款",
        "footer_contact": "联系",
        "footer_about": "关于",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "身高、体重、腰围 — 仅在浏览器中处理",
        "cta": "免费分析体型 →",
    },
    "fr": {
        "title": "À propos de FITME — Fondateur",
        "desc": "FITME est créé par Changyong Lee, fondateur solo à Ansan, Corée du Sud.",
        "h1": "À propos de FITME",
        "p1": "FITME est développé et maintenu par <strong>Changyong Lee</strong>, fondateur solo basé à Ansan, Corée du Sud.",
        "why_l": "Pourquoi j’ai créé FITME :",
        "why": "Les tailles S/M/L ignoraient mes proportions. J’ai étudié des systèmes comme <a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a> et <a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559</a>, puis j’ai bâti cet outil.",
        "started_l": "Début du projet :",
        "started": "mars 2026",
        "contact_l": "Contact :",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">Page contact</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "Analyse",
        "nav_blog": "Blog",
        "nav_about": "À propos",
        "nav_contact": "Contact",
        "nav_privacy": "Confidentialité",
        "footer_privacy": "Confidentialité",
        "footer_terms": "Conditions",
        "footer_contact": "Contact",
        "footer_about": "À propos",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "Taille, poids, tour de taille — dans le navigateur",
        "cta": "Analyser mes proportions gratuitement →",
    },
    "de": {
        "title": "Über FITME — Gründer",
        "desc": "FITME wird von Changyong Lee, Solo-Gründer in Ansan, Südkorea, betrieben.",
        "h1": "Über FITME",
        "p1": "FITME wird von <strong>Changyong Lee</strong>, Solo-Gründer in Ansan, Südkorea, entwickelt und betrieben.",
        "why_l": "Warum ich FITME gebaut habe:",
        "why": "S/M/L-Größen passten nicht zu meinen Proportionen. Ich recherchierte <a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a> und <a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559</a> und teile das Wissen hier.",
        "started_l": "Projektstart:",
        "started": "März 2026",
        "contact_l": "Kontakt:",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">Kontaktseite</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "Analyse",
        "nav_blog": "Blog",
        "nav_about": "Über uns",
        "nav_contact": "Kontakt",
        "nav_privacy": "Datenschutz",
        "footer_privacy": "Datenschutz",
        "footer_terms": "AGB",
        "footer_contact": "Kontakt",
        "footer_about": "Über uns",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "Größe, Gewicht, Taille — nur im Browser",
        "cta": "Proportionen kostenlos analysieren →",
    },
    "it": {
        "title": "Informazioni su FITME — Fondatore",
        "desc": "FITME è gestito da Changyong Lee, fondatore unico ad Ansan, Corea del Sud.",
        "h1": "Informazioni su FITME",
        "p1": "FITME è creato e gestito da <strong>Changyong Lee</strong>, fondatore unico con base ad Ansan, Corea del Sud.",
        "why_l": "Perché ho creato FITME:",
        "why": "Le taglie S/M/L non rispettavano le mie proporzioni. Ho studiato <a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a> e <a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559</a> e ho creato questo strumento.",
        "started_l": "Inizio progetto:",
        "started": "marzo 2026",
        "contact_l": "Contatto:",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">Pagina contatti</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "Analisi",
        "nav_blog": "Blog",
        "nav_about": "Chi siamo",
        "nav_contact": "Contatti",
        "nav_privacy": "Privacy",
        "footer_privacy": "Privacy",
        "footer_terms": "Termini",
        "footer_contact": "Contatti",
        "footer_about": "Chi siamo",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "Altezza, peso, vita — nel browser",
        "cta": "Analizza le proporzioni gratis →",
    },
    "ru": {
        "title": "О FITME — Основатель",
        "desc": "FITME создаёт Changyong Lee, основатель-одиночка из Ансана, Южная Корея.",
        "h1": "О FITME",
        "p1": "FITME разрабатывает и ведёт <strong>Changyong Lee</strong>, основатель-одиночка из Ансана, Южная Корея.",
        "why_l": "Зачем я создал FITME:",
        "why": "Размеры S/M/L не отражали мои пропорции. Я изучил <a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a> и <a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559</a> и сделал этот инструмент.",
        "started_l": "Старт проекта:",
        "started": "март 2026",
        "contact_l": "Контакты:",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">Страница контактов</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "Анализ",
        "nav_blog": "Блог",
        "nav_about": "О нас",
        "nav_contact": "Контакты",
        "nav_privacy": "Конфиденциальность",
        "footer_privacy": "Конфиденциальность",
        "footer_terms": "Условия",
        "footer_contact": "Контакты",
        "footer_about": "О нас",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "Рост, вес, талия — только в браузере",
        "cta": "Бесплатный анализ пропорций →",
    },
    "ar": {
        "title": "عن FITME — المؤسس",
        "desc": "يُشغّل FITME تشانغيونغ لي، مؤسس منفرد في أنسان، كوريا الجنوبية.",
        "h1": "عن FITME",
        "p1": "يُطوَّر FITME ويُدار بواسطة <strong>Changyong Lee</strong>، مؤسس منفرد مقيم في أنسان، كوريا الجنوبية.",
        "why_l": "لماذا أنشأت FITME:",
        "why": "مقاسات S/M/L لم تعكس نسب جسمي. بعد دراسة أنظمة مثل <a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a> و<a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559</a> بنيت هذه الأداة.",
        "started_l": "بداية المشروع:",
        "started": "مارس 2026",
        "contact_l": "تواصل:",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">صفحة التواصل</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "تحليل",
        "nav_blog": "مدونة",
        "nav_about": "عنّا",
        "nav_contact": "تواصل",
        "nav_privacy": "الخصوصية",
        "footer_privacy": "الخصوصية",
        "footer_terms": "الشروط",
        "footer_contact": "تواصل",
        "footer_about": "عنّا",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "الطول والوزن والخصر — في المتصفح فقط",
        "cta": "تحليل النسب مجانًا →",
    },
    "hi": {
        "title": "FITME के बारे में — संस्थापक",
        "desc": "FITME को दक्षिण कोरिया के अंसान में रहने वाले स्वतंत्र संस्थापक Changyong Lee चलाते हैं।",
        "h1": "FITME के बारे में",
        "p1": "FITME को <strong>Changyong Lee</strong> ने अकेले बनाया और संचालित किया है, जो दक्षिण कोरिया के अंसान में रहते हैं।",
        "why_l": "FITME क्यों बनाया:",
        "why": "S/M/L साइज़ मेरे अनुपात नहीं दिखाते थे। <a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a> और <a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559</a> का अध्ययन करके यह उपकरण बनाया।",
        "started_l": "प्रोजेक्ट शुरू:",
        "started": "मार्च 2026",
        "contact_l": "संपर्क:",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">संपर्क पृष्ठ</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "विश्लेषण",
        "nav_blog": "ब्लॉग",
        "nav_about": "परिचय",
        "nav_contact": "संपर्क",
        "nav_privacy": "गोपनीयता",
        "footer_privacy": "गोपनीयता",
        "footer_terms": "नियम",
        "footer_contact": "संपर्क",
        "footer_about": "परिचय",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "ऊँचाई, वजन, कमर — केवल ब्राउज़र में",
        "cta": "मुफ्त अनुपात विश्लेषण →",
    },
    "th": {
        "title": "เกี่ยวกับ FITME — ผู้ก่อตั้ง",
        "desc": "FITME ดำเนินการโดย Changyong Lee ผู้ก่อตั้งเดี่ยวที่อันซาน เกาหลีใต้",
        "h1": "เกี่ยวกับ FITME",
        "p1": "FITME สร้างและดูแลโดย <strong>Changyong Lee</strong> ผู้ก่อตั้งเดี่ยวที่อันซาน เกาหลีใต้",
        "why_l": "ทำไมถึงสร้าง FITME:",
        "why": "ไซส์ S/M/L ไม่สะท้อนสัดส่วนร่างกาย หลังศึกษา <a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a> และ <a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559</a> จึงทำเครื่องมือนี้",
        "started_l": "เริ่มโปรเจกต์:",
        "started": "มีนาคม 2026",
        "contact_l": "ติดต่อ:",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">หน้าติดต่อ</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "วิเคราะห์",
        "nav_blog": "บล็อก",
        "nav_about": "เกี่ยวกับ",
        "nav_contact": "ติดต่อ",
        "nav_privacy": "ความเป็นส่วนตัว",
        "footer_privacy": "ความเป็นส่วนตัว",
        "footer_terms": "ข้อกำหนด",
        "footer_contact": "ติดต่อ",
        "footer_about": "เกี่ยวกับ",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "ส่วนสูง น้ำหนัก เอว — ในเบราว์เซอร์เท่านั้น",
        "cta": "วิเคราะห์สัดส่วนฟรี →",
    },
    "id": {
        "title": "Tentang FITME — Pendiri",
        "desc": "FITME dioperasikan oleh Changyong Lee, pendiri solo di Ansan, Korea Selatan.",
        "h1": "Tentang FITME",
        "p1": "FITME dibuat dan dikelola oleh <strong>Changyong Lee</strong>, pendiri solo di Ansan, Korea Selatan.",
        "why_l": "Mengapa saya membuat FITME:",
        "why": "Ukuran S/M/L tidak mencerminkan proporsi tubuh. Setelah mempelajari <a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a> dan <a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559</a>, saya membuat alat ini.",
        "started_l": "Mulai proyek:",
        "started": "Maret 2026",
        "contact_l": "Kontak:",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">Halaman kontak</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "Analisis",
        "nav_blog": "Blog",
        "nav_about": "Tentang",
        "nav_contact": "Kontak",
        "nav_privacy": "Privasi",
        "footer_privacy": "Privasi",
        "footer_terms": "Ketentuan",
        "footer_contact": "Kontak",
        "footer_about": "Tentang",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "Tinggi, berat, pinggang — hanya di browser",
        "cta": "Analisis proporsi gratis →",
    },
    "vi": {
        "title": "Giới thiệu FITME — Nhà sáng lập",
        "desc": "FITME do Changyong Lee, nhà sáng lập độc lập tại Ansan, Hàn Quốc, vận hành.",
        "h1": "Giới thiệu FITME",
        "p1": "FITME do <strong>Changyong Lee</strong> tự xây dựng và vận hành, nhà sáng lập tại Ansan, Hàn Quốc.",
        "why_l": "Vì sao tôi tạo FITME:",
        "why": "Size S/M/L không phản ánh tỷ lệ cơ thể. Sau khi nghiên cứu <a href=\"{k}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">Kibbe Body Types</a> và <a href=\"{i}\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--accent);\">ISO 8559</a>, tôi làm công cụ này.",
        "started_l": "Bắt đầu dự án:",
        "started": "tháng 3 năm 2026",
        "contact_l": "Liên hệ:",
        "contact": "<a href=\"/{loc}/contact\" style=\"color:var(--accent);\">Trang liên hệ</a> · <a href=\"mailto:lcy861013@gmail.com\" style=\"color:var(--accent);\">lcy861013@gmail.com</a>",
        "nav_analysis": "Phân tích",
        "nav_blog": "Blog",
        "nav_about": "Giới thiệu",
        "nav_contact": "Liên hệ",
        "nav_privacy": "Quyền riêng tư",
        "footer_privacy": "Quyền riêng tư",
        "footer_terms": "Điều khoản",
        "footer_contact": "Liên hệ",
        "footer_about": "Giới thiệu",
        "footer_copy": "© 2026 FITME",
        "cta_sub": "Chiều cao, cân nặng, eo — chỉ trên trình duyệt",
        "cta": "Phân tích tỷ lệ miễn phí →",
    },
}


def robots_meta(loc: str) -> str:
    if loc in INDEXABLE_TRUST_LOCALES:
        return ""
    return '  <meta name="robots" content="noindex, follow">\n'


def hreflang_block() -> str:
    lines = [
        f'<link rel="alternate" hreflang="en" href="{SITE}/about">',
        f'<link rel="alternate" hreflang="ja" href="{SITE}/ja/about">',
        f'<link rel="alternate" hreflang="pt-BR" href="{SITE}/pt/about">',
        f'<link rel="alternate" hreflang="x-default" href="{SITE}/about">',
    ]
    return "\n".join(lines)


def main_body(loc: str, d: dict[str, str]) -> str:
    why = d["why"].format(k=KIBBE, i=ISO)
    contact = d["contact"].format(loc=loc)
    return f"""  <h1>{d['h1']}</h1>
  <p>{d['p1']}</p>
  <p><strong>{d['why_l']}</strong> {why}</p>
  <p><strong>{d['started_l']}</strong> {d['started']}</p>
  <p><strong>{d['contact_l']}</strong> {contact}</p>
"""


def locale_about_html(loc: str) -> str:
    d = LOCALES[loc]
    html_lang, extra = META[loc]
    canon = f"{SITE}/{loc}/about"
    body = main_body(loc, d)
    return f"""<!DOCTYPE html>
<html lang="{html_lang}"{extra}>
<head>
  <script src="/consent-init.js?v=7"></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-JW0DB4GXG3"></script>
  <script>gtag('js', new Date()); gtag('config', 'G-JW0DB4GXG3');</script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
{robots_meta(loc)}  <title>{d['title']}</title>
  <meta name="description" content="{d['desc']}">
  <meta property="og:title" content="{d['title']}">
  <meta property="og:description" content="{d['desc']}">
  <meta property="og:image" content="{SITE}/assets/og-image-en.png">
  <meta property="og:url" content="{canon}">
  <link rel="canonical" href="{canon}">
{hreflang_block()}
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
    <a href="/#analysis">{d['nav_analysis']}</a>
    <a href="/blog/">{d['nav_blog']}</a>
    <a href="/{loc}/about" style="color:var(--accent);">{d['nav_about']}</a>
    <a href="/{loc}/contact">{d['nav_contact']}</a>
    <a href="/privacy.html">{d['nav_privacy']}</a>
  </nav>
</header>
<main>
{body}
  <motion class="cta">
    <div style="font-weight:700;font-size:18px;margin-bottom:8px;">{d['cta_sub']}</div>
    <a href="/?utm_source=about&utm_medium=cta&utm_campaign=analysis#analysis" class="cta-btn">{d['cta']}</a>
  </div>
</main>
<footer><p>{d['footer_copy']} · <a href="/privacy.html">{d['footer_privacy']}</a> · <a href="/terms.html">{d['footer_terms']}</a> · <a href="/{loc}/contact">{d['footer_contact']}</a> · <a href="/{loc}/about">{d['footer_about']}</a></p></footer>
<script defer src="/cookie-consent.js?v=7"></script>
</body>
</html>
""".replace("<motion class=\"cta\">", '<motion class="cta">').replace(
        '<motion class="cta">', '<div class="cta">', 1
    )


def patch_root_about() -> None:
    p = ROOT / "about.html"
    text = p.read_text(encoding="utf-8")
    # Remove Korean section
    text = re.sub(
        r"\s*<hr class=\"divider\"[^>]*>.*?</section>\s*",
        "\n",
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(r'\s*<section lang="ko">.*?</section>\s*', "\n", text, flags=re.S)
    text = re.sub(r'\s*<section lang="en">\s*', "\n", text)
    text = re.sub(r"\s*</section>\s*(?=<div class=\"cta\")", "\n", text, count=1)
    # Replace hreflang block
    text = re.sub(
        r"\n*<link rel=\"alternate\" hreflang=\"[^\"]+\"[^>]*>\s*",
        "\n",
        text,
    )
    m = re.search(r"(<link rel=\"canonical\"[^>]*>\s*)", text, re.I)
    if m:
        text = text[: m.end()] + "\n" + hreflang_block() + "\n" + text[m.end() :]
    # schema inLanguage
    text = re.sub(
        r'"inLanguage": \[[^\]]+\]',
        '"inLanguage": ["ko","en","ja","pt","es","zh","fr","de","it","ru","ar","hi","th","id","vi"]',
        text,
    )
    p.write_text(text, encoding="utf-8")
    print("patched root about.html")


def regen_index_files() -> None:
    for loc in LANGS:
        about = ROOT / loc / "about.html"
        if not about.exists():
            continue
        text = about.read_text(encoding="utf-8")
        canon = f"{SITE}/{loc}/about"
        text = re.sub(
            r'<link rel="canonical" href="[^"]+"',
            f'<link rel="canonical" href="{canon}"',
            text,
            count=1,
        )
        text = re.sub(
            r'<meta property="og:url" content="[^"]+"',
            f'<meta property="og:url" content="{canon}"',
            text,
            count=1,
        )
        (ROOT / loc / "index.html").write_text(text, encoding="utf-8")
        print("wrote", loc, "index.html")


def main() -> None:
    for loc in LANGS:
        (ROOT / loc).mkdir(exist_ok=True)
        html = locale_about_html(loc)
        if "<motion" in html:
            html = html.replace("<motion class=\"cta\">", '<motion class="cta">')
            html = html.replace('<motion class="cta">', '<motion class="cta">', 1)
        html = html.replace("<motion class=\"cta\">", '<div class="cta">', 1)
        html = html.replace("</motion>", "</div>") if "</motion>" in html else html
        # fix botched cta div
        html = html.replace(
            '  <motion class="cta">',
            '  <div class="cta">',
        )
        out = ROOT / loc / "about.html"
        out.write_text(html, encoding="utf-8")
        print("wrote", out.relative_to(ROOT))
    patch_root_about()
    regen_index_files()


if __name__ == "__main__":
    main()
