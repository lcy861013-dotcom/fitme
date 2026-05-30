#!/usr/bin/env python3
"""Replace template author notes on blog20-25 with founder voice + series nav."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"

OLD_NOTE = """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>작성자 경험:</strong> 표준 사이즈표는 몸통-다리 비율을 반영하지 않아 저에게 맞지 않았습니다. 인체측정 데이터와 핏 시스템을 연구해 이 프레임워크를 만들었습니다. 본 가이드는 그 연구 결과이며 의학적 조언이 아닙니다.
</div>"""

SERIES = [
    ("blog20", "① 한 뼘 기준 잡기"),
    ("blog21", "② 어깨 너비"),
    ("blog22", "③ 팔 길이"),
    ("blog23", "④ 다리 길이"),
    ("blog24", "⑤ 엉덩이 둘레"),
    ("blog25", "⑥ WHR · 비율 정리"),
]

NOTES = {
    "blog20": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>저는 왜 손뼘부터 재기 시작했냐면</strong> — 매장보다 쇼핑몰에서 많이 샀는데, 매장에선 괜찮아 보이다가 집에서 입으면 애매해지는 경우가 많았거든요. “옷은 예쁜데 나랑 안 어울린다”… 그때는 우리 집 거울 탓인가 싶기도 하고, 입고 나가도 찝찝하고요. XL이면 대충 맞겠지, 허리 32면 32 입겠지 하다 보니 <em>내 비율</em>을 몰랐어요. 줄자부터 찾기 귀찮아서, 손에 붙어 있는 한 뼘으로 재기 시작했습니다. (스타일 조언이 아니라 제가 FITME 만들면서 쓰는 방법이에요.)
</div>""",
    "blog21": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>어깨에서 많이 망했어요.</strong> 상의는 “나 XL이니까 XL”만 보고 샀는데, 어깨 솔기가 짧으면 팔이 끼기고, 길면 옷이 처져서 어딘가 어색해 보이더라고요. 같은 XL인데 브랜드마다 어깨 실측이 1~2cm씩 다른 것도 나중에야 알았고요. 그래서 사이즈표보다 <em>내 어깨 너비 숫자</em> 하나 아는 게 먼저라고 생각합니다.
</div>""",
    "blog22": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>팔 길이는 사이즈 라벨에 잘 안 나와요.</strong> 몸통은 맞는데 소매만 길거나 짧을 때, “아 또 실패” 하고 반품했던 기억이 많습니다. 유행 따라가며 사면 포인트는 살아도 핏은 자꾸 어긋나더라고요. 상완·하완 길이를 대충이라도 숫자로 알면, 다음에 살 때 “이 정도 소매면 될 것 같다”는 감이 생깁니다.
</div>""",
    "blog23": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>바지는 기장에서 많이 깨졌어요.</strong> 허리 숫자만 맞추면 될 줄 알았는데, 다리 길이 비율이 안 맞으면 무릎·발목에서 핏이 이상해지더라고요. 키만 같다고 같은 기장이 아니라는 걸 반품 몇 번 하고 나서야 체감했습니다. 줄자 없을 때는 손뼘으로라도 다리 길이 감을 잡아 두는 게 도움이 됐어요.
</div>""",
    "blog24": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>허리 32 맞는데 엉덩이에서 터지는 적</strong> — 그거 알죠? 허리만 보고 샀는데 엉덩이·힙에서 끼거나, 반대로 허리만 헐렁한 바지. 저는 여기서 “사이즈가 아니라 <em>비율</em> 문제구나” 처음 느꼈어요. 엉덩이 둘레를 손뼘으로라도 재 두면, 다음 바지 고를 때 훨씬 덜 답답합니다.
</div>""",
    "blog25": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>솔직히</strong> 내 눈엔 예쁜데 나랑 안 어울리는 옷 입고 나가면 하루 종일 찝찝했어요. 반대로 “뭐지, 별로 화려하진 않은데” 편한 옷 입었을 때 주변에서 “오늘 좋은데?” 한마디 들으면 기분 최고거든요. WHR 같은 <em>비율 숫자</em>는 그 차이를 설명해 주는 쪽에 가깝고, FITME도 “패션 고수”가 아니라 <strong>내 장점을 숫자로 알고 자신감 갖자</strong>는 쪽으로 만들었습니다.
</div>""",
}

INTRO_20_OLD = """  <p>줄자가 없어도 괜찮습니다. 지금 당장 손을 펼쳐보세요. 엄지 끝에서 새끼손가락 끝까지의 거리 — 그게 당신의 <strong>한 뼘</strong>입니다. 이 하나의 수치를 알면 어깨, 허리, 팔, 다리를 어디서든 잴 수 있습니다.</p>"""

INTRO_20_NEW = """  <p>줄자 없어도 됩니다. 손만 펼치면 <strong>한 뼘</strong> 하나는 바로 나와요. 저도 쇼핑몰에서 “XL, 허리 32”만 보다가 집에서 입으면 애매해지는 날이 많았는데, 그때부터 몸을 <em>숫자·비율</em>로 보려고 했습니다. 이 글은 그 첫 단계 — <strong>내 한 뼘 기준 잡기</strong> — 입니다. 아래 ②~⑥에서 어깨·팔·다리·엉덩이·WHR까지 이어집니다.</p>"""


def series_nav(current: str) -> str:
    items = []
    for slug, label in SERIES:
        href = f"/blog/{slug}"
        if slug == current:
            items.append(
                f'      <li aria-current="step"><strong style="color:var(--accent);">{label}</strong></li>'
            )
        else:
            items.append(
                f'      <li><a href="{href}" style="color:#ccc;text-decoration:none;">{label}</a></li>'
            )
    return (
        '  <nav class="series-nav" aria-label="손뼘 측정 시리즈" '
        'style="margin:24px 0;padding:18px 20px;background:var(--card);'
        'border:1px solid var(--border);border-radius:12px;font-size:14px;line-height:1.75;">\n'
        '    <p style="margin:0 0 10px;font-weight:700;color:var(--accent);letter-spacing:0.5px;">'
        "📏 손뼘으로 재는 법 — 6단계 시리즈</p>\n"
        '    <ol style="margin:0;padding-left:20px;color:#ccc;">\n'
        + "\n".join(items)
        + "\n    </ol>\n"
        '    <p style="margin:12px 0 0;font-size:13px;color:var(--muted);">'
        "측정 후 → <a href=\"/?utm_source=blog&utm_medium=series&utm_campaign=analysis#analysis\" "
        'style="color:var(--accent);">FITME 무료 비율 분석</a></p>\n'
        "  </nav>\n"
    )


def patch_file(slug: str) -> bool:
    import re

    path = BLOG / f"{slug}.html"
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    orig = text
    nav = series_nav(slug)
    if 'class="series-nav"' not in text:
        if '  <div class="author-meta">' in text:
            text = text.replace(
                '  </div>\n\n  <p>',
                '  </div>\n\n' + nav + "\n  <p>",
                1,
            )
        else:
            text = re.sub(
                r'(  <div class="meta">.*?</div>\n)\n(  <p>)',
                r"\1\n" + nav + r"\n\2",
                text,
                count=1,
                flags=re.DOTALL,
            )
    if OLD_NOTE in text and slug in NOTES:
        text = text.replace(OLD_NOTE, NOTES[slug], 1)
    if slug == "blog20" and INTRO_20_OLD in text:
        text = text.replace(INTRO_20_OLD, INTRO_20_NEW, 1)
    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    for slug, _ in SERIES:
        if patch_file(slug):
            print("patched", slug)


if __name__ == "__main__":
    main()
