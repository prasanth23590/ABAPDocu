---
title: "adjust_numbers, RAP Saver Method"
source_file: abensaver_adjust_numbers.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Saver Class and Methods > RAP Saver Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# adjust_numbers, RAP Saver Method

## Syntax

``` abap
Declaration part:

CLASS lsc_bdef DEFINITION INHERITING FROM base_class ... 
     ... 
     METHODS adjust_numbers REDEFINITION. 
     ... 
ENDCLASS.  

Implementation part:

CLASS lsc_bdef IMPLEMENTATION. 
      ... 
      METHOD adjust_numbers. 
      ... 
      ENDMETHOD 
      ... 
ENDCLASS.  
```

[`CLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`DEFINITION`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`INHERITING FROM`](../../abap-programming-language/abap-declarations/abapclass_options.md) · [`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`REDEFINITION`](../../abap-programming-language/abap-declarations/abapmethods_redefinition.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_definition.md) · [`CLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`IMPLEMENTATION`](../../abap-programming-language/abap-declarations/abapclass_implementation.md) · [`METHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDMETHOD`](../../abap-programming-language/abap-program-structure/abapmethod.md) · [`ENDCLASS`](../../abap-programming-language/abap-declarations/abapclass_implementation.md)

## Description

[RAP saver method](../../abap-glossary/abenabp_saver_method_glosry.md) that is declared as part of a [RAP saver class](../../abap-glossary/abenabp_saver_class_glosry.md) `lsc_bdef` in the [CCIMP include](../../abap-glossary/abenccimp_glosry.md) of an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). The predefined saver method must be redefined.

`base_class` stands for the base class from which the RAP saver class inherits, for example, `CL_ABAP_BEHAVIOR_SAVER`.

The following points are relevant for this RAP saver method:

- Its use is mandatory.

- It is only available in [`late numbering`](../rap-behavior-definitions/abenbdl_late_numbering.md) scenarios.

- It is part of the [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md).

- It has the following implicit, predefined [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters when using `CL_ABAP_BEHAVIOR_SAVER` as base class `base_class` from which the [RAP saver class](../../abap-glossary/abenabp_saver_class_glosry.md) inherits:

  - [`mapped`](abaptype_response_for.md): [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md) that is of type [`TYPE RESPONSE FOR MAPPED LATE`](abaptype_response_for.md).

  - [`reported`](abaptype_response_for.md): [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md) that is of type [`TYPE RESPONSE FOR REPORTED LATE`](abaptype_response_for.md).

- It is responsible for converting and mapping preliminary keys and identifiers (e. g. [`%pid`](abapderived_types_pid.md) with which [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) are identified during the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md)) to the final key values of [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md).

- The [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md) `mapped` must be filled in the method implementation by mapping the preliminary keys and identifiers to the final key values. It must be ensured that the key values are unique.

## Hints

- The method is part of the [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Save Sequence Runtime](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ab7459048c7e4ecda98d0b6f51b01e7b?version=sap_cross_product_abap).

## Executable Example

The example [Example for a RAP Saver Class (Late Numbering Scenario)](abenabp_saver_ln_abexa.md) demonstrates this RAP saver method within a RAP saver class using a simple unmanaged RAP BO in late numbering scenario.
