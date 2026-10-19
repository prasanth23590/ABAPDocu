---
title: "ROLLBACK ENTITIES"
source_file: abaprollback_entities.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ROLLBACK ENTITIES

## Syntax

``` abap
ROLLBACK ENTITIES.  
```

## Description

Rolls back all changes of the current [RAP transaction](../../abap-glossary/abenrap_luw_glosry.md). This includes data changes (for example, changes stored in the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) by calling the [`cleanup`](abensaver_method_cleanup.md) method) and [locks](../../abap-glossary/abenlock_glosry.md). In [unmanaged](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) scenarios and in [managed](../rap-behavior-definitions/abenbdl_impl_type.md) scenarios that include an [`unmanaged or additional save`](../rap-behavior-definitions/abenbdl_saving.md), the [RAP BO provider](../../abap-glossary/abenrap_bo_provider_glosry.md) must be implemented to perform the above tasks.

The statement does not provide any output parameters, for example, response or result parameters. `ROLLBACK ENTITIES` cannot be called within the RAP BO implementation.

In case of a natively supported RAP scenario (for example, [OData](../../abap-glossary/abenodata_glosry.md)), the `ROLLBACK ENTITIES` call is performed by RAP. In other cases, for example, manually implemented services or applications, the `ROLLBACK ENTITIES` call must be done explicitly.

## Hints

- ABAP EML statements should not be used in loops. Using them can have a performance impact because it can result in multiple single database accesses. There should be only one ABAP EML statement to read the necessary data, and then the data should be modified with an ABAP EML modify request.

- The rollback request triggers the calling of the [`cleanup`](abensaver_method_cleanup.md) method that clears the transactional buffer.

- The rollback request (implicitly) triggers the calling of [`ROLLBACK WORK`](../../abap-programming-language/abap-database-access/abaprollback.md) if the current RAP transaction includes [RAP modify operations](../../abap-glossary/abenrap_modify_operation_glosry.md).

## More Information

When implementing RAP operations, ensure that you comply with [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). Follow the implementation guidelines in the development guide for the ABAP RESTful Application Programming Model, section [RAP Business Object Contract](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

You can find a selected set of guidelines in [here](abaprap_impl_rules.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code demonstrates the effect of the `ROLLBACK ENTITIES` statements. The instance of the first modify request is saved to the database. The second ABAP EML `MODIFY` statement is followed by a `ROLLBACK ENTITIES` statement that clears the instance data from the transactional buffer. Since there is no data in the transactional buffer to be persisted, the following `COMMIT ENTITIES` statement does not save any data to the database. Consequently, the internal table that is filled by a `SELECT` statement shows the same content for the second internal table as the first internal table.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DELETE FROM demo_tab_root. 
 
MODIFY ENTITY demo_managed_root 
  CREATE FIELDS ( key_field data_field1_root 
                  data_field2_root ) 
  WITH VALUE #( ( %cid = 'cid1' 
                key_field = 1 
                data_field1_root = 'aaa' 
                data_field2_root = 'bbb' ) ). 
 
COMMIT ENTITIES. 
 
IF sy-subrc = 0. 
  SELECT * FROM demo_tab_root 
    INTO TABLE @FINAL(itab1). 
ENDIF. 
 
out->write( itab1 ). 
 
MODIFY ENTITY demo_managed_root 
  CREATE FIELDS ( key_field data_field1_root 
                  data_field2_root ) 
  WITH VALUE #( ( %cid = 'cid2' 
                key_field = 2 
                data_field1_root = 'ccc' 
                data_field2_root = 'ddd' ) ). 
 
ROLLBACK ENTITIES. 
 
COMMIT ENTITIES. 
 
IF sy-subrc = 0. 
  SELECT * FROM demo_tab_root 
    INTO TABLE @FINAL(itab2). 
ENDIF. 
 
out->write( itab2 ). 
 
out->display( ).
```

## Executable Example

The class `CL_DEMO_RAP_EML_ROLLBACK_ENTTS` demonstrates the effect of the `ROLLBACK ENTITIES` statement with a managed [RAP BO](../../abap-glossary/abenrap_bo_glosry.md). Two modify operations are executed, the one including the creation of data sets only, the other creating and deleting data sets. Each modify operation is [committed](abapcommit_entities.md) separately. The database tables are then emptied and the same operations are carried out again. However, the second modify operation includes the `ROLLBACK ENTITIES` statement which rolls back the modifications that have not yet been saved from the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md). Consequently, the output table does not show the changes.
