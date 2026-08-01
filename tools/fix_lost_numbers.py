# -*- coding: utf-8 -*-
"""Second pass for the '??' corruption: number ranges and a few one-off characters.

Where the surviving side still has digits the lost digit is derived (the smaller
endpoint plus the retained tail leave exactly one valid value). Where the whole
endpoint was swallowed the value comes from the Korean edition of the same post,
falling back to the closest conventional range.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
EN_DASH = "\u2013"
EM_DASH = "\u2014"

# Endpoint fully lost: value taken from the Korean edition where it exists.
EXPLICIT: dict[str, list[tuple[str, str]]] = {
    "blog2-en.html": [
        ("roughly 4?? mm wider", f"roughly 4{EN_DASH}5 mm wider"),
        ("give your foot 2??mm more", f"give your foot 2{EN_DASH}3mm more"),
        ("wearing them for 1?? hours daily", f"wearing them for 1{EN_DASH}2 hours daily"),
        ("After 3?? sessions", f"After 3{EN_DASH}5 sessions"),
        ("gained 2??mm of effective width", f"gained 2{EN_DASH}4mm of effective width"),
        ('description ??"available in wide"', f'description {EM_DASH} "available in wide"'),
    ],
    "blog3-en.html": [
        ("typically 8?? inches below the waist", f"typically 8{EN_DASH}9 inches below the waist"),
    ],
    "blog6-en.html": [
        ("<p>??White round-neck tee", "<p>White round-neck tee"),
        ("last 3?? years", f"last 3{EN_DASH}5 years"),
    ],
    "blog7-en.html": [
        ("every 3?? months", f"every 3{EN_DASH}6 months"),
    ],
    "blog8-en.html": [
        ("typically 7?? inches below the natural waist", f"typically 7{EN_DASH}9 inches below the natural waist"),
        ("can add 1?? inches to the waist", f"can add 1{EN_DASH}2 inches to the waist"),
    ],
    "blog9-en.html": [
        ("added 1?? inches of apparent shoulder", f"added 1{EN_DASH}2 inches of apparent shoulder"),
    ],
    "blog10-en.html": [
        ("add 2?? cm visually", f"add 2{EN_DASH}3 cm visually"),
        ("appear 2?? inches taller", f"appear 2{EN_DASH}3 inches taller"),
    ],
    "blog11-en.html": [
        ("give 2?? extra centimeters", f"give 2{EN_DASH}3 extra centimeters"),
        ("ride up 1?? inches", f"ride up 1{EN_DASH}2 inches"),
        ("adds 2?? cm to the torso", f"adds 2{EN_DASH}3 cm to the torso"),
        ("3?? cm to the sleeve", f"3{EN_DASH}4 cm to the sleeve"),
    ],
    "blog12-en.html": [
        ("widest point, 7?? inches below the waist", f"widest point, 7{EN_DASH}9 inches below the waist"),
        ("which is 1?? inches above the navel", f"which is 1{EN_DASH}2 inches above the navel"),
        ("typically 1?? inches larger", f"typically 1{EN_DASH}2 inches larger"),
        ("typically 7?? inches below the natural waist", f"typically 7{EN_DASH}9 inches below the natural waist"),
        ("usually 3?? inches smaller", f"usually 3{EN_DASH}4 inches smaller"),
        ("Every 3?? months", f"Every 3{EN_DASH}6 months"),
    ],
    "blog15-en.html": [
        ("Over 12??4 months", f"Over 12{EN_DASH}24 months"),
        ("will have 3?? rules", f"will have 3{EN_DASH}5 rules"),
        ("a list of 3?? specific rules", f"a list of 3{EN_DASH}5 specific rules"),
        ("typically 2?? cm above the navel", f"typically 2{EN_DASH}3 cm above the navel"),
    ],
    "blog16-en.html": [
        ("approximately 3?? months", f"approximately 3{EN_DASH}6 months"),
    ],
    "blog17-en.html": [
        ("more than 8?? inches narrower", f"more than 8{EN_DASH}10 inches narrower"),
        ("apparent height by 1?? inches", f"apparent height by 1{EN_DASH}2 inches"),
    ],
    "blog18-en.html": [
        ("hip measurement 3?? cm smaller", f"hip measurement 3{EN_DASH}5 cm smaller"),
        ("A 4?? cm gap", f"A 4{EN_DASH}6 cm gap"),
    ],
    "blog19-en.html": [
        ("with 2??% elastane", f"with 2{EN_DASH}5% elastane"),
    ],
}

RANGE_RE = re.compile(r'(\d+(?:\.\d+)?)("?)\?\?(\.?\d+)')


def close_range(match: re.Match[str]) -> str:
    left, quote, tail = match.group(1), match.group(2), match.group(3)
    low = float(left)
    for digit in "0123456789":
        try:
            value = float(digit + tail)
        except ValueError:
            return match.group(0)
        if value > low:
            return f"{left}{quote}{EN_DASH}{digit}{tail}"
    return match.group(0)


def main() -> None:
    left_over = 0
    for path in sorted(ROOT.glob("blog/blog*-en.html")):
        text = path.read_text(encoding="utf-8")
        if "??" not in text:
            continue
        original = text
        for needle, replacement in EXPLICIT.get(path.name, []):
            text = text.replace(needle, replacement)
        text = RANGE_RE.sub(close_range, text)
        if text != original:
            path.write_text(text, encoding="utf-8")
        remaining = text.count("??")
        left_over += remaining
        print(f"{path.name}: remaining {remaining}")
    print("total remaining:", left_over)


if __name__ == "__main__":
    main()
