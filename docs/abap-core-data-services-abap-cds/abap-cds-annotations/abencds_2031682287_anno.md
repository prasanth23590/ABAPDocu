---
title: "AbapCatalog.extensibility.allowNewCompositions"
source_file: abencds_2031682287_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.extensibility.allowNewCompositions

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.extensibility.allowNewCompositions`   |
| **Scope**   | `#ENTITY`                                          |
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

## extensibility

Extensibility settings for CDS objects.

## allowNewCompositions

Allows node extensibility. In other words, explicitly allows new child nodes to be added by means of to-child associations.

## Annotation Values

true: Node extensibility is allowed.

false: Node extensibility is not allowed.

If the annotation is not specified, the value false is used.

## Further Information

The annotation is useful only in entity types that allow CDS compositions. For example, this annotation can be specified in CDS transactional interfaces; no syntax error occurs. But it does not have any effect, since the feature set of a transactional interface does not include CDS compositions.
