---
title: "DataIntegration.dataProduct.category"
source_file: abencds_698663424_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > DataIntegration"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DataIntegration.dataProduct.category

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `DataIntegration.dataProduct.category`                             |
| **Scope**   | `#SERVICE`                                                         |
| **Type**    | `String(30)`                                                       |
| **Enums**   | `#ANALYTICAL, #BUSINESS_OBJECT, #OTHER`                            |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## DataIntegration

No KTD found

## dataProduct

This annotation represents some mandatory attributes of the data product ORD definition.

## category

The category attribute is only important for the PUBLIC data products.

## Enums

## \#BUSINESS_OBJECT

The data product represents an SOT of the category "business object".

## \#ANALYTICAL

The data product represents an SOT of the category "analytical".

## \#OTHER

The data product is not related to an SOT (only allowed for the INTERNAL data products).
