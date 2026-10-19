---
title: "AbapCatalog.preserveKey"
source_file: abencds_450773322_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > AbapCatalog"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# AbapCatalog.preserveKey

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `AbapCatalog.preserveKey`                                     |
| **Scope**   | `#VIEW`                                                       |
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

## preserveKey

**Obsolete:** Used before release 7.58/7.90 to define the key fields of the CDS-managed DDIC view of an obsolete CDS DDIC-based view.

The annotation can be kept in existing DDLS sources, but it does not have an effect any more and leads to a warning from the syntax check. The key fields of the CDS-managed DDIC view are always defined by the addition KEY in the SELECT list.

## Annotation Values

true: This value was used to specify that the key fields of the CDS-managed DDIC view are defined by the addition KEY in the SELECT list. This is the present behavior.

false: This value was used to define the key fields of the CDS-managed DDIC view as for a DDIC database views in ABAP Dictionary, regardless of the addition KEY. It was also the standard value, when the annotation was not specified. Now, the behavior is always as for the value true.

## Note

The change in behavior between 7.57/7.89 and 7.58/7.90 is incompatible. The key fields of the CDS-managed DDIC view of an obsolete CDS DDIC-based view are defined differently now for views where the annotation was not specified or where it was specified with the value false.
