# -*- coding: utf-8 -*-
"""Align title/meta/H1/lead to GSC impression queries (no keyword stuffing)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        print(f"  MISS {label}: {old[:60]!r}")
        return text
    return text.replace(old, new, 1)


def set_meta_bundle(text: str, *, title: str, desc: str, h1_html: str | None = None) -> str:
    """Replace title, description, og/twitter titles & descriptions, and optional H1."""
    text = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", text, count=1, flags=re.S)
    text = re.sub(
        r'(<meta name="description" content=")[^"]*(")',
        rf"\1{desc}\2",
        text,
        count=1,
    )
    text = re.sub(
        r'(<meta property="og:title" content=")[^"]*(")',
        rf'\1{title.replace(" | FITME", "") if title.endswith(" | FITME") else title}\2'
        if False
        else rf"\1{title}\2",
        text,
        count=1,
    )
    # Keep og:title same as <title>
    text = re.sub(
        r'(property="og:title" content=")[^"]*(")',
        rf"\1{title}\2",
        text,
        count=1,
    )
    text = re.sub(
        r'(property="og:description" content=")[^"]*(")',
        rf"\1{desc}\2",
        text,
        count=1,
    )
    if 'name="twitter:title"' in text:
        text = re.sub(
            r'(name="twitter:title" content=")[^"]*(")',
            rf"\1{title}\2",
            text,
            count=1,
        )
    if 'name="twitter:description"' in text:
        text = re.sub(
            r'(name="twitter:description" content=")[^"]*(")',
            rf"\1{desc}\2",
            text,
            count=1,
        )
    # JSON-LD headline / description (first Article-ish occurrence)
    text = re.sub(
        r'("headline"\s*:\s*")[^"]*(")',
        rf'\1{title.replace(" | FITME", "")}\2',
        text,
        count=1,
    )
    text = re.sub(
        r'("description"\s*:\s*")[^"]*(")',
        rf"\1{desc}\2",
        text,
        count=1,
    )
    if h1_html is not None:
        text = re.sub(r"<h1\b[^>]*>.*?</h1>", h1_html, text, count=1, flags=re.S)
    return text


# ---- blog29 KO: 바지 밑위 뜻 / 남자 밑위 짧은 바지 ----
p = ROOT / "blog/blog29.html"
t = p.read_text(encoding="utf-8")
t = set_meta_bundle(
    t,
    title="바지 밑위 뜻 · 남자 밑위 짧은 바지 — 허벅지 실측으로 고르는 법 | FITME",
    desc="바지 밑위 뜻(허리밴드~가랑이)과 남자 밑위 짧은 바지 신호. 허리는 맞는데 앉을 때·허벅지만 실패할 때 볼 실측 체크리스트.",
    h1_html="<h1>바지 밑위 뜻 · 남자 밑위 짧은 바지<br>— 허벅지·앉을 때부터 보세요</h1>",
)
t = replace_once(
    t,
    '<p class="lead-answer"><strong>허리는 맞는데 허벅지가 끼거나, 서 있을 땐 괜찮은데 앉으면 당긴다면 — 사이즈 라벨 문제가 아니라 <em>허벅지·밑위·엉덩이</em> 실측 문제인 경우가 많습니다.</strong> “한 치수 업”만 하면 허리가 뜨고, 슬림만 고집하면 허벅지에서 또 실패해요. 이 글은 다이어트 조언이 아니라 <strong>지금 치수로 바지 고르는 쇼핑 메모</strong>입니다.</p>',
    '<p class="lead-answer"><strong>바지 밑위 뜻은 허리밴드에서 가랑이까지의 길이입니다.</strong> 남자 밑위 짧은 바지는 서 있을 땐 괜찮은데 앉으면 당기는 게 대표 신호예요. 허리는 맞는데 허벅지가 끼거나 앉을 때만 실패한다면 — 라벨이 아니라 <em>허벅지·밑위·엉덩이</em> 실측을 보세요. 다이어트 조언이 아니라 <strong>지금 치수로 고르는 쇼핑 메모</strong>입니다.</p>',
    "blog29 lead",
)
# FAQ: rename first question-ish — add explicit 밑위 뜻 FAQ at top of faq-block
if "<h3>바지 밑위 뜻은?</h3>" not in t:
    t = replace_once(
        t,
        '  <div class="faq-block">\n    <h3>허리는 맞는데 허벅지만 끼면 사이즈를 올려야 하나요?</h3>',
        '  <div class="faq-block">\n    <h3>바지 밑위 뜻은?</h3>\n    <p>허리밴드(또는 바지 윗단)에서 가랑이까지의 길이입니다. 실측표에 ‘밑위·앞밑위·총밑위’로 적히는 그 숫자예요. 짧으면 앉을 때 가랑이가 당기는 경우가 많습니다.</p>\n    <h3>허리는 맞는데 허벅지만 끼면 사이즈를 올려야 하나요?</h3>',
        "blog29 FAQ 밑위 뜻",
    )
p.write_text(t, encoding="utf-8")
print("updated blog29.html")

# ---- blog30 KO: already strong; sharpen desc ----
p = ROOT / "blog/blog30.html"
t = p.read_text(encoding="utf-8")
t = set_meta_bundle(
    t,
    title="와이드 팬츠 기장 고르는 법 — 인심·신발 높이 체크리스트 | FITME",
    desc="와이드 팬츠 기장이 짧아 보이거나 끌릴 때. 인심·밑단 폭·신발 높이로 비교하는 법. 172·175 기준 포함.",
    h1_html="<h1>와이드 팬츠 기장 고르는 법<br>— 인심·신발 높이부터</h1>",
)
p.write_text(t, encoding="utf-8")
print("updated blog30.html")

# ---- blog20 KO: 손 한뼘 길이 / 한뼘 기준 ----
p = ROOT / "blog/blog20.html"
t = p.read_text(encoding="utf-8")
t = set_meta_bundle(
    t,
    title="손 한뼘 길이·한뼘 기준 — 줄자 없이 몸 재는 법 | FITME",
    desc="손 한뼘 길이(엄지~새끼)를 한 번만 재두면 어깨·허리·다리 추정 가능. 한뼘 기준 오차와 온라인 실측 비교법.",
    h1_html="<h1>손 한뼘 길이·한뼘 기준<br>— 줄자 없이 몸 재는 법</h1>",
)
# fix misleading "사진" claim in any remaining desc - already replaced
# lead if present
old_lead = None
m = re.search(r'<p class="lead-answer">.*?</p>', t, re.S)
if m:
    t = t.replace(
        m.group(0),
        '<p class="lead-answer"><strong>손 한뼘 길이(엄지 끝~새끼손가락 끝)를 자로 한 번만 재두면, 그 길이가 한뼘 기준이 됩니다.</strong> 줄자가 없을 때 어깨·허리·다리 대략치를 메모하고, 중요한 주문 전에만 줄자로 교정하세요. 오차가 있는 방법이라 경계값이면 줄자로 확인하는 게 맞습니다.</p>',
        1,
    )
p.write_text(t, encoding="utf-8")
print("updated blog20.html")

# ---- blog20 EN ----
p = ROOT / "blog/blog20-en.html"
t = p.read_text(encoding="utf-8")
t = set_meta_bundle(
    t,
    title="Hand Span Length Method — Measure Body Without a Tape | FITME",
    desc="Calibrate thumb-to-pinky hand span length once. Use that span as your baseline to estimate shoulders, waist, and legs for online charts.",
    h1_html="<h1>Hand Span Length Method<br>— Measure Your Body Without a Tape</h1>",
)
m = re.search(r'<p class="lead-answer">.*?</p>', t, re.S)
if m:
    t = t.replace(
        m.group(0),
        '<p class="lead-answer"><strong>Hand span length (thumb tip to little-finger tip) becomes your personal ruler after one calibration.</strong> Use it to draft shoulder, waist, and leg notes when you have no tape — then verify with a real tape before an order that matters.</p>',
        1,
    )
p.write_text(t, encoding="utf-8")
print("updated blog20-en.html")

# ---- blog14-en: body symmetry ----
p = ROOT / "blog/blog14-en.html"
t = p.read_text(encoding="utf-8")
t = set_meta_bundle(
    t,
    title="Body Symmetry Explained — What It Means for Style | FITME",
    desc="Body symmetry and a symmetry body look: what research actually says, and how posture, shoulder seams, and vertical lines fix the impression in clothing.",
    h1_html="<h1>Body Symmetry Explained<br>— What It Means for Style</h1>",
)
m = re.search(r'<p class="lead-answer">.*?</p>', t, re.S)
if m:
    t = t.replace(
        m.group(0),
        '<p class="lead-answer"><strong>Body symmetry is left–right balance of the silhouette — not a demand for perfect twins.</strong> A “symmetry body” look in outfits usually comes from posture, shoulder seams that sit on the bone, and unbroken vertical lines. Clothing can correct the impression faster than chasing perfect measurements.</p>',
        1,
    )
p.write_text(t, encoding="utf-8")
print("updated blog14-en.html")

# ---- blog14 KO ----
p = ROOT / "blog/blog14.html"
t = p.read_text(encoding="utf-8")
t = set_meta_bundle(
    t,
    title="체형 대칭 · 바디 심메트리 — 옷으로 균형 잡는 법 | FITME",
    desc="체형 대칭(바디 심메트리)이 옷태에 미치는 영향. 완벽한 좌우보다 어깨·자세·세로 라인으로 균형 잡아 보이게 하는 실전 노트.",
    h1_html="<h1>체형 대칭 · 바디 심메트리<br>— 옷으로 균형 잡는 법</h1>",
)
p.write_text(t, encoding="utf-8")
print("updated blog14.html")

# ---- blog2 KO: 신발 발볼 ----
p = ROOT / "blog/blog2.html"
t = p.read_text(encoding="utf-8")
t = set_meta_bundle(
    t,
    title="신발 발볼 넓은 분 가이드 — Wide 사이즈·재는 법 12곳 | FITME",
    desc="신발 발볼이 넓어 앞이 눌릴 때. 발볼 재는 법과 뉴발란스·아식스·Hoka 등 Wide(E/2E) 브랜드 12곳.",
    h1_html="<h1>신발 발볼 넓은 분 가이드<br>— Wide 사이즈·재는 법</h1>",
)
m = re.search(r'<p class="lead-answer"[^>]*>.*?</p>', t, re.S)
if m:
    t = t.replace(
        m.group(0),
        '<p class="lead-answer" style="font-size:16px;line-height:1.85;margin-bottom:28px;padding:16px 18px;background:rgba(212,168,75,0.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;"><strong>신발 발볼이 넓으면 길이(mm)만 맞춰도 앞이 눌립니다.</strong> 같은 250이라도 라스트·너비(D/2E)에 따라 달라요. 발볼을 재고 Wide 표기가 있는 브랜드부터 보는 게 반품을 줄입니다.</p>',
        1,
    )
p.write_text(t, encoding="utf-8")
print("updated blog2.html")

# ---- blog27 KO: 실측 뜻 ----
p = ROOT / "blog/blog27.html"
t = p.read_text(encoding="utf-8")
t = set_meta_bundle(
    t,
    title="실측 뜻 · 무신사 실측표 읽는 법 — 반품 줄이는 체크리스트 | FITME",
    desc="실측 뜻은 옷·몸을 cm로 잰 숫자입니다. 무신사 실측표에서 어깨·가슴·총장·밑위를 내 치수와 비교하는 법(단면 vs 둘레 포함).",
    h1_html="<h1>실측 뜻 · 무신사 실측표 읽는 법<br>— 반품 줄이는 체크리스트</h1>",
)
m = re.search(r'<p class="lead-answer">.*?</p>', t, re.S)
if m:
    t = t.replace(
        m.group(0),
        '<p class="lead-answer"><strong>실측 뜻은 ‘옷을 펼쳐 잰 cm’ 또는 ‘내 몸을 잰 cm’입니다.</strong> 무신사에서 사이즈를 고를 때 제일 먼저 볼 곳은 ‘추천 사이즈’가 아니라 <em>실측표</em>예요. L/XL·키·몸무게 표는 참고만 하고, <strong>어깨·가슴(단면)·총장</strong>(바지는 <strong>허리·엉덩이·밑위·인심</strong>)을 내 메모와 ±1~2cm로 비교하세요.</p>',
        1,
    )
# FAQ add 실측 뜻 if missing
if "<h3>실측 뜻은 뭔가요?</h3>" not in t and '실측 뜻은' not in t.split("faq-block")[1] if "faq-block" in t else True:
    if 'class="faq-block"' in t and "<h3>실측 뜻은 뭔가요?</h3>" not in t:
        t = replace_once(
            t,
            '  <div class="faq-block">\n    <h3>',
            '  <div class="faq-block">\n    <h3>실측 뜻은 뭔가요?</h3>\n    <p>옷을 바닥에 펼쳐 잰 길이(또는 내 몸을 줄자로 잰 길이)를 cm로 적은 값입니다. 추천 사이즈·키몸무게 표와 다릅니다.</p>\n    <h3>',
            "blog27 FAQ 실측 뜻",
        )
p.write_text(t, encoding="utf-8")
print("updated blog27.html")

# ---- blog3-en: golden ratio in fashion ----
p = ROOT / "blog/blog3-en.html"
t = p.read_text(encoding="utf-8")
t = set_meta_bundle(
    t,
    title="Golden Ratio in Fashion — Dress for Your Proportions | FITME",
    desc="What the golden ratio in fashion actually means for outfits. Use shoulder–waist balance and vertical lines — not a literal 1.618 body.",
    h1_html="<h1>Golden Ratio in Fashion<br>— Dress for Your Proportions</h1>",
)
m = re.search(r'<p class="lead-answer">.*?</p>', t, re.S)
if m:
    t = t.replace(
        m.group(0),
        '<p class="lead-answer"><strong>The golden ratio in fashion is a styling idea about proportional balance — not a rule that your body must equal 1.618.</strong> In practice it means placing visual weight: high-rise and continuous vertical lines lengthen the leg; shoulder emphasis or lower-body volume balances an inverted triangle.</p>',
        1,
    )
p.write_text(t, encoding="utf-8")
print("updated blog3-en.html")

# ---- blog3 KO ----
p = ROOT / "blog/blog3.html"
t = p.read_text(encoding="utf-8")
t = set_meta_bundle(
    t,
    title="패션 황금비율 — 체형별 시각 보정 코디 | FITME",
    desc="패션에서 황금비율이란 무엇인지, 역삼각형·삼각형·직사각형 체형별 시각 보정 원리와 코디 전략.",
    h1_html="<h1>패션 황금비율<br>— 체형별 시각 보정 코디</h1>",
)
p.write_text(t, encoding="utf-8")
print("updated blog3.html")

print("\ndone HTML posts")
