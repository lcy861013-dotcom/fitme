#!/usr/bin/env python3
"""
Append/refresh ?v=NEW on every reference to our owned static assets across all HTML files.
Run after bumping the cache version. Touches:
  /consent-init.js
  /cookie-consent.js
  /cookie-consent.css
  /assets/fitme-app.css
  /assets/fitme-app.js
  /assets/fitme-ads.css
  /assets/fitme-ads.js
  /assets/satellite-pages-theme.css
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW_VERSION = "6"

ASSETS = [
    "/consent-init.js",
    "/cookie-consent.js",
    "/cookie-consent.css",
    "/assets/fitme-app.css",
    "/assets/fitme-app.js",
    "/assets/fitme-ads.css",
    "/assets/fitme-ads.js",
    "/assets/satellite-pages-theme.css",
]


def make_pattern(asset: str) -> re.Pattern:
    # Match the asset path optionally followed by ?v=NN, before " or '.
    return re.compile(re.escape(asset) + r"(?:\?v=\d+)?(?=[\"'])")


PATTERNS = [(asset, make_pattern(asset)) for asset in ASSETS]


def update_html(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    new = raw
    for asset, pattern in PATTERNS:
        new = pattern.sub(f"{asset}?v={NEW_VERSION}", new)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    touched = []
    for path in ROOT.rglob("*.html"):
        if "node_modules" in path.parts:
            continue
        if update_html(path):
            touched.append(path.relative_to(ROOT))
    print(f"Cache-busted asset URLs in {len(touched)} HTML files (v={NEW_VERSION}).")
    for p in sorted(touched)[:10]:
        print(f"  {p}")
    if len(touched) > 10:
        print(f"  ... and {len(touched) - 10} more")


if __name__ == "__main__":
    main()
