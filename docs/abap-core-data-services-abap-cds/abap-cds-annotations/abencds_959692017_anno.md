---
title: "UI.badge.title.criticalityRepresentation"
source_file: abencds_959692017_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > UI"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UI.badge.title.criticalityRepresentation

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `UI.badge.title.criticalityRepresentation`                         |
| **Scope**   | `#ENTITY`                                                          |
| **Type**    | `String(12)`                                                       |
| **Enums**   | `#WITHOUT_ICON, #WITH_ICON`                                        |
| **Default** | `#WITHOUT_ICON`                                                    |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## UI

The focus of OData UI vocabulary developed by SAP is on usage patterns of data in UIs, not on UI patterns. The vocabulary is completely independent of the UI technologies or devices that consume the data.

The usage patterns of data used by the OData UI vocabulary represent certain semantic views on business data. Some of them are very generic, others are based on the concept of an entity, something tangible to end-users. Examples for entities are semantic object instances or business object instances.

Looking at different UI patterns, these data usage patterns reoccur again and again. To generate OData annotations from CDS views, CDS annotations are reused from different domains, for example Consumption, Communication, Semantics, EndUserText. The CDS annotations that are additionally required in a UI domain are listed in the following table.

## badge

No KTD found

## title

### Short Description

This annotation creates a title for the badge. It is a required DataField restricted to the types, *WITH_NAVIGATION_PATH*, and *WITH_URL*.

## criticalityRepresentation

### Short Description

This annotation defines, whether criticality is represented by an icon or not.

### Use case

You don't want the criticality to be displayed as 'neutral (0)' or 'critical (2)' but instead you want to show it as a an icon for example an arrow pointing up or down.

## Enums

## \#WITHOUT_ICON

### Short Description

This annotation defines, that the criticality is not represented by an icon.

## \#WITH_ICON

### Short Description

This annotation defines, that the criticality is represented by an icon, for example an arrow.
