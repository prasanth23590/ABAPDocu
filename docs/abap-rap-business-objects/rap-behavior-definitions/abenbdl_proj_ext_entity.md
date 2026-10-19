---
title: "RAP - Projection Extension Entity"
source_file: abenbdl_proj_ext_entity.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - BDEF Projection Extension > RAP - extension for projection"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Projection Extension Entity

## Syntax

``` abap
... define behavior for ProjectionEntity ...  
```

[`... define behavior for ProjectionEntity ... `](abenbdl_projection_bo.md)

## Prerequisites

- As a prerequisite, the underlying [RAP projection behavior definition](../../abap-glossary/abencds_proj_bdef_glosry.md) must explicitly allow BDEF extensions as described in the topic [RAP - Extensibility Enabling for Projection BDEFs](abenbdl_ext_enabling_projection.md).

- The extension node must be added to the RAP data model via [RAP data model extension](../../abap-glossary/abenrap_data_model_ext_glosry.md).

## Description

A [projection extension entity](../../abap-glossary/abenrap_proj_ext_entity_glosry.md) defines the behavior for an extension node in a [BDEF projection extension](../../abap-glossary/abenrap_projec_bdef_ext_glosry.md) using the statement `define behavior for`.

The projection behavior for this extension node is defined in a similar way as for projection BDEFs. However, there are some restrictions.

Supported in a BDEF projection extension:

- Field attributes `readonly`, `readonly:update`, `suppress`.

- Reuse of RAP BO standard operations, actions, functions, and associations.

- Extend an existing RAP type mapping.

No behavior requiring implementation must be added. As a consequence, the following is not supported:

- No ABAP behavior pool must be specified, The statement `implementation in class unique` is forbidden.

- No authorization control must be specified. The keyword `authorization` in the entity behavior characteristics is forbidden.

- New actions and functions must not be specified in the entity behavior body.

- A [RAP foreign entity](../../abap-glossary/abenrap_foreign_entity_glosry.md) must not be specified.

- Adding a new [RAP authorization context for disable](../../abap-glossary/abencds_auth_context_glosry.md) is not possible. Extending a [full authorization context](../../abap-glossary/abencds_own_ac_glosry.md) is not supported either.

- Adding a [RAP type mapping](../../abap-glossary/abenrap_type_mapping_glosry.md) is not supported. However, extending an existing RAP type mapping with extension fields is supported.

- Enabling BDEF privileged mode `with privileged mode` is not supported.
