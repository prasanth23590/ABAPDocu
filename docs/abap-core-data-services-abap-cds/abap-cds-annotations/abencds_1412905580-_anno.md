---
title: "AnalyticsDetails.variable.usageType"
source_file: abencds_1412905580-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > AnalyticsDetails"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AnalyticsDetails.variable.usageType

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `AnalyticsDetails.variable.usageType`                              |
| **Scope**   | `#PARAMETER`                                                       |
| **Type**    | `String(20)`                                                       |
| **Enums**   | `#FILTER, #FORMULA, #PARAMETER`                                    |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AnalyticsDetails

To enable Analytics, there has to be defined CDS views which represent the Analytical Provider and CDS view, which represent analytical queries. Analytical queries must select from an Analytical model. Views which belong to the Analytical Provider can be enabled for data extraction. The analytical queries can be consumed by BI-tools like SAP Analytics Cloud, Analysis for Office and others via the Analytical Engine.

Annotations belonging to domain AnalyticsDetails are all on element or parameter level.

## variable

This is an annotation for a parameter. In core CDS a parameter represents a mandatory, single value variable at runtime. With this annotation a parameter becomes a variable which represents a hierarchy node, an interval or a range. It can also become optional or can represent multiple values. This is only supported in analytics. Analytical queries using this feature can't be published via OData.

## usageType

This is a classification that corresponds to the terminology Parameter Variable, Filter Variable, Formula Variable. The actual usage of the parameter in the view definition has to match the intended usage expressed with this annotation. Whether the parameter is used according to the usageType is not veryfied by the analytical engine.

## Enums

## \#PARAMETER

The variable is used for a parameter of the underlaying data source, i.e. the value is pushed down at runtime via SQL to the corresponding data source.

## \#FILTER

The variable is used in filters for the dimension represented by the element annotated as referenceElement. Filters are typically global filters (CDS: where clause), or element restrictions in Restricted Measures (CDS: sub expression in CASE...WHEN... expressions).

## \#FORMULA

The variable is used as a placeholder in expressions defining calculated measures (i.e. virtual elements with formula aggregation, referring to other elements with measure semantics).
