---
title: "RAP BO precheck"
source_file: abenrap_bo_precheck_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP BO precheck

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

A [RAP BO operation](abenrap_bo_operation_glosry.md) addition that must be implemented by a [RAP handler method](abenabp_handler_method_glosry.md). A precheck is defined for operations in the [behavior definition](abencds_behavior_definition_glosry.md) of a base business object or in the [projection business object](abenrap_projection_bo_glosry.md).

The implementation method is called before a modify request is executed on the [transactional buffer](abentransactional_buffer_glosry.md) to prevent unwanted changes from reaching the transactional buffer.

[***-\>* More about**](../abap-rap-business-objects/rap-behavior-definitions/abenbdl_precheck.md)
