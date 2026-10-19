---
title: "AnalyticsDetails.exceptionAggregationSteps.exceptionAggregationBehavior"
source_file: abencds_1873151419_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AnalyticsDetails"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AnalyticsDetails.exceptionAggregationSteps.exceptionAggregationBehavior

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)                    |
|-------------|---------------------------------------------------------------------------------------|
| **Syntax**  | `AnalyticsDetails.exceptionAggregationSteps[ ].exceptionAggregationBehavior`          |
| **Scope**   | `#ELEMENT`                                                                            |
| **Type**    | `String(14)`                                                                          |
| **Enums**   | `#AVG, #COUNT, #COUNT_DISTINCT, #FIRST, #LAST, #MAX, #MEDIAN, #MIN, #NHA, #STD, #SUM` |
| **Default** | `-`                                                                                   |
| **Text**    | `-`                                                                                   |
| **MDE**     | `-`                                                                                   |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                         |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AnalyticsDetails

To enable Analytics, there has to be defined CDS views which represent the Analytical Provider and CDS view, which represent analytical queries. Analytical queries must select from an Analytical model. Views which belong to the Analytical Provider can be enabled for data extraction. The analytical queries can be consumed by BI-tools like SAP Analytics Cloud, Analysis for Office and others via the Analytical Engine.

Annotations belonging to domain AnalyticsDetails are all on element or parameter level.

## exceptionAggregationSteps

Usually the Default Aggregation determines how measures are aggregated in analytics. But in some cases, for a special element of the entity (dimension of a cube) different aggregation behavior is needed. For example, measure “Inventory” can be summed up for the different plants and other dimensions but not for time. For time dimension, the last or average value might be relevant.

Exception aggregation is optional and used to define different (to the standard Default Aggregation) aggregation behavior for specified elements. In general there might be multiple elements in which a measure has to be aggregated differently. So a list of ExceptionAggregationSteps can be assigned.

## exceptionAggregationBehavior

This annotation defines the aggregation behavior.
