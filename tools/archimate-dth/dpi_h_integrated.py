"""DPI-H RA "Integrated View" (draft v1 Figs. 3.2 and 3.5) as ArchiMate views.

Source: WHO/ITU Reference Architecture and Guidance for DPI-H, review draft v1
(library/who-dpi-h-reference-architecture-draft-v1): Figure 3.2 (PDF 59, the
full poster) and Figure 3.5 (PDF 77, the DPI-H layers only).

One element per box of the figure. Boxes the model already has are reused
(EXISTING). Where an existing element may be the same thing under another name,
the new element carries `candidateMatch` naming it, for the owner to decide, as
in dth_sc.py (Q-IV-2). REDDHI components carry `reddhi=true`. Layer and domain
membership is Aggregation from a Grouping; no other relationship is added,
because the figure draws none.

Applied with: python3 -I tools/archimate-dth/add_views.py tools/archimate-dth/dpi_h_integrated.py <in> <out>
"""

NAMESPACE = "https://github.com/litlfred/smart-ra#integrated-view"
SOURCE = "WHO DPI-H Reference Architecture review draft v1, Figs. 3.2 and 3.5"
VIEW_FOLDER = "1. Reference Architecture"

FIG32 = "DPI-H RA draft v1, Figure 3.2 'DPI-H Reference Architecture — Integrated View' (PDF 59); the DPI-H layers recur in Figure 3.5 (PDF 77)"


def p(page, **kw):
    return {"raPage": f"PDF {page}", **kw}


