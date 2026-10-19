---
title: "RAP - extension_body, Projection Extension"
source_file: abenbdl_proj_ext_body.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - BDEF Projection Extension > RAP - extension for projection > RAP - Entity Projection Extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - extension_body, Projection Extension

## Syntax

``` abap
... 
  [field characteristics]; 
  [use]; 
  [extend mapping for];  
```

## Description

Defines the [behavior extension body](../../abap-glossary/abenrap_behavior_ext_body_glosry.md) to extend an existing [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md) in a [RAP projection behavior definition](../../abap-glossary/abencds_proj_bdef_glosry.md).

**Components**:

- `field characteristics`:

  - Adds [field attributes](../../abap-glossary/abenrap_field_char_glosry.md) to extension fields in a BDEF projection extension.

  - Field attributes can be added only for extension fields. Extension fields are fields which are added via [RAP data model extension](../../abap-glossary/abenrap_data_model_ext_glosry.md).

  - The following field attributes are available in BDEF projection extensions for extension fields: `readonly`, `suppress`, `readonly:update`.

  - These field attributes work as described in topic [Field Characteristics, Projection BDEF](abenbdl_field_projection.md).

    **Note:** The field characteristics `mandatory`, `modify`, and `features:instance` are not available in [BDEF projection extensions](../../abap-glossary/abenrap_projec_bdef_ext_glosry.md).

- `use`:

  - The keyword `use` allows the reuse of [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md).

  - The following operations can be reused: [RAP actions](../../abap-glossary/abenrap_action_glosry.md), [RAP functions](../../abap-glossary/abenrap_function_glosry.md), and [associations](abenbdl_association.md).

    **Limitation:** The [operation augmentation](../../abap-glossary/abenrap_bo_augmentation_glosry.md) is not available in BDEF projection extensions. As a consequence, the following is not supported: `use association _child {create(augment);}`.

  - Only extension operations that were created in the same software component can be reused. Operations from the original base BDEF of type `managed` or `unmanaged` must not be reused.

  - Actions, functions, and associations from the projection layer cannot be reused.

  - Reuse works as described in topic [RAP BDL - use](abenbdl_use_projection.md).

- [`extend mapping for`](abenbdl_type_mapping_ext.md):

  - An existing RAP type mapping can be extended with extension fields using the syntax [`extend mapping for`](abenbdl_type_mapping_ext.md) as described in topic [RAP BDL - `extend mapping`](abenbdl_type_mapping_ext.md).

## Executable Examples

- [BDEF Projection Extension, Node Extension](abenbdl_entity_proj_ext_abexa.md)
