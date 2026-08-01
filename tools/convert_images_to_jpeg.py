# -*- coding: utf-8 -*-
"""Convert oversized illustration PNGs to JPEG and repoint every reference.

The English blog thumbnails and the social share cards were exported as 1536px
PNGs (1.2-2.7 MB each). They are flat illustrations, so JPEG at 1200px keeps the
detail at a fraction of the weight.
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
MAX_WIDTH = 1200
SEARCH_SUFFIXES = {".html", ".js", ".xml", ".txt", ".json", ".webmanifest"}
SKIP_DIRS = {".git", "node_modules", "tools", "canvases"}


def targets() -> list[tuple[Path, int]]:
    items: list[tuple[Path, int]] = [(p, 85) for p in sorted((ROOT / "blog" / "img" / "en").glob("*.png"))]
    items.append((ROOT / "og-image.jpg", 88))
    items.append((ROOT / "assets" / "og-image-en.jpg", 88))
    return [(p, q) for p, q in items if p.exists()]


def convert(path: Path, quality: int) -> tuple[str, str, int, int]:
    before = path.stat().st_size
    dest = path.with_suffix(".jpg")
    with Image.open(path) as im:
        im = im.convert("RGB")
        if im.width > MAX_WIDTH:
            im = im.resize((MAX_WIDTH, round(im.height * MAX_WIDTH / im.width)), Image.LANCZOS)
        im.save(dest, format="JPEG", quality=quality, optimize=True, progressive=True)
    after = dest.stat().st_size
    path.unlink()
    return path.name, dest.name, before, after


def rewrite(pairs: list[tuple[str, str]]) -> None:
    changed = 0
    for path in sorted(ROOT.rglob("*")):
        if path.is_dir() or any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in SEARCH_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        new = text
        for old_name, new_name in pairs:
            new = new.replace(old_name, new_name)
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    print("files with updated references:", changed)


def main() -> None:
    pairs: list[tuple[str, str]] = []
    saved = 0
    for path, quality in targets():
        old_name, new_name, before, after = convert(path, quality)
        pairs.append((old_name, new_name))
        saved += before - after
        print(f"{old_name}: {before // 1024} KB -> {after // 1024} KB")
    rewrite(pairs)
    print(f"total saved: {saved // 1024} KB")


if __name__ == "__main__":
    main()
