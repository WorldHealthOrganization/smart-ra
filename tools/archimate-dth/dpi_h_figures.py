"""DPI-H RA figures drawn from the model: Fig. 3.1, Fig. 3.4.1 and Fig. A.1.

Source: WHO/ITU Reference Architecture and Guidance for DPI-H, review draft v1
(library/who-dpi-h-reference-architecture-draft-v1). Each view redraws one
figure of the draft, box for box. Where the figure and the text differ, the
text wins (owner rule, 2026-11-01).

- Fig. 2.2 "REDDHI" (PDF 40): only what the text defines (owner, Q-RAFIG-2
  A): REDDHI's components and the four full-STAC dimensions. The draft
  figure's other statements wait for the text (committee issue).
- Fig. 2.3 "DPI-H Architecture Design Principles" (PDF 48): the ten
  principles as Principle elements, named as the section 2.3 headings. The
  figure shows names only; what each means is the text's to say.
- Fig. 3.1 "Realisation relationships among architectural elements" (PDF 55):
  the four-step realisation chain, with the draft's worked example as names.
- Fig. 3.4.1 "Semantic Governance Infrastructure" (PDF 69): the governance,
  runtime, and content-and-application layers and the flow of content
  between them. Numbered IGs and apps are placeholders (illustrative=true).
- Fig. A.1 "Semantic governance capabilities, the roles that carry them out,
  and the supporting application components" (PDF 253): reuses the elements
  of the "Metadata Registry Governance" view. Their "<MD>" working prefixes
  and a "?????" marker are dropped (old names kept as formerName), and the
  supporting tools are linked as the Appendix F text describes.

Applied with: python3 -I tools/archimate-dth/add_views.py tools/archimate-dth/dpi_h_figures.py <in> <out>
"""

NAMESPACE = "https://github.com/litlfred/smart-ra#dpi-h-figures"
SOURCE = "WHO DPI-H Reference Architecture review draft v1"
VIEW_FOLDER = "1. Reference Architecture"

F22 = "DPI-H RA draft v1, Figure 2.2 'REDDHI' and section 2.2 (PDF 40)"
F23 = "DPI-H RA draft v1, Figure 2.3 'DPI-H Architecture Design Principles' and section 2.3 (PDF 48)"
F31 = "DPI-H RA draft v1, Figure 3.1 'Realisation relationships among architectural elements' (PDF 55)"
F341 = "DPI-H RA draft v1, Figure 3.4.1 'Semantic Governance Infrastructure' (PDF 69)"
FA1 = "DPI-H RA draft v1, Figure A.1 and Appendix F (PDF 253)"


def p(page, **kw):
    return {"raPage": f"PDF {page}", **kw}


ILL = {"illustrative": "true"}

PRINCIPLES = ["Governance", "Open Standards", "Interoperability", "Sustainability", "Modularity",
              "Local Capacity", "Equity and Inclusion", "Data Ownership, Access, and Control",
              "Trust and Security", "Ethics"]


def slug(s):
    return "".join(c if c.isalnum() else "-" for c in s.lower()).strip("-").replace("--", "-")


STAC = [("S", "Open Standards"), ("T", "Open Technologies"), ("A", "Open Architectures"), ("C", "Open Content")]
REDDHI = ["client-registry", "hfr", "hwr", "product-registry", "lhr"]

