---
title: "CLASS, FOR EVENTS OF, RAP Event Handler Class"
source_file: abenclass_for_events.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for RAP Business Events"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS, FOR EVENTS OF, RAP Event Handler Class

## Syntax

``` abap
CLASS cl_event_handler DEFINITION PUBLIC [ABSTRACT] [FINAL] FOR EVENTS OF ent. 
  ... 
ENDCLASS. 
 
CLASS cl_event_handler IMPLEMENTATION 
  ... 
ENDCLASS.  
```

[`CLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`DEFINITION`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`ABSTRACT`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`CLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`IMPLEMENTATION`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md)

## Description

Adding `FOR EVENTS OF` to the definition of a [global class](../../abap-glossary/abenglobal_class_glosry.md) creates a [RAP event handler class](../../abap-glossary/abenrap_event_handler_class_glosry.md).

`ent` specifies the name of a [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md) [interface BDEF](../../abap-glossary/abencds_interface_bdef_glosry.md) that exposes an event. The events that are handled by the class must be defined in the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md).

The global class is implicitly [`ABSTRACT`](../../abap-programming-language/abap-declarations/abapclass_options.md) and [`FINAL`](../../abap-programming-language/abap-declarations/abapclass_options.md). Therefore, `ABSTRACT` and `FINAL` may or may not be specified.

The actual handling of the events is done by [RAP event handler methods](../../abap-glossary/abenrap_event_handler_meth_glosry.md) that are implemented in the [CCIMP include](../../abap-glossary/abenccimp_glosry.md) of the event handler class.

## Executable Example

The example Local Consumption of RAP Business Events demonstrates the use of a RAP event handler class.
