#!/usr/bin/env python3
"""Replace template author notes on blog1-19 (KO + EN) with unique founder voice."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"

OLD_KO = """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>작성자 경험:</strong> 표준 사이즈표는 몸통-다리 비율을 반영하지 않아 저에게 맞지 않았습니다. 인체측정 데이터와 핏 시스템을 연구해 이 프레임워크를 만들었습니다. 본 가이드는 그 연구 결과이며 의학적 조언이 아닙니다.
</div>"""

OLD_EN = """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>My Research Note:</strong> Standard size charts failed me because they don't account for torso-to-leg ratio. I studied anthropometric data and fit systems to build this framework. This guide reflects that research and is for educational purposes only, not medical advice.
</div>"""

OLD_EN_ALT = """  <div class="personal-note">
<strong>My Research Note:</strong> Standard size charts failed me because they don't account for torso-to-leg ratio. I studied anthropometric data and fit systems to build this framework. This guide reflects that research and is for educational purposes only, not medical advice.
</div>"""

NOTES_KO = {
    "blog1": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>바지에서 제일 많이 망했어요.</strong> 허리 32면 된다고 샀는데 기장·허벅지·발목에서 핏이 갈리더라고요. 슬림/와이드 이름만 보고 사면 “옷은 예쁜데 나랑 안 어울린다”가 반복됐습니다. 팬츠는 사이즈 숫자보다 <em>핏 타입 + 내 다리 비율</em>을 같이 봐야 덜 실패합니다.
</div>""",
    "blog2": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>발볼 넓은 편이라 신발이 특히 힘들었어요.</strong> 사이즈 맞는데 앞이 눌리거나, 브랜드 바꾸면 갑자기 헐렁… 발 길이만 보고 샀거든요. 온라인은 더 답답해서 발볼·토박스 실측 후기를 꼭 찾게 됐고, 그 경험을 글로 남겼습니다.
</div>""",
    "blog3": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>황금비율을 ‘몸매 점수’로 쓰라는 글 아닙니다.</strong> 저는 쇼핑할 때 어깨·허리·다리 <em>비율 감</em>이 없어서 코디가 자꾸 어색했어요. 숫자로 대략적인 균형을 보면 “상의는 여유, 하의는 슬림” 같은 선택이 덜 감으로만 하게 됩니다.
</div>""",
    "blog4": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>상의는 목·어깨·기장에서 많이 깨졌어요.</strong> 유행 따라 사면 포인트는 살아도 어깨가 좁아 보이거나 몸통이 길어 보이더라고요. 체형별 상의는 ‘예쁜 옷’보다 <em>내 비율을 보완하는 옷</em> 고르는 쪽에 가깝습니다.
</div>""",
    "blog5": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>색은 저한테 어려웠어요.</strong> 같은 검정인데 어디를 밝게 두느냐에 따라 다리가 짧아 보이거나 어깨가 넓어 보이더라고요. 코디 실패할 때 “색 조합”만 바꿔도 체형 인상이 달라진 적이 많아서 정리해 봤습니다.
</div>""",
    "blog6": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>옷장에 있는데도 뭐 입을지 모르겠던 시기</strong> — 저도 그랬어요. 기본템 5개만 내 비율에 맞게 고르면 일주일은 버틴다는 걸 나중에 알았습니다. 트렌드템보다 <em>내 몸에 맞는 기본</em>이 먼저였어요.
</div>""",
    "blog7": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>체중 숫자만 보고 실패한 적 많아요.</strong> 같은 kg인데 상체·다리 비율이 다르면 옷태가 완전히 달라지더라고요. 저는 몸무게보다 <em>어디가 길고 짧은지</em>를 알고 나서 쇼핑 실패가 줄었습니다.
</div>""",
    "blog8": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>허리 32인데 하의가 안 맞을 때</strong> — 허리만 본 제 실수예요. 허리·엉덩이 비율(WHR)을 대충이라도 알면 “이 핏은 나한테 왜 어색하지?”가 설명됩니다. 의학 진단이 아니라 <em>쇼핑·코디 감</em> 잡는 용도로 씁니다.
