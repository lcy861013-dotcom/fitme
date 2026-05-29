#!/usr/bin/env python3
"""Replace Ansan/안산 city references with country-only wording (idempotent)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).name

REPLACEMENTS: list[tuple[str, str]] = [
    ("FITME는 안산의 1인 창업가", "FITME는 대한민국의 1인 창업가"),
    ("FITME는 안산에 거주하는", "FITME는 대한민국에 거주하는"),
    ("FITME 대표, 안산", "FITME 대표, 대한민국"),
    ("1인 창업 (안산)", "1인 창업 (대한민국)"),
    ("대한민국 안산", "대한민국"),
    ("· 안산 ·", "· 대한민국 ·"),
    ("FITME代表、安山", "FITME代表、韓国"),
    ("Ansan, South Korea", "South Korea"),
    ("in Ansan, South Korea", "in South Korea"),
    ("based in Ansan, South Korea", "based in South Korea"),
    ("em Ansan, Coreia do Sul", "na Coreia do Sul"),
    ("Ansan, Coreia do Sul", "Coreia do Sul"),
    ("Fundador FITME, Ansan", "Fundador FITME, Coreia do Sul"),
    ("en Ansan, Corea del Sur", "en Corea del Sur"),
    ("Ansan, Corea del Sur", "Corea del Sur"),
    ("à Ansan, Corée du Sud", "en Corée du Sud"),
    ("Ansan, Corée du Sud", "Corée du Sud"),
    ("in Ansan, Südkorea", "in Südkorea"),
    ("Ansan, Südkorea", "Südkorea"),
    ("ad Ansan, Corea del Sud", "in Corea del Sud"),
    ("Ansan, Corea del Sud", "Corea del Sud"),
    ("Ансан, Южная Корея", "Южная Корея"),
    ("أنسان، كوريا الجنوبية", "كوريا الجنوبية"),
    ("अंसान, दक्षिण कोरिया", "दक्षिण कोरिया"),
    ("韓国・安山", "韓国"),
    ("韩国安山", "韩国"),
]

SKIP_DIRS = {".git", "__pycache__", "node_modules", ".cursor"}
TEXT_SUFFIXES = {".html", ".py", ".js", ".md", ".txt"}


def main() -> None:
    n = 0
    for path in ROOT.rglob("*"):
        if path.name == SELF or not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        orig = text
        for old, new in REPLACEMENTS:
            text = text.replace(old, new)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            n += 1
    print(f"updated {n} files")


if __name__ == "__main__":
    main()
