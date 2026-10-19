---
title: "RAP - Extensibility Enabling for Projection BDEF Extensions"
source_file: abenbdl_ext_enabl_ext_proj.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - BDEF Extension, Extensibility Enabling > RAP - Extensibility Enabling for BDEF Extensions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Extensibility Enabling for Projection BDEF Extensions

## Syntax

``` abap
extension for projection 
extensible; 
[...] 
extend behavior for EntityName 
  [...] 
{ 
  [...] 
  [mapping for PartnerType corresponding extensible] 
   ... 
} 
 
define behavior for ExtNode 
  extensible 
  [...] 
{ 
  [...] 
  [mapping for PartnerType corresponding extensible] 
  ... 
} 
[...] 
...  
```

[`extension for projection`](abenbdl_extension_for_projection.md) · [`extensible`](abenbdl_extensible.md) · [`extend behavior for EntityName`](abenbdl_extend_beh_proj.md) · [`mapping for PartnerType corresponding extensible`](abenbdl_type_mapping.md) · [`define behavior for ExtNode`](abenbdl_proj_ext_entity.md) · [`extensible`](abenbdl_extensible.md) · [`mapping for PartnerType corresponding extensible`](abenbdl_type_mapping.md)

## Description

To extend a [BDEF projection extension](../../abap-glossary/abenrap_projec_bdef_ext_glosry.md), the keyword `extensible` can be specified in the following places:

- `extensible` in the BDEF extension header:

  Prerequisite for extensibility. If it is not specified, extensions are not allowed. If specified, at least one component of the RAP BO extension must be declared as extensible. Allows the following components to be added to a [RAP projection behavior definition](../../abap-glossary/abencds_proj_bdef_glosry.md) via a BDEF projection extension:

  - Defining behavior for an extension node on the projection layer by means of a [RAP projection extension entity](../../abap-glossary/abenrap_proj_ext_entity_glosry.md).

- `extensible` in the body of an [entity behavior extension](../../abap-glossary/abenrap_behavior_extension_glosry.md):

  - [`mapping for PartnerType corresponding extensible`](abenbdl_type_mapping.md): a [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) can be extended with extension fields. `extensible` can only be used in combination with `corresponding`, so that components with the same name are automatically mapped to each other.

    **Note:** It is not required that the underlying [projected BDEF](../../abap-glossary/abenrap_projected_bo_glosry.md) is declared as `extensible`. A BDEF projection can be extensible independently of the projected RAP BO.

- `extensible` in the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md) of an [extension entity behavior definition](../../abap-glossary/abenrap_ext_entity_behavior_glosry.md) (extension node):

  Mandatory for each individual extension node that allows extensions. Allows the following behavior extensions to be added via a BDEF extension:

  - [RAP field characteristics](../../abap-glossary/abenrap_field_char_glosry.md) can be added to extension fields.

  - Reuse of actions, functions, and associations from the base RAP BO of type `managed` or `unmanaged`.

- `extensible` can be specified in different places in the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md) of an extension node:

  - [`mapping for PartnerType corresponding extensible`](abenbdl_type_mapping.md): a [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) defined in the extended RAP business object can be extended with extension fields. `extensible` can only be used in combination with `corresponding`, so that components with the same name are automatically mapped to each other.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The BDEF extension `DEMO_RAP_EXT_LAYER_C_X` extends the projection BDEF `DEMO_RAP_EXT_LAYER_C`. It is declared as `extensible` and therefore allows for extension layering.

``` abap
extension for projection;
extensible;
extend behavior for DEMO_RAP_EXT_LAYER_C
{
use association _child {create; with draft;}
}

define behavior for DEMO_RAP_EXT_LAYER_C_CH
extensible
{
use association _to_parent {with draft;}
}
```

The BDEF extension `DEMO_RAP_C_X_X` extends the BDEF extension `DEMO_RAP_EXT_LAYER_C_X`.

``` abap
extension for projection;

extend behavior for DEMO_RAP_EXT_LAYER_C
{
}
```
