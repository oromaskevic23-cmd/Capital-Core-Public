(() => {
  "use strict";

  const disclosures = [...document.querySelectorAll(".language, .mobile-menu")];
  for (const disclosure of disclosures) {
    disclosure.addEventListener("click", (event) => {
      if (event.target.closest("a")) disclosure.open = false;
    });
    disclosure.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && disclosure.open) {
        disclosure.open = false;
        disclosure.querySelector("summary").focus();
      }
    });
  }
  document.addEventListener("pointerdown", (event) => {
    for (const disclosure of disclosures) {
      if (!disclosure.contains(event.target)) disclosure.open = false;
    }
  });

  const catalogue = document.querySelector(".landscape-catalogue");
  const frames = [...catalogue.querySelectorAll(".landscape-frame")];
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  let pending = false;

  function paintLandscapes() {
    pending = false;
    const bounds = catalogue.getBoundingClientRect();
    const viewport = window.innerHeight;
    const progress = Math.min(1, Math.max(0, (viewport * 0.52 - bounds.top) / (bounds.height + viewport * 0.12)));
    const position = reducedMotion.matches ? 0 : progress * (frames.length - 1);
    const current = Math.floor(position);
    const fraction = position - current;
    const blend = fraction * fraction * (3 - 2 * fraction);
    const base = frames[current].naturalWidth ? current : 0;
    frames.forEach((frame, index) => {
      const opacity = index === base ? "1" : index === current + 1 && frame.naturalWidth ? blend.toFixed(3) : "0";
      if (frame.style.opacity !== opacity) frame.style.opacity = opacity;
    });
  }

  function scheduleLandscapes() {
    if (pending) return;
    pending = true;
    window.requestAnimationFrame(paintLandscapes);
  }

  window.addEventListener("scroll", scheduleLandscapes, { passive: true });
  window.addEventListener("resize", scheduleLandscapes, { passive: true });
  reducedMotion.addEventListener("change", scheduleLandscapes);
  frames.forEach(frame => frame.addEventListener("load", scheduleLandscapes));
  paintLandscapes();

  // Preserve bookmarks into the technical material from the previous homepage.
  const legacySection = /^#(?:section-(?:[1-9]|[12]\d|30)|cheat-sheet|infrastructure|development|capital-core|nca-always-on|reference-sections|reference-search)$/;
  if (legacySection.test(location.hash)) {
    const legacy = new URL(document.querySelector("[data-legacy]").href);
    legacy.hash = location.hash;
    location.replace(legacy);
  }
})();
