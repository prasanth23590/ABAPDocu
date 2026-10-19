---
title: "RAP - extension for projection"
source_file: abenbdl_extension_for_projection.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - BDEF Projection Extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - extension for projection

## Syntax

``` abap
extension for projection 
[extensible  ;] 
  [define behavior for] 
  [extend behavior for] 
...  
```

[`extensible `](abenbdl_ext_enabl_ext_proj.md) · [`define behavior for`](abenbdl_proj_ext_entity.md) · [`extend behavior for`](abenbdl_extend_beh_proj.md)

## Description

Extends an existing [RAP projection behavior definition](../../abap-glossary/abencds_proj_bdef_glosry.md) using a [BDEF projection extension](../../abap-glossary/abenrap_projec_bdef_ext_glosry.md) in the [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md). A RAP projection behavior definition can have one or more BDEF projection extensions. The number of extensions is not limited.

A BDEF projection extension can have the following components:

- [`extensible`](abenbdl_ext_enabl_ext_proj.md): If specified, [extension layering](../../abap-glossary/abenrap_ext_layering_glosry.md) is allowed. For details, see [RAP - Extensibility Enabling for Projection BDEF Extensions](abenbdl_ext_enabl_ext_proj.md).

- [`define behavior for`](abenbdl_proj_ext_entity.md): Defines a [RAP projection extension entity](../../abap-glossary/abenrap_proj_ext_entity_glosry.md) using the statement [`define behavior for`](abenbdl_proj_ext_entity.md).

- [`extend behavior for`](abenbdl_extend_beh_proj.md): A [RAP entity projection extension](../../abap-glossary/abenrap_entity_proj_ext_glosry.md) extends the behavior of an existing entity of a projection BDEF.

**Note:**: No ABAP behavior pool must be specified. The statement `implementation in class ClassName unique` is forbidden.
