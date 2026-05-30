#!/usr/bin/env python3
"""AdSense consent-only wiring + blog ad slots + cache bumps."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ADS_SCRIPT_RE = re.compile(
    r'\s*<script async src="https://pagead2\.googlesyndication\.com/pagead/js/adsbygoogle\.js'
    r'\?client=ca-pub-6377720400458954" crossorigin="anonymous"></script>\s*\n?',
    re.I,
)

AD_SLOT = """  <div class="fitme-ad-slot" hidden aria-hidden="true">
    <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-6377720400458954" data-ad-format="auto" data-full-width-responsive="true"></ins>
  </div>
"""

ADS_ASSETS = """<link rel="stylesheet" href="/assets/fitme-ads.css?v=8">
<script defer src="/assets/fitme-ads.js?v=8"></script>
"""

SKIP = {
    "404.html",
    "googlee58e083c1a9f7cf1.html",
    "demo-video.html",
}


def should_add_slot(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    if path.name in SKIP:
        return False
    if rel == "index.html" or rel == "blog/index.html":
        return False
    if rel.startswith("blog/") and path.suffix == ".html":
        return True
    return False


def process_html(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text

    text = ADS_SCRIPT_RE.sub("\n", text)
    text = text.replace("fitme-ads.css?v=7", "fitme-ads.css?v=8")
    text = text.replace("fitme-ads.js?v=7", "fitme-ads.js?v=8")
    text = text.replace("cookie-consent.js?v=8", "cookie-consent.js?v=9")
    text = text.replace('hreflang="pt" href="https://perfectfitme.com/blog/pt/"', 'hreflang="pt-BR" href="https://perfectfitme.com/blog/pt/"')

    if should_add_slot(path) and "fitme-ad-slot" not in text and "</main>" in text:
        text = text.replace("</main>", AD_SLOT + "\n</main>", 1)

    if "fitme-ad-slot" in text and "fitme-ads.js" not in text:
        needle = '<script defer src="/cookie-consent.js'
        if needle in text:
            text = text.replace(needle, ADS_ASSETS + "\n" + needle, 1)
        elif "</body>" in text:
            text = text.replace("</body>", ADS_ASSETS + "\n</body>", 1)

    if path.name == "index.html" and path.parent == ROOT:
        text = text.replace(
            '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6377720400458954" crossorigin="anonymous"></script>\n',
            "",
        )

    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    changed = 0
    for path in ROOT.rglob("*.html"):
        if "node_modules" in path.parts:
            continue
        if process_html(path):
            changed += 1
            print("updated", path.relative_to(ROOT))
    print(f"done: {changed} files")


if __name__ == "__main__":
    main()
