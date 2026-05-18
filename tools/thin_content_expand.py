# Expanded JA/PT bodies for blog6–9 (Search Console: thin / low-value content).
# Editorial footer is appended in build-blog6-9-multilang.py.
from textwrap import dedent


def _edition_ja(en_slug: str) -> str:
    return dedent(f"""
  <p class="edition-note">このページは<strong>日本向けの編集・実践版</strong>です。同テーマの長文・FAQ完全版は
  <a href="/blog/{en_slug}">英語版ガイド</a> をあわせてご覧ください。以下は国内の既製服・サイズ感を踏まえた独自解説です。</p>
""")


def _edition_pt(en_slug: str) -> str:
    return dedent(f"""
  <p class="edition-note">Edição em português com exemplos para o mercado lusófono.
  Guia completo em inglês: <a href="/blog/{en_slug}">versão EN</a>.</p>
""")


THIN_JA = {
    "capsule-5-basics": _edition_ja("blog6-en") + dedent("""
  <p class="lead-answer"><strong>相互に組み合わせられる5着があれば、スニーカーとローファー2足で平日7コーデが可能です。</strong>
  白T・黒ストレート・デニムジャケット・ベージュチノ・ライトワイドデニムから始め、肩縫いと股上を先に合わせてください。</p>
  <h2>なぜ5点で足りるのか — 互換性がすべて</h2>
  <p>カプセルの核心は服の総数ではなく <strong>1着あたりの組み合わせ数</strong> です。5着それぞれが他の3着以上と組み合わせ可能であれば、靴2足で印象の違う7コーデが作れます。</p>
  <p>日本のユニクロ・無印等の既製服は平均体型向けパターンが多く、肩幅・ヒップ・股下でズレが出やすいです。FITMEでSHRと脚比率を把握してから5点を選ぶと失敗が減ります。</p>
  <h2>5つの基本ピース</h2>
  <p>① 白クルーネックT（肩縫い優先）② 黒ストレート（股上は脚比率に合わせる）③ ライトデニムジャケット ④ ベージュチノ ⑤ ライトワイドデニム。靴は白スニーカーと黒ローファー。</p>
  <h2>月〜金のコーデ例</h2>
  <p><strong>月</strong> 白×黒×ローファー（前だけイン）。<strong>火</strong> デニムジャケット×チノ。<strong>水</strong> ワイドは前ハーフタック。<strong>木</strong> 黒トーンオントーン＋デニム上着。<strong>金</strong> チノ×白T。</p>
  <h2>週末とお手入れ</h2>
  <p>土：デニムオンデニム（ウォッシュを変える）。日：ゆったりチノ＋白T。白Tは冷水、デニムは着用回数ベースで洗濯。</p>
  <h2>体型別の調整</h2>
  <p>逆三角：下ダーク・ワイド、上Vネック。洋ナシ：下ダーク、上に肩の構造。長方形：ハイライズ＋イン。りんご型：ハイウエスト、幅広ベルトは避ける。</p>
  <h2>購入前チェックリスト</h2>
  <p>肩の縫い目 → 胸・ヒップの引っ張り → 手持ち4着と3コーデ以上。満たさない服はカプセル外に。</p>
  <div class="faq-block">
    <h3>5着で1週間足りる？</h3><p>靴2足で平日7＋週末2が目安です。</p>
    <h3>ユニクロだけで組める？</h3><p>十分です。サイズは肩・ヒップ列を優先。</p>
    <h3>体型が変わったら？</h3><p>3〜6ヶ月ごとに<a href="/#analysis">無料診断</a>で再計測。</p>
  </div>
  <p>詳細は <a href="/blog/ja/pants-fit-guide">パンツガイド</a> · <a href="/blog/ja/taikei-fuku-erabikata">体型別ガイド</a>。</p>
"""),
    "proportion-not-weight": _edition_ja("blog7-en") + dedent("""
  <p class="lead-answer"><strong>同じ体重でも肩・腰・脚の比率が違えば似合う服は正反対です。</strong> BMIよりSHR・WHR・脚比率を優先してください。</p>
  <h2>体重計の落とし穴</h2>
  <p>身長・体重が同じでも、肩÷ヒップ、脚÷身長が違えばトップスの肩幅、パンツのライズ、丈は真逆です。BMIは人口統計用で、個人の服選びには向きません。</p>
  <h2>同じ体重、違うシルエット（具体例）</h2>
  <p>160cm台・55kgでも、SHRが高い人は下にボリューム、洋ナシ型はハイライズと上の構造 — 店頭の正解サイズは別物です。</p>
  <h2>測るべき3比率</h2>
  <p><strong>SHR</strong> 肩幅÷ヒップ。<strong>WHR</strong> 最細ウエスト÷最大ヒップ。<strong>脚比率</strong> 股下÷身長。</p>
  <h2>脚比率 — 見落とされがち</h2>
  <p>0.47以上は脚が長め、0.44未満は胴長。胴長はハイライズとクロップ上着で脚の開始位置を上げると改善します。</p>
  <h2>比率からスタイルへ</h2>
  <p>SHRが高い → 下に視覚重量。WHRが低い → ウエストマーク。数字が「強調・抑制」の指示になります。</p>
  <h2>再計測</h2>
  <p>3〜6ヶ月ごと。筋トレ・体重変化で比率は動きます。</p>
  <div class="tip">💡 <a href="/blog/ja/taikei-fuku-erabikata">体型別ガイド</a> · <a href="/blog/ja/find-body-type-data">データで体型判定</a> · <a href="/how-it-works.html">ツールの仕組み</a></div>
  <div class="faq-block">
    <h3>BMIは使わないの？</h3><p>健康参考にはなりますが、服のフィットは比率で決まります。</p>
    <h3>メジャーがない</h3><p>手の幅を単位にする方法もあります。FITMEは3項目から推定します。</p>
  </div>
"""),
    "whr-clothing-fit": _edition_ja("blog8-en") + dedent("""
  <p class="lead-answer"><strong>WHR（最細ウエスト÷最大ヒップ）は、パンツがヒップで締まりウエストが空く理由を1数字で説明します。</strong></p>
  <h2>WHRとは — 計算例</h2>
  <p>朝、下着のみで測定。例：ウエスト68cm÷ヒップ95cm≒0.72。同じウエストサイズ表示でもヒップが違えばWHRは変わります。</p>
  <h2>レンジ別スタイル</h2>
  <p><strong>0.65–0.75</strong>：ベルト、タックイン、ラップ、ハイウエスト。<br>
  <strong>0.75–0.85</strong>：既製パンツと相性が良い。<br>
  <strong>0.85+</strong>：ハイウエスト、Aライン、縦の色分け。低ライズスキニーは避けやすい。</p>
  <h2>サイズ選び</h2>
  <p>ヒップに合わせてサイズを取り、ウエストは補正が定番。レビューで「ウエストだけ大きい」はWHRが想定より高いサインです。</p>
  <h2>洋ナシ型との関係</h2>
  <p>ヒップが肩より広い体型ではWHRが低めになりがち。下ダーク、上に構造を足すとバランスが取りやすい。<a href="/blog/ja/pear-styling">洋ナシガイド</a>参照。</p>
  <h2>トップスへの応用</h2>
  <p>WHRが高い人はウエスト周りにボリュームのあるトップスが胴を強調しやすい。縦ライン（Vネック、ロングカーディガン）が有効な場合があります。</p>
  <div class="tip">💡 <a href="/blog/blog8-en">WHR guide (EN)</a> · <a href="/blog/ja/golden-ratio-fuku">ゴールデンレシオ</a></div>
  <div class="faq-block">
    <h3>理想のWHRは？</h3><p>服では「あなたの数値に合う股上・シルエット」を探すことが目的です。</p>
    <h3>同じサイズで合わない</h3><p>ブランドごとのヒップ想定が違います。</p>
  </div>
"""),
    "shoulder-fit-guide": _edition_ja("blog9-en") + dedent("""
  <p class="lead-answer"><strong>肩の縫い目が肩峰（アクロミオン）に乗らない服は、袖や胴を直しても崩れます。</strong> 肩を最優先にサイズ選びを。</p>
  <h2>肩がアンカーになる理由</h2>
  <p>既製服のパターンは肩幅から切られます。肩が合えば袖・胴は直せる — 逆はほぼ不可能です。オンライン返品の多くは「肩が合わない」が原因です。</p>
  <h2>肩幅別の選び方</h2>
  <p><strong>広肩</strong>：Vネック、ラグラン、深めのスキッパーで肩のラインを切る。上にフリルや大きな襟は避ける。<br>
  <strong>狭肩</strong>：構築的ブレザー、ボートネック、肩パッド入りジャケット。<br>
  <strong>標準</strong>：股上・丈・ウエストで微調整。</p>
  <h2>測り方（自宅）</h2>
  <p>鏡の前で、左右の肩峰（骨の出っ張り）の間をメジャーで測る。Tシャツ着用時は生地の厚み分を引く。FITMEは身長・ウエスト・ヒップから肩幅を推定します。</p>
  <h2>店頭・オンラインの順序</h2>
  <p>試着は <strong>肩の縫い目 → 胸 → ウエスト</strong> の順。サイズ表は「肩」列を最初に比較。レビューの「肩が狭い」はブランドのパターン差のことも多いです。</p>
  <h2>ジャケットとTシャツの違い</h2>
  <p>ジャケットは構造がある分、肩の許容幅が狭い。Tは多少のゆとりがあっても、縫い目が肩峰から2cm以上外れるとダメージに見えます。</p>
  <div class="tip">💡 <a href="/blog/blog21-en">肩幅セルフ計測（英語）</a> · <a href="/blog/ja/pants-fit-guide">パンツガイド</a></div>
  <div class="faq-block">
    <h3>肩だけ直せる？</h3><p>軽微なずれのみ。基本は肩が合うサイズを選ぶこと。</p>
    <h3>落ち肩デザインは？</h3><p>意図的なオーバーサイズなら可。ただし肩幅が広く見える効果があります。</p>
  </div>
"""),
}

