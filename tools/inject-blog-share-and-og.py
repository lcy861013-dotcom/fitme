#!/usr/bin/env python3
"""
For every blog post (KO + EN):
  1. Replace generic /og-image.png with the post's own thumbnail (huge SEO/SMM win).
  2. Inject /assets/fitme-share.js?v=8 before </body> if not already present.
Idempotent. Skips files that don't follow the blog template (no <main>).
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOG_DIR = ROOT / "blog"

SHARE_TAG = '<script defer src="/assets/fitme-share.js?v=8"></script>'

# Map each blog post to its thumbnail file path.
# We assume `/blog/img/en/blogN-...-thumb-en.png` exists (it does for blog1..blog25).
# For KO posts we reuse the same English thumbnail (single asset, language-neutral image).
THUMB_DIR_EN = BLOG_DIR / "img" / "en"


def find_thumb(blog_num: int) -> str | None:
    """Return /blog/img/en/blogN-...-thumb-en.png path string, if a single match exists."""
    candidates = sorted(THUMB_DIR_EN.glob(f"blog{blog_num}-*-thumb-en.png"))
    if not candidates:
        return None
    p = candidates[0]
    return f"/blog/img/en/{p.name}"


def update_post(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    new = raw

    m = re.match(r"blog(\d+)(?:-en)?\.html$", path.name)
    if not m:
        return False
    n = int(m.group(1))
    thumb = find_thumb(n)

    # 1) og:image rewrite — only when the existing one is the generic site OG.
    if thumb:
        absolute = f"https://perfectfitme.com{thumb}"
        new = re.sub(
            r'(<meta[^>]+property="og:image"[^>]+content=")[^"]+(")',
            r"\1" + absolute + r"\2",
            new,
            count=1,
        )
        # JSON-LD Article.image
        new = re.sub(
            r'("image":\s*)"https://perfectfitme\.com/og-image\.png"',
            r'\1"' + absolute + r'"',
            new,
            count=1,
        )
        # Optional twitter image (only if present)
        new = re.sub(
            r'(<meta[^>]+name="twitter:image"[^>]+content=")[^"]+(")',
            r"\1" + absolute + r"\2",
            new,
            count=1,
        )

    # 2) Inject share script if missing.
    if "fitme-share.js" not in new:
        if "</body>" in new:
            new = new.replace("</body>", "  " + SHARE_TAG + "\n</body>", 1)

    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    touched = []
    skipped = []
    for path in sorted(BLOG_DIR.glob("blog*.html")):
        if path.name == "index.html":
            continue
        if update_post(path):
            touched.append(path.relative_to(ROOT))
        else:
            skipped.append(path.relative_to(ROOT))
    print(f"Updated {len(touched)} blog posts, no-op {len(skipped)}.")
    for p in touched[:6]:
        print(f"  {p}")
    if len(touched) > 6:
        print(f"  ... and {len(touched) - 6} more")


if __name__ == "__main__":
    main()
