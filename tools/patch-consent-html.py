"""Patch static HTML for consent-init + deferred AdSense/Clarity.

Order matters: replace full head blocks BEFORE stripping standalone AdSense tags.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

OLD_STANDARD = """  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-JW0DB4GXG3"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-JW0DB4GXG3');
  </script>
  <script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "wk36ynf43e");
  </script>"""

NEW_STANDARD = """  <script src="/consent-init.js"></script>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-JW0DB4GXG3"></script>
  <script>
    gtag('js', new Date());
    gtag('config', 'G-JW0DB4GXG3');
  </script>"""

OLD_COMPACT = """<head>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-JW0DB4GXG3"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-JW0DB4GXG3');</script>
  <script type="text/javascript">(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y)})(window,document,"clarity","script","wk36ynf43e");</script>"""

NEW_COMPACT = """<head>
  <script src="/consent-init.js"></script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-JW0DB4GXG3"></script>
  <script>gtag('js',new Date());gtag('config','G-JW0DB4GXG3');</script>"""

OLD_404 = """  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-JW0DB4GXG3"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-JW0DB4GXG3');
  </script>
  <meta name="google-adsense-account" content="ca-pub-6377720400458954">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6377720400458954" crossorigin="anonymous"></script>
  <script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "wk36ynf43e");
  </script>"""

NEW_404 = """  <script src="/consent-init.js"></script>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-JW0DB4GXG3"></script>
  <script>
    gtag('js', new Date());
    gtag('config', 'G-JW0DB4GXG3');
  </script>
  <meta name="google-adsense-account" content="ca-pub-6377720400458954">"""

ADS_ONE_LINE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6377720400458954" crossorigin="anonymous"></script>'

ADS_TWO_LINE_PATTERN = re.compile(
    r'<script async src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js\?client=ca-pub-6377720400458954"\s*\n\s*crossorigin="anonymous"></script>\s*\n?',
    re.MULTILINE,
)


def inject_body(content: str) -> str:
    if "cookie-consent.js" in content:
        return content
    m = None
    for match in re.finditer(r"</body>", content, flags=re.IGNORECASE):
        m = match
    if not m:
        return content
    ins = '<script defer src="/cookie-consent.js"></script>\n'
    return content[: m.start()] + ins + content[m.start() :]


def strip_ads_scripts(content: str) -> str:
    content = ADS_TWO_LINE_PATTERN.sub("", content)
    while ADS_ONE_LINE in content:
        content = content.replace(ADS_ONE_LINE, "", 1)
    return content


def patch_file(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    orig = raw
    if OLD_404 in raw:
        raw = raw.replace(OLD_404, NEW_404)
    if OLD_STANDARD in raw:
        raw = raw.replace(OLD_STANDARD, NEW_STANDARD)
    if OLD_COMPACT in raw:
        raw = raw.replace(OLD_COMPACT, NEW_COMPACT)
    raw = strip_ads_scripts(raw)
    raw = inject_body(raw)
    if raw != orig:
        path.write_text(raw, encoding="utf-8", newline="\n")
        return True
    return False


def main():
    n = 0
    for p in ROOT.rglob("*.html"):
        if ".git" in p.parts:
            continue
        try:
            if patch_file(p):
                print("patched:", p.relative_to(ROOT))
                n += 1
        except Exception as ex:
            print("ERR", p, ex)
    print("total patched:", n)


if __name__ == "__main__":
    main()
