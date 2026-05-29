#!/usr/bin/env python3
"""
CTR-focused title + meta refresh for high-impression / low-click URLs.

Targets US/EU search intent: online fit anxiety, no-tape measuring, body ratios.
Updates <title>, meta description, og/twitter, and Article JSON-LD where present.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRAND = " | FITME"


def lim(s: str, n: int) -> str:
    return s if len(s) <= n else s[: n - 1].rstrip(",. -—") + "…"


def full_title(lead: str) -> str:
    lead = lim(lead, 60 - len(BRAND))
    return lead + BRAND


def patch_html(path: Path, lead: str, desc: str, *, json_ld: bool = True) -> bool:
    title = full_title(lead)
    desc = lim(desc, 158)
    raw = path.read_text(encoding="utf-8")
    new = raw

    new = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", new, count=1)
    new = re.sub(
        r'(<meta\s+name="description"\s+content=")[^"]*(")',
        lambda m: m.group(1) + desc + m.group(2),
        new,
        count=1,
    )
    new = re.sub(
        r'(<meta\s+property="og:title"\s+content=")[^"]*(")',
        lambda m: m.group(1) + title + m.group(2),
        new,
        count=1,
    )
    new = re.sub(
        r'(<meta\s+property="og:description"\s+content=")[^"]*(")',
        lambda m: m.group(1) + desc + m.group(2),
        new,
        count=1,
    )
    if 'name="twitter:title"' in new:
        new = re.sub(
            r'(<meta\s+name="twitter:title"\s+content=")[^"]*(")',
            lambda m: m.group(1) + title + m.group(2),
            new,
            count=1,
        )
    if 'name="twitter:description"' in new:
        new = re.sub(
            r'(<meta\s+name="twitter:description"\s+content=")[^"]*(")',
            lambda m: m.group(1) + desc + m.group(2),
            new,
            count=1,
        )

    if json_ld and '"@type":"Article"' in new or '"@type": "Article"' in new:
        new = re.sub(
            r'("headline":\s*)"[^"]*"',
            lambda m: m.group(1) + json.dumps(title, ensure_ascii=False),
            new,
            count=1,
        )
        new = re.sub(
            r'("description":\s*)"[^"]*"',
            lambda m: m.group(1) + json.dumps(desc, ensure_ascii=False),
            new,
            count=1,
        )
        new = re.sub(
            r'("position":\s*3,\s*"name":\s*)"[^"]*"',
            lambda m: m.group(1) + json.dumps(lead, ensure_ascii=False),
            new,
            count=1,
        )

    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


# path relative to ROOT -> (title lead without brand, description)
CTR: dict[str, tuple[str, str]] = {
    "index.html": (
        "Online Wrong Size? Free Body Proportion Tool",
        "Same S/M/L but different fit online? Map shoulder, waist & leg ratios in minutes. No photos, no signup — free analysis for smarter shopping.",
    ),
    "blog/index.html": (
        "Body Fit Guides: Pants, WHR & Hand-Span Measuring",
        "Guides for online shoppers: pants fit, no-tape body measuring, pear-shape outfits & more. Original English articles + free proportion tool.",
    ),
    "blog/blog1-en.html": (
        "Pants Fit: Slim vs Straight vs Wide (Your Body)",
        "Same waist tag, different leg line — which cut actually suits you? Slim, straight, wide & tapered compared + free 60-sec body map.",
    ),
    "blog/blog2-en.html": (
        "Wide Feet? 12 Shoe Brands That Actually Fit",
        "Shoes tight on the sides? 12 wide-width brands (men + women), width chart, and how to measure foot width at home before you buy.",
    ),
    "blog/blog8-en.html": (
        "WHR Guide: Fix Pants That Gape at the Waist",
        "Hips fit but waist gaps? Waist-to-hip ratio explains it. Measure WHR in 30 seconds + styling fixes for jeans and dresses.",
    ),
    "blog/blog11-en.html": (
        "Why Clothes Never Fit (It's Not Your Body)",
        "Size letters ignore your proportions. Brand chaos, vanity sizing, and 4 fixes that work — including a free 60-second ratio check.",
    ),
    "blog/blog18-en.html": (
        "Pear Body Shape: What to Wear (Jeans & Tops)",
        "Balance wider hips without hiding them: best necklines, denim rises, jackets & dresses. Outfit formulas + free proportion analysis.",
    ),
    "blog/blog20-en.html": (
        "No Tape? Measure Your Body with Hand Spans",
        "No ruler at home? Calibrate one hand span, then estimate shoulder, waist, hip & legs. Step-by-step guide + free FITME tool.",
    ),
    "blog/blog21-en.html": (
        "Measure Shoulder Width Alone — No Tape",
        "Find your acromion, count hand spans, compare to jacket charts. Self-measurement in 2 steps — no helper needed.",
    ),
    "blog/blog22-en.html": (
        "Measure Arm Length at Home (Sleeve Fit)",
        "Sleeves too short online? Upper arm, forearm & total sleeve length with hand spans. Sizing for jackets and shirts.",
    ),
    "blog/blog23-en.html": (
        "Measure Leg Length for Inseam — No Tape",
        "Wrong inseam again? Greater-trochanter to ankle with hand spans + how to use the number on size charts.",
    ),
    "blog/blog24-en.html": (
        "Measure Hip Size Alone — Hand-Span Method",
        "Jeans size from hip circumference: landmarks, posture & two-span method without a mirror struggle.",
    ),
    "blog/blog12-en.html": (
        "Find Your Real Body Type (4 Measurements)",
        "Hourglass labels miss your ratios. Four measurements + free FITME DNA score — know what to wear in 60 seconds.",
    ),
    # KO — GSC/GA에서 노출·유입 있는 글
    "blog/blog1.html": (
        "내 체형 팬츠 핏 — 슬림·와이드·테이퍼드 고르는 법",
        "같은 사이즈인데 핏이 다른 이유. 체형·신발 기준으로 슬림/스트레이트/와이드/테이퍼드 비교 + 무료 비율 분석.",
    ),
    "blog/blog20.html": (
        "줄자 없이 몸 재기 — 손 한 뼘으로 어깨·허리·다리",
        "줄자 없어도 OK. 한 뼘만 재두면 어깨·허리·다리 길이 계산. 단계별 사진 + 무료 체형 비율 분석.",
    ),
    "blog/blog8.html": (
        "허리·엉덩이 비율(WHR) — 바지 허리 뜸 해결법",
        "엉덩이는 맞는데 허리만 뜨는 이유. WHR 재는 법 30초 + 체형에 맞는 코디 팁.",
    ),
    "blog/blog18.html": (
        "하체 넓은 체형 코디 — 상의·바지 골라보기",
        "골반 넓어도 가릴 필요 없음. 넥라인·데님 핏·아우터 조합 + 무료 비율 분석.",
    ),
}


def main() -> None:
    done = []
    for rel, (lead, desc) in CTR.items():
        path = ROOT / rel
        if not path.exists():
            print("MISSING", rel)
            continue
        json_ld = "blog/" in rel and rel.endswith(".html")
        if patch_html(path, lead, desc, json_ld=json_ld):
            done.append(rel)
    print(f"CTR refresh: {len(done)} files")
    for r in done:
        print(" ", r)


if __name__ == "__main__":
    main()
