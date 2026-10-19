---
title: "CDS DDL - DDIC-Based View, SELECT, WHERE"
source_file: abencds_where_clause_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, SELECT, WHERE

## Syntax

``` abap
... WHERE cds_cond ...  
```

[`cds_cond`](abencds_conditional_expression_v1.md)

## Description

Defines a `WHERE` condition for the result set of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md). When the CDS view is accessed, the result set contains only the data from the data source [`data_source`](abencds_data_source_v1.md) that meets the condition [`cds_cond`](abencds_conditional_expression_v1.md) specified after `WHERE`.

The fields evaluated in the condition do not need to be defined as elements of the CDS view in the [`SELECT` list](abencds_select_list_v1.md). For the operands, [general](abencds_cond_expr_operands_v1.md) and [special rules](abencds_cond_expr_where_v1.md) apply when specifying the condition.

## Hint

Unlike in the [`HAVING` condition](abencds_having_clause_v1.md), [aggregate expressions](abencds_aggregate_functions_v1.md) cannot be specified in the `WHERE` condition.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

When the CDS view `demo_sales_order_old4` is accessed, the result set contains only orders where the company name of the business partner starts with *S* and that were created between January and March 2013.

``` abap
@AbapCatalog.sqlViewName: 'DEMO_SO_VW4'
define view DEMO_SALES_ORDER_OLD4
  as select from snwd_so
  association to snwd_bpa as _partner
    on snwd_so.buyer_guid = _partner.node_key
{
  key   so_id,
        snwd_so.buyer_guid,
        _partner.company_name,
        snwd_so.created_at,
        @Semantics.currencyCode
        currency_code,
        @Semantics.amount.currencyCode: 'currency_code'
        gross_amount
}
where
      _partner.company_name like    'S%'
  and created_at            between 2013010100000.0
      and 20130401000000.0; //Jan-March
```
