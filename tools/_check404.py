# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
path = os.path.join(os.environ["TEMP"], "404body.html")
data = open(path, "rb").read()
text = data.decode("utf-8", "replace")
print("bytes:", len(data))
for pattern in (r"<title>.*?</title>", r"<h1[^>]*>.*?</h1>", r'<div class="title">.*?</div>'):
    print(pattern, "->", [m[:100] for m in re.findall(pattern, text, re.S)])
