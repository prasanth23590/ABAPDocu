---
title: "Analytics.constraints.filter"
source_file: abencds_1043132933_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Analytics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Analytics.constraints.filter

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Analytics.constraints.filter`                                     |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(20)`                                                       |
| **Enums**   | `#UNIQUE_PER_CELL, #UNIQUE_PER_QUERY`                              |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Analytics

Analytics and AnalyticsDetails capture the analytical aspects of a CDS entity. It is relevant if the analytical engine is interpreting the views. Semantically, the “Analytics” annotations can be differentiated between annotations that are relevant for the InfoProvider/CUBE-level and annotations being only relevant for Analytical Queries.

## constraints

No KTD found

## filter

This annotation should be used for elements (dimensions) in **CUBE** views. It ensures that all analytic queries on top of the CUBE view provide a filter for that element.

## Enums

## \#UNIQUE_PER_CELL

\#UNIQUE_PER_CELL: The filter must be unique for each structure element, but different structure elements might have different filter values.

## \#UNIQUE_PER_QUERY

\#UNIQUE_PER_QUERY: The filter must be unique in the query.
