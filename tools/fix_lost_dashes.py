# -*- coding: utf-8 -*-
"""Restore characters that a lossy save turned into '??' inside the English posts.

The bad save replaced each non-ASCII character *and the byte after it* with '??'.
So "line — which" became "line ??which" and "wrong” body" became "wrong??body".
Cases where the swallowed byte was a digit (number ranges) cannot be inferred and
are reported instead of guessed.
"""
from __future__ import annotations

import io
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
EM = "\u2014"
CLOSE_Q = "\u201d"
OPEN_Q = "\u201c"
ARROW = "\u2192"


def repair(text: str) -> tuple[str, list[str]]:
    out: list[str] = []
    unresolved: list[str] = []
    open_quotes = 0
    i = 0
    while i < len(text):
        if text.startswith("??", i):
            prev = out[-1] if out else ""
            after = text[i + 2 : i + 6]

            if after.startswith("/a>"):
                out.append(ARROW + "<")
                i += 2
                continue

            nxt = text[i + 2] if i + 2 < len(text) else ""

            if open_quotes > 0 and (prev.isalnum() or prev in ",.!?;:"):
                out.append(CLOSE_Q + " ")
                open_quotes -= 1
                i += 2
                continue

            if prev == " " and (nxt.isalnum() or nxt in "<“"):
                out.append(EM + " ")
                i += 2
                continue

            unresolved.append(
                "".join(out[-45:]) + "[??]" + text[i + 2 : i + 30].replace("\n", " ")
            )
            out.append("??")
            i += 2
            continue

        ch = text[i]
        if ch == OPEN_Q:
            open_quotes += 1
        elif ch == CLOSE_Q:
            open_quotes = max(0, open_quotes - 1)
        out.append(ch)
        i += 1
    return "".join(out), unresolved


def main() -> None:
    report = io.open(ROOT / "tools" / "_qq_report.txt", "w", encoding="utf-8")
    total_fixed = 0
    total_left = 0
    for path in sorted(ROOT.glob("blog/blog*-en.html")):
        text = path.read_text(encoding="utf-8")
        before = text.count("??")
        if not before:
            continue
        fixed, unresolved = repair(text)
        after = fixed.count("??")
        path.write_text(fixed, encoding="utf-8")
        total_fixed += before - after
        total_left += after
        report.write(f"\n=== {path.name}: fixed {before - after}, left {after}\n")
        for line in unresolved:
            report.write("  " + line + "\n")
    report.close()
    print("restored:", total_fixed, "| still ambiguous:", total_left)


if __name__ == "__main__":
    main()
