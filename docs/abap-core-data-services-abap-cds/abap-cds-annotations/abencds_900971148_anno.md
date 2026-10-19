---
title: "AnalyticsDetails.query.displayHierarchy"
source_file: abencds_900971148_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AnalyticsDetails"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AnalyticsDetails.query.displayHierarchy

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `AnalyticsDetails.query.displayHierarchy`                          |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(20)`                                                       |
| **Enums**   | `#FILTER, #FILTER_ONLY, #OFF, #ON`                                 |
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

## displayHierarchy

This annotation allows you to specify the display hierarchy attribute for the element. It isn't possible for measures. The query result is shown in a hierarchy for the specified element.

## Enums

## \#OFF

No display hierarchy

## \#ON

With display hierarchy. The hierarchy used must be specified by AnalyticsDetails.query.hierarchyBinding. Only if there doesn't exist a hierarchy directory, the binding isn't necessary.

## \#FILTER

The display hierarchy is the same one defined on the filter for this element. In this case, a hierarchy filter needs to be defined on the same element. The hierarchy binding is taken from the filter.

## \#FILTER_ONLY

This is similar to FILTER but display hierarchy can't be changed at runtime. But the display hierarchy can still be deactivated and activated.
