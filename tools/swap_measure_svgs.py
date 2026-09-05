# -*- coding: utf-8 -*-
"""Point blog20–24 hero images at measurement SVGs (keep OG/schema on JPG)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"

MAP = {
    "blog20": ("/blog/img/en/blog20-span-thumb-en.jpg", "/blog/img/blog20-span-method.svg"),
    "blog21": ("/blog/img/en/blog21-shoulder-thumb-en.jpg", "/blog/img/blog21-shoulder-measurement.svg"),
    "blog22": ("/blog/img/en/blog22-arm-thumb-en.jpg", "/blog/img/blog22-arm-measurement.svg"),
    "blog23": ("/blog/img/en/blog23-leg-thumb-en.jpg", "/blog/img/blog23-leg-measurement.svg"),
    "blog24": ("/blog/img/en/blog24-hip-thumb-en.jpg", "/blog/img/blog24-hip-measurement.svg"),
}

ALTS = {
    "blog20": {
        "ko": "손뼘 측정 — 엄지 끝에서 새끼손가락 끝까지를 기준 길이로 쓰는 도해",
        "en": "Hand span diagram — measure thumb tip to little-finger tip as your personal unit",
    },
    "blog21": {
        "ko": "어깨 너비 측정 도해 — 좌우 견봉(어깨 끝뼈) 사이 직선",
        "en": "Shoulder width diagram — straight line between left and right acromion",
    },
    "blog22": {
        "ko": "팔 길이 측정 도해 — 상완(어깨~팔꿈치)과 하완(팔꿈치~손목)",
        "en": "Arm length diagram — upper arm (shoulder to elbow) and forearm (elbow to wrist)",
    },
    "blog23": {
        "ko": "다리 길이 측정 도해 — 대전자(엉덩이뼈 돌기)에서 발목까지",
        "en": "Leg length diagram — greater trochanter (hip bone bump) down to the ankle",
    },
    "blog24": {
        "ko": "엉덩이 둘레 측정 도해 — 가장 두꺼운 지점을 한 바퀴",
        "en": "Hip circumference diagram — full loop at the fullest seat point",
    },
}

IMG = re.compile(
    r'(<img\s+src=")(/blog/img/en/blog2[0-4]-[^"]+\.jpg)(\?v=\d+")(\s+alt=")([^"]*)("\s+class="guide-img">)',
    re.I,
)

changed = 0
for slug, (old, new) in MAP.items():
    for suffix, lang in ((".html", "ko"), ("-en.html", "en")):
        path = BLOG / f"{slug}{suffix}"
        if not path.exists():
            print(f"  MISS {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        alt = ALTS[slug][lang]

        def repl(m: re.Match) -> str:
            if old not in m.group(2):
                return m.group(0)
            return f'{m.group(1)}{new}?v=2" alt="{alt}" class="guide-img" width="800" height="480">'

        # Simpler: replace the guide-img line only
        pattern = re.compile(
            rf'<img src="{re.escape(old)}\?v=\d+" alt="[^"]*" class="guide-img">'
        )
        new_tag = f'<img src="{new}?v=2" alt="{alt}" class="guide-img" width="800" height="480">'
        if not pattern.search(text):
            # try without query
            pattern = re.compile(
                rf'<img src="{re.escape(old)}" alt="[^"]*" class="guide-img">'
            )
        if pattern.search(text):
            text = pattern.sub(new_tag, text, count=1)
            path.write_text(text, encoding="utf-8")
            changed += 1
            print(f"  swapped {path.name} → {new}")
        else:
            print(f"  WARN  no guide-img match in {path.name}")

print(f"\n{changed} pages updated (OG images left as JPG for social cards)")
