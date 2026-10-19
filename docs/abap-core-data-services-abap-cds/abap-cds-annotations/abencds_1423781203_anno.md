---
title: "EnterpriseSearch.responseField.standard.displayPosition"
source_file: abencds_1423781203_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > EnterpriseSearch"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EnterpriseSearch.responseField.standard.displayPosition

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `EnterpriseSearch.responseField.standard.displayPosition`          |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `DecimalFloat`                                                     |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
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

## standard

**Short Description**

Mark a view field as a normal/standard response field.

When defining CDS-based Search Models, at least one element/field has to be annotated with this CDS annotation.

**Use Case**

This CDS annotation defines a view field as a normal/standard response field. This response field is displayed within the search result item in the list of response fields at the numbered position displayPosition.

If you define several response fields (which will normally be the case), please make sure to use unique displayPosition values. For each search result item, only 12 response fields are displayed. For this reason, a maximum of 12 response fields (with the displayPosition values 1 to 12) should be defined.

## displayPosition

Define the sequence in which response fields are displayed in the search result.
