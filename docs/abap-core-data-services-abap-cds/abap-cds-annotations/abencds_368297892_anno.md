---
title: "AbapCatalog.amdp.allowedForWrite"
source_file: abencds_368297892_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.amdp.allowedForWrite

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.amdp.allowedForWrite`                 |
| **Scope**   | `#TABLE_ENTITY`                                    |
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

## amdp

Settings specific to AMDP usage.

## allowedForWrite

Enables or disables a CDS table entity for write access by AMDPs.

## Annotation Values

true: Write by AMDP is allowed. Buffering of this CDS table entity and its view stack is not allowed in this case.

false: Write by AMDP is not allowed.

If the annotation is not specified, the value false is used.
