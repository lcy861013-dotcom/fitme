# Webmaster Console — Bing & Yandex 등록 가이드

이 사이트는 이미 **Google Search Console**, **Naver Search Advisor** 등록이 끝나 있고
영문 SEO를 키우기 위해 **Bing Webmaster Tools** 와 **Yandex Webmaster** 를 추가합니다.

---

## 왜 두 개를 추가하나

| 검색엔진 | 점유율 (영어권 기준) | 비고 |
|---------|--------------------|------|
| Google | ~88% | Search Console 등록 완료 |
| Bing | ~7% | DuckDuckGo·Yahoo·ChatGPT Search 도 Bing 인덱스 사용 → 실제 영향 ~15% |
| Yandex | ~1% (글로벌) | 러시아·CIS·동유럽 시장 노출 |
| Naver | 한국 한정 | 등록 완료 |

> 영어권 트래픽을 키우려면 **Bing 등록은 사실상 필수**.
> Yandex 는 향후 러시아어 콘텐츠가 추가될 때를 위한 사전 작업.

---

## A. Bing Webmaster Tools 등록 (10분)

1. https://www.bing.com/webmasters/ 접속 → Microsoft 계정 로그인
2. 우측 상단 **+ Add a site** → `https://perfectfitme.com/` 입력
3. 검증 방법 3가지 중 **HTML Meta Tag** 또는 **Import from Google Search Console** 선택
   - **추천: Google 가져오기.** 이미 Google 등록돼 있으니 클릭 한 번으로 즉시 검증·sitemap 자동 인식.
   - 메타 태그 방식이면 Bing이 발급한 `<meta name="msvalidate.01" content="...">` 태그를 받아서 **`index.html` `<head>`** 에 추가.
4. 검증 통과 후 좌측 메뉴에서 **Sitemaps → Submit Sitemap** → `https://perfectfitme.com/sitemap.xml`
5. **URL Inspection** 으로 메인 + 영문 블로그 5~10개 즉시 인덱싱 요청
6. 며칠 후 **Search Performance** 탭에서 노출/클릭 데이터 확인 가능

### Bing 추가 권장 작업

- **IndexNow 활성화** (좌측 메뉴) — Cloudflare 와 연동하면 새 페이지 발행 즉시 인덱싱
- 만약 메타 검증을 쓴 경우 받은 토큰 알려 주시면 `index.html` 에 자동 삽입해 드림

---

## B. Yandex Webmaster 등록 (10분)

1. https://webmaster.yandex.com/ 접속 → Yandex 계정 로그인 (없으면 가입, 무료)
2. **+ Add site** → `https://perfectfitme.com/`
3. 검증 방법 4가지 중 **Meta Tag** 추천
   - 발급된 `<meta name="yandex-verification" content="...">` 를 **`index.html` `<head>`** 에 추가
   - 서브 페이지에는 필요 없음 (메인만)
4. 검증 후 **Indexing → Sitemap files** → `https://perfectfitme.com/sitemap.xml`
5. **Indexing → URL monitoring** 에서 메인 + 영문 블로그 핵심 5개 모니터링 등록

> Yandex 는 검증·인덱싱 속도가 Google/Bing 보다 느립니다. 1~2주 기다려야 Search Console 같은 데이터가 보이기 시작.

---

## 검증 토큰 받으면 알려주세요

발급된 메타 태그 두 줄을 알려 주시면 `index.html` `<head>` 에 다음과 같이 자동으로 박아 드립니다.

```html
<meta name="msvalidate.01" content="여기에-Bing-토큰" />
<meta name="yandex-verification" content="여기에-Yandex-토큰" />
```

> Google 가져오기 방식으로 Bing 검증을 통과하면 Bing 메타 태그는 필요 없습니다.

---

## 등록 후 체크리스트

- [ ] Bing Webmaster: 검증 완료
- [ ] Bing: sitemap.xml 제출, "Sitemaps" 탭에서 25+ URL 발견 확인
- [ ] Bing: URL Inspection 으로 메인 즉시 인덱싱
- [ ] Yandex: 검증 완료
- [ ] Yandex: sitemap.xml 제출
- [ ] (선택) Bing IndexNow 활성화

---

## 참고: 이미 안전하게 셋업돼 있는 부분

- ✅ `robots.txt` 에 `Sitemap: https://perfectfitme.com/sitemap.xml` 명시
- ✅ `sitemap.xml` 에 KO/EN 양 언어 모두 hreflang 체인 정확
- ✅ 메인 + 모든 블로그에 `canonical` 태그
- ✅ Schema.org Organization / WebSite / WebApplication / Article / BreadcrumbList JSON-LD
