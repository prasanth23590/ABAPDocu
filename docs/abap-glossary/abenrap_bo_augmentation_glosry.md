---
title: "RAP BO augmentation"
source_file: abenrap_bo_augmentation_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP BO augmentation

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

A [RAP BO operation](abenrap_bo_operation_glosry.md) addition that must be implemented by an [ABP handler method](abenabp_handler_method_glosry.md). Augmentation is defined in the [projection behavior definition](abencds_proj_bdef_glosry.md) for [RAP standard operations](abenrap_standard_operation_glosry.md).

The implementation is called when a [modify request](abenrap_modify_operation_glosry.md) reaches the [business object projection](abenrap_projection_bo_glosry.md) to add data to the request before it is passed to the corresponding handler of the [projected business object](abenrap_projected_bo_glosry.md).

[***-\>* More about**](../abap-rap-business-objects/rap-behavior-definitions/abenbdl_augment_projection.md)
