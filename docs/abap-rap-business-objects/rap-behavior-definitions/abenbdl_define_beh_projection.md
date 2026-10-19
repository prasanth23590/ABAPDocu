---
title: "RAP - EntityBehaviorDefinition, Projection BDEF"
source_file: abenbdl_define_beh_projection.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - EntityBehaviorDefinition, Projection BDEF

## Syntax

``` abap
define behavior for ProjectedEntity [alias AliasName] [ external ExternalName] 
{[implementation in class ClassName [unique]]} 
EntityBehaviorCharacteristics 
{ 
  EntityBehaviorBody 
} 
 
[behavior for ChildEntity1][, behavior for ChildEntity2][, ... 
]  
```

[`external`](abenbdl_external.md) · [`implementation in class ClassName [unique]`](abenbdl_in_class_unique.md) · [`EntityBehaviorCharacteristics`](abenbdl_character_projection.md) · [`EntityBehaviorBody`](abenbdl_body_projection.md)

## Description

Defines the behavior for a [RAP projection business object](../../abap-glossary/abenrap_projection_bo_glosry.md) in the [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md). A [RAP projection behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) can project a subset or all of the nodes of its underlying [base BO](../../abap-glossary/abenrap_projected_bo_glosry.md). The [root entity](../../abap-glossary/abenroot_entity_glosry.md) `ProjectedEntity` must be a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md).

Syntax additions and components:

- An alias name can be specified using the keyword `alias`. This name can be clearer than the entity name itself, since it does not need to be uniquely global in [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md). The alias name is visible in the method syntax of the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) of the business object and in the [derived types](../abap-for-rap-business-objects/abenrpm_derived_types.md). The length of an alias name `AliasName` is restricted to 30 characters.

- The optional addition [`external`](abenbdl_external.md) can be used to provide an alias name for external usage. This external name is exposed in the OData metadata, but it is not known by ABAP. It can be much longer than the alias name.

- An [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md), defined using [`implementation in class ClassName unique`](abenbdl_in_class_unique.md), can be specified for each entity that defines [new actions or functions](abenbdl_nonstandard_projection.md) and thus requires an implementation. It can be specified either in the [BDEF projection header](abenbdl_bdef_projection_header.md) or as part of the projection behavior definition.

- [Entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md) [`EntityBehaviorCharacteristics`](abenbdl_character.md) define general properties for each entity.

- The [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md) [`EntityBehaviorBody`](abenbdl_body.md) can expose a subset of the transactional behavior or the base BDEF, for example, standard operations or field properties. It is also possible to define new [actions](abenbdl_nonstandard_projection.md), [functions](abenbdl_function_projection.md), or [field properties](abenbdl_field_projection.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a projection BDEF. The projected BO is `DEMO_SALES_CDS_BUPA_2`. It exposes the standard operations and associations of the underlying BO.

``` abap
projection;
strict(2);
foreign entity demo_cds_validation;
define behavior for DEMO_RAP_PROJECTION_1 alias Parent
{
  use create;
  use update;
  use delete;

  use association _BuPa { create; }
}

define behavior for DEMO_RAP_PROJECTION_1_CHILD alias Child
{
  use update;
  use delete;

  use association _Address;
}
```
