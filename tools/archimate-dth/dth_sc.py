"""Supply chain DTH (litlfred/dth-sc): elements and views for smart-ra.

Source: WHO, Digital transformation handbook for health supply chain
architecture, 2024 (ISBN 9789240101197), L1 entry
who-iris/library/9789240101197-eng. Workplan: litlfred/dth-sc#2, section 4.

Only what the handbook states is modelled. Groupings and their members are
Fig. 14's; the flows of the track-and-trace view are Fig. 24's. No
relationship is added that the handbook does not draw or say. Where a new
element may be the same thing as an element 0.2.0 already has, the new one
carries `candidateMatch` naming it, for the owner to decide (open point 3).

Applied with: python3 -I tools/archimate-dth/add_views.py tools/archimate-dth/dth_sc.py <in> <out>
"""

NAMESPACE = "https://github.com/litlfred/dth-sc#archimate"
SOURCE = "WHO Digital transformation handbook for health supply chain architecture (9789240101197); litlfred/dth-sc"
VIEW_FOLDER = "Supply Chain"


def p(page, **kw):
    return {"dthPage": f"PDF {page}", **kw}


FIG14 = "DHSC architecture framework, Fig. 14 (PDF 34-35)"

ELEMENTS = {
    # Fig. 14 groupings
    "g-enterprise": ("Grouping", "Digital Health Supply Chain Enterprise", FIG14, p(34)),
    "g-shared": ("Grouping", "Shared Services", FIG14, p(34)),
    "g-foundational": ("Grouping", "Foundational Components",
                       "Components that provide system capabilities for organizing and managing master data such as product, facility and supplier data. (PDF 35)", p(35)),
    "g-interop": ("Grouping", "Interoperability Layer",
                  "This component facilitates the exchange of data across various systems as well as across levels of the health system. (PDF 35)", p(35)),
    "g-hscis": ("Grouping", "Health Supply Chain Information Systems",
                "These systems support the various supply chain processes. One system or digital platform might support one or more supply chain processes. (PDF 35)", p(35)),
    "g-data": ("Grouping", "Data Services",
               "Components that support data aggregation and analysis, and traceability services that use the aggregated supply chain data to enable health product tracking, tracing and verification. (PDF 35)", p(35)),
    "g-analytics": ("Grouping", "Analytics", FIG14, p(34)),
    "g-traceability": ("Grouping", "Traceability", FIG14, p(34)),
    "g-external": ("Grouping", "External Systems",
                   "Systems outside the public health ecosystem that may integrate with it to exchange data, including manufacturers' systems, global platforms developed by funders or procurement agencies, and global or regional data repositories. (PDF 35)", p(35)),
    "g-ecosystems": ("Grouping", "Digital Ecosystems",
                     "Other digital ecosystems that benefit from health supply chain data. (PDF 35)", p(35)),
    # interoperability layer: enabling components (Fig. 14)
    "if-authentication": ("ApplicationFunction", "Authentication", FIG14, p(34)),
    "if-orchestration": ("ApplicationFunction", "Orchestration", FIG14, p(34)),
    "if-encryption": ("ApplicationFunction", "Encryption", FIG14, p(34)),
    "if-validation": ("ApplicationFunction", "Validation", FIG14, p(34)),
    "if-transformation": ("ApplicationFunction", "Transformation", FIG14, p(34)),
    "if-translation": ("ApplicationFunction", "Translation", FIG14, p(34)),
    # HSCIS not in 0.2.0
    "cold-chain-system": ("ApplicationComponent", "Cold Chain Management System", FIG14, p(34)),
    # data services
    "data-warehouse": ("ApplicationComponent", "Data Warehouse", FIG14,
                       p(34, candidateMatch="Analytics & Reporting Platform (id-3fd92d497ca040c8a436f355c0b68770)")),
    "supply-chain-reports": ("ApplicationService", "Supply Chain Reports", FIG14, p(34)),
    "product-verification": ("ApplicationService", "Product Verification", FIG14,
                             p(34, candidateMatch="Verification (id-32999d2977774d8e96b486173dbfd01d)")),
    "track-and-trace": ("ApplicationService", "Track and Trace", FIG14,
                        p(34, candidateMatch="Tracking (id-49566812cc844dc4b1c2a1c08aac20a5); Traceability Services (id-fdce32337758449aab42701096622582)")),
    # external systems
    "manufacturer-systems": ("ApplicationComponent", "Manufacturer Systems", FIG14, p(34)),
    "data-repositories": ("ApplicationComponent", "Data Repositories",
                          "Global or regional data repositories that aggregate master or transactional data (e.g., product master data and serialization data). (PDF 34-35)", p(35)),
    "global-platforms": ("ApplicationComponent", "Global Platforms",
                         "Global platforms developed by funders or procurement agencies. (PDF 35)", p(35)),
    # digital ecosystems
    "regulatory-systems": ("ApplicationComponent", "Regulatory Systems",
                           "Regulatory systems that combine supply chain data from the dispensing system with health information and individuals' data to conduct post-market surveillance and pharmacovigilance, or use supply chain data to perform product recalls. (PDF 35)",
                           p(35, sharedWith="dth-sfp defines the regulatory and pharmacovigilance elements")),
    "finance-insurance-systems": ("ApplicationComponent", "Finance and Insurance Systems",
                                  "Finance and insurance systems that combine data from the dispensing system with individuals' information to verify and process insurance claims. (PDF 35)", p(35)),
    "hmis": ("ApplicationComponent", "Health Management Information System", FIG14, p(34)),
    "quality-systems": ("ApplicationComponent", "Quality Systems",
                        "Laboratory or quality monitoring systems that integrate with HSCISs to trigger alerts on quality issues or trigger product quarantines or recalls. (PDF 35)", p(35)),
    # Fig. 24 traceability data
    "traceability-event": ("DataObject", "Traceability Event",
                           "Traceability data. What: product identifier, batch no., serial no. When: date and time of the event. Where: location of the event. Why: details of the transaction (e.g., receiving, shipping, dispensing, discarding). (Fig. 24, PDF 55)", p(55)),
    # supply chain partners, Figs. 1 and 3
    "g-partners": ("Grouping", "Public Health Supply Chain Partners", "Fig. 1 (PDF 11) and Fig. 3 (PDF 13)", p(11)),
    "g-processes": ("Grouping", "Health Supply Chain Processes", "Fig. 1 (PDF 11) and Fig. 2 (PDF 12)", p(11)),
    "procurer": ("BusinessRole", "Procurer", "Fig. 1 (PDF 11)", p(11)),
    "manufacturer": ("BusinessRole", "Manufacturer / Distributor", "Fig. 1 (PDF 11)", p(11)),
    "nra": ("BusinessRole", "National Regulatory Authority", "Regulators, Fig. 1 (PDF 11); regulatory authority, Annex 5 (PDF 70).",
            p(11, altLabel="Regulator; NMRA", sharedWith="dth-pc and dth-sfp reuse this element")),
    "central-warehouse": ("BusinessRole", "Central Warehouse", "Fig. 1 (PDF 11)", p(11)),
    "regional-warehouse": ("BusinessRole", "Regional Warehouse", "Fig. 1 (PDF 11)", p(11)),
    "district-warehouse": ("BusinessRole", "District Warehouse", "Fig. 24 (PDF 55)", p(55)),
    "logistics-provider": ("BusinessRole", "Logistics Provider", "Fig. 1 (PDF 11)", p(11)),
    "community-health": ("BusinessRole", "Community Health", "Fig. 1 (PDF 11)", p(11)),
    "individual": ("BusinessRole", "Individual", "Fig. 1 (PDF 11): the individuals at the centre of supply chain processes.",
                   p(11, candidateMatch="Patients (stakeholder, id-a2320dbc07e6450b94f3f0f3e03bb877)")),
    "private-sector": ("BusinessRole", "Private Sector", "Fig. 3 (PDF 13)", p(13)),
}

