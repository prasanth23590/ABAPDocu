---
title: "cleanup_finalize, RAP Saver Method"
source_file: abapsaver_class_cleanup_finalize.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Saver Class and Methods > RAP Saver Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cleanup_finalize, RAP Saver Method

## Syntax

``` abap
Declaration part:

CLASS lsc_bdef DEFINITION INHERITING FROM base_class ... 
     ... 
     METHODS cleanup_finalize REDEFINITION. 
     ... 
ENDCLASS.  

Implementation part:

CLASS lsc_bdef IMPLEMENTATION. 
      ... 
      METHOD cleanup_finalize. 
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

- Its use is optional.

- It is part of the [RAP early save phase](../../abap-glossary/abenearly_rap_save_phase_glosry.md).

- It does not have any [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) or [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters.

- It clears the [RAP transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md). You can also undo changes if other RAP BOs are involved and there are dependencies on other RAP BOs in the early save phase. In [unmanaged](../rap-behavior-definitions/abenbdl_impl_type.md) scenarios, the cleanup must be user-implemented.

- It is only called if issues occur in the [`finalize`](abensaver_finalize.md) or [`check_before_save`](abensaver_check_before_save.md) methods within the current [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md). After calling the `cleanup_finalize` method, the [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md) is not processed. Instead, you return to the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Save Sequence Runtime](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ab7459048c7e4ecda98d0b6f51b01e7b?version=sap_cross_product_abap)

## Executable Example

- The example [Example for a RAP Saver Class](abenabp_saver_class_abexa.md) demonstrates this RAP saver method within a RAP saver class using a simple unmanaged RAP BO.

- The example [Example for a RAP Saver Class (Late Numbering)](abenabp_saver_ln_abexa.md) demonstrates this RAP saver method within a RAP saver class using a simple unmanaged RAP BO in late numbering scenario.
