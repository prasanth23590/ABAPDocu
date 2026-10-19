---
title: "EnterpriseSearch.freeStyleField.importance"
source_file: abencds_525210926-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > EnterpriseSearch"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EnterpriseSearch.freeStyleField.importance

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `EnterpriseSearch.freeStyleField.importance`                       |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(6)`                                                        |
| **Enums**   | `#HIGH, #LOW, #MEDIUM`                                             |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## EnterpriseSearch

`@EnterpriseSearch` annotations add semantics that is needed to use a view entity as a (CDS-based) search model in the Enterprise Search framework.

## freeStyleField

**Short Description**

Mark a view field for freestyle search.

When defining CDS-based Search Models, at least one element/field has to be annotated with this CDS annotation.

**Use Case**

This CDS annotation defines that a view field is used in the freestyle search. The search terms entered into the search bar are searched for in all freestyle search fields.

The importance part of the CDS annotation specifies how relevant a (freestyle search) hit on the respective field is for ranking. The (automatically calculated) ranking influences how the search hits are sorted. The better a search hit is ranked, the higher it appears in the list of search result items. There are the following three options for the relevance/importance of a freestyle field: \#LOW, \#MEDIUM and \#HIGH. We recommend that at least one freestyle field has the relevance/importance \#HIGH. For performance reasons, the number of fields enabled for freestyle search should not exceed 10 ~ 15.

By using the subannotation withAutoCompletion, the "auto-completion" function will be activated for the corresponding view field: While the user enters a search term into the search bar, Enterprise Search predicts the rest of the search term and makes appropriate suggestions for an automatic completion of this search term. For performance reasons, this function should be used for a maximum of 3 ~ 5 fields of a CDS-based Search Model.

## importance

No KTD found
