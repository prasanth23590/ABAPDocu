---
title: "Analytics.settings.valueHelp.supressInitialValue"
source_file: abencds_1693486678_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Analytics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Analytics.settings.valueHelp.supressInitialValue

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Analytics.settings.valueHelp.supressInitialValue`                 |
| **Scope**   | `#ENTITY`, `#TABLE_FUNCTION`, `#VIEW`                              |
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

## valueHelp

No KTD found

## supressInitialValue

This annotation can be used in views of the type *`@Analytics.dataCategory`: \#DIMENSION* and in views of type *`@ObjectModel.dataCategory`: \#TEXT*. It should be used in TEXT views only if there doesn't exist a DIMENSION view. This means, if exist a text association for the representative key field, then the annotation of the dimension is relevant and the annotation of the text view will be ignored.

If annotation *`@Analytics.settings.valueHelp.supressInitialValue`: true* is set, the Analytic Engine will not add an extra line for the initial value when value help is processed. If a record exists with initial key, it will always be shown, independent of the annotation.
