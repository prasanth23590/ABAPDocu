---
title: "SET HANDLER, static_event"
source_file: abapset_handler_static.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Call Event Handler > SET HANDLER"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SET HANDLER, static_event

## Syntax

``` abap
SET HANDLER handler1 handler2 ... [ACTIVATION act].  
```

### Addition

[`... ACTIVATION act`](abapset_handler_static.md#addition)

## Overview

### Description

This statement registers the [event handlers](../../abap-glossary/abenevent_handler_glosry.md) `handler1 handler2 ...` for the associated [static events](../../abap-glossary/abenstatic_event_glosry.md). The addition `ACTIVATION` can be used to deregister event handlers or to perform a dynamic registration.

An event handler is executed if the associated static event is raised using [`RAISE EVENT`](abapraise_event.md). The list `handler1 handler2 ...` has the same form as for [instance events](abapset_handler_instance.md), but can only contain event handlers for static events declared using [`CLASS-EVENTS`.](../abap-declarations/abapclass-events.md)

Events that can be handled by an event handler for static events are defined uniquely by their definition in the statement [`[CLASS-]`](../abap-declarations/abapclass-methods_event_handler.md)[`METHODS`](../abap-declarations/abapmethods_event_handler.md). During registration, the addition `FOR`, which is required to register or deregister instance event handlers that determine the raising instances, cannot be specified. An event handler for static events is registered or deregistered independently of the instance and this applies globally to the current [internal session](../../abap-glossary/abeninternal_session_glosry.md).

## Addition

`... ACTIVATION act`

### Description

The syntax and semantics of the addition `ACTIVATION` are the same as for the statement [`SET HANDLER`](abapset_handler_instance.md) for instance events.

### Hint

As long as the registration of an instance method as an event handler for a static event is not canceled using `ACTIVATION blank`, the associated object cannot be deleted by the [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md). This is because it is still used by the runtime framework.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Registration of a static handler for a static event. After the event has been raised, the handling takes place.

``` abap
CLASS output DEFINITION. 
  PUBLIC SECTION. 
    CLASS-DATA 
      out TYPE REF TO if_demo_output. 
    CLASS-METHODS 
      class_constructor. 
ENDCLASS. 
 
CLASS output IMPLEMENTATION. 
  METHOD class_constructor. 
    out = cl_demo_output=>new( ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    CLASS-EVENTS evt 
      EXPORTING VALUE(p) TYPE string DEFAULT `nop`. 
    CLASS-METHODS meth. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD meth. 
    RAISE EVENT evt EXPORTING p = `Ping!`. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS hdl DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS meth FOR EVENT evt OF cls 
      IMPORTING p. 
ENDCLASS. 
 
CLASS hdl IMPLEMENTATION. 
  METHOD meth. 
    output=>out->write( p 
              )->display( ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    SET HANDLER hdl=>meth ACTIVATION 'X'. 
    cls=>meth( ). 
  ENDMETHOD. 
ENDCLASS.
```
