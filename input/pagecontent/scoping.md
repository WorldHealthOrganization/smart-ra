### DRAFT Architecture Scope

<div style="display:block">
  <img src="../images/RAscope.JPG" alt="RA alignment image" width="700em"/>
</div>

The machine-readable DPI-H Reference Architecture (RA) aims to provide a modular, standards-based framework to guide the development and alignment of national digital health systems.

#### DRAFT Guiding Principles

- Informed by the OpenHIE framework and foundational national content such as the Core Data for Interoperability (CDI) and national Core Implementation Guides (IGs).
- Supports the consistent and systematic development of country-specific, use case-driven FHIR Implementation Guides.
- Promotes alignment across foundational national digital infrastructure and healthcare systems through consistent architectural patterns and interoperable service definitions.

#### DRAFT In-Scope

1. Define requirements for interoperability across domains and services.  
2. Define generic user personas, systems, functional roles, and processes across the health system to model user scenarios and system interactions that DPI-H components are expected to support.  
3. Define how national foundational digital infrastructure (e.g., identity, consent, messaging) integrates with health-sector infrastructure components (e.g., shared health repositories, registries). *— at architectural level_*  
4. Define mechanisms and identify APIs to enable interoperability between digital public infrastructure components and applications supporting service delivery, data exchange, and decision-making. *— at operational level_* 
5. Define trust services required for secure and ethical data exchange
6. Define reusable architectural patterns to support country-level customization while ensuring alignment with global conformance requirements.

#### Out of Scope

- The design and internal architecture of Point of Service (PoS) applications, registries, and line-of-business systems.
- The developement of National and Use Case–Specific FHIR Implementation Guides (e.g., for Immunisation, Maternal Health). However, the RA will use or refernece use-case specific FHIR IGs where available.
- Country-specific Enterprise Architectures or digital transformation strategies.
