---
title: "save, RAP Saver Method"
source_file: abensaver_method_save.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Saver Class and Methods > RAP Saver Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# save, RAP Saver Method

## Syntax

``` abap
Declaration part:

CLASS lsc_bdef DEFINITION INHERITING FROM base_class ... 
     ... 
     METHODS save REDEFINITION. 
     ... 
ENDCLASS.  

Implementation part:

CLASS lsc_bdef IMPLEMENTATION. 
      ... 
      METHOD save. 
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

- It is available in [unmanaged RAP BO providers](../../abap-glossary/abenunmanaged_rap_bo_prov_glosry.md).

- It has the following implicit, predefined [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter when using `CL_ABAP_BEHAVIOR_SAVER` as base class `base_class` from which the [RAP saver class](../../abap-glossary/abenabp_saver_class_glosry.md) inherits:

  - [`reported`](abaptype_response_for.md): [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md) that is of type [`TYPE RESPONSE FOR REPORTED LATE`](abaptype_response_for.md).

- It is responsible for saving the current state of the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md), i. e. all [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) (including instances from cross-BO relationships) from within the current [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md), to the database. However, the method is only called if each of the previous RAP saver methods has been processed successfully without any failures.

## Hints

- After persisting data to the database, it is recommended that the transactional buffer is cleared (using the RAP saver method [`cleanup`](abensaver_method_cleanup.md) if it is available and can be user-implemented) because the same ABAP session might be used for more than one RAP transaction and any remaining changes in the transactional buffer could lead to inconsistencies.

- The method is part of the [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Save Sequence Runtime](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ab7459048c7e4ecda98d0b6f51b01e7b?version=sap_cross_product_abap).

## Executable Example

- The example [Example for a RAP Saver Class](abenabp_saver_class_abexa.md) demonstrates this RAP saver method within a RAP saver class using a simple unmanaged RAP BO.

- The example [Example for a RAP Saver Class (Late Numbering)](abenabp_saver_ln_abexa.md) demonstrates this RAP saver method within a RAP saver class using a simple unmanaged RAP BO in late numbering scenario which also includes the `adjust_numbers` saver method.
