#!/usr/bin/env python3
"""Fix remaining EN author-meta (Research-based) and remove Wikipedia footers."""
import re
from pathlib import Path

BLOG = Path(__file__).resolve().parents[1] / "blog"

AUTHOR_SUB = {
    "blog1-en.html": "Pants fit — waist 32 kept failing online",
    "blog8-en.html": "WHR — waist matched, hips did not",
}

FOOTER_RE = re.compile(
    r'\n  <p style="font-size:13px;color:#8b8178;margin:12px 0 0;">Sources:.*?ISO 8559</a></p>',
    re.DOTALL,
)

AUTHOR_RE = re.compile(r'  <div class="author-meta">.*?</div>', re.DOTALL)


def author_block(subtitle: str) -> str:
    return f"""  <div class="author-meta">
    <p>By <strong>Changyong Lee</strong> · FITME solo founder (South Korea)</p>
    <p style="font-size:14px;color:#8b8178;">{subtitle} · <a href="/en/editorial-standards" style="color:#d4a84b;">Editorial standards</a> · <a href="/en/how-it-works" style="color:#d4a84b;">How it works</a> · <!--email_off--><a href="mailto:lcy861013@gmail.com" style="color:#d4a84b;">lcy861013@gmail.com</a><!--/email_off--></p>
  </div>"""


def main() -> None:
    for fn, sub in AUTHOR_SUB.items():
        p = BLOG / fn
        text = p.read_text(encoding="utf-8")
        if "Research-based guide" in text:
            text = AUTHOR_RE.sub(author_block(sub), text, count=1)
            p.write_text(text, encoding="utf-8")
            print("fixed author", fn)

    for p in BLOG.glob("blog*-en.html"):
        text = p.read_text(encoding="utf-8")
        new, n = FOOTER_RE.subn("", text)
        if n:
            p.write_text(new, encoding="utf-8")
            print("removed footer", p.name)


if __name__ == "__main__":
    main()