ELEMENTS = {
    'layer-goals': ("Grouping", 'Strategic health goals', FIG32, p(59)),
    'g1-trusted-data-foundations': ('Goal', 'Build trusted data foundations', FIG32, p(59, code='G1')),
    'g3-quality-continuity-of-care': ('Goal', 'Ensure quality and continuity of care', FIG32, p(59, code='G3')),
    'g4-personal-health-record': ('Goal', 'Establish trusted personal health records', FIG32, p(59, code='G4')),
    'g6-health-financing': ('Goal', 'Advance efficient and equitable health financing', FIG32, p(59, code='G6')),
    'g7-climate-epidemic-resilience': ('Goal', 'Strengthen climate and epidemic resilience', FIG32, p(59, code='G7')),
    'layer-governance': ("Grouping", 'Cross-cutting governance', FIG32, p(59)),
    'standards-certification-conformance': ('Principle', 'Standards, Certification & Conformance', FIG32, p(59)),
    'semantic-governance-stewardship': ('Principle', 'Semantic Governance & Stewardship', FIG32, p(59, candidateMatch='Information Model Governance (id-b0f5a5d5aa654a4a8d96f50f8364e54f)')),
    'auditability-assurance-accountability': ('Principle', 'Auditability, Assurance & Accountability', FIG32, p(59)),
    'layer-stakeholders': ("Grouping", 'Stakeholders', FIG32, p(59)),
    'financial-entities': ('Stakeholder', 'Financial entities', FIG32, p(59, candidateMatch='Health Insurance Organizations (id-afa7abb5039f46ae8f7f3f1ff15b77a2)')),
    'suppliers-manufacturers': ('Stakeholder', 'Suppliers / Manufacturers', FIG32, p(59, candidateMatch='Manufacturer / Distributor (id-66d0f91175c154b48413d57e9f952a34)')),
    'int-l-development-agencies': ('Stakeholder', "Int'l & Development Agencies", FIG32, p(59)),
    'layer-capabilities': ("Grouping", 'Capabilities', FIG32, p(59)),
    'access-consent-trust': ('Capability', 'Access, Consent, Trust', FIG32, p(59, candidateMatch='Identity & Access Management (id-615467fd36ab4ef083847eee4aeb8ec5)')),
    'knowledge-management': ('Capability', 'Knowledge Management', FIG32, p(59, candidateMatch='Guideline Adoption, Authoring and management (id-416d9bf3be8c40f8ba59c516b478800e)')),
    'clinical-services-care-coordination': ('Capability', 'Clinical Services & Care Coordination', FIG32, p(59)),
    'supply-chain': ('Capability', 'Supply Chain', FIG32, p(59, candidateMatch='Forecasting & Planning (id-e53b31972646454384c78f3380f5c40e)')),
    'climate-ph-surveillance': ('Capability', 'Climate & PH Surveillance', FIG32, p(59)),
    'layer-pos': ("Grouping", 'Point-of-service & functional applications', FIG32, p(59)),
    'provider-systems': ('ApplicationComponent', 'Provider Systems', FIG32, p(59, candidateMatch='Vendor EHR Product (id-3bd1011d76c843fa860255f00a6aa68f)')),
    'case-management': ('ApplicationComponent', 'Case Management', FIG32, p(59)),
    'chw-community': ('ApplicationComponent', 'CHW & Community', FIG32, p(59)),
    'citizen-patient-apps': ('ApplicationComponent', 'Citizen / Patient Apps', FIG32, p(59)),
    'supply-chain-functional': ('ApplicationComponent', 'Supply Chain Functional', FIG32, p(59, candidateMatch='Warehouse Management System (id-35d0806bcb5c46fab5102d75de09558f)')),
    'health-coverage-claims': ('ApplicationComponent', 'Health Coverage & Claims', FIG32, p(59, candidateMatch='Finance and Insurance Systems (id-38e8733e58775142ab2abec1b563131d)')),
    'financing-workforce-ops': ('ApplicationComponent', 'Financing & Workforce Ops', FIG32, p(59)),
    'public-health-apps': ('ApplicationComponent', 'Public Health Apps', FIG32, p(59)),
    'layer-reusable': ("Grouping", 'DPI-H reusable components', FIG32, p(59)),
    'domain-clinical-services': ("Grouping", 'Clinical Services', FIG32, p(59)),
    'domain-supply-chain': ("Grouping", 'Supply Chain', FIG32, p(59)),
    'domain-health-financing': ("Grouping", 'Health Financing', FIG32, p(59)),
    'benefits-package-registry': ('ApplicationComponent', 'Benefits Package Registry', FIG32, p(59)),
    'domain-public-health-analytics': ("Grouping", 'Public Health & Analytics', FIG32, p(59)),
    'ph-surveillance-platform': ('ApplicationComponent', 'PH Surveillance Platform', FIG32, p(59)),
    'domain-cross-cutting': ("Grouping", 'Cross-cutting', FIG32, p(59)),
    'ai-enabled-intelligence': ('ApplicationComponent', 'AI-Enabled Intelligence', FIG32, p(59)),
    'secondary-use': ('ApplicationComponent', 'Secondary use', FIG32, p(59)),
    'layer-shared': ("Grouping", 'DPI-H shared data layer', FIG32, p(59)),
    'client-registry-for-health': ('ApplicationComponent', 'Client Registry for Health', FIG32, p(59, reddhi='true')),
    'layer-dpif': ("Grouping", 'Foundational DPI (DPI-F)', FIG32, p(59)),
    'foundational-identity': ('ApplicationComponent', 'Foundational Identity', FIG32, p(59, candidateMatch='Identity Management Service (id-646c18afcfc54f4fb33ae93110e02c2c)')),
    'national-trust-services': ('ApplicationComponent', 'National Trust Services', FIG32, p(59, candidateMatch='DPI-F Security & Consent Module (id-d79aa0eec0584b0792b44bca408afeb6)')),
    'payment-rails': ('ApplicationComponent', 'Payment Rails', FIG32, p(59)),
    'data-exchange-fabric': ('ApplicationComponent', 'Data Exchange Fabric', FIG32, p(59)),
    'crvs-other-sector': ('ApplicationComponent', 'CRVS & Other-Sector', FIG32, p(59)),
    'geo-location-notification': ('ApplicationComponent', 'Geo-location · Notification', FIG32, p(59)),
    'layer-tech': ("Grouping", 'Technology', FIG32, p(59)),
    'hybrid-sovereign-cloud': ('Node', 'Hybrid / Sovereign Cloud', FIG32, p(59)),
    'ai-ml-platform': ('Node', 'AI / ML Platform', FIG32, p(59)),
    'security-trust-operations': ('Node', 'Security & Trust Operations', FIG32, p(59)),
    'data-platform': ('Node', 'Data Platform', FIG32, p(59, candidateMatch='Data Warehouse (id-2158ff0de2f95b2cbe005c3bf6fc9c01)')),
    'observability-devsecops': ('Node', 'Observability · DevSecOps', FIG32, p(59)),
    'layer-interop': ("Grouping", 'Interoperability (cross-cutting)', FIG32, p(59)),
    'open-standards': ('ApplicationComponent', 'Open standards', FIG32, p(59)),
    'integration-patterns': ('ApplicationComponent', 'Integration patterns', FIG32, p(59)),
}

