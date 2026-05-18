#!/usr/bin/env python3
"""Add JA/PT localized posts for EN blog6–blog9 topics; rebuild ja/pt indexes."""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://perfectfitme.com"

spec = importlib.util.spec_from_file_location(
    "mb", ROOT / "tools" / "build-multilang-blog.py"
)
mb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mb)

JP_EXTRA = [
    {
        "ko_slug": "blog6",
        "en_slug": "blog6-en",
        "pt_slug": "guarda-roupa-capsula-5-pecas",
        "slug": "capsule-5-basics",
        "title": "週5着が回る！5つの基本服カプセル｜FITME",
        "desc": "白T・黒スラックス・デニムジャケット・チノ・ワイドデニムの5点で7コーデ。体型比率に合わせた選び方。",
        "tag": "CAPSULE WARDROBE",
        "h1": "5つの基本服で1週間コーデ",
        "meta_label": "2026.05.18 · FITME スタイルガイド",
        "date": "2026-05-18",
        "thumb": "/blog/img/en/blog6-basics-thumb-en.png",
        "thumb_alt": "週間コーデ用の基本ワードローブ",
        "card_title": "5つの基本服で1週間コーデ",
        "card_desc": "少ない点数で最大の組み合わせ — 比率に合わせた5点選び。",
        "breadcrumb_post": "5つの基本服で1週間コーデ",
        "body": dedent("""
  <h2>なぜ5点で足りるのか</h2>
  <p>カプセルワードローブの核心は <strong>相互互換性</strong> です。白T、黒ストレートパンツ、デニムジャケット、ベージュチノ、ライトインディゴのワイドデニム — この5点は互いに3着以上と組み合わせ可能。スニーカーとローファー2足で月〜金の印象を変えられます。</p>
  <h2>体型別の注意点</h2>
  <p>洋ナシ型は下をダークトーン、上に構造（肩パッド・ボートネック）を。逆三角型はワイドパンツで下半身にボリューム。胴長型はハイライズとインスタイルで脚の開始位置を上げる。</p>
  <div class="tip">💡 基本服は肩の縫い目が正しいか最初に確認。丈とウエストは後から直せます。</div>
  <h2>FITMEで比率を把握</h2>
  <p>身長・ウエスト・ヒップから肩幅・脚比率を60秒で推定。自分に合うシルエットを無料で確認できます。</p>
"""),
        "related": [
            ("/blog/ja/pants-fit-guide", "パンツのシルエット完全ガイド"),
            ("/blog/ja/taikei-fuku-erabikata", "体型別の服の選び方"),
            ("/blog/ja/golden-ratio-fuku", "ゴールデンレシオで似合う服"),
        ],
    },
    {
        "ko_slug": "blog7",
        "en_slug": "blog7-en",
        "pt_slug": "proporcao-importa-mais-que-peso",
        "slug": "proportion-not-weight",
        "title": "体重より体型比率が大事な理由｜FITME",
        "desc": "同じ体重でも見え方は正反対。肩・腰・脚の比率が服の似合わせを決める。",
        "tag": "PROPORTION SCIENCE",
        "h1": "体重より体型比率が服の似合わせを決める",
        "meta_label": "2026.05.18 · FITME スタイルガイド",
        "date": "2026-05-18",
        "thumb": "/blog/img/en/blog7-proportion-thumb-en.png",
        "thumb_alt": "体型比率と体重の比較",
        "card_title": "体重より体型比率",
        "card_desc": "BMIではなくSHR・WHR・脚比率で選ぶ。",
        "breadcrumb_post": "体重より体型比率",
        "body": dedent("""
  <h2>体重計の落とし穴</h2>
  <p>同じ身長・体重でも、肩幅対ヒップ、脚対胴の比率が違えば似合う服は真逆です。<strong>比率こそがシルエットの設計図</strong> です。</p>
  <h2>測るべき3つの比率</h2>
  <p>① 肩幅÷ヒップ（SHR）② ウエスト÷ヒップ（WHR）③ 股下÷身長（脚比率）。この3つでトップスの肩選び、ボトムスのライズ、丈が決まります。</p>
  <div class="tip">💡 3〜6ヶ月ごとに再計測。筋トレや体重変化で比率は動きます。</div>
"""),
        "related": [
            ("/blog/ja/find-body-type-data", "データで体型を見つける"),
            ("/blog/ja/golden-ratio-fuku", "ゴールデンレシオ"),
        ],
    },
    {
        "ko_slug": "blog8",
        "en_slug": "blog8-en",
        "pt_slug": "whr-e-caimento",
        "slug": "whr-clothing-fit",
        "title": "WHR（ウエストヒップ比）と服のフィット｜FITME",
        "desc": "ウエスト÷ヒップの数字が、パンツとトップスのサイズ選びを左右する。測り方とスタイル別対策。",
        "tag": "WHR GUIDE",
        "h1": "WHRと服のフィットの関係",
        "meta_label": "2026.05.18 · FITME ガイド",
        "date": "2026-05-18",
        "thumb": "/blog/img/en/blog8-whr-thumb-en.png",
        "thumb_alt": "ウエストヒップ比の図解",
        "card_title": "WHRと服のフィット",
        "card_desc": "低WHR・高WHRそれぞれの選び方。",
        "breadcrumb_post": "WHRと服のフィット",
        "body": dedent("""
  <h2>WHRとは</h2>
  <p>最細ウエスト÷最大ヒップ。例：ウエスト68cm÷ヒップ95cm≒0.72。この1数字が、既製服のパターンとのズレを説明します。</p>
  <h2>レンジ別スタイル</h2>
  <p><strong>0.65–0.75</strong>：ウエストマークが効く — ベルト、タックイン、ラップ。<br><strong>0.75–0.85</strong>：最も汎用。<br><strong>0.85+</strong>：ハイウエスト、Aライン、色の縦割りでウエストを作る。</p>
  <div class="tip">💡 ヒップに合わせてサイズを取り、ウエストは補正が定番。</div>
"""),
        "related": [
            ("/blog/ja/golden-ratio-fuku", "ゴールデンレシオ"),
            ("/blog/ja/pear-styling", "洋ナシ体型ガイド"),
        ],
    },
    {
        "ko_slug": "blog9",
        "en_slug": "blog9-en",
        "pt_slug": "ombro-e-caimento",
        "slug": "shoulder-fit-guide",
        "title": "肩幅が服全体の印象を決める｜FITME",
        "desc": "肩の縫い目は直せない。アクロミオンに合わせてから胸・ウエストを見る。",
        "tag": "SHOULDER FIT",
        "h1": "肩幅と服のフィット",
        "meta_label": "2026.05.18 · FITME ガイド",
        "date": "2026-05-18",
        "thumb": "/blog/img/en/blog9-shoulder-thumb-en.png",
        "thumb_alt": "肩幅測定とスタイリング",
        "card_title": "肩幅と服のフィット",
        "card_desc": "肩の縫い目を最優先に選ぶ。",
        "breadcrumb_post": "肩幅と服のフィット",
        "body": dedent("""
  <h2>肩がアンカー</h2>
  <p>ジャケットもTも、肩の縫い目が肩峰（アクロミオン）から外れると全体が崩れます。<strong>肩が合えば袖・胴は直せる</strong> — 逆はほぼ不可能です。</p>
  <h2>肩幅別の選び方</h2>
  <p>広肩：Vネック・ラグラン。狭肩：構築的ブレザー・ボートネック。標準：ほぼ全シルエット可。</p>
  <div class="tip">💡 オンラインはサイズ表の「肩」列を最初に比較。</div>
"""),
        "related": [
            ("/blog/ja/pants-fit-guide", "パンツガイド"),
            ("/blog/ja/taikei-fuku-erabikata", "体型別ガイド"),
        ],
    },
]

