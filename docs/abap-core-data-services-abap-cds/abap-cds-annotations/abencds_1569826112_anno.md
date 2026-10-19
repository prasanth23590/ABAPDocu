---
title: "AbapCatalog.typeSpec.outputLength"
source_file: abencds_1569826112_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.typeSpec.outputLength

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.typeSpec.outputLength`                |
| **Scope**   | `#ELEMENT`, `#SIMPLE_TYPE`                         |
| **Type**    | `Integer`                                          |
| **Enums**   | `-`                                                |
| **Default** | `-`                                                |
| **Text**    | `-`                                                |
| **MDE**     | `-`                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AbapCatalog

Technical settings of a CDS entity.

## typeSpec

Settings for CDS type definitions.

## Hint

CDS metadata extensions (MDE) are not supported for CDS type definitions. If required, the metadata of a CDS type can be extended when the CDS type is used in another CDS object, such as a CDS view entity.

## outputLength

Specifies the output length of the CDS type. If the annotation is not set, then the output length is derived from the data element or calculated from the built-in type definition.

## Example

`@AbapCatalog.typeSpec.outputLength`: 30

Sets output length 30 in metadata and runtime object.
