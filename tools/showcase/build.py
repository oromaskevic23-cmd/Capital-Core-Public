"""Regenerate the static, localized IMPERIAL Core showcase on gh-pages."""

import argparse
import hashlib
from html import escape
import json
from pathlib import Path
import re

from content import COPY, FEATURED, FEATURE_TEXT, LANGUAGES, MORE, MORE_TEXT, REFERENCE_LABELS

ROOT = Path(__file__).resolve().parents[2]
REFERENCE = ROOT / "reference"
HOST = "https://oromaskevic23-cmd.github.io"
BASE = "/Capital-Core-Public"
SHOWCASE = BASE + "/reference/"
ASSETS = SHOWCASE + "assets/"
DUBAI = ASSETS + "dubai/"
ART = ASSETS + "showcase/"
FOUNDER = HOST + "/oromaskevic23-cmd/"
GIT = "https://github.com/oromaskevic23-cmd"
CONTEST = GIT + "/IMPERIAL-DUBAI-2027-Public"
STUDIO = SHOWCASE + "constructor-ai/studio/studio.html"
SCENES = ("terrace", "waterfront", "atrium", "aerial", "intelligence", "night")
CARD_ICONS = ("gem", "stack-2", "topology-star-3", "shield-check", "id", "topology-star-3", "code", "cpu", "users")
ALT_NAMES = ("Alexander Nikolaevich Romaskevich", "Александр Николаевич Ромаскевич", "Олександр Ромаскевич", "RomaskevicH")


def suffix(lang):
    return "" if lang == "en" else f"{lang}/"


def icon(name):
    return f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><use href="{ASSETS}showcase-icons.svg?v=3#{name}"/></svg>'


def link(label, href, style="text-link", arrow=True, extra=""):
    mark = f'<span class="arrow">{icon("arrow-up-right")}</span>' if arrow else ""
    classes = f' class="{style}"' if style else ""
    return f'<a{classes} href="{escape(href, quote=True)}"{extra}>{escape(label)}{mark}</a>'


def identity(lang, url, title, description):
    person = FOUNDER + "#person"
    organization = HOST + BASE + "/#organization"
    website = HOST + BASE + "/#website"
    return {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebPage", "@id": url + "#page", "url": url, "name": title,
             "description": description, "inLanguage": lang, "isPartOf": {"@id": website},
             "about": {"@id": organization}, "author": {"@id": person}},
            {"@type": "Organization", "@id": organization, "name": "IMPERIAL Core",
             "url": HOST + BASE + "/", "founder": {"@id": person},
             "logo": HOST + BASE + "/assets/imperial-core-diamond-20261116.jpg",
             "sameAs": [GIT + "/Capital-Core-Public"]},
            {"@type": "Person", "@id": person, "name": "Alexander Romaskevich", "alternateName": ALT_NAMES,
             "url": FOUNDER, "jobTitle": COPY[lang]["role"],
             "image": HOST + DUBAI + "alexander-romaskevich.webp", "sameAs": [GIT],
             "affiliation": {"@id": organization}},
            {"@type": "WebSite", "@id": website, "name": "IMPERIAL Core", "url": HOST + BASE + "/",
             "publisher": {"@id": organization}},
        ],
    }


