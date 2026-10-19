---
title: "RAP - Entity Projection Extension"
source_file: abenbdl_extend_beh_proj.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - BDEF Projection Extension > RAP - extension for projection"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Entity Projection Extension

## Syntax

``` abap
extend behavior for ProjectionEntity 
 { 
   projection_extension_body 
 } 
...  
```

[`projection_extension_body`](abenbdl_proj_ext_body.md)

## Description

An [entity projection extension](../../abap-glossary/abenrap_entity_proj_ext_glosry.md) extends a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md) `ProjectionEntity`. As a prerequisite, extensions must be explicitly enabling as described in topic [RAP - Extensibility Enabling for Projection BDEFs](abenbdl_ext_enabling_projection.md).

**Syntax additions and components:**

- [`projection_extension_body`](abenbdl_proj_ext_body.md): extends the [entity behavior body](../../abap-glossary/abencds_entity_body_glosry.md) of a projection BDEF.
