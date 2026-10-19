---
title: "CDS DDL - proj_view_annot"
source_file: abencds_proj_view_annotations.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - proj_view_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) as a view annotation in the definition of a CDS projection view in front of the statement`DEFINE [TRANSIENT] VIEW ENTITY AS PROJECTION ON`. The character `@` must be placed directly in front of the name `annotation` of the annotation. The annotation should be defined as a CDS object in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). In the annotation definition, the annotation `@Scope` should be used with the value `#VIEW`.

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- AbapCatalog Annotations

  - [`AbapCatalog.dataMaintenance`](../abap-cds-annotations/abencds_67699033-_anno.md)

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

- Projection views inherit the field and association annotations of the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). Header annotations are not inherited and must be specified anew, if required.

- Alongside the view annotations shown here, the globally valid [entity annotations](abencds_f1_entity_annotations.md) can also be specified for a CDS projection view.

- Only a limited number of view annotations can be used in CDS projection views. The following groups of annotations are not possible and are therefore not listed below:

  - Client handling is done implicitly in CDS projection views. The client is always set to `#session_variable_filter`. Therefore, client handling annotations cannot be explicitly set in CDS projection views.

  - `DataAging` annotations are currently not supported for projection views.

- Most `Abap.Catalog` annotations supported in CDS views are not supported in CDS projection views, for the following reasons:

  - `AbapCatalog.buffering` annotations are not possible, since [buffering](../../abap-glossary/abentable_buffering_glosry.md) does not work with another CDS view as data source.

  - `AbapCatalog.compiler.compareFilter` is not required, since the optimization of joins is done automatically.

  - `AbapCatalog.sqlViewName` is not required, since projection views do not have a corresponding SQL view in ABAP Dictionary.

- The annotations `AccessControl` and `ObjectModel` have further [framework-specific subannotations](../abap-cds-annotations/abencds_annotations_frmwrk.md).
