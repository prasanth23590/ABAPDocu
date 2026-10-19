---
title: "sql_exp - sql_agg"
source_file: abapselect_aggregate.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - sql_agg

## Syntax

``` abap
... agg_func ...  
```

[`agg_func`](abensql_agg_func.md)

## Description

[Aggregate expression](../../abap-glossary/abenaggregate_expression_glosry.md) in ABAP SQL. An aggregate expression consists of an [aggregate function](../../abap-glossary/abenaggregate_function_glosry.md) [`agg_func`](abensql_agg_func.md) that aggregates the values of multiple rows of the result set of a [query](../../abap-glossary/abenasql_query_glosry.md) into a single value. It can be used in the following operand positions:

- As an [SQL expression](abapsql_expr.md) for

  - a column [`col_spec`](abapselect_clause_col_spec.md) of the result set in the [`SELECT` list](abapselect_list.md) of a [query](../../abap-glossary/abenasql_query_glosry.md),

  - an operand on the left side of [relational expressions](abenabap_sql_stmt_logexp.md) of the condition [`sql_cond`](abenasql_cond.md) of the [`HAVING`](abaphaving_clause.md) clause of a [query](../../abap-glossary/abenasql_query_glosry.md).

    Here, an aggregate expression can be specified directly or as an operand of an [SQL expression](abapsql_expr.md) except for another aggregate expression.

- As an operand on the right side of [relational expressions](abenabap_sql_stmt_logexp.md) of the condition [`sql_cond`](abenasql_cond.md) of the [`HAVING`](abaphaving_clause.md) clause of a [query](../../abap-glossary/abenasql_query_glosry.md). Here, no SQL expressions can be used except for directly specified aggregate expressions.

All [aggregate functions](abensql_agg_func.md) can be used as an aggregate expression except for `PRODUCT`. An aggregate function used as an aggregate expression can have one of the following arguments:

- An SQL expression [`sql_exp`](abapsql_expr.md) except aggregate expressions and window expressions for the aggregate functions `MAX`, `MIN`, `SUM`, `STRING_AGG`, and `COUNT`.

- A column [`col`](abenabap_sql_columns.md) of a [data source](abapselect_data_source.md) of a [query](../../abap-glossary/abenasql_query_glosry.md) for the aggregate functions `AVG` and `GROUPING`.

The aggregate functions take the values of the column or the results of the SQL expression of multiple rows of the query result set and determine a single value. Either all rows of the result set or the rows of the current group created using [`GROUP BY`](abapgroupby_clause.md) are evaluated. If the value of an aggregate expression is too large for the [target area](abapinto_clause.md), an exception is raised.

## Hints

- The [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) cannot process all aggregate expressions except a standalone `COUNT( * )`, `MAX`, `MIN`, and `SUM` in the `SELECT` list. The ABAP SQL statement bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md), and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Returns the flight date, the number of passengers, and the average and maximum luggage weight of all Lufthansa flights with the flight number 0400.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT FROM sbook 
       FIELDS fldate, 
              COUNT( * ) AS count, 
              AVG( luggweight AS DEC( 16,4 ) ) AS avg, 
              MAX( luggweight ) AS max 
       WHERE carrid = 'LH' AND 
             connid = '0400' 
       GROUP BY fldate 
       INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```

## Executable Examples

- [SQL Expressions, Use in Aggregate Expressions](abensql_expr_in_aggregates_abexa.md)

- [SQL Expressions, Aggregate Expressions in SQL Expressions](abensql_expr_aggr_in_expr_abexa.md)