def render(lang):
    t = COPY[lang]
    labels = REFERENCE_LABELS[lang].split(" | ")
    platform, solutions, resources, about, contact, access, overview, highlights, capabilities = labels[:9]
    capabilities_labels = labels[9:13]
    feature_labels = labels[13:19]
    capabilities_details = labels[19:]
    current = suffix(lang)
    url = HOST + SHOWCASE + current
    title = f"IMPERIAL Core | {t['hero1']} {t['hero2']}"
    direction = "rtl" if lang == "ar" else "ltr"
    desc = f"{t['intro']} Alexander Romaskevich · IMPERIAL Core."
    archived = SHOWCASE + "technical/" + current
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{code}" href="{HOST}{SHOWCASE}{suffix(code)}">'
        for code in LANGUAGES
    )
    language_links = "\n".join(
        link(name, SHOWCASE + suffix(code), "", False,
             f' lang="{code}" hreflang="{code}"' + (' aria-current="page"' if lang == code else ""))
        for code, name in LANGUAGES.items()
    )
    navigation = (
        (platform, "architecture"), (solutions, "capabilities"), (t["portfolio"], "official-projects"),
        (resources, "dubai-2027"), (about, "architect"), (contact, "contact"),
    )
    nav = "".join(link(label, "#" + target, "", False) for label, target in navigation)
    principles = [
        ("HANTER", feature_labels[0], "#hanter", "gem"),
        (t["federation"], "", "#architecture", "stack-2"),
        (t["scope"], "", "#nano-core-agents", "cpu"),
        ("Zero Trust", "", GIT + "/ZERO-TRUST", "shield-check"),
        ("Audit Ledger", "", GIT + "/AUDIT-LEDGER", "database"),
        (capabilities_labels[1], "", "#velion", "topology-star-3"),
    ]
    principle_links = "".join(
        f'<a href="{href}">{icon(symbol)}<span>{escape(label)}'
        f'{f"<small>{escape(subtitle)}</small>" if subtitle else ""}</span></a>'
        for label, subtitle, href, symbol in principles
    )
    cards = []
    for i, ((name, repo, art, panorama, dest), description) in enumerate(zip(FEATURED, FEATURE_TEXT[lang], strict=True)):
        cid = name.lower().replace(" ", "-")
        featured = i < len(feature_labels)
        image = f"{ART}{cid}.webp" if featured else f"{DUBAI}{art}{'-800' if art in SCENES else ''}.webp"
        caption = feature_labels[i] if featured else description
        width, height = (590, 442) if featured else (800, 450)
        demo = f' data-demo="{STUDIO}"' if repo == "CONSTRUCTOR-AI" else ""
        href = f"{GIT}/{repo}{dest}"
        cards.append(f"""<a class="product" id="{cid}" href="{href}" data-scene="{panorama}" data-panorama="{DUBAI}{panorama}-800.webp" data-description="{escape(description)}"{demo}>
<img src="{image}" width="{width}" height="{height}" alt="" loading="lazy" decoding="async">
<div class="product-copy">{icon(CARD_ICONS[i])}<h3>{escape(name)}</h3><p>{escape(caption)}</p></div>
<span class="arrow">{icon("arrow-right")}</span></a>""")
    more_cards = "\n".join(
        f'<a href="{GIT}/{repo}"><strong>{escape(name)}</strong><span>{escape(trail)}</span></a>'
        for (name, repo), trail in zip(MORE, MORE_TEXT[lang].split(" | "), strict=True)
    )
    points = "".join(
        f'<a href="{href}">{icon(symbol)}<span><strong>{escape(t[key])}</strong><small>{escape(detail)}</small></span></a>'
        for key, href, symbol, detail in (
            ("federation", archived + "#architecture", "stack-2", capabilities_details[1]),
            ("scope", "#nano-core-agents", "gem", capabilities_details[0]),
            ("identity", GIT + "/APPROVAL-GATEWAY", "shield-check", capabilities_details[2]),
            ("audit", GIT + "/AUDIT-LEDGER", "database", "Audit Ledger"),
        )
    )
    capability_cards = "".join(
        f'<a href="{href}">{icon(symbol)}<span><strong>{escape(label)}</strong><small>{escape(detail)}</small></span></a>'
        for label, detail, href, symbol in zip(
            capabilities_labels, capabilities_details,
            ("#nano-core-agents", "#architecture", GIT + "/GUARDIAN-CORE", "#all-projects"),
            ("rocket", "topology-star-3", "shield-check", "gem"), strict=True
        )
    )
    candidate_links = {
        "business": CONTEST + "/blob/main/PRODUCT_BRIEF.md",
        "personal": CONTEST + "/blob/main/TRIPLE_CROWN.md#personal",
        "societal": CONTEST + "/blob/main/TRIPLE_CROWN.md#societal",
    }
    entries = "\n".join(f"""<article class="entry"><span class="track">{escape(t[track])}</span>
<h3>{escape(t[track + "Title"])}</h3><p>{escape(t[track + "Body"])}</p>
{link(t["evidence"], href)}</article>""" for track, href in candidate_links.items())
    crypto = " ".join(link(name, f"{GIT}/{repo}") for name, repo in (
        ("GitHub", "CRYPTO-IMPERIAL-Ecosystem-Public"), ("IMPERIUM", "IMPERIUM"), ("NDB", "N.D.B"),
        ("NZT", "NZT-"), ("LISA", "Lisa-"),
    ))
    founder_locale = lang.split("-")[0]
    founder_link = FOUNDER + suffix(founder_locale)
    graph = json.dumps(identity(lang, url, title, desc), ensure_ascii=False, separators=(",", ":"))
    scenes = escape(json.dumps(SCENES, separators=(",", ":")), quote=True)
    t = {k: escape(v) for k, v in t.items()}
    return f"""<!doctype html>
<html lang="{lang}" dir="{direction}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="author" content="Alexander Romaskevich">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0d0f12">
<link rel="canonical" href="{url}">
{alternates}
<link rel="alternate" hreflang="x-default" href="{HOST}{SHOWCASE}">
<link rel="icon" href="{ASSETS}showcase-gem.svg" type="image/svg+xml">
<link rel="stylesheet" href="{ASSETS}showcase.css?v=3">
<meta property="og:type" content="website">
<meta property="og:site_name" content="IMPERIAL Core">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{HOST}{DUBAI}terrace.webp">
<meta property="og:image:width" content="1536">
<meta property="og:image:height" content="864">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{graph}</script>
<script defer src="{ASSETS}showcase.js?v=3"></script>
</head>
<body>
<a href="#main-content" class="skip">{t["skip"]}</a>
<header class="masthead" id="top"><div class="wrap">
<a class="brand" href="{SHOWCASE}{current}"><img src="{ASSETS}showcase-gem.svg" width="39" height="39" alt=""><span>IMPERIAL <em>Core</em></span></a>
<nav class="main-nav" aria-label="{t["nav"]}">{nav}</nav>
<div class="bar-actions">
<details class="language"><summary aria-label="{t["languages"]} · {LANGUAGES[lang]}"><bdi>{lang.split("-")[0].upper()}</bdi></summary>
<div class="language-panel">{language_links}</div></details>
<details class="mobile-menu"><summary aria-label="{t["nav"]}">{icon("menu-2")}</summary><nav>{nav}</nav></details>
{link(access, "#contact", "btn btn-gold masthead-cta")}
</div>
</div></header>
<main id="main-content" tabindex="-1">
<section class="hero" data-scenes="{scenes}" aria-labelledby="hero-title">
  <div class="hero-media" aria-hidden="true">
    <img class="is-visible" src="{DUBAI}terrace.webp" srcset="{DUBAI}terrace-800.webp 800w, {DUBAI}terrace.webp 1536w" sizes="100vw" width="1536" height="864" alt="" fetchpriority="high" data-scene-root="{DUBAI}">
    <img sizes="100vw" width="1536" height="864" alt="" data-scene-root="{DUBAI}">
  </div>
  <div class="wrap hero-inner"><h1 id="hero-title">{t["hero1"]} <span>{t["hero2"]}</span></h1>
    <p>{t["intro"]}</p>
    <div class="actions">{link(COPY[lang]["explore"], "#official-projects", "btn btn-gold")}
    {link(overview, "#architecture", "btn btn-outline", False)}</div>
  </div>
  <div class="wrap carousel" role="group" aria-label="{t["views"]}" hidden>
    <button type="button" data-previous aria-label="{t["previous"]}">{icon("arrow-left")}</button>
    <output aria-live="off">1 / 6</output>
    <button type="button" data-next aria-label="{t["next"]}">{icon("arrow-right")}</button>
    <button type="button" data-playback data-play="{t["play"]}" data-pause="{t["pause"]}" aria-label="{t["play"]}">{icon("player-play")}</button>
  </div>
</section>
<nav class="wrap principles" aria-label="{t["architecture"]}">{principle_links}</nav>
<section class="wrap section" id="official-projects">
  <div class="section-head"><h2>{t["portfolioTitle"].replace("IMPERIAL Core", "<em>IMPERIAL Core</em>")}</h2>{link(COPY[lang]["all"], "#all-projects")}</div>
  <div class="cards">{"".join(cards[:len(feature_labels)])}</div>
</section>
<section class="wrap section" id="architecture">
  <div class="architecture">
  <figure class="architecture-art"><img src="{ART}architecture.webp" width="1160" height="580" alt="" loading="lazy" decoding="async"></figure>
  <div><p class="eyebrow">{escape(highlights)}</p><h2>{t["architectureTitle"]}</h2><p>{t["architectureBody"]}</p>
  <div class="architecture-points">{points}</div></div></div>
</section>
<section class="wrap section capabilities" id="capabilities">
  <div class="section-head"><h2>{escape(capabilities)}</h2>{link(COPY[lang]["reference"], archived, extra=" data-legacy")}</div>
  <div class="capability-grid">{capability_cards}</div>
</section>
<section class="closing" id="contact"><div class="wrap"><h2>{t["ctaTitle"].replace("IMPERIAL Core", "<em>IMPERIAL Core</em>")}</h2>
{link(COPY[lang]["contact"], "mailto:oromaskevic23@gmail.com", "btn btn-gold")}</div></section>
<section class="wrap section" id="all-projects">
  <div class="section-head"><h2>{t["moreTitle"]}</h2>{link(COPY[lang]["all"], SHOWCASE + "projects/")}</div>
  <p class="section-lead">{t["moreIntro"]}</p>
  <div class="cards extra-cards">{"".join(cards[len(feature_labels):])}</div>
  <details class="more"><summary>{t["all"]}</summary><div class="more-grid">{more_cards}</div>
  <aside class="crypto"><h3>{t["cryptoTitle"]}</h3><p>{t["cryptoBody"]}</p><nav aria-label="{t["cryptoTitle"]}">{crypto}</nav></aside></details>
  <div class="statement"><img src="{DUBAI}digital-diamond.webp" width="150" height="150" alt="" loading="lazy" decoding="async">
  <div><blockquote>{t["digitalQuote"]}</blockquote><p>{t["digitalBody"]}</p></div></div>
  <p class="governance-boundaries"><bdi>AI Passport · Enterprise Skills · Guardian Core · Approval Gateway · Audit Ledger · Zero Trust · Owner Kill Switch · Public/Private Boundary · CRYPTO IMPERIAL Ecosystem Boundary</bdi></p>
</section>
<section class="dubai" id="dubai-2027"><div class="wrap section">
  <h2>{t["dubaiTitle"]}</h2><p class="section-lead">{t["dubaiIntro"]}</p>
  <div class="entries">{entries}</div>
  <div class="actions">{link(COPY[lang]["walkthrough"], FOUNDER + "dubai-2027/", "btn btn-gold")}
  {link(COPY[lang]["candidateEvidence"], CONTEST + "/blob/main/TRIPLE_CROWN.md", "btn btn-outline")}</div>
</div></section>
<section class="wrap section founder" id="architect">
  <figure class="portrait"><img src="{DUBAI}alexander-romaskevich.webp" width="900" height="1125" alt="Alexander Romaskevich" loading="lazy" decoding="async"></figure>
  <div class="founder-bio"><p class="founder-title">{t["founderTitle"]}</p><h2><bdi>Alexander Romaskevich</bdi></h2>
  <p class="founder-role">{t["role"]}</p></div>
  <div class="founder-details"><p>{t["founderBody"]}</p>
  <p><bdi>Александр Николаевич Ромаскевич · RomaskevicH</bdi></p>
  <div class="actions">{link(COPY[lang]["founderProfile"], founder_link, "btn btn-outline", True, ' rel="author"')}
  {link(COPY[lang]["engineering"], FOUNDER + "engineering/", "btn btn-outline")}</div></div>
</section>
</main>
<footer class="site-footer"><div class="wrap">
<p><bdi>IMPERIAL Core</bdi> · {t["footerArchitecture"]}</p>
<nav aria-label="{t["reference"]}">{link(COPY[lang]["reference"], archived)}
{link("GitHub", GIT)} {link(COPY[lang]["evidence"], GIT + "/oromaskevic23-cmd/blob/main/docs/UNIFIED_ECOSYSTEM_EVIDENCE.md")}</nav>
</div></footer>
<dialog id="project-dialog" aria-labelledby="project-title">
  <img class="dialog-image" alt="" width="800" height="450">
  <button class="dialog-close" type="button" aria-label="{t["close"]}" autofocus>×</button>
  <div class="dialog-copy"><h2 id="project-title"></h2><p></p><div class="actions">
  <a class="btn btn-gold dialog-project">{t["project"]} <span class="arrow">{icon("arrow-up-right")}</span></a>
  <a class="btn btn-outline dialog-demo" hidden>Template Studio <span class="arrow">{icon("arrow-up-right")}</span></a>
  </div></div>
</dialog>
</body>
</html>
"""


