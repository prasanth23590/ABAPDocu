---
title: "save_modified, RAP Saver Method"
source_file: abaprap_saver_meth_save_modified.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Saver Class and Methods > RAP Saver Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# save_modified, RAP Saver Method

## Syntax

``` abap
Declaration part:

CLASS lsc_bdef DEFINITION INHERITING FROM base_class ... 
     ... 
     METHODS save_modified REDEFINITION. 
     ... 
ENDCLASS.  

Implementation part:

CLASS lsc_bdef IMPLEMENTATION. 
      ... 
      METHOD save_modified. 
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

- It is only available for managed scenarios that include an additional or unmanaged save implementation. In this case, the RAP saver method [`save`](abensaver_method_save.md) cannot be used. See the BDEF prerequisites in [RAP - `SavingOptions`](../rap-behavior-definitions/abenbdl_saving.md).

- It is responsible for saving the current state of the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md), i.e. all [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) (including instances from cross-BO relationships) from within the current [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md), to the database. However, the method is only called if each of the previous RAP saver methods has been processed successfully without any failures.

- It has the following implicit, predefined [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - `create`: Includes information on instances that have been created within the current RAP transaction. It is of type [`TYPE REQUEST FOR CHANGE`](abaptype_request_for.md).

  - `update`: Includes information on instances that have been updated within the current RAP transaction. It is of type [`TYPE REQUEST FOR CHANGE`](abaptype_request_for.md).

  - `delete`: Includes information on instances that have been deleted within the current RAP transaction. It is of type [`TYPE REQUEST FOR DELETE`](abaptype_request_for.md).

- It has the following implicit, predefined [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters when using `CL_ABAP_BEHAVIOR_SAVER` as base class `base_class` from which the [RAP saver class](../../abap-glossary/abenabp_saver_class_glosry.md) inherits:

  - [`reported`](abaptype_response_for.md): [RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md) that is of type [`TYPE RESPONSE FOR REPORTED LATE`](abaptype_response_for.md).

## Hints

- After persisting data to the database, it is recommended that the transactional buffer is cleared (using the RAP saver method [`cleanup`](abensaver_method_cleanup.md) if it is available and can be user-implemented) because the same ABAP session might be used for more than one RAP transaction and any remaining changes in the transactional buffer could lead to inconsistencies.

- The method is part of the [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Save Sequence Runtime](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ab7459048c7e4ecda98d0b6f51b01e7b?version=sap_cross_product_abap).

## Executable Example

- The example [ABAP EML - `TYPE REQUEST FOR` in a Managed RAP BO with Additional Save](abenrap_additional_save_abexa.md) demonstrates the `save_modified` method in the context of a simple managed RAP BO whose BDEF is specified with `with additional save`.

- The example [ABAP EML - `TYPE REQUEST FOR` in a Managed RAP BO with Unmanaged Save](abenrap_managed_unm_save_abexa.md) demonstrates the `save_modified` method in the context of a simple managed RAP BO whose BDEF is specified with `with unmanaged save`.
