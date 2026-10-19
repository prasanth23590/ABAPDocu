---
title: "CDS DDL - EXTEND VIEW, extension_annot"
source_file: abencds_f1_extend_view_annotations.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entity Extension > CDS DDL - EXTEND VIEW ddic_based"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - EXTEND VIEW, extension_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) as an extension annotation in the definition of a [CDS view extension](../../abap-glossary/abencds_view_extend_glosry.md) before the statement [`EXTEND VIEW`](abencds_extend_view.md). The character `@` must be placed in front of the name `annotation` of the annotation. The annotation should be defined as a CDS object in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). In the annotation definition, the annotation `@Scope` should be used with the value `#EXTEND_VIEW`.

For `annotation`, both [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) and [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be specified that are available for this scope. For framework-specific annotations, refer to [Framework-Specific Annotation Syntax](../abap-cds-annotations/abencds_annotations_frmwrk_tables.md).

The following is a list of the ABAP annotations for the current scope:

- AbapCatalog Annotations

  - [`AbapCatalog.sqlViewAppendName`](../abap-cds-annotations/abencds_873797739_anno.md)

## Hints

- Each definition of a CDS view extension must contain the ABAP annotation `AbapCatalog.sqlViewAppendName` that defines the name of the DDIC append view in ABAP Dictionary.

- The name given to the DDIC append view can no longer be changed after the CDS view extension is transported into a follow-on system.
