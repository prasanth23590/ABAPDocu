---
title: "RAP - group"
source_file: abenbdl_grouping.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - group

## Syntax

``` abap
... 
group Group1 implementation in class Class1 unique 
{ 
  // implementation-relevant content 
} 
 
group Group2 implementation in class Class2 unique 
{ 
  //implementation-relevant content 
} 
 
[group Group3 ...] 
...  
```

[`implementation in class Class1 unique`](abenbdl_in_class_unique.md) · [`implementation in class Class2 unique`](abenbdl_in_class_unique.md)

## Description

Grouping divides the implementation-relevant parts of a [business object's](../../abap-glossary/abenrap_bo_glosry.md) business logic into multiple groups for behavior implementation. Each group is assigned to a separate [implementation class](abenbdl_in_class_unique.md). This allows the implementation of a business object to be divided technically into multiple parts. Otherwise, the implementation could be done only by one person at a time, since the [CCIMP include](../../abap-glossary/abenccimp_glosry.md) prevents simultaneous work.

If used, the following implementation-relevant parts of a [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md) must be included in a group (in both a managed and an unmanaged RAP BO):

- [actions](abenbdl_action.md)

- [determinations](abenbdl_determinations.md)

- [validations](abenbdl_validations.md)

- feature control (for [fields](abenbdl_field_char.md) and for [RAP BO operations](abenbdl_actions_fc.md))

- In an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), the following operations must be included in a group:

  - The standard operations `create`, `read`, `update`, and `delete`.

  - [Operations for associations](abenbdl_association.md)

  - `Lock` - the [RAP locking mechanism](abenbdl_locking.md) for the [lock master entity](../../abap-glossary/abenrap_lock_ma_ent_glosry.md) must be assigned to a group.

Not allowed within a group is:

- [Type mapping](abenbdl_type_mapping.md) (no implementation required)

Optionally inside or outside of a group:

- In a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md), `create`, `update`, and `delete` and operations for associations can be specified either inside or outside of a group.

- [Field additions](abenbdl_field_char.md) that do not require an implementation.

Further rules:

- When grouping is used, an implementation class on entity level is not allowed.

  Example: this is not allowed `define behavior for MyEntity alias MyAlias implementation in class ClassName unique`

- An implementation class in the [RAP behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md) that applies to the complete BO with all subnodes is allowed.

  Example: this is allowed: `managed implementation in class ClassName unique`

- Different groups can be implemented in the same implementation class.

- The group names `Group1`, `Group2`, ... must not conflict with actions, determinations, or validations of the same name.

- For [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md), the group names are irrelevant and therefore, group names can be changed retrospectively.

- Associations can only be assigned as a whole to a group and therefore, [read-by-association](../../abap-glossary/abenrap_rba_operation_glosry.md) and [create-by-association](../../abap-glossary/abenrap_cba_operation_glosry.md) must be implemented in the same class.

## Availability

- [Managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [Using Groups in Large Development Projects](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/590871b5608546d0ba251d8b7af58c0c?version=sap_cross_product_abap).
