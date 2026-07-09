# 3.7  Architecture, conformance and testing

## Purpose

When a country or organization defines its digital health architecture, it does so in the
context of its own health priorities, existing infrastructure, and regulatory environment.
The reference architecture offers a common benchmark against which such architectures — and
the systems that realise them — can be assessed, whether they were developed with the
reference architecture in mind or independently.

What makes this possible is that the reference architecture is not merely a narrative: its
elements and the relationships between them are **structured and machine-readable** (§3.1).
An architecture expressed in this way can be *tested*, not only described — and testing
applies at two complementary levels:

- **Conformance of the systems** — whether the components that realise the architecture
  correctly implement the capabilities, services, and standards expected of them.
- **Conformance of the architecture itself** — whether an architecture is well-formed and
  aligned with the reference: its elements defined with sufficient rigour, its relationships
  complete and traceable, and any deviations or gaps made explicit (whether the architecture
  *adopts*, *adapts*, or *maps to* the reference).

A third, related question — whether the architecture is actually achieving its goals — is
assessed by monitoring the **outcomes** those goals define, traced back through the
capabilities and components meant to deliver them.

The rest of this section sets out the small, structured model that makes these assessments
possible: how a system's conformance to its role is defined and tested, and how the same
typed structure lets a whole architecture be checked for alignment, completeness, and gaps.

## The model

Each construct is bound to one ArchiMate element type. The element types and the four
structural relationships introduced in §3.1 (*Realises, Composes, Serves, Accesses*) carry
most of the model. Describing conformance and testing requires a small addition to that
palette, summarised in Table 3.7.1 and to be reflected in Table 3.1.

*Table 3.7.1: Element and relationship types added for conformance and testing*

| Type | What it represents | Example |
|---|---|---|
| Application Interaction *(element)* | Collective application behaviour performed by two or more components | A transaction such as *Provide and Register* between a Document Source and a Document Repository |
| Application Function *(element)* | Internal automated behaviour of a component | The document-registration behaviour that realises a registration service |
| Assignment *(relationship)* | Allocates an active structure element to the behaviour it performs | An actor performs the interaction it takes part in; a component performs its function |
| Triggering *(relationship)* | A causal "leads to" between behaviours | A user's create-and-submit action triggers the transaction |

The two element types are already present in the metamodel; the two relationships are the
additions required to §3.1. Further types (Application Interface, Business Process and Role,
Requirement/Constraint) are introduced only by the UI-testing and explicit-criteria views,
and would be declared if and when those views are adopted; see the companion notes.

### Actors as Application Components

An **actor** is an abstract information-processing role — for example a *Document Source*
or a *Patient Demographics Consumer*. It names a set of responsibilities, independently of
any product that fulfils them. An actor is modelled as an **Application Component**. A
concrete system — a vendor product, a national service — is also an Application Component,
bound to the actor by a **realisation relationship**: *the system realises the actor*. One
system may realise several actors; one actor may be realised by many systems.

### Offered and required Application Services

What an actor *does* is expressed as **Application Services**, related to the actor by two
different relationship types according to whether the service is offered or required:

- A service the actor **offers** is one it **realises** — a service it exposes, which in
  turn *serves* its consumers. This is the **responder** role in an interaction.
- A service the actor **requires** is one that **serves** the actor — a capability it
  depends on. This is the **initiator** role in an interaction.

A component thus *realises* the services it provides and is *served by* the services it
consumes; it never *serves* its own service. These offered and required services are the
contractually meaningful surface of the actor — the externally observable behaviour
against which conformance is declared.