PT_EXTRA = [
    {
        "ko_slug": "blog6",
        "en_slug": "blog6-en",
        "ja_slug": "capsule-5-basics",
        "slug": "guarda-roupa-capsula-5-pecas",
        "title": "5 Peças Básicas = 7 Looks na Semana | FITME",
        "desc": "Camiseta branca, calça preta, jaqueta jeans, chino e jeans wide — monte a semana com duas sapatilhas.",
        "tag": "GUARDA-ROUPA CÁPSULA",
        "h1": "5 Básicos para uma Semana Inteira",
        "meta_label": "18.05.2026 · Guia FITME",
        "date": "2026-05-18",
        "thumb": "/blog/img/en/blog6-basics-thumb-en.png",
        "thumb_alt": "Peças básicas para coordenação semanal",
        "card_title": "5 Básicos = 7 Looks",
        "card_desc": "Menos peças, mais combinações — escolha por proporção.",
        "breadcrumb_post": "5 Básicos para uma Semana Inteira",
        "body": dedent("""
  <h2>Por que 5 peças bastam</h2>
  <p>O segredo é <strong>compatibilidade cruzada</strong>: cada peça combina com pelo menos três outras. Com tênis branco e loafer preto, você cobre a semana sem repetir a mesma silhueta.</p>
  <h2>Proporção importa</h2>
  <p>Corpo pera: parte de baixo escura, parte de cima com estrutura. Ombros largos: calça wide ou flare. Tronco longo: cintura alta e top por dentro.</p>
  <div class="tip">💡 Sempre teste o ombro primeiro no provador. Barra e cintura o alfaiate resolve.</div>
"""),
        "related": [
            ("/blog/pt/guia-modelagem-calcas", "Guia de Calças"),
            ("/blog/pt/como-se-vestir-tipo-de-corpo", "Tipos de Corpo"),
        ],
    },
    {
        "ko_slug": "blog7",
        "en_slug": "blog7-en",
        "ja_slug": "proportion-not-weight",
        "slug": "proporcao-importa-mais-que-peso",
        "title": "Proporção Corporal Importa Mais que Peso | FITME",
        "desc": "Mesmo peso, silhuetas opostas. Ombro, cintura, quadril e perna definem o caimento.",
        "tag": "PROPORÇÕES",
        "h1": "Proporção vs Peso na Hora de Vestir",
        "meta_label": "18.05.2026 · Guia FITME",
        "date": "2026-05-18",
        "thumb": "/blog/img/en/blog7-proportion-thumb-en.png",
        "thumb_alt": "Proporção corporal vs peso",
        "card_title": "Proporção vs Peso",
        "card_desc": "SHR, WHR e perna-tronco guiam suas compras.",
        "breadcrumb_post": "Proporção vs Peso",
        "body": dedent("""
  <h2>A armadilha da balança</h2>
  <p>Duas pessoas com o mesmo peso podem precisar de silhuetas totalmente diferentes. <strong>Proporção é o mapa</strong> — peso é só um ponto no mapa.</p>
  <h2>Três razões essenciais</h2>
  <p>Ombro÷quadril (SHR), cintura÷quadril (WHR), entreperna÷altura. Com esses números você prevê onde a roupa vai falhar antes de comprar online.</p>
"""),
        "related": [
            ("/blog/pt/como-se-vestir-tipo-de-corpo", "Tipos de Corpo"),
            ("/blog/pt/whr-065-significado", "WHR 0,65"),
        ],
    },
    {
        "ko_slug": "blog8",
        "en_slug": "blog8-en",
        "ja_slug": "whr-clothing-fit",
        "slug": "whr-e-caimento",
        "title": "WHR e Caimento de Roupas | FITME",
        "desc": "Cintura÷quadril explica por que a calça fecha no quadril e folga na cintura. Como medir e vestir.",
        "tag": "WHR",
        "h1": "WHR e o Caimento das Roupas",
        "meta_label": "18.05.2026 · Guia FITME",
        "date": "2026-05-18",
        "thumb": "/blog/img/en/blog8-whr-thumb-en.png",
        "thumb_alt": "Razão cintura-quadril",
        "card_title": "WHR e Caimento",
        "card_desc": "Estratégias para WHR baixo e alto.",
        "breadcrumb_post": "WHR e Caimento",
        "body": dedent("""
  <h2>O que é WHR</h2>
  <p>Cintura no ponto mais fino ÷ quadril no ponto mais largo. A maioria das calças prontas assume um WHR médio — fora disso, ou aperta no quadril ou sobra na cintura.</p>
  <h2>Como vestir</h2>
  <p>WHR baixo: cintura marcada, cinto, vestido envelope. WHR alto: cintura alta, linha A, blocos de cor vertical.</p>
  <div class="tip">💡 Compre pelo quadril, ajuste a cintura no alfaiate.</div>
"""),
        "related": [
            ("/blog/pt/whr-065-significado", "WHR 0,65 — significado"),
            ("/blog/pt/corpo-pera-como-vestir", "Corpo Pera"),
        ],
    },
    {
        "ko_slug": "blog9",
        "en_slug": "blog9-en",
        "ja_slug": "shoulder-fit-guide",
        "slug": "ombro-e-caimento",
        "title": "Largura dos Ombros Define o Look | FITME",
        "desc": "A costura do ombro deve cair no acrômio. Ombro errado não conserta — troque o tamanho.",
        "tag": "OMBROS",
        "h1": "Ombro: A Base de Toda Blusa",
        "meta_label": "18.05.2026 · Guia FITME",
        "date": "2026-05-18",
        "thumb": "/blog/img/en/blog9-shoulder-thumb-en.png",
        "thumb_alt": "Medição de ombros",
        "card_title": "Ombro e Caimento",
        "card_desc": "Priorize ombro antes do peito.",
        "breadcrumb_post": "Ombro: A Base de Toda Blusa",
        "body": dedent("""
  <h2>Ombro é a âncora</h2>
  <p>Se a costura passa do ombro, nada fica certo. <strong>Compre pelo ombro</strong>; peito e cintura o alfaiate ajusta.</p>
  <h2>Por tipo de ombro</h2>
  <p>Ombros largos: decote V, raglan. Ombros estreitos: blazer estruturado, gola barco. Médios: quase tudo funciona.</p>
"""),
        "related": [
            ("/blog/pt/guia-modelagem-calcas", "Guia de Calças"),
            ("/blog/pt/como-parecer-mais-alta", "Parecer Mais Alta"),
        ],
    },
]


