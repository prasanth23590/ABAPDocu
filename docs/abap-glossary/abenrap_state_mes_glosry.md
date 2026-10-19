---
title: "RAP state message"
source_file: abenrap_state_mes_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP state message

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

A [message](abenrap_message_glosry.md) in the [`reported`](../abap-rap-business-objects/abap-for-rap-business-objects/abapeml_response.md) [RAP response parameter](abenrap_response_param_glosry.md) of a [RAP business object](abenrap_bo_glosry.md) that refers to the state of an [entity instance](abenrap_bo_entity_inst_glosry.md). A state message is defined with the parameter [`%state_area`](../abap-rap-business-objects/abap-for-rap-business-objects/abapderived_types_state_area.md), which assigns it to the corresponding state area. A state message is persisted with the instance it refers to in [draft-enabled BOs](abendraft_rap_bo_glosry.md).

RAP state messages are relevant in the following contexts:

- Draft-enabled RAP BOs

- The [`cleanup_finalize`](../abap-rap-business-objects/abap-for-rap-business-objects/abapsaver_class_cleanup_finalize.md) and [`check_before_save`](../abap-rap-business-objects/abap-for-rap-business-objects/abensaver_check_before_save.md) [RAP saver methods](abenabp_saver_method_glosry.md) in [unmanaged RAP BOs](abenunmanaged_rap_bo_glosry.md)

- [Determinations](abenrap_determination_glosry.md) and [validations](abenrap_validation_glosry.md) in [managed RAP BOs](abenmanaged_rap_bo_glosry.md)
