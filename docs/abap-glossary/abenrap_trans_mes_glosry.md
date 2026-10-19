---
title: "RAP transition message"
source_file: abenrap_trans_mes_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP transition message

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

A message in the [`reported`](../abap-rap-business-objects/abap-for-rap-business-objects/abapeml_response.md) [RAP response parameter](abenrap_response_param_glosry.md) that is semantically related to the current ABAP EML `MODIFY` request and independent of the state of the [entity instance](abenrap_bo_entity_inst_glosry.md). Unlike [RAP state messages](abenrap_state_mes_glosry.md), transition messages are [RAP messages](abenrap_message_glosry.md) that do not have a state area assigned ([`%state_area`](../abap-rap-business-objects/abap-for-rap-business-objects/abapderived_types_state_area.md)) and are not persisted with the state. Therefore, these messages cannot be accessed at a later point in time.

There are [instance transition messages](abeninstance_rap_trans_mes_glosry.md) and [static transition messages](abenstatic_rap_trans_mes_glosry.md).
