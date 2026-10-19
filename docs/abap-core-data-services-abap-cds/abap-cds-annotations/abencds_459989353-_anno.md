---
title: "AnalyticsDetails.query.cellReference.characteristicStructureElement"
source_file: abencds_459989353-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AnalyticsDetails"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AnalyticsDetails.query.cellReference.characteristicStructureElement

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)    |
|-------------|-----------------------------------------------------------------------|
| **Syntax**  | `AnalyticsDetails.query.cellReference.characteristicStructureElement` |
| **Scope**   | `#ELEMENT`                                                            |
| **Type**    | `ElementRef`                                                          |
| **Enums**   | `-`                                                                   |
| **Default** | `-`                                                                   |
| **Text**    | `-`                                                                   |
| **MDE**     | `-`                                                                   |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`         |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AnalyticsDetails

To enable Analytics, there has to be defined CDS views which represent the Analytical Provider and CDS view, which represent analytical queries. Analytical queries must select from an Analytical model. Views which belong to the Analytical Provider can be enabled for data extraction. The analytical queries can be consumed by BI-tools like SAP Analytics Cloud, Analysis for Office and others via the Analytical Engine.

Annotations belonging to domain AnalyticsDetails are all on element or parameter level.

## query

This section defines the additional annotations that we need on the level of analytical queries.

## cellReference

This annotation can only be used for cell elements. It specifies the coordinates which should be overwritten in a two-structure query.

## characteristicStructureElement

The element name of the characteristic structure.
