"""Product catalogue DTH (litlfred/dth-pc): elements and views for smart-ra.

Source: WHO, Digital transformation handbook for health product catalogue,
2025 (ISBN 9789240116191), L1 entry who-iris/library/9789240116191-eng.
Workplan: litlfred/dth-pc#2, section 2a and PC-3.

Only what the handbook states is modelled. Element names are the KG concepts
of dth-pc's glossary (glossary/dth-pc.glossary.json), Capitalized. Where a new
element may be the same thing as an element 0.2.0 already has, it carries
`candidateMatch` naming it, for the owner to decide. Medical devices are out
of the handbook's scope (owner, 2026-10-31, Q4); the views say so.

Supply chain partners, warehouse and regulator roles and the supply chain
capabilities are dth-sc's or 0.2.0's, reused by id, never redefined.

Applied with: python3 -I tools/archimate-dth/add_views.py tools/archimate-dth/dth_pc.py <in> <out>
"""

NAMESPACE = "https://github.com/litlfred/dth-pc#archimate"
SOURCE = "WHO Digital transformation handbook for health product catalogue (9789240116191); litlfred/dth-pc"
VIEW_FOLDER = "Supply Chain"

SKOS = "https://github.com/litlfred/dth-pc/blob/main/glossary/dth-pc.glossary.json#"
SCOPE = "Medical devices are out of the handbook's scope."


def p(page, term=None, **kw):
    d = {"dthPage": f"PDF {page}", **kw}
    if term:
        d["skosConcept"] = SKOS + term
    return d


ELEMENTS = {
    # Information model, Figs. 8-9 (PDF 28-29)
    "classification": ("BusinessObject", "Product Classification",
                       "Classifications such as ATC/DDD and ICD categorize diseases, pathogens, or health products. (PDF 28)",
                       p(28, "product-classification")),
    "generic-product": ("BusinessObject", "Generic Product",
                        "The general identifying details of a health product, excluding any manufacturer-specific information. (PDF 8)",
                        p(29, "generic-product")),
    "trade-item": ("BusinessObject", "Trade Item",
                   "Manufacturer-specific branded health products. (PDF 28) Narrower than the GS1 trade item (broadMatch, litlfred/smart-ra#142).",
                   p(28, "trade-item", broadMatch="https://www.gs1.org/standards/id-keys/gtin")),
    "regulated-trade-item": ("BusinessObject", "Regulated Trade Item",
                             "An authorization of a Trade Item within a given jurisdiction under a Product Authorization. (PDF 28)",
                             p(28, "regulated-trade-item")),
    "pmd": ("BusinessObject", "Product Master Data",
            "Central to all operational processes across supply chain partners; links all supply chain data from manufacturing to dispensing. (Fig. 2, PDF 11)",
            p(11, "product-master-data",
              candidateMatch="Health Product Data? (DataObject, id-783de50de1ae4db7b52cdfd21002d938)")),
    # the tool, Ch 3 (PDF 35)
    "npc": ("ApplicationComponent", "National Product Catalogue",
            "A technology tool that supports the ongoing management of product master data; a widely used term for such a tool is the NPC. (PDF 35) " + SCOPE,
            p(35, "national-product-catalogue",
              candidateMatch="Product Catalog Management System (id-bb1fc1b7425444ed8a0c420bec960edd); Product Registry (id-59c26d672a4248e0bb83cf4d26cba10c)")),
    # data management roles, PDF 26, 32, 43
    "data-owner": ("BusinessRole", "Data Owner",
                   "Responsible for the overall strategy, governance, and quality of the product master data; approves changes to the product master data. (PDF 26)",
                   p(26, "data-owner")),
    "data-custodian": ("BusinessRole", "Data Custodian",
                       "Responsible for the technical management and security of product master data. (PDF 26)",
                       p(26, "data-custodian")),
    "data-steward": ("BusinessRole", "Data Steward",
                     "Responsible for the day-to-day management, maintenance, and quality control of the product master data. (PDF 26)",
                     p(26, "data-steward")),
    "mdgg": ("BusinessCollaboration", "Master Data Governance Group",
             "Composed of all relevant stakeholders to provide leadership and guidance in managing product master data additions and changes. (PDF 32)",
             p(32, "master-data-governance-group")),
    "catalogue-manager": ("BusinessRole", "Catalogue Manager",
                          "An operational role needed to support the NPC. (PDF 43)",
                          p(43, "catalogue-manager")),
    # Fig. 2 partners not yet in the model
    "donor": ("BusinessRole", "Donor", "Fig. 2 (PDF 11)", p(11)),
    "shipper": ("BusinessRole", "Shipper", "Fig. 2 (PDF 11)",
                p(11, candidateMatch="Logistics Provider (dth-sc)")),
    "g-partners": ("Grouping", "Supply Chain Partners", "Fig. 2 (PDF 11)", p(11)),
    "g-processes": ("Grouping", "Supply Chain Processes", "Fig. 2 (PDF 11)", p(11)),
    "g-roles": ("Grouping", "Product Master Data Management Roles", "Illustrative data management roles (PDF 26), Master Data Governance Group (PDF 32), Catalogue Manager (PDF 43)", p(26)),
}

