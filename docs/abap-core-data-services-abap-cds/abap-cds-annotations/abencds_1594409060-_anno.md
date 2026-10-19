---
title: "Search.ranking"
source_file: abencds_1594409060-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Search"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Search.ranking

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Search.ranking`                                                   |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `String(6)`                                                        |
| **Enums**   | `#HIGH, #LOW, #MEDIUM`                                             |
| **Default** | `#MEDIUM`                                                          |
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

## ranking

## Evaluation Engine

Runtime: Interpreted by Enterprise Search and SADL

### Short Description

Specifies how relevant the values of an element are for ranking, if the freestyle search terms match the element value.

Usually, such a search must not operate on all elements – for performance reasons, and because not all elements (e.g. internal keys) do qualify for this kind of access.

### Enums

### \#HIGH

The element is of high relevancy; this holds usually for ID and their descriptions.

### \#MEDIUM

The element is of medium relevancy; this holds usually for other, important element. This is the default.

### \#LOW

Although the element is relevant for freestyle search, a hit in this element has no real significance for a result item's ranking.
