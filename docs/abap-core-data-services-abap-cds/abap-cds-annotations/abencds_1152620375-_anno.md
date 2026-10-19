---
title: "Analytics.variableCheck.implementedBy"
source_file: abencds_1152620375-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Analytics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Analytics.variableCheck.implementedBy

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Analytics.variableCheck.implementedBy`                            |
| **Scope**   | `#ENTITY`, `#TABLE_FUNCTION`, `#VIEW`                              |
| **Type**    | `String(255)`                                                      |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Analytics

Analytics and AnalyticsDetails capture the analytical aspects of a CDS entity. It is relevant if the analytical engine is interpreting the views. Semantically, the “Analytics” annotations can be differentiated between annotations that are relevant for the InfoProvider/CUBE-level and annotations being only relevant for Analytical Queries.

## variableCheck

This is only interpreted in the context of an analytical query to check the consistency of the variable input.

## implementedBy

Prefix “ABAP:” followed by the name of an ABAP class that implements interface IF_RSRTS_CDS_VARIABLE_CHECK.

For example:

*`@Analytics.variableCheck.implementedBy`: 'ABAP:ZCL_CHECK_VARIABLES'*

In the above annotation, 'ZCL_CHECK_VARIABLES' is the name of the ABAP class that implemented interface IF_RSRTS_CDS_VARIABLE_CHECK.

Refer to Interface Documentation for more information on IF_RSRTS_CDS_VARIABLE_CHECK.
