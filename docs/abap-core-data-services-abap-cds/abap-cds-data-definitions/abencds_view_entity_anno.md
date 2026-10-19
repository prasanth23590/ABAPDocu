---
title: "CDS DDL - CDS View Entity, view_entity_annot"
source_file: abencds_view_entity_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, view_entity_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) as a view entity annotation in the definition of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) in front of the statement [`DEFINE VIEW ENTITY`](abencds_define_view_entity.md). The character `@` must be placed directly in front of the name `annotation` of the annotation. The annotation must be defined as a [CDS object](../../abap-glossary/abencds_object_glosry.md) in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). Otherwise, a syntax error occurs. In the annotation definition, the annotation `@Scope` should be used with the value `#VIEW`.

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- AbapCatalog Annotations

  - [`AbapCatalog.dataMaintenance`](../abap-cds-annotations/abencds_67699033-_anno.md)

  - [`AbapCatalog.entityBuffer.definitionAllowed`](../abap-cds-annotations/abencds_2036691489-_anno.md)

  - [`AbapCatalog.entityBuffer.propagationAllowed`](../abap-cds-annotations/abencds_1859277801_anno.md)

  - [`AbapCatalog.entityBuffer.definitionType`](../abap-cds-annotations/abencds_1760222934_anno.md)

  - [`AbapCatalog.extensibility.allowNewDatasources`](../abap-cds-annotations/abencds_1925198989-_anno.md)

  - [`AbapCatalog.extensibility.dataSources`](../abap-cds-annotations/abencds_1373877666-_anno.md)

  - [`AbapCatalog.viewEnhancementCategory`](../abap-cds-annotations/abencds_801468554-_anno.md)

- AccessControl Annotations

  - [`AccessControl.authorizationCheck`](../abap-cds-annotations/abencds_1180334353_anno.md)

- Metadata Annotations

  - [`Metadata.ignorePropagatedAnnotations`](../abap-cds-annotations/abencds_1433174898-_anno.md)

- ObjectModel Annotations

  - [`ObjectModel.usageType.dataClass`](../abap-cds-annotations/abencds_1091668137-_anno.md)

  - [`ObjectModel.usageType.serviceQuality`](../abap-cds-annotations/abencds_1255374604-_anno.md)

  - [`ObjectModel.usageType.sizeCategory`](../abap-cds-annotations/abencds_1163152301_anno.md)

## Hints

- Alongside the view annotations listed here, the globally valid [entity annotations](abencds_f1_entity_annotations.md) can also be specified for a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md).

- Client handling is done implicitly and automatically for [CDS view entities](../../abap-glossary/abencds_v2_view_glosry.md) by filtering the client [session variable](../../abap-glossary/abensession_variable_glosry.md) [`$session.client`](abencds_session_variable_v2.md). Client handling annotations are not required and not allowed.

- The following `AbapCatalog` annotations are available in other CDS entities, but they are not supported in CDS view entities:

  - Buffering annotations are currently not supported in CDS view entities, because buffering is not yet possible.

  - The annotation `@AbapCatalog.compiler.compareFilter` is not required and not allowed in CDS view entities, because the filter is implicitly and automatically compared.

  - The [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) [`@AbapCatalog.dbHints`](../abap-cds-annotations/abencds_annotations_abap_tables.md) that was used in [CDS DDIC-based views (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) is not supported. The [framework-specific annotation](../../abap-glossary/abenfrmwrk_annotation_glosry.md) [`@Consumption.dbHints`](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md) is available instead.

- The annotations `AccessControl` and `ObjectModel` have further [framework-specific subannotations](../abap-cds-annotations/abencds_annotations_frmwrk.md). The subannotations of `ObjectModel` used as ABAP annotations characterize CDS view entities with respect to their performance-relevant properties.
