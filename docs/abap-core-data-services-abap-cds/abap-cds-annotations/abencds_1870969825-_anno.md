---
title: "Analytics.settings.olapPushdown"
source_file: abencds_1870969825-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Analytics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Analytics.settings.olapPushdown

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Analytics.settings.olapPushdown`                                  |
| **Scope**   | `#ENTITY`, `#TABLE_FUNCTION`, `#VIEW`                              |
| **Type**    | `String(30)`                                                       |
| **Enums**   | `#BASIC, #MAX, #OFF`                                               |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Analytics

Analytics and AnalyticsDetails capture the analytical aspects of a CDS entity. It is relevant if the analytical engine is interpreting the views. Semantically, the “Analytics” annotations can be differentiated between annotations that are relevant for the InfoProvider/CUBE-level and annotations being only relevant for Analytical Queries.

## settings

No KTD found

## olapPushdown

The Analytic Engine can map some OLAP features as an SAP HANA calculation scenario. This means some calculations are not calculated in the ABAP server but rather in HANA, which is faster in most cases. This is what we call "pushdown". Unfortunately, the performance is not improved by the pushdown in all cases. By default, all queries using certain features will be processed with pushdown. With Analytics.settings.olapPushdown: \#OFF set for a cube view, you can switch off the pushdown for all queries of that cube. If the annotation is set on query level, then the setting of the cube is overruled. This means with \#OFF you can switch off the pushdown for a single query. With \#MAX, pushdown is performed even if the pushdown has been switched off in the cube.

## Enums

## \#OFF

The Analytic Engine doesn't use the pushdown mechanism and accesses cube data via SQL (corresponds to TREXOPS = 0).

## \#BASIC

## \#MAX

The Analytic Engine performs the pushdown if the relevant features are used in the query (corresponds to TREXOPS = 9).
