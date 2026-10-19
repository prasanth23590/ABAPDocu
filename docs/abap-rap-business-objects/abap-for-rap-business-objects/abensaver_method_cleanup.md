---
title: "cleanup, RAP Saver Method"
source_file: abensaver_method_cleanup.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Saver Class and Methods > RAP Saver Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cleanup, RAP Saver Method

## Syntax

``` abap
Declaration part:

CLASS lsc_bdef DEFINITION INHERITING FROM base_class ... 
     ... 
     METHODS cleanup REDEFINITION. 
     ... 
ENDCLASS.  

Implementation part:

CLASS lsc_bdef IMPLEMENTATION. 
      ... 
      METHOD cleanup. 
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

- It is part of the [RAP late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md).

- It is the final method of the RAP save sequence and responsible for clearing the [RAP transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md).

- It is called after the data has been persisted to the database or a rollback request is triggered with [`ROLLBACK ENTITIES`](abaprollback_entities.md).

- It is the final method of the RAP save sequence, which is called when instances have been successfully saved to the database.

- It does not have any [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) or [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters.

## Hints

- If only read operations are performed in the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md) and a [`COMMIT ENTITIES`](abapcommit_entities.md) statement is specified, only the `cleanup` method is called.

- In [managed](../rap-behavior-definitions/abenbdl_impl_type.md) scenarios, the task of the method is performed by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md). An exception is when the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md) is specified with [unmanaged or additional save](../rap-behavior-definitions/abenbdl_saving.md) and the notation `... and cleanup`. Then, and generally in [unmanaged](../rap-behavior-definitions/abenbdl_impl_type.md) scenarios, the cleanup must be user-implemented.

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [Save Sequence Runtime](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ab7459048c7e4ecda98d0b6f51b01e7b?version=sap_cross_product_abap)

- [Invalid Statements and Operations in Transactional Contexts](../../abap-programming-language/abap-database-access/abapinvalid_stmts_in_tx.md)

## Executable Example

- The example [Example for a RAP Saver Class](abenabp_saver_class_abexa.md) demonstrates this RAP saver method within a RAP saver class using a simple unmanaged RAP BO.

- The examples [Example for a RAP Saver Class (Late Numbering)](abenabp_saver_ln_abexa.md) and [Phases in a RAP transaction](abenrap_luw_abexa.md) demonstrate this RAP saver method within a RAP saver class using a simple unmanaged RAP BO in late numbering scenario.