</div>""",
    "blog9": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>자켓·아우터는 어깨에서 판가름 났어요.</strong> XL이라도 어깨 솔기가 짧으면 전체가 작아 보이고, 길면 처져 보이더라고요. 어깨 너비 숫자 하나 알고 나면 상의 반품이 확 줄었습니다.
</div>""",
    "blog10": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>키는 같은데 다리 길이 느낌이 다른 이유</strong> — 저도 허리선·기장에서 많이 깨졌어요. 다리 비율만 알아도 하의 기장·신발 조합이 달라져서 “조금 더 길어 보인다”는 말을 들은 적 있습니다.
</div>""",
    "blog11": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>“사이즈 문제 아닌데 왜 안 맞지?”</strong> — 저의 쇼핑 실패 대부분이 이거였어요. 라벨은 맞는데 어깨·다리·허리 비율이 안 맞으면 어딘가 항상 어색합니다. FITME 만들게 된 이유도 여기서 시작됐어요.
</div>""",
    "blog12": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>체형 이름(모래시계·역삼각형)만으로는 부족했어요.</strong> 같은 라벨 체형도 어깨·다리 숫자가 다르더라고요. 그래서 대략적인 치수·비율을 같이 보면 “내 몸”에 더 가깝게 옷을 고를 수 있었습니다.
</div>""",
    "blog13": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>코디 공식만 외우면 또 실패합니다.</strong> 저는 “상의는 이렇게”만 보고 샀다가 하체 비율이랑 안 맞을 때가 많았어요. 강조/보완을 <em>내 숫자</em> 기준으로 고르는 쪽이 덜 헛발질이었습니다.
</div>""",
    "blog14": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>대칭 얘기를 ‘예쁘게 생겨야’로 오해하지 마세요.</strong> 저는 한쪽 어깨·다리 길이 감이 달라 보일 때 옷 선택이 달라졌어요. 패션으로 시선·실루엣을 맞추는 쪽에 가깝게 정리했습니다.
</div>""",
    "blog15": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>감으로 고르던 스타일이 데이터로 바뀐 건 아닙니다.</strong> 여전히 감도 쓰는데, <em>어깨·허리·다리 숫자</em>가 있으면 “이번에도 반품?” 확률이 줄어요. FITME도 패션 고수용이 아니라 쇼핑 실패 줄이려고 만든 도구예요.
</div>""",
    "blog16": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>AI·데이터 얘기만 하면 거리감 있죠.</strong> 저는 그냥 온라인에서 사이즈만 보고 실패가 반복돼서, 내 치수를 한 번 재 두고 필터링하고 싶었어요. 그게 지금 FITME 방향입니다.
</div>""",
    "blog17": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>옷장 10벌도 ‘다 나한테 맞는 10벌’은 아니었어요.</strong> 기본템을 체형·비율 기준으로 다시 고르니 입을 때마다 편한 날이 늘었습니다. 많이 사는 것보다 <em>맞는 것</em> 먼저였어요.
</div>""",
    "blog18": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>하체 발달형 체형은 상·하 균형이 핵심이었어요.</strong> 하의만 넓어 보이게 입으면 더 그쪽으로 시선이 갔고요. 상의·기장·색으로 균형 맞추는 공식을 제 경험 기준으로 적었습니다.
</div>""",
    "blog19": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>같은 디자인인데 소재만 바꾸면 실루엣이 달라져요.</strong> 저는 얇은 니트 vs 두꺼운 면 티에서 “어느 쪽이 나한테 낫지?”를 몰라 실패한 적이 많습니다. 체형보다 <em>드레이프·두께</em>가 먼저인 날도 있습니다.
</div>""",
}

