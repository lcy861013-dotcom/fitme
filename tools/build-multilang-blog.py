#!/usr/bin/env python3
"""
Build Japanese and Brazilian-Portuguese blog directories with 5 fully-localized
posts each + an index page. Mirrors the existing /blog/blogN.html template
(dark/light theme, share bar, consent, schema, hreflang chain).

Run-time effects:
  - Writes blog/ja/blog1..blog5.html, blog/ja/index.html
  - Writes blog/pt/blog1..blog5.html, blog/pt/index.html
  - Idempotent: overwrites on each run, safe to re-run after content edits.

NB: This script ONLY writes blog pages. After running, run
    tools/append-multilang-sitemap.py to refresh sitemap.xml and hreflang chains
    across existing KO/EN posts.
"""
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://perfectfitme.com"


# -------------------- Shared template --------------------

def page(*, lang: str, locale_code: str, slug: str, title: str, desc: str,
         tag: str, h1: str, meta_label: str, date: str, hreflang_alts: dict[str, str],
         thumb_path: str, thumb_alt: str, body_html: str,
         related: list[tuple[str, str]], cta_title: str, cta_sub: str,
         cta_btn: str, breadcrumb_home: str, breadcrumb_blog: str,
         breadcrumb_post: str, header_nav: list[tuple[str, str]],
         footer_text: str) -> str:
    """Render a full blog post HTML matching the existing satellite template."""
    canonical = f"{SITE}/blog/{lang}/{slug}"
    hreflang_links = "\n".join(
        f'<link rel="alternate" hreflang="{h}" href="{u}">'
        for h, u in hreflang_alts.items()
    )
    related_html = "\n    ".join(
        f'<a href="{href}" class="related-card">{txt}</a>'
        for href, txt in related
    )
    nav_html = "\n    ".join(
        f'<a href="{href}">{lbl}</a>' for href, lbl in header_nav
    )
    bcrumb = (
        '{"@type": "ListItem", "position": 1, "name": "' + breadcrumb_home
        + '", "item": "' + SITE + '/"},\n    '
        + '{"@type": "ListItem", "position": 2, "name": "' + breadcrumb_blog
        + '", "item": "' + SITE + '/blog/' + lang + '/"},\n    '
        + '{"@type": "ListItem", "position": 3, "name": "'
        + breadcrumb_post.replace('"', '\\"')
        + '", "item": "' + canonical + '"}'
    )
    return dedent(f"""\
<!DOCTYPE html>
<html lang="{locale_code}">
<head>
  <script src="/consent-init.js?v=7"></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-JW0DB4GXG3"></script>
  <script>
    gtag('js', new Date());
    gtag('config', 'G-JW0DB4GXG3');
  </script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}{thumb_path}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="{locale_code.replace('-', '_')}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}{thumb_path}">
<link rel="canonical" href="{canonical}">
{hreflang_links}
<link rel="icon" href="/favicon-32x32.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600;700&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
<meta name="google-adsense-account" content="ca-pub-6377720400458954">
<style>
:root{{--bg:#0f0e0d;--surface:#161412;--card:#1c1a18;--accent:#d4a84b;--text:#e0dcd8;--muted:#8b8178;--border:#2a2724;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:var(--bg);color:var(--text);font-family:'DM Sans','Noto Sans JP',sans-serif;line-height:1.85;}}
header{{padding:16px 24px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;background:rgba(10,10,10,0.95);backdrop-filter:blur(15px);z-index:100;}}
.logo{{font-family:'Bebas Neue',sans-serif;font-size:24px;color:var(--accent);text-decoration:none;letter-spacing:2px;}}
.logo span {{ color: var(--text); }}
nav {{ display: flex; gap: 20px; align-items: center; }}
nav a {{ color: var(--muted); font-size: 13px; text-decoration: none; letter-spacing: 1px; cursor: pointer; transition: color 0.2s; font-family: 'DM Sans',sans-serif; }}
nav a:hover {{ color: var(--accent); }}
@media (max-width:600px){{header{{flex-direction:column;gap:12px;padding:12px;}}nav{{gap:12px;}}nav a{{font-size:11px;}}}}
main{{max-width:720px;margin:0 auto;padding:40px 20px 80px;}}
.tag{{font-size:11px;letter-spacing:3px;color:var(--accent);margin-bottom:14px;font-family:'DM Sans',sans-serif;font-weight:600;}}
h1{{font-family:'Bebas Neue','Noto Sans JP',sans-serif;font-size:clamp(28px,6vw,44px);line-height:1.25;margin-bottom:10px;letter-spacing:1px;}}
.meta{{font-size:13px;color:var(--muted);margin-bottom:36px;padding-bottom:24px;border-bottom:1px solid var(--border);}}
h2{{font-family:'DM Sans','Noto Sans JP',sans-serif;font-size:19px;font-weight:700;margin:32px 0 12px;color:var(--text);}}
p{{font-size:15px;line-height:1.95;color:#d0d0d0;margin-bottom:18px;}}
.tip{{background:rgba(232,255,71,0.07);border-left:3px solid var(--accent);padding:14px 18px;border-radius:0 8px 8px 0;font-size:14px;line-height:1.8;margin:24px 0;color:#ccc;}}
.cta{{margin-top:56px;padding:32px;background:var(--card);border-radius:16px;border:1px solid var(--border);text-align:center;}}
.cta-btn{{display:inline-block;background:var(--accent);color:#0f0e0d;padding:14px 36px;border-radius:50px;font-family:'DM Sans','Noto Sans JP',sans-serif;font-weight:700;font-size:16px;text-decoration:none;margin-top:14px;}}
.related{{margin:48px 0 32px;}}
.related-title{{font-size:12px;letter-spacing:3px;color:var(--muted);margin-bottom:16px;font-weight:600;text-transform:uppercase;}}
.related-grid{{display:grid;gap:10px;}}
.related-card{{display:block;padding:14px 18px;background:var(--card);border:1px solid var(--border);border-radius:10px;font-size:14px;color:var(--text);text-decoration:none;line-height:1.5;transition:border-color .2s,color .2s;}}
.related-card:hover{{border-color:var(--accent);color:var(--accent);}}
footer{{text-align:center;padding:24px;font-size:12px;color:var(--muted);border-top:1px solid var(--border);}}
.guide-img{{width:100%;border-radius:12px;margin:28px 0;border:1px solid var(--border);}}
</style>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{title}",
  "description": "{desc}",
  "url": "{canonical}",
  "datePublished": "{date}",
  "dateModified": "{date}",
  "inLanguage": "{locale_code}",
  "author": {{ "@type": "Organization", "name": "FITME", "url": "{SITE}" }},
  "publisher": {{
    "@type": "Organization", "name": "FITME",
    "logo": {{ "@type": "ImageObject", "url": "{SITE}/icon-192.png" }}
  }},
  "image": "{SITE}{thumb_path}",
  "mainEntityOfPage": {{ "@type": "WebPage", "@id": "{canonical}" }}
}}
</script>
<script type="application/ld+json">
{{ "@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
    {bcrumb}
]}}
</script>
  <link rel="stylesheet" href="/assets/satellite-pages-theme.css?v=7">
</head>
<body>
<header>
  <a href="/" class="logo">FIT<span>ME</span></a>
  <nav>
    {nav_html}
  </nav>
</header>
<main>
  <div class="tag">{tag}</div>
  <h1>{h1}</h1>
  <div class="meta">{meta_label}</div>
  <img src="{thumb_path}" alt="{thumb_alt}" class="guide-img">

{body_html}

  <div class="related">
    <div class="related-title">{breadcrumb_blog}</div>
    <div class="related-grid">
    {related_html}
    </div>
  </div>
  <div class="cta">
    <div style="font-family:'DM Sans','Noto Sans JP',sans-serif;font-weight:700;font-size:18px;margin-bottom:8px;">{cta_title}</div>
    <div style="font-size:14px;color:var(--muted);">{cta_sub}</div>
    <a href="/?utm_source=blog&utm_medium=cta&utm_campaign=analysis_{lang}#analysis" class="cta-btn">{cta_btn}</a>
  </div>
</main>
<footer><p>{footer_text} · <a href="/privacy.html" style="color:var(--muted);">Privacy</a></p></footer>
<script defer src="/cookie-consent.js?v=7"></script>
<script defer src="/assets/fitme-share.js?v=7"></script>
</body>
</html>
""")


