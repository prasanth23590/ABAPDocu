---
title: "AbapCatalog.buffering.type"
source_file: abencds_464103458_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.buffering.type

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.buffering.type`                       |
| **Scope**   | `#VIEW`                                            |
| **Type**    | `String(10)`                                       |
| **Enums**   | `#FULL, #GENERIC, #NONE, #SINGLE`                  |
| **Default** | `#NONE`                                            |
| **Text**    | `-`                                                |
| **MDE**     | `-`                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AbapCatalog

Technical settings of a CDS entity.

## buffering

Defines table buffering for a CDS DDIC-based view.

## type

Defines the type of table buffering for a CDS DDIC-based view.

If the annotation is not specified, the value \#NONE is used.

## Enums

## \#SINGLE

Single record buffering.

## \#GENERIC

Generic buffering.

## \#FULL

Full buffering.

## \#NONE

No buffering.

## Further Information

More information:

- [Table Buffering of CDS DDIC-Based Views](../abap-cds-obsolete-language-elements/abencds_v1_buffering.md)

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Refer to [AbapCatalog.buffering.status](abencds_1242119123-_anno.md)
