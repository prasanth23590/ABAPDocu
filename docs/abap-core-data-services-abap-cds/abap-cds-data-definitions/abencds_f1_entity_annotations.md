---
title: "CDS DDL - entity_annot"
source_file: abencds_f1_entity_annotations.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Common DDL Elements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - entity_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) as an entity annotation in front of the statement `DEFINE` in the definition of a [CDS entity](../../abap-glossary/abencds_entity_glosry.md). Can be used for the following entities:

- [`DEFINE TABLE ENTITY`](abencds_define_table_entity.md)

- [`DEFINE VIEW ENTITY`](abencds_define_view_entity.md)

- [`DEFINE VIEW ENTITY AS PROJECTION ON`](abencds_define_view_as_projection.md)

- [`DEFINE TABLE FUNCTION`](abencds_f1_define_table_function.md)

- [`DEFINE EXTERNAL ENTITY`](abencds_define_external_entity.md)

- [`DEFINE HIERARCHY`](abencds_f1_define_hierarchy.md)

- [`DEFINE CUSTOM ENTITY`](abencds_f1_define_custom_entity.md)

- [`DEFINE ABSTRACT ENTITY`](abencds_f1_define_abstract_entity.md)

- [`DEFINE VIEW`](../abap-cds-obsolete-language-elements/abencds_define_view_v1.md)

The character `@` must be placed in front of the name `annotation` of the annotation. The annotation should be defined as a CDS object in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). In the annotation definition, the annotation `@Scope` should be used with the value `#ENTITY`.

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- AbapCatalog Annotations

  - [`AbapCatalog.extensibility.allowNewCompositions`](../abap-cds-annotations/abencds_2031682287_anno.md)

  - [`AbapCatalog.extensibility.elementSuffix`](../abap-cds-annotations/abencds_864724495_anno.md)

  - [`AbapCatalog.extensibility.extensible`](../abap-cds-annotations/abencds_1159849682_anno.md)

  - [`AbapCatalog.extensibility.quota.maximumBytes`](../abap-cds-annotations/abencds_699341645-_anno.md)

  - [`AbapCatalog.extensibility.quota.maximumFields`](../abap-cds-annotations/abencds_1345726382_anno.md)

- EndUserText Annotations

  - [`EndUserText.label`](../abap-cds-annotations/abencds_924137870_anno.md)

- Metadata Annotations

  - [`Metadata.allowExtensions`](../abap-cds-annotations/abencds_1985816297-_anno.md)

- ObjectModel Annotations

  - [`ObjectModel.query.implementedBy`](../abap-cds-annotations/abencds_763589850-_anno.md)

## Hint

The `AbapCatalog` annotations listed here are supported in all CDS entities except for [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md), [CDS table functions](../../abap-glossary/abencds_table_function_glosry.md), and [CDS external entities](../../abap-glossary/abencds_external_entity_glosry.md).