EXISTING = {
    'g2-health-workforce': 'id-3f93004c75b54d8ca60caa93e40d0187',  # Ensure all health workers receive timely payments by adopting reliable digital payroll systems. This includes maintaining a health workforce registry to ensure qualification, retention, capacity building, and career development.
    'g5-supply-chain': 'id-3fd56c1375c44038a7d61f56715945ea',  # Safe health products and services delivered when and where they are needed
    'policy-legislation-regulation': 'id-88a90dfa38904fba930a49add401e660',  # Governance, Policy, and Legislation
    'cybersecurity-privacy-consent': 'id-d4539867eb074f9383ede25c9318a5eb',  # Privacy / Concent/ Trust
    'citizens-care-recipients': 'id-a2320dbc07e6450b94f3f0f3e03bb877',  # Patients
    'health-workforce': 'id-8d3dd8b68d504c2a9fe8cf414b16c127',  # Health Workers
    'government-moh': 'id-1c5c0bc9234e4282b654dbc71b9da706',  # Ministry of Health
    'healthcare-facilities': 'id-515be0d38c564767bc2b1ee5fcb0adb6',  # Health Care Institutions
    'research-academia': 'id-82fc8a35ade94ff3a02acc9194490fc8',  # Academic & Training Institutions
    'identity-mgmt': 'id-788f660553e14f0283b93c2dda3ae441',  # Client Identity Management
    'health-record-mgmt': 'id-4a08b39b55a6469098a89697af71daae',  # Health Record Sharing
    'health-workforce-mgmt': 'id-4d0a6161789f4a4ca8b13c7b2d542544',  # Health Workforce Management
    'health-financing': 'id-34c4ebbdf32b4062b7fe81718c599d83',  # Health Financing Management
    'analytics-bi': 'id-3d0c2c2525ed4131ae533eed8893d4d0',  # Analytics & Business Intelligence
    'pharmacy-dispensing': 'id-370b6bdcb29449c9be74644ffacc94aa',  # Dispensing System
    'computable-decision-support-engine': 'id-539b04ae45f147258d8253ae5cb87402',  # Decision Support Engine
    'supplier-registry': 'id-199c0717881f4992970d6ba85780b74e',  # Supplier registry
    'hmis': 'id-d626508a7dc55b1fb11bf34f57f8ddd9',  # Health Management Information System
    'lifelong-health-record': 'id-0e6d89398fff4f20994a31b4de58e7d7',  # SHR Repository
    'health-workforce-registry': 'id-350840520ae44f658b6ad3b3762e382e',  # DPI-H Health Workforce Registry (HWR)
    'facility-registry': 'id-4e0767822dcf46409554156a133fbc67',  # DPI-H: Facility Registry
    'product-registry': 'id-59c26d672a4248e0bb83cf4d26cba10c',  # Product Registry
    'terminology-service': 'id-3f41de2b51c24041b08243bf72b140d1',  # Terminology Service
    'logical-info-model-repo': 'id-c0d39bf67fe64f54b07fbeb9bf37d404',  # Logical Information Model Registry
    'information-mediator': 'id-3c5d846710034c4595e206e748d65e36',  # DPI-F Information Mediator
}

