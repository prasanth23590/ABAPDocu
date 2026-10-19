---
title: "UI.statusInfo.invocationGrouping"
source_file: abencds_2139917933-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > UI"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UI.statusInfo.invocationGrouping

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `UI.statusInfo[ ].invocationGrouping`                              |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(12)`                                                       |
| **Enums**   | `#CHANGE_SET, #ISOLATED`                                           |
| **Default** | `#ISOLATED`                                                        |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## UI

The focus of OData UI vocabulary developed by SAP is on usage patterns of data in UIs, not on UI patterns. The vocabulary is completely independent of the UI technologies or devices that consume the data.

The usage patterns of data used by the OData UI vocabulary represent certain semantic views on business data. Some of them are very generic, others are based on the concept of an entity, something tangible to end-users. Examples for entities are semantic object instances or business object instances.

Looking at different UI patterns, these data usage patterns reoccur again and again. To generate OData annotations from CDS views, CDS annotations are reused from different domains, for example Consumption, Communication, Semantics, EndUserText. The CDS annotations that are additionally required in a UI domain are listed in the following table.

## statusInfo

### Short Description

Contains an ordered collection of abstract DataFields that describes the status of an entity identified by HeaderInfo and Identification.

### Use Case

UI.statusInfo annotations are usually used in the header section of an item's object view floorplan.

### Value

array of

### Evaluation Runtime (Engine)

SADL: Translates CDS annotations into the corresponding OData annotations

## invocationGrouping

### Short Description

This annotation describes how to group multiple invocations of the same action on multiple instances.

## Enums

## \#ISOLATED

### Short Description

If not all items can be copied but the user still wants to copy the majority of them except the one that can't be copied.

## \#CHANGE_SET
