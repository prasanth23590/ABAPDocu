---
title: "UI.badge.secondaryInfo.type"
source_file: abencds_374889579_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > UI"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UI.badge.secondaryInfo.type

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)           |
|-------------|------------------------------------------------------------------------------|
| **Syntax**  | `UI.badge.secondaryInfo.type`                                                |
| **Scope**   | `#ENTITY`                                                                    |
| **Type**    | `String(40)`                                                                 |
| **Enums**   | `#STANDARD, #WITH_INTENT_BASED_NAVIGATION, #WITH_NAVIGATION_PATH, #WITH_URL` |
| **Default** | `#STANDARD`                                                                  |
| **Text**    | `-`                                                                          |
| **MDE**     | `X`                                                                          |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## UI

The focus of OData UI vocabulary developed by SAP is on usage patterns of data in UIs, not on UI patterns. The vocabulary is completely independent of the UI technologies or devices that consume the data.

The usage patterns of data used by the OData UI vocabulary represent certain semantic views on business data. Some of them are very generic, others are based on the concept of an entity, something tangible to end-users. Examples for entities are semantic object instances or business object instances.

Looking at different UI patterns, these data usage patterns reoccur again and again. To generate OData annotations from CDS views, CDS annotations are reused from different domains, for example Consumption, Communication, Semantics, EndUserText. The CDS annotations that are additionally required in a UI domain are listed in the following table.

## badge

No KTD found

## secondaryInfo

### Short Description

The content of UI.badge.secondaryInfo annotations is subordinate to the content of the UI.badge.mainInfo annotations. This annotation represents a property of type UI.DataFieldAbstract restricted to the types *STANDARD*, *WITH_NAVIGATION_PATH*, and *WITH_URL*.

### Use case

The OData annotations DataFieldAbstract are the basis for all DataField types and represent values with optional labels that can trigger navigation to related data, or execute actions on data.

## type

### Short Description

Annotations belonging to UI.headerInfo.title represent a property of type UI.DataFieldAbstract restricted to the types *STANDARD*, *WITH_NAVIGATION_PATH*, *WITH_URL*, and *WITH_INTENT_BASED_NAVIGATION*. `@UI.headerInfo.title` annotations are mandatory and are usually used to represent the title of an item on the header of an item's object page.

The OData annotations DataFieldAbstract are the basis for all DataField types and represent values with optional labels that can trigger navigation to related data, or execute actions on data.

## Enums

## \#STANDARD

## \#WITH_INTENT_BASED_NAVIGATION

## \#WITH_NAVIGATION_PATH

## \#WITH_URL