ELEMENTS = {
    # Fig. 2.2 (Q-RAFIG-2 A): only what the text defines. REDDHI's components are
    # the ones the model already marks reddhi=true; the four full-STAC
    # dimensions are the section 2.2.2 list. "Open Standards" is the same
    # element as the design principle of that name (Fig. 2.3).
    "reddhi-group": ("Grouping", "REDDHI: Resilient Essential Data and Digital Health Infrastructure", F22, p(40)),
    "stac-group": ("Grouping", "Full-STAC foundations", F22, p(40)),
    **{f"stac-{l.lower()}": ("Principle", n, f"{F22}; full-STAC dimension '{l}', defined in section 2.2.2.", p(40, stac=l))
       for l, n in STAC if l != "S"},
    # Fig. 2.3: the ten architecture design principles, named as the section 2.3 headings
    "adp-group": ("Grouping", "DPI-H architecture design principles", F23, p(48)),
    **{f"adp-{slug(n)}": ("Principle", n, f"{F23}; principle {i} of 10, defined in the text of section 2.3.", p(48, order=str(i)))
       for i, n in enumerate(PRINCIPLES, 1)},
    # Fig. 3.1: each lower element realises the one above.
    "f31-capability": ("Capability", "Identity maintained across services", F31, p(55, figureNote="Business Capability")),
    "f31-service": ("ApplicationService", "Resolving and matching identity", F31, p(55, figureNote="Application Service")),
    "f31-function": ("ApplicationFunction", "Identity matching", F31, p(55, figureNote="Application Function")),
    # Fig. 3.4.1
    "sgi-governance": ("Grouping", "Governance services", F341, p(69)),
    "sgi-runtime": ("Grouping", "Runtime services", F341, p(69)),
    "sgi-content": ("Grouping", "Content and application layers", F341, p(69)),
    "sgi-igs": ("Grouping", "IGs", F341, p(69)),
    "sgi-apps": ("Grouping", "Applications / use cases", F341, p(69)),
    "sgi-profile-authoring": ("ApplicationComponent", "Profile authoring", F341, p(69)),
    "sgi-conformance-resources": ("ApplicationComponent", "Conformance resources", F341, p(69)),
    "sgi-governance-tms": ("ApplicationComponent", "Governance TMS", F341,
                           p(69, candidateMatch="Terminology Service (id-3f41de2b51c24041b08243bf72b140d1)")),
    "sgi-runtime-ts": ("ApplicationComponent", "Runtime TS", F341,
                       p(69, candidateMatch="Terminology Service (id-3f41de2b51c24041b08243bf72b140d1)")),
    "sgi-runtime-other": ("ApplicationComponent", "Other runtime services", F341, p(69, figureNote="...", **ILL)),
    "sgi-global-content": ("ApplicationComponent", "Global content sources", F341, p(69)),
    "sgi-ig-1": ("Artifact", "IG 1", F341, p(69, **ILL)),
    "sgi-ig-2": ("Artifact", "IG 2", F341, p(69, **ILL)),
    "sgi-ig-3": ("Artifact", "IG 3", F341, p(69, **ILL)),
    "sgi-app-1": ("ApplicationComponent", "App 1", F341, p(69, **ILL)),
    "sgi-app-2": ("ApplicationComponent", "App 2", F341, p(69, **ILL)),
    "sgi-app-3": ("ApplicationComponent", "App 3", F341, p(69, **ILL)),
}

EXISTING = {
    "hfr": "id-4e0767822dcf46409554156a133fbc67",
    "hwr": "id-350840520ae44f658b6ad3b3762e382e",
    "product-registry": "id-59c26d672a4248e0bb83cf4d26cba10c",
    "lhr": "id-0e6d89398fff4f20994a31b4de58e7d7",
    "client-registry": "id-bc813024f32358c98e5512e43cf2c9bc",
    "limr": "id-c0d39bf67fe64f54b07fbeb9bf37d404",
    # Fig. A.1 (view "Metadata Registry Governance")
    "md-consume": "id-2dafda6622b54d80aa8975688a60be96",
    "md-change-requests": "id-7195059397624e21ba02cfb8305aa771",
    "md-change-management": "id-6c3eff21600c4a94b85d1105a58c43c6",
    "md-publication": "id-c4b3ee6bc379479f8efeb0ac34f24d6c",
    "md-monitoring": "id-671fc5bddfb44440a7187643db24fb57",
    "md-stakeholder": "id-8b18cf7ed0534fc8b9bf4ba4868a8975",
    "md-author": "id-d60c1f59f4d64f5aa7d9c3089a399e35",
    "md-owner": "id-99b92fe529e94fcd8ceac04cb16aefd7",
    "md-content": "id-3ba37ce39645467eb954c74e63e6231d",
    "md-upstream": "id-04141e93cb084711a861dfb1a680ef61",
    "md-rules": "id-8ceb8598df444a2288aa91c215ba2b56",
    "md-cr-tooling": "id-59eefeb14ee849b5922557ae4a47e7b6",
    "md-authoring": "id-c81a5272868141fcb61a9cf68ad8074d",
    "md-repository": "id-a738938b20d0405b9d4cee2b558a9d89",
}

