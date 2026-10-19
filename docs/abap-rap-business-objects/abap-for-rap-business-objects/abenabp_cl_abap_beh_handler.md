---
title: "CL_ABAP_BEHAVIOR_HANDLER, RAP Handler Class"
source_file: abenabp_cl_abap_beh_handler.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Handler Classes and Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_BEHAVIOR_HANDLER, RAP Handler Class

## Syntax

``` abap
CLASS lhc_bdef DEFINITION 
  INHERITING FROM CL_ABAP_BEHAVIOR_HANDLER   [ABSTRACT] [FINAL]. 
  PRIVATE SECTION. 
 
    handler_method_declarations 
    ... 
 
ENDCLASS. 
 
CLASS lhc_bdef IMPLEMENTATION 
 
  handler_method_implementations 
  ... 
 
ENDCLASS.  
```

[`CLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`DEFINITION`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`INHERITING FROM`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`CL_ABAP_BEHAVIOR_HANDLER`](abenabp_cl_abap_beh_handler.md) · [`ABSTRACT`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`PRIVATE SECTION`](../../abap-programming-language/abap-declarations/abapprivate.md) · [`handler_method_declarations`](abapmethods_for_rap_behv.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`CLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`IMPLEMENTATION`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`handler_method_implementations`](abapmethods_for_rap_behv.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md)

## Description

A handler class can be defined in the [CCIMP include](../../abap-glossary/abenccimp_glosry.md) of an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). It consists of method declarations [`handler_method_declarations`](abapmethods_for_rap_behv.md) and implementations [`handler_method_implementations`](abapmethods_for_rap_behv.md).

A handler class `lhc_bdef` inherits from class `CL_ABAP_BEHAVIOR_HANDLER`. For modularization purposes, one behavior pool can define several handler classes. For example, each entity can have its own handler class, or individual handler classes can be defined to distinguish between reading and changing RAP BO entities.

Handler classes are implicitly [`ABSTRACT`](../../abap-programming-language/abap-declarations/abapclass_options.md) and [`FINAL`](../../abap-programming-language/abap-declarations/abapclass_options.md) since instantiating and calling only happens through the [RAP runtime engine](../../abap-glossary/abenrap_runtime_engine_glosry.md).

## Executable Example

The example [Example for RAP Handler Methods](abenrap_handler_methods_abexa.md) demonstrates RAP handler methods within a RAP handler class using a simple unmanaged RAP BO that is draft-enabled.
