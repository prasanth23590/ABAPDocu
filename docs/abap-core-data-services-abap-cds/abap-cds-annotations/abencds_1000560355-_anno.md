---
title: "Environment.sql.passValue"
source_file: abencds_1000560355-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > Environment"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Environment.sql.passValue

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `Environment.sql.passValue`                        |
| **Scope**   | `#ELEMENT`, `#PARAMETER`                           |
| **Type**    | `Boolean`                                          |
| **Enums**   | `-`                                                |
| **Default** | `true`                                             |
| **Text**    | `-`                                                |
| **MDE**     | `-`                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Environment

Controls value passing to parameters.

## sql

No KTD found

## passValue

Specifies whether a placeholder ? or a literal value is passed to the database in an ABAP SQL condition when a CDS element or parameter is compared with a host variable.

## Annotation Values

true: The literal value of the host variable is passed.

false: A placeholder ? is passed.

If the annotation is not specified, the value false is used.

## Further Information

This annotation is recommended specifically for optimal performance of union views. For details, see the topic [Performance Aspects of Specific Features](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/e5e92c73593e49be896a62c56426e114?version=sap_cross_product_abap) in the CDS Performance guide. In other use cases, the annotation is not recommended.
