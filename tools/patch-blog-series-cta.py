#!/usr/bin/env python3
"""Mid-article CTA + related links for measurement series blog20–25 (KO + EN)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG = ROOT / "blog"
LASTMOD = "2026-05-30"

MID_MARKER = "blog-mid-cta"

RELATED_BEFORE_CTA = re.compile(
    r"(<p class=\"ymyl-disclaimer\">.*?</p>\n)(<div class=\"cta\">)",
    re.DOTALL,
)

KO = {
    "blog20.html": {
        "mid_after": "스마트폰 실제 너비와 비교해서 한 뼘을 계산할 수도 있어요.</div>\n\n",
        "mid_title": "한 뼘만 알아도 실측표 비교가 쉬워져요",
        "mid_sub": "지금 재 둔 한 뼘·어깨·허리 숫자를 FITME에 넣으면 비율과 스타일 방향을 한번에 볼 수 있어요.",
        "utm": "blog20",
        "related": [
            ("/blog/blog21", "② 어깨 너비 재기 — 견봉부터 손뼘까지"),
            ("/blog/blog22", "③ 팔 길이 재기 — 소매 기장 맞추기"),
            ("/blog/blog25", "⑥ WHR · 비율 정리"),
        ],
    },
    "blog21.html": {
        "mid_after": "그래서 사이즈표보다 <em>내 어깨 너비 숫자</em> 하나 아는 게 먼저라고 생각합니다.\n</div>\n\n",
        "mid_title": "어깨 숫자 하나가 상의 반품을 줄여요",
        "mid_sub": "2XL 오버핏이어도 어깨 실측이 브랜드마다 달라요. 측정값을 FITME에 넣고 비율부터 확인해 보세요.",
        "utm": "blog21",
        "related": [
            ("/blog/blog20", "① 한 뼘 기준 잡기"),
            ("/blog/blog22", "③ 팔 길이 재기"),
            ("/blog/blog9", "어깨 너비가 옷 핏을 바꾸는 법"),
        ],
    },
    "blog22.html": {
        "mid_after": "다음에 살 때 “이 정도 소매면 될 것 같다”는 감이 생깁니다.\n</div>\n\n",
        "mid_title": "소매는 몸통 사이즈와 별개예요",
        "mid_sub": "상완·하완 길이를 메모해 두고 FITME에서 팔 비율과 추천 실루엣을 확인해 보세요.",
        "utm": "blog22",
        "related": [
            ("/blog/blog21", "② 어깨 너비 재기"),
            ("/blog/blog23", "④ 다리 길이 재기"),
            ("/blog/blog10", "다리 길이 비율 — 더 길어 보이는 코디"),
        ],
    },
    "blog23.html": {
        "mid_after": "줄자 없을 때는 손뼘으로라도 다리 길이 감을 잡아 두는 게 도움이 됐어요.\n</div>\n\n",
        "mid_title": "허리 맞아도 기장에서 깨지는 경우",
        "mid_sub": "다리 비율을 알면 인심·하이웨이스트 선택이 쉬워집니다. FITME 무료 분석으로 확인해 보세요.",
        "utm": "blog23",
        "related": [
            ("/blog/blog20", "① 한 뼘 기준 잡기"),
            ("/blog/blog24", "⑤ 엉덩이 둘레 재기"),
            ("/blog/blog10", "다리 길이 비율 스타일링"),
        ],
    },
    "blog24.html": {
        "mid_after": "엉덩이 둘레를 손뼘으로라도 재 두면, 다음 바지 고를 때 훨씬 덜 답답합니다.\n</div>\n\n",
        "mid_title": "허리 32와 힙 실측은 다른 문제",
        "mid_sub": "엉덩이·허리 숫자로 WHR을 보면 바지 핏 실패가 줄어요. FITME에서 비율을 계산해 보세요.",
        "utm": "blog24",
        "related": [
            ("/blog/blog23", "④ 다리 길이 재기"),
            ("/blog/blog25", "⑥ WHR · 비율 정리"),
            ("/blog/blog8", "허리-골반 비율(WHR) 완전 가이드"),
        ],
    },
    "blog25.html": {
        "mid_after": "엉덩이 둘레 손뼘 측정법 →</a></div>\n\n",
        "mid_title": "WHR 숫자만 알면 쇼핑이 달라져요",
        "mid_sub": "허리·골반·어깨를 한 번 입력하면 체형 분류와 스타일 방향을 FITME가 정리해 줍니다.",
        "utm": "blog25",
        "related": [
            ("/blog/blog20", "① 손뼘으로 모든 부위 재기"),
            ("/blog/blog24", "⑤ 엉덩이 둘레 재기"),
            ("/blog/blog7", "몸무게보다 비율이 중요한 이유"),
        ],
    },
}

EN = {
    "blog20-en.html": {
        "mid_after": "compare against the phone's known width to calculate your hand span.</div>\n\n",
        "mid_title": "One hand span unlocks every other measurement",
        "mid_sub": "Enter your span and key numbers in FITME for ratio-based fit cues—free, no signup.",
        "utm": "blog20_en",
        "related": [
            ("/blog/blog21-en", "② Measure shoulder width alone"),
            ("/blog/blog22-en", "③ Arm length — sleeve fit"),
            ("/blog/blog25-en", "⑥ WHR & proportion wrap-up"),
        ],
    },
    "blog21-en.html": {
        "mid_after": "Same 2XL, 1–2cm shoulder difference between brands. One number beats S/M/L for structured tops.\n</div>\n\n",
        "mid_title": "Shoulder cm beats the size label",
        "mid_sub": "Even in 2XL oversize, shoulder seams vary by brand. Run your numbers in FITME free.",
        "utm": "blog21_en",
        "related": [
            ("/blog/blog20-en", "① Hand span baseline"),
            ("/blog/blog22-en", "③ Arm length guide"),
            ("/blog/blog9-en", "Shoulder width & fit"),
        ],
    },
    "blog22-en.html": {
        "mid_after": "Rough arm numbers gave me a “this sleeve should work” sense.\n</div>\n\n",
        "mid_title": "Sleeve length ≠ chest size",
        "mid_sub": "Save upper/lower arm numbers and check arm ratio + styling in FITME.",
        "utm": "blog22_en",
        "related": [
            ("/blog/blog21-en", "② Shoulder width"),
            ("/blog/blog23-en", "④ Leg length"),
            ("/blog/blog10-en", "Leg ratio styling tricks"),
        ],
    },
    "blog23-en.html": {
        "mid_after": "Hand span helped me lock a leg baseline when I had no tape.\n</div>\n\n",
        "mid_title": "Waist size won't fix hem problems",
        "mid_sub": "Leg ratio drives inseam and rise choices—see yours in FITME's free analyzer.",
        "utm": "blog23_en",
        "related": [
            ("/blog/blog20-en", "① Hand span baseline"),
            ("/blog/blog24-en", "⑤ Hip circumference"),
            ("/blog/blog10-en", "Look taller — leg ratio"),
        ],
    },
    "blog24-en.html": {
        "mid_after": "Even a rough hip measure helped the next jeans pick.\n</div>\n\n",
        "mid_title": "Waist 32 can still fail at the hips",
        "mid_sub": "Hip + waist numbers → WHR and better pants picks. Try FITME free.",
        "utm": "blog24_en",
        "related": [
            ("/blog/blog23-en", "④ Leg length"),
            ("/blog/blog25-en", "⑥ WHR guide"),
            ("/blog/blog8-en", "WHR science & styling"),
        ],
    },
    "blog25-en.html": {
        "mid_after": "Hand span measurement guide →</a></div>\n\n",
        "mid_title": "Know your WHR before you buy",
        "mid_sub": "Enter waist and hip measurements—FITME classifies your shape and suggests styling.",
        "utm": "blog25_en",
        "related": [
            ("/blog/blog20-en", "① Hand-span measuring"),
            ("/blog/blog24-en", "⑤ Hip measurement"),
            ("/blog/blog7-en", "Proportions over weight"),
        ],
    },
}


def mid_cta(title: str, sub: str, utm: str, en: bool) -> str:
    btn = "Analyze My Body Type Free →" if en else "내 체형 무료 분석 →"
    font = "'DM Sans',sans-serif" if en else "'Black Han Sans',sans-serif"
    return f"""  <aside class="{MID_MARKER}" style="margin:28px 0;padding:20px 22px;background:var(--card);border:1px solid var(--border);border-radius:12px;border-left:3px solid var(--accent);">
    <p style="font-family:{font};font-size:17px;margin:0 0 6px;">{title}</p>
    <p style="font-size:14px;color:var(--muted);margin:0 0 14px;line-height:1.6;">{sub}</p>
    <a href="/?utm_source=blog&amp;utm_medium=mid_cta&amp;utm_campaign={utm}#analysis" class="cta-btn" style="margin-top:0;">{btn}</a>
  </aside>

