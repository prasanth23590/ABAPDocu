---
title: "CDS DDL - ANNOTATE, metadata_extension_annot"
source_file: abencds_f1_metadata_ext_annos.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - Specifying Annotations > ABAP CDS - Metadata Extensions > ABAP CDS - DDL for Metadata Extensions > CDS DDL - ANNOTATE ENTITY, VIEW"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - ANNOTATE, metadata_extension_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](abencds_annotations_syntax.md) as a metadata extension annotation in front of the statement [`ANNOTATE`](abencds_f1_annotate_view.md) in the definition of a CDS metadata extension in [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md) The character `@` must be placed in front of the name `annotation` of the annotation. The annotation must be defined as a CDS object in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). In the annotation definition, the annotation `@Scope` must be specified using the value `#ANNOTATE`.

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- AbapAnnotation Annotations

  - [`Metadata.layer`](abencds_195182532_anno.md)

## Hint

All other annotations specified in this place are extension annotations [`@entity_annot1`](abencds_f1_annotate_view.md), [`@entity_annot2`](abencds_f1_annotate_view.md), ..., [`@view_annot1`](abencds_f1_annotate_view.md), [`@view_annot2`](abencds_f1_annotate_view.md), ..., used to expand the entity.
