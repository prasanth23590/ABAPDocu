---
title: "CDS DDL - DDIC-Based View, view_annot"
source_file: abencds_view_anno_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, view_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) as a view annotation in the definition of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) in front of the statement [`DEFINE VIEW`](abencds_define_view_v1.md). The character `@` must be placed directly in front of the name `annotation` of the annotation. The annotation should be defined as a CDS object in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). In the annotation definition, the annotation `@Scope` should be used with the value `#VIEW`.

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- AbapCatalog Annotations

  - [`AbapCatalog.buffering.status`](../abap-cds-annotations/abencds_1242119123-_anno.md)

  - [`AbapCatalog.buffering.type`](../abap-cds-annotations/abencds_464103458_anno.md)

  - [`AbapCatalog.buffering.numberOfKeyFields`](../abap-cds-annotations/abencds_1619044161-_anno.md)

  - [`AbapCatalog.dataMaintenance`](../abap-cds-annotations/abencds_67699033-_anno.md)

  - [`AbapCatalog.compiler.compareFilter`](../abap-cds-annotations/abencds_1687178802-_anno.md)

  - [`AbapCatalog.sqlViewName`](../abap-cds-annotations/abencds_253495944_anno.md)

  - [`AbapCatalog.viewEnhancementCategory`](../abap-cds-annotations/abencds_801468554-_anno.md)

- AccessControl Annotations

  - [`AccessControl.authorizationCheck`](../abap-cds-annotations/abencds_1180334353_anno.md)

- ClientHandling Annotations

  - [`ClientHandling.type`](../abap-cds-annotations/abencds_613831553_anno.md)

  - [`ClientHandling.algorithm`](../abap-cds-annotations/abencds_1114072352_anno.md)

- Metadata Annotations

  - [`Metadata.ignorePropagatedAnnotations`](../abap-cds-annotations/abencds_1433174898-_anno.md)

- ObjectModel Annotations

  - [`ObjectModel.usageType.dataClass`](../abap-cds-annotations/abencds_1091668137-_anno.md)

  - [`ObjectModel.usageType.serviceQuality`](../abap-cds-annotations/abencds_1255374604-_anno.md)

  - [`ObjectModel.usageType.sizeCategory`](../abap-cds-annotations/abencds_1163152301_anno.md)

## Hints

- The ABAP annotation `AbapCatalog.sqlViewName` is **mandatory**. It defines the name of the [CDS-managed DDIC view (obsolete)](../../abap-glossary/abencds_mngdddic_view_glosry.md) in ABAP Dictionary. The name given to the DDIC database view can no longer be changed after the CDS view is transported into a follow-on system.

- The following `AbapCatalog` annotations are obsolete:

  - [`@AbapCatalog.dbHints`](abencds_annotation_obsolete.md)

  - [`@AbapCatalog.preserveKey`](abencds_annotation_obsolete.md)

- Alongside the view annotations listed here, the globally valid [entity annotations](../abap-cds-data-definitions/abencds_f1_entity_annotations.md) can also be specified for a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md).
