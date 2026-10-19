---
title: "Analytics.settings.zeroValues.hideOnAxis"
source_file: abencds_1301366722-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Analytics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Analytics.settings.zeroValues.hideOnAxis

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Analytics.settings.zeroValues.hideOnAxis`                         |
| **Scope**   | `#ENTITY`, `#TABLE_FUNCTION`, `#VIEW`                              |
| **Type**    | `String(20)`                                                       |
| **Enums**   | `#COLUMNS, #ROWS, #ROWS_COLUMNS`                                   |
| **Default** | `#ROWS_COLUMNS`                                                    |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Analytics

Analytics and AnalyticsDetails capture the analytical aspects of a CDS entity. It is relevant if the analytical engine is interpreting the views. Semantically, the “Analytics” annotations can be differentiated between annotations that are relevant for the InfoProvider/CUBE-level and annotations being only relevant for Analytical Queries.

## settings

No KTD found

## zeroValues

No KTD found

## hideOnAxis

You can specify whether rows or columns that contain zeros as values are to be hidden.

## Enums

## \#ROWS

\#ROWS: Only rows that contain zeros as values are to be hidden.

## \#COLUMNS

\#COLUMNS: Only columns that contain zeros as values are to be hidden.

## \#ROWS_COLUMNS

\#ROWS_COLUMNS: Rows and columns that contain zeros as values are to be hidden. The default is \#ROWS_COLUMNS.
