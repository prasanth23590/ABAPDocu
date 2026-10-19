---
title: "EnterpriseSearch.title.titleField"
source_file: abencds_1589352869_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > EnterpriseSearch"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EnterpriseSearch.title.titleField

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `EnterpriseSearch.title.titleField`                                |
| **Scope**   | `#ENTITY`                                                          |
| **Type**    | `ElementRef`                                                       |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## EnterpriseSearch

`@EnterpriseSearch` annotations add semantics that is needed to use a view entity as a (CDS-based) search model in the Enterprise Search framework.

## title

**Short Description**

Set the title of the search result items.

For defining CDS-based Search Models, this CDS annotation is mandatory.

**Use Case**

This CDS annotation defines which field of the CDS View Entity is used as the title (titleField), and (optionally) which field of the CDS View Entity is used as the subtitle (subTitleField) to identify a specific result item.

## titleField

Define the field of the CDS View Entity that is used as the title to identify a specific result item.
