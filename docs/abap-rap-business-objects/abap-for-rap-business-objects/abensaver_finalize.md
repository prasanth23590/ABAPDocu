---
title: "finalize, RAP Saver Method"
source_file: abensaver_finalize.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Saver Class and Methods > RAP Saver Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# finalize, RAP Saver Method

## Syntax

``` abap
Declaration part:

CLASS lsc_bdef DEFINITION INHERITING FROM base_class ... 
     ... 
     METHODS finalize REDEFINITION. 
     ... 
ENDCLASS.  

Implementation part:

CLASS lsc_bdef IMPLEMENTATION. 
      ... 
      METHOD finalize. 
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

- It is part of the [RAP early save phase](../../abap-glossary/abenearly_rap_save_phase_glosry.md). There, it is the first method to be called.

- It is used to make any final calculations and data modifications involving all [RAP BOs](../../abap-glossary/abenrap_bo_glosry.md) in the current [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md).

- In [managed](../rap-behavior-definitions/abenbdl_impl_type.md) scenarios, [determinations](../rap-behavior-definitions/abenbdl_determinations.md) with `ON SAVE` are called during the `finalize` method call.

- It has the following implicit, predefined [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - [`failed`](abaptype_response_for.md): [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md) that is of type [`TYPE RESPONSE FOR FAILED LATE`](abaptype_response_for.md).

  - [`reported`](abaptype_response_for.md): [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md) that is of type [`TYPE RESPONSE FOR REPORTED LATE`](abaptype_response_for.md).

- If the method returns an error in the `failed` parameter, the save sequence is terminated and the [`cleanup_finalize`](abapsaver_class_cleanup_finalize.md) method is called to discard any changes made to the data in the current RAP transaction and to clean up the transactional buffer. After that, the [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md) is not processed. Instead, you return to the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md).

- If a [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md) includes multiple ABAP EML `MODIFY` requests to multiple related RAP BOs (such as [RAP projection business objects](../../abap-glossary/abenrap_projection_bo_glosry.md) and [RAP BO interfaces](../../abap-glossary/abenrap_bo_interface_glosry.md) in a cross-BO scenario), and a commit is triggered, the `finalize` saver method can be called multiple times. If, while executing the `finalize` method in a BO, an ABAP EML `MODIFY` request is made to another BO for which the finalize method has already been executed, the `finalize` method of that specific BO is called again. Make sure that you avoid a cyclical calling of the `finalize` method.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Save Sequence Runtime](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ab7459048c7e4ecda98d0b6f51b01e7b?version=sap_cross_product_abap).

## Executable Example

- The example [Example for a RAP Saver Class](abenabp_saver_class_abexa.md) demonstrates this RAP saver method within a RAP saver class using a simple unmanaged RAP BO.

- The examples [Example for a RAP Saver Class (Late Numbering)](abenabp_saver_ln_abexa.md) and [Phases in a RAP transaction](abenrap_luw_abexa.md) demonstrate this RAP saver method within a RAP saver class using a simple unmanaged RAP BO in late numbering scenario which also includes the `adjust_numbers` saver method.
