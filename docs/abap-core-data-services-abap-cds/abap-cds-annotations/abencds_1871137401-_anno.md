---
title: "Aggregation.allowPrecisionLoss"
source_file: abencds_1871137401-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Aggregation"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Aggregation.allowPrecisionLoss

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Aggregation.allowPrecisionLoss`                                   |
| **Scope**   | `#ENTITY`                                                          |
| **Type**    | `Boolean`                                                          |
| **Enums**   | `-`                                                                |
| **Default** | `true`                                                             |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Aggregation

## allowPrecisionLoss

The annotation can be used in the views of dataCategory: \#CUBE or \#FACT. They must contain a currency or unit conversion.

## Value

Boolean default true

You can specify the order of the currency or unit conversion

If an analytical query (Analytics.query: true) is built with a \#CUBE view, the database aggregates the units or currency and then performs the conversion. This is faster than converting on row level. The results maybe slightly different due to rounding.
