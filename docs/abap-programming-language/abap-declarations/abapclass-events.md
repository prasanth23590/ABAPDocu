---
title: "CLASS-EVENTS"
source_file: abapclass-events.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Events"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS-EVENTS

## Syntax

``` abap
CLASS-EVENTS evt [EXPORTING parameters].  
```

[`parameters`](abapevents_parameters.md)

### Addition

[`... EXPORTING parameters`](abapclass-events.md#addition)

## Overview

### Description

This statement declares a static event `evt` in a class or interface. The [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the name `evt`. The statement [`RAISE EVENT`](../abap-calling-and-exiting-program-units/abapraise_event.md) can be used to raise the static event `evt` in all methods of the same class or of a class that implements the interface, as well as in the methods of subclasses if it is visible here.

### Hint

Event handlers that are declared for a [static event inherited from a superclass](../abap-abap-objects/abeninheritance_statical.md) can only respond to this event if it is raised by a method of the subclass or one of its subclasses. If the event is raised in a static method of a superclass, it is not handled, even if the method is called in a subclass or if the name of the subclass is specified.

## Addition

`... EXPORTING parameters`

### Description

The addition `EXPORTING` defines the parameter interface of the event `evt`. The syntax and meaning of the additions [`parameters`](abapevents_parameters.md) are the same as in the definition of instance events using the statement [`EVENTS`](abapevents.md).

### Hint

Static events do not have an implicit formal parameter `sender`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of static events.

``` abap
CLASS cl_abap_browser DEFINITION 
  ... 
  PUBLIC SECTION. 
    ... 
    CLASS-EVENTS 
      sapevent 
        EXPORTING 
          VALUE(action) TYPE string 
          VALUE(query_table) TYPE cnht_query_table OPTIONAL. 
    CLASS-EVENTS 
      closed. 
    ... 
ENDCLASS.
```

### Executable Example

[Events in Inheritance](abenevent_inheritance_abexa.md)
