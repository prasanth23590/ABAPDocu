---
title: "RAP - Events"
source_file: abenbdl_event_overview.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Events

## Syntax Forms

**[RAP Business Event](abenbdl_event.md)**

``` abap
event EventName [[deep] parameter ParamName];
```

**[RAP Derived Event](abenbdl_managed_event.md)**

``` abap
managed event DerivedEventName on RefEvent parameter ViewEntityName;
```

**[RAP Business Event for Side Effects](abenbdl_event_side_effect.md)**

``` abap
event EventName for side effects;
```

## Description

- RAP supports event-driven architecture. A [RAP business event](../../abap-glossary/abenrap_entity_event_glosry.md) enables asynchronous communication between an event provider and an event consumer. Details are described in the topic [RAP - `event`](abenbdl_event.md).

- A [RAP derived event](../../abap-glossary/abenrap_derived_event_glosry.md) is defined with reference to an existing [RAP business event](../../abap-glossary/abenrap_entity_event_glosry.md). It redefines the [payload](../../abap-glossary/abenpayload_glosry.md) of the existing event. Details are described in the topic [RAP - `managed event`](abenbdl_managed_event.md).

- [RAP business events for side effects](../../abap-glossary/abenrap_side_effct_event_glosry.md) are business events that are defined to be used exclusively for an [event-driven side effect](../../abap-glossary/abenrap_event_sideef_glosry.md).