EXISTING = {
    "fsp": "id-4f7d1037d878435aa3a0fbdcee0c685b",          # Forecasting & Supply Planning System
    "pms": "id-58832f74225140c38ddc4ebaa5fef90c",          # Procurement Management System
    "oms": "id-f6022dce920d4f828581dd2f7e15280f",          # Order Management System
    "scms": "id-566242a824b24ede92c7b6593b827b94",         # Supplier & Contract Management System
    "wms": "id-35d0806bcb5c46fab5102d75de09558f",          # Warehouse Management System
    "tms": "id-ba1ec21bae4641378c56f714f72042d7",          # Transportation Management System
    "dispensing-system": "id-370b6bdcb29449c9be74644ffacc94aa",
    "hf-lmis": "id-67637a829ea744cb930ac67459bc9894",      # Health Facility Logistics Management System (inventory management, Figs. 18-19, 24)
    "product-registry": "id-59c26d672a4248e0bb83cf4d26cba10c",
    "supplier-registry": "id-199c0717881f4992970d6ba85780b74e",
    "facility-registry": "id-5f6d9b9678824b37b95952735420ae8d",
    "interop-component": "id-80856538cbd44167a37b276e38c994c3",
    "moh": "id-1c5c0bc9234e4282b654dbc71b9da706",          # Ministry of Health (stakeholder)
    "warehouse": "id-fc49aa813f2f40a18f01c014a2312e41",    # Warehouse (role)
    "health-facility": "id-9cecae7a982548e1960a36ed41713a7c",
    "cap-forecasting": "id-e53b31972646454384c78f3380f5c40e",
    "cap-supplier-contracts": "id-f3331a72444d4cc49391c25e0f7745fd",
    "cap-procurement": "id-9825f8c281d74fa5a9ec0171e246fb27",
    "cap-order": "id-f9c2f2cd09fd4799ac06f33ed88bb61c",
    "cap-warehouse": "id-2d603034c4194b058762690fd6415ff0",
    "cap-transportation": "id-b37bf4947ec9430197f9056d283eb5b0",
    "cap-dispensing": "id-f9f30d3e83e24a8daa3393eebb0838eb",
    "cap-traceability": "id-e88f6d077d31407bb1af5f2ecfd3b48a",
}

