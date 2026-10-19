---
title: "DataIntegration.dataProduct.release.version.minor"
source_file: abencds_1912854538-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > DataIntegration"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DataIntegration.dataProduct.release.version.minor

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `DataIntegration.dataProduct.release.version.minor`                |
| **Scope**   | `#SERVICE`                                                         |
| **Type**    | `Integer`                                                          |
| **Enums**   | `-`                                                                |
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

## release

Groups the attributes describing the changes of a data product between specific releases.

## version

Version of the data product according to the semantic versioning notation: https://semver.org/. The attribute is a combination of 3 integer values for MAJOR, MINOR and PATCH versions.

## minor

MINOR should be increased if new CDS views were added to the services definition or new fields were added to the existing views.
