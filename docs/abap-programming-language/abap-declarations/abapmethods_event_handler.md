---
title: "METHODS, FOR EVENT"
source_file: abapmethods_event_handler.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Methods > METHODS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# METHODS, FOR EVENT

## Syntax

``` abap
METHODS meth [ABSTRACT|FINAL] 
            |[DEFAULT IGNORE|FAIL]   
   FOR EVENT evt OF {class|intf}   
   [IMPORTING p1 p2 ... [sender]].  
```

[`ABSTRACT|FINAL`](abapmethods_abstract_final.md) · [`DEFAULT IGNORE|FAIL`](abapmethods_default.md)

### Addition

[`... IMPORTING p1 p2 ... [sender]`](abapmethods_event_handler.md#addition)

## Overview

### Description

This statement declares the instance method `meth` as an [event handler](../../abap-glossary/abenevent_handler_glosry.md) for the event `evt` of the class `class` or interface `intf`. For `class` and `intf`, all classes and interfaces can be specified that are visible in this position and that contain an event `evt` as a component that is visible here.

The visibility section of the event handler cannot be more general than the visibility section of the event because otherwise properties of the method would be defined in a visibility section more restricted than the method itself.

If the event `evt` is an instance event, the event handler `meth` can handle it for all objects whose classes match `class` or that are subclasses of `class` or which implement the interface `intf` directly or by using a superclass. If the event is a [static event](../../abap-glossary/abenstatic_event_glosry.md), the event handler `meth` can handle it for the class `class` and its subclasses or for all classes that implement the interface `intf`.

- Using the additions [`ABSTRACT`](abapmethods_abstract_final.md) and [`FINAL`](abapmethods_abstract_final.md), event handlers can either be made abstract or final just like [general methods](abapmethods_general.md) in classes.

- The addition [`DEFAULT`](abapmethods_default.md) can be used to make event handlers optional, just like [general methods](abapmethods_general.md) in interfaces.

### Hints

- To ensure that an event handler handles a raised event, it must be registered with the statement [`SET HANDLER`](../abap-calling-and-exiting-program-units/abapset_handler.md).

  In event handlers, no class-based exceptions can be declared using `RAISING`. See [Class-Based Exceptions in Event Handlers](../abap-program-flow-logic/abenexceptions_events.md).

- When declaring event handlers for static events, note that these events are generally raised in static methods as well. In such a method, the class in which the method is declared is always the raising class, and not the subclass in which or with whose name the method was called.

- Method declarations using this syntax are not to be confused with method declarations in the context of [RAP business events](../../abap-glossary/abenrap_entity_event_glosry.md): [`METHODS, FOR ENTITY EVENT`](../../abap-rap-business-objects/abap-for-rap-business-objects/abenmethod_for_entity_event.md)

## Addition

`... IMPORTING p1 p2 ... [sender]`

### Description

The addition `IMPORTING` defines the input parameters of the event handler. For `p`, only those names of formal parameters can be specified that are defined as output parameters of the event by using the addition `EXPORTING` of the statement [`EVENTS`](abapevents.md) or [`CLASS-EVENTS`](abapclass-events.md) in the declaration of the event `evt` in the class `class` or in the interface `intf`. The additions `TYPE` or `LIKE` and `OPTIONAL` or `DEFAULT` are not possible. The [typing](../../abap-glossary/abentyping_glosry.md) of the input parameters and whether they are optional, and any replacement parameters, are inherited from the declaration of the event. Not all output parameters of the event need to be specified.

If `evt` is an instance event, a formal parameter called `sender` can be defined as an input parameter of an event handler in addition to the explicitly defined output parameters of the event. The formal parameter `sender` is an implicit output parameter of every instance event. It is completely typed as a reference variable, which itself has the class `class` or the interface `intf` as a static type, as specified in the declaration of the event handler after `EVENT evt OF`. If the event handler is called by an instance event, it is passed a reference to the raising object in `sender`.

### Hint

Each event handler determines the type of its formal parameter `sender`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The class `picture` contains an event handler `handle_double_click` for the instance event `picture_dblclick` of the global class `cl_gui_picture`. The event handler inherits two explicit output parameters of the event and the implicit parameter `sender` as input parameters.

``` abap
CLASS picture DEFINITION. 
  PUBLIC SECTION. 
    METHODS handle_double_click 
            FOR EVENT picture_dblclick OF cl_gui_picture 
            IMPORTING mouse_pos_x mouse_pos_y sender. 
ENDCLASS. 
 
CLASS picture IMPLEMENTATION. 
  METHOD handle_double_click. 
    ... 
  ENDMETHOD. 
ENDCLASS.
```
