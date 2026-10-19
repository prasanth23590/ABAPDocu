---
title: "CDS DCL - DEFINE ASPECT, aspect_annot"
source_file: abencds_f1_dcl_as_annotations.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Access Control > ABAP CDS - DCL Statements > CDS DCL - DEFINE ACCESSPOLICY > CDS DCL - DEFINE ASPECT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DCL - DEFINE ASPECT, aspect_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) in the definition of an aspect [`DEFINE ASPECT`](abencds_f1_define_generic_aspect.md). The character `@` must be placed in front of the name `annotation` of the annotation.

The following [ABAP annotations](../../abap-glossary/abenabap_annotation_glosry.md) can be specified for `annotation`. No other annotations can be specified.

- EndUserText Annotations

  - [`EndUserText.label`](../abap-cds-annotations/abencds_924137870_anno.md)