NOTES_EN = {
    "blog1": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Pants were my biggest online-shopping fail.</strong> Waist 32 “should work,” but inseam, thigh, and ankle line killed the look. Slim vs wide names alone kept giving me “nice pants, wrong body.” Fit type + <em>your leg ratio</em> matter more than the waist tag.
</div>""",
    "blog2": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Wide feet made shoes brutal for me.</strong> Length fit but toes crushed — or another brand felt sloppy. I started hunting toe-box reviews before buying online; this post is that checklist.
</div>""",
    "blog3": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Not a “score your body” article.</strong> I shopped without shoulder/waist/leg balance and outfits felt off. Rough ratio numbers helped me pick “room on top, cleaner on bottom” with less guesswork.
</div>""",
    "blog4": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Tops broke on neckline, shoulder, and length.</strong> Trendy pieces looked sharp on the rack but wrong on my frame. This guide is about <em>proportion fixes</em>, not “pretty tops.”
</div>""",
    "blog5": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Color was my blind spot.</strong> Same black, different placement — legs looked shorter or shoulders wider. I wrote this after small color shifts saved outfits that fit but felt wrong.
</div>""",
    "blog6": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Full closet, nothing to wear — been there.</strong> Five basics that match <em>my</em> proportions got me through a week. Right basics beat more trend pieces.
</div>""",
    "blog7": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Same weight, different silhouette — I lived it.</strong> Torso/leg split changed how clothes sat more than the scale. I shop proportions first now, kg second.
</div>""",
    "blog8": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Waist size matched, pants still wrong.</strong> WHR explained “why this cut feels off.” Educational styling context only — not medical advice.
</div>""",
    "blog9": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Jackets live or die on shoulder width.</strong> Same size label, wrong shoulder seam — instant return. One shoulder measurement cut my outerwear fails a lot.
</div>""",
    "blog10": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Same height, different leg line.</strong> Hem and rise choices mattered more than “tall size.” Leg ratio notes helped me look a bit longer without heels tricks only.
</div>""",
    "blog11": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>“Size is fine — why does it look wrong?”</strong> Most of my returns were proportion, not label size. That frustration is why I built FITME.
</div>""",
    "blog12": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Body-type labels weren’t enough.</strong> Two “rectangles” can have different shoulder/leg numbers. Adding rough measurements made shopping less random for me.
</div>""",
    "blog13": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Formulas alone failed me.</strong> I bought “rules” that ignored my lower-body ratio. Emphasize vs balance works better when tied to <em>your</em> numbers.
</div>""",
    "blog14": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Not about being “born symmetrical.”</strong> Small shoulder/leg asymmetry changed what I could wear comfortably. This is styling optics, not beauty standards.
</div>""",
    "blog15": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>I still use instinct — with fewer returns.</strong> Shoulder/waist/leg numbers don’t replace taste; they reduce “why again?” moments. FITME is for shoppers like past me.
</div>""",
    "blog16": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Less sci-fi, more practical.</strong> I wanted to measure once, filter online size chaos, and stop guessing. That’s the direction behind FITME.
</div>""",
    "blog17": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Ten random basics ≠ ten that fit you.</strong> Re-picking core pieces for my proportions made getting dressed calmer. Fewer, better matched wins.
</div>""",
    "blog18": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Lower-body volume needs upper-body balance.</strong> I looked bottom-heavy when both top and bottom were loud. Length, color, and shoulder line fixes from my own trial and error.
</div>""",
    "blog19": """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>Same cut, different fabric — different story.</strong> Thin knit vs heavy cotton changed what flattered me. Sometimes fabric drape matters before “body type rules.”
</div>""",
}


def patch_ko(slug: str) -> bool:
    path = BLOG / f"{slug}.html"
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    if OLD_KO not in text:
        return False
    path.write_text(text.replace(OLD_KO, NOTES_KO[slug], 1), encoding="utf-8")
    return True


def patch_en(slug: str) -> bool:
    path = BLOG / f"{slug}-en.html"
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    note = NOTES_EN[slug]
    if OLD_EN in text:
        path.write_text(text.replace(OLD_EN, note, 1), encoding="utf-8")
        return True
    if OLD_EN_ALT in text:
        path.write_text(text.replace(OLD_EN_ALT, note.replace('style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;"', "").replace("  <div class=\"personal-note\">", '  <div class="personal-note">'), 1), encoding="utf-8")
        return True
    return False


def main() -> None:
    ko_ok = en_ok = 0
    for i in range(1, 20):
        slug = f"blog{i}"
        if patch_ko(slug):
            ko_ok += 1
            print("patched KO", slug)
        else:
            print("skip KO", slug)
        if patch_en(slug):
            en_ok += 1
            print("patched EN", slug)
    print(f"Done: {ko_ok} KO, {en_ok} EN")


if __name__ == "__main__":
    main()