def archive_originals():
    for lang in LANGUAGES:
        folder = suffix(lang)
        old = REFERENCE / folder / "index.html"
        archive = REFERENCE / "technical" / folder / "index.html"
        archive.parent.mkdir(parents=True, exist_ok=True)
        if archive.exists():
            continue
        original = old.read_text()
        assert "reference/assets/reference.css" in original, old
        markup = re.sub(r'<meta name="robots" content="[^"]*">', '<meta name="robots" content="noindex,follow">', original, count=1)
        markup = re.sub(r'<link rel="(?:canonical|alternate)"[^>]*>', "", markup)
        markup = markup.replace(f'href="{SHOWCASE}" lang="en"', f'href="{SHOWCASE}technical/" lang="en"')
        markup = re.sub(rf'href="{SHOWCASE}([^/]+)/" lang=', rf'href="{SHOWCASE}technical/\1/" lang=', markup)
        archive.write_text(markup)


def update_manifest():
    path = REFERENCE / "publication-manifest.json"
    old = json.loads(path.read_text())
    assets = [p for p in (REFERENCE / "assets").glob("showcase*") if p.is_file()]
    assets += list((REFERENCE / "assets/dubai").glob("*.webp"))
    assets += list((REFERENCE / "assets/showcase").glob("*.webp"))
    assets += list((REFERENCE / "assets").glob("*LICENSE.txt")) + list((REFERENCE / "assets").glob("*OFL.txt"))
    tracked = {entry["path"] for entry in old["files"]}
    tracked.update(p.relative_to(REFERENCE).as_posix() for p in assets)
    tracked.update(p.relative_to(REFERENCE).as_posix() for p in (REFERENCE / "technical").rglob("index.html"))
    tracked.update(f"{suffix(lang)}index.html" for lang in LANGUAGES)
    old.update(date="2026-11-23", brand="digital-diamond")
    old["files"] = [
        {"path": name, "sha256": hashlib.sha256((REFERENCE / name).read_bytes()).hexdigest()}
        for name in sorted(tracked) if (REFERENCE / name).is_file()
    ]
    path.write_text(json.dumps(old, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive-originals", action="store_true")
    args = parser.parse_args()
    if args.archive_originals:
        archive_originals()
    for lang in LANGUAGES:
        (REFERENCE / suffix(lang) / "index.html").write_text(render(lang))
    update_manifest()


if __name__ == "__main__":
    main()
