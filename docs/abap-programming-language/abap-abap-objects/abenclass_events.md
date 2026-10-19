---
title: "ABAP Objects - Class Events"
source_file: abenclass_events.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Classes > ABAP Objects - Components of Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Class Events

In ABAP Objects, [events](abenevents_overview.md) are declared as components of classes. There is a distinction between instance events and static events. Triggers and handlers can be objects and classes, depending on whether they are instance or static events, or event handlers.

## Instance Events

Instance events are declared using the statement [`EVENTS`](../abap-declarations/abapevents.md). They can only be raised in instance methods.

## Static Events

Static events are declared using the statement [`CLASS-EVENTS`](../abap-declarations/abapclass-events.md). All methods (instance methods and [static methods](../../abap-glossary/abenstatic_method_glosry.md)) can raise static events. Static events, however, are the only events that can be raised in static methods.
