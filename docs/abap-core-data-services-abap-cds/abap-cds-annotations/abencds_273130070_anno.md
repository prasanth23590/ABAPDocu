---
title: "AnalyticsDetails.exceptionAggregationSteps.exceptionAggregationElements"
source_file: abencds_273130070_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AnalyticsDetails"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AnalyticsDetails.exceptionAggregationSteps.exceptionAggregationElements

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)              |
|-------------|---------------------------------------------------------------------------------|
| **Syntax**  | `AnalyticsDetails.exceptionAggregationSteps[ ].exceptionAggregationElements[ ]` |
| **Scope**   | `#ELEMENT`                                                                      |
| **Type**    | `String(30)`                                                                    |
| **Enums**   | `-`                                                                             |
| **Default** | `-`                                                                             |
| **Text**    | `-`                                                                             |
| **MDE**     | `-`                                                                             |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                   |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AnalyticsDetails

To enable Analytics, there has to be defined CDS views which represent the Analytical Provider and CDS view, which represent analytical queries. Analytical queries must select from an Analytical model. Views which belong to the Analytical Provider can be enabled for data extraction. The analytical queries can be consumed by BI-tools like SAP Analytics Cloud, Analysis for Office and others via the Analytical Engine.

Annotations belonging to domain AnalyticsDetails are all on element or parameter level.

## exceptionAggregationSteps

Usually the Default Aggregation determines how measures are aggregated in analytics. But in some cases, for a special element of the entity (dimension of a cube) different aggregation behavior is needed. For example, measure “Inventory” can be summed up for the different plants and other dimensions but not for time. For time dimension, the last or average value might be relevant.

Exception aggregation is optional and used to define different (to the standard Default Aggregation) aggregation behavior for specified elements. In general there might be multiple elements in which a measure has to be aggregated differently. So a list of ExceptionAggregationSteps can be assigned.

## exceptionAggregationElements

The elements which should be aggregated in one step are listed in this annotation. These have to be part of the same entity as the measure element.

For example, in a cube entity there is a measure which should show the number of customers above a certain sales amount. For this, at first the sales has to be aggregated (SUM) on customer level and then “COUNT” has to be performed. This means if the sales for a customer is above the level, then the sales is replaced by 1 otherwise it is set to 0. This number can be summed up again. This measure element has the Default Aggregation “SUM” and the ExcepetionAggregationBehavior “COUNT” with the ReferenceElement customer.

Note that, the logical order in which the aggregation is performed is as follows: At first the standard aggregation is performed. This intermediate result is still grouped by all Elements in the list of ExceptionAggregationSteps. Then the result is aggregated by the exception aggregation in the order of StepNumber.

The first remark holds even if the Default Aggregation is “FORMULA”. This means that the calculation is done when the result is still grouped by the exception aggregation elements. After calculating the formula the result is aggregated according to the list of ExceptionAggregationSteps.

With this the aggregation level on which has to be calculated can be defined precisely.