# Existing elements renamed to the handbook's names (owner, Q-IV-2 B, Q-IV-3 A).
# The old name is kept as property formerName. Only same-thing renames are here;
# narrower or differently typed elements got a new element with candidateMatch.
RENAMES = {
    'g2-health-workforce': 'Support a capable, well-distributed health workforce',  # was 'Ensure all health workers receive timely payments by adopting reliable digital payroll systems. This includes maintaining a health workforce registry to ensure qualification, retention, capacity building, and career development.'
    'g5-supply-chain': 'Optimise supply chain management',  # was 'Safe health products and services delivered when and where they are needed'
    'policy-legislation-regulation': 'Policy, Legislation & Regulation',  # was 'Governance, Policy, and Legislation'
    'cybersecurity-privacy-consent': 'Cybersecurity, Privacy & Consent',  # was 'Privacy / Concent/ Trust'
    'citizens-care-recipients': 'Citizens / Care recipients',  # was 'Patients'
    'healthcare-facilities': 'Healthcare facilities',  # was 'Health Care Institutions'
    'research-academia': 'Research / Academia',  # was 'Academic & Training Institutions'
    'identity-mgmt': 'Identity Management',  # was 'Client Identity Management'
    'health-record-mgmt': 'Health Record Management',  # was 'Health Record Sharing'
    'computable-decision-support-engine': 'Computable Decision Support Engine',  # was 'Decision Support Engine'
    'supplier-registry': 'Supplier Registry',  # was 'Supplier registry'
    'lifelong-health-record': 'Lifelong Health Record',  # was 'SHR Repository'
    'health-workforce-registry': 'Health Workforce Registry',  # was 'DPI-H Health Workforce Registry (HWR)'
    'facility-registry': 'Health Facility Registry',  # was 'DPI-H: Facility Registry'
    'logical-info-model-repo': 'Logical Information Model Repository',  # was 'Logical Information Model Registry'
}

MEMBERS = {
    "layer-goals": [
        "g1-trusted-data-foundations",
        "g2-health-workforce",
        "g3-quality-continuity-of-care",
        "g4-personal-health-record",
        "g5-supply-chain",
        "g6-health-financing",
        "g7-climate-epidemic-resilience"
    ],
    "layer-governance": [
        "policy-legislation-regulation",
        "cybersecurity-privacy-consent",
        "standards-certification-conformance",
        "semantic-governance-stewardship",
        "auditability-assurance-accountability"
    ],
    "layer-stakeholders": [
        "citizens-care-recipients",
        "health-workforce",
        "government-moh",
        "healthcare-facilities",
        "financial-entities",
        "suppliers-manufacturers",
        "int-l-development-agencies",
        "research-academia"
    ],
    "layer-capabilities": [
        "identity-mgmt",
        "access-consent-trust",
        "health-record-mgmt",
        "knowledge-management",
        "clinical-services-care-coordination",
        "health-workforce-mgmt",
        "health-financing",
        "supply-chain",
        "analytics-bi",
        "climate-ph-surveillance"
    ],
    "layer-pos": [
        "provider-systems",
        "case-management",
        "pharmacy-dispensing",
        "chw-community",
        "citizen-patient-apps",
        "supply-chain-functional",
        "health-coverage-claims",
        "financing-workforce-ops",
        "public-health-apps"
    ],
    "layer-reusable": [
        "domain-clinical-services",
        "domain-supply-chain",
        "domain-health-financing",
        "domain-public-health-analytics",
        "domain-cross-cutting"
    ],
    "domain-clinical-services": [
        "computable-decision-support-engine"
    ],
    "domain-supply-chain": [
        "supplier-registry"
    ],
    "domain-health-financing": [
        "benefits-package-registry"
    ],
    "domain-public-health-analytics": [
        "ph-surveillance-platform",
        "hmis"
    ],
    "domain-cross-cutting": [
        "ai-enabled-intelligence",
        "secondary-use"
    ],
    "layer-shared": [
        "client-registry-for-health",
        "lifelong-health-record",
        "health-workforce-registry",
        "facility-registry",
        "product-registry",
        "terminology-service",
        "logical-info-model-repo"
    ],
    "layer-dpif": [
        "foundational-identity",
        "national-trust-services",
        "payment-rails",
        "data-exchange-fabric",
        "crvs-other-sector",
        "geo-location-notification"
    ],
    "layer-tech": [
        "hybrid-sovereign-cloud",
        "ai-ml-platform",
        "security-trust-operations",
        "data-platform",
        "observability-devsecops"
    ],
    "layer-interop": [
        "information-mediator",
        "open-standards",
        "integration-patterns"
    ]
}

