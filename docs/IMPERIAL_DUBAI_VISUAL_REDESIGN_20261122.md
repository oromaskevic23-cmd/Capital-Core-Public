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


## Verified follow-up — 2026-11-22

### Corrections integrated into the draft PR

- Original illustrated first-party skyline fallback added as `assets/imperial-skyline-fallback.svg`. It is used when external scene images fail to load.
- Original owner-approved diamond is referenced directly from `assets/imperial-core-diamond-20261116.jpg`. Its source asset and SHA remain unchanged.
- Redundant legacy hero banner suppressed in enhanced view through CSS only; the file remains intact.
- The mobile parachute overlay was moved below the introductory text and reduced in size/opacity to avoid collisions.
- Existing founder portrait `assets/alexander-romaskevich-portrait.jpeg` remains unmodified, with layered gold-frame presentation.
- All 10 language HTML pages are still unchanged.

### Reproducible execution evidence

| Verification | Observed outcome | Limit |
| --- | --- | --- |
| JavaScript simulated DOM across 10 locales | **292/292** in-memory assertions PASS: scene state, button exclusivity, keyboard arrows, captions, broken-image fallback and stale image request handling | V8 simulation, not an actual browser |
| Browser responsive sweep | Chromium **360, 390, 768, 1440, 1920 px**: four buttons present, no horizontal overflow, scene modes switch | Chromium browser; actual iOS Safari not checked |
| Locale smoke in browser | `en`, `ru`, `ar` (RTL), `ja`, `zh` at 390 px: distinct four scenes, no horizontal overflow, and portrait URL preserved | Remaining five locales checked by source and simulated DOM only |
| Reduced-motion | `prefers-reduced-motion: reduce` disables parachute animation; scene transition duration becomes near-zero | Chromium environment only |
| Founder portrait | Source image loaded successfully, native resolution **1122×1402**, framed width **400 px** at desktop preview | Manual browser view, no formal visual-diff baseline |
| Real page asset loader | Tested original live HTML with draft branch `assets/site.js`, stylesheet and scene script injected via browser request interception. CSS and JS both loaded, 4 buttons rendered | Isolated browser simulation of release, **not** an actual preview deployment |
| Asset integrity | GitHub branch diff examined; original diamond and portrait files, translations and canonical links untouched | No independent external design certification |

The live-page browser harness fetched **candidate assets from the GitHub draft branch**, rendered them onto the existing public DOM in an isolated browser, and checked responsive states. This is not a production release or evidence of iOS Safari QA.

### Known operational constraints

- External photographic scenes currently use Unsplash URLs; the original first-party vector illustration provides deterministic fallback. External image loading may disclose the visitor's IP address to the image host.
- Interface labels are unchanged for the existing localized body content; only the new four visual-scene controls use already-supplied translations.
- No real skydiving, parachute telemetry, 3D simulator, payment, blockchain transaction, or production AI runtime is implied by these decorative scenes.
- Free-tier-only browser and GitHub verification. No paid deployment, Val Town, secrets, or production APIs used.
- Production publication must be verified by loading the **actual** GitHub Pages URL after a governed merge, and rolled back if critical navigation, hero or language switching fails.

### Engineering acceptance after browser QA

- [x] Show canonical diamond without re-drawing it
- [x] Keep original founder portrait and the ten language HTML files
- [x] Four clickable scene buttons and mobile responsive layout
- [x] Verify browser rendering at representative widths and five locale routes
- [x] Confirm fallback SVG and reduced-motion preference
- [x] Verify progressive loader in isolated browser
- [ ] Real iPhone Safari device verification
- [ ] Production URL check after release/merge
