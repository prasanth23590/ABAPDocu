---
title: "ABAP Objects - Inheritance and Events"
source_file: abeninheritance_events.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Inheritance"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Inheritance and Events

Once declared in a superclass, an event is known in all subclasses of the inheritance tree in which it is visible and can be raised in the methods there.

An event handler can be declared with reference to all classes of the inheritance tree in which the event is visible for the event handler. However, it can only handle events raised in classes that are more specific than or equal to the class for which it is declared. If the event is raised in a method of a superclass of the class for which an event handler is declared, it cannot handle it.

The latter is particularly important when raising static events in static methods, since a static method is always executed in the class in which it was declared (see also [Inheritance and Static Components](abeninheritance_statical.md)).

## Hint

In the case of event handlers for events declared in interfaces, the above also applies to the class in which the interface is included.

## Executable Example

[Events in Inheritance](../abap-declarations/abenevent_inheritance_abexa.md)
