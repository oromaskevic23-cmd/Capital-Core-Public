# IMPERIAL Core — Dubai-Ready Immersive Website Redesign
Date: 2026-11-22  
Status: PROPOSED / BRANCH ONLY. This is not a live-production release.

## Scope and visual design
- Existing IMPERIAL Core site published from `gh-pages`; redesign is isolated to `design/imperial-dubai-immersive-20261122`.
- 4 selectable scenes: Dubai Skyline, Skyscraper, Freefall visualization, AI Command Center.
- Cinematic photography, midnight-blue / warm-gold glass UI, responsive hero, premium cards, and original founder portrait inside a layered gold frame.
- Existing owner-selected diamond and founder photo are referenced in place; source files are not modified.
- All 10 language HTML files and the existing language selector, profile schema, canonical links, product content, and architectural disclosures remain unchanged.
- The flight scene is an illustrative visual experience, **not** actual skydiving or real-time 3D footage.

## Modified files
- `assets/imperial-experience.css`: scene and layout styles including reduced-motion and mobile.
- `assets/imperial-experience.js`: view-switch buttons, keyboard navigation, visuals, no analytics.
- `assets/site.js`: progressively loads the optional feature only for `body.ecosystem`.
- This evidence document.

## Evidence run in connected GitHub / JS execution
- Commit: `42d86a1533f5f7613be551dc8bb1fe11f5d40f8f`.
- JS syntax: parsed (PASS).
- CSS braces: balanced (PASS).
- Simulated DOM runtime: ran without exception; four buttons selected the matching scene and exposed `aria-pressed` correctly; 12 scripted assertions (PASS).
- GitHub diff checked: only three implementation files in original commit; locale pages and binary assets unchanged.
- External photography requests have an image-load error fallback to the existing local diamond banner.
- **Not yet verified:** full Chromium/iOS visual regressions, live CDN image response status, mobile Safari layout, independent accessibility audit, live deployment. No production PASS is claimed.

## Media and privacy boundaries
- Dubai-themed scene images are loaded from `images.unsplash.com` by the visitor's browser. This is an external network dependency; consider self-hosting optimized files before production.
- Image identifiers: `photo-1512453979798-5ea266f8880c` (Dubai skyline), `photo-1546412414-e1885259563a` (Dubai architecture), `photo-1526495124232-a04e1849168c` (Dubai aerial visual).
- Unsplash licensing reference: https://unsplash.com/license . Do not claim endorsements by any image owner, landmark, or organization.
- No API keys, contact data, private runtime, surveillance, payment processing, or token action is involved.

## Acceptance checklist before production
- [ ] Visually compare at widths 375, 768, 1440 and 1920 px.
- [ ] Test all 10 language routes including RTL Arabic, menu, project links, CTA and footer.
- [ ] Validate source images load, alt text, focus rings, keyboard controls and reduced motion.
- [ ] Confirm photo remains recognizable, with no generated face or crop damage.
- [ ] Confirm existing HANTER / VELION / NCA / Guardian / Audit / Crypto boundary wording remains unaltered.
- [ ] Human review of visual preview and approval to merge to the publishing branch.

**Founder and final architectural authority:** Alexander Nikolaevich Romaskevich — Founder · Owner · CEO.
