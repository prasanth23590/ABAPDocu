---
title: "SET HANDLER"
source_file: abapset_handler.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Call Event Handler"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SET HANDLER

## Syntax Forms

**[Register Instance Event Handlers](abapset_handler_instance.md)**

``` abap
1. SET HANDLER handler1 handler2 ... FOR oref|{ALL INSTANCES} 
                                    [ACTIVATION act].
```

**[Register Static Event Handlers](abapset_handler_static.md)**

``` abap
2. SET HANDLER handler1 handler2 ... [ACTIVATION act].
```

## Description

This statement registers or deregisters the [event handlers](../../abap-glossary/abenevent_handler_glosry.md) `handler` for the corresponding [instance events](../../abap-glossary/abeninstance_event_glosry.md) or [static events](../../abap-glossary/abenstatic_event_glosry.md).

## System Fields

| **`sy-subrc`** | **Meaning**                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------------------|
| 0              | All specified handlers could be registered or deregistered.                                                          |
| 4              | At least one of the specified handlers could not be registered, as it is already registered for the same event.      |
| 8              | At least one of the specified handlers could not be deregistered, as it is not registered for the event in question. |

## Hints

- The statement `SET HANDLER` internally manages different system tables that relate the event raisers and event handlers to each other in single registrations, mass registrations, and registrations of static events. Each registration represents one line in one of the system tables assigned to the trigger. A handler can only occur once in a particular system table but can appear in multiple system tables, that is, it can be registered for different events. When an event is raised using `RAISE EVENT`, the system evaluates the corresponding system tables and calls the event handlers registered there.

- The order of the calls of registered event handlers is not defined and can change at program runtime. To get a fixed order of different method calls, these can be called in one event handler.

- When an instance method is registered, a reference to the corresponding object is added in the relevant table and then deleted again when deregistering. With respect to the [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md), such a reference has the same effect as a reference in a reference variable. Objects registered as handlers are therefore not deleted as long as they are registered, that is, they are not deregistered using the addition `ACTIVATION`. If a triggering instance is deleted by the Garbage Collector, the corresponding system table is also deleted and, as a result, its registrations are removed.

- If the statement `SET HANDLER` registers the current handler again for the current event that has just been handled, it is not defined whether the registration is ignored by the current event handler. This can produce endless recursions and should be avoided.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Registration of event handlers for two instance events and a static event. In the first statement `SET HANDLER`, a static event handler `h1` and an instance method `h2`, are registered for the instance events `e1` and `e2` of the object referenced by the reference variable `trigger`. In the second statement `SET HANDLER`, an instance method `h3` is registered for the static event `ce1` of the class `c1`.

``` abap
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    EVENTS e1. 
    CLASS-EVENTS ce1. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
  PUBLIC SECTION. 
    EVENTS e2. 
ENDCLASS. 
 
CLASS c3 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS  h1 FOR EVENT e1 OF c1. 
    METHODS: h2 FOR EVENT e2 OF c2, 
      h3 FOR EVENT ce1 OF c1. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
... 
 
CLASS c3 IMPLEMENTATION. 
  METHOD h1. 
    ... 
  ENDMETHOD. 
  METHOD h2. 
    ... 
  ENDMETHOD. 
  METHOD h3. 
    ... 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    DATA: trigger TYPE REF TO c2, 
          handler TYPE REF TO c3. 
 
    SET HANDLER: c3=>h1 handler->h2 FOR trigger, 
                 handler->h3. 
  ENDMETHOD. 
ENDCLASS.
```