MEMBERS = {
    "g-enterprise": ["g-shared", "g-interop", "g-hscis", "g-data"],
    "g-shared": ["g-foundational"],
    "g-foundational": ["product-registry", "supplier-registry", "facility-registry"],
    "g-interop": ["interop-component", "if-authentication", "if-orchestration", "if-encryption",
                  "if-validation", "if-transformation", "if-translation"],
    "g-hscis": ["fsp", "pms", "oms", "scms", "wms", "tms", "cold-chain-system", "dispensing-system"],
    "g-data": ["g-analytics", "g-traceability"],
    "g-analytics": ["data-warehouse", "supply-chain-reports"],
    "g-traceability": ["product-verification", "track-and-trace"],
    "g-external": ["manufacturer-systems", "data-repositories", "global-platforms"],
    "g-ecosystems": ["regulatory-systems", "finance-insurance-systems", "hmis", "quality-systems"],
    "g-partners": ["moh", "procurer", "manufacturer", "nra", "central-warehouse", "regional-warehouse",
                   "logistics-provider", "health-facility", "community-health", "individual", "private-sector"],
    "g-processes": ["cap-forecasting", "cap-supplier-contracts", "cap-procurement", "cap-order",
                    "cap-warehouse", "cap-transportation", "cap-dispensing", "cap-traceability"],
}

RELATIONS = [("Aggregation", g, m) for g, ms in MEMBERS.items() for m in ms]
RELATIONS += [("Specialization", w, "warehouse") for w in ("central-warehouse", "regional-warehouse", "district-warehouse")]
# Fig. 24: HSCISs and external systems send data through the interoperability
# layer to the data repository; traceability services read the aggregated
# traceability data; individuals and regulators verify products.
TT_FLOWS = [("Flow", s, "interop-component") for s in ("wms", "tms", "hf-lmis", "dispensing-system",
                                                       "manufacturer-systems", "data-repositories", "global-platforms")]
