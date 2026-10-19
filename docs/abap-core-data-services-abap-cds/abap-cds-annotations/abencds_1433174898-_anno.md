---
title: "Metadata.ignorePropagatedAnnotations"
source_file: abencds_1433174898-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > Metadata"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Metadata.ignorePropagatedAnnotations

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md)            |
|-------------|---------------------------------------------------------------|
| **Syntax**  | `Metadata.ignorePropagatedAnnotations`                        |
| **Scope**   | `#VIEW`                                                       |
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

## ignorePropagatedAnnotations

Defines whether annotations are inherited from used CDS objects when analyzing them with the annotation API CL_DD_DDL_ANNOTATION_SERVICE.

## Annotation Values

true: Only direct and derived annotations of the definition are respected.

false: Inherited annotations of used definitions are also respected.

If the annotation is not specified, the value false is used.