def fix_body_typos(html: str) -> str:
    return html.replace('<motion class="tip">', '<div class="tip">')


EDITORIAL_JA = (
    '<p style="font-size:13px;color:var(--muted);margin-top:28px;">'
    "編集：FITME · <a href=\"/about.html\" style=\"color:var(--accent);\">運営</a> · "
    "<a href=\"/editorial-standards.html\" style=\"color:var(--accent);\">コンテンツ基準</a> · "
    "<a href=\"/how-it-works.html\" style=\"color:var(--accent);\">ツールの仕組み</a></p>"
)
EDITORIAL_PT = (
    '<p style="font-size:13px;color:var(--muted);margin-top:28px;">'
    'Editorial FITME · <a href="/about.html" style="color:var(--accent);">Sobre</a> · '
    '<a href="/editorial-standards.html" style="color:var(--accent);">Padrões</a> · '
    '<a href="/how-it-works.html" style="color:var(--accent);">Como funciona</a></p>'
)

_tce_spec = importlib.util.spec_from_file_location(
    "tce", ROOT / "tools" / "thin_content_expand.py"
)
tce = importlib.util.module_from_spec(_tce_spec)
_tce_spec.loader.exec_module(tce)

EXPAND_JA = {
    k: fix_body_typos(v) + EDITORIAL_JA for k, v in tce.THIN_JA.items()
}
EXPAND_PT = {
    k: fix_body_typos(v) + EDITORIAL_PT for k, v in tce.THIN_PT.items()
}

