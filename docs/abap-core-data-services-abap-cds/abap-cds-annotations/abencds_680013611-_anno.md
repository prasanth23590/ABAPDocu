---
title: "AbapCatalog.dbHints.dbSystem"
source_file: abencds_680013611-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.dbHints.dbSystem

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)           |
|-------------|--------------------------------------------------------------|
| **Syntax**  | `AbapCatalog.dbHints[ ].dbSystem`                            |
| **Scope**   | `#VIEW`                                                      |
| **Type**    | `String(3)`                                                  |
| **Enums**   | `#ADA, #ALL, #ASE, #DB2, #DB4, #DB6, #HDB, #INF, #MSS, #ORA` |
| **Default** | `-`                                                          |
| **Text**    | `-`                                                          |
| **MDE**     | `-`                                                          |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                            |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AbapCatalog

Technical settings of a CDS entity.

## dbHints

**Obsolete:** Specifications for database hints.

Replaced by `@Consumption.dbHints`.

## dbSystem

**Obsolete:** Database system for which a database hint is specified (evaluated using SADL).

## Enums

## \#ADA

SAP MaxDB

## \#DB2

IBM DB2

## \#DB4

IBM DB2 for AS/400

## \#DB6

IBM DB2 UDB

## \#INF

Informix

## \#MSS

Microsoft SQL Server

## \#ORA

Oracle DB

## \#HDB

SAP HANA database

## \#ASE

Sybase ASE

## \#ALL

All database systems

## Further Information

The [framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) [`@Consumption.dbHints`](abencds_annotations_frmwrk_tables.md) replaces the [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) [`@AbapCatalog.dbHints`](abencds_annotations_abap_tables.md) and makes it obsolete. The ABAP annotation is evaluated by frameworks such as SADL and not by the ABAP runtime framework.