RENAMES = {
    "md-consume": "Consume",
    "md-change-requests": "Change requests",
    "md-change-management": "Change management",
    "md-publication": "Publication / distribution",
    "md-monitoring": "Monitoring",
    "md-stakeholder": "Stakeholder",
    "md-content": "Content",
    "md-upstream": "Upstream content",
    "md-rules": "Management rules",
    "md-cr-tooling": "Change-request tooling",
    "md-authoring": "Authoring tool",
    "md-repository": "Repository",
}

EXISTING_RELATIONS = {
    ("Association", "md-stakeholder", "md-consume"): "id-365980e842c144e8aaf62cfc1d150451",
    ("Association", "md-consume", "md-change-requests"): "id-2e234297eee84facae1c81761a142286",
    ("Association", "md-change-requests", "md-change-management"): "id-4b976e2df482407e96c47dc26fe2723f",
    ("Association", "md-author", "md-change-management"): "id-7d48e2693c2e449e80ed136d2809a227",
    ("Association", "md-change-management", "md-owner"): "id-d5a793f4118142d99fd014f775f58d2c",
    ("Flow", "md-change-management", "md-publication"): "id-5a44401920e54dc6897c70a5a554ff54",
    ("Association", "md-publication", "md-content"): "id-a237fe62ece44de1a1abf272d21b556e",
    ("Association", "md-content", "md-owner"): "id-f12db89702a54c699a0fd4ea4ad921c9",
    ("Association", "md-monitoring", "md-publication"): "id-93446998f72644bcbc2d312e77cc3d59",
    ("Association", "md-rules", "md-monitoring"): "id-bfc87838a80d4adb8476faac9899847a",
    ("Serving", "md-authoring", "md-author"): "id-42a891f6319b4b14a7a7ba21b20a92fc",
}

STAC_KEYS = ["adp-open-standards"] + [f"stac-{l.lower()}" for l, _ in STAC if l != "S"]

RELATIONS = [
    # Fig. 2.2
    *[("Aggregation", "reddhi-group", k) for k in REDDHI],
    *[("Aggregation", "stac-group", k) for k in STAC_KEYS],
    # Fig. 2.3
    *[("Aggregation", "adp-group", f"adp-{slug(n)}") for n in PRINCIPLES],
    # Fig. 3.1
    ("Realization", "f31-service", "f31-capability"),
    ("Realization", "f31-function", "f31-service"),
    ("Realization", "client-registry", "f31-function"),
    # Fig. 3.4.1: layer membership, and the flow of content between layers
    *[("Aggregation", "sgi-governance", k) for k in ("limr", "sgi-profile-authoring", "sgi-conformance-resources", "sgi-governance-tms")],
    *[("Aggregation", "sgi-runtime", k) for k in ("sgi-runtime-other", "sgi-runtime-ts")],
    ("Aggregation", "sgi-content", "sgi-igs"),
    ("Aggregation", "sgi-content", "sgi-apps"),
    *[("Aggregation", "sgi-igs", f"sgi-ig-{i}") for i in (1, 2, 3)],
    *[("Aggregation", "sgi-apps", f"sgi-app-{i}") for i in (1, 2, 3)],
    ("Flow", "sgi-global-content", "sgi-governance-tms", {"name": "Content syndication"}),
    ("Flow", "sgi-governance-tms", "sgi-runtime-ts"),
    ("Flow", "sgi-runtime-ts", "sgi-governance-tms"),
    # Fig. A.1: Appendix F, "supported by tools (change-request tooling,
    # authoring and repository services), with upstream content ... feeding the process"
    ("Association", "md-cr-tooling", "md-change-requests"),
    ("Serving", "md-authoring", "md-change-management"),
    ("Serving", "md-repository", "md-publication"),
    ("Association", "md-upstream", "md-publication"),
]

