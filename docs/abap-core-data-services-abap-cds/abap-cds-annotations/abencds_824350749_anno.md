---
title: "UI.facet.type"
source_file: abencds_824350749_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > UI"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UI.facet.type

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)                                                                                                                                                                                                                                                                             |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Syntax**  | `UI.facet[ ].type`                                                                                                                                                                                                                                                                                                                             |
| **Scope**   | `#ELEMENT`                                                                                                                                                                                                                                                                                                                                     |
| **Type**    | `String(40)`                                                                                                                                                                                                                                                                                                                                   |
| **Enums**   | `#ADDRESS_REFERENCE, #BADGE_REFERENCE, #CHART_REFERENCE, #COLLECTION, #CONTACT_REFERENCE, #DATAPOINT_REFERENCE, #FIELDGROUP_REFERENCE, #HEADERINFO_REFERENCE, #IDENTIFICATION_REFERENCE, #LINEITEM_REFERENCE, #NOTE_REFERENCE, #PRESENTATIONVARIANT_REFERENCE, #SELECTIONPRESENTATIONVARIANT_REFERENCE, #STATUSINFO_REFERENCE, #URL_REFERENCE` |
| **Default** | `-`                                                                                                                                                                                                                                                                                                                                            |
| **Text**    | `-`                                                                                                                                                                                                                                                                                                                                            |
| **MDE**     | `X`                                                                                                                                                                                                                                                                                                                                            |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                                                                                                                                                                                                                                                                                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## UI

The focus of OData UI vocabulary developed by SAP is on usage patterns of data in UIs, not on UI patterns. The vocabulary is completely independent of the UI technologies or devices that consume the data.

The usage patterns of data used by the OData UI vocabulary represent certain semantic views on business data. Some of them are very generic, others are based on the concept of an entity, something tangible to end-users. Examples for entities are semantic object instances or business object instances.

Looking at different UI patterns, these data usage patterns reoccur again and again. To generate OData annotations from CDS views, CDS annotations are reused from different domains, for example Consumption, Communication, Semantics, EndUserText. The CDS annotations that are additionally required in a UI domain are listed in the following table.

## facet

No KTD found

## type

### Short Description

This annotation specifies what hierarchy type is used

different values determine which CDS elements are required or available.

## Enums

## \#COLLECTION

## \#ADDRESS_REFERENCE

## \#BADGE_REFERENCE

## \#CHART_REFERENCE

## \#CONTACT_REFERENCE

## \#DATAPOINT_REFERENCE

## \#FIELDGROUP_REFERENCE

## \#HEADERINFO_REFERENCE

## \#IDENTIFICATION_REFERENCE

## \#SELECTIONPRESENTATIONVARIANT_REFERENCE

## \#PRESENTATIONVARIANT_REFERENCE

## \#LINEITEM_REFERENCE

## \#NOTE_REFERENCE

## \#STATUSINFO_REFERENCE

## \#URL_REFERENCE
