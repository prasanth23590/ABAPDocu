---
title: "AnalyticsDetails.query.temporalJoin.derivationType"
source_file: abencds_1919095871-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AnalyticsDetails"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AnalyticsDetails.query.temporalJoin.derivationType

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `AnalyticsDetails.query.temporalJoin.derivationType`               |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(20)`                                                       |
| **Enums**   | `#FIRST_DAY, #LAST_DAY, #OFFSET`                                   |
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

## temporalJoin

When an annotation is set to a hierarchy association within a query, the hierarchy is joined in a temporal manner. This implies that the fact data is assigned to the corresponding node at the specific time indicated in the fact row. Given that there may be multiple time dimensions within the cube, an annotation is required to reference the pertinent time element. The validity of a leaf or node in the hierarchy is always delineated by a date-based interval. Consequently, a rule is necessary for deriving a date in situations where the time element is not explicitly a date but rather a month, quarter, fiscal period, etc. There are three available rules: 1) use the start date of the period, 2) use the end date of the period, or 3) apply an offset starting from the first day. If the offset exceeds the length of the period, the last day is utilized.

## derivationType

If the time element is not a date, you can specify with this annotation, whether the derived date should be the first date, last date, or a date with special offset of that period.
