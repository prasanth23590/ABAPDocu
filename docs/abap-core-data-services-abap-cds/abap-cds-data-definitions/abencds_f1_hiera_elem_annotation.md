---
title: "CDS DDL - DEFINE HIERARCHY, element_annot"
source_file: abencds_f1_hiera_elem_annotation.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Hierarchies > CDS DDL - DEFINE HIERARCHY > CDS DDL - DEFINE HIERARCHY, element_list > CDS DDL - DEFINE HIERARCHY, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE HIERARCHY, element_annot

## Syntax

``` abap
... @annotation ...   
... @<annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) · [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) in the definition of an [element](abencds_f1_hiera_element.md) of a [CDS hierarchy](../../abap-glossary/abencds_hierarchy_glosry.md) as element notation. Element annotations can be specified before and after the element.

- In front of the element, the character `@` must be placed before the name `annotation` of the annotation.

- Following the element, the characters `@<` must be placed before the name `annotation` of the annotation.

The elements of [CDS entities](../../abap-glossary/abencds_entity_glosry.md) can be assigned to the element annotations grouped under [`element_annot`](abencds_f1_element_annotation.md).
