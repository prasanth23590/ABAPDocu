---
title: "AbapCatalog.entityBuffer.definitionAllowed"
source_file: abencds_2036691489-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.entityBuffer.definitionAllowed

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.entityBuffer.definitionAllowed`       |
| **Scope**   | `#TABLE_ENTITY`, `#VIEW`                           |
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

## entityBuffer

Defines settings for the table buffering of a CDS object.

## definitionAllowed

Enables or disables table buffering for a CDS object.

## Annotation Values

true: Table buffering allowed.

false: Table buffering not allowed.

If the annotation is not specified, the value false is used.

## Further Information

More information:

- [ABAP CDS - Table Buffering of CDS View Entities](../abap-cds-data-definitions/abencds_v2_view_buffering.md)

- [ABAP CDS - Table Buffering of CDS Table Entities](../abap-cds-data-definitions/abencds_table_entity_buffering.md)
