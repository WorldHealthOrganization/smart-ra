# AGENTS.md — Reference Architecture and Guidance for Digital Public Infrastructure for the Health Sector

This is a **folio**: the content repository. The authoring platform —
skills, schemas, MCP tools, the publication pipeline — is
[folio-assistant](https://github.com/litlfred/folio-assistant.git): its layers are remote-mounted at the repository root (see **Commands**).

This file is the **agent-generic** source of truth, read natively by Claude
Code, Gemini CLI, Antigravity, Cursor and Copilot. `CLAUDE.md` and
`GEMINI.md` are thin stubs pointing here.

> **Content lives here; formalism lives in the platform.** If you are about to
> add a schema, a validator, a QA criterion or a skill, it belongs in
> folio-assistant, not in this repo. If you are about to add a chapter, a
> recommendation or a table, it belongs here.

## Content type: `document`

A **document** folio: structured prose — policy guidance, a standard, a
report, a handbook. No Lean formalization, and no TeX installation required to
publish.

**Block kinds you may use:** `prose`, `example`, `remark`, `algorithm`,
`simulator`, `equation`, `diagram`, `table`.

**Kinds you may NOT use:** `definition`, `theorem`, `lemma`,
`proposition`, `corollary`, `conjecture`, `proof`. Those are the paper
profile — their assertion is a formal mathematical claim backed by a `.lean`
sibling, and this folio has no toolchain to check one. `content_validate`
enforces this on every run.

Reaching for `theorem` to carry a recommendation is the common mistake. Load
the `normative-statements` skill instead.

## Layout

```
folio/dpi-h-ra/          the document
  dpi-h-ra.ts             its manifest — chapters, in reading order
  <chapter>/<chapter>.ts   a chapter manifest — sections, in reading order
  <chapter>/<root>.ts      a block manifest
  <chapter>/<root>.md      that block's prose
folio/schema/            re-export shim for the platform's builders
test/results/block-qa/     QA verdicts, one per block, mirroring folio/ (machine-written working copy — published to qa-reports)
test/attestations/         reviewer judgements and baseline attestations (committed on main)
library/                   ingested source documents (read-only reference)
uploads/                   source PDFs, for offline citation verification
smart-base/ … bootstrap-tools/   the platform's layers, remote-mounted (gitignored)
beans/                    the work plan
```

## Commands

The platform's layers are remote-mounted at the repository root (`index.config.json`, locked in `index.lock.json`): `smart-base/`, `fhir-harness/`, `folio-assistant-core/`, `cat-harness/`, `cat-harness-tools/`, `bootstrap/`, `bootstrap-tools/`. `folio-assistant-sci/` is no longer mounted: core declares its own `document` adapter since bean bzwk (2026-10-12), so a document folio needs nothing from sci. Every workflow mounts them through `.github/actions/mount-layers`, and a session through `.claude/hooks/session-start.sh` when they are absent; `.mcp.json` runs the MCP server from the `cat-harness-tools/` mount. There is no `folio-assistant/` submodule any more (bean n3h9).

```sh
bun run cat-harness-tools/scripts/remote-mount.ts                 # lay the mounts down
bun run cat-harness-tools/src/index.ts --stdio --repo .           # the MCP server
bun run cat-harness-tools/pipeline/qa-sweep.ts folio      # QA every block
```

**The site** — the document, the public-comment dashboard, the library, the
node-kind pages, the ArchiMate models and the RA mapper (`en/mapper/`) — is built and published by an agent,
never by a workflow (owner, 2026-10-10; bean n3h9). The scripts it runs are
this repository's `package.json`:

```sh
bun run cat-harness-tools/scripts/stage-local.ts --repo . [--plan | --dry-run]
```

The steps are declared once, in `index.config.json` (the `dpi-h-ra` entry) under `site.build`:
`pre` (the gates: `check:archimate`, `check:kg-blocks`, `check:library-kg`), `sourceSteps` (run before Jekyll, into
the site source) and `siteSteps` (run after Jekyll, on the built site). The
command reads them from there. On `main` it publishes the root, keeping
`STAGING/` and `_render-log/`; on any other branch it publishes the preview at
`STAGING/<branch>/`. `--plan` prints what it would do, and `--dry-run` builds
without publishing. Either way it publishes only once every link resolves.
It is the same command for every agent-run repository, folio or IG (owner,
2026-10-10: "one consolidated workflow"). It hands this one to
`build-instance-site.ts --instance dpi-h-ra`, which can also be run directly;
any step flag given there replaces the declared recipe.

This folio is not an IG, so its site builds no FHIR artefact index and owes
no artefact pages for smart-base, the IG layer it mounts. smart-base's
`fhir-artifact-index/index.json` is built at publish by IG sites only
(fhir-harness#124), and the publish check owes an `artifact-index` page only
where that index is built (owner, 2026-10-30, #103).

## QA — every block is checked from the first commit

`qa-sweep` runs every criterion a script can check against each block, and
writes one verdict file per block under `test/results/block-qa/`. That is a
machine-written working copy: derived verdicts are published to the orphan
`qa-reports` branch (`qa-store.ts publish`, by the shared
`folio-qa-sweep` workflows), never committed to `main` (owner, 2026-10-30:
"qa-reports branch", the platform's model, as in dth-hrh). Judgements an agent
or reviewer records stay on `main` in `test/attestations/`. A verdict is keyed
on the block's content hash, so one older than its block reads as stale, never
as passing.

The staging preview is built and published by an agent (see **The site**
above); the review page's QA column reports that build. `.github/workflows/qa-sweep.yml`
runs the full sweep on every pull request (warn-only) and publishes it to
`qa-reports` under `pr/<n>/<sha>`, and `qa-sweep-nightly.yml` refreshes stale
verdicts under `main/<sha>`, by dispatch only. Both call cat-harness-tools'
reusable `folio-qa-sweep*` workflows. Criteria that need an
agent's judgement (voice, exposition, adversarial review) are not run by the
sweep; they stay unaudited until an agent records them.

## Work plan — use `beans`

`beans/` is committed, so the plan survives a fresh container and a sibling
session sees it. Claim before you work; never resolve a sibling's bean.

```sh
cat-harness-tools/scripts/install-beans.sh
beans list
beans create "<title>"
beans <id> --status in-progress
```

**Check before you create** — `beans create` is not idempotent and dedupes on
nothing, so re-entering a step duplicates the plan rather than no-op'ing.

## The skills are in the platform, not here

Ask for them by name and the agent loads them over MCP (`skill_fetch`):

| Package | What |
|---|---|
| `folio-core` | content-agnostic: bean coordination, editorial review, QA |
| `folio-document-adapter` | `document-authoring`, `document-structure`, `normative-statements`, `document-publishing` |

Do not copy a skill body into this repo. It will drift, and the platform's copy
is the one every other folio is reading.

## This folio: the DPI-H Reference Architecture, in public review

The document is the WHO/ITU *Reference Architecture and Guidance for Digital
Public Infrastructure for the Health Sector*. It is an **L1** document that will
replace the OpenHIE references in the DIIG, and it runs on the **smart-base**
harness (`needs` in `dpi-h-ra.json`). The FHIR IG under `input/` is
downstream of this document and is not part of the folio.

- **The review version is frozen.**
  `library/who-dpi-h-reference-architecture-draft-v1/` holds the line-numbered
  PDF and the .docx exactly as circulated for public comment. Every comment
  cites that version. Never edit it to answer a comment.
- **The folio is the document now.** `folio/dpi-h-ra/` was extracted from the
  review version once (`docx-structure.py` → `pdf-line-map.py` →
  `docx-to-folio.ts`). Edit the blocks there. Each block's `meta.source`, and
  `folio/dpi-h-ra/review-anchors.json`, keep its page and line in the review
  version, so comments still resolve after edits. Do not re-run the extraction
  over the folio.
- **Public comments** are adjudicated with the platform's `public-comment`
  skill and `folio-assistant-core/scripts/public-comment.ts`.
  The record is `review/public-comment/`, and the process is
  `public-comment.bpmn`:
  - triage and placement: review coordinator;
  - recommendation: review committee;
  - decision: editor;
  - the edit: an author, human or agentic, on a feature branch;
  - the change-set review: on the branch's staging preview.

  Move a comment only through the tool. Its status is what the dashboard
  counts.
- **Returned spreadsheets hold reviewers' emails.** Import them from
  `review/public-comment/raw/` (gitignored) or from outside the repository.
  Never commit them.

## Translations

Owner, 2026-11-18 (option A, widened to A + B + C): the five UN target locales
`ar`, `es`, `fr`, `ru`, `zh`, beside the English source. The platform's
process is `multi-locale-translation` (cat-harness `translation-manager`,
`translation-refresh`); this section is what that process asks the layer to
name.

- **Everything is UNOFFICIAL.** Agent drafts, no human sign-off. Never write
  `official: true`, `X-Folio-Official: yes` or a `translationStatus` of
  `official`; a person does that (`human-translation-workflow`).
- **Declared in** `index.config.json` (`translation`, on the `dpi-h-ra`
  entry) and `dpi-h-ra.json` (`dpi-h-ra-translations`, `translations/`,
  graph typology `translation-sources`). Declaring it is what makes the site
  build publish `assets/translation-status/review.json`, which a block's 🌐
  pane reads (`publish-translation-review.ts`, run by `build-instance-site.ts`).
- **Templates** are one `.pot` per document chapter, per target locale:
  `translations/<locale>/<chapter-dir>.pot`, plus `dpi-h-ra.pot` (the
  document's title). That is the chapter level of the platform's `.po`
  resolution (`po-resolve.ts`). They are written by the platform's extractor,
  the `translation_extract` MCP tool (`pot-extract.ts`): call it with the
  chapter directory and the target `locale`, once per locale. **The
  `glossary` chapter is the exception**: `translations/<locale>/glossary.po`
  is the platform's terminology-hints file for translation QA, so that
  chapter is extracted per block (`t-glossary-lead-a31853`,
  `t-acronyms-lead-bf4749`), with `translation_extract` on each block's `.md`.
- **The glossary** is translated in `glossary/*.glossary.json` itself, as
  language-tagged `prefLabel` and `definition` (`{"en": …, "fr": …}`), with
  `translationStatus` per locale `unofficial` (owner card Q1, 2026-11-18).
  The platform's glossary extractor (`glossary-pot.ts`) takes `authored`
  terms only, and every term here is a `candidate`. A term's `status` is not
  changed by translating it. `altLabel` is plain strings in `folio-glossary/v1`
  and cannot carry a language, so alternative labels stay English.
- **Merge policy: open only.** A translation PR is sent to the merge manager;
  no translation session merges.
- **Pages.** `/<locale>/` chapter pages need the document site builder to
  render a locale (folio-assistant-core `build-document-site.ts` renders
  `/en/` only today). Until it does, the catalogues are drafts for review on
  the 🌐 pane and the review page.

### UNTERM: official candidates drop in here

UNTERM (unterm.un.org) is not reachable from a cloud session; its lookup is
bean `folio-assistant-untm`, worked by the owner's local agent. **Never fake
or guess an UNTERM entry.** What it writes, through the platform's one
candidate writer (`addCandidates`, `scripts/lib/translation-candidates.ts`):

- into `translations/<locale>/<catalogue>.candidates.json`
  (`translation-candidates/v1`), one candidate per matched string:
  `source: {kind: "official", id: "unterm:<entry>"}`, and `sourceText`, the
  English exactly as UNTERM prints it;
- the platform auto-picks it as official only when `sourceText` equals the
  msgid exactly; any other match is a candidate for a person to adjudicate;
- for a glossary term, the catalogues are the glossary chapter's
  (`t-glossary-lead-a31853`, `t-acronyms-lead-bf4749`), whose msgids carry the
  term names; the language-tagged label in the glossary JSON is replaced by
  the UNTERM text only after that adjudication.

Likely UNTERM matches, to look up (unverified; a list of what to ask, not an
answer): the UN-system organisation names (United Nations, World Health
Organization, Pan American Health Organization, United Nations Children's
Fund, United Nations Industrial Development Organization, International
Telecommunication Union, International Organization for Standardization,
Global Fund to Fight AIDS, Tuberculosis and Malaria, Gavi, the Vaccine
Alliance), and the general terms Artificial Intelligence, Sustainable
Development Goal, Digital Public Infrastructure, Interoperability, Digital
Health, Digital Transformation, Health Information System, International
Health Regulations, International Classification of Diseases, Civil
Registration and Vital Statistics, Low-and-Middle-Income Country,
Non-Governmental Organization, Ministry of Health, Public Key Infrastructure,
Information and Communications Technology, Monitoring, Evaluation,
Governance, Stakeholder, Human Resources for Health, Antenatal Care, United
Nations Standard Products and Services Code. Product names (FHIR, SNOMED CT,
LOINC, DHIS2, OpenMRS, ArchiMate, TOGAF) are unlikely to have UNTERM entries.