THIN_PT = {
    "guarda-roupa-capsula-5-pecas": _edition_pt("blog6-en") + dedent("""
  <p class="lead-answer"><strong>Cinco peças compatíveis + dois sapatos cobrem a semana de trabalho.</strong>
  Camiseta branca, calça preta reta, jaqueta jeans, chino bege, jeans wide claro — confira ombro e cintura antes de comprar.</p>
  <h2>Por que cinco peças bastam</h2>
  <p>O segredo é <strong>compatibilidade cruzada</strong>: cada peça combina com pelo menos três outras. Armários grandes com peças que não combinam geram menos looks úteis que um cápsula bem escolhido.</p>
  <h2>As cinco peças</h2>
  <p>① Camiseta branca ② Calça preta reta ③ Jaqueta jeans clara ④ Chino bege ⑤ Jeans wide claro. Sapatos: tênis branco e loafer preto.</p>
  <h2>Segunda a sexta</h2>
  <p>Seg: branco + preto + loafer. Ter: jaqueta + chino + tênis. Qua: jeans wide com barra na frente. Qui: preto tom sobre tom + jaqueta. Sex: chino + camiseta.</p>
  <h2>Fim de semana e cuidados</h2>
  <p>Sáb: jeans sobre jeans (lavagens diferentes). Dom: chino solto + branco. Lave a camiseta branca à frio; jeans por uso, não por calendário.</p>
  <h2>Por proporção corporal</h2>
  <p>Ombros largos: calça estruturada escura, decote V. Pera: parte de baixo escura, blusa com estrutura no ombro. Retângulo: cintura alta e top por dentro.</p>
  <h2>Checklist antes de comprar</h2>
  <p>Costura do ombro no acrômio → sem puxar no peito/quadril → combina com 3 looks das outras peças.</p>
  <div class="faq-block">
    <h3>Funciona no Brasil?</h3><p>Sim — marcas como Renner e C&amp;A seguem a mesma lógica de tamanho por quadril.</p>
    <h3>Preciso de mais peças?</h3><p>Comece com cinco; acrescente só o que passar no checklist.</p>
  </div>
  <p>Veja também <a href="/blog/pt/guia-modelagem-calcas">guia de calças</a> · <a href="/blog/pt/como-se-vestir-tipo-de-corpo">tipos de corpo</a>.</p>
"""),
    "proporcao-importa-mais-que-peso": _edition_pt("blog7-en") + dedent("""
  <p class="lead-answer"><strong>Proporção define o caimento — peso sozinho não.</strong> SHR, WHR e perna-tronco antes do BMI.</p>
  <h2>A armadilha da balança</h2>
  <p>Duas pessoas com o mesmo peso podem precisar de silhuetas opostas se ombro-quadril e perna-tronco forem diferentes. O IMC não diz onde a roupa vai apertar.</p>
  <h2>Mesmo peso, silhuetas opostas</h2>
  <p>Quem tem ombros largos e quadril fino precisa de volume embaixo; corpo pera precisa de cintura alta e estrutura em cima — mesmo número na balança.</p>
  <h2>Três razões essenciais</h2>
  <p><strong>SHR</strong> ombro÷quadril. <strong>WHR</strong> cintura fina÷quadril largo. <strong>Perna-tronco</strong> entreperna÷altura. Use o FITME antes de comprar online.</p>
  <h2>Perna-tronco — o detalhe esquecido</h2>
  <p>Acima de 0,47: pernas longas. Abaixo de 0,44: tronco longo — prefira cós alto e top cropped por dentro.</p>
  <h2>Reavalie a cada 3–6 meses</h2>
  <p>Treino e mudança de peso alteram proporções mais que a balança sugere.</p>
  <div class="tip">💡 <a href="/blog/pt/como-se-vestir-tipo-de-corpo">Tipos de corpo</a> · <a href="/how-it-works.html">Como funciona</a></div>
  <div class="faq-block">
    <h3>E o IMC?</h3><p>Útil para saúde geral, não para escolher calça e blusa.</p>
    <h3>Sem fita métrica?</h3><p>Use a largura da mão como unidade ou o estimador FITME.</p>
  </div>
"""),
    "whr-e-caimento": _edition_pt("blog8-en") + dedent("""
  <p class="lead-answer"><strong>WHR (cintura fina ÷ quadril largo) explica calça apertada no quadril e folgada na cintura.</strong></p>
  <h2>O que é WHR</h2>
  <p>Meça de manhã, de roupa íntima. Exemplo: 68÷95 ≈ 0,72. O mesmo número na etiqueta da cintura pode esconder quadril diferente.</p>
  <h2>Como vestir por faixa</h2>
  <p><strong>0,65–0,75</strong>: cintura marcada, cinto, vestido envelope.<br>
  <strong>0,75–0,85</strong>: boa compatibilidade com pronta-modagem.<br>
  <strong>0,85+</strong>: cós alto, linha A, blocos verticais; evite skinny de cós baixo.</p>
  <h2>Tamanho</h2>
  <p>Compre pelo quadril; ajuste cintura no alfaiate. Avaliações “cintura grande” podem indicar WHR acima do padrão da marca.</p>
  <h2>Corpo pera</h2>
  <p>Quadril maior que ombros costuma dar WHR mais baixo. Parte de baixo escura e blusa com estrutura no ombro equilibram. <a href="/blog/pt/corpo-pera-como-vestir">Guia corpo pera</a>.</p>
  <div class="tip">💡 <a href="/blog/blog8-en">WHR guide (EN)</a> · <a href="/blog/pt/whr-065-significado">WHR 0,65</a></div>
  <div class="faq-block">
    <h3>Qual WHR é ideal?</h3><p>Para roupa, o ideal é o cós e silhueta que combinam com o seu número.</p>
  </div>
"""),
    "ombro-e-caimento": _edition_pt("blog9-en") + dedent("""
  <p class="lead-answer"><strong>A costura do ombro deve cair no acrômio — se errar, manga e corpo não salvam o look.</strong></p>
  <h2>Por que ombro é âncora</h2>
  <p>A modelagem parte do ombro. Costura caída = manga longa e visual desleixado. Peito e cintura o alfaiate ajusta depois.</p>
  <h2>Por tipo de ombro</h2>
  <p><strong>Largos</strong>: decote V, raglan. <strong>Estreitos</strong>: blazer estruturado, gola barco. <strong>Médios</strong>: quase tudo funciona com ajuste de cós e barra.</p>
  <h2>Como medir em casa</h2>
  <p>Entre os acrômios (ossos do ombro) com fita métrica. O FITME estima a partir de altura, cintura e quadril.</p>
  <h2>Compras online</h2>
  <p>Compare a coluna “ombro” primeiro. “Ombro largo” nas reviews pode ser troca de marca, não só tamanho.</p>
  <h2>Blazer vs camiseta</h2>
  <p>Blazer tolera menos erro no ombro. Camiseta pode ter folga leve, mas costura 2 cm fora do acrômio já parece larga demais.</p>
  <div class="tip">💡 <a href="/blog/blog21-en">Medir ombros (EN)</a> · <a href="/blog/pt/guia-modelagem-calcas">Guia de calças</a></div>
  <div class="faq-block">
    <h3>Dá para ajustar só o ombro?</h3><p>Só desvios pequenos. Escolha o tamanho certo no ombro.</p>
    <h3>Ombro caído de propósito?</h3><p>Ok se for oversize intencional — alarga a silhueta.</p>
  </div>
"""),
}

