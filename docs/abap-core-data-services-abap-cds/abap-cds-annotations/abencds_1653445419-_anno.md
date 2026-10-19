---
title: "EnterpriseSearch.filteringAttribute.considerNullValues"
source_file: abencds_1653445419-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > EnterpriseSearch"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EnterpriseSearch.filteringAttribute.considerNullValues

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `EnterpriseSearch.filteringAttribute.considerNullValues`           |
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

## filteringAttribute

**Short Description**

By providing a filter based on the view field, a more specific search is enabled.

The usage of this CDS annotation is optional. You may define a CDS-based Search Model without this CDS annotation.

**Use Case**

The “Filters” section of the Fiori Launchpad Search UI, contains a filter based on the view field. By providing a filter value, you can restrict the current list of search result items to the respective hits. If, for example, the view field “locationOfBuilding” is annotated accordingly, you may restrict the current list of search result items to buildings located in Walldorf by providing the filter value “Walldorf” to the filter which is based on this view field.

## considerNullValues

Cause the search engine to count the NULL-values and to return them as a facet filter value.

As ABAP does not use real NULL values and because this count is very costly, the annotation should only be used in special cases.
