---
title: "SET HANDLER, FOR"
source_file: abapset_handler_instance.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Call Event Handler > SET HANDLER"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SET HANDLER, FOR

## Syntax

``` abap
SET HANDLER handler1 handler2 ... FOR { oref |{ALL INSTANCES} }   
                                  [ACTIVATION act].  
```

### Addition

[1. `... FOR oref`](abapset_handler_instance.md#addition-1)

[2. `... FOR ALL INSTANCES`](abapset_handler_instance.md#addition-2)

[3. `... ACTIVATION act`](abapset_handler_instance.md#addition-3)

## Overview

### Description

This statement registers the [event handlers](../../abap-glossary/abenevent_handler_glosry.md) `handler1 handler2 ...` for the associated [instance events](../../abap-glossary/abeninstance_event_glosry.md) of the objects specified after `FOR`. The addition `ACTIVATION` can be used to deregister event handlers or perform a dynamic registration.

An event handler is executed if the associated instance event is raised using [`RAISE EVENT`](abapraise_event.md) in an object for which it is registered. An event handler `handler` can be specified as follows, where the names have the same meaning as in the [explicit method call](abapcall_method_meth_ident_stat.md):

- `meth`

- `oref->meth`

- `class=>meth`

Methods `meth` can be specified from the same class or from other classes defined as instance event handlers using the addition `FOR EVENT evt OF {class|intf}` of the statements [`[CLASS-]`](../abap-declarations/abapclass-methods_event_handler.md)[`METHODS`](../abap-declarations/abapmethods_event_handler.md). No event handlers for [static events](../../abap-glossary/abenstatic_event_glosry.md) can be specified. At least one name must be specified.

The type `class` or `intf` specified after `FOR EVENT OF` in the definition of an instance event handler specifies the objects whose events it can handle. Single objects or all handleable objects can be specified after the addition `FOR`.

## Addition 1

`... FOR oref`

### Description

This addition registers or deregisters the event handlers of the list `handler1 handler2 ...` for exactly one object. `oref` is an object reference that must point to an object whose events can be handled by the specified event handlers. The class of the object must be `class` or a subclass of `class`, or must implement the interface `intf` directly or through a superclass.

`oref` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Registration of an event handler for an ALV event.

``` abap
CLASS demo DEFINITION. 
  PUBLIC SECTION. 
    METHODS main. 
  PRIVATE SECTION. 
    DATA itab TYPE TABLE OF scarr. 
    METHODS handle_double_click 
            FOR EVENT double_click OF cl_salv_events_table. 
ENDCLASS. 
 
CLASS demo IMPLEMENTATION. 
  METHOD main. 
    DATA alv TYPE REF TO cl_salv_table. 
    ... 
    TRY. 
        cl_salv_table=>factory( 
          IMPORTING r_salv_table = alv 
          CHANGING  t_table      = itab ). 
        SET HANDLER handle_double_click FOR alv->get_event( ). 
      CATCH cx_salv_msg. 
        ... 
    ENDTRY. 
  ENDMETHOD. 
  METHOD handle_double_click. 
     ... 
  ENDMETHOD. 
ENDCLASS.
```

## Addition 2

`... FOR ALL INSTANCES`

### Description

This addition registers or deregisters the event handlers of the list `handler1 handler2 ...` for all objects whose events they can handle. These are all objects whose classes are either `class` or the subclass of `class`, or which implement the interface `intf` directly or through a superclass. Such a registration also applies to all raising instances created after the statement `SET HANDLER`.

### Hint

Registration with `FOR ALL INSTANCES` applies also in particular to temporary instances that can be created when using the instantiation operator [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md).

## Addition 3

`... ACTIVATION act`

### Description

A single-character text-like field `act` can be specified after the addition `ACTIVATION`. If `act` has the value *X* (the default value), the event handlers `handler` are registered. If `act` has the value blank, however, the registration of the event handlers `handler` is canceled. A single registration cannot, however, be deregistered using mass deregistration. Conversely, individual raising objects cannot be excluded from registration after a mass registration.

### Hint

As long as the registration of an instance method as an event handler for an instance event is not canceled using `ACTIVATION ' '` or all raising instances are deleted, the associated object cannot be deleted by the [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md). This is because it is still used by the runtime framework.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Registration of an event handler with `FOR ALL INSTANCES`. The events of all temporary instances created with [`NEW`](../abap-creating-objects-and-values/abenconstructor_expression_new.md) are handled until registration is stopped. The code is taken from class `CL_DEMO_SET_HANDLER_FOR_ALL` and can be executed there.

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
    EVENTS evt 
      EXPORTING VALUE(p) TYPE string DEFAULT `nop`. 
    METHODS meth 
      IMPORTING p TYPE string. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD meth. 
    RAISE EVENT evt EXPORTING p = p. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS hdl DEFINITION. 
  PUBLIC SECTION. 
    METHODS meth FOR EVENT evt OF cls 
      IMPORTING p. 
ENDCLASS. 
 
CLASS hdl IMPLEMENTATION. 
  METHOD meth. 
    output=>out->write( p ). 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(href) = NEW hdl( ). 
    SET HANDLER href->meth FOR ALL INSTANCES. 
 
    NEW cls( )->meth( `Ping 1` ). 
    NEW cls( )->meth( `Ping 2` ). 
    NEW cls( )->meth( `Ping 3` ). 
 
    SET HANDLER href->meth FOR ALL INSTANCES ACTIVATION ' '. 
 
    NEW cls( )->meth( `Ping 4` ). 
    NEW cls( )->meth( `Ping 5` ). 
    NEW cls( )->meth( `Ping 6` ). 
 
    output=>out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
