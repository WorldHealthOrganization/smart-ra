import { chapterRef, paper } from "../schema/builders";

/**
 * Reference Architecture and Guidance for Digital Public Infrastructure for the Health Sector
 *
 * Extracted from the frozen review version in the library
 * (`library/who-dpi-h-reference-architecture-draft-v1/`) by folio-assistant's docx-to-folio. From
 * here on this folio IS the document: edit the blocks, not the source.
 * Every block's `meta.source` keeps its page and line in the review PDF, so
 * public comments citing the review version still resolve after edits.
 */
export default paper({
  title: "Reference Architecture and Guidance for Digital Public Infrastructure for the Health Sector",
  meta: { subtitle: "A Digital Transformation Handbook for Digital Public Infrastructure for Health (DPI-H)" },
  authors: ["World Health Organization","International Telecommunication Union"],
  date: "2026-07-08",
  chapters: [
    chapterRef({ dir: "executive-summary" }),
    chapterRef({ dir: "how-to-use-this-guidance" }),
    chapterRef({ dir: "ch1-introduction" }),
    chapterRef({ dir: "ch2-dpi-h-reference-architecture-fra" }),
    chapterRef({ dir: "ch3-the-reference-architecture-for-d" }),
    chapterRef({ dir: "ch4-implementing-a-national-digital" }),
    chapterRef({ dir: "ch5-future-proofing-the-architecture" }),
    // Back matter: annexes, then the glossary (terms, then acronyms), then references.
    // The document opens on the executive summary, not on reference lists.
    chapterRef({ dir: "appendix" }),
    chapterRef({ dir: "glossary" }),
    chapterRef({ dir: "references" }),
  ],
});
