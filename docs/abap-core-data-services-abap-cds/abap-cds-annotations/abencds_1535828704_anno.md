---
title: "AnalyticsDetails.query.ignoreFurtherFilter.forAllElements"
source_file: abencds_1535828704_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AnalyticsDetails"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AnalyticsDetails.query.ignoreFurtherFilter.forAllElements

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `AnalyticsDetails.query.ignoreFurtherFilter.forAllElements`        |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `Boolean`                                                          |
| **Enums**   | `-`                                                                |
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

## ignoreFurtherFilter

The feature "constant selection" of the analytic engine can be modeled by using the annotations AnalyticsDetails.query.ignoreFurtherFilter.forElement, which expects a list of elements, names, and the annotation, and AnalyticsDetails.query.ignoreFurtherFilter.forAllElements, With variant forAllElements, filters for all dimensions are ignored. With variant,forElement, only the filters for the dimension in that list are ignored. For more information about this features see the documentation https://help.sap.com/viewer/0ecf5244825c4742a7b062a89d11c2ac/1709.latest/en-US/4f03364885212f98e10000000a42189d.html?q=constant%20selection

## forAllElements

See above.
