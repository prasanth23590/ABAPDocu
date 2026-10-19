---
title: "AnalyticsDetails.query.collisionHandling.formula"
source_file: abencds_1480232296_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AnalyticsDetails"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AnalyticsDetails.query.collisionHandling.formula

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `AnalyticsDetails.query.collisionHandling.formula`                 |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(20)`                                                       |
| **Enums**   | `#CONCURRENT, #DEFAULT, #THIS`                                     |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AnalyticsDetails

To enable Analytics, there has to be defined CDS views which represent the Analytical Provider and CDS view, which represent analytical queries. Analytical queries must select from an Analytical model. Views which belong to the Analytical Provider can be enabled for data extraction. The analytical queries can be consumed by BI-tools like SAP Analytics Cloud, Analysis for Office and others via the Analytical Engine.

Annotations belonging to domain AnalyticsDetails are all on element or parameter level.

## query

This section defines the additional annotations that we need on the level of analytical queries.

## collisionHandling

If a query has a measure and a characteristic structure, conflicts can occur. For instance, both structures might contain a member with a formula. Then it has to be specified which property should be the taken for the resulting cell: the property from the measure structure member or the property from the characteristic structure member. For instance, if both members are a formula it has to be specified, which formula should be calculated for the resulting cell. If nothing is specified, the property of the measure structure will be taken.

Note: The query.collisionHandling annotation must be used with special elements. query.collisionHandling.decimals, -.formula, -.scaling, or -.semanticObject.

## formula

Determines which formula should be calculated in the resulting cell.

## Enums

## \#formula

Determines which formula should be calculated in the resulting cell.

## \#decimals

Determines which setting for decimals (query.decimals) should be set for the resulting cell. This annotation is only relevant for measures. For other elements it will be ignored.

## \#scaling

Determines which setting for scaling (query.scaling) should be set for the resulting cell.

## \#semanticObject

Determines which semantic object (Consumption.semanticObject) should be assigned to the resulting cell.
