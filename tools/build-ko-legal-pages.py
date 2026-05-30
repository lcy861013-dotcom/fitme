#!/usr/bin/env python3
"""Generate Korean trust/legal pages under /ko/ (noindex, extensionless canonical)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://perfectfitme.com"
KO = ROOT / "ko"

HEAD = """<!DOCTYPE html>
<html lang="ko">
<head>
  <script src="/consent-init.js?v=7"></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-JW0DB4GXG3"></script>
  <script>gtag('js', new Date()); gtag('config', 'G-JW0DB4GXG3');</script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, follow">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{SITE}/assets/og-image-en.png">
  <meta property="og:url" content="{SITE}/ko/{slug}">
  <link rel="canonical" href="{SITE}/ko/{slug}">
  <link rel="alternate" hreflang="en" href="{SITE}/{slug}">
  <link rel="alternate" hreflang="x-default" href="{SITE}/{slug}">
  <link rel="icon" href="/favicon-32x32.png">
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600;700&family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
  <meta name="google-adsense-account" content="ca-pub-6377720400458954">
  <style>
    :root{{--bg:#0f0e0d;--card:#1c1a18;--accent:#d4a84b;--text:#e0dcd8;--muted:#8b8178;--border:#2a2724;}}
    *{{margin:0;padding:0;box-sizing:border-box;}}
    body{{background:var(--bg);color:var(--text);font-family:'Noto Sans KR','DM Sans',sans-serif;line-height:1.7;}}
    header{{padding:16px 24px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;position:sticky;top:0;background:rgba(10,10,10,0.95);backdrop-filter:blur(15px);z-index:100;}}
    .logo{{font-family:'Bebas Neue',sans-serif;font-size:24px;color:var(--accent);text-decoration:none;letter-spacing:2px;}}
    .logo span{{color:var(--text);}}
    nav{{display:flex;gap:18px;flex-wrap:wrap;}}
    nav a{{color:var(--muted);font-size:13px;text-decoration:none;}}
    nav a:hover{{color:var(--accent);}}
    main{{max-width:720px;margin:0 auto;padding:56px 20px 80px;}}
    h1{{font-family:'Bebas Neue',sans-serif;font-size:clamp(32px,7vw,48px);color:var(--accent);margin-bottom:12px;}}
    h2{{font-size:16px;font-weight:700;margin:28px 0 10px;}}
    p,li{{font-size:15px;line-height:1.9;color:#d0d0d0;margin-bottom:14px;}}
    ul{{margin:0 0 16px 22px;}}
    .sub,.updated{{font-size:13px;color:var(--muted);margin-bottom:32px;padding-bottom:20px;border-bottom:1px solid var(--border);}}
    .highlight,.steps{{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:18px 20px;margin:20px 0;}}
    a{{color:var(--accent);}}
    footer{{text-align:center;padding:24px;font-size:12px;color:var(--muted);border-top:1px solid var(--border);}}
    footer a{{color:var(--muted);}}
  </style>
  <link rel="stylesheet" href="/assets/satellite-pages-theme.css?v=7">
</head>
<body>
<header>
  <a href="/" class="logo">FIT<span>ME</span></a>
  <nav>
    <a href="/blog/">블로그</a>
    <a href="/ko/how-it-works">작동 방식</a>
    <a href="/ko/about">소개</a>
    <a href="/ko/editorial-standards">콘텐츠 기준</a>
    <a href="/ko/contact">문의</a>
  </nav>
</header>
<main>
{body}
</main>
<footer><p>© 2026 FITME · <a href="/ko/privacy">개인정보처리방침</a> · <a href="/ko/terms">이용약관</a> · <a href="/ko/contact">문의</a> · <a href="/ko/about">소개</a></p></footer>
<script defer src="/cookie-consent.js?v=8"></script>
</body>
</html>
"""

PAGES = {
    "privacy": {
        "title": "개인정보처리방침 — FITME",
        "desc": "FITME 개인정보처리방침. 체형 측정 데이터는 서버에 저장되지 않으며 브라우저에서만 처리됩니다.",
        "body": """
  <h1>개인정보처리방침</h1>
  <div class="updated">최종 업데이트: 2026년 5월 20일</div>
  <div class="highlight">체형 측정 데이터는 서버로 전송·저장되지 않습니다. 모든 분석은 브라우저에서만 실행되며 탭을 닫으면 사라집니다.</div>
  <h2>1. 수집하는 정보</h2>
  <ul>
    <li><strong>체형 측정값</strong> (키, 몸무게, 허리, 어깨 등) — 사용자가 입력하며 브라우저에서만 처리됩니다.</li>
    <li><strong>익명 이용 통계</strong> — Google Analytics(페이지뷰, 세션, 기기 유형). 개인 식별 정보는 수집하지 않습니다.</li>
    <li><strong>서버 로그</strong> — IP, 브라우저 종류, 유입 URL. 보안·성능 목적이며 체형 데이터와 연결되지 않습니다.</li>
    <li><strong>광고 쿠키</strong> — Google AdSense 맥락 광고용. Google 개인정보처리방침이 적용됩니다.</li>
  </ul>
  <h2>2. 이용 목적</h2>
  <ul>
    <li>기기 내 체형 비율 분석 및 스타일 교육 콘텐츠 제공</li>
    <li>집계된 익명 통계로 서비스 개선</li>
    <li>Google AdSense를 통한 맥락 광고</li>
  </ul>
  <p>체형 측정값은 마케팅·광고 타깃·제3자 제공에 사용하지 않습니다.</p>
  <h2>3. 저장 및 보관</h2>
  <p>체형 측정값은 <strong>FITME 서버에 저장되지 않습니다</strong>. 언어·단위 설정만 localStorage에 저장되며 서버로 전송되지 않습니다.</p>
  <h2>4. 제3자 서비스</h2>
  <ul>
    <li><strong>Google Analytics</strong> — 비필수 쿠키 동의 후 로드</li>
    <li><strong>Google AdSense</strong> — 비필수 쿠키 동의 후 로드</li>
    <li><strong>Google Fonts</strong> — 글꼴 CDN</li>
    <li><strong>카카오 SDK</strong> — 선택적 카카오톡 공유(측정값 미전송)</li>
    <li><strong>Microsoft Clarity</strong> — UX 개선용 익명 세션(동의 후)</li>
    <li><strong>ipapi.co</strong> — 국가 감지로 단위 자동 설정(국가 코드만 사용)</li>
  </ul>
  <h2>5. 쿠키</h2>
  <ul>
    <li><strong>fitme_lang</strong>, <strong>fitme_units</strong>, <strong>fitme_cookie_consent</strong> — localStorage</li>
    <li>Analytics·Clarity·AdSense 쿠키 — 배너에서 <strong>동의</strong>한 경우에만 로드</li>
  </ul>
  <p>AdSense 게시자 ID: <strong>pub-6377720400458954</strong> · <a href="/ads.txt">ads.txt</a></p>
  <h2>6. 이용자 권리</h2>
  <p>서버에 체형 데이터가 없으므로 삭제 요청 대상이 없습니다. 기타 문의는 아래 이메일로 연락해 주세요.</p>
  <h2>7. 아동</h2>
  <p>만 14세 이상 이용을 권장합니다. 14세 미만 정보가 있다고 판단되면 즉시 연락해 주세요.</p>
  <h2>8. 문의</h2>
  <p>이메일: <a href="mailto:lcy861013@gmail.com">lcy861013@gmail.com</a><br>답변 목표: 72시간 이내</p>
""",
    },
    "terms": {
        "title": "이용약관 — FITME",
        "desc": "FITME 이용약관. 무료 체형 비율 분석 도구 및 핏 가이드 이용 조건.",
        "body": """
  <h1>이용약관</h1>
  <div class="updated">최종 업데이트: 2026년 5월 20일</div>
  <p>FITME는 회원가입 없이 무료로 이용할 수 있습니다. 서비스를 이용하면 아래 약관에 동의한 것으로 봅니다.</p>
  <h2>1. 서비스 목적</h2>
  <p>웹 기반 체형 비율 분석 도구와 교육용 핏·스타일 가이드를 제공합니다. 측정값은 브라우저에서만 처리되며 서버로 전송되지 않습니다.</p>
  <h2>2. 이용 자격</h2>
  <ul>
    <li>만 14세 이상</li>
    <li>계정·로그인 불필요</li>
    <li>무료 제공</li>
  </ul>
  <h2>3. 제공 기능</h2>
  <ul>
    <li>체형 비율 추정 및 교육용 스타일 방향(의료·전문 수선 아님)</li>
    <li>측정 가이드 및 블로그 콘텐츠</li>
    <li>로케일 기반 단위 설정</li>
  </ul>
  <h2>4. 면책</h2>
  <p>결과는 통계적 참고용이며 의학·진단·전문 스타일링 조언이 아닙니다. 이용으로 인한 손해에 대해 FITME는 법령이 허용하는 범위에서 책임을 제한합니다.</p>
  <h2>5. 금지 행위</h2>
  <ul>
    <li>봇·스크래퍼로의 대량 요청</li>
    <li>무단 상업적 복제</li>
    <li>제공하지 않는 앱·의료 진단 등 허위 홍보</li>
    <li>키워드 스터핑·도어마이 페이지 등 검색 스팸 — <a href="/ko/editorial-standards">콘텐츠 기준</a> 참고</li>
  </ul>
  <h2>6. 광고</h2>
  <p>Google AdSense 광고가 표시될 수 있습니다. 쿠키는 <a href="/ko/privacy">개인정보처리방침</a>을 따릅니다.</p>
  <h2>7. 문의</h2>
  <p>이메일: <a href="mailto:lcy861013@gmail.com">lcy861013@gmail.com</a></p>
""",
    },
    "how-it-works": {
        "title": "작동 방식 — FITME",
        "desc": "FITME 무료 체형 비율 분석 도구의 입력값, 결과, 개인정보 처리 방식 설명.",
        "body": """
  <h1>FITME 작동 방식</h1>
  <p>FITME는 무료 체형 비율 분석 도구와 의류 핏 가이드를 함께 제공합니다. 도구가 하는 일·하지 않는 일·콘텐츠 운영 방식을 설명합니다.</p>
  <h2>입력하는 값</h2>
  <p>키, 몸무게, 허리 둘레(선택 단위 설정). 사진·계정·결제가 필요 없습니다. 표준 흐름에서는 측정값이 FITME 서버에 저장되지 않습니다(<a href="/ko/privacy">개인정보처리방침</a>).</p>
  <h2>받는 결과</h2>
  <div class="steps">
    <p><strong>1. 비율 추정</strong> — 허리·키, 어깨·힙, 다리·몸통 등</p>
    <p><strong>2. 체형 프로필</strong> — 실용적인 스타일 방향</p>
    <p><strong>3. FITME DNA 점수</strong> — 0–100 요약(교육용, 의료 아님)</p>
  </div>
  <p>3D 스캔·의료 검사·전문 수선 치수표가 아닙니다. 한계는 <a href="/ko/about">소개</a>를 참고하세요.</p>
  <h2>블로그 콘텐츠</h2>
  <p><a href="/blog/">블로그</a>에 바지 핏, WHR, 캡슐 워드로브 등 원문 가이드를 게시합니다. 영어 글이 가장 완전하고, 일본어·포르투갈어는 현지화 판입니다(<a href="/ko/editorial-standards">콘텐츠 기준</a>).</p>
  <h2>도구 사용하기</h2>
  <p><a href="/#analysis">무료 체형 분석 시작 →</a> · <a href="/demo-video">데모 영상</a> · 문의: <a href="mailto:lcy861013@gmail.com">lcy861013@gmail.com</a></p>
""",
    },
    "editorial-standards": {
        "title": "콘텐츠 기준 — FITME",
        "desc": "FITME 핏·체형 가이드의 작성 원칙, 업데이트 정책, 품질 기준.",
        "body": """
  <h1>콘텐츠 기준</h1>
  <p class="sub">최종 업데이트: 2026년 5월 20일 · perfectfitme.com</p>
  <p>FITME는 체형 비율·의류 핏·스타일링에 관한 <strong>독창적 교육 콘텐츠</strong>를 게시합니다. 검색·광고만을 위한 얇은 페이지가 아니라, 독자가 실제로 옷을 고를 때 도움이 되는 정보를 목표로 합니다.</p>
  <h2>독창 콘텐츠</h2>
  <p>어깨·힙, 허리·힙, 다리·몸통 비율 등 자체 방법론으로 글을 작성·편집합니다. 타 사이트 전문을 복사하지 않습니다.</p>
  <p>영어 가이드가 가장 완전합니다. 일본어·포르투갈어 글은 현지 사이즈·습관 메모가 추가된 현지화 판이며, 짧은 글은 영어 전문 가이드로 연결합니다.</p>
  <h2>피하는 것</h2>
  <ul>
    <li>실질 내용 없는 키워드 나열·도어마이 페이지</li>
    <li>가치 없이 동일 문단을 여러 URL에 복제</li>
    <li>스크랩·자동 생성 문장을 사람 글처럼 위장</li>
    <li>제공하지 않는 앱·다운로드·의료 서비스 허위 표기</li>
  </ul>
  <h2>업데이트</h2>
  <p>방법·도구·핏 조언이 바뀌면 글을 수정합니다. 홈의 분석 도구는 브라우저에서만 동작합니다.</p>
  <h2>관련 페이지</h2>
  <p><a href="/ko/about">소개</a> · <a href="/ko/privacy">개인정보</a> · <a href="/ko/terms">이용약관</a> · <a href="/ko/contact">문의</a> · <a href="/ko/how-it-works">작동 방식</a></p>
""",
    },
}


def main() -> None:
    KO.mkdir(exist_ok=True)
    for slug, data in PAGES.items():
        html = HEAD.format(
            SITE=SITE,
            slug=slug,
            title=data["title"],
            desc=data["desc"],
            body=data["body"].strip(),
        )
        out = KO / f"{slug}.html"
        out.write_text(html, encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
