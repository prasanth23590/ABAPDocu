---
title: "Analytics.settings.runtimeExtensibility.allowed"
source_file: abencds_1999912159_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Analytics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Analytics.settings.runtimeExtensibility.allowed

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Analytics.settings.runtimeExtensibility.allowed`                  |
| **Scope**   | `#ENTITY`, `#VIEW`                                                 |
| **Type**    | `Boolean`                                                          |
| **Enums**   | `-`                                                                |
| **Default** | `true`                                                             |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Analytics

Analytics and AnalyticsDetails capture the analytical aspects of a CDS entity. It is relevant if the analytical engine is interpreting the views. Semantically, the “Analytics” annotations can be differentiated between annotations that are relevant for the InfoProvider/CUBE-level and annotations being only relevant for Analytical Queries.

## settings

No KTD found

## runtimeExtensibility

No KTD found

## allowed

*`@Analytics.settings.runtimeExtensibility.allowed`: true*: If this annotation is set in the header of the CDS query view, some BI tools offer the possibility to extend the runtime view with further dimensions or measures at runtime. This is not possible if this annotation is not set. If not all dimensions or measures of the cube view should be used, these can be excluded with the annotation *`@Analytics.excludeFromRuntimeExtensibility`: true*.
