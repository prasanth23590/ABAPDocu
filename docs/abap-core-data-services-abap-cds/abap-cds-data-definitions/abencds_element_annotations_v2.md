---
title: "CDS DDL - CDS View Entity, SELECT, element_annot"
source_file: abencds_element_annotations_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - CDS View Entity, SELECT, select_list > CDS DDL - CDS View Entity, SELECT, element"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, SELECT, element_annot

## Syntax

``` abap
... @annotation ...  
```

[`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md)

## Description

Specifies an [annotation](../../abap-glossary/abencds_annotation_glosry.md) [`annotation`](../abap-cds-annotations/abencds_annotations_syntax.md) in the definition of an [element](abencds_select_list_entry_v2.md) of a [`SELECT` list](abencds_select_list_v2.md) in a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) as element annotation. Element annotations must be specified before the element they belong to, and the character `@` must be placed in front of the name `annotation` of the annotation.

For CDS view entities, there are strict checks that all element annotations used must be defined as a [CDS object](../../abap-glossary/abencds_object_glosry.md) in a [CDS annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md). Otherwise, a syntax error occurs.

All available element annotations are listed in topic [`element_annot`](abencds_f1_element_annotation.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

In the CDS view entity `DEMO_SALES_CDS_ELEM_ANNOT`, a short text and a tooltip are assigned to the element `given_name`.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_SALES_CDS_ELEM_ANNOT
  as select from
                 demo_sales_bupa
      inner join demo_sales_order as sales_order
        on demo_sales_bupa.id = sales_order.id
    {
      key demo_sales_bupa.id,
          demo_sales_bupa.gender,
          demo_sales_bupa.title,
          @EndUserText.label: 'First name'
          @EndUserText.quickInfo: 'Customer''s first name'
          demo_sales_bupa.given_name
    }
    where
      demo_sales_bupa.gender = 'f'
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how element annotations are passed on between views via [CDS associations](../../abap-glossary/abencds_association_glosry.md). The following CDS view entity defines and exposes a CDS association `_some_assoc`:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_ASSOC_ANNO2_VE
  as select from demo_join2
  association to many demo_join3 as _some_assoc 
    on _some_assoc.l = demo_join2.d
{
  key d,
      @EndUserText.label: 'Association to demo_join3'
      _some_assoc
}
```

A further CDS view entity accesses the view and also exposes the CDS association. Here, the annotation `@EndUserText.label` is inherited.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_ASSOC_ANNO1_INH_VE
  as select from Demo_Cds_Assoc_Anno2
{
  key d,
      _some_assoc
}
```

The following CDS view entity defines and exposes its own CDS association `_some_assoc`. In this case, the CDS annotation `@EndUserText.label` is not inherited.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_CDS_ASSOC_ANNO1_LOC_VE
  as select from Demo_Cds_Assoc_Anno2
  association to many demo_join1 as _some_assoc 
    on Demo_Cds_Assoc_Anno2.d = _some_assoc.d
{
  key d,
      _some_assoc
}
```

If the CDS association `_some_assoc` was exposed from `DEMO_CDS_ASSOC_ANNO2_VE` instead of or in addition to `_some_assoc` by specifying the name `Demo_Cds_Assoc_Anno2_ve._some_assoc` explicitly, the annotation would be inherited again. The class `CL_DEMO_CDS_ASSOC_ANNO_VE` evaluates the annotations of both views. No local element annotations are defined for the locally defined association `_some_assoc` of the view `DEMO_CDS_ASSOC_ANNO1_LOC_VE`, which means that the result for this CDS association is empty.
