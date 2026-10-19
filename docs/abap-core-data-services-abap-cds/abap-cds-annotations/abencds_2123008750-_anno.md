---
title: "Event.context.attribute"
source_file: abencds_2123008750-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Event"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Event.context.attribute

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Event.context.attribute`                                          |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(20)`                                                       |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Event

No KTD found

## context

No KTD found

## attribute

## Short Description

Use this annotation in an abstract entity to define which fields are exposed in the cloud event envelope. Furthermore, it can be used to filter the events on a channel. The attribute name must follow these naming guidelines:

- It must have an *xsap* prefix.

- It must not exceed 20 characters in length.

- It should only include lowercase letters (a-z) or numbers (0-9).

## Excluded Annotations

You can use this annotation in combination with the following annotations for the same field:

- `@Semantics.amount.currencyCode`

- `@Semantics.quantity.unitofmeasure`
