---
title: "Analytics.settings.zeroValues.handling"
source_file: abencds_2016857059-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Analytics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Analytics.settings.zeroValues.handling

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Analytics.settings.zeroValues.handling`                           |
| **Scope**   | `#ENTITY`, `#TABLE_FUNCTION`, `#VIEW`                              |
| **Type**    | `String(20)`                                                       |
| **Enums**   | `#HIDE, #HIDE_IF_ALL, #SHOW`                                       |
| **Default** | `#SHOW`                                                            |
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

## handling

This is only interpreted in the context of an analytical query and defines how zero values should be treated in the result set.

## Enums

## \#SHOW

\#SHOW: You can specify that zeros are to be displayed (i.e., no zero suppression takes place). The default is \#SHOW.

## \#HIDE

\#HIDE: If you want to suppress zeros, there are two options available: \#HIDE and \#HIDE_IF_ALL . For queries that have characteristics in the rows and key figures in the columns (or the other way around, with key figures in the rows and characteristics in the columns), the effect of the settings is identical. The two settings only differ in how they affect queries that have characteristics in the rows and columns (cross-classified table). If you use zero suppression with the \#HIDE value, the system checks whether there are zero values in the results area. If there are zero values in the results area, the corresponding row or column is hidden.

## \#HIDE_IF_ALL

\#HIDE_IF_ALL: For queries that have characteristics in the rows and key figures in the columns (or the other way around, with key figures in the rows and characteristics in the columns), the effect of the value is identical to \#HIDE. If your query has characteristics in the rows and columns however (cross-classified table), and you use zero suppression with the \#HIDE_IF_ALL value, the system hides all rows or columns that contain zero values.

Note: If a detail row is not equal to zero (in a hierarchy for example), all superordinate rows are displayed, even if they contain zeros. As a result, the system ensures that the business context of the query is retained for the end user, even if the value \#HIDE_IF_ALL is set.
