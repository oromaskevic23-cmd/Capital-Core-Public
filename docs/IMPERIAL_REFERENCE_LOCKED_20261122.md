# IMPERIAL Core — Reference-Locked Homepage Correction

Date: 2026-11-22
Authority: Alexander Nikolaevich Romaskevich · Founder · Owner · CEO
Mode: EXISTING WEBSITE / GITHUB PAGES / FREE_ONLY

## Locked visual reference
User-supplied original: 1122×1402 screenshot with luxury Dubai rooftop and infinity pool, serif headline, six gold-icon features, two rows of six technology modules, architecture and four capability panels, concluding Dubai banner.

## What changed
- Replaces the previously overcomplicated homepage visual treatment with only the content sections visible in the user's reference: hero, 6 capability icons, 6 module cards, 1 architecture panel, 4 enterprise capabilities and 1 closing call-to-action.
- Decorative gold diamond appears correctly inside header. Original canonical icon file is untouched.
- **No Founder photo, no human likeness, no award badge and no extra people anywhere on this homepage.** Existing original founder photograph remains in the source file, unedited and not displayed on the landing page. This avoids the earlier accidental fictional portrait.
- Scenic rooftop look uses licensed external stock photos for sky and lounge, with original SVG roof/sofa/diamond/pool decoration. It is an implementation approximating the screenshot photo, not a claim to be a pixel-identical photograph.
- All six main cards are clickable and point to existing GitHub repositories / AI Passport documentation.
- Header navigation has 6 working destinations. 'Platform Overview' goes to the visible architecture section; no fictional overview video is claimed.
- Original ten locale HTML files retained, other than replacing **only** a version query parameter on the common script URL to prevent cached older releases.
- Existing original engineering evidence, SEO metadata and i18n source contents remain in the repository, untouched.

## Public evidence links verified with connected GitHub
- HANTER: https://github.com/oromaskevic23-cmd/HANTER-Public
- VELION: https://github.com/oromaskevic23-cmd/VELION-LLM-Public
- Nano Core Agents: https://github.com/oromaskevic23-cmd/Nano-Core-Agents-Public
- CYBER HAK: https://github.com/oromaskevic23-cmd/CYBER-HAK-Public
- AI Passport documentation: https://github.com/oromaskevic23-cmd/oromaskevic23-cmd/blob/main/docs/AI_PASSPORT_CONCEPT.md
- AGY: https://github.com/oromaskevic23-cmd/AGY
- Zero Trust: https://github.com/oromaskevic23-cmd/ZERO-TRUST
- Audit Ledger: https://github.com/oromaskevic23-cmd/AUDIT-LEDGER

## Visual resources
- Pexels Dubai rooftop skyline by Popoy Dev, Free to use: https://www.pexels.com/photo/burj-khalifa-in-dubai-12462486/
- Pexels warm lounge photo, Free to use: https://www.pexels.com/photo/inteirior-design-of-room-19074480/
- No use of the incorrect generated portrait. Card and architecture decorations are local SVG embedded in the application code.

## Executed tests (not hypothetical)
- Actual Chromium, draft assets substituted into the existing public GitHub Pages DOM, all 10 locales: en, uk, ru, de, fr, es, pt, ja, zh and ar.
- Each locale renders 6 module links, 6 capability icons, 6 navigation links, zero legacy flight-scene buttons, no visible founder/person image, decorative gold diamond, and no horizontal overflow at 390 px.
- Arabic keeps RTL document direction.
- Viewports 360, 390, 768, 1100, 1440, 1920 px: no horizontal overflow, 6 cards each, hidden legacy founder photo.
- Header icon bounds checked at desktop and confirmed inside the header after the earlier CSS positioning collision was fixed.
- Candidate CSS/JS scripts available via HTTP 200 through GitHub raw and loaded in the isolated browser.
- No actual iPhone Safari device QA or independent visual certification claimed.

## Release
Post-merge check required: published URL (with uncached query), 6 module links, header symbol and locale routes. If GitHub Pages CDN lags, do not claim the live site is updated until verified.
