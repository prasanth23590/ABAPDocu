---
title: "AbapCatalog.extensibility.quota.maximumBytes"
source_file: abencds_699341645-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.extensibility.quota.maximumBytes

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.extensibility.quota.maximumBytes`     |
| **Scope**   | `#ENTITY`                                          |
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

## extensibility

Extensibility settings for CDS objects.

## quota

Defines maximum numbers of bytes or fields that can be added to a released API via extensions.

## maximumBytes

Maximum number of bytes.

## Annotation Value

Integer between 0 and 100,000.

## Further Information

- The maximum byte count specified after `maximumBytes` plus the byte count of the current CDS entity must not exceed the technical limitations of the ABAP server. Currently, the technical limitation is at 2^19-1 bytes.

- The value specified should be at least 1000 (indicated by a syntax check warning).
