---
title: "CDS DDL - element_annot, Transactional Query"
source_file: abencds_element_annotations_pv.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries > CDS DDL - projection_list, Transactional Query > CDS DDL - proj_element, Transactional Query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - element_annot, Transactional Query

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) in the definition of an element of a projection list in a CDS projection view as element annotation. Element annotations must be specified before the element they belong to, and the character `@` must be placed in front of the name `annotation` of the annotation.

For CDS projection views, there are strict checks that all element annotations used must be defined as a [CDS object](../../abap-glossary/abencds_object_glosry.md) in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). Otherwise, a syntax error occurs.

All available element annotations are listed in topic [`element_annot`](abencds_f1_element_annotation.md).

**Propagation of Element Annotations in CDS Projection Views**

- Projected elements and exposed associations from the projected entity inherit the element annotations from the projected entity. Any annotations defined in the projected CDS entity `cds_entity` at element level are passed to the CDS projection view `projection_view`. This means that the CDS projection view has the same annotation values as the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). Only if an annotation is defined explicitly for the same element in the CDS projection view, the values are overwritten and only the new values are valid for the element in question. [Framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) can be used to give the element specific semantic properties for other SAP frameworks.

  If you use an annotation with an element reference `ElementRef` in the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) and the reference element is aliased in the projection entity, the reference is not drawn to the element in the projection view, due to the name change. In such a case, you have to redefine the annotation in the projection view and use the alias name of the element in the annotation value. **Exception:** In an analytical projection view, the annotation `Aggregation.default` that defines an analytical measure is inherited from the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) and it cannot be overwritten.

- If a field is not directly projected but used in an expression or built-in function, element annotations are not inherited.

  **Exception:** If a field is used in the [`CAST PRESERVING TYPE`](abencds_cast_expression_v2.md) expression, element annotations are inherited.

- Inheritance of element annotations can be switched off by using the header annotation [`@Metadata.ignorePropagatedAnnotations`](abencds_proj_view_annotations.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS projection view `DEMO_SALES_PV_SO_I_LIST` is a projection of the CDS view `DEMO_SALES_CDS_SO_I`. Even though the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) uses a semantics annotation to connect the gross amount to the currency and the quantity field to the respective unit, the projection view repeats these annotations. This is required because of the alias name of the currency and unit fields.