def index_page(*, lang: str, locale_code: str, title: str, desc: str,
               page_title: str, page_sub: str, posts: list[dict],
               header_nav: list[tuple[str, str]],
               footer_text: str, section_label: str,
               other_lang_links: list[tuple[str, str]]) -> str:
    """Render an index page for the language with cards for each post."""
    canonical = f"{SITE}/blog/{lang}/"
    nav_html = "\n    ".join(
        f'<a href="{href}">{lbl}</a>' for href, lbl in header_nav
    )
    cards = "\n".join(
        f'    <a class="blog-card" href="/blog/{lang}/{p["slug"]}">'
        f'<img src="{p["thumb"]}" alt="{p["thumb_alt"]}" loading="lazy">'
        f'<div class="bc-body"><div class="bc-tag">{p["tag"]}</div>'
        f'<div class="bc-title">{p["card_title"]}</div>'
        f'<div class="bc-desc">{p["card_desc"]}</div></div></a>'
        for p in posts
    )
    other_html = "  ·  ".join(
        f'<a href="{href}" style="color:var(--accent);text-decoration:none;">{lbl}</a>'
        for href, lbl in other_lang_links
    )
    return dedent(f"""\
<!DOCTYPE html>
<html lang="{locale_code}">
<head>
  <script src="/consent-init.js?v=7"></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-JW0DB4GXG3"></script>
  <script>
    gtag('js', new Date());
    gtag('config', 'G-JW0DB4GXG3');
  </script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/assets/og-image-en.png?v=7">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="{locale_code.replace('-', '_')}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="ko" href="{SITE}/blog/">
<link rel="alternate" hreflang="en" href="{SITE}/blog/">
<link rel="alternate" hreflang="ja" href="{SITE}/blog/ja/">
<link rel="alternate" hreflang="pt-BR" href="{SITE}/blog/pt/">
<link rel="alternate" hreflang="x-default" href="{SITE}/blog/">
<link rel="icon" href="/favicon-32x32.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500;600;700&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
<meta name="google-adsense-account" content="ca-pub-6377720400458954">
<style>
:root{{--bg:#0f0e0d;--surface:#161412;--card:#1c1a18;--accent:#d4a84b;--text:#e0dcd8;--muted:#8b8178;--border:#2a2724;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:var(--bg);color:var(--text);font-family:'DM Sans','Noto Sans JP',sans-serif;line-height:1.7;}}
header{{padding:16px 24px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;background:rgba(10,10,10,0.95);backdrop-filter:blur(15px);z-index:100;}}
.logo{{font-family:'Bebas Neue',sans-serif;font-size:24px;color:var(--accent);text-decoration:none;letter-spacing:2px;}}
.logo span {{ color: var(--text); }}
nav {{ display: flex; gap: 20px; align-items: center; }}
nav a {{ color: var(--muted); font-size: 13px; text-decoration: none; letter-spacing: 1px; cursor: pointer; transition: color 0.2s; font-family:'DM Sans',sans-serif; }}
nav a:hover {{ color: var(--accent); }}
@media (max-width:600px){{header{{flex-direction:column;gap:12px;padding:12px;}}nav{{gap:12px;}}nav a{{font-size:11px;}}}}
main{{max-width:1100px;margin:0 auto;padding:48px 20px 80px;}}
.page-title{{font-family:'Bebas Neue','Noto Sans JP',sans-serif;font-size:clamp(32px,6vw,48px);margin-bottom:8px;letter-spacing:1px;}}
.page-sub{{font-size:15px;color:var(--muted);margin-bottom:40px;}}
.lang-strip{{font-size:13px;color:var(--muted);margin:-24px 0 32px;}}
.section-label{{font-size:11px;letter-spacing:3px;color:var(--accent);font-weight:700;margin-bottom:20px;padding-bottom:12px;border-bottom:1px solid var(--border);}}
.blog-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px;}}
.blog-card{{background:var(--card);border:1px solid var(--border);border-radius:14px;overflow:hidden;text-decoration:none;color:var(--text);transition:transform .2s,border-color .2s;display:flex;flex-direction:column;}}
.blog-card:hover{{transform:translateY(-2px);border-color:var(--accent);}}
.blog-card img{{width:100%;aspect-ratio:16/9;object-fit:cover;background:#000;border-bottom:1px solid var(--border);}}
.bc-body{{padding:18px;}}
.bc-tag{{font-size:11px;letter-spacing:2.5px;color:var(--accent);font-weight:600;margin-bottom:10px;}}
.bc-title{{font-family:'DM Sans','Noto Sans JP',sans-serif;font-weight:700;font-size:17px;line-height:1.35;margin-bottom:8px;}}
.bc-desc{{font-size:13px;color:var(--muted);line-height:1.55;}}
footer{{text-align:center;padding:24px;font-size:12px;color:var(--muted);border-top:1px solid var(--border);}}
</style>
<script type="application/ld+json">
{{
  "@context":"https://schema.org","@type":"CollectionPage",
  "name":"{title}","description":"{desc}","url":"{canonical}",
  "inLanguage":"{locale_code}",
  "publisher":{{ "@type":"Organization","name":"FITME","url":"{SITE}" }}
}}
</script>
  <link rel="stylesheet" href="/assets/satellite-pages-theme.css?v=7">
</head>
<body>
<header>
  <a href="/" class="logo">FIT<span>ME</span></a>
  <nav>
    {nav_html}
  </nav>
</header>
<main>
  <h1 class="page-title">{page_title}</h1>
  <div class="page-sub">{page_sub}</div>
  <div class="lang-strip">{other_html}</div>
  <div class="section-label">{section_label}</div>
  <div class="blog-grid">
{cards}
  </div>
</main>
<footer><p>{footer_text} · <a href="/privacy.html" style="color:var(--muted);">Privacy</a></p></footer>
<script defer src="/cookie-consent.js?v=7"></script>
</body>
</html>
""")


# -------------------- JP content --------------------

JP_NAV = [
    ("/#why-fitme", "計測ガイド"),
    ("/#analysis", "体型分析"),
    ("/blog/ja/", "ブログ"),
    ("/about.html", "FITMEとは"),
]
JP_FOOTER = "© 2026 FITME. All rights reserved."
JP_CTA = dict(
    title="自分にぴったりのシルエットを見つけませんか？",
    sub="身長・体重・ウエストを入力するだけで、無料で体型分析と個別おすすめを受け取れます。",
    btn="無料で体型を分析する →",
)


