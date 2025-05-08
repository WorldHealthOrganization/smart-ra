### Architect's Guide


<div style="display:block">
	<img src="architecture.png" width="675em"/>
</div>


#### Scope

In the development of Reference Architecture, the following areas are to be considered:
* The intersection of health infrastructural components with foundational infrastructural components 
* The intersection of health infrastructural components with digital health applications
* An individuals access to personal health records and utilization digital health services
* The necessary digital infrastructure to operationalization workflows defined in [Digital Adaptation Kits](https://pmc.ncbi.nlm.nih.gov/articles/PMC8885357/)

#### Methodology and Tooling

Architectural documentation shall follow the [WHO SMART Guideline](https://www.who.int/teams/digital-health-and-innovation/smart-guidelines) methodology which structures digital health documentation into the following components:
* L1: Narrative
* L2: Operational
* L3: Machine Readable
* L4: Executable
* L5: Dynamic

The primary focus will be creating the L3 artifacts necessary for the realizing of prioritized digital health workflows and a set of tests that can be utilized by digital health vendors to determine the adherence of their products to that infrastructure.  In some cases, the L2 artifacts may not be fully developed and the architects will contribute to the development of these artifacts in coordination with appropriate subject matter experts.

For the production of content, we utilize the [HL7 FHIR IG Publisher](https://build.fhir.org/ig/FHIR/ig-guidance/) as the main publication tool for the development of architectural content.  In particular, the [Authoring L3 Content](https://smart.who.int/ig-starter-kit/authoring_overview.html).

#### Utilization of L2: Digital Adaptation Kits

The Digital Adaptation Kits (DAKs) provide a structured set of business requirements for digital health applications.  While some of these artifacts will be or are already being developed using standards for business requirements (e.g. BPMN, DMN tables) this artifacts are primarily designed for accurate representation of business needs from subject matter experts by business analysts. We are developing tooling to automate or ease the development of corresponding L3 artifacts in terms of HL7 FHIR Resources.

One essential component of this is the definition and representation of the appropriate requirements (as FHIR Requirements resources)  and system or human actors (as FHIR ActorDefinition resources).  (Draft) examples include:
* [DAK: Birth Defects Surveillance](http://worldhealthorganization.github.io/smart-dak-bds/artifacts.html) from the [system requirements](https://worldhealthorganization.github.io/smart-dak-bds/system-requirements.html)
* [DAK: Clinical Care in Crises](http://worldhealthorganization.github.io/smart-dak-ccc/artifacts.html) from the [system requirements](https://worldhealthorganization.github.io/smart-dak-bds/system-requirements.html)
* [DAK: Immunizations](http://worldhealthorganization.github.io/smart-dak-immz/artifacts.html) from the [system requirements](https://worldhealthorganization.github.io/smart-dak-immz/system-requirements.html)


Another essential component are the generic business processes and workflows (which we are standardizing to BPMN diagrams for computability).  These workflows outline the main functionality needed for the actors/generic personas.  The Reference Architecture shall define the digital health infrastructural components and necessary transactions (e.g. messages sent via APIs) to realize these workflows.


#### Relationship to OpenHIE 
The Reference Architecture draws from the [OpenHIE](https://ohie.org/) architectural components, in particular the Business Domain Services & Registry Services.

==To Do:== review [OpenHIE components](https://guides.ohie.org/arch-spec/architecture-specification/overview-of-the-architecture#architecture-component-descriptions) and include them, refining as necessary, into the Reference Architecture.

* Registry Services:
  * Terminology Services
  * Client Registry
  * Facility Registry
  * Health Worker Registry
  * Product Catalogue
* Business Domain Services:
  * Logistics Management System
  * Shared Health Records
  * Health Management Information System
  * Finance and Insurance Service

These components should be brought into the architecture by identifying a specific requirement or workflow coming from a DAK.

#### Architects and Technical Writers


==To Do:== add your name 
The following people are contributing to the core architecture
* Carl Leitner (WHO)
* Esteban Hebel (Chile)
* Rada Hussein (LBG)
* José Costa Teixeira (Belgium)
* Anusree Jayakrishnan (Centre for Digital Public Infrastructure)
* Umer Nisar (CSIRO Australia)
* Eric Ramirez (El Salvador)



