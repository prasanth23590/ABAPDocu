---
title: "RAP - late numbering"
source_file: abenbdl_late_numbering.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorCharacteristics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - late numbering

## Syntax

``` abap
 ... 
late numbering 
...  
```

## Description

Defines [internal](../../abap-glossary/abenrap_int_numbering_glosry.md) [late numbering](../../abap-glossary/abenrap_late_numbering_glosry.md) for all primary key fields of a [business object entity](../../abap-glossary/abenrap_bo_entity_glosry.md). Internal late numbering means:

- The [RAP runtime engine](../../abap-glossary/abenrap_runtime_engine_glosry.md) assigns values to the primary key fields.

- In the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md), the [RAP saver method](../../abap-glossary/abenabp_saver_method_glosry.md) [`adjust_numbers`](../abap-for-rap-business-objects/abensaver_adjust_numbers.md) must be implemented to assign a final primary key value for each entity instance.

- The key value for an instance is assigned just before the instance is saved on the database. Thus, a gapless assignment of unique keys is ensured.

Internal late numbering must be defined in the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md) for each [entity behavior definition](../../abap-glossary/abencds_entity_bdef_glosry.md) separately. If the [parent node](../../abap-glossary/abenparent_node_glosry.md) of an entity defines late numbering, then its direct [child node](../../abap-glossary/abenchild_node_glosry.md) must also define late numbering.

When using `late numbering` for a draft-enabled scenario, it is mandatory that the [RAP draft table](abenbdl_draft_table.md) has an additional key field `DRAFTUUID` of data type `raw(16)`.

## Availability

- [Managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- In a [projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md) and in a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), late numbering is automatically reused from the base BDEF and does not need to be explicitly defined. For details, see the topic [RAP - `EntityBehaviorCharacteristics`, Projection BDEF](abenbdl_character_projection.md).

## Hint

Alternative options for numbering:

- [`early numbering`](abenbdl_early_numb.md)

- [`numbering:managed`](abenbdl_field_numbering.md)

## More Information

For further conceptual background on early and late numbering, see the development guide for the ABAP RESTful Application Programming Model, section [Numbering](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/d85aec25222145f0b0cbbe8b02db51f0?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows an unmanaged BDEF that defines late numbering for the root view entity `DEMO_UNMANAGED_LATE_NUMBERING`.

**Note:** This example does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). It is intentionally kept short and simple and focuses on specific RAP aspects. For example, [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) is not enabled. See more information on the RAP BO contract in the [Development guide for the ABAP RESTful Application Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

``` abap
unmanaged implementation in class bp_demo_unmanaged_late_numberi unique;

define behavior for DEMO_UNMANAGED_LATE_NUMBERING
late numbering
{
  create;
  field (readonly:update) key_field;
}
```

The ABAP behavior pool implements the local handler class `adjust_numbers`. In this class, values are defined for the primary key field `key_field`. The first new entity instance is assigned the value '1' and each new entity instance is assigned the next higher integer.

Code snippet:

``` abap
METHOD adjust_numbers. 
  DATA number TYPE i. 
  number = 1. 
 
 LOOP AT lcl_buffer=>root_buffer ASSIGNING FIELD-SYMBOL(<ls_create>). 
    <ls_create>-key_field = number. 
    number = number + 1. 
    APPEND VALUE #( %pid     = <ls_create>-pid 
                    key_field = number ) 
                    TO mapped-demo_unmanaged_late_numbering. 
  ENDLOOP. 
ENDMETHOD.
```

You can see the complete source code in the `BP_DEMO_UNMANAGED_LATE_NUMBERICCIMP`.

- The ABAP class `CL_DEMO_RAP_UNMANAGED_LATE_NMB` uses [EML](../../abap-glossary/abeneml_glosry.md) to access the [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) and performs the following steps:

  - It creates three entity instances by specifying a value for the field `data_field1_root`.

  - It commits the three new entity instances to the database.

  - Using the ABAP SQL `SELECT` statement, it displays the content of the database table. It can be seen that the primary key field `KEY_FIELD` of each entity instance contains a value, which was generated by means of late numbering.

Result: the values for the primary key field `KEY_FIELD` are generated automatically. ![figure](images_abdoc_late_numb.png)
