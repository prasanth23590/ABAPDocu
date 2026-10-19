---
title: "RAP - internal"
source_file: abenbdl_internal.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - RAP BO Operation, Additions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - internal

## Syntax

``` abap
... internal ...  
```

## Description

Defines a [RAP BO operation](../../abap-glossary/abenrap_bo_operation_glosry.md) as [internal](../../abap-glossary/abenrap_internal_operation_glosry.md). That means that the operation in question can only be accessed from within the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md), for example from an [action](abenbdl_action.md), a [validation](abenbdl_validations.md), or a [determination](abenbdl_determinations.md). When an external [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) tries to execute an internal RAP BO operation, a [runtime error](../../abap-glossary/abenruntime_error_glosry.md) occurs.

`internal` can be applied to the following operations:

- [standard operations](abenbdl_standard_operations.md)

- [operations for associations](abenbdl_association.md)

- [actions](abenbdl_action.md)

- [functions](abenbdl_function.md)

- [determine actions](abenbdl_determine_action.md)

- [draft actions](abenbdl_draft_action.md)

This feature is provided by the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md). No implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required.

## Hints

- If an operation is marked as `internal`, [feature control](abenbdl_actions_fc.md) is not supported. Feature control is for external access control and is not required for internal operations.

- [`precheck`](abenbdl_precheck.md) is not available for internal operations.

- [`authorization:update`](abenbdl_actions_auth_update.md), [`authorization:global`](abenbdl_actions_auth_global.md), and [`authorization:instance`](abenbdl_actions_auth_instance.md) are not available for internal operations.

- Internal operations cannot be reused with the keyword [`use`](abenbdl_use_projection.md) in a projection BDEF or in an interface BDEF, because they are not visible there.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF that defines the internal action `calculateTotalAmount` and the `on modify` determination `calcTotal`.

``` abap
managed implementation in class bp_demo_rap_internal unique;
strict ( 2 );

define behavior for DEMO_RAP_INTERNAL alias RootEntity
persistent table demo_dbtab_field
lock master
authorization master ( none )
{
  create;
  update;
  delete;

  field ( numbering : managed, readonly ) KeyField;

  internal action calculateTotalAmount;

  determination calcTotal on modify { create; }

  mapping for demo_dbtab_field
    {
      KeyField  = key_field;
      CharField = char_field1;
      Amount    = int_field1;
      Quantity  = int_field2;
      Total     = int_field3;
    }
}
```

The internal action multiplies the value of field `Quantity` with the value of field `Amount` and inserts the result into field `Total` per entity instance. It is executed from the ABAP behavior pool by the `on modify` determination `calcTotal`.

Code snippet: determination that triggers the internal action:

``` abap
METHOD calcTotal. 
 
  MODIFY ENTITIES OF demo_rap_internal IN LOCAL MODE 
      ENTITY RootEntity 
        EXECUTE calculateTotalAmount 
          FROM CORRESPONDING #( keys ) 
          REPORTED DATA(lt_reported). 
 
ENDMETHOD.
```

For the full ABAP behavior pool implementation, see `BP_DEMO_RAP_INTERNAL==========CCIMP`.

The ABAP class `CL_DEMO_RAP_INTERNAL` uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object:

- It creates five new entity instances by specifying values for the fields `Amount` and `Quantity`.

  Code snippet:

``` abap
DELETE FROM demo_dbtab_field. 
    MODIFY ENTITIES OF demo_rap_internal 
       ENTITY RootEntity 
       CREATE FIELDS ( Amount Quantity Total ) WITH VALUE #( 
       ( %cid = '1' Amount = 16  Quantity = 1 ) 
       ( %cid = '2' Amount = 211 Quantity = 2 ) 
       ( %cid = '3' Amount = 3   Quantity = 3 ) 
       ( %cid = '4' Amount = 18  Quantity = 4 ) 
       ( %cid = '5' Amount = 10  Quantity = 5 ) ) 
          MAPPED FINAL(mapped) 
          FAILED  FINAL(failed) 
          REPORTED FINAL(reported). 
    COMMIT ENTITIES.
```

- Using the ABAP SQL `SELECT` statement, the content of the underlying database table is displayed.

Result: for each entity instance, the value of the field `Total` is calculated. ![figure](images_abdoc_internal.png)
