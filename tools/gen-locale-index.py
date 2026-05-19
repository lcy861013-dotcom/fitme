#!/usr/bin/env python3
"""Create /{locale}/index.html from about.html with canonical -> /{locale}/about."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://perfectfitme.com"

for loc in ("ko", "en", "ja", "pt"):
    about = ROOT / loc / "about.html"
    text = about.read_text(encoding="utf-8")
    canon = f"{SITE}/{loc}/about"
    text = re.sub(
        r'<link rel="canonical" href="[^"]+"',
        f'<link rel="canonical" href="{canon}"',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta property="og:url" content="[^"]+"',
        f'<meta property="og:url" content="{canon}"',
        text,
        count=1,
    )
    out = ROOT / loc / "index.html"
    out.write_text(text, encoding="utf-8")
    print("wrote", out.relative_to(ROOT))