# Figure 3.2's short text under each box, transcribed from the figure (PDF 59). Keyed as in dpi_h_integrated.py.
FIGURE_NOTES = {
    "g1-trusted-data-foundations": "Capture once, use many times · Quality, secondary use, AI training",
    "g2-health-workforce": "Timely pay, proven skills, equitable distribution · Payroll, credentials, CPD",
    "g3-quality-continuity-of-care": "Protocols that guide · Decision support, care coord.",
    "g4-personal-health-record": "Right to your own record · Portable, secure, consent-driven",
    "g5-supply-chain": "Safe health products when & where needed · Forecast, traceability",
    "g6-health-financing": "Smarter spending, stronger protection · PFM, coverage, claims",
    "g7-climate-epidemic-resilience": "Predict early, act fast · Surveillance, AER, response",
    "policy-legislation-regulation": "Legal mandates · data-protection law · Architecture principles · investment governance",
    "cybersecurity-privacy-consent": "Zero-trust · encryption · PKI mgmt · Granular, revocable, purpose-bound consent",
    "standards-certification-conformance": "FHIR profiles · SNOMED · ICD · LOINC · GS1 · Test harnesses · IHE Connectathons · certification",
    "semantic-governance-stewardship": "Reference + local terminology curation · Logical model versioning · code-system maps",
    "auditability-assurance-accountability": "Immutable logs · digital signatures · Independent audit · open disclosure",
    "citizens-care-recipients": "Families & caregivers",
    "health-workforce": "Providers, CHWs, system mgrs",
    "government-moh": "Regulators, MoF, Public Health Auth.",
    "healthcare-facilities": "Hospitals, labs, clinics",
    "financial-entities": "Payers, insurers, procurement",
    "suppliers-manufacturers": "Other supply chain actors",
    "int-l-development-agencies": "Civil society, media, advocacy",
    "research-academia": "Training, academic, research",
    "identity-mgmt": "Person identification · Record linkage · Identity reconciliation · Federation to DPI-F",
    "access-consent-trust": "Consent & access mgmt · Verification · Provenance · Trust services integration",
    "health-record-mgmt": "Longitudinal record curation · Provenance & versioning · Patient-controlled views · Secondary-use enablement",
    "knowledge-management": "Terminology curation · Logical info-model authoring · Computable guidelines · Semantic stewardship",
    "clinical-services-care-coordination": "Decision support at PoC · Care planning & transitions · Orders & medicines mgmt · Referrals & task management",
    "health-workforce-mgmt": "Registration & licensing · Payroll & incentives · Qualifications, CPD & competency · Workforce planning & distribution",
    "health-financing": "PFM & risk pooling · Enrolment, eligibility & entitlement · Purchasing & claims · Contracts, payments & revenue",
    "supply-chain": "Forecasting & planning · Procurement & logistics · Dispensing & traceability · Supplier & product stewardship",
    "analytics-bi": "Analytics · Reporting · Business intelligence · Performance & equity insights",
    "climate-ph-surveillance": "Disease surveillance & alert · Adverse event reporting · Outbreak mgmt & routine HMIS · Communication mgmt · Climate & incident mgmt",
    "provider-systems": "EMR / EHR · HIS · LIMS · PACS · RIS · e-Prescribing (EPMA) · Telemedicine clients",
    "case-management": "Electronic Immunization Reg. · HIV / TB / MNCH registries · Disease-specific tooling · Patient follow-up workflows",
    "pharmacy-dispensing": "Pharmacy mgmt system · Dispensing apps · Pharmacovigilance entry · Inventory at POS",
    "chw-community": "CHW field apps · Outreach / campaigns · Offline-first tooling · Household registration",
    "citizen-patient-apps": "PHR / Digital Health Wallet · Self-service booking · Citizen alerting client · Consent dashboard UI",
    "supply-chain-functional": "WMS / LMIS · Transport mgmt (TMS) · Procurement / e-tender · Cold-chain monitoring",
    "health-coverage-claims": "Claims authoring · Beneficiary Registry · Member / provider portals · Contracts & Benefit Mgmt",
    "financing-workforce-ops": "IFMIS / Treasury · HFIS / Budget planning · HRIS · Payroll · LMS / training · Audit & disclosure tools",
    "public-health-apps": "Contact tracing · Outbreak management · Disease surveillance dashboards · Outbreak alerting",
    "domain-clinical-services": "Components that consume LHR & knowledge at the point of care",
    "domain-supply-chain": "Shared services for supplier and traceability data across logistics",
    "domain-health-financing": "Reference data defining coverage and entitlements for purchasing",
    "domain-public-health-analytics": "Platforms for secondary use, intelligence, response",
    "domain-cross-cutting": "Cross-cutting",
    "computable-decision-support-engine": "CDS Hooks · SMART on FHIR · Consumes LHR + standards-based computable guidelines",
    "supplier-registry": "Vetted manufacturers, 3PLs · Cross-domain reuse for procurement & traceability",
    "benefits-package-registry": "Authoritative spec of covered services, tariffs & rules · Consumed by claims & PFM",
    "ph-surveillance-platform": "Event / case detection · Outbreak workflows · IHR / IPS cross-border",
    "hmis": "Aggregated indicators · M&E · dashboards · Performance & equity",
    "ai-enabled-intelligence": "Sovereign, reusable models · Risk stratification · Climate-health forecasting",
    "secondary-use": "Curated, consented, de-identified extracts flow into AI / ML training, public-good analytics, performance & equity, IHR / IPS reporting",
    "client-registry-for-health": "Person Identity · Health-sector master patient index · Unique health ID · Identity reconciliation · Record linkage",
    "lifelong-health-record": "Health Record · Longitudinal record · FHIR-based store · Provenance, versioning · Consent-scoped views",
    "health-workforce-registry": "Workforce · Verified providers, credentials, licensing · Consumed by EMR, claims, surveillance",
    "facility-registry": "Location · List of all health facilities (public + private) · Geocoded, services offered · catchments",
    "product-registry": "Health Products · Health products, devices and commodities · GTIN · IDMP · UDI · GS1",
    "terminology-service": "Semantics – Meaning · Code systems, value sets & concept maps · SNOMED · ICD · LOINC · Local code systems · Reference value sets",
    "logical-info-model-repo": "Syntax – Structure · Structural artefacts and national datasets · FHIR profiles · eObjects · IPS · datasets · Versioning & stewardship",
    "foundational-identity": "eKYC · MFA · biometrics · National / federated ID · Population register",
    "national-trust-services": "PKI · digital signatures · Verifiable credentials · Certificate authority · GDHCN",
    "payment-rails": "Treasury · fast payments · Provider disbursement · Workforce payroll",
    "data-exchange-fabric": "Cross-sectoral · Scalable arch. · Brokered API access · Audit, throttling, SLA",
    "crvs-other-sector": "Whole-of-government · Birth, death (cause: ICD) · Social protection, education",
    "geo-location-notification": "Cross-sectoral data + channels · Common Geo Reg. · address · SMS · email · push",
    "hybrid-sovereign-cloud": "Public, private, on-prem · data residency · Containers · Kubernetes · edge",
    "ai-ml-platform": "Sovereign + responsible AI · Model registry · MLOps · bias monitoring",
    "security-trust-operations": "Zero-trust posture · SIEM / SOAR · IAM · HSM · encryption",
    "data-platform": "Lakehouse + warehouse · ETL / ELT · MDM · privacy-preserving",
    "observability-devsecops": "Connectivity, SRE, CI/CD · Logs · metrics · traces · IaC",
    "information-mediator": "API gateway · HIE · Authenticates, authorises, routes, transforms, audits every transaction · Reuses DPI-F fabric where available",
    "open-standards": "HL7 FHIR · IHE · openEHR · IPS · SNOMED CT · ICD-11 · LOINC · GS1 / GTIN · IDMP / UDI · CDS Hooks · SMART on FHIR · OpenID / OAuth2 · DICOM",
    "integration-patterns": "REST APIs (FHIR R4) · Event streams · Document (IHE) · Federated query · Bulk data ($export) · Cross-border (IHR/IPS)",
}

