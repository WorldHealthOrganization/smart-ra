# ArchiMate models — one folder per version, named by SemVer

Each folder holds one `.archimate` model (Archi native XML or a zipped Archi
archive) and is named for the version of this IG it belongs to — the
`version:` in `sushi-config.yaml`. Nothing else says which one is current:
the folder whose name equals that `version:` is.

| folder | model | where it came from |
|---|---|---|
| `0.3.0-draft.1/` | `WHO_RA` plus the supply chain views (DTH SC Figs. 1-3, 14, 24) and the RA's Integrated View (Figs. 3.2, 3.5) | made from `0.2.0/` by `tools/archimate-dth/add_views.py` with `dth_sc.py`, then `dpi_h_integrated.py` (which also renames 15 elements to the RA's names, keeping `formerName`); draft. The NHWA items it had carried over from the old 0.2.0 (CDE-HWR, NHWA Dataset, their 7 relationships and 2 notes) were taken out on 2026-11-01: the owner ruled that NHWA is not part of smart-ra, and they live in the dth-hrh overlay |
| `0.2.0/` | `WHO_RA` — 20 views, incl. Testing and Conformance | `v3/` (and its byte-identical copy `v2/`), 2026-07-09 |
| `0.2.0-draft.3/` | `WHO Models` | `v1/` |
| `0.2.0-draft.2/` | `WHO Reference Architecture` | `prev1/` |
| `0.2.0-draft.1/` | `WHO Models` | `prev2/` — "WHO Reference Architecture Draft v.2 - 6.2.2026" |

The `draft.N` order is the order the previous folder names gave
(`prev2` < `prev1` < `v1` < `v3`); the history before 2026-07-09 renames the
same files back and forth too often to recover a better one.

**Releasing a version:** when `sushi-config.yaml` moves to a new `version:`,
add `archimate/<that version>/` with its model. Until it exists the workflows
warn and publish no current model at `/archimate`.

## Published

Every site build (the root on `main`, and each branch's preview) runs
cat-harness's `archimate` subgraph over the models `cat-archimate.config.json`
names — skill `archimate-models`, Tools `archimate-check` and
`archimate-pages`. The pages sit under the harness, at `/en/dpi-h-ra/archimate/`,
because `dpi-h-ra.json` declares the `archimate` visualiser there; the data
they draw from stays at `/archimate/`:

- `/en/dpi-h-ra/archimate/` — every model;
- `/en/dpi-h-ra/archimate/<version>/` — a model's views, and its elements by
  layer;
- `/en/dpi-h-ra/archimate/<version>/views/<id>/` — a view, drawn as SVG from
  the model, every box a link to its element;
- `/en/dpi-h-ra/archimate/<version>/elements/<id>/`, `…/relationships/<id>/` —
  one page per element and relationship, keyed by Archi's id;
- `/archimate/` — the data the pages are drawn from: a `.json` and `.jsonld`
  per version, and under `/archimate/<version>/` the model plus a `.json` and
  `.jsonld` per view, element and relationship (one JSON-LD IRI each), and an
  `.svg` per view;
- `/en/mapper/` — the RA mapper (`tools/ra-mapper/build-site.sh`, the site
  build's `site:mapper` step), current version first.

**No Java.** The Archi command-line report that `archimate.yml` used to run
(a JVM, a virtual display and a ~200 MB download per run) is gone (owner,
2026-10-09). Draw in Archi on your own machine; commit the `.archimate`; the
build does the rest. A branch's preview has the same paths under
`STAGING/<branch>/`, so its pages are at `STAGING/<branch>/en/dpi-h-ra/archimate/`.
