---
title: "RAP draft instance"
source_file: abenrap_draft_instance_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP draft instance

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

A [RAP BO entity instance](abenrap_bo_entity_inst_glosry.md) in a [draft-enabled RAP business object](abendraft_rap_bo_glosry.md) for which a commit triggers the saving to the [RAP draft table](abendraft_table_glosry.md). The [BDEF derived type](abenrap_derived_type_glosry.md) of such an instance has the [draft indicator](abenrap_draft_indicator_glosry.md) set to *true*. A draft instance can be produced by a [create operation](abenrap_create_operation_glosry.md) ( [new-draft instances](abenrap_new_draft_inst_glosry.md)) or by the [draft action](abenrap_bo_draft_action_glosry.md) `Edit` ([edit-draft instances](abenrap_edit_draft_inst_glosry.md)) in draft scenarios. There are [exclusive draft](abenrap_exclusive_draft_glosry.md) instances, where only a single user is allowed to edit a draft, and [collaborative draft](abenrap_collaborative_draft_glosry.md) instances, where multiple users can work concurrently on the same draft.
