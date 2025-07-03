Instance: ClientRegistry
InstanceOf: ActorDefinition
Usage: #definition
* name = "Client Registry"
* title = "Client Registry"
* description = "The Client Registry assists in uniquely identifying individuals who receive health care services by:
Maintaining a central registry of all patients and their demographics and assigning a unique identifier to each patient.  \n
Linking patient registration entries that result due to changes in patient demographics (patient moved to another location), data entry errors during patient registration, or missing demographic information.  \n
Enabling health care workers to identify facilities at which a patient has received care."
* status = #active
* experimental = false
* publisher = "OpenHIE"
* type = #system



Instance: HealthWorkerRegistry
InstanceOf: ActorDefinition
Usage: #definition
* name = "Health Worker Registry"
* title = "Health Worker Registry"
* description = "A registry that maintains information about health workers, including their identifiers, roles, and affiliations.  \n
The Health Worker Registry serves as an authority for maintaining the unique identities of health workers within a context.  \n
* Pulls the minimum dataset of health workforce information from the various source data systems.  \n 
* Merges the source data systems into an authoritative registry of health workers according to a data governance policy.   \n
* Allows queries of health worker information by client systems.  \n"
* status = #active
* experimental = false
* publisher = "OpenHIE"
* type = #system



Instance: FacilityRegistry
InstanceOf: ActorDefinition
Usage: #definition
* name = "Facility Registry"
* title = "Facility Registry"
* description = "A registry that stores and manages standardized information about health facilities, serving as a central authority for facility data."
* status = #active
* experimental = false
* publisher = "OpenHIE"
* type = #system



Instance: SharedHealthRecord
InstanceOf: ActorDefinition
Usage: #definition
* name = "Shared Health Record"
* title = "Shared Health Record"
* description = "A centralized repository that stores and manages longitudinal patient health records, enabling access to clinical data across systems."
* status = #active
* experimental = false
* publisher = "OpenHIE"
* type = #system



Instance: InteroperabilityLayer
InstanceOf: ActorDefinition
Usage: #definition
* name = "Interoperability Layer"
* title = "Interoperability Layer"
* description = """A component that enables communication of services across domains and organizations, This MMAY include:  
 - Service discovery and identification  
 - Service identity life cycle management  
 - Encryption of service to service communications  
 - Authentication, authorization and permissions at the service level (not application or user level)  
 - Service monitoring and transaction logging  
  
Depending on the governance requirements, this layer may also include tools to centralize service logic including message routing, workflow and service orchestration, and message translation.
"""
* status = #active
* experimental = false
* publisher = "smart-ra"
* type = #system



Instance: TerminologyService
InstanceOf: ActorDefinition
Usage: #definition
* name = "Terminology Service"
* title = "Terminology Service"
* description = "A service that provides access to standardized code systems, value sets, and mappings to ensure consistent use of terminology across systems."
* status = #active
* experimental = false
* publisher = "OpenHIE"
* type = #system



Instance: LogisticsManagementInformationSystem
InstanceOf: ActorDefinition
Usage: #definition
* name = "Logistics Management Information System"
* title = "Logistics Management Information System"
* description = "A system that manages the supply chain operations, including tracking and distribution of health commodities."
* status = #active
* experimental = false
* publisher = "OpenHIE"
* type = #system




Instance: HealthManagementInformationSystem
InstanceOf: ActorDefinition
Usage: #definition
* name = "Health Management Information System"
* title = "Health Management Information System"
* description = "A system that collects, analyzes, and reports health data for monitoring and decision-making purposes."
* status = #active
* experimental = false
* publisher = "OpenHIE"
* type = #system




Instance: PointOfServiceSystem
InstanceOf: ActorDefinition
Usage: #definition
* name = "Point-of-Service System"
* title = "Point-of-Service System"
* description = "A system used at the point of care, such as electronic medical records (EMRs), to capture and manage patient encounters and clinical data."
* status = #active
* experimental = false
* publisher = "OpenHIE"
* type = #system




