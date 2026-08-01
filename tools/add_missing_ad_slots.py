# -*- coding: utf-8 -*-
"""Insert the standard AdSense slot into blog posts that are missing it."""
from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]

SLOT = (
    '  <div class="fitme-ad-slot" hidden aria-hidden="true">\n'
    '    <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-6377720400458954"'
    ' data-ad-format="auto" data-full-width-responsive="true"></ins>\n'
    "  </div>\n\n"
)


def main() -> None:
    added = 0
    for path in sorted(ROOT.glob("blog/blog*.html")):
        text = path.read_text(encoding="utf-8")
        if "fitme-ad-slot" in text:
            continue
        if "fitme-ads.js" not in text or "</main>" not in text:
            print(f"skip (no ads assets or main): {path.name}")
            continue
        text = text.replace("</main>", SLOT + "</main>", 1)
        path.write_text(text, encoding="utf-8")
        added += 1
        print(f"slot added: {path.name}")
    print("posts updated:", added)


if __name__ == "__main__":
    main()
