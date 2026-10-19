---
title: "CL_ABAP_BEHAVIOR_EVENT_HANDLER"
source_file: abencl_abap_behavior_event_handler.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for RAP Business Events"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_BEHAVIOR_EVENT_HANDLER

## Syntax

``` abap
CLASS lhe_event DEFINITION 
  INHERITING FROM CL_ABAP_BEHAVIOR_EVENT_HANDLER   [ABSTRACT] [FINAL]. 
  PRIVATE SECTION. 
 
    event_handler_method_definitions 
    ... 
 
ENDCLASS. 
 
CLASS lhe_event IMPLEMENTATION 
 
    event_handler_method_declarations 
    ... 
 
ENDCLASS.  
```

[`CLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`DEFINITION`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`INHERITING FROM`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`CL_ABAP_BEHAVIOR_EVENT_HANDLER`](abencl_abap_behavior_event_handler.md) · [`ABSTRACT`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`PRIVATE SECTION`](../../abap-programming-language/abap-declarations/abapprivate.md) · [`event_handler_method_definitions`](abenmethod_for_entity_event.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`CLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`IMPLEMENTATION`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`event_handler_method_declarations`](abenmethod_for_entity_event.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md)

## Description

A [local class](../../abap-glossary/abenlocal_class_glosry.md) inheriting from `CL_ABAP_BEHAVIOR_EVENT_HANDLER` can be implemented in the CCIMP include of a [RAP event handler class](../../abap-glossary/abenrap_event_handler_class_glosry.md) to locally consume [RAP business events](../../abap-glossary/abenrap_entity_event_glosry.md). The events are handled by [RAP event handler methods](../../abap-glossary/abenrap_event_handler_meth_glosry.md) that are defined ([`event_handler_method_definitions)`](abenmethod_for_entity_event.md) and implemented ([`event_handler_method_declarations`](abenmethod_for_entity_event.md)) in this local class.

The local class is implicitly both [`ABSTRACT`](../../abap-programming-language/abap-declarations/abapclass_options.md) and [`FINAL`](../../abap-programming-language/abap-declarations/abapclass_options.md), so specifying `ABSTRACT` and `FINAL` is optional.

## Executable Example

The example Local Consumption of RAP Business Events demonstrates the use of a RAP event handler class.
