---
title: "UI.facet.purpose"
source_file: abencds_1670155180_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > UI"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UI.facet.purpose

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)             |
|-------------|--------------------------------------------------------------------------------|
| **Syntax**  | `UI.facet[ ].purpose`                                                          |
| **Scope**   | `#ELEMENT`                                                                     |
| **Type**    | `String(40)`                                                                   |
| **Enums**   | `#FILTER, #HEADER, #OPERATION_PARAMETER, #QUICK_CREATE, #QUICK_VIEW,#STANDARD` |
| **Default** | `#STANDARD`                                                                    |
| **Text**    | `-`                                                                            |
| **MDE**     | `X`                                                                            |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## UI

The focus of OData UI vocabulary developed by SAP is on usage patterns of data in UIs, not on UI patterns. The vocabulary is completely independent of the UI technologies or devices that consume the data.

The usage patterns of data used by the OData UI vocabulary represent certain semantic views on business data. Some of them are very generic, others are based on the concept of an entity, something tangible to end-users. Examples for entities are semantic object instances or business object instances.

Looking at different UI patterns, these data usage patterns reoccur again and again. To generate OData annotations from CDS views, CDS annotations are reused from different domains, for example Consumption, Communication, Semantics, EndUserText. The CDS annotations that are additionally required in a UI domain are listed in the following table.

## facet

No KTD found

## purpose

### Short Description

This annotation cointains the purpose information about the facet.

### Use case

You want to give further information about the purpose of a used facet in order to give more information of said facet to the user.

## Enums

## \#STANDARD

## \#HEADER

## \#QUICK_VIEW

## \#QUICK_CREATE

## \#FILTER

## \#OPERATION_PARAMETER
