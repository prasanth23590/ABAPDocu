---
title: "AbapCatalog.entityBuffer.definitionType"
source_file: abencds_1760222934_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.entityBuffer.definitionType

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.entityBuffer.definitionType[ ]`       |
| **Scope**   | `#VIEW`                                            |
| **Type**    | `String(20)`                                       |
| **Enums**   | `#DELEGATED, #MATERIALIZED`                        |
| **Default** | `-`                                                |
| **Text**    | `-`                                                |
| **MDE**     | `-`                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AbapCatalog

Technical settings of a CDS entity.

## entityBuffer

Defines settings for the table buffering of a CDS object.

## definitionType

## Enums

## \#DELEGATED

Only delegated buffer definitions and type none can be defined. Only the delegated buffer definitions apply.

## \#MATERIALIZED

Only materialized buffer definitions (type single, generic, full, and none) can be defined.
