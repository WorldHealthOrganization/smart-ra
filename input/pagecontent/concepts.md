These are the core terms used in this specification. These are largely inspired by **TOGAF/ArchiMate**, and **OpenHIE**. The glossary is grouped into layers.  
Some examples are provided for clarity.

---

## Business Layer

---

### Goal
> A high-level statement of intent, direction, or desired end state for an organization and its stakeholders. 

*In principle, a goal can represent anything a stakeholder may desire, such as a state of affairs, or a produced value. Examples of goals are: to increase profit, to reduce waiting times at the helpdesk, or to introduce online portfolio management. Goals are typically used to measure success of an organization. Goals are generally expressed using qualitative words; e.g., "increase", "improve", or "easier". Goals can also be decomposed; e.g., “increase profit” can be decomposed into the goals "reduce cost" and "increase sales". However, it is also very common to associate concrete outcomes with goals, which can be used to describe both the quantitative and time-related results that are essential to describe the desired state, and when it should be achieved.*    


---


### Value

> The relative worth, utility, or importance of a concept.

*Value represents the usefulness, advantage, benefit, desirability, or gain for a customer, stakeholder, or end user by, for example, selling a product, using a service, or completing some activity. Value is often expressed in terms of money, but it has long since been recognized that non-monetary value is also essential to business; for example, practical/functional value (including the right to use a service), and the value of information or knowledge. Though value can hold internally for some system or organizational unit, it is most typically applied to external appreciation of goods, services, information, knowledge, or money, normally as part of some sort of customer-provider relationship. A value can be associated with any concept. To model the stakeholder for whom this value applies, this stakeholder can also be associated with that value. Although the name of a value can be expressed in many different ways (including amounts, objects), where the “functional” value of an architecture element is concerned, it is recommended to try and express it as an action or state that can be performed or reached as a result of the corresponding element being available.*


---


### Business Capability
> A particular ability that a business may possess or exchange to achieve a specific purpose.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Health Workforce Management"_  


---


### Business Function
> A collection of business processes based on a chosen set of criteria, closely aligned to an organization.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Managing Workforce Identity"_  

---


### Business Process
> Groups behavior based on an ordering of activities. It defines a set of products or business services.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Assign Unique Health Worker ID"_  


---


### Value Stream
An end-to-end stakeholder journey that delivers value across multiple business capabilities, business functions (BF), and business processes (BP).


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_Examples:_  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- _"Register and Deploy a Qualified Health Worker"_  


---


### Stakeholder

> Represents the role of an individual, team, or organization (or classes thereof) that represents their interests in the effects of the architecture.

A stakeholder has one or more interests in, or concerns about, the organization and its Enterprise Architecture. In order to direct efforts to these interests and concerns, stakeholders change, set, and emphasize goals. Stakeholders may also influence each other. Examples of stakeholders are the Chief Executive Officer (CEO), the board of directors, shareholders, customers, business and application architects, but also legislative authorities. The name of a stakeholder should preferably be a noun.


---


### Business Outcome

> An end result, effect, or consequence of a certain state of affairs. 

Outcomes are high-level, business-oriented results produced by capabilities of an organization, and by inference by the core elements of its architecture that realize these capabilities. Outcomes are tangible, possibly quantitative, and time-related, and can be associated with assessments. An outcome may have a different value for different stakeholders. The notion of outcome is important in business outcome-driven approaches to Enterprise Architecture and in capability-based planning. Outcomes are closely related to requirements, goals, and other intentions. The distinction between goals and outcomes is important. Simply put, a goal is what you want, and an outcome is what you get. Outcomes are the end results, and goals or requirements are often related to outcomes that should be realized. Capabilities can be designed to achieve such outcomes. However, not all outcomes relate to goals. When modeling a future state, an outcome models some result or effect that is expected to have been achieved or occur at that future point in time. Unlike goals, outcomes can also be used to model potentially unwanted effects; for example, in order to design appropriate mitigating measures. Outcome names should unambiguously identify end results that have been achieved or are expected to be achieved at a definite point in the future. Examples include "First-place customer satisfaction ranking achieved"” and "Key supplier partnerships in place"”. Outcome names can also be more specific; e.g., "10% year-over-year quarterly profits increase in 2018".   


---


### Product

> A coherent collection of services and/or passive structure elements, accompanied by a contract, which is offered as a whole to (internal or external) customers. 

This definition covers both intangible, services-based, or information products that are common in information-intensive organizations, as well as tangible, physical products. A financial or information product consists of a collection of services along with a contract that specifies the characteristics, rights, and requirements associated with the product. "Buying" a product gives the customer the right to use the associated services. Generally, the product element is used to specify a product type. The number of product types in an organization is typically relatively stable compared to the processes that realize or support the products. "Buying" is usually one of the services associated with a product which results in a new instance of that product (belonging to a specific customer). Similarly, there may be services to modify or destroy a product. A product may aggregate or compose business services, application services, technology services, business objects, data objects, and technology passive structure elements (artifacts and material), as well as a contract. Hence a product may aggregate or compose elements from other layers than the Business Layer. A value may be associated with a product. The name of a product is usually the name used in the communication with customers, or possibly a more generic noun (e.g., "travel insurance").   


---


## Application layer


### Application Service

> An explicitly defined exposed application behavior. An application service exposes the functionality of components to their environment. 

This functionality is accessed through one or more application interfaces and is realized by one or more application functions that are performed by the component. It may require, use, and produce data objects. An application service should be meaningful from the point of view of the environment; it should provide a unit of behavior that is, in itself, useful to its users. It has a purpose that states this utility to the environment in terms of the value it delivers, modeled as a value element associated with the service. This means that if this environment includes business processes, application services should have business relevance. An application service may serve business, application, and technology behavior or active structure elements. An application function or process may realize an application service. An application interface may be assigned to an application service. An application service may access data objects. The name of an application service should preferably be a verb ending with "-ing"; e.g., "transaction processing". Also, a name explicitly containing the word "service" may be used.  


---


### Application Component 

> An  encapsulation of application functionality aligned to implementation structure, which is modular and replaceable. 

An application component is a self-contained unit. As such, it is independently deployable, reusable, and replaceable. An application component performs one or more application functions. It encapsulates its behavior and data, exposes services, and makes them available through interfaces. Cooperating application components are connected via application collaborations. An application component may be assigned to one or more application functions. An application component has one or more application interfaces, which expose its functionality. Application interfaces of other application components may serve an application component. The name of an application component should preferably be a noun. The application component element is used to model entire applications (i.e., deployed and operational IT systems, and individual parts of such applications, at all relevant levels of detail. Application components can realize other application components.  



