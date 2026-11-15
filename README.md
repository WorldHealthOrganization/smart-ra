<!--badges-->
[![License: CC BY-IGO 3.0](https://licensebuttons.net/l/by-nc/3.0/igo/80x15.png)](https://creativecommons.org/licenses/by/3.0/igo)
![CI Build](https://img.shields.io/github/actions/workflow/status/WorldHealthOrganization/smart-ra/ghbuild.yml)  
   
![QA errors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2FWorldHealthOrganization.github.io%2Fsmart-ra%2Fqa.json&query=%24.errs&logoColor=red&label=QA%20errors&color=yellow)
![QA warnings](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2FWorldHealthOrganization.github.io%2Fsmart-ra%2Fqa.json&query=%24.warnings&logoColor=orange&label=QA%20warnings&color=yellow)
![QA hints](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2FWorldHealthOrganization.github.io%2Fsmart-ra%2Fqa.json&query=%24.hints&logoColor=yellow&label=QA%20hints&color=yellow)
<!--/badges-->

# WHO SMART GUIDELINES - Reference Architecture

## DPI-H Reference Architecture guidance: public review

The *Reference Architecture and Guidance for Digital Public Infrastructure for
the Health Sector* (draft v1.0, for public comment) is held here as an
editable document, with every public comment placed on the paragraph it is
about.

- **Read the document, with its comments:** https://litlfred.github.io/smart-ra/en/dpi-h-ra/
- **Open comments dashboard:** https://litlfred.github.io/smart-ra/en/folio-assistant-core/public-comments/folio/dpi-h-ra/
- **ArchiMate models** — every view drawn, every element and relationship with
  its own page: https://litlfred.github.io/smart-ra/en/dpi-h-ra/archimate/ (the RA mapper:
  https://litlfred.github.io/smart-ra/en/mapper/). How they are versioned and
  built: [`archimate/README.md`](archimate/README.md).
- **The review version as circulated** (line-numbered PDF and .docx):
  [`library/who-dpi-h-reference-architecture-draft-v1/`](library/who-dpi-h-reference-architecture-draft-v1/)

**Review committee and editor:** answer a comment in a conversation comment on
any pull request in this repository:

```
pc: PC-0042
recommend: accepted-modified

Why, in as many lines as needed.
```

Use `decide:` instead of `recommend:` for the editor's decision. The codes are
`accepted`, `accepted-modified`, `not-accepted`, `noted` and `deferred`. Every
code except `accepted` needs a reason. A recommendation is recorded from any
collaborator on this repository, and a decision only from its owner. To change
who counts, add `committee` or `editors` login lists to
[`review/public-comment/config.json`](review/public-comment/config.json).

**Changes** are made on feature branches. Each one may answer several comments,
and each pull request gets a staging preview at
`https://litlfred.github.io/smart-ra/STAGING/<branch>/`. The dashboard links
each comment's paragraph before (main) and after (the branch).

CI-Build: https://worldhealthorganization.github.io/smart-ra/

Please see these [instructions](https://smart.who.int/ig-starter-kit/ig_setup.html#github-setup)


## Changes and feedback

Feedback and issues about this empty framework can be submitted via the [issues](https://github.com/WorldHealthOrganization/smart-ra/issues) page, and will be incorporated into subsequent releases.


The Core Architects WG is currently responsible for the changes.