EXISTING = {
    "product-registry": "id-59c26d672a4248e0bb83cf4d26cba10c",
    "pcms": "id-bb1fc1b7425444ed8a0c420bec960edd",          # Product Catalog Management System
    "cap-pmdm": "id-366955c9809942bc8a57d0a77c11d202",      # Product Master Data Management
    "manufacturer": "id-66d0f91175c154b48413d57e9f952a34",  # Manufacturer / Distributor (dth-sc)
    "procurer": "id-2bfebc1bb917583cbc21e7d1bfac3164",      # Procurer (dth-sc)
    "nra": "id-8e67c8e9e1195cdc857b03a2c640e7fe",           # National Regulatory Authority (dth-sc)
    "moh": "id-1c5c0bc9234e4282b654dbc71b9da706",           # Ministry of Health
    "warehouse": "id-fc49aa813f2f40a18f01c014a2312e41",
    "health-facility": "id-9cecae7a982548e1960a36ed41713a7c",
    "patients": "id-a2320dbc07e6450b94f3f0f3e03bb877",
    "cap-forecasting": "id-e53b31972646454384c78f3380f5c40e",
    "cap-procurement": "id-9825f8c281d74fa5a9ec0171e246fb27",
    "cap-order": "id-f9c2f2cd09fd4799ac06f33ed88bb61c",
    "cap-warehouse": "id-2d603034c4194b058762690fd6415ff0",
    "cap-transportation": "id-b37bf4947ec9430197f9056d283eb5b0",
    "cap-dispensing": "id-f9f30d3e83e24a8daa3393eebb0838eb",
    "cap-recall": "id-a9c92f8fa2924d4180e8f5512b0d0097",
}

# Fig. 9 / PDF 29: the attributes that link the four objects, with their cardinality.
MODEL = [
    ("Association", "generic-product", "classification", {"name": "classification 0..*"}),
    ("Association", "trade-item", "generic-product", {"name": "associatedGenericProduct 0..*"}),
    ("Association", "trade-item", "trade-item", {"name": "contains 0..* (packaging hierarchy)"}),
    ("Association", "regulated-trade-item", "trade-item", {"name": "authorisedTradeItem 1..1"}),
]
for o in ("classification", "generic-product", "trade-item", "regulated-trade-item"):
    MODEL.append(("Composition", "pmd", o))

NPC = [
    ("Access", "npc", "pmd", {"accessType": 3}),          # "oversee product master data" (PDF 35)
    ("Realization", "npc", "cap-pmdm"),                   # "supports the ongoing management of product master data" (PDF 35)
    ("Association", "manufacturer", "pmd", {"name": "source of truth"}),  # PDF 21
]

ROLES = [
    ("Association", "data-owner", "pmd", {"name": "approves changes"}),            # PDF 26
    ("Association", "data-custodian", "pmd", {"name": "technical management and security"}),
    ("Association", "data-steward", "pmd", {"name": "day-to-day management and quality control"}),
    ("Association", "mdgg", "pmd", {"name": "leadership on additions and changes"}),  # PDF 32
    ("Association", "catalogue-manager", "npc", {"name": "supports"}),           # PDF 43
]

PARTNERS = ["manufacturer", "procurer", "moh", "donor", "shipper", "nra", "warehouse", "health-facility", "patients"]
PROCESSES = ["cap-forecasting", "cap-procurement", "cap-order", "cap-warehouse", "cap-transportation",
             "cap-dispensing", "cap-recall"]
MEMBERS = {"g-partners": PARTNERS, "g-processes": PROCESSES,
           "g-roles": ["data-owner", "data-custodian", "data-steward", "mdgg", "catalogue-manager"]}

RELATIONS = [("Aggregation", g, m) for g, ms in MEMBERS.items() for m in ms]
RELATIONS += MODEL + NPC + ROLES


def g(key, cols, kids):
    return ("group", key, cols, kids)


def b(key):
    return ("box", key)


def boxes(*keys):
    return [b(k) for k in keys]


V_MODEL = "Product Master Data Information Model (DTH PC Figs. 8-9)"
V_NPC = "National Product Catalogue (DTH PC Fig. 2, Ch. 2-3)"

VIEWS = [
    (V_MODEL,
     "Product Classification, Generic Product, Trade Item and Regulated Trade Item, linked by the attributes and cardinalities printed on PDF 29 (Figs. 8-9). " + SCOPE,
     ("row", [("col", boxes("pmd")),
              ("col", boxes("classification", "generic-product", "trade-item", "regulated-trade-item"))])),
    (V_NPC,
     "Product Master Data between supply chain partners and supply chain processes (Fig. 2, PDF 11), managed in the National Product Catalogue (PDF 35) by the data management roles (PDF 26, 32, 43). The handbook does not assign processes to partners, so no line is drawn between them. Fig. 2's ordering and inventory processes map to the 0.2.0 capabilities by name only; Finance / Insurance is not drawn. " + SCOPE,
     ("row", [
         g("g-partners", 1, boxes(*PARTNERS)),
         ("col", [b("pmd"), b("npc"), b("cap-pmdm")]),
         g("g-roles", 1, boxes("data-owner", "data-custodian", "data-steward", "mdgg", "catalogue-manager")),
         g("g-processes", 1, boxes(*PROCESSES)),
     ])),
]

# The contains self-association is in the model but not drawn: a loop on one box reads poorly.
VIEW_CONNECTIONS = {V_MODEL: [r for r in MODEL if r[1] != r[2]], V_NPC: NPC + ROLES}
