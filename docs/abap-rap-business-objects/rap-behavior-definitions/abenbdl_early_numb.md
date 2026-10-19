---
title: "RAP - early numbering"
source_file: abenbdl_early_numb.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorCharacteristics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - early numbering

## Syntax

``` abap
 ... 
early numbering 
...  
```

## Description

Defines unmanaged [early numbering](../../abap-glossary/abenrap_early_numbering_glosry.md) for all primary key fields of a [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md). Unmanaged early numbering means:

- The [RAP runtime engine](../../abap-glossary/abenrap_runtime_engine_glosry.md) assigns values to the primary key fields.

- How the value assignment takes place is defined by the application developer in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) (therefore, it is called *unmanaged*). The implementation must be done in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR NUMBERING`](../abap-for-rap-business-objects/abaphandler_meth_numbering.md).

- The key value for an instance is available in the transactional buffer instantly after the [`MODIFY`](../abap-for-rap-business-objects/abapmodify_entity_entities.md) request for `CREATE` (which is why it is called *early* numbering, as opposed to [late numbering](abenbdl_late_numbering.md)).

Unmanaged early numbering is defined in the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md) for each [entity behavior definition](../../abap-glossary/abencds_entity_bdef_glosry.md) separately. That means that some business object entities may use unmanaged early numbering, while others use different methods to fill the primary key fields. The affected key fields must be specified as [`readonly`](abenbdl_field_char.md).

## Availability

- [Managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) and [draft-enabled](../../abap-glossary/abendraft_rap_bo_glosry.md) RAP BOs.

  **Note:** Not available in unmanaged RAP BOs without draft handling.

- In [projection business objects](../../abap-glossary/abenrap_projection_bo_glosry.md) and [RAP BO interfaces](../../abap-glossary/abenrap_bo_interface_glosry.md), early numbering is automatically reused from the [base BDEF](../../abap-glossary/abenrap_base_bdef_glosry.md) and does not need to be explicitly defined.

## Hint

Alternative options for numbering:

- [`numbering:managed`](abenbdl_field_numbering.md)

- [`late numbering`](abenbdl_late_numbering.md)

## More Information

For further conceptual background on early and late numbering, see the development guide for the ABAP RESTful Application Programming Model, section [Numbering](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/d85aec25222145f0b0cbbe8b02db51f0?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF that defines unmanaged early numbering for the root view entity `DEMO_RAP_EARLY_NUMBERING`. The primary key field `KeyField` is defined as `readonly`.

**Note:** This example is intentionally kept short and simple and serves demonstration purposes only.

``` abap
managed implementation in class bp_demo_rap_early_numbering unique;
strict(2);

define behavior for DEMO_RAP_EARLY_NUMBERING alias RootEntity
persistent table demo_dbtab_root
lock master
early numbering
authorization master (global)
{
  create;
  update;
  delete;

  field(readonly) KeyField;

  mapping for demo_dbtab_root
  {
    KeyField = key_field;
    DataField = data_field;
    CharField = char_field;
  }
}
```

The ABAP behavior pool implements the local handler class `earlynumbering_create`. This class assigns ascending integer values as primary keys for each entity instance.

Code snippet:

``` abap
METHOD earlynumbering_create. 
 
  SELECT SINGLE 
  FROM demo_dbtab_root 
  FIELDS MAX( key_field ) 
  INTO @DATA(dobj). 
 
  LOOP AT entities INTO DATA(entity). 
 
    dobj += 1. 
 
    APPEND VALUE #( 
        %cid      = entity-%cid 
        KeyField  = dobj 
      ) TO mapped-rootentity. 
  ENDLOOP. 
ENDMETHOD.
```

You can see the complete source code in the `BP_DEMO_RAP_EARLY_NUMBERING===CCIMP`.

- The ABAP class `CL_DEMO_RAP_MANAGED_EARLY_NUMB` uses [EML](../../abap-glossary/abeneml_glosry.md) to access to [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) and performs the following steps:

  - It creates three entity instances by specifying a value for the field `CharField`.

  - It commits the three new entity instances to the database.

  - Using the ABAP SQL `SELECT` statement, it displays the content of the database table. It can be seen that the primary key field `KEY_FIELD` of each entity instance contains a value, which was generated by means of unmanaged early numbering.
