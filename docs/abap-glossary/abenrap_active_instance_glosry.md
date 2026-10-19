---
title: "RAP active instance"
source_file: abenrap_active_instance_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP active instance

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

A [RAP BO entity instance](abenrap_bo_entity_inst_glosry.md) in a [draft-enabled RAP business object](abendraft_rap_bo_glosry.md) for which a commit triggers the saving to the [persistent table](abenrap_persistent_table_glosry.md). The [BDEF derived type](abenrap_derived_type_glosry.md) of such an instance has the [draft indicator](abenrap_draft_indicator_glosry.md) set to *false*. An active instance can be produced by a [create operation](abenrap_create_operation_glosry.md) or by the [draft action](abenrap_bo_draft_action_glosry.md) `Activate` in draft scenarios.