V22 = "REDDHI and its full-STAC foundations (Fig. 2.2)"
V23 = "DPI-H architecture design principles (Fig. 2.3)"
V31 = "Realisation relationships among architectural elements (Fig. 3.1)"
V341 = "Semantic Governance Infrastructure (Fig. 3.4.1)"
VA1 = "Semantic governance capabilities, roles and tools (Fig. A.1)"

VIEWS = [
    (V22, F22, ("col", [("group", "reddhi-group", 5, [("box", k) for k in REDDHI]),
                        ("group", "stac-group", 4, [("box", k) for k in STAC_KEYS])])),
    (V23, F23, ("group", "adp-group", 5, [("box", f"adp-{slug(n)}") for n in PRINCIPLES])),
    (V31, "Each lower element realises the one above. " + F31,
     ("col", [("box", "f31-capability"), ("box", "f31-service"), ("box", "f31-function"), ("box", "client-registry")])),
    (V341, F341,
     ("row", [
         ("col", [
             ("group", "sgi-governance", 4, [("box", "limr"), ("box", "sgi-profile-authoring"),
                                             ("box", "sgi-conformance-resources"), ("box", "sgi-governance-tms")]),
             ("row", [("gap",), ("gap",), ("group", "sgi-runtime", 2, [("box", "sgi-runtime-other"), ("box", "sgi-runtime-ts")])]),
             ("group", "sgi-content", 1, [
                 ("group", "sgi-igs", 3, [("box", f"sgi-ig-{i}") for i in (1, 2, 3)]),
                 ("group", "sgi-apps", 3, [("box", f"sgi-app-{i}") for i in (1, 2, 3)]),
             ]),
         ]),
         # a column's space, so "Content syndication" sits clear of both boxes
         ("gap",),
         ("box", "sgi-global-content"),
     ])),
    (VA1, FA1,
     ("row", [
         ("col", [("box", "md-stakeholder"), ("box", "md-consume")]),
         ("col", [("gap",), ("box", "md-change-requests"), ("box", "md-cr-tooling")]),
         ("col", [("row", [("box", "md-author"), ("box", "md-owner")]),
                  ("row", [("gap",), ("box", "md-change-management")]),
                  # under Author, so its line to Author stays clear of Change management
                  ("row", [("box", "md-authoring"), ("gap",)])]),
         ("col", [("row", [("box", "md-content"), ("box", "md-upstream")]),
                  ("box", "md-publication"), ("box", "md-repository")]),
         ("col", [("box", "md-rules"), ("box", "md-monitoring")]),
     ])),
]

VIEW_CONNECTIONS = {
    V31: [("Realization", "f31-service", "f31-capability"),
          ("Realization", "f31-function", "f31-service"),
          ("Realization", "client-registry", "f31-function")],
    V341: [("Flow", "sgi-global-content", "sgi-governance-tms"),
           ("Flow", "sgi-governance-tms", "sgi-runtime-ts"),
           ("Flow", "sgi-runtime-ts", "sgi-governance-tms")],
    VA1: [*EXISTING_RELATIONS.keys(),
          ("Association", "md-cr-tooling", "md-change-requests"),
          ("Serving", "md-authoring", "md-change-management"),
          ("Serving", "md-repository", "md-publication"),
          ("Association", "md-upstream", "md-publication")],
}
