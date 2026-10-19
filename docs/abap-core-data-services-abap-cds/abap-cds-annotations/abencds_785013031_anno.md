---
title: "AnalyticsDetails.elimination.pair.dimension2"
source_file: abencds_785013031_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AnalyticsDetails"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AnalyticsDetails.elimination.pair.dimension2

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `AnalyticsDetails.elimination.pair[ ].dimension2`                  |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(30)`                                                       |
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

## elimination

Eliminate Internal Business Volume with This Feature

This functionality enables the elimination of internal business volume. Here is an illustrative example to clarify its meaning: Consider a company with multiple subsidiaries, each further divided into additional subsidiaries, forming a hierarchical structure. Inter-subsidiary product sales are recorded as external sales for each subsidiary. However, if both subsidiaries are descendants of a parent subsidiary, these sales are considered internal sales at the parent level.

To implement this, use the annotation in cube views (Analytics.dataCategory: \#CUBE) or in analytical queries (define a transient view entity using an analytical query provider contract).

Prerequisites

A defined company hierarchy with subsidiaries.

Active inter-subsidiary sales processes.

Procedure

To eliminate internal business volume in cube views, apply the Analytics.dataCategory: \#CUBE annotation.

For analytical queries, define a transient view entity and use an analytical query provider contract.

Result Internal sales between subsidiaries of the same parent are excluded from the overall sales volume, providing a more accurate representation of external sales performance.

## pair

Elimination Check Pairs: This list specifies the pairs (dimension1 and dimension2) that are evaluated for elimination. Both dimensions must have a foreign key association with the same target data view. When the annotation is applied at the cube level, both dimensions must be elements of the cube. When the annotation is used within an analytical query, both dimensions must be components of the source cube view.

## dimension2

Followed with the literal value of dimension2 name.
