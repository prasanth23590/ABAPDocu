---
title: "RAP - precheck"
source_file: abenbdl_precheck.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - RAP BO Operation, Additions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - precheck

## Syntax

``` abap
... precheck ...  
```

## Description

A method that is called before a modify request is executed on the transactional buffer to prevent unwanted changes from reaching the application buffer.

A precheck can be defined for the following [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md):

- [standard operations](abenbdl_standard_operations.md)

- [operations for associations](abenbdl_association.md)

- [actions](abenbdl_nonstandard.md)

- [RAP hierarchy actions](../../abap-glossary/abenrap_hierarchy_action_glosry.md)

An implementation in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR PRECHECK`](../abap-for-rap-business-objects/abaphandler_meth_precheck.md) in the local [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required.

## Hints

- Cannot be used for internal operations using the keyword [`internal`](abenbdl_internal.md).

- When accessing an operation with the ABAP EML statement [`IN LOCAL MODE`](../abap-for-rap-business-objects/abapin_local_mode.md), the precheck method is not called.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Operation Precheck](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/f6e3880b641649b1b8247486579a1c9b?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows an unmanaged BDEF based on the CDS view entity `DEMO_RAP_UNMANAGED_PRECHECK`. It defines the RAP BO operation addition `precheck` for the standard operation `create`.

``` abap
unmanaged
implementation in class bp_demo_rap_unmanaged_precheck unique;
strict(2);

define behavior for DEMO_RAP_UNMANAGED_PRECHECK
lock master
authorization master ( none )
{
  create(precheck);
  update;
  delete;
  field ( readonly:update ) KeyFieldRoot;
}
```

In the ABAP behavior pool `BP_DEMO_RAP_UNMANAGED_PRECHECK`, the precheck method implements a uniqueness check. It checks that the primary keys for new entity instances are unique. If the primary key values already exist, an entry is written into the `failed` and `reported` structures and the respective entity instance does not reach the application buffer.

Code snippet:

``` abap
METHOD precheck_create. 
  "prep buffer 
  LOOP AT entities ASSIGNING FIELD-SYMBOL(<buffer>). 
    IF line_exists( lcl_buffer=>root_buffer[ key_field 
                    = <buffer>-KeyFieldRoot ] ). 
    ELSE. 
      SELECT SINGLE @abap_true 
       FROM demo_dbtab_root 
       WHERE key_field = @<buffer>-KeyFieldRoot 
       INTO @DATA(exists). 
      IF sy-subrc = 0. 
        SELECT * 
        FROM demo_dbtab_root 
        WHERE key_field = @<buffer>-KeyFieldRoot 
        APPENDING CORRESPONDING FIELDS 
        OF TABLE @lcl_buffer=>root_buffer. 
      ENDIF. 
    ENDIF. 
  ENDLOOP. 
 
  "Uniqueness Check 
  LOOP AT entities ASSIGNING FIELD-SYMBOL(<entity>). 
    "Conditions for adding instances to the transactional buffer: 
    " - %control of key field must not be flagged with 00 
    " - key field must not be initial 
    " - line with the key must not exist (but if the line exists 
    "   and it is marked as deleted, it can be added) 
    "It is assumed that %cid is always unique. 
    IF <entity>-KeyFieldRoot IS INITIAL 
    OR <entity>-%control-KeyFieldRoot = if_abap_behv=>mk-off 
    OR line_exists( lcl_buffer=>root_buffer[ key_field 
    = <entity>-KeyFieldRoot ] ) 
    AND lcl_buffer=>root_buffer[ key_field 
    = <entity>-KeyFieldRoot ]-deleted IS INITIAL. 
      "Fill FAILED/REPORTED response structures. 
      APPEND VALUE #( keyfieldroot = <entity>-KeyFieldRoot 
                      %cid         = <entity>-%cid 
                      %delete      = if_abap_behv=>mk-off 
                      %update      = if_abap_behv=>mk-off 
                      %create      = if_abap_behv=>mk-on 
                      %fail-cause  = if_abap_behv=>cause-unspecific 
                    ) 
                TO failed-demo_rap_unmanaged_precheck. 
      APPEND VALUE #( %msg      = new_message_with_text( 
                   severity  = if_abap_behv_message=>severity-error 
                   text      = 'Create operation failed.' ) 
                   keyfieldroot = <entity>-KeyFieldRoot 
                   %cid      = <entity>-%cid ) 
                   TO reported-demo_rap_unmanaged_precheck. 
    ENDIF. 
  ENDLOOP. 
ENDMETHOD.
```

For the complete implementation in the ABAP behavior pool, see `BP_DEMO_RAP_UNMANAGED_PRECHECKCCIMP`.

The class `CL_DEMO_RAP_UNMANAGED_PRECHECK` accesses the business object using [EML](../../abap-glossary/abeneml_glosry.md) and performs the following steps:

- It inserts data into the database using ABAP SQL [`INSERT`](../../abap-programming-language/abap-database-access/abapinsert_dbtab.md).

- It creates two valid new entity instances with unique keys. They pass the precheck and are written to the database.

- It creates two more new entity instances - one is valid, one has a duplicate key value (value '1' already exists).

- The entity instance with duplicate key is written into the `failed` and `reported` structures. The valid entity instance is committed to the database.
