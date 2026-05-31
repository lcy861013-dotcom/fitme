#!/usr/bin/env python3
"""Full founder-voice pass: author-meta, personal-notes, body beats, EN series fixes."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"

NOTE_STYLE = (
    'style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;'
    'margin:20px 0;font-size:14px;line-height:1.8;"'
)

OLD_KO_NOTE = """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>작성자 경험:</strong> 표준 사이즈표는 몸통-다리 비율을 반영하지 않아 저에게 맞지 않았습니다. 인체측정 데이터와 핏 시스템을 연구해 이 프레임워크를 만들었습니다. 본 가이드는 그 연구 결과이며 의학적 조언이 아닙니다.
</div>"""

OLD_EN_NOTE = """  <div class="personal-note" style="background:#1c1a18;padding:15px;border-left:3px solid #d4a84b;margin:20px 0;font-size:14px;line-height:1.8;">
<strong>My Research Note:</strong> Standard size charts failed me because they don't account for torso-to-leg ratio. I studied anthropometric data and fit systems to build this framework. This guide reflects that research and is for educational purposes only, not medical advice.
</div>"""

OLD_AUTHOR_KO_RE = re.compile(
    r'    <div class="author-meta" style="border-bottom:1px solid #2a2724[^"]*">.*?</div>',
    re.DOTALL,
)
OLD_AUTHOR_EN_RE = re.compile(
    r'    <div class="author-meta" style="border-bottom:1px solid #2a2724[^"]*">.*?</div>',
    re.DOTALL,
)
PERSONAL_NOTE_RE = re.compile(
    r'  <div class="personal-note"[^>]*>.*?</div>',
    re.DOTALL,
)

AUTHOR_SUBTITLE_KO = {
    "blog1": "팬츠 핏 · 허리 32 반복 실패에서 정리한 글",
    "blog2": "발볼 넓은 발 · 온라인 신발 반품에서 정리한 글",
    "blog3": "황금비율 · 코디 감각 대신 내 숫자로 고른 글",
    "blog4": "상의 핏 · 어깨·목·기장에서 깨진 경험 정리",
    "blog5": "컬러 · 같은 옷인데 색만 바꿔도 달라진 날들",
    "blog6": "기본템 5 · 옷장은 있는데 입을 게 없던 시기",
    "blog7": "몸무게보다 비율 — 쇼핑 실패에서 정리한 글",
    "blog8": "WHR · 허리 32 맞는데 바지가 안 맞던 이유",
    "blog9": "아우터 · 어깨 솔기에서 판가름 난 경험",
    "blog10": "다리 비율 · 키는 같은데 기장이 다른 이유",
    "blog11": "사이즈는 맞는데 핏이 어색했던 쇼핑 실패",
    "blog12": "체형 분류 · 라벨만으로는 부족했던 경험",
    "blog13": "체형 코디 · 공식만 외우다 실패한 적",
    "blog14": "대칭 · 시선·실루엣 맞추는 쪽으로 정리",
    "blog15": "데이터 쇼핑 · 반품 줄이려고 만든 FITME",
    "blog16": "AI·핏 · 온라인 사이즈만 보다 실패 반복",
    "blog17": "캡슐 · 10벌 중 맞는 건 몇 벌이었나",
    "blog18": "하체 발달형 · 상·하 균형 맞추던 시행착오",
    "blog19": "소재 · 같은 컷인데 원단만 바꿔 실패",
    "blog20": "손뼘 측정 · FITME 만들면서 쓰는 첫 단계",
    "blog21": "어깨 너비 · 상의 반품 줄인 첫 치수",
    "blog22": "팔 길이 · 소매에서 깨진 온라인 주문",
    "blog23": "다리 길이 · 바지 기장 반복 실패",
    "blog24": "엉덩이 둘레 · 허리 32 맞는데 힙에서 터짐",
    "blog25": "WHR · 내 비율 숫자로 자신감 잡기",
}

AUTHOR_SUBTITLE_EN = {
    "blog1": "Pants fit — waist 32 kept failing online",
    "blog2": "Wide feet — shoe returns taught me width first",
    "blog3": "Golden ratio — numbers, not body scoring",
    "blog4": "Tops — neckline, shoulder, length failures",
    "blog5": "Color — same cut, different shade, different fit feel",
    "blog6": "Five basics — full closet, nothing to wear",
    "blog7": "Proportion over weight — why I shop by ratio",
    "blog8": "WHR — waist matched, hips did not",
    "blog9": "Outerwear — shoulder seam made or broke it",
    "blog10": "Leg ratio — same height, different hem line",
    "blog11": "Label fit, body did not — why I built FITME",
    "blog12": "Body types — labels were not enough for me",
    "blog13": "Outfit rules — formulas failed my lower body",
    "blog14": "Symmetry — styling optics, not beauty standards",
    "blog15": "Data shopping — fewer returns, not less taste",
    "blog16": "AI fit — less sci-fi, more practical filtering",
    "blog17": "Capsule — ten pieces, not ten that fit",
    "blog18": "Lower-body volume — balance from trial and error",
    "blog19": "Fabric — same cut, different drape, different story",
    "blog20": "Hand span — step one of how I measure at home",
    "blog21": "Shoulder width — first number that cut returns",
    "blog22": "Arm length — sleeve fails on every label size",
    "blog23": "Leg length — inseam broke more pants than waist",
    "blog24": "Hip circumference — waist 32, hips still tight",
    "blog25": "WHR — confidence from ratio, not trend chasing",
}


def note_ko(body: str) -> str:
    return f'  <div class="personal-note" {NOTE_STYLE}>\n{body}\n</div>'


def note_en(body: str) -> str:
    return f'  <div class="personal-note" {NOTE_STYLE}>\n{body}\n</div>'


NOTES_KO = {
    "blog1": note_ko(
        '<strong>바지에서 제일 많이 망했어요.</strong> 허리 32면 된다고 샀는데 기장·허벅지·발목에서 핏이 갈리더라고요. '
        '슬림/와이드 이름만 보고 사면 “옷은 예쁜데 나랑 안 어울린다”가 반복됐습니다. 쇼핑몰에서 허리 32 테이퍼드, 32 스트레이트, 32 와이드 — 셋 다 “허리는 맞는데” '
        '허벅지·기장·발목에서 따로 노는 날이 많아서 결국 둘은 반품했어요. 숫자는 같은데 <em>핏 타입 + 내 다리·엉덩이 비율</em>이 안 맞았던 거더라고요. '
        '지금은 사이즈표보다 인심·허벅지 실측부터 비교합니다. (다이어트/의학 글이 아니라 제 쇼핑 노트예요.)'
    ),
    "blog2": note_ko(
        '<strong>발볼 넓은 편이라 신발이 특히 힘들었어요.</strong> 265mm 맞는데 앞이 눌리거나, 브랜드 바꾸면 갑자기 헐렁… 발 길이만 보고 샀거든요. '
        '매장에선 괜찮아 보이다가 하루 종일 신으면 발볼이 아프고, 쇼핑몰은 더 답답해서 “발볼 넓음”, “토박스 좁음” 리뷰를 꼭 찾게 됐어요. '
        '뉴발란스 2E랑 나이키 D를 번갈아 사 보면서 <em>같은 mm도 브랜드·라스트가 다르다</em>는 걸 체감했고, 그 경험을 글로 남겼습니다.'
    ),
    "blog3": note_ko(
        '<strong>황금비율을 ‘몸매 점수’로 쓰라는 글 아닙니다.</strong> 저는 쇼핑할 때 어깨·허리·다리 <em>비율 감</em>이 없어서 코디가 자꾸 어색했어요. '
        '감으로 “상의 여유, 하의 슬림” 정도만 알고 있었는데, FITME 만들면서 어깨 너비÷허리 둘레를 대략 재 보니 제가 생각한 체형이랑 실제 숫자가 달랐어요. '
        '숫자가 틀렸다기보다 <em>느낌과 측정</em>이 어긋난 거였고, 그다음부터 “이 상의는 나한테 너무 타이트/너무 박스” 같은 선택이 덜 감으로만 하게 됐습니다. (1.618 외우라는 뜻 아님 — 쇼핑할 때 참고용입니다.)'
    ),
    "blog4": note_ko(
        '<strong>상의는 목·어깨·기장에서 많이 깨졌어요.</strong> XL이면 대충 맞겠지 하고 쇼핑몰에서 샀는데, 어깨 솔기는 짧고 가슴은 넉넉하거나 반대로 어깨만 처지는 날이 반복됐어요. '
        '유행 따라 사면 포인트는 살아도 어깨가 좁아 보이거나 몸통이 길어 보이더라고요. 나중에 알고 보니 <em>어깨 너비 숫자</em> 하나 아는 게 S/M/L보다 먼저였고, '
        '체형별 상의는 ‘예쁜 옷’보다 <em>내 비율을 보완하는 옷</em> 고르는 쪽에 가깝습니다.'
    ),
    "blog5": note_ko(
        '<strong>색은 저한테 어려웠어요.</strong> 같은 검정인데 어디를 밝게 두느냐에 따라 다리가 짧아 보이거나 어깨가 넓어 보이더라고요. '
        'XL·허리 32 맞는 바지인데 상의 색만 잘못 골라 “거의 맞는데… 나한테는 아닌” 그 느낌이 색에서 온 적도 많아요. '
        '코디 실패할 때 “색 조합”만 바꿔도 체형 인상이 달라진 적이 많아서 정리해 봤습니다. (의학·다이어트 글이 아니라 스타일 참고용입니다.)'
    ),
    "blog6": note_ko(
        '<strong>옷장에 있는데도 뭐 입을지 모르겠던 시기</strong> — 저도 그랬어요. 유행템은 많은데 입을 때마다 어딘가 어색한 날이 반복됐고, '
        '기본템 5개만 내 비율(어깨·다리·허리 감)에 맞게 고르면 일주일은 버틴다는 걸 나중에 알았습니다. '
        '트렌드템보다 <em>내 몸에 맞는 기본</em>이 먼저였어요. 쇼핑몰에서 “세트 코디”만 따라 하다 실패한 경험도 여기서 정리했습니다.'
    ),
    "blog7": note_ko(
        '<strong>체중 숫자만 보고 실패한 적 많아요.</strong> 저울 숫자는 비슷한데 상의·바지 핏이 완전 달라지더라고요. XL이면 대충 맞겠지, 허리 32면 32 입겠지 — '
        '쇼핑몰에서 그렇게 샀는데 집에서 입으면 어깨는 널널하고 허벅지만 끼거나, 반대로 허리는 맞는데 기장·다리 라인이 어색한 날이 반복됐어요. '
        '친구랑 kg 숫자 비교해 봐도 실루엣은 전혀 달랐고요. 저는 몸무게보다 <em>어깨·허리·다리 비율</em>을 대략이라도 알고 나서 쇼핑 실패가 줄었습니다. (의학 조언이 아니라 제가 FITME 쓰면서 정리한 경험입니다.)'
    ),
    "blog8": note_ko(
        '<strong>허리 32 맞는데 엉덩이에서 터지는 적</strong> — 그거 알죠? 허리만 보고 샀는데 엉덩이·힙에서 끼거나, 반대로 허리만 헐렁한 바지. '
        '저는 여기서 “사이즈가 아니라 <em>비율</em> 문제구나” 처음 느꼈어요. WHR을 대략이라도 알면 “이 핏은 나한테 왜 어색하지?”가 설명됩니다. '
        '의학 진단이 아니라 <em>쇼핑·코디 감</em> 잡는 용도로 씁니다.'
    ),
    "blog9": note_ko(
        '<strong>자켓·아우터는 어깨에서 판가름 났어요.</strong> XL이라도 어깨 솔기가 짧으면 전체가 작아 보이고, 길면 처져 보이더라고요. '
        '쇼핑몰에서 “오버핏”만 보고 샀다가 집에서 입으면 어깨가 처져서 “거의 맞는데…” 반품한 적이 많아요. '
        '어깨 너비 숫자 하나 알고 나면 상의·아우터 반품이 확 줄었습니다. (<a href="/blog/blog21" style="color:#d4a84b;">어깨 너비 측정</a> 글도 참고하세요.)'
    ),
    "blog10": note_ko(
        '<strong>키는 같은데 다리 길이 느낌이 다른 이유</strong> — 저도 허리선·기장에서 많이 깨졌어요. 허리 32 맞는 바지인데 기장만 길어 보이거나 무릎에서 핏이 어색한 날이 반복됐고요. '
        '다리 비율만 알아도 하의 기장·신발 조합이 달라져서 “조금 더 길어 보인다”는 말을 들은 적 있습니다. '
        '키 숫자보다 <em>다리÷키</em> 감이 먼저예요.'
    ),
    "blog11": note_ko(
        '<strong>“사이즈 문제 아닌데 왜 안 맞지?”</strong> — 저의 쇼핑 실패 대부분이 이거였어요. 라벨은 맞는데 어깨·다리·허리 비율이 안 맞으면 어딘가 항상 어색합니다. '
        '상의는 어깨 봉제선이 처지고, 바지는 허리만 맞고 허벅지가 끼거나 기장이 엉뚱해지고요. 매장보다 쇼핑몰에서 더 자주 겪었어요 — 사진·리뷰는 예쁜데 집에서 입으면 “거의 맞는데… 나한테는 아닌” 그 패턴. '
        '반품 박스 쌓이면서 “내 체형이 이상한 건가?” 싶었는데, 나중에 알고 보니 <em>브랜드 표준 비율</em>과 내 어깨·다리·허리 비율이 안 맞았던 거더라고요. FITME 만들게 된 이유도 여기서 시작됐어요.'
    ),
    "blog12": note_ko(
        '<strong>체형 이름(모래시계·역삼각형)만으로는 부족했어요.</strong> 같은 라벨 체형도 어깨·다리 숫자가 다르더라고요. '
        '저는 “역삼각형”이라고만 알고 상의만 줄여 봤는데, 실제로는 다리 비율이 짧아서 하의 기장·핏이 더 문제였어요. '
        '그래서 대략적인 치수·비율을 같이 보면 “내 몸”에 더 가깝게 옷을 고를 수 있었습니다.'
    ),
    "blog13": note_ko(
        '<strong>코디 공식만 외우면 또 실패합니다.</strong> 저는 “상의는 이렇게”만 보고 샀다가 하체 비율이랑 안 맞을 때가 많았어요. '
        'XL 상의 + 슬림 바지 공식이 유행일 때 따라 샀는데, 허리 32 맞는 바지가 허벅지에서 끼이면 전체가 어색해지더라고요. '
        '강조/보완을 <em>내 숫자</em> 기준으로 고르는 쪽이 덜 헛발질이었습니다.'
    ),
    "blog14": note_ko(
        '<strong>대칭 얘기를 ‘예쁘게 생겨야’로 오해하지 마세요.</strong> 저는 한쪽 어깨·다리 길이 감이 달라 보일 때 옷 선택이 달라졌어요. '
        '쇼핑몰 사진처럼 “완벽 대칭”을 목표로 삼기보다, 패션으로 시선·실루엣을 맞추는 쪽에 가깝게 정리했습니다. '
        '의학·미용 수술 얘기가 아닙니다.'
    ),
    "blog15": note_ko(
        '<strong>감으로 고르던 스타일이 데이터로 바뀐 건 아닙니다.</strong> 여전히 감도 쓰는데, <em>어깨·허리·다리 숫자</em>가 있으면 “이번에도 반품?” 확률이 줄어요. '
        '온라인에서 사이즈만 보고 실패가 반복되던 저를 위해 FITME도 패션 고수용이 아니라 쇼핑 실패 줄이려고 만든 도구예요.'
    ),
    "blog16": note_ko(
        '<strong>AI·데이터 얘기만 하면 거리감 있죠.</strong> 저는 그냥 온라인에서 XL·허리 32만 보고 실패가 반복돼서, 내 치수를 한 번 재 두고 필터링하고 싶었어요. '
        '줄자 찾기 귀찮아서 손뼘부터 썼고, 그게 지금 FITME 방향입니다. 거창한 패션 AI가 아니라 <em>내 숫자 메모</em>에 가깝습니다.'
    ),
    "blog17": note_ko(
        '<strong>옷장 10벌도 ‘다 나한테 맞는 10벌’은 아니었어요.</strong> 세일·유행 따라 사면 많아지는데, 입을 때마다 “거의 맞는데…”가 반복됐어요. '
        '기본템을 체형·비율 기준으로 다시 고르니 입을 때마다 편한 날이 늘었습니다. 많이 사는 것보다 <em>맞는 것</em> 먼저였어요.'
    ),
    "blog18": note_ko(
        '<strong>하체 발달형 체형은 상·하 균형이 핵심이었어요.</strong> 하의만 넓어 보이게 입으면 더 그쪽으로 시선이 갔고요. '
        '저도 와이드 바지에 박스 티만 입었다가 “다리만 굵어 보인다”는 말 들은 적 있어요. 상의·기장·색으로 균형 맞추는 공식을 제 경험 기준으로 적었습니다.'
    ),
    "blog19": note_ko(
        '<strong>같은 디자인인데 소재만 바꾸면 실루엣이 달라져요.</strong> 저는 얇은 니트 vs 두꺼운 면 티에서 “어느 쪽이 나한테 낫지?”를 몰라 실패한 적이 많습니다. '
        '쇼핑몰 썸네일은 비슷한데 집에서 입으면 드레이프가 전혀 다르더라고요. 체형보다 <em>드레이프·두께</em>가 먼저인 날도 있습니다.'
    ),
}

NOTES_EN = {
    "blog1": note_en(
        '<strong>Pants were my biggest online-shopping fail.</strong> Waist 32 “should work,” but inseam, thigh, and ankle line killed the look. '
        'I ordered tapered, straight, and wide—all waist 32—and only the waist matched; two went back. '
        'Fit type + <em>your leg ratio</em> matter more than the waist tag. (Shopping notes, not medical advice.)'
    ),
    "blog2": note_en(
        '<strong>Wide feet made shoes brutal for me.</strong> Length fit but toes crushed—or the next brand felt sloppy. '
        'I only checked mm size until New Balance 2E vs Nike D taught me lasts differ. '
        'I hunt toe-box reviews before every online order; this post is that checklist.'
    ),
    "blog3": note_en(
        '<strong>Not a “score your body” article.</strong> I shopped without shoulder/waist/leg balance and outfits felt off. '
        'Measuring rough ratios showed my guess about my frame was wrong—not the math, but my <em>feel vs numbers</em>. '
        'Rough ratio numbers helped me pick “room on top, cleaner on bottom” with less guesswork.'
    ),
    "blog4": note_en(
        '<strong>Tops broke on neckline, shoulder, and length.</strong> XL “should work” online, but shoulder seams sat wrong while the chest was roomy—or the opposite. '
        'Trendy pieces looked sharp on the rack but wrong on my frame. One shoulder measurement cut my returns a lot.'
    ),
    "blog5": note_en(
        '<strong>Color was my blind spot.</strong> Same black, different placement—legs looked shorter or shoulders wider. '
        'Pants could be waist 32 and still feel “almost right but not on me” because of color blocking. '
        'I wrote this after small color shifts saved outfits that fit but felt wrong.'
    ),
    "blog6": note_en(
        '<strong>Full closet, nothing to wear—been there.</strong> Trend pieces piled up; getting dressed still felt off. '
        'Five basics matched to <em>my</em> proportions got me through a week. Right basics beat more trend pieces.'
    ),
    "blog7": note_en(
        '<strong>Same weight, different silhouette—I lived it.</strong> XL and waist 32 online still failed at shoulder, thigh, or hem. '
        'A friend and I shared similar kg but looked nothing alike in clothes. I shop proportions first now, kg second.'
    ),
    "blog8": note_en(
        '<strong>Waist size matched, pants still wrong.</strong> Waist 32 but hips tight—or waist loose while hips fit. '
        'WHR explained “why this cut feels off.” Educational styling context only—not medical advice.'
    ),
    "blog9": note_en(
        '<strong>Jackets live or die on shoulder width.</strong> Same size label, wrong shoulder seam—instant return. '
        '“Oversized” online often meant droopy shoulders at home. One shoulder measurement cut my outerwear fails a lot.'
    ),
    "blog10": note_en(
        '<strong>Same height, different leg line.</strong> Waist 32 pants still broke on inseam or knee line. '
        'Hem and rise choices mattered more than “tall size.” Leg ratio notes helped me look a bit longer without heel tricks only.'
    ),
    "blog11": note_en(
        '<strong>“Size is fine—why does it look wrong?”</strong> Most of my returns were proportion, not label size. '
        'Online photos looked great; at home it was “almost right but not on me.” That frustration is why I built FITME.'
    ),
    "blog12": note_en(
        '<strong>Body-type labels weren’t enough.</strong> Two “rectangles” can have different shoulder/leg numbers. '
        'I trimmed tops as an “inverted triangle” when my real issue was short leg ratio and hem length.'
    ),
    "blog13": note_en(
        '<strong>Formulas alone failed me.</strong> XL top + slim pants was the trend; waist 32 slim pants still pinched at the thigh. '
        'Emphasize vs balance works better when tied to <em>your</em> numbers.'
    ),
    "blog14": note_en(
        '<strong>Not about being “born symmetrical.”</strong> Small shoulder/leg asymmetry changed what I could wear comfortably. '
        'This is styling optics, not beauty standards or medical advice.'
    ),
    "blog15": note_en(
        '<strong>I still use instinct—with fewer returns.</strong> Shoulder/waist/leg numbers don’t replace taste; they reduce “why again?” moments. '
        'FITME is for shoppers like past me, not fashion experts.'
    ),
    "blog16": note_en(
        '<strong>Less sci-fi, more practical.</strong> I kept ordering XL and waist 32 online and failing. '
        'I wanted to measure once—hand span when no tape—and filter chaos. That’s the direction behind FITME.'
    ),
    "blog17": note_en(
        '<strong>Ten random basics ≠ ten that fit you.</strong> Sale hauls grew the closet; “almost right” repeats didn’t. '
        'Re-picking core pieces for my proportions made getting dressed calmer. Fewer, better matched wins.'
    ),
    "blog18": note_en(
        '<strong>Lower-body volume needs upper-body balance.</strong> Wide pants + boxy tee made me look bottom-heavy. '
        'Length, color, and shoulder line fixes from my own trial and error—not one body-type label.'
    ),
    "blog19": note_en(
        '<strong>Same cut, different fabric—different story.</strong> Thin knit vs heavy cotton changed what flattered me. '
        'Thumbnails looked alike online; drape at home was not. Sometimes fabric drape matters before “body type rules.”'
    ),
}

NOTES_EN_SERIES = {
    "blog20": note_en(
        '<strong>Why I started with hand span:</strong> I ordered XL and waist 32 online; at home shoulders or hem still felt off. '
        'No tape handy, I marked thumb-to-pinky once against a ruler and reused it for shoulder and waist estimates—the same idea in the live analyzer. '
        'Educational styling only; not medical advice.'
    ),
    "blog21": note_en(
        '<strong>Shoulders broke most of my tops.</strong> I bought “XL” without checking shoulder width—seams too short pinched my arms; too long and the coat drooped. '
        'Same label, 1–2cm shoulder difference between brands. One number beats S/M/L for structured tops.'
    ),
    "blog22": note_en(
        '<strong>Sleeve length rarely shows on the size tag.</strong> Torso fit, sleeves wrong—“failed again” and return. '
        'Trend chasing looked good in photos; fit kept missing at the wrist. Rough arm numbers gave me a “this sleeve should work” sense.'
    ),
    "blog23": note_en(
        '<strong>Pants broke on length more than waist.</strong> I thought waist 32 was enough; wrong inseam ruined the knee and ankle line. '
        'Same height ≠ same length. Hand span helped me lock a leg baseline when I had no tape.'
    ),
    "blog24": note_en(
        '<strong>Waist 32, hips still tight—you know it.</strong> I bought for waist only; hips pinched or the waist gaped. '
        'That’s when I felt it was a <em>ratio</em> problem, not “wrong size.” Even a rough hip measure helped the next jeans pick.'
    ),
    "blog25": note_en(
        '<strong>Honestly,</strong> pretty clothes that felt wrong all day vs plain clothes people complimented—that gap WHR helped explain for me. '
        'FITME isn’t “fashion guru”—it’s <strong>know your strengths in numbers and dress with confidence</strong>. Not medical advice.'
    ),
}

# (marker substring, paragraph html, guard id to avoid double insert)
BODY_BEATS_KO: dict[str, tuple[str, str, str]] = {
    "blog2": (
        "대부분의 쇼핑몰은 무료 반품을 제공합니다.",
        '  <p>저는 처음 뉴발란스 살 때 265와 270, D와 2E를 같이 주문해 오후에 신어 보고 덜 맞는 쪽만 반품했어요. '
        '길이만 맞추면 발볼은 여전히 아픈 날이 많더라고요 — <em>너비 옵션</em>까지 같이 비교하는 게 제 루틴입니다.</p>',
        "beat-blog2-online",
    ),
    "blog4": (
        "리뷰에서 \"어깨가 좁다\"",
        '  <p>저도 XL 재킷을 “오버핏”이라고만 보고 샀다가 어깨 솔기가 처져서 반품한 적이 많아요. '
        '이제는 상세페이지 <strong>어깨 실측</strong>부터 내 숫자(<a href="/blog/blog21" style="color:#d4a84b;">어깨 너비 측정</a>)와 1cm 이내인지 봅니다.</p>',
        "beat-blog4-online",
    ),
    "blog5": (
        "피팅룸에서 컬러 핏을 확인하는 방법",
        '  <p>저는 한동안 상의·바지 핏은 맞는데 색 배치만 잘못 골라 “옷은 괜찮은데 나랑 안 어울린다”가 반복됐어요. '
        '거울 앞에서 상·하 명도만 바꿔 보면 체형 인상이 꽤 달라지더라고요 — 치수 다음으로 색이 제 두 번째 필터입니다.</p>',
        "beat-blog5-color",
    ),
    "blog6": (
        "캡슐 워드로브 시작을 위한 옷장 정리법",
        '  <p>정리하면서 “허리는 맞는데 어딘가 어색한” 옷이 절반 넘더라고요. '
        'XL·32 맞는 것처럼 보여도 어깨·기장·핏 타입이 안 맞으면 입을 때마다 찝찝했어요. '
        '남긴 5벌은 <em>라벨</em>보다 실제로 편했던 것들이었습니다.</p>',
        "beat-blog6-closet",
    ),
    "blog8": (
        "피팅룸에서의 시간과 온라인 반품 횟수가 눈에 띄게 줄어듭니다",
        '  <p>허리 32 스트레이트는 맞는데 힙에서 끼이거나, 슬림은 허리만 헐렁한 — 저의 바지 실패 패턴이 WHR 감으로 설명되더라고요. '
        '의학 수치가 아니라 “다음 바지 고를 때 뭐를 의심할지” 정도로 씁니다.</p>',
        "beat-blog8-whr",
    ),
    "blog9": (
        "숄더(Shoulder) 항목을 직접 확인하세요.",
        '  <p>쇼핑몰에서 코트 XL을 샀는데 몸통은 여유인데 어깨 솔기만 짧아 팔이 끼였던 적이 있어요. '
        '그때부터 아우터는 가슴 둘레보다 <strong>어깨 실측</strong>을 먼저 봅니다.</p>',
        "beat-blog9-shoulder",
    ),
    "blog10": (
        "로우라이즈 팬츠가 이미 낮은 허리선을 더 아래로 끌어내리기 때문입니다.",
        '  <p>키·몸무게는 친구랑 비슷한데 바지 기장 감이 완전 달랐어요. '
        '허리 32는 맞는데 무릎·발목에서 “뭔가 어색”한 날이 많았고, 다리 길이 비율을 대략 알고 나서 하이라이즈·기장 선택이 달라졌습니다.</p>',
        "beat-blog10-leg",
    ),
    "blog11": (
        "실측 어깨 너비, 가슴 둘레, 총 기장, 팔 기장을 내 실측치와 비교하세요",
        '  <p>저는 한때 M·L·XL을 연달아 주문해 비교 반품했어요 — 라벨만 믿으면 “거의 맞는데…”가 반복되더라고요. '
        '지금은 어깨·인심 숫자 메모해 두고 상세페이지 실측과 ±1~2cm만 맞춰 봅니다.</p>',
        "beat-blog11-online",
    ),
    "blog12": (
        "신체 데이터로 쇼핑하기",
        '  <p>“역삼각형”이라고만 알고 상의만 줄였는데, 실제 문제는 짧은 다리 비율·바지 기장이더라고요. '
        '라벨 하나보다 어깨·허리·다리 숫자 세 개가 쇼핑할 때 더 도움이 됐습니다.</p>',
        "beat-blog12-shop",
    ),
    "blog13": (
        "체형 코디의 공통 원칙",
        '  <p>유행 공식(XL 오versize + 슬림)을 따라 샀는데 허리 32 슬림이 허벅지에서 끼이면 상의만 예뻐도 전체가 어색해지더라고요. '
        '저는 이제 “강조/보완”을 체형 이름보다 <em>내 어깨·다리 숫자</em>로 고릅니다.</p>',
        "beat-blog13-formula",
    ),
    "blog15": (
        "데이터로 쇼핑하는 법",
        '  <p>온라인에서 사이즈표만 보고 XL·32 주문하던 시절, 반품 상자가 쌓였어요. '
        '어깨·허리·인심을 한 번 메모해 두고 상세 실측과 비교하기 시작한 뒤로 “이번에도?” 확률이 줄었습니다 — 완벽한 AI가 아니라 <em>내 메모</em>에 가깝습니다.</p>',
        "beat-blog15-data",
    ),
    "blog16": (
        "AI 스타일링을 지금 당장 활용하는 법",
        '  <p>FITME도 거창한 패션 AI가 아니라, 제가 쇼핑몰에서 실패 반복하다 “내 숫자 한 번만 재 두자”에서 출발했어요. '
        '손뼘·줄자로 대략 치수 잡고 사이즈표랑 비교 — 그게 지금도 제 루틴입니다.</p>',
        "beat-blog16-ai",
    ),
    "blog17": (
        "흔한 실수와 피하는 법",
        '  <p>세일·추천 알고리즘으로 산 옷 중 “입을 때 편한” 비율이 맞는 건 절반도 안 됐어요. '
        '캡슐은 유행 리스트가 아니라 <em>내 어깨·다리·허리에 맞는 10벌</em>로 다시 짰습니다.</p>',
        "beat-blog17-capsule",
    ),
    "blog18": (
        "자주 하는 실수",
        '  <p>와이드 바지 + 박스 티만 입었다가 “하체만 커 보인다”는 말 들은 적 있어요. '
        '하체 볼륨형은 하의만 키우면 시선이 더 가더라고요 — 상의 어깨·색·기장을 먼저 맞추는 쪽이 저한테는 낫습니다.</p>',
        "beat-blog18-mistake",
    ),
    "blog19": (
        "소재를 이해하면 쇼핑몰 상세 페이지의 소재 정보만으로도",
        '  <p>썸네일은 비슷한데 집에서 입으면 얇은 니트는 드레이프되고 두꺼운 면 티는 박스처럼 서더라고요. '
        '같은 XL·32라도 <em>원단</em>에 따라 “거의 맞는데…”가 갈렸습니다.</p>',
        "beat-blog19-fabric",
    ),
    "blog21": (
        "어깨가 맞으면 가슴·허리 사이즈는 수선으로 조정할 수 있지만",
        '  <p>저는 상의 살 때 가슴 둘레보다 <strong>어깨 실측</strong>을 먼저 봅니다. '
        'XL이라도 어깨 솔기 1cm만 어긋나도 “거의 맞는데…” 반품이었거든요.</p>',
        "beat-blog21-shop",
    ),
    "blog23": (
        "다리 길이는 거의 변하지 않으므로",
        '  <p>허리 32는 맞는데 기장·무릎선만 어색한 바지 반품이 많았어요. '
        '키 숫자보다 <em>다리 길이÷키</em> 감을 잡고 나서 인심·라이즈를 먼저 비교합니다.</p>',
        "beat-blog23-inseam",
    ),
}

BODY_BEATS_EN: dict[str, tuple[str, str, str]] = {
    "blog2": (
        "Most stores offer free returns",
        '  <p>I ordered 265 vs 270 and D vs 2E on my first New Balance buy, tried both in the afternoon, returned the loser. '
        'Length alone left my ball of foot sore—<em>width</em> has to be in the comparison.</p>',
        "beat-en-blog2",
    ),
    "blog4": (
        "If two or more reviews say \"shoulders run narrow\"",
        '  <p>I returned plenty of XL “oversized” jackets because the shoulder seam drooped while the chest was fine. '
        'Now I match <strong>shoulder spec</strong> first (<a href="/blog/blog21-en" style="color:#d4a84b;">shoulder measure guide</a>).</p>',
        "beat-en-blog4",
    ),
    "blog11": (
        "Compare listed shoulder width, chest, total length, and sleeve to your numbers",
        '  <p>I used to order M, L, and XL and compare returns—label alone kept giving “almost right but not on me.” '
        'Now I keep shoulder and inseam in Notes and match ±1–2cm on the size chart.</p>',
        "beat-en-blog11",
    ),
    "blog21": (
        "If shoulders match, chest and waist can often be altered",
        '  <p>I check <strong>shoulder width</strong> before chest on every structured top. '
        'XL with a 1cm wrong shoulder seam was still a return for me.</p>',
        "beat-en-blog21",
    ),
}


def author_meta_ko(subtitle: str) -> str:
    return f"""  <div class="author-meta">
    <p>작성: <strong>이창용</strong> · FITME 1인 창업 (대한민국)</p>
    <p style="font-size:14px;color:#8b8178;">{subtitle} · <a href="/ko/editorial-standards" style="color:#d4a84b;">콘텐츠 기준</a> · <a href="/ko/how-it-works" style="color:#d4a84b;">도구 설명</a> · <!--email_off--><a href="mailto:lcy861013@gmail.com" style="color:#d4a84b;">lcy861013@gmail.com</a><!--/email_off--></p>
  </div>"""


def author_meta_en(subtitle: str) -> str:
    return f"""  <div class="author-meta">
    <p>By <strong>Changyong Lee</strong> · FITME solo founder (South Korea)</p>
    <p style="font-size:14px;color:#8b8178;">{subtitle} · <a href="/en/editorial-standards" style="color:#d4a84b;">Editorial standards</a> · <a href="/en/how-it-works" style="color:#d4a84b;">How it works</a> · <!--email_off--><a href="mailto:lcy861013@gmail.com" style="color:#d4a84b;">lcy861013@gmail.com</a><!--/email_off--></p>
  </div>"""


def author_meta_series_ko(subtitle: str) -> str:
    return f"""  <div class="author-meta">
    <p>작성: <strong>이창용</strong> · FITME 1인 창업 (대한민국)</p>
    <p style="font-size:14px;color:#8b8178;">{subtitle} · <a href="/ko/editorial-standards" style="color:#d4a84b;">콘텐츠 기준</a> · <a href="/ko/how-it-works" style="color:#d4a84b;">도구 설명</a> · <!--email_off--><a href="mailto:lcy861013@gmail.com" style="color:#d4a84b;">lcy861013@gmail.com</a><!--/email_off--></p>
  </div>

