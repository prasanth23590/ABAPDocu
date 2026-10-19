---
title: "CDS DDL - CDS DDL Aspect, element, element_annot"
source_file: abencds_element_annotations_aspect.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Aspects > CDS DDL - DEFINE ASPECT > CDS DDL - CDS Aspect, element_list > CDS DDL - CDS Aspect, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS DDL Aspect, element, element_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) in the definition of an [element](abencds_aspect_element.md) of a [element list](abencds_ddl_aspect_element_list.md) in a [CDS DDL aspect](abencds_ddl_aspect_glosry.md) as element annotation. Element annotations must be specified before the element they belong to, and the character `@` must be placed in front of the name `annotation` of the annotation.

For CDS DDL aspects, there are strict checks that all element annotations used must be defined as a [CDS object](../../abap-glossary/abencds_object_glosry.md) in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). Otherwise, a syntax error occurs.

All available element annotations are listed in topic [`element_annot`](abencds_f1_element_annotation.md).