"""


def related_block(links: list[tuple[str, str]], en: bool) -> str:
    title = "Measurement series · Related" if en else "손뼘 측정 시리즈 · 관련"
    cards = "\n".join(
        f'      <a href="{href}" class="related-card">{label}</a>' for href, label in links
    )
    return f"""<div class="related">
    <div class="related-title">{title}</div>
    <div class="related-grid">
{cards}
    </div>
  </div>

"""


def patch_html(path: Path, cfg: dict, en: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text
    changed = False

    if MID_MARKER not in text and cfg.get("mid_after") and cfg["mid_after"] in text:
        insert = mid_cta(cfg["mid_title"], cfg["mid_sub"], cfg["utm"], en)
        text = text.replace(cfg["mid_after"], cfg["mid_after"] + insert, 1)
        changed = True

    rel_html = related_block(cfg["related"], en)
    if '<div class="related">' in text:
        text = re.sub(
            r'<div class="related">[\s\S]*?</div>\s*\n',
            rel_html,
            text,
            count=1,
        )
        changed = True
    elif RELATED_BEFORE_CTA.search(text):
        text = RELATED_BEFORE_CTA.sub(r"\1" + rel_html + r"\2", text, count=1)
        changed = True

    if text != orig:
        path.write_text(text, encoding="utf-8")
    return changed


def patch_sitemap() -> int:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    new, n = re.subn(
        r"<lastmod>\d{4}-\d{2}-\d{2}</lastmod>",
        f"<lastmod>{LASTMOD}</lastmod>",
        text,
    )
    if n:
        path.write_text(new, encoding="utf-8")
    return n


def patch_feed() -> None:
    path = ROOT / "feed.xml"
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r"<updated>[^<]+</updated>",
        f"<updated>{LASTMOD}T12:00:00Z</updated>",
        text,
        count=1,
    )
    text = re.sub(
        r"(<entry>[\s\S]*?<updated>)[^<]+(</updated>)",
        rf"\g<1>{LASTMOD}T12:00:00Z\g<2>",
        text,
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    print("blog series CTA + related:")
    for name, cfg in KO.items():
        p = BLOG / name
        if patch_html(p, cfg, False):
            print(f"  {name}")
    for name, cfg in EN.items():
        p = BLOG / name
        if patch_html(p, cfg, True):
            print(f"  {name}")

    print("sitemap:")
    print(f"  {patch_sitemap()} lastmod tags updated")
    print("feed:")
    patch_feed()
    print("  feed.xml updated")
    print("done")


if __name__ == "__main__":
    main()