def apply_expansions(posts: list, expansions: dict) -> list:
    return [
        {**post, "body": expansions[post["slug"]]}
        if post["slug"] in expansions
        else post
        for post in posts
    ]


def write_posts(lang: str, locale: str, posts: list, nav, footer, cta, index_meta):
    for post in posts:
        slug = post["slug"]
        html = mb.page(
            lang=lang,
            locale_code=locale,
            slug=slug,
            title=post["title"],
            desc=post["desc"],
            tag=post["tag"],
            h1=post["h1"],
            meta_label=post["meta_label"],
            date=post["date"],
            hreflang_alts=mb.hreflang_alts_for(lang, slug, post),
            thumb_path=post["thumb"],
            thumb_alt=post["thumb_alt"],
            body_html=fix_body_typos(post["body"]),
            related=post["related"],
            cta_title=cta["title"],
            cta_sub=cta["sub"],
            cta_btn=cta["btn"],
            breadcrumb_home="Home",
            breadcrumb_blog=index_meta["section_label"],
            breadcrumb_post=post["breadcrumb_post"],
            header_nav=nav,
            footer_text=footer,
        )
        out = ROOT / "blog" / lang / f"{slug}.html"
        out.write_text(html, encoding="utf-8")
        print(f"  wrote {out.relative_to(ROOT)}")