JP_POSTS = [
    {
        "n": 1,
        "slug": "taikei-fuku-erabikata",
        "title": "体型別の服の選び方 完全ガイド｜FITME",
        "desc": "洋ナシ・りんご・砂時計・長方形・逆三角の5体型別に、似合う服の選び方を体系化。無料の体型診断で自分の比率を60秒で把握。",
        "tag": "BODY TYPE STYLING",
        "h1": "体型別の服の選び方 完全ガイド",
        "meta_label": "2026.05.16 · FITME スタイルガイド",
        "date": "2026-05-16",
        "thumb": "/blog/img/en/blog13-types-thumb-en.png",
        "thumb_alt": "5つの体型タイプ図解 — 洋ナシ・りんご・砂時計・長方形・逆三角",
        "card_title": "体型別の服の選び方 完全ガイド",
        "card_desc": "5体型を見極めて似合う服を選ぶ手順。比率データで失敗を減らす。",
        "body": dedent("""
  <h2>そもそも「体型」とは何か — サイズではなく比率</h2>
  <p>体型診断という言葉は普及していますが、ほとんどのアドバイスが「胸が大きい人」「お尻が大きい人」のような感覚的な分類で止まっています。本当に重要なのは <strong>絶対値ではなく比率</strong>。同じ身長160cm・体重55kgでも、肩幅とヒップ幅の比率が違えば似合うシルエットは正反対になります。FITMEでは肩幅・ウエスト・ヒップの3点を入力するだけで、あなたの比率を5つのカテゴリーに自動分類します。</p>
  <p>この記事では、5体型それぞれに対する <strong>失敗しない選び方の原則</strong> と、買う前にチェックするべきポイントを順を追って整理します。</p>

  <h2>① 洋ナシ型（ペアシェイプ） — 肩より腰が広いタイプ</h2>
  <p>肩幅が華奢で、ウエストから腰にかけて広くなる体型。日本人女性に最も多い体型の一つです。スタイリングの目標は <strong>「視線を上半身に集めること」</strong>。</p>
  <p>選び方: 肩のデザインがあるトップス（パフスリーブ、ボートネック、エポーレット）、明るい色や柄を上に、ダークトーンを下に。ボトムはストレートかワイドでヒップラインを拾わないシルエット。スキニーは腰の広さを強調するため、夏でも避けるか丈をくるぶし上で切るのが安全。</p>
  <div class="tip">💡 ポイント: ジャケットは肩の構築があるテーラードタイプ。落ち感のあるドレープジャケットは肩を細く見せる効果はあるが、洋ナシ型では腰幅をさらに強調するので注意。</div>

  <h2>② 逆三角型 — 肩が広く腰が細いタイプ</h2>
  <p>水泳・ラケット系をやっていた人、骨格的に鎖骨が長い人に多い体型。目標は <strong>「下半身にボリュームを足してバランスを取る」</strong>。</p>
  <p>選び方: Vネック、深めのスキッパー、ラグランスリーブで肩のラインを切る。ボトムはワイドパンツ、プリーツスカート、フレアスカート。色は下半身を明るく。トップにフリルや大きな襟がついたデザインは肩幅をさらに広く見せるため避ける。</p>

  <h2>③ 砂時計型 — 肩と腰がほぼ同幅、ウエストがくびれているタイプ</h2>
  <p>最も着られるシルエットが多い体型。ただし <strong>「ウエストを隠す服を選ぶと一気にバランスが崩れる」</strong> という落とし穴があります。</p>
  <p>選び方: ハイウエストのボトム、ベルト、リブニット、ラップワンピース。直線的なボックスシルエットや大きすぎるオーバーサイズは砂時計の最大の武器であるくびれを消してしまうので、サイズ感に注意。</p>

  <h2>④ 長方形型（ストレート） — 肩・ウエスト・腰の幅がほぼ同じタイプ</h2>
  <p>シャープでクリーンに見える反面、メリハリを出すには工夫が必要。目標は <strong>「腰位置や肩のラインで縦の線を作る」</strong>。</p>
  <p>選び方: ペプラム、フレアスカート、ベルテッドコート、ハイウエスト＋クロップトップで擬似的にくびれを作る。柔らかい素材（カシミヤ、レーヨン、シルク）は体に沿いやすく、長方形型の薄さと相性が良い。</p>

  <h2>⑤ りんご型（アップル） — 上半身にボリュームがあるタイプ</h2>
  <p>胸・お腹周りにボリュームがあり、脚は比較的細い体型。目標は <strong>「腰の位置を視覚的に上げて、脚の長さを活かす」</strong>。</p>
  <p>選び方: ハイウエスト＋ストレートかワイドのボトム、Vネックで首から胸の縦ラインを伸ばす。タック入りのウエストバンドや幅広ベルトは <strong>避ける</strong>（最も気にしている部分に視線を集めてしまうため）。落ち感のあるロングジャケットは胴の長さを縦線で割ってくれる名手。</p>

  <h2>5体型共通の3原則</h2>
  <p><strong>① 試着で「肩」を最初に見る。</strong>肩の縫い目があるべき場所にあれば、丈や袖は調整できる。肩が落ちている服は何をしても綺麗に着られない。</p>
  <p><strong>② 「サイズが入る」と「似合う」は別。</strong>ボタンが閉まることは似合うことの証拠ではない。鏡で2メートル離れて見たときのシルエットがすべて。</p>
  <p><strong>③ ブランド表記より自分の実測値を信じる。</strong>同じ「Mサイズ」でもブランド間で胸囲が10cm違うのは普通。お気に入りの服の実寸を控えて、他ブランドはその数字で買うと失敗が激減する。</p>

  <h2>体型診断の最短ルート — 自分の比率を数値で知る</h2>
  <p>本記事のアドバイスは「自分がどの体型に当てはまるか」を正確に知ってから初めて意味を持ちます。鏡で見ても自分の体型を客観視するのは難しい。FITMEでは身長・ウエスト・ヒップの3点を入力するだけで、肩幅と脚比率まで含めた <strong>FITME DNAスコア</strong> を60秒で算出します。診断は完全無料、メール登録不要、結果はそのまま保存できます。</p>
"""),
        "related": [
            ("/blog/ja/golden-ratio-fuku", "ゴールデンレシオで似合う服を見つける方法"),
            ("/blog/ja/pear-styling", "洋ナシ体型のための着こなしガイド"),
            ("/blog/ja/pants-fit-guide", "パンツのシルエット完全ガイド"),
            ("/blog/ja/find-body-type-data", "データで自分の本当の体型を見つける"),
        ],
        "breadcrumb_post": "体型別の服の選び方 完全ガイド",
    },
    {
        "n": 2,
        "slug": "find-body-type-data",
        "title": "データで本当の体型を見つける方法｜FITME",
        "desc": "「洋ナシ」「砂時計」などのラベルでなく、4つの実測値から自分の体型を判定する方法。FITME DNAスコアで60秒。",
        "tag": "BODY DIAGNOSIS",
        "h1": "データで本当の体型を見つける方法",
        "meta_label": "2026.05.16 · FITME 体型診断",
        "date": "2026-05-16",
        "thumb": "/blog/img/en/blog12-body-data-thumb-en.png",
        "thumb_alt": "体型診断のための4つの測定ポイント図解",
        "card_title": "データで本当の体型を見つける方法",
        "card_desc": "ラベルではなく数値で自分の比率を客観視する手順。",
        "body": dedent("""
  <h2>「体型ラベル」の落とし穴</h2>
  <p>「あなたは洋ナシ型ですね」「砂時計型は珍しい」— 体型診断サービスでよく聞く言葉ですが、実は <strong>同じラベルの中でも比率は大きく違います</strong>。例えば「洋ナシ」とされる人の中でも、ヒップと肩幅の差が3cmの人と15cmの人では選ぶべき服が全く違います。</p>
  <p>ラベルに従って買い物をしていたのに「なんとなく似合わない」感じが消えないのは、 <strong>分類が荒すぎる</strong> から。本当に必要なのは <strong>自分の身体の比率を実数で把握すること</strong> です。</p>

  <h2>たった4つの数字で体型は決まる</h2>
  <p>体型を構造的に説明する変数は驚くほど少ない。次の4点だけで、服のフィットの大半が決まります。</p>
  <p><strong>① 肩幅（肩峰幅）</strong>: 左右の肩の骨の出っ張り（肩峰）の間の直線距離。<br><strong>② ウエスト周り</strong>: 一番細い位置の周径。<br><strong>③ ヒップ周り</strong>: お尻の一番出っ張った部分の周径。<br><strong>④ 身長</strong>: 朝の身長。</p>
  <p>この4数値から自動で計算される指標が3つあります: <strong>ウエスト-ヒップ比（WHR）、肩-ヒップ比、胴-脚比</strong>。FITMEはこの3指標から、世界中の人体データと比較した「あなたの位置」を百分位で出します。</p>

  <h2>家で正確に測る — 手のひらメソッド</h2>
  <p>メジャーがなくても、自分の手の幅（手首から中指の先まで）を測っておけば、それを単位にしてウエストやヒップを測れます。手の幅の平均は男性18cm・女性16cm前後。一度自分の手の幅を測って覚えておけば、出張先や試着室でも素早く採寸できます。</p>
  <div class="tip">💡 ウエストは「一番細い位置」で測る。へその位置ではない。自然に呼吸しながら、息を吸い込まず吐き切らない中間で。</div>

  <h2>結果の読み方 — FITME DNA スコア</h2>
  <p>FITMEは入力された4数値を元に、 <strong>FITME DNAスコア</strong> という0-100の総合指標を返します。これは「あなたの比率が、世界のどの位置にあるか」のパーセンタイル。70以上であれば一般的な既製服での適合率が高く、30以下なら既製服のサイズ調整が必須レベル、という運用基準です。</p>
  <p>大事なのはスコアの数字自体ではなく、 <strong>「どの数値があなたを既製服から遠ざけているか」</strong>。スコアの下に出る「肩幅が広め（上位15%）」「胴が短め（下位25%）」のようなコメントを見れば、買い物時にチェックすべきポイントが具体的に分かります。</p>

  <h2>診断後にやるべきこと</h2>
  <p><strong>① 自分の数値を保存する。</strong>FITMEは結果をURLで保存でき、買い物の際に開いて確認できます。<br><strong>② お気に入りブランドのサイズ表と比較する。</strong>「Mサイズ」の数字を見るのではなく、自分の実測値が入るかを直接見る。<br><strong>③ 体型が変わったら再診断する。</strong>体重1-2kgで比率は意外に動きます。季節ごとに見直すのがおすすめ。</p>
"""),
        "related": [
            ("/blog/ja/taikei-fuku-erabikata", "体型別の服の選び方 完全ガイド"),
            ("/blog/ja/golden-ratio-fuku", "ゴールデンレシオで似合う服を見つける方法"),
            ("/blog/ja/pear-styling", "洋ナシ体型のための着こなしガイド"),
            ("/blog/ja/pants-fit-guide", "パンツのシルエット完全ガイド"),
        ],
        "breadcrumb_post": "データで本当の体型を見つける方法",
    },
    {
        "n": 3,
        "slug": "pear-styling",
        "title": "洋ナシ体型のための着こなしガイド｜FITME",
        "desc": "肩より腰が広い洋ナシ体型に似合うトップス・ボトム・アウター。視覚バランスを整える具体的なテクニックと、無料の体型診断。",
        "tag": "PEAR BODY STYLING",
        "h1": "洋ナシ体型のための着こなしガイド",
        "meta_label": "2026.05.16 · FITME 体型別ガイド",
        "date": "2026-05-16",
        "thumb": "/blog/img/en/blog18-pear-thumb-en.png",
        "thumb_alt": "洋ナシ体型のシルエット図と推奨ファッション",
        "card_title": "洋ナシ体型のための着こなしガイド",
        "card_desc": "上下のボリュームバランスを整える実践的テクニック。",
        "body": dedent("""
  <h2>洋ナシ体型を正しく理解する</h2>
  <p>洋ナシ体型は <strong>肩幅よりヒップ幅が明確に広い体型</strong> のこと。日本人女性に最も多いタイプで、特に20代後半から30代以降に骨盤の広がりで顕著になります。決して悪い体型ではなく、欧米では「フェミニン体型」として歴史的に高く評価されてきました。重要なのは欠点を隠すことではなく、 <strong>視覚バランスを取って自分の良さを活かす</strong> こと。</p>

  <h2>トップス — 上半身に存在感を持たせる</h2>
  <p>洋ナシ体型のスタイリングの第一原則は「視線を上に集める」。具体的には次のアイテムが効果的です。</p>
  <p><strong>パフスリーブ・コクーンスリーブ</strong>: 肩から袖にかけてボリュームがあり、肩幅を実際より広く見せる。<br><strong>ボートネック・スクエアネック</strong>: 鎖骨を横に広く露出させて、肩のラインを視覚的に拡張。<br><strong>ホルターネック</strong>: 肩のシャープな三角形を作り、腰のボリュームと対比させる。</p>
  <p>避けたいのは <strong>ラグランスリーブ</strong> と <strong>深いVネック</strong>。どちらも肩のラインを内側に絞って見せるため、すでに細い肩がさらに細く見えてしまいます。</p>

  <h2>ボトム — シルエットは「直線」で</h2>
  <p>洋ナシ体型に最も合うボトムシルエットは <strong>ストレートとワイドパンツ</strong>。腰のラインから足先までの幅が一定に近いほど、ヒップの広さが視覚的に目立ちません。逆にスキニーは腰幅とふくらはぎ幅の差を強調するため、最も避けたいシルエット。</p>
  <p>色は <strong>ダークトーン</strong>（ブラック、ダークネイビー、チャコール）が基本。ベージュやライトデニムを履きたい場合は、トップを必ずダークにして上下のコントラストでバランスを取る。</p>
  <div class="tip">💡 デニムを選ぶときはハイウエスト・ストレートを最優先。中綿入りや厚手の生地は腰のラインをカモフラージュしてくれる。</div>

  <h2>アウター — 肩で勝負する</h2>
  <p>テーラードジャケットは洋ナシ体型の最強の味方。肩パッドが入った構築的なジャケットを羽織るだけで、肩幅が3-5cm広く見え、腰のボリュームが相対的に小さく感じられます。ロングコートは <strong>必ずベルトを締める</strong>。ストンと落ちる完全ストレートのコートはヒップを強調しがちなので、ベルトで腰位置を上げると安全。</p>

  <h2>ワンピース — Aラインとラップが鉄板</h2>
  <p>洋ナシ体型に最も合うワンピースシルエットは <strong>Aライン</strong>。胸の下から自然に広がる形が、ヒップ周りを目立たせずに視線を上に集めます。次点は <strong>ラップ（巻きつけ）ワンピース</strong>。V字の襟元で上半身に視線を引き、ウエスト部分の絞りで自然なくびれを作れます。</p>

  <h2>体型診断で自分の「広さ」を数値化する</h2>
  <p>同じ洋ナシ体型でも、肩幅とヒップ幅の差が5cmの人と15cmの人では選ぶべき服の振れ幅が違います。FITMEで自分の数値を測ると、 <strong>「あなたは上下差12cm、洋ナシの中でも標準より広め」</strong> のように具体的な位置が出ます。服を買う前に1分でチェックする習慣をつけると、失敗率が大きく下がります。</p>
"""),
        "related": [
            ("/blog/ja/taikei-fuku-erabikata", "体型別の服の選び方 完全ガイド"),
            ("/blog/ja/find-body-type-data", "データで本当の体型を見つける方法"),
            ("/blog/ja/pants-fit-guide", "パンツのシルエット完全ガイド"),
            ("/blog/ja/golden-ratio-fuku", "ゴールデンレシオで似合う服"),
        ],
        "breadcrumb_post": "洋ナシ体型のための着こなしガイド",
    },
    {
        "n": 4,
        "slug": "pants-fit-guide",
        "title": "パンツのシルエット完全ガイド｜FITME",
        "desc": "スキニー・ストレート・ワイド・テーパード、4つのパンツシルエットを体型と靴に合わせて選ぶ方法。日本人体型に最適化。",
        "tag": "PANTS FIT GUIDE",
        "h1": "パンツのシルエット完全ガイド",
        "meta_label": "2026.05.16 · FITME スタイルガイド",
        "date": "2026-05-16",
        "thumb": "/blog/img/en/blog1-pants-thumb-en.png",
        "thumb_alt": "スキニー・ストレート・ワイド・テーパードのシルエット比較",
        "card_title": "パンツのシルエット完全ガイド",
        "card_desc": "4つのシルエットを体型と靴に合わせて選ぶ実践ガイド。",
        "body": dedent("""
  <h2>パンツが似合うかは「シルエット × 靴」で決まる</h2>
  <p>同じウエストサイズでも、シルエットが違えば全く別人に見えます。さらに足元に合わせる靴で、シルエットの効果は2倍にも半分にもなる。本記事では4つの主要シルエット（スキニー・ストレート・ワイド・テーパード）と、それぞれに合う靴・体型・着丈を整理します。</p>

  <h2>① スキニーフィット — 細身の脚を最大化</h2>
  <p>太もも〜くるぶしまで均一に細くなるシルエット。脚のラインを完全に出すため、 <strong>太ももが太い人には不向き</strong>。低身長でも縦ラインを強調できる効果は強い。合わせる靴は <strong>スニーカー、チェルシーブーツ、アンクルブーツ</strong>。チャンキーな厚底ブーツとは相性が悪く、くるぶしで線が断たれてしまう。</p>

  <h2>② ストレートフィット — 最も汎用性が高い</h2>
  <p>太ももから裾まで同じ幅で落ちるシルエット。逆三角・砂時計・長方形どの体型にも合う安全牌。 <strong>太ももが気になる人はハーフサイズ上を選ぶ</strong> ことで突っ張りを回避できる。靴はローファー、ダービーシューズ、スニーカーすべてOK。</p>

  <h2>③ ワイドレッグ — 2024年以降の主流</h2>
  <p>ウエストから裾までゆったり落ちるシルエット。 <strong>トップスは必ずタックイン</strong>するか、クロップド丈で対応。オーバーサイズトップ＋ワイドパンツの組み合わせはシルエットが消えるので注意。</p>
  <p>素材選びが重要。ワイドはハリのある厚手生地（ウール、リネン混、構築的なコットン）で本領発揮。軽すぎるジャージー素材は綺麗に落ちず、シルエットが崩れる。</p>
  <div class="tip">💡 ワイドパンツでは「ハーフタックイン」（前だけ入れる）が日本人体型と相性抜群。自然にウエストが見え、抜け感が出る。</div>

  <h2>④ テーパードフィット — スキニーの上位互換</h2>
  <p>太もも周りに余裕があり、膝下から裾にかけて細くなる。 <strong>下半身が気になる人にとっての最適解</strong>。動きやすく、フォーマル寄りのコーディネートにも対応できる。スキニーが「カジュアル過ぎる」場面でもテーパードは品良くまとまる。</p>

  <h2>着丈ガイド — 靴で決まる</h2>
  <p><strong>スニーカー</strong>: くるぶしが少し見える「クロップド丈」が最もクリーン。<br><strong>ローファー・ダービー</strong>: 靴の甲に少し乗るか、床ギリギリまで。<br><strong>ブーツ</strong>: 「スタック」と呼ばれる、ブーツの上に少し溜まる丈感が今のトレンド。</p>
  <p>迷ったら <strong>短めを選ぶ</strong>。長すぎは「裾上げをしていない」印象、短めは「意図して選んだ」印象になる。裾上げは1,500円前後の安価な調整なので、丈が合わないまま履く理由はない。</p>

  <h2>日本人体型の頻出パターン別おすすめ</h2>
  <p><strong>胴長短足が気になる</strong>: ハイウエスト＋ストレートで脚位置を視覚的に上げる。<br><strong>太ももががっしりしている</strong>: テーパードを最優先。<br><strong>身長が低い</strong>: クロップド丈のストレートかスキニーで縦線を強調。<br><strong>下半身にボリュームがある</strong>: ワイドパンツ＋細めのトップでバランス。</p>
"""),
        "related": [
            ("/blog/ja/taikei-fuku-erabikata", "体型別の服の選び方 完全ガイド"),
            ("/blog/ja/find-body-type-data", "データで本当の体型を見つける方法"),
            ("/blog/ja/pear-styling", "洋ナシ体型のための着こなしガイド"),
            ("/blog/ja/golden-ratio-fuku", "ゴールデンレシオで似合う服"),
        ],
        "breadcrumb_post": "パンツのシルエット完全ガイド",
    },
    {
        "n": 5,
        "slug": "golden-ratio-fuku",
        "title": "ゴールデンレシオで似合う服を見つける方法｜FITME",
        "desc": "黄金比は美容整形の話だけではない。体の比率からシルエット・色・丈の最適解を導く具体的な方法とFITME DNAスコア。",
        "tag": "GOLDEN RATIO",
        "h1": "ゴールデンレシオで似合う服を見つける方法",
        "meta_label": "2026.05.16 · FITME プロポーション理論",
        "date": "2026-05-16",
        "thumb": "/blog/img/en/blog3-golden-thumb-en.png",
        "thumb_alt": "黄金比に基づく身体プロポーション図",
        "card_title": "ゴールデンレシオで似合う服を見つける方法",
        "card_desc": "比率を意識した着こなしの理論と具体的な適用法。",
        "body": dedent("""
  <h2>ゴールデンレシオとは何か — 美しさを決める1.618</h2>
  <p>黄金比（1:1.618）は古代ギリシャの彫刻、ルネサンス絵画、現代の建築まで「美しい」と感じる比率の基準として使われてきました。人体においても、 <strong>身長に対する各部位の比率がこの数値に近いほど「整って見える」</strong> という研究があります（Tovée & Cornelissen, 2001 など）。</p>
  <p>大事なのは「黄金比に近づくため」ではなく、 <strong>自分の比率が黄金比からどう外れているかを知って、服でその差を埋めること</strong>。これがゴールデンレシオを使ったスタイリングの本質です。</p>

  <h2>身体の主要比率3つ</h2>
  <p><strong>① ウエスト-ヒップ比（WHR）</strong>: 女性の理想は0.65-0.75、男性は0.85-0.95。<br><strong>② 肩-ウエスト比</strong>: 女性は1.4前後、男性は1.6以上で「逆三角形」と認識される。<br><strong>③ 胴-脚比</strong>: 身長の45%が脚の長さに近いと「脚が長い」印象。</p>

  <h2>比率から服を決める</h2>
  <p><strong>WHRが大きい（くびれが浅い）人</strong>: ベルト、ペプラム、ラップワンピースで擬似的なくびれを作る。<br><strong>肩-ウエスト比が小さい人</strong>: 肩のデザインを強調（パフスリーブ、エポーレット）。<br><strong>胴-脚比が小さい（脚が短く見える）人</strong>: ハイウエストで脚の起点を視覚的に上げる。</p>
  <div class="tip">💡 黄金比は絶対的な目標ではなく、 <strong>「視覚的にバランスが取れて見える基準」</strong>。自分の比率を知ったうえで、その方向に服で調整するだけで効果は大きい。</div>

  <h2>FITMEで自分の比率を一気に出す</h2>
  <p>FITMEは身長・ウエスト・ヒップを入力すると、3つの比率を自動計算して百分位（パーセンタイル）で表示します。 <strong>「WHR 上位15%」「脚比 下位30%」</strong> のような数値で出るので、どこを服で補強すべきかが明確になります。診断は60秒、完全無料、メール登録不要。</p>

  <h2>比率の知識は買い物の精度を変える</h2>
  <p>店頭で「これ似合うかな？」と悩む時間が長い人ほど、 <strong>自分の比率を数値で把握していない</strong> 傾向があります。逆に自分の3比率を覚えている人は、ハンガーラックを見ただけで「これは合う・合わない」が秒で判別できる。スタイリングは才能ではなく、 <strong>自分の数値を覚えているかどうか</strong>。</p>
"""),
        "related": [
            ("/blog/ja/taikei-fuku-erabikata", "体型別の服の選び方 完全ガイド"),
            ("/blog/ja/find-body-type-data", "データで本当の体型を見つける方法"),
            ("/blog/ja/pear-styling", "洋ナシ体型のための着こなしガイド"),
            ("/blog/ja/pants-fit-guide", "パンツのシルエット完全ガイド"),
        ],
        "breadcrumb_post": "ゴールデンレシオで似合う服を見つける方法",
    },
]


