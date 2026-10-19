---
title: "VDM.viewType"
source_file: abencds_2063101229-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > VDM"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# VDM.viewType

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)                  |
|-------------|-------------------------------------------------------------------------------------|
| **Syntax**  | `VDM.viewType`                                                                      |
| **Scope**   | `#ENTITY`                                                                           |
| **Type**    | `String(30)`                                                                        |
| **Enums**   | `#BASIC, #COMPOSITE, #CONSUMPTION, #DERIVATION_FUNCTION, #EXTENSION,#TRANSACTIONAL` |
| **Default** | `-`                                                                                 |
| **Text**    | `-`                                                                                 |
| **MDE**     | `-`                                                                                 |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                       |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## VDM

VDM annotations classify CDS views of the virtual data model in terms of their admissible resuse options and provisioned content.

The intention of the annotations is to enable certain functionalities that are based on the VDM, such as view browsers, to interpret the CDS entities correctly.

**Evaluation Runtimes**

VDM annotations have no influence on runtime, so there are no dependencies for runtime engines.

## viewType

This annotation defines which view type a specific VDM CDS view belongs to.

## Enums

## \#BASIC

CDS views of type BASIC are interface views that are intended for reuse. They form the core data basis without data redundancies.

## \#COMPOSITE

CDS views of type COMPOSITE are reusable interface views. They provide data that is derived and/or composed from BASIC views.

## \#CONSUMPTION

CDS views of type CONSUMPTION serve specific application purposes and are based on BASIC, COMPOSITE, or TRANSACTIONAL views.

## \#EXTENSION

CDS views of type EXTENSION are also known as *Extension include views*. They are technical carrier views for key user field extensibility.

## \#DERIVATION_FUNCTION

CDS views of type DERIVATION_FUNCTION are used to define derivations for parameters and filter values.

### Related Annotations

This annotation works in combination with the following related annotations:

- `@Consumption.derivation`

- `@Consumption.filter` (for filter values)

## \#TRANSACTIONAL

CDS views of type TRANSACTIONAL are special composite views that define the transactional runtime of an object (including draft support).
