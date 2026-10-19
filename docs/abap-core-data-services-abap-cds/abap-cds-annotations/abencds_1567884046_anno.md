---
title: "Search.searchable"
source_file: abencds_1567884046_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Search"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Search.searchable

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Search.searchable`                                                |
| **Scope**   | `#ENTITY`                                                          |
| **Type**    | `Boolean`                                                          |
| **Enums**   | `-`                                                                |
| **Default** | `true`                                                             |
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

## searchable

## Evaluation Engine

Runtime: Interpreted by Enterprise Search and SADL

### Short Description

Defines if a CDS entity is generally relevant for search scenarios. This annotation must be set in case other search-related annotations are being defined for elements of the respective CDS entity. The annotation offers a general switch and a means to quickly detect whether a view is relevant or not.

If a CDS entity is annotated with `@EnterpriseSearch.model` it is not necessary to additionally annotate it with `@Search.searchable`.
