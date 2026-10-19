---
title: "EnterpriseSearch.responseField.thumbNail"
source_file: abencds_949259184_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > EnterpriseSearch"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EnterpriseSearch.responseField.thumbNail

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `EnterpriseSearch.responseField.thumbNail`                         |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `Boolean`                                                          |
| **Enums**   | `-`                                                                |
| **Default** | `true`                                                             |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## EnterpriseSearch

`@EnterpriseSearch` annotations add semantics that is needed to use a view entity as a (CDS-based) search model in the Enterprise Search framework.

## responseField

**Short Description**

This annotation is needed to mark a field as (ordinary, non-title) response field.

The special type of the response field is defined by the respective subannotation.

## thumbNail

**Short Description**

Mark a view field as a thumbnail response field.

The usage of this CDS annotation is optional. You may define a CDS-based Search Model without this CDS annotation.

**Use Case**

This CDS annotation indicates that the response field contains a URL to a (non-person) image. This image is displayed in the search result item as a miniature image.

Since the miniature image is positioned automatically within the search result item, no displayPosition needs to be specified.
