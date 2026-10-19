---
title: "ABAP Objects - Events"
source_file: abenevents.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Events

Events are declared using the following statements:

- [`EVENTS`](abapevents.md)

- [`CLASS-EVENTS`](abapclass-events.md)

These statements are only possible in the declaration part of classes and interfaces.

The declaration of an event of a class has the effect that the methods of the class raise the event and hence trigger the execution of the [event handlers](../../abap-glossary/abenevent_handler_glosry.md). In the declaration, output parameters can be defined for an event for which actual parameters are then passed to the event handlers when the event is raised.

The statement `EVENTS` declares instance events. Instance events are bound to objects. They can only be raised in instance methods of the same class.

The statement `CLASS-EVENTS` declares static events. Static events are not bound to objects. They can be raised in all methods of the same class.
