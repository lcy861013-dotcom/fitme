#!/usr/bin/env python3
"""Remove forbidden credential/expert-impersonation terms from site content."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {"__pycache__", ".git"}

# Order matters: longer phrases first
REPLACEMENTS: list[tuple[str, str]] = [
    # Korean
    ("전문가 수준의", "더 정밀한"),
    ("전문가 제안", "맞춤"),
    ("전문가 스타일링", "비율 기반"),
    ("패션 전문가의", "비율 기반"),
    ("패션 전문가들은", "맞춤 제작 관행에서는"),
    ("패션 전문가들에게", "맞춤 제작 관행에는"),
    ("AI 스타일리스트", "AI 스타일 도구"),
    ("인간 스타일리스트", "수동 코디 상담"),
    ("개인 스타일리스트", "유료 맞춤 상담"),
    ("스타일리스트", "코디 참고"),
    ("전문가", "비율"),
    # English phrases (blog / feeds)
    ("private stylists with years of experience", "expensive one-on-one fitting sessions"),
    ("private stylist charging hundreds of dollars per session", "paid fitting sessions costing hundreds of dollars"),
    ("private stylists", "paid styling services"),
    ("private stylist", "paid styling service"),
    ("The Era of the AI Stylist", "The Era of AI Styling Tools"),
    ("AI stylists combining", "AI styling tools combining"),
    ("deploying AI stylists,", "deploying AI styling tools,"),
    ("an AI stylist can", "an AI styling tool can"),
    ("AI stylists,", "AI styling tools,"),
    ("AI stylists ", "AI styling tools "),
    ("internalized expertise", "internalized know-how"),
    ("AI stylists", "AI styling tools"),
    # SVG / cards
    ("Traditional Stylist", "Traditional fitting"),
    ("personal stylist", "personalized FITME"),
    ("AI + measurement = your personal stylist", "AI + measurement = your proportion guide"),
]

# Word-boundary English: stylist but not stylistic/ally
STYLIST_RE = re.compile(
    r"\bstylist(s)?\b(?![a-z])",
    re.IGNORECASE,
)


def scrub_text(text: str) -> str:
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    # stylists measuring -> tailors (blog7-en)
    text = re.sub(
        r"\bstylist(s)? have been measuring\b",
        "tailors have been measuring",
        text,
        flags=re.I,
    )
    text = re.sub(
        r"\bit's the reason stylists have been\b",
        "it's the reason tailors have been",
        text,
        flags=re.I,
    )
    # Remaining standalone stylist/stylists (not stylistic)
    def _stylist_sub(m: re.Match[str]) -> str:
        w = m.group(0).lower()
        if w.startswith("stylist") and w.endswith("s"):
            return "styling tools"
        return "styling tool"

    text = STYLIST_RE.sub(_stylist_sub, text)
    # Code identifiers
    text = text.replace("runExpertAnalysis", "runProportionAnalysis")
    return text


def scrub_file(path: Path) -> bool:
    try:
        raw = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return False
    new = scrub_text(raw)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    exts = {".html", ".js", ".xml", ".txt", ".md", ".svg"}
    n = 0
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix not in exts:
            continue
        if any(s in p.parts for s in SKIP):
            continue
        if p.name == "scrub-forbidden-credentials.py":
            continue
        if scrub_file(p):
            n += 1
            print(p.relative_to(ROOT))
    print(f"Scrubbed {n} files")


if __name__ == "__main__":
    main()
