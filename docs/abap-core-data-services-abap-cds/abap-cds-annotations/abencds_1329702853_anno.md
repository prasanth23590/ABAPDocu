---
title: "DataIntegration.dataProduct.release.version.major"
source_file: abencds_1329702853_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > DataIntegration"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DataIntegration.dataProduct.release.version.major

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `DataIntegration.dataProduct.release.version.major`                |
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

## major

MAJOR is 0 for the data products of status BETA and 1 if status is RELEASED.

Major version should be increased further when one of internal elements of a data product changes its state to "decommissioned":

- An element of one of the included views

- One of the views included into the service definition - the successor \*\* view must be included into the data product

- One of the APIs referenced in outputPorts - the successors must be added to the outputPorts
