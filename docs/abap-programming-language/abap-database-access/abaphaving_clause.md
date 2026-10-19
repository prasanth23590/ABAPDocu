---
title: "SELECT, HAVING"
source_file: abaphaving_clause.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, HAVING

## Syntax

``` abap
... HAVING sql_cond ...  
```

[`sql_cond`](abenasql_cond.md)

## Description

The addition `HAVING` limits the number of rows in groups in the result set of a [query](../../abap-glossary/abenasql_query_glosry.md) by using the logical expression `sql_cond` on these rows. The logical expression evaluates the content of row groups. Those rows are placed in the result set for which the logical expression is true.

The following applies to the operands of the relational expressions of the logical expression [`sql_cond`](abenabap_sql_stmt_logexp.md):

- Non-aggregated [columns](abenabap_sql_columns.md) used as operands in the [data sources](abapselect_data_source.md) specified after [`FROM`](abapfrom_clause.md) do not have to be listed as such in the [`SELECT` list](abapselect_list.md) and are listed after the addition [`GROUP BY`](abapgroupby_clause.md) instead. For each group, the value used for the grouping is evaluated.

- If [SQL expressions](abapsql_expr.md) are used on the left side, either the same expression must be specified or all non-aggregated columns of the expression must be specified individually after [`GROUP BY`](abapgroupby_clause.md).

- In a `HAVING` condition, aggregate expressions [`sql_agg`](abapselect_aggregate.md) can be used directly or as operands of SQL expressions on both sides of comparisons. Columns that are specified as the argument of an aggregate expression directly or via an SQL expression do not need to be listed after `GROUP BY`. This kind of aggregate expression is evaluated for each row group defined in `GROUP BY` and its result is used as an operand in the comparison. The aggregate functions of the [`SELECT` list](abapselect_list.md) and the `HAVING` clause and the SQL expressions specified as arguments here do not need to be the same.

If a `HAVING` clause is specified, all columns in the [`SELECT` list](abapselect_list.md) that are not arguments of [aggregate expressions](abapselect_aggregate.md) here must be specified after [`GROUP BY`](abapgroupby_clause.md). If the [`SELECT` list](abapselect_list.md) is specified as `*`, `HAVING` clauses without [`GROUP BY` clauses](abapgroupby_clause.md) cannot be used.

[Implicit ABAP SQL client handling](abenabap_sql_client_handling.md) applies to the `HAVING` clause. The [client column](../../abap-glossary/abenclient_column_glosry.md) of a client-dependent data source cannot be used as an operand in the `HAVING` condition.

## Hints

- Aggregate expressions on the left side of a logical expression after `HAVING` are SQL expressions. Thus, all SQL expressions except for window expressions can be specified there. Aggregate expressions on the right side of a logical expression are an exception to the rule that no SQL expressions can be specified here.

- Columns that are specified as arguments of aggregate expressions after `HAVING` can also be specified after `GROUP BY`.

- If the addition `GROUP BY` is not specified or the data object `column_syntax` in the dynamic column specification after `GROUP BY` is initial, the addition `HAVING` can only be specified if the entire result set is grouped into a row, that is, if there are only aggregate expressions specified after `SELECT`. In this case, only those aggregate expressions can be specified as operands in `sql_cond` that are evaluated for all rows in the result set.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the number of bookings in each class and for each flight date of a connection.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: carrid TYPE sbook-carrid VALUE 'LH', 
      connid TYPE sbook-connid VALUE '400'. 
 
cl_demo_input=>new( 
  )->add_field( CHANGING field = carrid 
  )->add_field( CHANGING field = connid )->request( ). 
 
SELECT fldate, class, COUNT( * ) AS class_cnt 
       FROM sbook 
       WHERE connid = @connid 
       GROUP BY carrid, fldate, class 
       HAVING carrid = @carrid 
       ORDER BY fldate, class 
       INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```

## Executable Example

[SQL Expressions, Use in Aggregate Expressions](abensql_expr_in_aggregates_abexa.md)