PROPERTIES = {k: {"figureNote": v} for k, v in FIGURE_NOTES.items()}
# REDDHI components (starred in the figure), whether new or already in the model
for k in ("client-registry-for-health", "lifelong-health-record", "health-workforce-registry",
          "facility-registry", "product-registry"):
    PROPERTIES[k]["reddhi"] = "true"

RELATIONS = [("Aggregation", g, m) for g, ms in MEMBERS.items() for m in ms]


def g(key, cols, kids):
    return ("group", key, cols, kids)


def b(key):
    return ("box", key)


def boxes(*keys):
    return [b(k) for k in keys]


INTEROP = g("layer-interop", 1, [b('information-mediator'), b('open-standards'), b('integration-patterns')])

VIEWS = [
    ("DPI-H Reference Architecture — Integrated View (Fig. 3.2)", FIG32,
     ("row", [("col", [
            g("layer-goals", 7, [b('g1-trusted-data-foundations'), b('g2-health-workforce'), b('g3-quality-continuity-of-care'), b('g4-personal-health-record'), b('g5-supply-chain'), b('g6-health-financing'), b('g7-climate-epidemic-resilience')]),
            g("layer-governance", 5, [b('policy-legislation-regulation'), b('cybersecurity-privacy-consent'), b('standards-certification-conformance'), b('semantic-governance-stewardship'), b('auditability-assurance-accountability')]),
            g("layer-stakeholders", 8, [b('citizens-care-recipients'), b('health-workforce'), b('government-moh'), b('healthcare-facilities'), b('financial-entities'), b('suppliers-manufacturers'), b('int-l-development-agencies'), b('research-academia')]),
            g("layer-capabilities", 10, [b('identity-mgmt'), b('access-consent-trust'), b('health-record-mgmt'), b('knowledge-management'), b('clinical-services-care-coordination'), b('health-workforce-mgmt'), b('health-financing'), b('supply-chain'), b('analytics-bi'), b('climate-ph-surveillance')]),
            g("layer-pos", 9, [b('provider-systems'), b('case-management'), b('pharmacy-dispensing'), b('chw-community'), b('citizen-patient-apps'), b('supply-chain-functional'), b('health-coverage-claims'), b('financing-workforce-ops'), b('public-health-apps')]),
            g("layer-reusable", 7, [g('domain-clinical-services', 1, boxes(*['computable-decision-support-engine'])), g('domain-supply-chain', 1, boxes(*['supplier-registry'])), g('domain-health-financing', 1, boxes(*['benefits-package-registry'])), g('domain-public-health-analytics', 2, boxes(*['ph-surveillance-platform', 'hmis'])), g('domain-cross-cutting', 2, boxes(*['ai-enabled-intelligence', 'secondary-use']))]),
            g("layer-shared", 7, [b('client-registry-for-health'), b('lifelong-health-record'), b('health-workforce-registry'), b('facility-registry'), b('product-registry'), b('terminology-service'), b('logical-info-model-repo')]),
            g("layer-dpif", 6, [b('foundational-identity'), b('national-trust-services'), b('payment-rails'), b('data-exchange-fabric'), b('crvs-other-sector'), b('geo-location-notification')]),
            g("layer-tech", 5, [b('hybrid-sovereign-cloud'), b('ai-ml-platform'), b('security-trust-operations'), b('data-platform'), b('observability-devsecops')])]), INTEROP])),
    ("DPI-H Reference Architecture — DPI-H layers (Fig. 3.5)", "DPI-H RA draft v1, Figure 3.5 (PDF 77)",
     ("row", [("col", [
            g("layer-pos", 9, [b('provider-systems'), b('case-management'), b('pharmacy-dispensing'), b('chw-community'), b('citizen-patient-apps'), b('supply-chain-functional'), b('health-coverage-claims'), b('financing-workforce-ops'), b('public-health-apps')]),
            g("layer-reusable", 7, [g('domain-clinical-services', 1, boxes(*['computable-decision-support-engine'])), g('domain-supply-chain', 1, boxes(*['supplier-registry'])), g('domain-health-financing', 1, boxes(*['benefits-package-registry'])), g('domain-public-health-analytics', 2, boxes(*['ph-surveillance-platform', 'hmis'])), g('domain-cross-cutting', 2, boxes(*['ai-enabled-intelligence', 'secondary-use']))]),
            g("layer-shared", 7, [b('client-registry-for-health'), b('lifelong-health-record'), b('health-workforce-registry'), b('facility-registry'), b('product-registry'), b('terminology-service'), b('logical-info-model-repo')]),
            g("layer-dpif", 6, [b('foundational-identity'), b('national-trust-services'), b('payment-rails'), b('data-exchange-fabric'), b('crvs-other-sector'), b('geo-location-notification')])]), INTEROP])),
]

VIEW_CONNECTIONS = {}