def rebuild_index(lang: str, locale: str, all_posts: list, nav, footer, index_meta):
    idx = mb.index_page(
        lang=lang,
        locale_code=locale,
        title=index_meta["title"],
        desc=index_meta["desc"],
        page_title=index_meta["page_title"],
        page_sub=index_meta["page_sub"],
        posts=all_posts,
        header_nav=nav,
        footer_text=footer,
        section_label=index_meta["section_label"],
        other_lang_links=index_meta["other_lang_links"],
        site_about_html=mb.SITE_ABOUT_HTML.get(lang, ""),
    )
    path = ROOT / "blog" / lang / "index.html"
    path.write_text(idx, encoding="utf-8")
    print(f"  rebuilt {path.relative_to(ROOT)}")


def patch_sitemap():
    raw = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    pairs = [
        (6, "capsule-5-basics", "guarda-roupa-capsula-5-pecas"),
        (7, "proportion-not-weight", "proporcao-importa-mais-que-peso"),
        (8, "whr-clothing-fit", "whr-e-caimento"),
        (9, "shoulder-fit-guide", "ombro-e-caimento"),
    ]
    for n, ja_slug, pt_slug in pairs:
        for variant in (f"blog{n}", f"blog{n}-en"):
            pat = re.compile(
                r"(<url>\s*<loc>https://perfectfitme\.com/blog/"
                + re.escape(variant)
                + r"</loc>.*?</url>)",
                re.DOTALL,
            )
            m = pat.search(raw)
            if not m:
                continue
            block = m.group(1)
            new_block = block
            ja_url = f"{SITE}/blog/ja/{ja_slug}"
            pt_url = f"{SITE}/blog/pt/{pt_slug}"
            if f'hreflang="ja"' not in new_block:
                new_block = new_block.replace(
                    "</url>",
                    f'\n    <xhtml:link rel="alternate" hreflang="ja" href="{ja_url}"/>\n  </url>',
                )
            if f'hreflang="pt-BR"' not in new_block:
                new_block = new_block.replace(
                    "</url>",
                    f'\n    <xhtml:link rel="alternate" hreflang="pt-BR" href="{pt_url}"/>\n  </url>',
                )
            if new_block != block:
                raw = raw.replace(block, new_block, 1)
        for lang, slug in (("ja", ja_slug), ("pt", pt_slug)):
            loc = f"{SITE}/blog/{lang}/{slug}"
            if loc in raw:
                continue
            alts = {
                "ko": f"{SITE}/blog/blog{n}",
                "en": f"{SITE}/blog/blog{n}-en",
                "ja": f"{SITE}/blog/ja/{ja_slug}",
                "pt-BR": f"{SITE}/blog/pt/{pt_slug}",
                "x-default": f"{SITE}/blog/blog{n}-en",
            }
            alt_lines = "\n".join(
                f'    <xhtml:link rel="alternate" hreflang="{h}" href="{u}"/>'
                for h, u in alts.items()
                if h == lang or h in ("ko", "en", "x-default") or (h == "pt-BR" and lang == "pt")
            )
            # build proper chain
            chain = {
                "ko": f"{SITE}/blog/blog{n}",
                "en": f"{SITE}/blog/blog{n}-en",
                "x-default": f"{SITE}/blog/blog{n}-en",
            }
            chain["ja"] = f"{SITE}/blog/ja/{ja_slug}"
            chain["pt-BR"] = f"{SITE}/blog/pt/{pt_slug}"
            alt_lines = "\n".join(
                f'    <xhtml:link rel="alternate" hreflang="{h}" href="{u}"/>'
                for h, u in chain.items()
            )
            block = (
                f"  <url>\n    <loc>{loc}</loc>\n"
                f"    <lastmod>2026-05-18</lastmod>\n"
                f"    <changefreq>monthly</changefreq>\n"
                f"    <priority>0.7</priority>\n"
                f"{alt_lines}\n  </url>"
            )
            raw = raw.replace("</urlset>", block + "\n</urlset>")
    (ROOT / "sitemap.xml").write_text(raw, encoding="utf-8")
    print("  patched sitemap.xml")


