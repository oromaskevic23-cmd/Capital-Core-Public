"""Regenerate the redirects from the former IMPERIAL Core showcase."""

import hashlib
from html import escape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT / "reference"
HOST = "https://oromaskevic23-cmd.github.io"
OLD = HOST + "/Capital-Core-Public/reference/"
SHOWCASE = HOST + "/oromaskevic23-cmd/imperial-core/"
LABELS = {
    "en": "Open IMPERIAL Core",
    "ru": "Открыть IMPERIAL Core",
    "uk": "Відкрити IMPERIAL Core",
    "de-CH": "IMPERIAL Core öffnen",
    "fr": "Ouvrir IMPERIAL Core",
    "es": "Abrir IMPERIAL Core",
    "pt": "Abrir IMPERIAL Core",
    "ar": "افتح IMPERIAL Core",
    "ja": "IMPERIAL Coreを開く",
    "zh": "打开 IMPERIAL Core",
}


def render(lang, target):
    return f"""<!doctype html>
<html lang="{lang}"{' dir="rtl"' if lang == 'ar' else ''}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>IMPERIAL Core</title>
<link rel="canonical" href="{target}">
<meta http-equiv="refresh" content="0; url={target}">
</head>
<body>
<main><h1>IMPERIAL Core</h1><p><a href="{target}">{escape(LABELS[lang])}</a></p></main>
<script>location.replace(document.querySelector('link[rel="canonical"]').href + location.search + location.hash);</script>
</body>
</html>
"""


def main():
    former_urls = set()
    for lang in LABELS:
        suffix = "" if lang == "en" else lang + "/"
        former_urls.add(OLD + suffix)
        (REFERENCE / suffix / "index.html").write_text(render(lang, SHOWCASE + suffix), encoding="utf-8")
    for file in (ROOT / "sitemap.xml", REFERENCE / "sitemap.xml"):
        xml = file.read_text(encoding="utf-8")
        xml = re.sub(r"(?m)^[ \t]*<url>\s*<loc>([^<]+)</loc>[\s\S]*?</url>\n?",
                     lambda match: "" if match[1] in former_urls else match[0], xml)
        file.write_text(xml, encoding="utf-8")

    manifest = REFERENCE / "publication-manifest.json"
    data = json.loads(manifest.read_text(encoding="utf-8"))
    data["pages"] = [url for url in data["pages"] if url not in former_urls]
    for file in data["files"]:
        file["sha256"] = hashlib.sha256((REFERENCE / file["path"]).read_bytes()).hexdigest()
    manifest.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
