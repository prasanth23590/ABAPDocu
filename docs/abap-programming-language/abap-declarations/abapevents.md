---
title: "EVENTS"
source_file: abapevents.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Events"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EVENTS

## Syntax

``` abap
EVENTS evt [EXPORTING parameters].  
```

[`parameters`](abapevents_parameters.md)

### Addition

[`... EXPORTING parameters`](abapevents.md#addition)

## Overview

### Description

This statement declares an instance event `evt` in a class or interface. The [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) apply to the name `evt`. The statement [`RAISE EVENT`](../abap-calling-and-exiting-program-units/abapraise_event.md) can be used to raise the instance event `evt` in any instance method of the same class, or of any class that implements the interface, as well as in the instance methods of subclasses if they are visible there.

## Addition

`... EXPORTING parameters`

### Description

The addition `EXPORTING` defines the parameter interface of the event `evt`. An event can only have output parameters [`parameters`](abapevents_parameters.md) that are passed by value.

When an [event handler](../../abap-glossary/abenevent_handler_glosry.md) is declared using the addition `FOR EVENT OF` of the statement [`METHODS`](abapmethods_event_handler.md) or [`CLASS-METHODS`](abapclass-methods_event_handler.md), the output parameters of the event are defined as the input parameters of the event handler. The properties of the input parameters are transferred from the output parameters defined in `EVENTS`.

In addition to the output parameters defined explicitly using `EXPORTING`, each instance event has an implicit output parameter, `sender`. This output parameter has the type reference variable. When the event is raised using `RAISE EVENT`, the reference to the raising object is implicitly assigned to `sender`.

The static type of the input parameter `sender` is defined for every event handler by the object type (class or interface) that is specified after the addition `FOR EVENT OF` of the statement `METHODS` or `CLASS-METHODS`.

### Hint

The dynamic type of the implicit formal parameter `sender` is always the class of the object in which the event is raised.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the interface `window`, three events are declared, each with an explicit non-optional output parameter `status`. The class `dialog_window` implements the interface `window`. The interface `window_handler` contains [event handlers](../../abap-glossary/abenevent_handler_glosry.md), which import both the explicit parameters and the implicit parameter `sender`. The static type of the input parameter `sender` is the class `dialog_window`.

``` abap
INTERFACE window. 
  EVENTS: minimize EXPORTING VALUE(status) TYPE i, 
          maximize EXPORTING VALUE(status) TYPE i, 
          restore  EXPORTING VALUE(status) TYPE i. 
ENDINTERFACE. 
 
CLASS dialog_window DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES window. 
ENDCLASS. 
 
INTERFACE window_handler. 
  METHODS: minimize_window 
             FOR EVENT window~minimize OF dialog_window 
             IMPORTING status sender, 
           maximize_window 
             FOR EVENT window~maximize OF dialog_window 
             IMPORTING status sender, 
           restore 
             FOR EVENT window~restore OF dialog_window 
             IMPORTING status sender. 
ENDINTERFACE.
```

### Executable Example

[Events in Inheritance](abenevent_inheritance_abexa.md)
