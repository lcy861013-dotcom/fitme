# -*- coding: utf-8 -*-
"""Convert oversized PNG blog thumbnails to compact JPEGs and update references."""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
IMG = ROOT / "blog" / "img"
MAX_WIDTH = 1200
QUALITY = 85
STEMS = [
    "blog26-oversize-thumb-ko",
    "blog27-musinsa-size-thumb-ko",
    "blog28-short-height-coord-ko",
    "blog29-thigh-rise-pants-ko",
]
SEARCH_GLOBS = ("*.html", "blog/*.html", "assets/*.js", "*.txt", "*.xml")


def to_jpeg(stem: str) -> bool:
    src = IMG / f"{stem}.png"
    if not src.exists():
        print("skip (no png):", stem)
        return False
    dst = IMG / f"{stem}.jpg"
    before = src.stat().st_size
    with Image.open(src) as im:
        im = im.convert("RGB")
        if im.width > MAX_WIDTH:
            im = im.resize((MAX_WIDTH, round(im.height * MAX_WIDTH / im.width)), Image.LANCZOS)
        im.save(dst, format="JPEG", quality=QUALITY, optimize=True, progressive=True)
    print(f"{stem}: {before // 1024} KB png -> {dst.stat().st_size // 1024} KB jpg")
    src.unlink()
    return True


def rewrite_refs() -> None:
    files: list[Path] = []
    for pattern in SEARCH_GLOBS:
        files.extend(ROOT.glob(pattern))
    changed = 0
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        new = text
        for stem in STEMS:
            new = new.replace(f"{stem}.png", f"{stem}.jpg")
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
            print("updated refs:", path.relative_to(ROOT))
    print("files updated:", changed)


if __name__ == "__main__":
    for stem in STEMS:
        to_jpeg(stem)
    rewrite_refs()
