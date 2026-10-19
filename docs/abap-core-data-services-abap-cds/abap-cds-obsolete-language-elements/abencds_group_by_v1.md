---
title: "CDS DDL - DDIC-Based View, SELECT, GROUP BY"
source_file: abencds_group_by_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, SELECT, GROUP BY

## Syntax

``` abap
... GROUP BY field1, field2, ... 
             path_expr1, path_expr2, ...  
```

[`path_expr1`](abencds_path_expression_v1.md) · [`path_expr2`](abencds_path_expression_v1.md)

## Description

Groups those rows in the result set of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) that have the same content in the elements specified by the fields `field1`, `field2`, ... or [path expressions](abencds_path_expression_v1.md) `path_expr1`, `path_expr2` ... as a single row. The fields must be specified using the same names as the fields in the data source [`data_source`](abencds_data_source_v1.md). It is not allowed to use the alias names defined in the current CDS view using with [`AS`](abencds_select_list_entry_v1.md).

The `GROUP BY` clause is mandatory if the `SELECT` list contains any aggregate expressions. All elements that are **not** defined using an aggregate expression must be listed after `GROUP BY`. Literals and other expressions cannot be specified after `GROUP BY`.

When the CDS view is accessed, the results of the aggregate expressions are calculated from the values of the corresponding fields of the combined rows and the results are placed in the element of the resulting row in the result set.

The fields specified after `GROUP BY` cannot be of the [type](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) `LCHR`, `LRAW`, `STRING`, `RAWSTRING`, or `GEOM_EWKB`.

## Hint

A [`WHERE` condition](abencds_where_clause_v1.md) is evaluated before the rows are combined using `GROUP BY`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

When a CDS view is accessed, the view returns `sales_order` for every role of a business partner and returns the number of business partners and the total of all gross amounts for every currency.

``` abap
@AbapCatalog.sqlViewName: 'SALES_ORDER_VW' 
define view sales_order as 
  select from snwd_so 
    inner join 
      snwd_bpa on buyer_guid = snwd_bpa.node_key 
      { bp_role as role, //e.g. customer or supplier 
        count(distinct buyer_guid) as partners_count, 
        @Semantics.currencyCode snwd_so.currency_code, 
        @Semantics.amount.currencyCode: 'currency_code' 
          sum(snwd_so.gross_amount) as sum_gross_amount } 
      group by bp_role, snwd_so.currency_code;
```
