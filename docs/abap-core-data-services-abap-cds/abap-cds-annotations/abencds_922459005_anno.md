---
title: "Analytics.settings.columns.totalsLocation"
source_file: abencds_922459005_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Analytics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Analytics.settings.columns.totalsLocation

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Analytics.settings.columns.totalsLocation`                        |
| **Scope**   | `#ENTITY`, `#TABLE_FUNCTION`, `#VIEW`                              |
| **Type**    | `String(10)`                                                       |
| **Enums**   | `#LEFT, #RIGHT`                                                    |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Analytics

Analytics and AnalyticsDetails capture the analytical aspects of a CDS entity. It is relevant if the analytical engine is interpreting the views. Semantically, the “Analytics” annotations can be differentiated between annotations that are relevant for the InfoProvider/CUBE-level and annotations being only relevant for Analytical Queries.

## settings

No KTD found

## columns

This is only interpreted in the context of an analytical query and must be used in the header of the CDS view.

## totalsLocation

This annotation specifies if the totals are shown to the right or the left of the details.

If nothing is specified, the default is \#RIGHT without display hierarchy and \#LEFT with display hierarchy.
