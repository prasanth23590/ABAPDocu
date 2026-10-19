---
title: "AbapCatalog.dbHints.hint"
source_file: abencds_828976635-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.dbHints.hint

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.dbHints[ ].hint`                      |
| **Scope**   | `#VIEW`                                            |
| **Type**    | `String(1298)`                                     |
| **Enums**   | `-`                                                |
| **Default** | `-`                                                |
| **Text**    | `-`                                                |
| **MDE**     | `-`                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AbapCatalog

Technical settings of a CDS entity.

## dbHints

**Obsolete:** Specifications for database hints.

Replaced by `@Consumption.dbHints`.

## hint

Obsolete: Database hint (evaluated using SADL).

\####Annotation Value

Platform-dependent database hint.

## Further Information

The [framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) [`@Consumption.dbHints`](abencds_annotations_frmwrk_tables.md) replaces the [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) [`@AbapCatalog.dbHints`](abencds_annotations_abap_tables.md) and makes it obsolete. The ABAP annotation is evaluated by frameworks such as SADL and not by the ABAP runtime framework.

There is a syntax check that checks the value of the annotation against a list of allowed values.

### SAP-internal Hint

The ABAP class `CL_SADL_GW_CDS_DBHINT` lists the database hints that are allowed as values for this annotation.
