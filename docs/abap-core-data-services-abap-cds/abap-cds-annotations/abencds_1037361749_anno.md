---
title: "Analytics.settings.maxProcessingEffort"
source_file: abencds_1037361749_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Analytics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Analytics.settings.maxProcessingEffort

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Analytics.settings.maxProcessingEffort`                           |
| **Scope**   | `#ENTITY`, `#TABLE_FUNCTION`, `#VIEW`                              |
| **Type**    | `String(20)`                                                       |
| **Enums**   | `#HIGH, #LOW, #MEDIUM, #UNLIMITED`                                 |
| **Default** | `#HIGH`                                                            |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Analytics

Analytics and AnalyticsDetails capture the analytical aspects of a CDS entity. It is relevant if the analytical engine is interpreting the views. Semantically, the “Analytics” annotations can be differentiated between annotations that are relevant for the InfoProvider/CUBE-level and annotations being only relevant for Analytical Queries.

## settings

No KTD found

## maxProcessingEffort

This annotation will be interpreted by the Analytic Engine for analytical query views (*define transient view entity ... provider contract analytical_query as projection on* or annotation *`@Analytics.query`: true*).

If InfoProviders store large amounts of data, certain queries can retrieve large result sets. The maxProcessingEffort is the maximum effort expected by Analytic Engine for processing the data it retrieves.

When the limit is reached, the Analytic Engine returns an error message, and the user can set filters or remove dimensions from the axis to get smaller result sets.

Without this annotation, by default the maxProcessingEffort = \#HIGH.

## Enums

## \#LOW

\#LOW: Effort limit is 1,000

## \#MEDIUM

\#MEDIUM: Effort limit is 100,000

## \#HIGH

\#HIGH: Effort limit is 1,000,000 (the default value)

## \#UNLIMITED

\#UNLIMITED: There is no limit when reading data, but processing might crash memory overflow error or other similar issues may occur.
