# IMPERIAL Core — Sovereign Dubai Visual Redesign
Date: 2026-11-22
Owner: Alexander Nikolaevich Romaskevich · Founder · Owner · CEO
Status: PROPOSED on `design/imperial-sovereign-reference-v2-20261122` before merge.

## Directive
Rebuild IMPERIAL Core's GitHub Pages homepage toward the owner's supplied Dubai premium reference: large cinematic Dubai photo, serif title, gold icon strip, six rich technology cards, architecture graphic, four capabilities, tasteful gold-framed original Founder portrait in **The Architect** section below the hero, and a direct contact CTA. No likeness-generating algorithms or substituted founder portrait.

## Source boundaries
- Existing `gh-pages` HTML for 10 languages stays unchanged.
- Canonical diamond `assets/imperial-core-diamond-20261116.jpg` is loaded without modification.
- Original founder photo `assets/alexander-romaskevich-portrait.jpeg` is reused at its native 1122×1402 resolution. Never use the previously generated fictional portrait.
- Original footer, original evidence content, SEO metadata, canonical/alternate links, bilingual navigation and engineering disclosures remain in place.
- No change to Capital Core brand or site, no Val Town, no payments or backend/AI runtime access.

## New visual layer
- `assets/imperial-sovereign.css`: mobile-first premium Dubai design, six-card technology module grid, gold Founder frame, four trust principles, accessibly sized controls and reduced-motion support.
- `assets/imperial-sovereign.js`: original SVG graphics and click-through links. Uses the existing original language locale in each of 10 translations, without editing locale HTML. The new hero does **not** contain the founder photograph.
- `assets/site.js`: replaces the prior four-scene experimental loader with the sovereign design files; only enhances `body.ecosystem`.

## Real repository / evidence links
- HANTER: https://github.com/oromaskevic23-cmd/HANTER-Public
- VELION: https://github.com/oromaskevic23-cmd/VELION-LLM-Public
- Nano Core Agents: https://github.com/oromaskevic23-cmd/Nano-Core-Agents-Public
- CYBER HAK: https://github.com/oromaskevic23-cmd/CYBER-HAK-Public
- AI Passport concept: https://github.com/oromaskevic23-cmd/oromaskevic23-cmd/blob/main/docs/AI_PASSPORT_CONCEPT.md
- AGY: https://github.com/oromaskevic23-cmd/AGY
- Company engineering evidence: https://oromaskevic23-cmd.github.io/oromaskevic23-cmd/engineering/
- Founder profile: https://oromaskevic23-cmd.github.io/oromaskevic23-cmd/

## QA evidence (executed in isolated Chromium)
- [x] Real HTML plus candidate JS/CSS via request substitution: all 3 candidate assets returned HTTP 200 and loaded successfully.
- [x] 10 actual language routes: `en/ru/uk/de/fr/es/pt/ja/zh/ar`. Exactly 6 module cards and 6 top capability icons on each, each card links to an official GitHub source, no legacy four-scene buttons, and no horizontal overflow at 390 px.
- [x] Arabic retains right-to-left document direction.
- [x] Desktop and mobile viewport checks: 360, 390, 768, 1440, 1920 px. No horizontal overflow. The original Founder image remains sourced from the existing asset.
- [x] Founder section visually inspected in Chromium: photo is not in hero, intrinsic 1122×1402, displayed in layered gold frame; desktop grid has portrait LEFT and Architect text RIGHT.
- [x] JavaScript compiles and CSS brace balance verified.
- [x] All original 10 locale HTML files and existing brand binary files unchanged by the Git diff.
- [ ] Physical iPhone Safari / touch test not executed.
- [ ] Independent design review not executed.
- [ ] Final production GitHub Pages response test pending merge.

## Visual provenance / third-party image boundary
Decorative photographs only. The hero and sunset CTA use Pexels Popoy Dev photo `12462486`:
https://www.pexels.com/photo/burj-khalifa-in-dubai-12462486/
under Pexels' published free-to-use terms. Some cards use freely accessible Unsplash photos; existing first-party AI Passport art is unchanged. Third-party CDN requests carry privacy and availability implications; a production self-hosted replacement is a future improvement. Photography and diagram imagery do not claim a deployed real-time AI control center, customer engagement, or externally certified capabilities.

## Release gates
- Keep changed paths limited to new styling, new first-party JS, loader and this evidence note.
- No production success claim until merged `gh-pages` is served over the public URL and the 10 languages and original portrait survive the live check.
