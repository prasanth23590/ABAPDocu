---
title: "Analytics.settings.displayOriginalInitialValue"
source_file: abencds_33267603-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Analytics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Analytics.settings.displayOriginalInitialValue

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Analytics.settings.displayOriginalInitialValue`                   |
| **Scope**   | `#ELEMENT`, `#ENTITY`, `#VIEW`                                     |
| **Type**    | `Boolean`                                                          |
| **Enums**   | `-`                                                                |
| **Default** | `true`                                                             |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Analytics

Analytics and AnalyticsDetails capture the analytical aspects of a CDS entity. It is relevant if the analytical engine is interpreting the views. Semantically, the “Analytics” annotations can be differentiated between annotations that are relevant for the InfoProvider/CUBE-level and annotations being only relevant for Analytical Queries.

## settings

No KTD found

## displayOriginalInitialValue

The Analytic Engine usually displays the initial value of a dimension as '#'.

With annotation *`@Analytics.settings.displayOriginalInitialValue`: true*, the external value of the initial value will be shown.

This annotation can be set in the header of a DIMENSION or TEXT view, or it can be set in a CUBE view for a field without foreign key association or text association. Also, this annotation can only be set for dimensions where the initial value is not a space.

Showing '#' is the default if the annotation is not set.
