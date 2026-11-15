import { chapter, section } from "../../schema/builders";

export default chapter({
  title: "Glossary",
  label: "chap:glossary",
  sections: [
    section({
      title: "Glossary",
      label: "sec:glossary-lead",
      lead: true,
      blocks: ["t-glossary-lead-a31853"],
    }),
    // Acronyms are the glossary's short forms (SKOS notation), so they are a
    // subsection of the Glossary, not a chapter of their own.
    section({
      title: "Acronyms",
      label: "sec:acronyms-lead",
      blocks: ["t-acronyms-lead-bf4749"],
    }),
  ],
});
