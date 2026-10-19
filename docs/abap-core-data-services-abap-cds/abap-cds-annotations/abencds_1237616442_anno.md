---
title: "AnalyticsDetails.query.hierarchyBinding.type"
source_file: abencds_1237616442_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AnalyticsDetails"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AnalyticsDetails.query.hierarchyBinding.type

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `AnalyticsDetails.query.hierarchyBinding[ ].type`                  |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(12)`                                                       |
| **Enums**   | `#CONSTANT, #ELEMENT, #PARAMETER, #SYSTEM_FIELD, #USER_INPUT`      |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AnalyticsDetails

To enable Analytics, there has to be defined CDS views which represent the Analytical Provider and CDS view, which represent analytical queries. Analytical queries must select from an Analytical model. Views which belong to the Analytical Provider can be enabled for data extraction. The analytical queries can be consumed by BI-tools like SAP Analytics Cloud, Analysis for Office and others via the Analytical Engine.

Annotations belonging to domain AnalyticsDetails are all on element or parameter level.

## query

This section defines the additional annotations that we need on the level of analytical queries.

## hierarchyBinding

The AnalyticsDetails.query.hierarchyBinding annotations allow you to specify a special hierarchy for an element with a display hierarchy. One tuple has to be specified for each key field of the hierarchy directory view. The first entry is supplied to the first key field of the hierarchy directory, the second entry to the second key field, and so on. If there is no hierarchy directory, the hierarchy binding can be omitted.

General example for AnalyticsDetails.hierarchyBinding type annotations:

AnalyticsDetails.query.hierarchBinding: {type : \#PARAMETER, value 'parameter_name'}.

In this case, parameter_name specifies the name of a parameter. This annotation is an array of the sub-annotations -type, -value, and variablesequence. See details below.

## type

AnalyticsDetails.query.hierarchyBinding.type determines how the key element is filled (by a constant, a parameter, a filtered element or by a user input field). The type specifies the type of AnalyticsDetails.query.hierarchyBinding.value.
