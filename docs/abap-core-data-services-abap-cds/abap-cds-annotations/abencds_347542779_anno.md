---
title: "UI.lineItem.type"
source_file: abencds_347542779_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > UI"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UI.lineItem.type

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)                                                                                                                                                                                                                                                                   |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Syntax**  | `UI.lineItem[ ].type`                                                                                                                                                                                                                                                                                                                |
| **Scope**   | `#ELEMENT`                                                                                                                                                                                                                                                                                                                           |
| **Type**    | `String(40)`                                                                                                                                                                                                                                                                                                                         |
| **Enums**   | `#AS_ADDRESS, #AS_CHART, #AS_CONNECTED_FIELDS, #AS_CONTACT, #AS_DATAPOINT, #AS_FIELDGROUP, #AS_PRESENTATION_VARIANT, #AS_SELECTION_PRESENTATION_VARIANT, #FOR_ACTION, #FOR_ACTION_GROUP, #FOR_INTENT_BASED_NAVIGATION, #STANDARD, #WITH_ACTION, #WITH_ACTION_GROUP, #WITH_INTENT_BASED_NAVIGATION, #WITH_NAVIGATION_PATH, #WITH_URL` |
| **Default** | `#STANDARD`                                                                                                                                                                                                                                                                                                                          |
| **Text**    | `-`                                                                                                                                                                                                                                                                                                                                  |
| **MDE**     | `X`                                                                                                                                                                                                                                                                                                                                  |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                                                                                                                                                                                                                                                                        |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## UI

The focus of OData UI vocabulary developed by SAP is on usage patterns of data in UIs, not on UI patterns. The vocabulary is completely independent of the UI technologies or devices that consume the data.

The usage patterns of data used by the OData UI vocabulary represent certain semantic views on business data. Some of them are very generic, others are based on the concept of an entity, something tangible to end-users. Examples for entities are semantic object instances or business object instances.

Looking at different UI patterns, these data usage patterns reoccur again and again. To generate OData annotations from CDS views, CDS annotations are reused from different domains, for example Consumption, Communication, Semantics, EndUserText. The CDS annotations that are additionally required in a UI domain are listed in the following table.

## lineItem

### Short Description

This annotation contains an ordered collection of DataField that is used to represent data from multiple data instances in table or list.

There can be multiple LineItem annotations for different purposes, distinguished by a qualifier.

### More information

<https://github.com/SAP-samples/abap-platform-fiori-feature-showcase/wiki/Feature-Showcase-App-Guide#actions>

## type

### Short Description

This annotation specifies what hierarchy type is used. Different values determine which CDS-elements are required or available.

## Enums

## \#AS_ADDRESS

## \#AS_CHART

## \#AS_CONNECTED_FIELDS

## \#AS_CONTACT

## \#AS_DATAPOINT

## \#AS_FIELDGROUP

## \#AS_PRESENTATION_VARIANT

## \#AS_SELECTION_PRESENTATION_VARIANT

## \#FOR_ACTION

## \#FOR_ACTION_GROUP

## \#FOR_INTENT_BASED_NAVIGATION

## \#STANDARD

## \#WITH_ACTION

## \#WITH_ACTION_GROUP

## \#WITH_INTENT_BASED_NAVIGATION

## \#WITH_NAVIGATION_PATH

## \#WITH_URL
