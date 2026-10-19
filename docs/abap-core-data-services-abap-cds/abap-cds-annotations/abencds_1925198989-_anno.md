---
title: "AbapCatalog.extensibility.allowNewDatasources"
source_file: abencds_1925198989-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.extensibility.allowNewDatasources

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.extensibility.allowNewDatasources`    |
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

## extensibility

Extensibility settings for CDS objects.

## allowNewDatasources

Defines whether a CDS object extension is allowed to use new data sources. More precisely, if a CDS object extension specifies an association, this annotation defines whether the newly defined local association is allowed to be used in path expressions.

## Annotation Values

true: New data sources in extensions allowed.

false: New data sources in extensions not allowed.

If the annotation is not specified, the value false is used.

## Further Information

`AbapCatalog.extensibility.allowNewdataSources` must be set to `false` in CDS view entities. The value `true` is only allowed in CDS projection views.
