---
title: "Search.textIndex.required"
source_file: abencds_284009624_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Search"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Search.textIndex.required

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Search.textIndex.required`                                        |
| **Scope**   | `#ELEMENT`                                                         |
| **Type**    | `Boolean`                                                          |
| **Enums**   | `-`                                                                |
| **Default** | `true`                                                             |
| **Text**    | `-`                                                                |
| **MDE**     | `X`                                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                                  |

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

## textIndex

Specify field characterisics regarding a text index.

## required

Indicate that a text index is required for searching on a field.
