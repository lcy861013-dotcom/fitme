#!/usr/bin/env python3
"""Align founder-voice copy: 175cm, 78kg, tops 2XL, waist 32, foot 250mm."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Order matters: longer / more specific patterns first.
REPLACEMENTS_KO = [
    ("175·78·허리 32만 보고 주문하던 시절, 반품", "2XL·허리 32만 보고 주문하던 시절, 반품"),
    ("175·78·허리 32만 보고 주문", "2XL·허리 32만 보고 주문"),
    ("175·78·허리 32", "2XL·허리 32"),
    ("“175·78kg·허리 32”", "“175·78kg · 2XL · 허리 32”"),
    ("175·78kg·허리 32만", "175·78kg · 2XL · 허리 32만"),
    (
        "175·78kg·허리 32면 바지는 맞겠지, 상의는 어깨에서",
        "2XL·허리 32만 맞춰도 어깨·기장·비율에서",
    ),
    ("175·78kg인데 상의는 라벨 L~XL만 보고", "175·78kg · 상의 2XL(오버핏)인데 라벨·“오버핏”만 보고"),
    ("175·78kg인데 라벨만 보고", "175·78kg · 2XL 오버핏인데 라벨만 보고"),
    ("라벨 L~XL만", "2XL 오버핏만"),
    ("L~XL", "2XL"),
    ("유행 공식(오verfit L + 슬림 32)", "유행 공식(오버핏 2XL + 슬림 32)"),
    ("넉넉한 상의 + 슬림", "오버핏 2XL + 슬림"),
    ("M·L·XL을", "XL·2XL을"),
    ("“175·78kg·허리 32”만 보다가", "“175·78kg · 2XL · 허리 32”만 보다가"),
    (
        "175·78kg·허리 32면 바지는 맞겠지, 상의는 어깨에서 하다 보니",
        "2XL·허리 32만 맞춰도 어깨·기장에서 어긋나다 보니",
    ),
    ("175·78kg·허리 32 맞는 바지인데", "175·78kg · 2XL · 허리 32 맞는 바지인데"),
    ("175·78kg인데 친구랑", "175·78kg · 2XL 입는데 친구랑"),
]

REPLACEMENTS_EN = [
    ("waist 32 online online", "tops 2XL, waist 32"),
    ("175 cm, 78 kg — kept ordering waist 32", "175 cm, 78 kg — 2XL oversize tops, waist 32 pants"),
    ("175 cm, 78 kg — waist 32 online", "175 cm, 78 kg — 2XL tops, waist 32"),
    ("175 cm, 78 kg — labels “should work”", "175 cm, 78 kg — 2XL oversize, labels “should work”"),
    ("bought by label (L~XL)", "wear 2XL for oversize but bought by label"),
    ("L~XL", "2XL"),
    ("Roomy top + slim", "oversize 2XL top + slim"),
]

STORY_P3_KO = (
    "저는 매장보다 온라인 쇼핑을 훨씬 많이 해요. "
    "키 175·78kg · 상의 2XL(오버핏) · 허리 32 · 발 250mm — "
    "요즘 유행도 그렇고 배 편하려고 2XL 많이 입어요. "
    "그런데 사이즈표만 보면 “거의 맞겠지” 싶었거든요 — "
    "사진·리뷰 보고 집에서 입어 보면 “거의 맞는데… 나한테는 아닌” 그 느낌이 반복됐어요. "
    "예쁜 옷인데 실루엣이 안 맞는, 그 패턴요."
)

STORY_P3_EN = (
    "I shop online more than in stores — 175 cm, 78 kg, 2XL oversize tops "
    "(trend + belly comfort), waist 32, foot 250 mm — size charts still felt “close enough.” "
    "Photos and reviews looked fine; at home it was “almost… but not on me” again. "
    "Pretty clothes, wrong silhouette."
)

OLD_STORY_KO = (
    "저는 매장보다 온라인 쇼핑을 훨씬 많이 해요. "
    "키 175·78kg·허리 32·발 250mm인데도 사이즈표만 보면 “거의 맞겠지” 싶었거든요 — "
    "사진·리뷰 보고 집에서 입어 보면 “거의 맞는데… 나한테는 아닌” 그 느낌이 반복됐어요. "
    "예쁜 옷인데 실루엣이 안 맞는, 그 패턴요."
)

OLD_STORY_EN = (
    "I shop online more than in stores — 175 cm, 78 kg, waist 32, foot 250 mm — "
    "and size charts still felt “close enough.” Photos and reviews looked fine; "
    "at home it was “almost… but not on me” again. Pretty clothes, wrong silhouette."
)

# Targeted paragraph fixes (exact match).
EXACT_KO = {
    """<strong>체중 숫자만 보고 실패한 적 많아요.</strong> 저울 숫자는 비슷한데 상의·바지 핏이 완전 달라지더라고요. 2XL·허리 32만 맞춰도 어깨·기장·비율에서 — 쇼핑몰에서 그렇게 샀는데 집에서 입으면 어깨는 널널하고 허벅지만 끼거나, 반대로 허리는 맞는데 기장·다리 라인이 어색한 날이 반복됐어요. 친구랑 kg 숫자 비교해 봐도 실루엣은 전혀 달랐고요. 저는 몸무게보다 <em>어깨·허리·다리 비율</em>을 대략이라도 알고 나서 쇼핑 실패가 줄었습니다. (의학 조언이 아니라 제가 FITME 쓰면서 정리한 경험입니다.)""": """<strong>체중 숫자만 보고 실패한 적 많아요.</strong> 저울 숫자는 비슷한데 상의·바지 핏이 완전 달라지더라고요. 175·78kg · 상의 2XL(오버핏) · 허리 32 — 트렌드도 그렇고 배 편하려고 2XL 많이 입어요. 그런데 바지 32는 맞는데 기장·허벅지·비율에서, 상의 2XL도 어깨·기장에서 “거의 맞는데…”가 반복됐어요. 친구랑 kg 숫자 비교해 봐도 실루엣은 전혀 달랐고요. 저는 몸무게보다 <em>어깨·허리·다리 비율</em>을 대략이라도 알고 나서 쇼핑 실패가 줄었습니다. (의학 조언이 아니라 제가 FITME 쓰면서 정리한 경험입니다.)""",
    """<strong>상의는 목·어깨·기장에서 많이 깨졌어요.</strong> 175·78kg · 2XL 오버핏인데 라벨만 보고 쇼핑몰에서 샀는데, 어깨 솔기는 짧고 가슴은 넉넉하거나 반대로 어깨만 처지는 날이 반복됐어요. 유행 따라 사면 포인트는 살아도 어깨가 좁아 보이거나 몸통이 길어 보이더라고요. 나중에 알고 보니 <em>어깨 너비 숫자</em> 하나 아는 게 S/M/L보다 먼저였고, 체형별 상의는 ‘예쁜 옷’보다 <em>내 비율을 보완하는 옷</em> 고르는 쪽에 가깝습니다.""": """<strong>상의는 목·어깨·기장에서 많이 깨졌어요.</strong> 175·78kg · 상의 2XL(오버핏) — 배 편하려고 크게 입는데, 라벨·“오버핏”만 보고 샀더니 어깨 솔기는 짧고 몸통은 넉넉하거나 반대로 어깨만 처지는 날이 반복됐어요. 2XL이라도 브랜드마다 어깨 실측이 달라서요. 나중에 알고 보니 <em>어깨 너비 숫자</em> 하나 아는 게 라벨보다 먼저였고, 체형별 상의는 ‘예쁜 옷’보다 <em>내 비율을 보완하는 옷</em> 고르는 쪽에 가깝습니다.""",
    """  <p>어깨 너비는 혼자 재기 가장 어려운 부위 중 하나입니다. 눈에 보이지 않고, 뒤에서 닿지 않기 때문입니다. 저도 175·78kg · 상의 2XL(오버핏)인데 배 편하려고 크게 입어도, 라벨·“오버핏”만 보고 샀다가 어깨 솔기에서 반복 실패했어요. 손뼘을 이용하면 도우미 없이도 2단계로 정확히 잴 수 있습니다.</p>""": """  <p>어깨 너비는 혼자 재기 가장 어려운 부위 중 하나입니다. 눈에 보이지 않고, 뒤에서 닿지 않기 때문입니다. 저도 175·78kg · 상의 2XL(오버핏)인데 — 트렌드도 그렇고 배 편하려고 2XL 많이 입어요 — 라벨·“오버핏”만 보고 샀다가 어깨 솔기에서 반복 실패했어요. 손뼘을 이용하면 도우미 없이도 2단계로 정확히 잴 수 있습니다.</p>""",
    """<strong>어깨에서 많이 망했어요.</strong> 상의는 2XL 오버핏만 보고 샀는데, 어깨 솔기가 짧으면 팔이 끼기고, 길면 옷이 처져서 어딘가 어색해 보이더라고요. 같은 라벨인데 브랜드마다 어깨 실측이 1~2cm씩 다른 것도 나중에야 알았고요. 그래서 사이즈표보다 <em>내 어깨 너비 숫자</em> 하나 아는 게 먼저라고 생각합니다.""": """<strong>어깨에서 많이 망했어요.</strong> 상의는 2XL 오버핏(배 편하려고)인데도, 라벨·“오버핏”만 보고 샀더니 어깨 솔기가 짧으면 팔이 끼기고, 길면 옷이 처져서 어딘가 어색해 보이더라고요. 같은 2XL인데 브랜드마다 어깨 실측이 1~2cm씩 다른 것도 나중에야 알았고요. 그래서 사이즈표보다 <em>내 어깨 너비 숫자</em> 하나 아는 게 먼저라고 생각합니다.""",
    """<strong>코디 공식만 외우면 또 실패합니다.</strong> 저는 “상의는 이렇게”만 보고 샀다가 하체 비율이랑 안 맞을 때가 많았어요. 오버핏 2XL + 슬림 바지 공식이 유행일 때 따라 샀는데, 허리 32 맞는 바지가 허벅지에서 끼이면 전체가 어색해지더라고요. 강조/보완을 <em>내 숫자</em> 기준으로 고르는 쪽이 덜 헛발질이었습니다.""": """<strong>코디 공식만 외우면 또 실패합니다.</strong> 저는 “상의는 이렇게”만 보고 샀다가 하체 비율이랑 안 맞을 때가 많았어요. 오버핏 2XL + 슬림 32 공식이 유행일 때 따라 샀는데 — 배 편하려고 2XL 입는 편인데 — 허리 32 맞는 바지가 허벅지에서 끼이면 전체가 어색해지더라고요. 강조/보완을 <em>내 숫자</em> 기준으로 고르는 쪽이 덜 헛발질이었습니다.""",
    """  <p data-founder-beat="beat-blog11-online">저는 한때 XL·2XL을 연달아 주문해 비교 반품했어요 — 라벨만 믿으면 “거의 맞는데…”가 반복되더라고요. 지금은 어깨·인심 숫자 메모해 두고 상세페이지 실측과 ±1~2cm만 맞춰 봅니다.</p>""": """  <p data-founder-beat="beat-blog11-online">저는 한때 XL·2XL을 연달아 주문해 비교 반품했어요 — 평소 2XL 오버핏 입는데도 라벨만 믿으면 “거의 맞는데…”가 반복되더라고요. 지금은 어깨·인심 숫자 메모해 두고 상세페이지 실측과 ±1~2cm만 맞춰 봅니다.</p>""",
    """  <p data-founder-beat="beat-blog15-data">온라인에서 사이즈표만 보고 2XL·허리 32만 보고 주문하던 시절, 반품 상자가 쌓였어요. 어깨·허리·인심을 한 번 메모해 두고 상세 실측과 비교하기 시작한 뒤로 “이번에도?” 확률이 줄었습니다 — 완벽한 AI가 아니라 <em>내 메모</em>에 가깝습니다.</p>""": """  <p data-founder-beat="beat-blog15-data">온라인에서 사이즈표만 보고 2XL·허리 32 주문하던 시절, 반품 상자가 쌓였어요. 어깨·허리·인심을 한 번 메모해 두고 상세 실측과 비교하기 시작한 뒤로 “이번에도?” 확률이 줄었습니다 — 완벽한 AI가 아니라 <em>내 메모</em>에 가깝습니다.</p>""",
}

EXACT_EN = {
    """<strong>Same weight, different silhouette—I lived it.</strong> 175 cm, 78 kg — tops 2XL, waist 32 still failed at shoulder, thigh, or hem. A friend and I shared similar kg but looked nothing alike in clothes. I shop proportions first now, kg second.""": """<strong>Same weight, different silhouette—I lived it.</strong> 175 cm, 78 kg — 2XL oversize tops (trend + belly comfort), waist 32 pants — still failed at shoulder, thigh, or hem. A friend and I shared similar kg but looked nothing alike in clothes. I shop proportions first now, kg second.""",
    """<strong>Tops broke on neckline, shoulder, and length.</strong> I’m 175 cm, 78 kg — 2XL oversize, labels “should work” online, but shoulder seams sat wrong while the chest was roomy—or the opposite. Trendy pieces looked sharp on the rack but wrong on my frame. One shoulder measurement cut my returns a lot.""": """<strong>Tops broke on neckline, shoulder, and length.</strong> I’m 175 cm, 78 kg — I wear 2XL for oversize (trend + belly comfort), but buying by label online still failed: shoulder seams sat wrong while the chest was roomy—or the opposite. One shoulder measurement cut my returns a lot.""",
    """<strong>Shoulders broke most of my tops.</strong> I’m 175 cm, 78 kg — wear 2XL for oversize but bought by label without checking shoulder width—seams too short pinched my arms; too long and the coat drooped. Same label, 1–2cm shoulder difference between brands. One number beats S/M/L for structured tops.""": """<strong>Shoulders broke most of my tops.</strong> I’m 175 cm, 78 kg — I wear 2XL oversize (trend + comfort) but bought by label without checking shoulder width—seams too short pinched my arms; too long and the coat drooped. Same 2XL, 1–2cm shoulder difference between brands. One number beats S/M/L for structured tops.""",
    """<strong>Why I started with hand span:</strong> I'm 175 cm, 78 kg — tops 2XL, waist 32; at home shoulders or hem still felt off. No tape handy, I marked thumb-to-pinky once against a ruler and reused it for shoulder and waist estimates—the same idea in the live analyzer. Educational styling only; not medical advice.""": """<strong>Why I started with hand span:</strong> I'm 175 cm, 78 kg — 2XL oversize tops, waist 32 pants; at home shoulders or hem still felt off. No tape handy, I marked thumb-to-pinky once against a ruler and reused it for shoulder and waist estimates—the same idea in the live analyzer. Educational styling only; not medical advice.""",
    """<strong>Less sci-fi, more practical.</strong> I'm 175 cm, 78 kg — 2XL oversize tops, waist 32 pants and failing. I wanted to measure once—hand span when no tape—and filter chaos. That’s the direction behind FITME.""": """<strong>Less sci-fi, more practical.</strong> I'm 175 cm, 78 kg — kept ordering 2XL tops and waist 32 pants online and failing. I wanted to measure once—hand span when no tape—and filter chaos. That’s the direction behind FITME.""",
}


def apply_replacements(text: str, pairs: list[tuple[str, str]]) -> tuple[str, int]:
    n = 0
    for old, new in pairs:
        if old in text:
            count = text.count(old)
            text = text.replace(old, new)
            n += count
    return text, n


def patch_blogs() -> None:
    blog = ROOT / "blog"
    for path in sorted(blog.glob("blog*.html")):
        text = path.read_text(encoding="utf-8")
        pairs = REPLACEMENTS_EN if path.name.endswith("-en.html") else REPLACEMENTS_KO
        exact = EXACT_EN if path.name.endswith("-en.html") else EXACT_KO
        new, n = apply_replacements(text, pairs)
        for old, repl in exact.items():
            if old in new:
                new = new.replace(old, repl, 1)
                n += 1
        if new != text:
            path.write_text(new, encoding="utf-8")
            print(f"  {path.name}: {n} replace(s)")


def patch_story() -> None:
    for rel in ("index.html", "assets/fitme-app.js"):
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        orig = text
        text = text.replace(OLD_STORY_KO, STORY_P3_KO)
        text = text.replace(OLD_STORY_EN, STORY_P3_EN)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print(f"  {rel}: story-p3 updated")


def main() -> None:
    print("blogs:")
    patch_blogs()
    print("story:")
    patch_story()
    print("done")


if __name__ == "__main__":
    main()