TT_FLOWS += [("Flow", "interop-component", "data-warehouse")]
TT_OTHER = [
    ("Access", "data-warehouse", "traceability-event", {"accessType": 3}),
    ("Access", "track-and-trace", "traceability-event", {"accessType": 1}),
    ("Access", "product-verification", "traceability-event", {"accessType": 1}),
    ("Serving", "product-verification", "individual"),
    ("Serving", "product-verification", "nra"),
    ("Serving", "track-and-trace", "individual"),
]
RELATIONS += TT_FLOWS + TT_OTHER


def g(key, cols, kids):
    return ("group", key, cols, kids)


def b(key):
    return ("box", key)


def boxes(*keys):
    return [b(k) for k in keys]


V_FRAMEWORK = "DHSC Architecture Framework (DTH SC Fig. 14)"
V_TT = "Track and Trace through DHSC Components (DTH SC Fig. 24)"
V_PARTNERS = "Health Supply Chain Partners and Processes (DTH SC Figs. 1-3)"

VIEWS = [
    (V_FRAMEWORK,
     "The DHSC architecture framework of the supply chain DTH (Fig. 14, PDF 34), based on TOGAF and OpenHIE. Groupings and members as drawn; no relationships beyond membership are asserted.",
     ("row", [
         g("g-enterprise", 1, [
             g("g-interop", 7, boxes("interop-component", "if-authentication", "if-orchestration", "if-encryption",
                                     "if-validation", "if-transformation", "if-translation")),
             g("g-hscis", 4, boxes("fsp", "pms", "oms", "scms", "wms", "tms", "cold-chain-system", "dispensing-system")),
             ("row", [
                 g("g-shared", 1, [g("g-foundational", 1, boxes("product-registry", "supplier-registry", "facility-registry"))]),
                 g("g-data", 2, [g("g-analytics", 1, boxes("data-warehouse", "supply-chain-reports")),
                                 g("g-traceability", 1, boxes("product-verification", "track-and-trace"))]),
             ]),
         ]),
         g("g-external", 1, boxes("manufacturer-systems", "data-repositories", "global-platforms")),
         g("g-ecosystems", 1, boxes("regulatory-systems", "finance-insurance-systems", "hmis", "quality-systems")),
     ])),
    (V_TT,
     "Achieving track and trace capabilities through DHSC architecture components, centralized traceability model (Fig. 24, PDF 55). The handbook uses the centralized model to illustrate and recommends no model.",
     ("row", [
         ("col", [g("g-external", 1, boxes("manufacturer-systems", "data-repositories", "global-platforms")),
                  ("col", boxes("wms", "tms", "hf-lmis", "dispensing-system"))]),
         ("col", [b("interop-component")]),
         g("g-data", 1, [g("g-analytics", 1, boxes("data-warehouse", "supply-chain-reports")),
                         g("g-traceability", 1, boxes("product-verification", "track-and-trace"))]),
         ("col", boxes("traceability-event", "individual", "nra")),
     ])),
    (V_PARTNERS,
     "Public health supply chain partners and the supply chain processes between them (Figs. 1-3, PDF 11-13). The handbook names the partners and the processes but does not assign processes to partners, so no relationship is drawn between them.",
     ("row", [
         g("g-partners", 3, boxes("moh", "procurer", "manufacturer", "nra", "central-warehouse", "regional-warehouse",
                                  "logistics-provider", "health-facility", "community-health", "individual", "private-sector")),
         g("g-processes", 2, boxes("cap-forecasting", "cap-supplier-contracts", "cap-procurement", "cap-order",
                                   "cap-warehouse", "cap-transportation", "cap-dispensing", "cap-traceability")),
     ])),
]

VIEW_CONNECTIONS = {V_TT: TT_FLOWS + TT_OTHER}
