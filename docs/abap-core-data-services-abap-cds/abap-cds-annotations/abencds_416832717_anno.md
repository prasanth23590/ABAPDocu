---
title: "AnalyticsDetails.query.hierarchySettings.childNodePosition"
source_file: abencds_416832717_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AnalyticsDetails"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AnalyticsDetails.query.hierarchySettings.childNodePosition

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `AnalyticsDetails.query.hierarchySettings.childNodePosition`       |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(10)`                                                       |
| **Enums**   | `#ABOVE, #BELOW`                                                   |
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

## hierarchySettings

Defines some settings of the display hierarchy in the initial layout.

## childNodePosition

Defines whether the nodes should expand to the bottom or to the top.

## Enums

## \#hidePostedNodesValues

A posted node has to components, it represents a node and one of its children is the key of the node itself. With the annotation, the child-part can be hidden.

## \#hideNodeWithOneChild

If this is set, a node is not displayed, if it just has one child. Instead the child will be displayed as child of the parent node of this suppressed node.

## \#childNodePosition

Defines whether the nodes should expand to the bottom or to the top.
