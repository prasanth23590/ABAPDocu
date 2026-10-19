---
title: "AbapCatalog.typeSpec.changeDocumentRelevant"
source_file: abencds_2016919924-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.typeSpec.changeDocumentRelevant

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.typeSpec.changeDocumentRelevant`      |
| **Scope**   | `#SIMPLE_TYPE`                                     |
| **Type**    | `Boolean`                                          |
| **Enums**   | `-`                                                |
| **Default** | `true`                                             |
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

## changeDocumentRelevant

Specifies whether changes to fields with reference to this simple type are logged when change document objects are involved.

## Annotation Values

true: Change documents are written.

false: Change documents are not written.

If the annotation is not specified, the value false is used.

## Further Information

The change document settings of a CDS simple type are similar to the change document settings of DDIC data elements described in topic [DDIC - Semantic Properties of Data Elements](../../abap-dictionary-ddic/ddic-data-types/abenddic_data_elements_sema.md). If a CDS type is based on a DDIC data element, this setting is inherited from the data element and the annotation value is set in accordance with the DDIC setting.
