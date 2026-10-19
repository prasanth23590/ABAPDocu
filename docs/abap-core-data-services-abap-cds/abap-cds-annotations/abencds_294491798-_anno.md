---
title: "Search.fuzzinessThreshold"
source_file: abencds_294491798-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Search"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Search.fuzzinessThreshold

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Search.fuzzinessThreshold`                                        |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `Decimal(3,2)`                                                     |
| **Enums**   | `-`                                                                |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Search

Search annotations mark a view as searchable. You define the fuzziness threshold as well as the specifics of term mappings at element level.

### Scope and Definition

`@Scope`:\[#ENTITY\]

Annotation Search

{

searchable : Boolean default true;

};

`@Scope`:\[#ELEMENT\]

Annotation Search

{

defaultSearchElement : Boolean default true;

ranking : String(6) enum { HIGH = 'high'; MEDIUM = 'medium'; LOW = 'low'; } default \#MEDIUM;

fuzzinessThreshold : Decimal(3,2);

termMappingDictionary : String(128);

termMappingListId : array of String(32);

};

## fuzzinessThreshold

## Evaluation Engine

Runtime: Interpreted by Enterprise Search and SADL

### Short Description

Specifies the least level of fuzziness (with regard to some comparison criteria passed at runtime) the element has to have to be considered in a fuzzy search at all.

Usually, such a search must not operate on all elements – for performance reasons, and because not all elements (e.g. internal keys) do qualify for this kind of access.

### Note

A fuzzy search enables a certain degree of error tolerance and returns records even if the search term contains additional or missing characters or other types of spelling errors.

- To perform a fuzzy search you have to set the search mode to fuzzy in the customizing settings of your ABAP system. Find the customizing node under SAP NetWeaver Implementation Guide Search and Operational Analytics Enterprise Search Search Configuration Set Parameters for Federated Search.

- If in the customizing a value for Fuzzy Similarity is present, the value of the parameter Search.fuzzinessThreshold will become void.

### Value

Decimal (3,2): The least level of fuzziness the element has to have to be considered in a fuzzy search at all, e.g. 0.7.

The value can be between 0 and 1.

We recommend using the default value 0.7 to start with. Later on, you can fine-tune the search settings based on your experiences with the search. You can also fine-tune the search using feedback collected from your users. A value between 0.7 and 0.99 would be most useful. Use 1 for exact matches.