# -------------------- PT-BR content --------------------

PT_NAV = [
    ("/#why-fitme", "Como medir"),
    ("/#analysis", "Análise corporal"),
    ("/blog/pt/", "Blog"),
    ("/about.html", "Sobre"),
]
PT_FOOTER = "© 2026 FITME. Todos os direitos reservados."
PT_CTA = dict(
    title="Quer descobrir o caimento ideal para o seu corpo?",
    sub="Informe altura, peso e cintura — receba análise corporal e recomendações personalizadas, grátis.",
    btn="Analisar meu corpo grátis →",
)


PT_POSTS = [
    {
        "n": 1,
        "slug": "como-se-vestir-tipo-de-corpo",
        "title": "Como Se Vestir para Cada Tipo de Corpo — Guia Completo | FITME",
        "desc": "Pera, ampulheta, retângulo, maçã, triângulo invertido: o guia completo de como se vestir para cada tipo de corpo. Análise corporal grátis em 60 segundos.",
        "tag": "TIPOS DE CORPO",
        "h1": "Como Se Vestir para Cada Tipo de Corpo",
        "meta_label": "16.05.2026 · Guia FITME de Estilo",
        "date": "2026-05-16",
        "thumb": "/blog/img/en/blog13-types-thumb-en.png",
        "thumb_alt": "Cinco tipos de corpo ilustrados — pera, ampulheta, retângulo, maçã, triângulo invertido",
        "card_title": "Como Se Vestir para Cada Tipo de Corpo",
        "card_desc": "Diagnóstico claro e roupas certas para os 5 tipos de corpo principais.",
        "body": dedent("""
  <h2>O que é tipo de corpo, na prática</h2>
  <p>Tipo de corpo não é peso, é <strong>proporção</strong>. Duas pessoas de 1,65 m e 60 kg podem ter cinturas, ombros e quadris totalmente diferentes — e por isso roupas que ficam incríveis em uma podem ficar péssimas na outra. O ponto de partida do estilo bem ajustado é parar de pensar em "tamanho" e começar a pensar em <strong>razão entre ombros, cintura e quadril</strong>.</p>
  <p>Neste guia organizamos os cinco tipos de corpo mais discutidos e mostramos quais peças, comprimentos e cores funcionam melhor para cada um — sem clichês.</p>

  <h2>1. Pera — quadril mais largo que os ombros</h2>
  <p>O tipo de corpo mais comum entre brasileiras. O objetivo do styling é <strong>chamar atenção para a parte superior</strong> e equilibrar o volume do quadril.</p>
  <p>Funciona: ombros estruturados (mangas bufantes, ombreiras suaves), decotes canoa e quadrado, blusas claras com calças escuras, calça reta ou flare em vez de skinny, blazer com cintura marcada.</p>
  <p>Evite: bolsos grandes na altura do quadril, calças com pregas largas na cintura, tons claros embaixo com blusa escura em cima.</p>
  <div class="tip">💡 Dica: cinto fino na cintura com vestido reto cria a curva visual sem exagerar a largura do quadril.</div>

  <h2>2. Triângulo invertido — ombros largos, quadril estreito</h2>
  <p>Comum em mulheres atléticas e em homens com biotipo "V". Meta: <strong>adicionar volume embaixo</strong> para equilibrar com os ombros largos.</p>
  <p>Funciona: calças wide leg, saia midi com pregas, decote V profundo, raglan que "corta" a linha do ombro, cores escuras em cima e claras embaixo.</p>
  <p>Evite: ombreiras pesadas, gola alta com manga bufante, regata muito fina que expõe o trapézio.</p>

  <h2>3. Ampulheta — ombros e quadril equilibrados, cintura definida</h2>
  <p>O tipo de corpo mais "fácil de vestir", mas com uma armadilha: <strong>peças oversized escondem o maior ativo, que é a cintura</strong>.</p>
  <p>Funciona: cintura alta sempre, malhas canelado, vestido envelope, jeans mom com blusa por dentro.</p>
  <p>Evite: vestido tubinho sem cintura, camisetão sem demarcação, jaqueta sem caimento.</p>

  <h2>4. Retângulo — ombros, cintura e quadril com larguras parecidas</h2>
  <p>Aparência limpa e moderna, mas exige peças que <strong>criem curva visual</strong>. Meta: marcar a cintura artificialmente.</p>
  <p>Funciona: peplum, cintos largos, blazer com cintura marcada, vestido com recorte na cintura, saia rodada.</p>
  <p>Evite: peças completamente retas em tecidos rígidos, modelagem oversized total, alfaiataria muito quadrada.</p>

  <h2>5. Maçã — volume na parte superior e abdômen</h2>
  <p>Volume concentrado no torso. Meta: <strong>levantar a linha visual da cintura</strong> e valorizar as pernas, que geralmente são finas neste biotipo.</p>
  <p>Funciona: cintura alta com calça reta ou wide, decote V para alongar o pescoço, sobreposições longas que cortam o tronco no comprimento, vestido empire (cintura logo abaixo do busto).</p>
  <p>Evite: cintos largos no meio do abdômen, calça com pregas que somam volume na barriga, regata com decote redondo curto.</p>

  <h2>Os 3 princípios que valem para qualquer tipo de corpo</h2>
  <p><strong>① Sempre verifique o ombro primeiro no provador.</strong> Se o ombro caiu, nada salva a peça. Comprimento e barra a gente ajusta; ombro mal posicionado, não.</p>
  <p><strong>② "Cabe" não é "fica bem".</strong> O zíper subir não significa que a silhueta ficou boa. O teste real é olhar no espelho a 2 metros de distância.</p>
  <p><strong>③ Confie em medidas reais, não em tamanho declarado.</strong> "M" varia até 10 cm de busto entre marcas. Anote as medidas das suas peças favoritas e compare com a tabela de medidas de qualquer outra marca antes de comprar.</p>

  <h2>Descubra seu tipo de corpo em 60 segundos</h2>
  <p>Adivinhar o tipo de corpo no espelho é difícil — quase ninguém acerta. O FITME usa altura, cintura e quadril para calcular o seu <strong>FITME DNA Score</strong> em um minuto. Você descobre não só o seu tipo de corpo, mas também os percentis exatos de WHR (cintura-quadril), proporção ombro-quadril e perna-tronco. Grátis e sem cadastro.</p>
"""),
        "related": [
            ("/blog/pt/corpo-pera-como-vestir", "Corpo Pera: Guia de Como se Vestir"),
            ("/blog/pt/whr-065-significado", "WHR 0,65 — O que significa e como vestir"),
            ("/blog/pt/guia-modelagem-calcas", "Guia Completo de Modelagem de Calças"),
            ("/blog/pt/como-parecer-mais-alta", "Como Parecer Mais Alta(o) — 5 truques"),
        ],
        "breadcrumb_post": "Como Se Vestir para Cada Tipo de Corpo",
    },
    {
        "n": 2,
        "slug": "corpo-pera-como-vestir",
        "title": "Corpo Pera: Guia Completo de Como Se Vestir | FITME",
        "desc": "Como se vestir para corpo pera: blusas, calças, vestidos e jaquetas que equilibram ombros e quadril. Análise corporal grátis em 60 segundos.",
        "tag": "CORPO PERA",
        "h1": "Corpo Pera — Como Se Vestir e Equilibrar a Silhueta",
        "meta_label": "16.05.2026 · Guia FITME por Tipo de Corpo",
        "date": "2026-05-16",
        "thumb": "/blog/img/en/blog18-pear-thumb-en.png",
        "thumb_alt": "Ilustração de corpo pera com sugestões de roupas",
        "card_title": "Corpo Pera: Guia de Como Se Vestir",
        "card_desc": "As peças que equilibram quadril largo e ombros mais estreitos.",
        "body": dedent("""
  <h2>O que é corpo pera, exatamente</h2>
  <p>Corpo pera (também chamado de "triângulo") é o biotipo em que <strong>o quadril é claramente mais largo que os ombros</strong>. É o tipo de corpo mais comum entre brasileiras adultas, e a confusão começa porque ele é frequentemente descrito como "problema" — quando, na verdade, é só uma proporção que pede um tipo de styling específico.</p>
  <p>O objetivo não é "esconder o quadril": é <strong>distribuir a atenção visual</strong> para que olhem o conjunto, não só a parte de baixo.</p>

  <h2>Parte de cima — volume e detalhes</h2>
  <p>Roupas que dão volume nos ombros equilibram a silhueta. Funcionam muito bem:</p>
  <p><strong>Mangas bufantes ou estruturadas</strong>: aumentam visualmente os ombros, neutralizando o quadril largo.<br><strong>Decote canoa e ombro a ombro</strong>: alargam a linha do pescoço/clavícula, criando paralelo com o quadril.<br><strong>Estampas e cores claras em cima</strong>: tons vivos chamam o olhar para o alto. Estampas com elementos pequenos funcionam melhor que estampas grandes.</p>
  <p>Evite raglan e decote V muito profundo — eles afinam a linha dos ombros e desequilibram ainda mais.</p>

  <h2>Parte de baixo — silhueta em linha reta</h2>
  <p>A regra é: <strong>quanto mais reto o caimento, melhor</strong>. Skinny é o pior inimigo do corpo pera porque expõe a diferença entre quadril e tornozelo. Calças retas, wide leg e bootcut suave são suas melhores opções. Sempre prefira tons escuros (preto, marinho, chumbo) por baixo.</p>
  <p>Jeans: cintura alta com modelagem reta é praticamente uniforme. Se quiser usar jeans claro, equilibre com blusa preta ou marinho.</p>
  <div class="tip">💡 Bolso traseiro grande no jeans aumenta visualmente o quadril. Para corpo pera, prefira bolsos médios e posicionados em ângulo.</div>

  <h2>Vestidos — o reinado do Aline e do envelope</h2>
  <p>Vestido evasê (linha A) é a peça perfeita para o corpo pera: aberto a partir do busto, o caimento não "agarra" o quadril e o olhar fica na parte superior. Vestido envelope (wrap dress) também é excelente — o decote em V chama atenção para o tronco e a amarração marca a cintura sem expor a largura do quadril.</p>
  <p>Vestido tubinho é o que mais falha para corpo pera porque acompanha exatamente a curva mais larga. Se gostar do estilo, use sempre com blazer estruturado por cima.</p>

  <h2>Jaquetas e blazers — o segredo do equilíbrio</h2>
  <p>Blazer com ombreira sutil é a peça mais poderosa que uma mulher com corpo pera pode ter. <strong>O blazer cria a impressão de ombros 4-6 cm mais largos</strong>, o que muda totalmente a percepção de proporção. Prefira blazer na altura do quadril (não muito longo, não muito curto) e com botão único na cintura para marcar a curva.</p>
  <p>Casacos longos: sempre com cinto. Casaco reto que cai liso até abaixo do quadril alarga ainda mais a parte de baixo.</p>

  <h2>Calcule sua medida exata</h2>
  <p>O corpo pera tem variação grande: algumas mulheres têm 8 cm de diferença entre ombro e quadril, outras 18 cm. O styling ideal muda conforme essa diferença. No FITME, em 60 segundos você descobre <strong>exatamente quantos centímetros de diferença você tem entre ombro e quadril</strong>, sua WHR (cintura-quadril) e em que percentil você está. Com esse número, comprar roupa deixa de ser tentativa e erro.</p>
"""),
        "related": [
            ("/blog/pt/como-se-vestir-tipo-de-corpo", "Como Se Vestir para Cada Tipo de Corpo"),
            ("/blog/pt/whr-065-significado", "WHR 0,65 — O que significa e como vestir"),
            ("/blog/pt/guia-modelagem-calcas", "Guia Completo de Modelagem de Calças"),
            ("/blog/pt/como-parecer-mais-alta", "Como Parecer Mais Alta(o) — 5 truques"),
        ],
        "breadcrumb_post": "Corpo Pera — Como Se Vestir e Equilibrar a Silhueta",
    },
    {
        "n": 3,
        "slug": "whr-065-significado",
        "title": "WHR 0,65 — O Que Significa e Como Vestir | FITME",
        "desc": "WHR 0,65 é o índice cintura-quadril considerado ideal cientificamente. Entenda o que significa, como medir o seu e como vestir. Cálculo grátis.",
        "tag": "WHR & PROPORÇÕES",
        "h1": "WHR 0,65 — O Que Significa e Como Vestir",
        "meta_label": "16.05.2026 · Ciência das Proporções FITME",
        "date": "2026-05-16",
        "thumb": "/blog/img/en/blog25-whr-thumb-en.png",
        "thumb_alt": "Diagrama de razão cintura-quadril com WHR 0,65 destacado",
        "card_title": "WHR 0,65 — O Que Significa e Como Vestir",
        "card_desc": "O número 0,65 explicado: ciência, medição e impacto no styling.",
        "body": dedent("""
  <h2>O que é WHR e por que 0,65 é tão citado</h2>
  <p>WHR (Waist-to-Hip Ratio) é a razão entre cintura e quadril, calculada simplesmente dividindo um pelo outro. Por exemplo, cintura 65 cm ÷ quadril 100 cm = <strong>0,65</strong>. Esse valor virou referência porque dezenas de estudos (Singh, 1993; Tovée et al., 2000; entre outros) mostram que <strong>WHR próximo de 0,65-0,70 é universalmente percebido como atraente em mulheres</strong>, em culturas e épocas muito diferentes.</p>
  <p>Importante: WHR não é uma sentença. É uma <strong>medida</strong>. Saber o seu permite escolher peças que valorizam a curva real, em vez de comprar baseado em "tamanho M" abstrato.</p>

  <h2>Como medir WHR corretamente</h2>
  <p><strong>Cintura</strong>: meça no ponto mais fino do tronco (geralmente 2 cm acima do umbigo). Não puxe nem solte a barriga; respire normal.<br><strong>Quadril</strong>: meça no ponto mais largo, geralmente na altura do "osso do quadril" ou um pouco abaixo, dependendo do biotipo.<br><strong>Divida</strong>: cintura ÷ quadril.</p>
  <p>WHR &lt; 0,75 em mulheres → forma curvilínea pronunciada.<br>WHR 0,75-0,85 → forma intermediária.<br>WHR &gt; 0,85 → forma mais retilínea (corpo "tubo" ou "maçã").</p>
  <div class="tip">💡 Não tem fita métrica? Use a largura da sua mão (do pulso à ponta do dedo médio) como unidade. A maioria das mulheres tem mão de ~16 cm.</div>

  <h2>Como vestir baseado no seu WHR</h2>
  <p><strong>WHR baixo (0,65-0,72)</strong>: cintura naturalmente marcada. Use peças que mostrem isso — vestido envelope, jeans cintura alta com blusa por dentro, blazer com botão na cintura. Cuidado com peças totalmente retas (tubinho sem corte, camisetão), que jogam fora a curva.</p>
  <p><strong>WHR médio (0,73-0,82)</strong>: equilíbrio sutil. Cinto fino ajuda; jeans cintura média (não muito alta) é mais confortável. Recortes verticais (zipper aparente, costuras) afinam visualmente.</p>
  <p><strong>WHR alto (&gt;0,83)</strong>: silhueta mais reta. Crie cintura artificial com peplum, vestido com cinturão largo, blazer com pences pronunciadas. Decotes V profundos e listras verticais também ajudam.</p>

  <h2>WHR não é o mesmo que peso</h2>
  <p>Você pode ter WHR 0,65 com 50 kg ou com 80 kg — é uma <strong>proporção</strong>, não um número absoluto. Por isso WHR é tão útil para escolher roupa: independe do quanto você pesa hoje.</p>

  <h2>Calcule seu WHR e proporções no FITME</h2>
  <p>No FITME, você insere cintura, quadril e altura. Em 60 segundos recebe seu WHR exato, o percentil global (onde você está em comparação com milhões de outras medições), e <strong>quais peças e cortes maximizam sua proporção</strong>. Tudo grátis, sem cadastro.</p>
"""),
        "related": [
            ("/blog/pt/como-se-vestir-tipo-de-corpo", "Como Se Vestir para Cada Tipo de Corpo"),
            ("/blog/pt/corpo-pera-como-vestir", "Corpo Pera — Como Se Vestir"),
            ("/blog/pt/guia-modelagem-calcas", "Guia Completo de Modelagem de Calças"),
            ("/blog/pt/como-parecer-mais-alta", "Como Parecer Mais Alta(o)"),
        ],
        "breadcrumb_post": "WHR 0,65 — O Que Significa e Como Vestir",
    },
    {
        "n": 4,
        "slug": "guia-modelagem-calcas",
        "title": "Guia Completo de Modelagem de Calças: Skinny, Reta, Wide, Tapered | FITME",
        "desc": "Skinny, reta, wide leg ou tapered: o guia completo de modelagem de calças para cada tipo de corpo e cada sapato. Comprimentos, barras e ajustes.",
        "tag": "GUIA DE CALÇAS",
        "h1": "Guia Completo de Modelagem de Calças",
        "meta_label": "16.05.2026 · Guia FITME de Estilo",
        "date": "2026-05-16",
        "thumb": "/blog/img/en/blog1-pants-thumb-en.png",
        "thumb_alt": "Comparação dos 4 tipos de modelagem de calça: skinny, reta, wide e tapered",
        "card_title": "Guia Completo de Modelagem de Calças",
        "card_desc": "Como escolher entre skinny, reta, wide ou tapered para seu corpo.",
        "body": dedent("""
  <h2>A calça certa muda completamente o look</h2>
  <p>Você pode usar a mesma blusa com 4 modelagens de calça diferentes e parecer 4 pessoas distintas. <strong>Modelagem é mais importante que tamanho</strong>: é ela que define a silhueta, alonga ou encurta a perna, equilibra ou desequilibra a proporção. Neste guia, as 4 modelagens principais com as combinações de corpo e sapato que funcionam.</p>

  <h2>1. Skinny — para silhuetas que querem alongar a perna</h2>
  <p>Caimento justo do quadril ao tornozelo. Funciona bem para quem tem <strong>pernas finas e quer evidenciar a linha</strong>. Para corpo pera, esquece — escancara a diferença entre quadril e tornozelo. Sapato ideal: tênis baixo, ankle boot, scarpin de bico fino.</p>

  <h2>2. Reta — a modelagem mais democrática</h2>
  <p>Largura constante do quadril à barra. <strong>Funciona em praticamente qualquer biotipo</strong>, especialmente para quem tem coxa grossa. Se sua coxa é forte, suba meio número para evitar repuxe. Sapato: loafer, oxford, tênis, ankle boot.</p>

  <h2>3. Wide Leg — a tendência dominante desde 2024</h2>
  <p>Caimento largo do quadril até a barra. Cria silhueta editorial e moderna. <strong>Exige blusa por dentro</strong> ou cropped — se usar com camisetão por fora, a silhueta colapsa. O tecido importa muito: prefira tecidos com corpo (alfaiataria de lã, linho misto, algodão estruturado). Jersey leve em wide leg cai pesado e amassa rápido.</p>
  <div class="tip">💡 Para wide leg, teste o "meio por dentro": coloque só a parte da frente da blusa por dentro. Marca cintura sem ficar formal demais.</div>

  <h2>4. Tapered — o coringa entre conforto e elegância</h2>
  <p>Mais larga na coxa, afina do joelho à barra. <strong>A melhor opção para quem tem coxa cheia mas quer caimento elegante</strong>. Funciona em situações mais formais onde a skinny seria casual demais. Combine com loafer, mocassim ou tênis branco minimalista.</p>

  <h2>Comprimento — o detalhe que define tudo</h2>
  <p><strong>Com tênis</strong>: comprimento "cropped" mostrando o tornozelo é o mais limpo.<br><strong>Com loafer/oxford</strong>: deixe encostar levemente na parte de cima do sapato.<br><strong>Com bota</strong>: "stacked length" — pequeno acúmulo de tecido em cima da bota.</p>
  <p>Na dúvida, <strong>vai de mais curto</strong>. Curto demais parece intencional, longo demais parece descuido. E barra é o ajuste mais barato em qualquer costureira — vale absolutamente a pena.</p>

  <h2>Encontre a modelagem ideal para o seu corpo</h2>
  <p>A "calça perfeita" depende da relação entre cintura, quadril e altura de cavalo. O FITME calcula essas três proporções em 60 segundos e te diz, com base em milhares de outras silhuetas similares, <strong>quais modelagens têm maior probabilidade de funcionar no seu corpo</strong>. Análise grátis, sem cadastro.</p>
"""),
        "related": [
            ("/blog/pt/como-se-vestir-tipo-de-corpo", "Como Se Vestir para Cada Tipo de Corpo"),
            ("/blog/pt/corpo-pera-como-vestir", "Corpo Pera — Como Se Vestir"),
            ("/blog/pt/whr-065-significado", "WHR 0,65 — O que significa"),
            ("/blog/pt/como-parecer-mais-alta", "Como Parecer Mais Alta(o)"),
        ],
        "breadcrumb_post": "Guia Completo de Modelagem de Calças",
    },
    {
        "n": 5,
        "slug": "como-parecer-mais-alta",
        "title": "Como Parecer Mais Alta(o): 5 Truques que Adicionam até 5 cm | FITME",
        "desc": "Cinco truques de styling que adicionam até 5 cm visualmente. Cintura alta, monocromia, comprimento certo da calça e mais. Para homens e mulheres.",
        "tag": "ALONGAR A SILHUETA",
        "h1": "Como Parecer Mais Alta(o) — 5 Truques de Styling",
        "meta_label": "16.05.2026 · Guia FITME de Estilo",
        "date": "2026-05-16",
        "thumb": "/blog/img/en/blog10-leg-thumb-en.png",
        "thumb_alt": "Comparação visual: roupas que alongam vs roupas que encurtam a silhueta",
        "card_title": "Como Parecer Mais Alta(o) — 5 Truques",
        "card_desc": "Cinco truques de styling que adicionam até 5 cm visualmente.",
        "body": dedent("""
  <h2>Por que styling tem mais impacto que sapato</h2>
  <p>Salto adiciona altura real, mas styling adiciona <strong>altura percebida</strong> — e os dois efeitos somam. Um look monocromático pode acrescentar 4-5 cm visuais sem ajuda nenhuma de salto. Cinco truques específicos, baseados em como o cérebro humano lê linhas verticais e contraste:</p>

  <h2>1. Cintura alta sempre</h2>
  <p>A peça mais simples e a mais subestimada. Calça cintura alta <strong>move o ponto de início visual da perna para mais perto do umbigo</strong>, fazendo a perna parecer começar antes. Para quem tem tronco longo e perna curta, esse efeito sozinho transforma a proporção. Funciona em jeans, alfaiataria, saia.</p>

  <h2>2. Monocromia vertical</h2>
  <p>Vestir tudo na mesma cor (especialmente tons escuros) cria uma <strong>linha visual ininterrupta</strong> do ombro ao pé. Cores diferentes em cima e embaixo "cortam" a silhueta na cintura, encurtando ambas as metades. Look all-black, all-navy ou all-tom-terroso é o mais alongador que existe.</p>
  <div class="tip">💡 Se não quer monocromia total, use o sapato na mesma cor da calça. Continua o efeito de linha visual contínua até o chão.</div>

  <h2>3. Comprimento certo da calça</h2>
  <p>Calça com barra arrastando no chão encurta visualmente. Calça acima do tornozelo (cropped) <strong>mostra um pouco da perna</strong> e adiciona alongamento. Para qualquer tipo de calça, ajustar a barra para cair exatamente no osso do tornozelo (ou ligeiramente acima) é a melhor regra.</p>

  <h2>4. Decote V e linhas diagonais</h2>
  <p>Decote V profundo <strong>alonga o pescoço visualmente</strong> e cria uma linha diagonal que distrai o olhar de "altura horizontal". Mesma lógica vale para blazer aberto, lapela larga e cardigan aberto.</p>

  <h2>5. Sapato bico afilado, mesma cor da perna</h2>
  <p>Bico fino continua a linha visual da perna além do tornozelo. Combinado com sapato na cor da calça ou da meia (look "pernoneck"), pode adicionar 3-4 cm percebidos.</p>

  <h2>O que <strong>evitar</strong> se quer parecer mais alta(o)</h2>
  <p>1. Listras horizontais largas. 2. Cinto largo de cor contrastante. 3. Calça muito longa com pé "comendo" o sapato. 4. Botas com cano que termina no meio da panturrilha. 5. Camisetão por fora da calça que esconde a cintura alta.</p>

  <h2>Saiba qual sua proporção perna-tronco</h2>
  <p>O quanto cada truque funciona em você depende da sua razão perna-tronco. No FITME, em 60 segundos, você descobre se seu tronco é proporcionalmente longo ou curto em relação à perna — e quais ajustes de styling têm o maior efeito específico no seu corpo. Grátis, sem cadastro.</p>
"""),
        "related": [
            ("/blog/pt/como-se-vestir-tipo-de-corpo", "Como Se Vestir para Cada Tipo de Corpo"),
            ("/blog/pt/corpo-pera-como-vestir", "Corpo Pera — Como Se Vestir"),
            ("/blog/pt/whr-065-significado", "WHR 0,65 — O que significa"),
            ("/blog/pt/guia-modelagem-calcas", "Guia Completo de Modelagem de Calças"),
        ],
        "breadcrumb_post": "Como Parecer Mais Alta(o) — 5 Truques de Styling",
    },
]


