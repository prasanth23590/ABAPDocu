---
title: "EnterpriseSearch.filteringFacet.displayPosition"
source_file: abencds_1949728172_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > EnterpriseSearch"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# EnterpriseSearch.filteringFacet.displayPosition

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `EnterpriseSearch.filteringFacet.displayPosition`                  |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `Integer`                                                          |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## EnterpriseSearch

`@EnterpriseSearch` annotations add semantics that is needed to use a view entity as a (CDS-based) search model in the Enterprise Search framework.

## filteringFacet

**Short Description**

Based on the value distribution of a view field, a more specific search is enabled.

The usage of this CDS annotation is optional. You may define a CDS-based Search Model without this CDS annotation.

**Use Case**

In the “Filter By” section of the Fiori Launchpad Search UI, different values of the view field are displayed with the number of search hits that contain the respective value (the values displayed are called filter values). By selecting one or more filter values, you can restrict the current list of search result items to the respective hits (for multiple selected filter values, the filter values are connected using “or”).

If, for example, the view field “locationOfBuilding” is annotated accordingly, the following (selectable) filter values may be provided in the “Filter By” section: Walldorf (326), Bangalore (102), New York (57), Berlin (32), Tokyo (27) – saying that the list of search result items contains 326 buildings located in Walldorf, 102 buildings located in Bangalore, 57 buildings located in New York and so on. By selecting the filter values “Walldorf” and “New York”, you can restrict the current list of search result items to buildings that are located in Walldorf or New York.

The subannotation default defines, that the view field (along with its filter values) is displayed by default in the “Filter By” section (in case the “Filter By” section is not hidden).

The subannotation displayPosition defines the position at which the view field (along with its filter values) is displayed in the “Filter By” section. The subannotation numberOfValues defines how many different filter values are displayed for the view field (maximum).

If you omit the subannotation numberOfValues, the system typically displays a maximum of five filter values. However, it may make sense to display more than five filter values.

## displayPosition

Define the order of facets which is not necessarily the same as the order of elements in the view.

As the a mixed list of filtering facets and filtering attributes is produced, the position should be defined uniquely across both annotations.
