---
title: "RAP - EntityBehaviorBody, Projection BDEF"
source_file: abenbdl_body_projection.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Projection Behavior Definitions > RAP - EntityBehaviorDefinition, Projection BDEF"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - EntityBehaviorBody, Projection BDEF

## Syntax

``` abap
 
... {[FieldCharacteristics]; 
     [FieldAugmentation]; 
     [use]; 
     [action]; 
     [function]; 
     [TypeMapping];} 
...  
```

[`FieldCharacteristics`](abenbdl_field_projection.md) · [`FieldAugmentation`](abenbdl_field_augment.md) · [`use`](abenbdl_use_projection.md) · [`action`](abenbdl_nonstandard_projection.md) · [`function`](abenbdl_nonstandard_projection.md) · [`TypeMapping`](abenbdl_type_mapping.md)

## Description

In the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md) of a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md), elements of the projected BDEF can be reused and new elements can be added.

- [`FieldCharacteristics`](abenbdl_field_projection.md): A projection BDEF automatically and implicitly inherits all the field characteristics of its underlying projected BO. If no field characteristic is specified for a certain field in the [base BDEF](../../abap-glossary/abenrap_base_bdef_glosry.md), a field characteristic for the field in question can be specified in the projection BDEF.

- [`FieldAugmentation`](abenbdl_field_augment.md): [RAP BO augmentation](../../abap-glossary/abenrap_bo_augmentation_glosry.md) for read-only fields in a CDS projection behavior definition.

- [`use`](abenbdl_use_projection.md): [Reuse](abenbdl_use_projection.md) of [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md). All operations (standard operations, operations for associations, actions, [functions](../../abap-glossary/abenrap_function_glosry.md), and draft actions) that are to be reused from the base BO must be explicitly specified using the keyword `use`. For details about reuse, see the topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

- [Actions](abenbdl_nonstandard_projection.md) can be defined. An implementation in an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required.

- [Functions](abenbdl_function_projection.md) can be defined. An implementation in an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required.

- [`TypeMapping`](abenbdl_type_mapping.md): A [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) can be used to map [BDEF derived types](../../abap-glossary/abenrap_derived_type_glosry.md) from the current data model to other data types that do not match the BDEF derived component pattern. This works for projection BDEFs in the same way as for managed and unmanaged BDEFs. For more information, see the topic [RAP - `TypeMapping`](abenbdl_type_mapping.md).
