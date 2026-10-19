---
title: "RAP business event"
source_file: abenrap_entity_event_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP business event

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

A RAP business event is a business event that usually represents a piece of information about the outcome of a [CUD operation](abencud_glosry.md) in the context of a [RAP BO entity](abenrap_bo_entity_glosry.md). For example, the creation of a [RAP BO entity instance](abenrap_bo_entity_inst_glosry.md) raises a RAP business event. Then, an interested party that has subscribed to this event can consume and process it. The information that is passed (i. e. the [payload](abenpayload_glosry.md) of the event) always includes the instance key and, if need be, further information like the action (CUD).

[RAP derived events](abenrap_derived_event_glosry.md) and [RAP business events for side effects](abenrap_side_effct_event_glosry.md) are special types of RAP business events.

[***-\>* More about**](../abap-rap-business-objects/rap-behavior-definitions/abenbdl_event.md)