_EXTRA_JA = {
    "capsule-5-basics": dedent("""
  <h2>各ピースの詳しい選び方（日本の既製服）</h2>
  <p><strong>白T</strong>：綿220g前後が無難。肩の縫い目が肩峰より内側のサイズは避ける。</p>
  <p><strong>黒ストレート</strong>：胴長型はハイライズ、脚長型はミドルライズ。裾はくるぶし上がスニーカー向き。</p>
  <p><strong>デニムジャケット</strong>：肩が合わない場合は別ブランドを検討。インディゴは白・黒と相性◎。</p>
  <p><strong>チノ</strong>：ベージュは全組み合わせ可。ポリ混はシワに強くオフィス向き。</p>
  <p><strong>ワイドデニム</strong>：ヒップに余裕。洋ナシ型でも窮屈になりにくい。</p>
  <h2>よくある失敗</h2>
  <p>トレンド5着は互換性が崩れます。色とシルエットのルールが先。上明るく下暗いコントラストを1組入れる。</p>
  <h2>オンライン購入</h2>
  <p>肩・ヒップ・股下をお気に入り服の実寸と比較。返品が多いブランドはパターン不一致のサイン。</p>
"""),
    "proportion-not-weight": dedent("""
  <h2>SHRとトップス</h2>
  <p>SHR 0.95以上：Vネック、ラグランで肩のラインを切る。SHR 0.85未満：構築的ブレザー、ボートネックで上半身に存在感。</p>
  <h2>WHRと股上</h2>
  <p>WHR低：ミドル〜ハイでくびれを見せる。WHR高：ハイウエストで脚の開始位置を上げ、低ライズは腰回りを強調しやすい。</p>
  <h2>脚比率と丈</h2>
  <p>脚比率0.44未満：クロップ、ハイライズ、靴と同色で脚長見せ。0.47以上：過度なハイライズは不自然に見えることも。</p>
  <h2>記録の仕方</h2>
  <p>日付・3比率・合わなかった服の理由をメモ。FITMEスクショはオンライン購入時に便利。</p>
  <h2>健康との線引き</h2>
  <p>比率はスタイリング用。急な体重変化時は医療機関を優先。</p>
"""),
    "whr-clothing-fit": dedent("""
  <h2>スカート・ワンピース</h2>
  <p>ヒップ基準でサイズ、ウエスト補正。AラインはWHR高め、ペンシル＋ハイウエストはWHR低めに向きやすい。</p>
  <h2>素材</h2>
  <p>ストレッチはヒップで伸びウエストが空きやすい。通勤ときれいめで使い分け。</p>
  <h2>ブランド比較表</h2>
  <p>同じMでもヒップ実寸が8cm違うことは普通。3ブランドの実寸を表にすると選びやすい。</p>
  <h2>レビューの読み方</h2>
  <p>「ウエストだけ大きい」はWHRと想定のズレ。「全体的に小さい」は肩・ヒップ列を見直す。</p>
"""),
    "shoulder-fit-guide": dedent("""
  <h2>アウター</h2>
  <p>肩が合うサイズ＋薄いインナーが、肩だけ合わずサイズアップよりきれい。</p>
  <h2>ニット</h2>
  <p>縫い目が不明瞭なら袖根元・脇・着丈で判断。落ち肩は最内層向き。</p>
  <h2>袖丈</h2>
  <p>肩OKで袖長い→カフス調整可。肩落ちで袖短い→小さすぎる。</p>
  <h2>ラインの違い</h2>
  <p>メンズ・レディース・ユニセックスで肩パターンが異なる。ゆったりは肩落ちデザインのことも。</p>
"""),
}

