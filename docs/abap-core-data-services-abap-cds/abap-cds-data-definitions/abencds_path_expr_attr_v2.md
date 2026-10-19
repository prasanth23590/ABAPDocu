---
title: "CDS DDL - CDS View Entity, path_expr, attributes"
source_file: abencds_path_expr_attr_v2.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - View Entities > CDS DDL - DEFINE VIEW ENTITY > CDS DDL - CDS View Entity, SELECT > CDS DDL - SELECT, CDS View Entity, Operands and Expressions > CDS DDL - CDS View Entity, path_expr"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS View Entity, path_expr, attributes

## Syntax

``` abap
... [ [cardinality] [INNER|{LEFT OUTER}] [WHERE] [cds_cond] ] ...  
```

[`[cardinality]`](abencds_path_expr_card_v2.md) · [`[INNER|{LEFT OUTER}]`](abencds_path_expr_jointype_v2.md) · [`[WHERE] [cds_cond]`](abencds_path_expression_filter_v2.md)

## Description

For every CDS association [`_assoc`](abencds_association_v2.md) of a [path expression](abencds_path_expression_v2.md) of a [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md), attributes for this part of the path expression can be defined in square brackets `[ ]`. The following attributes can be specified:

- With [`cardinality`](abencds_path_expr_card_v2.md), the [cardinality](../../abap-glossary/abencardinality_glosry.md) of the section can be specified.

- With [`INNER|{LEFT OUTER}`](abencds_path_expr_jointype_v2.md) the [join type](../../abap-glossary/abenjoin_type_glosry.md) can be specified.

- With [`[WHERE] cds_cond`](abencds_path_expression_filter_v2.md) a filter condition `cds_cond` can be specified.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view entity contains path expressions with filter conditions in the `FROM` clause, in the `SELECT` list, and in the `WHERE` clause.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_SALES_CDS_PATH_EXPR_1
  as select from
    DEMO_SALES_CDS_SO_I._SalesOrder 
      [lifecycle_status <> 'C' and lifecycle_status <> 'X']
    association to exact one demo_so_inv_he as _invoice_header
      on DEMO_SALES_CDS_SO.id = _invoice_header.buyer_id
    {
      key so_key as soKey,
          lifecycle_status,
          _invoice_header.dunning_level,
          DEMO_SALES_CDS_SO._Buyer,
          DEMO_SALES_CDS_SO[inner].buyer_id,
          DEMO_SALES_CDS_SO.id
    }
    where
      _invoice_header.dunning_level > '0' and
      _Items[to one:currency <> 'EUR'].material = 'WOOD'
```
