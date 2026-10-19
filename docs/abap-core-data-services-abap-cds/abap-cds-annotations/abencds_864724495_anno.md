---
title: "AbapCatalog.extensibility.elementSuffix"
source_file: abencds_864724495_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.extensibility.elementSuffix

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.extensibility.elementSuffix`          |
| **Scope**   | `#ENTITY`                                          |
| **Type**    | `String(3)`                                        |
| **Enums**   | `-`                                                |
| **Default** | `-`                                                |
| **Text**    | `-`                                                |
| **MDE**     | `-`                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AbapCatalog

Technical settings of a CDS entity.

## extensibility

Extensibility settings for CDS objects.

## elementSuffix

Defines a 3-character element suffix which must be used for extension fields and extension associations when extending a released API.

## Annotation Value

suffix must consist of exactly three characters. These characters can be alphabetical or numerical (0-9).

## Further Information

A valid suffix must obey the following rules:

- If the object is created in a customer or partner system, the suffix must have Y or Z as first character.

- If the object is created in an SAP system, the suffix must not have Y or Z as first character.

- If the field suffix is already used by another development object, a syntax check warning occurs.
