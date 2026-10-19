---
title: "AbapCatalog.typeSpec.conversionExit"
source_file: abencds_58258031_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.typeSpec.conversionExit

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.typeSpec.conversionExit`              |
| **Scope**   | `#ELEMENT`, `#SIMPLE_TYPE`                         |
| **Type**    | `String(5)`                                        |
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

## conversionExit

If specified, connects the CDS type to a conversion exit.

## Annotation Value

name: The name of the conversion exit can be a character string with a maximum of 5 characters consisting of letters, numbers, and underscores.

## Further Information

When a CDS type is typed with a DDIC data element, the conversion exit of the data element is automatically reused as conversion exit of the CDS type.
