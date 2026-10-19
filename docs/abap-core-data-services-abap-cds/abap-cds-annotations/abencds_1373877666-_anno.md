---
title: "AbapCatalog.extensibility.dataSources"
source_file: abencds_1373877666-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.extensibility.dataSources

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `AbapCatalog.extensibility.dataSources[ ]`         |
| **Scope**   | `#VIEW`                                            |
| **Type**    | `LocalDefinitionRef`                               |
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

## dataSources

Allowlist of stable alias names of data sources and locally defined associations to be used in extensions.

## Annotation Values

data_source_name:

Alias name of a data source or alias name of a locally defined or redefined association.

## Further Information

`AbapCatalog.extensibility.dataSources`

- can only be specified if extensions are allowed. If `@AbapCatalog.extensibility.extensible` is set to `false` or `@AbapCatalog.viewEnhancementCategory` is set to `#NONE`, no data sources can be specified.

- can specify only such associations as `data_source_name` which have a maximum [target cardinality](../../abap-glossary/abentarget_cardinality_glosry.md) not greater than 1.

- must not be set in union views.
