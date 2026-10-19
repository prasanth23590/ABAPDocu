---
title: "AnalyticsDetails.elimination.rule"
source_file: abencds_1795438715-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AnalyticsDetails"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AnalyticsDetails.elimination.rule

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `AnalyticsDetails.elimination.rule`                                |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(20)`                                                       |
| **Enums**   | `#ELIMINATE_IF_ALL, #ELIMINATE_IF_ONE`                             |
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

## rule

## Enums

## \#ELIMINATE_IF_ALL

The volume is eliminated if all pairs are internal (this is the default rule).

## \#ELIMINATE_IF_ONE

The volume is eliminated if at least one pair is internal.
