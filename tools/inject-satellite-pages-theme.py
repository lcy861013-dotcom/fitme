#!/usr/bin/env python3
"""Inject /assets/satellite-pages-theme.css link before </head> on static pages (not index/app demos)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK_LINE = '<link rel="stylesheet" href="/assets/satellite-pages-theme.css">\n'


def skip(path: Path) -> bool:
    if path.suffix.lower() != ".html":
        return True
    if path.name.startswith("google") and path.name.endswith(".html"):
        return True
    if "demos" in path.parts:
        return True
    if path.name == "index.html" and path.parent == ROOT:
        return True
    return False


def main() -> None:
    touched = []
    for path in ROOT.rglob("*.html"):
        if skip(path):
            continue
        raw = path.read_text(encoding="utf-8")
        if "satellite-pages-theme.css" in raw:
            continue
        lower = raw.lower()
        idx = lower.find("</head>")
        if idx == -1:
            continue
        new = raw[:idx].rstrip() + "\n  " + LINK_LINE.rstrip() + "\n" + raw[idx:]
        path.write_text(new, encoding="utf-8")
        touched.append(path.relative_to(ROOT))
    print(f"Injected stylesheet into {len(touched)} HTML files:")
    for p in sorted(touched)[:20]:
        print(f"  {p}")
    if len(touched) > 20:
        print(f"  … and {len(touched) - 20} more")


if __name__ == "__main__":
    main()
