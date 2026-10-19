---
title: "Analytics.dataCategory"
source_file: abencds_568606453-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > Framework-Specific Annotations > Analytics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Analytics.dataCategory

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [Framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) |
|-------------|--------------------------------------------------------------------|
| **Syntax**  | `Analytics.dataCategory`                                           |
| **Scope**   | `#ENTITY`, `#TABLE_FUNCTION`, `#VIEW`                              |
| **Type**    | `String(20)`                                                       |
| **Enums**   | `#AGGREGATIONLEVEL, #CUBE, #DIMENSION, #DOCSTORE, #FACT`           |
| **Default** | `-`                                                                |
| **Text**    | `-`                                                                |
| **MDE**     | `-`                                                                |
| **API**     | `RELEASED_FOR_KEY_USER_APPS, RELEASED_FOR_SAP_CLOUD_PLATFORM`      |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## Analytics

Analytics and AnalyticsDetails capture the analytical aspects of a CDS entity. It is relevant if the analytical engine is interpreting the views. Semantically, the “Analytics” annotations can be differentiated between annotations that are relevant for the InfoProvider/CUBE-level and annotations being only relevant for Analytical Queries.

## dataCategory

By specifying the dataCategory, you can give directives and hints to analytical engine how to interpret the individual entities. In addition to the below mentioned data categories, *ObjectModel.dataCategory: \#TEXT* is relevant for CDS views with language dependent text.

## Enums

## \#DIMENSION

This value indicates that the entity represents master data. Typically it is a target of a foreign-key association. Furthermore, this kind of view can be used for replication and for queries.

Example: Typical dimensions are material view and customer view.

## \#FACT

Indicates that the entity represents transactional data. Usually, it contains the measures. It can can be used for replication.

## \#CUBE

The \#CUBE value (like \#FACT) also represents factual data, but \#CUBE doesn't have to be without redundancy. This means joins with master data are possible. Queries are usually built on top of \#CUBE, where data is selected from facts.

## \#AGGREGATIONLEVEL

This value indicates a projection. For this kind of view, the analytic manager offers write-back functionality (planning functionality). Views in this category must select from a view with dataCategory = \#CUBE, which supports the annotation Analytics.writeBack.className. No associations are allowed, and elements can't be renamed.

Note: This value should not be used for this annotation. This is used for planning scenarios. These planning scenarios aren't currently available in cloud platforms but only on premise.

## \#DOCSTORE

This value indicates that the view stores comments/documents which are displayed in result sets of analytical queries. The view must select from a database table and renaming (alias) of fields is not allowed.
