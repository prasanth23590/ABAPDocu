---
title: "Analytics.document.semantics"
source_file: abencds_669838829-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Analytics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Analytics.document.semantics

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md)                                                                                  |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Syntax**  | `Analytics.document.semantics`                                                                                                                      |
| **Scope**   | `#ELEMENT`                                                                                                                                          |
| **Type**    | `String(30)`                                                                                                                                        |
| **Enums**   | `#DOCUMENT, #ID, #INFOPROV, #KYFNM, #OWNER, #PROPERTY, #QPROV, #SELECTIONS, #SESSION_ID, #STATUS, #SVA_INFOPROV, #TAG, #TIMESTAMP, #TYPE, #VERSION` |
| **Default** | `-`                                                                                                                                                 |
| **Text**    | `-`                                                                                                                                                 |
| **MDE**     | `X`                                                                                                                                                 |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`                                                                                       |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Analytics

Analytics and AnalyticsDetails capture the analytical aspects of a CDS entity. It is relevant if the analytical engine is interpreting the views. Semantically, the “Analytics” annotations can be differentiated between annotations that are relevant for the InfoProvider/CUBE-level and annotations being only relevant for Analytical Queries.

## document

The business users would like to add, modify, or delete comments in the cells of the result set of a Query in Analytic Engine. The comments should be visible in all queries of one cube view which share the same filters. With the proposed annotations we would like to achieve this. With the **document** Annotations it is possible to define a storage for documents, assign cube views to a storage and enable an analytical query for comments. The view which provides the documents (storage) needs the annotation *`@Analytics.dataCategory`: \#DOCSTORE*.

## semantics

The annotation *`@Analytics.document.semantics`* is used for describing the meaning of the fields in the Document CDS View.

## Enums

## \#ID

\#ID: Field of type NUMC 16

## \#VERSION

\#VERSION:

## \#TAG

\#TAG: Field of type CHAR 60

## \#QPROV

\#QPROV: Field of type CHAR 30

## \#TYPE

\#TYPE: Field of type CHAR 1

## \#OWNER

\#OWNER: Field of type CHAR 12

## \#INFOPROV

\#INFOPROV: Field of the type CHAR 30

## \#SVA_INFOPROV

\#SVA_INFOPROV: Field of the type CHAR 1

## \#KYFNM

\#KYFNM: Field of type CHAR 30

## \#STATUS

\#STATUS: Field of type CHAR 1

## \#SESSION_ID

\#SESSION_ID: Field of type CHAR 30

## \#TIMESTAMP

\#TIMESTAMP: Field of type DEC 15. In CDS:ABAP data element with reference to domain TZNTSTMPS.

## \#DOCUMENT

\#DOCUMENT: Field of type RAWSTRING

## \#SELECTIONS

\#SELECTIONS: Field of type RAWSTRING

## \#PROPERTY

\#PROPERTY: Field of type RAWSTRING
