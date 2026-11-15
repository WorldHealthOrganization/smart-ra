# ArchiMate models visualiser — as-is intent

**Covers:** `en/dpi-h-ra/archimate/index.html` (declared visualiser `dpi-h-ra/archimate`). It is the `coverage.visualiser[0].ref` (title "ArchiMate models") of the `archimate` directory (`path: archimate/`, graph typology `archimate`) in `dpi-h-ra.json`, and the instance's `visualisers` entry `{ "id": "archimate", "renderedBy": "archimate-pages", "covers": ["archimate"] }`. The site build's `site:archimate` step writes it with `cat-harness-tools/archimate/scripts/gen-archimate-pages.ts --instance . --out <site>`, from the models `archimate/cat-archimate.config.json` names. It is static HTML; each model's own page loads its content from JSON-LD and needs JavaScript.

**Who it is for:** a reader of the DPI-H reference architecture, or a reviewer of its public-comment draft, who wants the ArchiMate model behind a figure, and a maintainer checking which model versions are published.

**What they need to do:**
- see which ArchiMate models the reference architecture publishes, and which one is current (the folder named for the IG's `version:` in `sushi-config.yaml`; `archimate/README.md`)
- compare the versions by size: views and elements per model
- open one model, and from it its views (drawn as SVG), its elements by layer and its relationships

**What it must show** (from the generator): the heading "ArchiMate models", then one row per configured model in config order, each the model's title as a link to `<id>/`, its id in code type, and its view and element counts. The page carries a `data-fa-visualiser-nav` block, from which the site's navbar draws the same list. A model that is not named in the config (such as the source model held in `library/dpi4health-hrh-archimate/`) is not listed.

## Observed (built from main, 2026-10-15)

Rendered at 1280×800 and 390×844 from `bun run site:archimate <out>`:

1. `h1` "ArchiMate models".
2. A list of four models: "WHO Reference Architecture 0.2.0" (`0.2.0`, 20 views, 258 elements), "… 0.2.0-draft.3" (33 views, 1132 elements), "… 0.2.0-draft.2" (32 views, 535 elements), "… 0.2.0-draft.1" (46 views, 611 elements).

Nothing on the page says which model is current; the order is the config's, which puts the current one first. That is a finding for the visualiser, not for this drawing: a reader who does not know the config cannot tell "first" from "current".

At 390 px each row wraps under its link and nothing scrolls sideways.