# -------------------- Build --------------------

def build_lang(lang: str, locale_code: str, posts: list[dict],
               nav: list[tuple[str, str]], footer: str, cta: dict,
               index_meta: dict, header_nav_for_other_lang: list[tuple[str, str]]):
    out_dir = ROOT / "blog" / lang
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for post in posts:
        slug = post["slug"]
        other_alts = {
            "en": f"{SITE}/blog/{post.get('en_canonical_slug', '')}"
            if post.get("en_canonical_slug")
            else None,
            lang: f"{SITE}/blog/{lang}/{slug}",
            "x-default": f"{SITE}/blog/blog{post['n']}-en",
        }
        hreflang_alts = {k: v for k, v in other_alts.items() if v}
        html = page(
            lang=lang, locale_code=locale_code, slug=slug,
            title=post["title"], desc=post["desc"], tag=post["tag"],
            h1=post["h1"], meta_label=post["meta_label"], date=post["date"],
            hreflang_alts=hreflang_alts, thumb_path=post["thumb"],
            thumb_alt=post["thumb_alt"], body_html=post["body"],
            related=post["related"], cta_title=cta["title"],
            cta_sub=cta["sub"], cta_btn=cta["btn"],
            breadcrumb_home="Home", breadcrumb_blog=index_meta["section_label"],
            breadcrumb_post=post["breadcrumb_post"],
            header_nav=nav, footer_text=footer,
        )
        path = out_dir / f"{slug}.html"
        path.write_text(html, encoding="utf-8")
        written.append(path.relative_to(ROOT))

    idx_html = index_page(
        lang=lang, locale_code=locale_code,
        title=index_meta["title"], desc=index_meta["desc"],
        page_title=index_meta["page_title"], page_sub=index_meta["page_sub"],
        posts=posts, header_nav=nav, footer_text=footer,
        section_label=index_meta["section_label"],
        other_lang_links=index_meta["other_lang_links"],
    )
    (out_dir / "index.html").write_text(idx_html, encoding="utf-8")
    written.append((out_dir / "index.html").relative_to(ROOT))
    return written


