---
title: "RAP - EntityBehaviorDefinition"
source_file: abenbdl_define_beh.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - EntityBehaviorDefinition

## Syntax

``` abap
define behavior for RootEntity [alias AliasName] [ external ExternalName] 
{[implementation in class ClassName [unique]]} 
EntityBehaviorCharacteristics 
{ 
  EntityBehaviorBody 
} 
 
[define behavior for ChildEntity1][, define behavior for ChildEntity2][, ... 
]  
```

[`external`](abenbdl_external.md) · [`implementation in class ClassName [unique]`](abenbdl_in_class_unique.md) · [`EntityBehaviorCharacteristics`](abenbdl_character.md) · [`EntityBehaviorBody`](abenbdl_body.md)

## Description

Defines the behavior for a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) in the [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md). A [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) can consist of one or more [entity behavior definitions](../../abap-glossary/abencds_entity_bdef_glosry.md) that start with `define behavior for`, each one referring to a different [node](../../abap-glossary/abenrap_bo_entity_glosry.md) of the business object. An entity behavior definition for the [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md) `RootEntity` is mandatory, whereas entity behavior definitions for [child entities](../../abap-glossary/abenchild_entity_glosry.md) are optional. If a RAP BO entity does not have a dedicated entity behavior definition, the entity does not have a transactional character. It is then not modifiable within the [ABAP RESTful application programming model](../../abap-glossary/abenarap_glosry.md).

In a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md), the possible root entities `RootEntity` are [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) or [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

In an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), the possible root entities `RootEntity` are [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md), [CDS custom entities](../../abap-glossary/abencds_custom_entity_glosry.md), or [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). **Note:** Custom entities serve as data model basis for [RAP unmanaged queries](../../abap-glossary/abenrap_unmanged_query_glosry.md).

Syntax additions and components:

- An alias name `AliasName` can be specified using the keyword `alias`. This name can be clearer than the entity name itself, since it does not need to be uniquely global in [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md). The alias name is visible in the method syntax of the [behavior pool](../abap-for-rap-business-objects/abenabap_behavior_pools.md) of the business object and in the [derived types](../abap-for-rap-business-objects/abenrpm_derived_types.md). The length of an alias name `AliasName` is restricted to 30 characters.

- The optional addition [`external`](abenbdl_external.md) can be used to provide an alias name `ExternalName` for external usage. This external name is exposed in the OData metadata, but it is not known by ABAP. It can be much longer than the alias name.

- An [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) can be specified for each RAP BO entity using the syntax [`implementation in class ClassName unique`](abenbdl_in_class_unique.md). This class can be used to implement the transactional behavior for the RAP BO entity it refers to.

- [Entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md) [`EntityBehaviorCharacteristics`](abenbdl_character.md) define general properties for a RAP BO entity.

- The [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md) [`EntityBehaviorBody`](abenbdl_body.md) defines the transactional behavior of the RAP BO entity.

## Hints

- If [BDEF strict mode](abenbdl_strict.md) is enabled, no gaps are allowed in the behavior enablement of a [composition tree](../../abap-glossary/abencds_composition_tree_glosry.md). For example, if a composition tree consists of entities 1 (root), 2 (child), and 3 (grandchild), the definition of a behavior for entities 1 and 3 but not for entity 2 is not allowed, as this would be a gap.

- If [BDEF strict mode](abenbdl_strict.md) is enabled, the underlying CDS entities `RootEntity`, `ChildEntity1`, `ChildEntity2` and so on, must not be [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF based on the CDS root view entity `DEMO_RAP_MANAGED_ASSOC_ROOT`. The CDS composition tree consists of the root entity and one child entity. For both entities, an entity behavior definition is defined.

**Note:** This example does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md). It is intentionally kept short and simple and serves demonstration purposes only. See more information on the RAP BO contract in the [Development guide for the ABAP RESTful Application Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/3a402c5cf6a74bc1a1de080b2a7c6978?version=sap_cross_product_abap).

``` abap
managed
implementation in class BP_DEMO_RAP_MANAGED_ASSOC_ROOT unique;
strict ( 2 );
with cross associations;

define behavior for DEMO_RAP_MANAGED_ASSOC_ROOT alias _Root
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  association _child { create; }
  association _ext { create; }
  field ( readonly : update ) KeyFieldRoot;

  mapping for demo_dbtab_root
    {
      KeyFieldRoot  = key_field;
      DataFieldRoot = data_field;
      CharFieldRoot = char_field;
      CharFieldRoot2 = char_field_2;
      DecFieldRoot  = dec_field;
      constant 'Demo' = char_field_3;
    }
}

define behavior for DEMO_RAP_MANAGED_ASSOC_CHILD alias _Child
persistent table demo_dbtab_child
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;

  association _parent { }

  field ( readonly : update ) KeyField, KeyFieldChild;
  mapping for demo_dbtab_child
    {
      KeyField      = key_field;
      KeyFieldChild = key_field_child;
      DataField     = data_field;
      CharField     = char_field;
    }
}
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows an unmanaged BDEF based on the CDS root view entity `DEMO_RAP_UNMANAGED_DRAFT_ROOT`. The CDS composition tree consists of the root entity and one child entity. For both entities, an entity behavior definition is defined.

``` abap
unmanaged implementation in class bp_demo_rap_unmanaged_draft_ro unique;
strict(2);
with draft;


define behavior for DEMO_RAP_UNMANAGED_DRAFT_ROOT alias ParentEntity
draft table demo_dbtab_draft
lock master
total etag Timestamp
etag master LastChangedAt
authorization master ( global, instance )
{
  create;
  update;
  delete;
  field ( readonly:update ) KeyFieldRoot;
  field ( readonly ) Timestamp, LastChangedAt;

  draft action Activate optimized;
  draft action Discard;
  draft action Edit;
  draft action Resume;
  draft determine action Prepare;

  association _child { create; with draft; }
}

define behavior for DEMO_RAP_UNMANAGED_DRAFT_CHILD alias ChildEntity
draft table demo_draft_ch5
(lock, authorization, etag) dependent by _parent
{
  update;
  delete;

  association _parent { with draft; }

  field ( readonly:update ) keyfield, KeyFieldChild;
}
```

The behavior is defined in the `BP_DEMO_RAP_UNMANAGED_DRAFT_ROCCIMP` of the ABAP behavior pool.
