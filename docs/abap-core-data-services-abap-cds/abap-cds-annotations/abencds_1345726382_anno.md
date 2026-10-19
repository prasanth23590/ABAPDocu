---
title: "AbapCatalog.extensibility.quota.maximumFields"
source_file: abencds_1345726382_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.extensibility.quota.maximumFields

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.extensibility.quota.maximumFields`    |
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

## maximumFields

Maximum number of fields.

## Annotation Value

Integer between 0 and 1,000.

## Further Information

- The maximum field count specified after `maximumFields` plus the field count of the current CDS entity must not exceed the technical limitations of the ABAP server. Currently, the technical limitation is at 1500 fields.

- The value specified should be at least 100 (indicated by a syntax check warning).
