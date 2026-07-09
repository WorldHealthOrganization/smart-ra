# SMART RA Mapper — build

Single-file web app for EIRA-style (ABB/SBB) conformance mapping against the WHO reference architecture.

## Rebuild when a new RA version is published

    cd tools/ra-mapper
    python build_ra_mapper.py \
        ../../archimate/draft/WHOBaseFile.archimate \
        ../../archimate/current/WHOBaseFile_prev.archimate \
        -l "WHO RA (draft)" "WHO RA (previous)" \
        -o ../SMART-RA-Mapper.html

Pass any number of models (Archi `.archimate`, exchange XML, or zipped Archi archive);
the first one is the default version. All are embedded and selectable from the
version dropdown in the app header. Users can also load any RA file at runtime
("Load RA file…"), and import their country architecture via
My Architecture → "Import my architecture from ArchiMate…".

Mappings are keyed by element ID, so they survive switching between RA versions
that share IDs.

## Deployment

The app is one self-contained HTML file — host anywhere static
(GitHub Pages via `.github/workflows/ra-mapper.yml`, share by email, USB, etc.).
User work autosaves in the browser; the exported ArchiMate exchange XML is the
durable, shareable artifact.
