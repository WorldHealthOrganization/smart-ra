"""DPI-H RA Figs. 3.3, 3.4 and 3.5 (Q&CC sub-goal), moved into the current model.

Owner, 2026-11-01, card Q-RAC-5 A: the three layered views were drawn in the
separate model 0.2.0-draft.3. They are copied, box for box, into
0.3.0-draft.1. Elements the current model already holds are reused, and
names follow the document's figures (PDF 56-58).

- Reused: Health Record Management (Capability), Lifelong Health Record (the
  figures' label for 0.2.0-draft.3's "Shared Health Record"), Terminology
  Service and Facility Registry (ApplicationComponents).
- Renamed to the document's label: the "Product Catalogue" data object is
  "Product Registry" in Figs. 3.3 and 3.5.
- The draft drew each view with its own copies of shared elements. Those
  merge into one element per type and name.

Not reused, for the review committee (smart-ra#212): the current model's
"Client Registry for Health", "Product Registry" (an ApplicationComponent, where
these figures draw a data object) and "National Trust Services" are near
matches with different names, and the figures' names are kept.

Applied with: python3 -I tools/archimate-dth/copy_views.py tools/archimate-dth/dpi_h_layered.py \
    archimate/0.2.0-draft.3/WHOBaseFile.archimate <in> <out>
"""

NAMESPACE = "https://github.com/litlfred/smart-ra#dpi-h-layered"
SOURCE = "WHO DPI-H Reference Architecture review draft v1, Figs. 3.3-3.5 (PDF 56-58), from model 0.2.0-draft.3"
VIEW_FOLDER = "1. Reference Architecture"

VIEWS = {
    "id-793b6a7849184ec8a26e8d9e96c8276a": "TPHR Sub-goal #1 Layered View (Fig. 3.3)",
    "id-7da6c80d57a84f39a22fba722473e84b": "TPHR High Level Layered View (Fig. 3.4)",
    "id-5c86a1b619f64fdab1bc08d0e01fa60b": "Q&CC Sub-goal #1 Layered View (Fig. 3.5)",
}

REUSE = {
    ("Capability", "Health Record Management"): "id-4a08b39b55a6469098a89697af71daae",
    ("ApplicationComponent", "Shared Health Record"): "id-0e6d89398fff4f20994a31b4de58e7d7",
    ("ApplicationComponent", "Terminology Service"): "id-3f41de2b51c24041b08243bf72b140d1",
    ("ApplicationComponent", "Facility Registry"): "id-5f6d9b9678824b37b95952735420ae8d",
}

NAMES = {
    ("DataObject", "Product Catalogue"): "Product Registry",
}