def main():
    print("JP extra posts:")
    write_posts("ja", "ja", apply_expansions(JP_EXTRA, EXPAND_JA), mb.JP_NAV, mb.JP_FOOTER, mb.JP_CTA, {
        "title": "FITMEブログ — 体型・スタイリング完全ガイド | FITME",
        "desc": "体型診断、パンツ、カプセル、WHR、肩幅まで。データで導く着こなし。",
        "page_title": "FITME ブログ",
        "page_sub": "比率データで導く、失敗しない着こなしガイド",
        "section_label": "最新記事",
        "other_lang_links": [
            ("/blog/", "한국어"),
            ("/blog/", "English"),
            ("/blog/pt/", "Português"),
        ],
    })
    rebuild_index("ja", "ja", mb.JP_POSTS + JP_EXTRA, mb.JP_NAV, mb.JP_FOOTER, {
        "title": "FITMEブログ — 体型・スタイリング完全ガイド | FITME",
        "desc": "体型診断、パンツ、カプセル、WHR、肩幅まで。",
        "page_title": "FITME ブログ",
        "page_sub": "比率データで導く、失敗しない着こなしガイド",
        "section_label": "最新記事",
        "other_lang_links": [
            ("/blog/", "한국어"),
            ("/blog/", "English"),
            ("/blog/pt/", "Português"),
        ],
    })

    print("PT extra posts:")
    write_posts("pt", "pt-BR", apply_expansions(PT_EXTRA, EXPAND_PT), mb.PT_NAV, mb.PT_FOOTER, mb.PT_CTA, {
        "title": "FITME Blog — Guia de Tipos de Corpo e Estilo | FITME",
        "desc": "Cápsula, proporções, WHR e ombros — guias em português.",
        "page_title": "FITME Blog",
        "page_sub": "Guias de estilo baseados em proporção corporal",
        "section_label": "Últimos artigos",
        "other_lang_links": [
            ("/blog/", "한국어"),
            ("/blog/", "English"),
            ("/blog/ja/", "日本語"),
        ],
    })
    rebuild_index("pt", "pt-BR", mb.PT_POSTS + PT_EXTRA, mb.PT_NAV, mb.PT_FOOTER, {
        "title": "FITME Blog — Guia de Tipos de Corpo e Estilo | FITME",
        "desc": "Cápsula, proporções, WHR e ombros.",
        "page_title": "FITME Blog",
        "page_sub": "Guias de estilo baseados em proporção corporal",
        "section_label": "Últimos artigos",
        "other_lang_links": [
            ("/blog/", "한국어"),
            ("/blog/", "English"),
            ("/blog/ja/", "日本語"),
        ],
    })
    patch_sitemap()
    print("Done. Run inject-blog-hreflang.py next.")


if __name__ == "__main__":
    main()