Each actor–service association additionally carries a support qualifier: the service may
be **mandatory** or **optional** for that actor. A mandatory service must be supported by
any system claiming the actor; an optional service may be supported or not, and where it
is, must behave as specified. This is independent of the offered/required *direction*, and
corresponds to the *required*/*optional* (R/O) designation an IHE profile gives each
transaction. ArchiMate has no native qualifier for it, so it is recorded as a **Property**
on the serving relationship, or — where normative and testable — as a motivation-layer
**Constraint**. (Note the two senses of "required": a *required service* is one the actor
depends on; a *mandatory* service is one whose support is obligatory. This document
reserves **offered/required** for the direction and **mandatory/optional** for support.)

### Interactions and transactions

The architecture models the exchange between two actors as an **Application Interaction** —
collective application behaviour performed by two or more cooperating components. The
interaction is the shared behaviour the initiator and responder jointly perform; each actor
owns its side, and each is **assigned to** the interaction.

A **transaction** — a fully specified machine-to-machine protocol exchange, with defined
trigger events, message semantics, and expected actions — is **one kind** of Application
Interaction: its precise, specifiable subset. The architecture works at the broader level
of interaction, because the same service is often reached by interactions that are not
machine-to-machine transactions (see *Multiple access patterns to a single service*) and by
exchanges not yet specified to transaction level. Where an interaction *is* specified as a
transaction, that specification may be supplied by a framework such as IHE rather than
restated here (see *Alignment with IHE profiles*).

Crucially, **the interaction is not the unit of conformance.** It describes an exchange —
useful for documentation, sequence diagrams, and message specification — but a product is
never certified as "conformant to an interaction" in isolation; it is certified as
correctly playing an actor's role *in* that interaction.

### Multiple access patterns to a single service

The architecture treats the Application Service as the stable unit of capability and the
Application Interaction as one *way of reaching* it. A single service can be reached
through more than one interaction — a machine-to-machine transaction is one access pattern;
a human-initiated UI workflow is another — and both reach the same Application Service. This
matters for conformance: conformance is asserted about the *service the component provides*,
not about any one channel through which it is invoked.

### Conformance at the Application Component level

Conformance is a statement about a **system**, expressed in terms of the actors it claims to
realise and the options it supports:

> **Conformance** is the assertion that a given **Application Component** correctly realises
> the **Application Services** associated with a named actor role — as **initiator**, as
> **responder**, or both.

It follows that:

1. **The unit of conformance is the Application Component** (the system realising the actor),
   not the Application Interaction.
2. **Conformance is role-directional.** A system may conform as the *responder* without
   conforming as the *initiator*, and vice versa, because these are distinct services.
3. **Testing exercises one side of an interaction at a time.** The component under test plays
   one actor role; a **simulator** — itself an Application Component realising the *opposite*
   actor — plays the other side. The test verifies that the system-under-test's services
   behave as specified.
4. **The support qualifier determines what must be tested.** Every *mandatory* service is
   tested; an *optional* service is tested only where the system declares support for it.

## Alignment with IHE profiles

IHE is the principal example of a framework accommodated within this model, and the
correspondence is close enough that the reference architecture may adopt IHE specifications
directly. The consequence is **deferral**: where an interaction corresponds to an IHE
transaction, the architecture names the actor and the transaction and defers to the IHE
specification for the protocol detail, and to IHE conformance tooling for testing that side
of the interaction. The architecture keeps ownership of the *model* — which actors exist,
which services they offer and require, which interactions connect them — while the
*specification* of a transaction may be drawn from IHE or, where no profile exists, supplied
by another standard or specified afresh.

The correspondence also marks a boundary: the model covers interactions that IHE does not —
the human-initiated paths of *Multiple access patterns to a single service*, or exchanges not
yet specified to transaction level — for which there is nothing to defer to, and which the
architecture specifies by other means.

## Planning testing from the architecture

The same decomposition that makes the architecture legible makes the testing work plannable.
Because conformance is declared component by component, against the services of an actor
role, the architecture is in effect a map of what must be tested: each component carries a
defined test scope, and each test exercises one side of an interaction at a time. The
structure also distinguishes the testing an adopter can **reuse** from the testing it must
**build**:

- **Standard components arrive tested.** Where a component realises a standardised actor —
  one governed by an IHE profile, say — the conformance tests already exist: the published
  test plans, simulators, and reference data that accompany the standard. The adopter reuses
  them, deferring testing to the framework just as it defers the specification.
- **Non-standard components must be tested by the adopter.** Where a component, service, or
  interaction is bespoke, or is an interaction not yet specified to transaction level (for
  instance a human-initiated UI workflow), no ready-made tests exist. The architecture still
  bounds the task: it names the services to satisfy, the role being claimed, and the side of
  the interaction to exercise, with a simulator or operator playing the other side.

The effect is that conformance testing can be **planned as part of the architecture work**,
not retrofitted afterwards: walking the components and their services yields, early, a test
plan that separates what comes tested from what must be built, sizes each, and identifies the
simulators, drivers, and test data needed.

This is an instance of a more general property. Because the elements and their relationships
are **structured and machine-readable**, an architecture expressed in this way can be
*assessed*, not merely described. When a country adapts the reference architecture, or adopts
only selected parts of it, the model makes gaps explicit and checkable — for example a
capability with no component realising it, an actor whose required service nothing provides,
or an interaction with no conforming implementation. Completeness and consistency thereby
become properties that can be checked against the model itself, informing decisions about
what to adopt, extend, or build.

## Summary

The stable, conformance-bearing elements are the **Application Service** (capability) and the
**Application Component** (system in an actor role); the **Application Interaction** is the
descriptive connection between them, and where it is a transaction its specification may be
deferred to IHE.

| Architectural concept | ArchiMate 3.2 element | Bound by | IHE counterpart |
|---|---|---|---|
| Actor (abstract role) | Application Component | — | **Actor** |
| System realising an actor | Application Component | **Realisation** (system → actor) | a product claiming an actor (IHE Integration Statement) |
| Service an actor offers (responder) | Application Service | **Realisation** (actor → service); service then **serves** consumers | responder side of a **transaction** |
| Service an actor requires (initiator) | Application Service | **Serving** (service → actor) | initiator side of a **transaction** |
| Support qualifier (mandatory / optional) | **Property** on the serving relationship (or **Constraint**) | — | the **R**/**O** designation in the profile's actor/transaction table |
| Interaction (transaction = one kind) | Application Interaction | **Assignment** (actors → interaction) | **transaction** (machine-to-machine subset) |
| Conformance (per actor role) | assertion over a component's services | — | conformance to an **actor** within a **profile** |
| Simulator | Application Component realising the opposite actor | **Realisation** (simulator → opposite actor) | an IHE-supplied simulator / test tool |

## Figures

*Build-specifications for the figures below are in the companion modeller notes.*

[Figure 3.7.1: A system realising an actor, with its offered and required services — to be
inserted from the ArchiMate model.]

[Figure 3.7.2: Two actors connected by a transaction (Application Interaction), each owning
its side — to be inserted from the ArchiMate model.]

[Figure 3.7.3: Conformance testing view — system under test, simulator, and the UI-driven
test path — to be inserted from the ArchiMate model.]
