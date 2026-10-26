#!/usr/bin/env python3
"""Build index.html from src/template.html + src/data.json (single-file PWA)."""
import json, pathlib, hashlib, datetime

root = pathlib.Path(__file__).parent
tpl = (root / "src/template.html").read_text(encoding="utf-8")
data = json.loads((root / "src/data.json").read_text(encoding="utf-8"))

compact = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
build = datetime.datetime.now().strftime("%Y%m%d.%H%M")
html = tpl.replace("__DATA__", compact).replace("__BUILD__", build)
(root / "index.html").write_text(html, encoding="utf-8")

total = sum(len(v) for v in data.values())
print(f"index.html {len(html)} bytes — {total} items — build {build}")
for k, v in data.items():
    print(f"  {k}: {len(v)}")
print("sha", hashlib.sha256(html.encode()).hexdigest()[:12])
