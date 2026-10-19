---
title: "UI.fieldGroup.invocationGrouping"
source_file: abencds_1713184207_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > UI"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UI.fieldGroup.invocationGrouping

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `UI.fieldGroup[ ].invocationGrouping`                              |
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

## fieldGroup

### Short Description

Annotations in this category are an ordered collection of data fields with a label for the group.

### More information

[Data Field for Action](https://github.com/SAP-samples/abap-platform-fiori-feature-showcase/wiki/Feature-Showcase-App-Guide#actions)

[Multi Input Field](https://github.com/SAP-samples/abap-platform-fiori-feature-showcase/wiki/Feature-Showcase-App-Guide#multi-input-field)

## invocationGrouping

### Short Description

This annotation expresses how multiple invocations of the same action are handled.

## Enums

## \#ISOLATED

### Use case

A user selects five items in a list and wants to copy them. One item cannot be copied. This item will not be copied, the other four items are copied.

## \#CHANGE_SET

### Use case

A user selects five items in a list and wants to copy them. One item cannot be copied. None of the selected items are copied.