_EXTRA_PT = {
    "guarda-roupa-capsula-5-pecas": dedent("""
  <h2>Detalhe de cada peça</h2>
  <p>Camiseta 180–220 g; calça reta com elastano; jaqueta indigo clara; chino bege; jeans wide.</p>
  <h2>Erros</h2>
  <p>Moda sem compatibilidade enche o armário. Regra de cor antes de comprar.</p>
  <h2>Online BR</h2>
  <p>Compare quadril e ombro; use medidas de uma peça que serviu bem.</p>
"""),
    "proporcao-importa-mais-que-peso": dedent("""
  <h2>SHR e blusas</h2>
  <p>SHR alto: decote V. SHR baixo: estrutura no ombro.</p>
  <h2>Registrar</h2>
  <p>Anote data e três razões no celular; screenshot do FITME ajuda.</p>
"""),
    "whr-e-caimento": dedent("""
  <h2>Saias e vestidos</h2>
  <p>Quadril na etiqueta, cintura no alfaiate. Linha A vs lápis conforme WHR.</p>
  <h2>Jeans elastano</h2>
  <p>Estica no quadril, folga na cintura — ajuste local costuma valer a pena.</p>
"""),
    "ombro-e-caimento": dedent("""
  <h2>Casacos</h2>
  <p>Ombro certo com camada fina; não suba tamanho só por moletom grosso.</p>
  <h2>Malha</h2>
  <p>Julgue pela raiz da manga se não houver costura visível no ombro.</p>
"""),
}

for _slug, _html in _EXTRA_JA.items():
    THIN_JA[_slug] = THIN_JA[_slug] + _html
for _slug, _html in _EXTRA_PT.items():
    THIN_PT[_slug] = THIN_PT[_slug] + _html
