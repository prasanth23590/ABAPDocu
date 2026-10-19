---
title: "RAISE EVENT"
source_file: abapraise_event.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Call Event Handler"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAISE EVENT

## Syntax

``` abap
RAISE EVENT evt [EXPORTING p1 = a1 p2 = a2 ...].  
```

### Addition

[`... EXPORTING p1 = a1 p2 = a2 ...`](abapraise_event.md#addition)

## Overview

### Description

This statement can only be used in methods. It raises the event `evt`. `evt` is the name to be specified directly for an event that must be declared with the statement [`EVENTS`](../abap-declarations/abapevents.md) or [`CLASS-EVENTS`](../abap-declarations/abapclass-events.md) directly in the same class, in a superclass, or in an implemented interface.

After the event is raised, all [event handlers](../../abap-glossary/abenevent_handler_glosry.md) that were registered for this event with the statement [`SET HANDLER`](abapset_handler.md) are executed. The order of execution is undefined and can change during program execution. After the event handlers have been executed, the method continues after `RAISE EVENT`.

## Addition

`... EXPORTING p1 = a1 p2 = a2 ...`

### Description

If the addition `EXPORTING` is used, actual parameters `a1 a2 ...` can be assigned to all optional formal parameters `p1 p2...` of the event `evt` and must be assigned to all non-optional formal parameters. The values of the actual parameters are passed to those event handlers whose definition lists the according formal parameters after the addition `IMPORTING` of the statements [`[CLASS-]`](../abap-declarations/abapclass-events.md)[`EVENTS`](../abap-declarations/abapevents.md).

`a1`, `a2`, ... are [general expression positions](../../abap-glossary/abengeneral_expr_position_glosry.md), which means that, alongside data objects, expressions can also be passed as actual parameters. [Special rules](../abap-declarations/abentyping_arith_expr.md) apply in this case.

### Hints

- To avoid endless recursion, a maximum of 1023 further events can be raised using `RAISE EVENT` in event handling.

- If the formal parameter `sender` is defined for an event handler, this is automatically supplied with the reference to the raising object when instance events are raised. It cannot be specified explicitly after `EXPORTING`.

- If there is an exception in an event handler, event handling is canceled. For a class-based exception, the control is then returned to the trigger. See [Class-Based Exceptions in Event Handlers](../abap-program-flow-logic/abenexceptions_events.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Raising of the instance event `e1`. An actual parameter must be assigned to the non-optional formal parameter `p1`.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    EVENTS e1 EXPORTING value(p1) TYPE string 
                        value(p2) TYPE i OPTIONAL. 
    METHODS m1. 
ENDCLASS. 
 
... 
 
CLASS c1 IMPLEMENTATION. 
  METHOD m1. 
    ... 
    RAISE EVENT e1 EXPORTING p1 = '...'. 
    ... 
  ENDMETHOD. 
ENDCLASS.
```
