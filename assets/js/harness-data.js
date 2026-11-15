// The harness data that is the same on every page of a build, written ONCE
// here instead of into each page (bean `gp2f`, page weight). Measured on
// gh-pages 1ad53fa, 2026-10-23: the tiles list was 12.5 KB and the navbar icon
// row 2.5 KB of every Jekyll page, about 15 KB of a 42 KB page.
//
// `head_custom.html` keeps the two places the readers look, empty, and loads
// this as the FIRST deferred script. Deferred scripts run in document order,
// so `navbar-row.js` and `docs-ui.js` find them filled, exactly as when the
// data was inlined. If this file does not load, the islands stay named and
// empty, and the readers report a failed load instead of "declared none".
(function () {
  var row = document.getElementById("fa-navbar-row");
  if (row && row.getAttribute("data-fa-row-src") === "harness-data" && !row.textContent) {
    row.textContent = "{\"icons\":[\"close\",\"qr\",\"launcher\"],\"hrefs\":{},\"notes\":{},\"folders\":[{\"kind\":\"archimate\",\"label\":\"Archimate\",\"path\":\"/en/dpi-h-ra/archimate/\"},{\"kind\":\"beans\",\"label\":\"Plans and work\",\"note\":\"dpi-h-ra's beans graph is not published on this site\"},{\"kind\":\"folio\",\"label\":\"Folio\",\"path\":\"/en/dpi-h-ra/\"},{\"kind\":\"fsh-guts\",\"label\":\"FSH guts\",\"stagingOnly\":true,\"path\":\"https://litlfred.github.io/folio-assistant/en/cat-harness/fsh-guts/\"},{\"kind\":\"glossary\",\"label\":\"Glossary\",\"note\":\"no viewer yet\"},{\"kind\":\"library\",\"label\":\"Library\",\"path\":\"https://litlfred.github.io/folio-assistant/en/cat-harness/library/dpi-h-ra/\"},{\"kind\":\"references\",\"label\":\"References\",\"note\":\"no viewer yet\"},{\"kind\":\"todo-items\",\"label\":\"Todo items\",\"note\":\"dpi-h-ra's todo-items graph is not published on this site\"},{\"kind\":\"uploads\",\"label\":\"Uploads\",\"note\":\"dpi-h-ra's uploads graph is not published on this site\"}]}";
    row.removeAttribute("data-fa-row-src");
  }
  var tiles = document.querySelector('meta[name="fa-tiles"][data-fa-src="harness-data"]');
  if (tiles && !tiles.getAttribute("content")) {
    tiles.setAttribute("content", "[{\"id\":\"archimate\",\"directory\":\"archimate\",\"title\":\"Archimate\",\"qualifier\":\"Reference Architecture and Guidance for Digital Public Infrastructure for the Health Sector\",\"ref\":\"docs/en/dpi-h-ra/archimate/index.html\",\"surfaces\":[\"navbar\",\"board\",\"glass\"],\"hidden\":false},{\"id\":\"folio\",\"directory\":\"folio\",\"title\":\"The document\",\"qualifier\":\"Reference Architecture and Guidance for Digital Public Infrastructure for the Health Sector\",\"ref\":\"en/dpi-h-ra/index.html\",\"surfaces\":[\"navbar\",\"board\",\"glass\"],\"hidden\":false},{\"id\":\"library\",\"directory\":\"library\",\"title\":\"Library\",\"qualifier\":\"Reference Architecture and Guidance for Digital Public Infrastructure for the Health Sector\",\"ref\":\"en/folio-assistant-core/library/index.html\",\"surfaces\":[\"navbar\",\"board\",\"glass\"],\"hidden\":false,\"icon\":\"library\"},{\"id\":\"public-comments\",\"directory\":\"public-comments\",\"title\":\"Public comments\",\"qualifier\":\"Reference Architecture and Guidance for Digital Public Infrastructure for the Health Sector\",\"ref\":\"en/folio-assistant-core/public-comments/folio/dpi-h-ra/index.html\",\"surfaces\":[\"navbar\",\"board\",\"glass\"],\"hidden\":false}]");
    tiles.removeAttribute("data-fa-src");
  }
})();
