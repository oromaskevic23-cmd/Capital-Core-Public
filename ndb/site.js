"use strict";

const artView = document.querySelector("#coin-view");
const tabs = document.querySelectorAll("[data-view]");

for (const tab of tabs) {
  tab.addEventListener("click", () => {
    artView.src = `/Capital-Core-Public/ndb/assets/ndb-${tab.dataset.view}.webp`;
    artView.alt = tab.dataset.imageAlt;
    for (const option of tabs) option.setAttribute("aria-pressed", String(option === tab));
  });
}

for (const button of document.querySelectorAll("[data-copy]")) {
  button.addEventListener("click", async () => {
    const source = document.getElementById(button.dataset.copy);
    const status = document.getElementById(button.dataset.status);
    try {
      await navigator.clipboard.writeText(source.textContent.trim());
      status.textContent = button.dataset.success;
    } catch {
      const range = document.createRange();
      range.selectNodeContents(source);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      status.textContent = button.dataset.fallback;
    }
  });
}
