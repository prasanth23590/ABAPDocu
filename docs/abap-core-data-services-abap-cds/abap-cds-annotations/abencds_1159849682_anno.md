---
title: "AbapCatalog.extensibility.extensible"
source_file: abencds_1159849682_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.extensibility.extensible

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `AbapCatalog.extensibility.extensible`                        |
| **Scope**   | `#ENTITY`, `#SERVICE`                                         |
| **Type**    | `Boolean`                                                     |
| **Enums**   | `-`                                                           |
| **Default** | `true`                                                        |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## AbapCatalog

Technical settings of a CDS entity.

## extensibility

Extensibility settings for CDS objects.

## extensible

Enables or disables extensibility for the current scope.

## Annotation Values

true: Extensions are allowed.

false: Extensions are not allowed.

If the annotation is not specified:

- For CDS entities extended by CDS entity extensions, the value `true` is used.

- In other cases, the value `false` is used.

## Further Information

The annotation `@AbapCatalog.extensibility.extensible` with the value `true` is a prerequisite for the [C0 release](../../abap-glossary/abenc0_contract_glosry.md) of a CDS service definition.
