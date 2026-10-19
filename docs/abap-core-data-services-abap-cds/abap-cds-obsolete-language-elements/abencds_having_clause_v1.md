---
title: "CDS DDL - DDIC-Based View, SELECT, HAVING"
source_file: abencds_having_clause_v1.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Obsolete Language Elements > Obsolete CDS Entities > ABAP CDS - DDIC-Based Entities (Obsolete) > ABAP CDS - DDIC-Based Views (Obsolete) > CDS DDL - DEFINE VIEW ddic_based > CDS DDL - DDIC-Based View, SELECT > CDS DDL - DDIC-Based View, SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DDIC-Based View, SELECT, HAVING

## Syntax

``` abap
... HAVING cds_cond ...  
```

[`cds_cond`](abencds_conditional_expression_v1.md)

## Description

Defines a `HAVING` condition for the result set of a [CDS DDIC-based view (obsolete)](../../abap-glossary/abencds_v1_view_glosry.md) after a [`GROUP BY` clause](abencds_group_by_v1.md) is evaluated. A `HAVING` condition can only be specified together with `GROUP BY`. For the operands, [general](abencds_cond_expr_operands_v1.md) and [special rules](abencds_cond_expr_having_v1.md) apply when specifying the condition.

Removes all rows from the result set that do not meet the condition [`cds_cond`](abencds_conditional_expression_v1.md) specified after `HAVING`.

## Hint

[Aggregate expressions](abencds_aggregate_functions_v1.md) can be specified in the `HAVING` condition, which is not possible in the [`WHERE` condition](abencds_where_clause_v1.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

When accessed, the CDS view `sales_order` returns the number of business partners for each business partner role in which the total gross amount in euros is greater than `100000.00`.

``` abap
@AbapCatalog.sqlViewName: 'SALES_ORDER_VW' 
define view sales_order as 
  select from snwd_so 
    inner join 
      snwd_bpa on buyer_guid = snwd_bpa.node_key 
  {  key bp_role as role, //e.g. customer or supplier 
     count(distinct buyer_guid) as partners_count, 
     sum(snwd_so.gross_amount) as sum_gross_amount } 
  where snwd_so.currency_code = 'EUR' 
  group by bp_role 
  having sum(snwd_so.gross_amount) > 100000.00;
```
