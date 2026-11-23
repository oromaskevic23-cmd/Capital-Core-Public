(() => {
  "use strict";

  const hero = document.querySelector(".hero");
  const gallery = document.querySelector(".carousel");
  const pictures = [...hero.querySelectorAll(".hero-media img")];
  const scenes = JSON.parse(hero.dataset.scenes);
  const output = gallery.querySelector("output");
  const playback = gallery.querySelector("[data-playback]");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const dialog = document.querySelector("#project-dialog");
  let current = 0;
  let timer = null;
  let pending = 0;
  let transition = Promise.resolve();
  let previousTrigger = null;

  function showScene(index) {
    const request = ++pending;
    const scene = scenes[(index + scenes.length) % scenes.length];
    transition = transition.catch(() => {}).then(async () => {
      if (request !== pending || scenes[current] === scene) return;
      const shown = pictures.find((picture) => picture.classList.contains("is-visible"));
      const incoming = pictures.find((picture) => picture !== shown);
      const url = new URL(shown.dataset.sceneRoot, document.baseURI);
      incoming.srcset = `${new URL(scene + "-800.webp", url)} 800w, ${new URL(scene + ".webp", url)} 1536w`;
      incoming.src = new URL(scene + ".webp", url);
      try {
        await incoming.decode();
      } catch {
        return;
      }
      if (request !== pending) return;
      incoming.classList.add("is-visible");
      shown.classList.remove("is-visible");
      current = scenes.indexOf(scene);
      output.value = `${current + 1} / ${scenes.length}`;
      if (!reduceMotion.matches) {
        await new Promise((resolve) => window.setTimeout(resolve, 875));
      }
    });
  }

  function setPlaying(playing) {
    if (timer !== null) window.clearInterval(timer);
    timer = playing
      ? window.setInterval(() => { if (!document.hidden && !dialog.open) showScene(current + 1); }, 10500)
      : null;
    playback.setAttribute("aria-label", playback.dataset[playing ? "pause" : "play"]);
    playback.textContent = playing ? "Ⅱ" : "▷";
    output.setAttribute("aria-live", playing ? "off" : "polite");
  }

  gallery.querySelector("[data-previous]").addEventListener("click", () => {
    setPlaying(false);
    showScene(current - 1);
  });
  gallery.querySelector("[data-next]").addEventListener("click", () => {
    setPlaying(false);
    showScene(current + 1);
  });
  playback.addEventListener("click", () => setPlaying(timer === null));
  reduceMotion.addEventListener("change", () => { if (reduceMotion.matches) setPlaying(false); });
  gallery.hidden = false;
  setPlaying(!reduceMotion.matches);

  if (typeof dialog.showModal === "function") {
    for (const trigger of document.querySelectorAll("a[data-scene]")) {
      trigger.addEventListener("click", (event) => {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        setPlaying(false);
        showScene(scenes.indexOf(trigger.dataset.scene));
        previousTrigger = trigger;
        dialog.querySelector(".dialog-image").src = trigger.dataset.panorama;
        dialog.querySelector("h2").textContent = trigger.querySelector("h3").textContent;
        dialog.querySelector("p").textContent = trigger.querySelector("p").textContent;
        dialog.querySelector(".dialog-project").href = trigger.href;
        const demo = dialog.querySelector(".dialog-demo");
        demo.hidden = !trigger.dataset.demo;
        if (trigger.dataset.demo) demo.href = trigger.dataset.demo;
        dialog.showModal();
      });
    }
    dialog.querySelector(".dialog-close").addEventListener("click", () => dialog.close());
    dialog.addEventListener("close", () => previousTrigger?.focus({ preventScroll: true }));
    dialog.addEventListener("click", (event) => { if (event.target === dialog) dialog.close(); });
  }

  const language = document.querySelector(".language");
  document.addEventListener("pointerdown", (event) => { if (!language.contains(event.target)) language.open = false; });
  language.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && language.open) {
      language.open = false;
      language.querySelector("summary").focus();
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
