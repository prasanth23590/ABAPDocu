---
title: "sql_agg - ALLOW_PRECISION_LOSS"
source_file: abapselect_allow_precision_loss.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_agg > sql_agg - agg_func"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_agg - ALLOW_PRECISION_LOSS

## Syntax

``` abap
... ALLOW_PRECISION_LOSS( SUM( [DISTINCT] sql_exp ) )  
```

[`SUM`](abensql_agg_func.md) · [`sql_exp`](abapsql_expr.md)

## Description

The `ALLOW_PRECISION_LOSS` statement can improve the performance of an [aggregate expression](../../abap-glossary/abenaggregate_expression_glosry.md) [`agg_exp`](abapselect_aggregate.md) at the cost of accuracy of the result. This function should only be used on decimal values and when loss of precision is acceptable. Currently, [`SUM`](abensql_agg_func.md) is the only supported aggregate expression.

## Hint

A different result is not necessarily obtained when using the `ALLOW_PRECISION_LOSS` statement to sum up decimal values. A different result and simultaneous improvement in performance is only obtained during certain complex operations. One example is when operations are carried out in a different order to reduce the total number of operations. See the executable example below for further details.

## Executable Example

[Aggregate function, allow precision loss](abensql_expr_aggr_prec_loss_abexa.md)
