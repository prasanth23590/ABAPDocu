---
title: "AbapCatalog.entityBuffer.propagationAllowed"
source_file: abencds_1859277801_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.entityBuffer.propagationAllowed

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.entityBuffer.propagationAllowed`      |
| **Scope**   | `#VIEW`                                            |
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

## propagationAllowed

Note: propagated buffers are obsolete. It is still possible, but not recommended to create CDS propagated buffers. However, this is advised against, as there are no longer performance gains to be had.

Enables or disables buffer propagation for a CDS object.

## Annotation Values

true: Buffer propagation allowed.

false: Buffer propagation not allowed.

If the annotation is not specified, the value false is used.
