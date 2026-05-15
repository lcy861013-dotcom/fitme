#!/usr/bin/env python3
"""One-off: extract index.html inline CSS/JS to assets/."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
index_path = root / "index.html"
lines = index_path.read_text(encoding="utf-8").splitlines(keepends=True)

css = "".join(lines[153:1775])
(root / "assets" / "fitme-app.css").write_text(css, encoding="utf-8")

js = "".join(lines[2964:8374])
(root / "assets" / "fitme-app.js").write_text(js, encoding="utf-8")

out = []
out.extend(lines[:153])
out.append('  <link rel="stylesheet" href="/assets/fitme-app.css">\n')
head_tail = lines[1775:]
if head_tail and "</style>" in head_tail[0]:
    head_tail[0] = head_tail[0].replace("</style>", "", 1)
out.extend(head_tail[:2962 - 1775])
out.append('<script defer src="/assets/fitme-app.js"></script>\n')
out.extend(lines[8375:])
index_path.write_text("".join(out), encoding="utf-8")

print(f"fitme-app.css: {len(css.splitlines())} lines")
print(f"fitme-app.js: {len(js.splitlines())} lines")
print(f"index.html: {len(out)} lines")