"""


def insert_body_beat(text: str, marker: str, paragraph: str, guard: str) -> tuple[str, bool]:
    if guard in text or marker not in text:
        return text, False
    idx = text.find(marker)
    close = text.find("</p>", idx)
    if close == -1:
        return text, False
    insert_at = close + 4
    tagged = paragraph.replace("<p>", f'<p data-founder-beat="{guard}">', 1)
    return text[:insert_at] + "\n" + tagged + text[insert_at:], True


def replace_first_personal_note(text: str, new_note: str) -> tuple[str, bool]:
    if not PERSONAL_NOTE_RE.search(text):
        return text, False
    return PERSONAL_NOTE_RE.sub(new_note, text, count=1), True


def remove_duplicate_template_notes(text: str) -> tuple[str, int]:
    count = 0
    while OLD_EN_NOTE in text:
        text = text.replace(OLD_EN_NOTE, "", 1)
        count += 1
    return text, count


def patch_author_meta(text: str, subtitle: str, lang: str) -> tuple[str, bool]:
    if "연구 기반 가이드" in text or "Research-based guide" in text:
        if lang == "ko":
            new = author_meta_ko(subtitle)
            return OLD_AUTHOR_KO_RE.sub(new, text, count=1), True
        new = author_meta_en(subtitle)
        return OLD_AUTHOR_EN_RE.sub(new, text, count=1), True
    # blog21-25 KO: add author-meta after meta if missing block
    if lang == "ko" and 'class="author-meta"' in text and "FITME 1인 창업" not in text:
        # blog20 style without subtitle line content — upgrade subtitle on blog20 only
        pass
    return text, False


def add_series_author_meta_ko(text: str, slug: str) -> tuple[str, bool]:
    if slug not in {"blog21", "blog22", "blog23", "blog24", "blog25"}:
        return text, False
    if "FITME 1인 창업" in text:
        return text, False
    subtitle = AUTHOR_SUBTITLE_KO[slug]
    block = author_meta_series_ko(subtitle)
    if 'class="series-nav"' in text:
        return text.replace('  <nav class="series-nav"', block + "  <nav class=\"series-nav\"", 1), True
    return text, False


def bump_date_modified(text: str) -> tuple[str, bool]:
    new = re.sub(
        r'"dateModified"\s*:\s*"[^"]*"',
        '"dateModified":"2026-05-30"',
        text,
    )
    new = re.sub(
        r'"dateModified"\s*:\s* "[^"]*"',
        '"dateModified":"2026-05-30"',
        new,
    )
    return new, new != text


def bump_visible_meta(text: str, lang: str) -> tuple[str, bool]:
    if "2026.05.30 업데이트" in text:
        return text, False
    if lang == "ko":
        pat = re.compile(r'(<div class="meta">[^<]*)( · FITME)', re.DOTALL)
        def repl(m):
            base = m.group(1)
            if "업데이트" in base:
                return m.group(0)
            return base + " · 2026.05.30 업데이트" + m.group(2)
        new, n = pat.subn(repl, text, count=1)
        return new, n > 0
    pat = re.compile(r'(<div class="meta">[^<]*)( · FITME)', re.DOTALL)
    def repl(m):
        base = m.group(1)
        if "Updated" in base:
            return m.group(0)
        return base + " · Updated 2026.05.30" + m.group(2)
    new, n = pat.subn(repl, text, count=1)
    return new, n > 0


def patch_file(path: Path, slug: str, lang: str) -> list[str]:
    changes: list[str] = []
    text = path.read_text(encoding="utf-8")
    orig = text

    sub = AUTHOR_SUBTITLE_KO if lang == "ko" else AUTHOR_SUBTITLE_EN
    if slug in sub:
        text, ok = patch_author_meta(text, sub[slug], lang)
        if ok:
            changes.append("author-meta")

    if lang == "ko":
        text, ok = add_series_author_meta_ko(text, slug)
        if ok:
            changes.append("series-author-meta")

    notes = NOTES_KO if lang == "ko" else NOTES_EN
    if slug in notes:
        text, ok = replace_first_personal_note(text, notes[slug])
        if ok:
            changes.append("personal-note")
    elif lang == "en" and slug in NOTES_EN_SERIES:
        text, ok = replace_first_personal_note(text, NOTES_EN_SERIES[slug])
        if ok:
            changes.append("personal-note-series-en")

    if lang == "en":
        text, n = remove_duplicate_template_notes(text)
        if n:
            changes.append(f"removed-{n}-template-notes")

    beats = BODY_BEATS_KO if lang == "ko" else BODY_BEATS_EN
    if slug in beats:
        marker, para, guard = beats[slug]
        text, ok = insert_body_beat(text, marker, para, guard)
        if ok:
            changes.append("body-beat")

    text, ok = bump_date_modified(text)
    if ok:
        changes.append("dateModified")

    text, ok = bump_visible_meta(text, lang)
    if ok:
        changes.append("visible-meta")

    if text != orig:
        path.write_text(text, encoding="utf-8")
    return changes


def main() -> None:
    total = 0
    for i in range(1, 26):
        slug = f"blog{i}"
        ko = BLOG / f"{slug}.html"
        if ko.exists():
            ch = patch_file(ko, slug, "ko")
            if ch:
                print(f"{slug}.html:", ", ".join(ch))
                total += 1
        en = BLOG / f"{slug}-en.html"
        if en.exists():
            ch = patch_file(en, slug, "en")
            if ch:
                print(f"{slug}-en.html:", ", ".join(ch))
                total += 1
    print(f"Done - {total} files patched")


if __name__ == "__main__":
    main()