def main():
    jp_index_meta = {
        "title": "FITMEブログ — 体型・スタイリング完全ガイド | FITME",
        "desc": "体型診断、パンツの選び方、ゴールデンレシオ、洋ナシ体型のコーディネートなど、データで導く着こなしガイド。",
        "page_title": "FITME ブログ",
        "page_sub": "比率データで導く、失敗しない着こなしガイド",
        "section_label": "最新記事",
        "other_lang_links": [
            ("/blog/", "한국어"),
            ("/blog/", "English"),
            ("/blog/pt/", "Português"),
        ],
    }
    pt_index_meta = {
        "title": "FITME Blog — Guia de Tipos de Corpo e Estilo | FITME",
        "desc": "Guias de tipos de corpo, modelagens de calça, WHR, corpo pera e como parecer mais alta(o) — baseados em dados de proporção corporal.",
        "page_title": "FITME Blog",
        "page_sub": "Guias de estilo baseados em dados reais de proporção corporal",
        "section_label": "Últimos artigos",
        "other_lang_links": [
            ("/blog/", "한국어"),
            ("/blog/", "English"),
            ("/blog/ja/", "日本語"),
        ],
    }

    jp_files = build_lang("ja", "ja", JP_POSTS, JP_NAV, JP_FOOTER, JP_CTA, jp_index_meta, JP_NAV)
    pt_files = build_lang("pt", "pt-BR", PT_POSTS, PT_NAV, PT_FOOTER, PT_CTA, pt_index_meta, PT_NAV)

    print(f"JP wrote {len(jp_files)} files:")
    for f in jp_files:
        print(f"  {f}")
    print(f"PT wrote {len(pt_files)} files:")
    for f in pt_files:
        print(f"  {f}")


if __name__ == "__main__":
    main()
