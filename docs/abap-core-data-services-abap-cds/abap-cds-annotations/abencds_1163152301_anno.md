---
title: "ObjectModel.usageType.sizeCategory"
source_file: abencds_1163152301_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > ObjectModel"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ObjectModel.usageType.sizeCategory

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `ObjectModel.usageType.sizeCategory`                          |
| **Scope**   | `#ENTITY`, `#TABLE_FUNCTION`                                  |
| **Type**    | `String(3)`                                                   |
| **Enums**   | `#L, #M, #S, #XL, #XXL`                                       |
| **Default** | `#S`                                                          |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## ObjectModel

### Short Description

ObjectModel annotations provide definitions of text-related aspects of the CDS-based data model.

## usageType

Defines properties of the data delivered by CDS object.

## sizeCategory

## Evaluation Engine

Runtime

### Short Description

Specifies the size of the data volume that must be searched to return the result. This usually corresponds to the largest underlying table.

### Use Case

A CDS object can be assigned to one size category, specified by an Enum value.

If the annotation is not specified, the value \#S is used.

### Enums

### \#S

The expected size of the data volume that needs to be searched is less than 1000.

### \#M

The expected size of the data volume that needs to be searched is less than 100,000.

### \#L

The expected size of the data volume that needs to be searched is less than 10,000,000.

### \#XL

The expected size of the data volume that needs to be searched is less than 100,000,000.

### \#XXL

The expected size of the data volume that needs to be searched is 100,000,000 or greater.
