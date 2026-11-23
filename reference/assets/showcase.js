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

  // Preserve bookmarks into the technical material from the previous homepage.
  const legacySection = /^#(?:section-(?:[1-9]|[12]\d|30)|cheat-sheet|infrastructure|development|capital-core|nca-always-on|reference-sections|reference-search)$/;
  if (legacySection.test(location.hash)) {
    const legacy = new URL(document.querySelector("[data-legacy]").href);
    legacy.hash = location.hash;
    location.replace(legacy);
  }
})();
