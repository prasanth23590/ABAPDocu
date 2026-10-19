---
title: "Aggregation.referenceElement"
source_file: abencds_1237865219-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Aggregation"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Aggregation.referenceElement

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Aggregation.referenceElement[ ]`                                  |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `ElementRef`                                                       |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Aggregation

## referenceElement

This annotation references the element that is used for distinct counts.

In Query scenarios this element can only be used in combination with the annotation @Aggregation.Default: \#COUNT_DISCTINCT.

*Analytical Engine*

This annotation references the element that is used for the exception. In views of dataCategory: \#CUBE or \#DIMENSION you can use exactly one element. In analytic queries (Analytics.query: true) you can use up to five elements. The elements in the list cannot be measures.

**Evaluation Runtime**

- SADL/ Query Runtime Framework / Orchestration Framework

- Analytical Engine

## Value

Array of elementRef

You can specify a reference characteristic
