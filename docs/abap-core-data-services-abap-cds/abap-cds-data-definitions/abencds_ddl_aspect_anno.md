---
title: "CDS DDL - CDS Aspect, cds_ddl_aspect_annot"
source_file: abencds_ddl_aspect_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Aspects > CDS DDL - DEFINE ASPECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Aspect, cds_ddl_aspect_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) as an aspect annotation in the definition of a [CDS DDL aspect](abencds_ddl_aspect_glosry.md) in front of the statement [`DEFINE ASPECT`](abencds_define_aspect.md). The character `@` must be placed directly in front of the name `annotation` of the annotation. The annotation must be defined in a [CDS object](../../abap-glossary/abencds_object_glosry.md); in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). Otherwise, a syntax error occurs. In the annotation definition, the annotation `@Scope` should be used with the value `#ASPECT`.

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- EndUserText Annotations

  - [`EndUserText.label`](../abap-cds-annotations/abencds_924137870_anno.md)

  - [`EndUserText.quickInfo`](../abap-cds-annotations/abencds_26162021_anno.md)

## Hint

All annotations are optional, and an aspect can also be created without any annotations.
