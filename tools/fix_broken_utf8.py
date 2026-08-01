# -*- coding: utf-8 -*-
"""Repair HTML files whose multi-byte characters lost their leading bytes.

A previous lossy save replaced the first two bytes of some UTF-8 sequences with
an ASCII '?', leaving invalid bytes that browsers render as U+FFFD. The trailing
bytes are intact, so each pattern maps back to exactly one character.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]

# '?' + surviving tail bytes -> original UTF-8 bytes
REPAIRS: list[tuple[bytes, bytes]] = [
    (b"\x3f\x92\xa1", "\U0001F4A1".encode()),  # 💡
    (b"\x3f\xa5\x87", "\U0001F947".encode()),  # 🥇
    (b"\x3f\xa5\x88", "\U0001F948".encode()),  # 🥈
    (b"\x3f\xa5\x89", "\U0001F949".encode()),  # 🥉
    (b"\x3f\x94", "\u2014".encode()),  # —
    (b"\x3f\x93", "\u2013".encode()),  # –
    (b"\x3f\x9c", "\u201c".encode()),  # “
    (b"\x3f\x9d", "\u201d".encode()),  # ”
    (b"\x3f\x98", "\u2018".encode()),  # ‘
    (b"\x3f\x99", "\u2019".encode()),  # ’
    (b"\x3f\xa6", "\u2026".encode()),  # …
]


def repair(path: Path) -> int:
    raw = path.read_bytes()
    try:
        raw.decode("utf-8")
        return 0
    except UnicodeDecodeError:
        pass

    fixed = raw
    total = 0
    for broken, good in REPAIRS:
        count = fixed.count(broken)
        if count:
            fixed = fixed.replace(broken, good)
            total += count

    try:
        fixed.decode("utf-8")
    except UnicodeDecodeError as exc:
        print(f"{path.name}: STILL INVALID after repair -> {exc}")
        return 0

    path.write_bytes(fixed)
    return total


def main() -> None:
    targets = sorted(ROOT.glob("**/*.html")) + sorted(ROOT.glob("**/*.js")) + sorted(ROOT.glob("**/*.txt"))
    grand = 0
    for path in targets:
        if ".git" in path.parts or "node_modules" in path.parts:
            continue
        fixed = repair(path)
        if fixed:
            print(f"{path.relative_to(ROOT)}: repaired {fixed} characters")
            grand += fixed
    print("total characters repaired:", grand)


if __name__ == "__main__":
    main()
