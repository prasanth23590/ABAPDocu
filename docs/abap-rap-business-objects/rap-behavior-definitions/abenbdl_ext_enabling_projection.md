---
title: "RAP - Extensibility Enabling for Projection BDEFs"
source_file: abenbdl_ext_enabling_projection.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - BDEF Extension, Extensibility Enabling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Extensibility Enabling for Projection BDEFs

## Syntax

``` abap
projection 
strict[(version)]; 
extensible; 
define behavior for ProjectedEntity 
  extensible 
  [...] 
{ 
  [...] 
  [mapping for PartnerType corresponding extensible] 
  [...] 
} 
 ...  
```

[`projection`](abenbdl_impl_type.md) · [`strict[(version)]`](abenbdl_strict.md) · [`extensible`](abenbdl_extensible.md) · [`define behavior for ProjectedEntity`](abenbdl_define_beh_projection.md) · [`extensible`](abenbdl_extensible.md) · [`mapping for PartnerType corresponding extensible`](abenbdl_type_mapping.md)

## Prerequisite

To allow [BDEF projection extensions](../../abap-glossary/abenrap_projec_bdef_ext_glosry.md) to a [RAP projection behavior definition](../../abap-glossary/abencds_proj_bdef_glosry.md), [BDEF strict mode](../../abap-glossary/abenrap_strict_mode_glosry.md) must be switched on using the keyword [`strict [(version)]`](abenbdl_strict.md).

## Description

The keyword `extensible` can be specified at different places to allow for extensions:

- `extensible` in the [RAP behavior definition header](../../abap-glossary/abencds_bdef_header_glosry.md)

  Prerequisite for extensibility. If it is not specified, then extensions are not allowed. If specified, at least one RAP BO entity must be declared as extensible in the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md). Allows the following components to be added to a [RAP projection behavior definition](../../abap-glossary/abencds_proj_bdef_glosry.md) via a BDEF projection extension:

  - Defining behavior for an extension node on the projection layer by means of a [RAP projection extension entity](../../abap-glossary/abenrap_proj_ext_entity_glosry.md).

- `extensible` in the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md)

  Mandatory for each individual [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md) that allows extensions. Allows the following behavior extensions to be added via a BDEF projection extension for the RAP BO entity in question:

  - [RAP field characteristics](../../abap-glossary/abenrap_field_char_glosry.md) can be added to extension fields.

  - Reuse of actions, functions, and associations from the base RAP BO of type `managed` or `unmanaged`.

- `extensible` in the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md):

  [`mapping for PartnerType corresponding extensible`](abenbdl_type_mapping.md): a [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) defined in the extended RAP business object can be extended with extension fields. `extensible` can only be used in combination with `corresponding`, so that components with the same name are automatically mapped to each other.

**Note:** It is not required that the underlying [projected BDEF](../../abap-glossary/abenrap_projected_bo_glosry.md) is declared as `extensible`. A BDEF projection can be extensible independently of the projected RAP BO.
