---
title: "AnalyticsDetails.query.elementHierarchy.initiallyCollapsed"
source_file: abencds_1595836893_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AnalyticsDetails"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AnalyticsDetails.query.elementHierarchy.initiallyCollapsed

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `AnalyticsDetails.query.elementHierarchy.initiallyCollapsed`       |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `Boolean`                                                          |
| **Enums**   | `-`                                                                |
| **Default** | `true`                                                             |
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

## elementHierarchy

A hierarchical display of structure members can be displayed with this annotation. The hierarchy can be defined within the measure structure and the characteristic structure. This annotation must be used with an element, -.elementHierarchy.inilliallyCollapsed or -.elementHierarchy.parent.

## initiallyCollapsed

This is a Boolean value. If true, the hierarchy node represented by the annotated entry will be initially collapsed (only applicable if the annotated entry has children. The elements of the measure structure and characteristic structure can be displayed in a hierarchical way. With AnalyticsDeltails.query.elementHierarch.parent, an element becomes the child of another element.
