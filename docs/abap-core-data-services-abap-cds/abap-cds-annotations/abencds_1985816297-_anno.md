---
title: "Metadata.allowExtensions"
source_file: abencds_1985816297-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > Metadata"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Metadata.allowExtensions

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `Metadata.allowExtensions`                                    |
| **Scope**   | `#ENTITY`                                                     |
| **Type**    | `Boolean`                                                     |
| **Enums**   | `-`                                                           |
| **Default** | `true`                                                        |
| **Text**    | `-`                                                           |
| **MDE**     | `-`                                                           |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM` |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Metadata

Defines the handling of metadata of a CDS object.

## allowExtensions

Defines whether a CDS object can be extended with metadata extensions.

## Annotation Values

true: The current CDS object can be extended.

false: The current CDS object cannot be extended.

If the annotation is not specified, the value false is used.

## Further Information

Metadata extensions are currently only supported in [CDS views](../../abap-glossary/abencds_view_glosry.md) and [CDS abstract entities](../../abap-glossary/abencds_abstract_entity_glosry.md). In all other CDS entities, there is no syntax error, but the annotation `Metadata.allowExtensions` has no effect.
