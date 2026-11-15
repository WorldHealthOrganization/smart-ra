# library/

**Ingested** source documents — a guideline this folio adapts, a standard it
cites, a paper it builds on. Machine-extracted structure, not authored content.

```
library/<doc-id>/
  structure.json        extracted document structure
  sections/<sid>.md     extracted section text
  candidates.json       extraction proposals
  manifest.jsonld       graph node for the document
```

**Nothing here is folio content.** Every node carries
`provenance: "ingested"` and is attributed to its source, so a query can
always separate *what that document claims* from *what this folio claims*.
Promoting something into `folio/` is a separate, deliberate act — see the
platform's `document-intake` skill.
