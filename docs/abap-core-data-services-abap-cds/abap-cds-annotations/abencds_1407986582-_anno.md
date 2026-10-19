---
title: "DataIntegration.dataProduct.type"
source_file: abencds_1407986582-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > DataIntegration"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DataIntegration.dataProduct.type

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `DataIntegration.dataProduct.type`                                 |
| **Scope**   | `#SERVICE`                                                         |
| **Type**    | `String(20)`                                                       |
| **Enums**   | `#DERIVED, #PRIMARY`                                               |
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

## type

Defines the type of a data product in the context of S/4HANA.

## Enums

## \#PRIMARY

Data product supports the replication API, i.e. the definition of the corresponding service has the "replication" support.

## \#DERIVED

Data product do not provide support for data replication. It can offer federation, metadata and additional query APIs.
