#!/usr/bin/env python3
from pathlib import Path
import re

p = Path(__file__).resolve().parents[1] / "assets" / "fitme-app.js"
t = p.read_text(encoding="utf-8")

# Soften "15 languages" publisher claim → analyzer UI languages
replacements = {
    "🌍 15개국 언어": "🌐 분석기 UI 다국어",
    "🌍 15 Languages": "🌐 Analyzer UI languages",
    "🌍 15言語対応": "🌐 分析UI多言語",
    "🌍 15种语言": "🌐 分析UI多语言",
    "🌍 15 langues": "🌐 Langues de l’UI",
    "🌍 15 idiomas": "🌐 Idiomas de la UI",
    "🌍 15 Sprachen": "🌐 UI-Sprachen",
    "🌍 15 lingue": "🌐 Lingue UI",
    "🌍 15 языков": "🌐 Языки UI",
    "🌍 15 لغة": "🌐 لغات الواجهة",
    "🌍 15 भाषाएं": "🌐 UI भाषाएँ",
    "🌍 15 ภาษา": "🌐 ภาษา UI",
    "🌍 15 Bahasa": "🌐 Bahasa UI",
    "🌍 15 ngôn ngữ": "🌐 Ngôn ngữ UI",
}

n = 0
for old, new in replacements.items():
    c = t.count(old)
    if c:
        t = t.replace(old, new)
        n += c

# PT uses same "15 idiomas" as ES — already handled by replace_all once
p.write_text(t, encoding="utf-8")
left = re.findall(r"'hero-badge3':'([^']*15[^']*)'", t)
print(f"replaced={n} left_with_15={left}")
