---
title: "ABAP SQL - SQL Expressions sql_exp"
source_file: abapsql_expr.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - SQL Expressions sql_exp

## Syntax

``` abap
... sql_elem 
  | sql_func 
  | cds_scalar_func 
  | sql_arith 
  | sql_cast 
  | sql_string 
  | sql_case 
  | sql_agg 
  | sql_win 
  | sql_null ...  
```

[`sql_elem`](abensql_elem.md) · [`sql_func`](abensql_builtin_func.md) · [`cds_scalar_func`](abensql_cds_scalar_func.md) · [`sql_arith`](abensql_arith.md) · [`sql_cast`](abensql_cast.md) · [`sql_string`](abensql_string.md) · [`sql_case`](abensql_case.md) · [`sql_agg`](abapselect_aggregate.md) · [`sql_win`](abapselect_over.md) · [`sql_null`](abensql_null.md)

## Description

SQL expressions are expressions that generally can be specified in the following positions of ABAP SQL statements:

- As [columns specified](abapselect_clause_col_spec.md) in the [`SELECT` list](abapselect_list.md)

- As arguments of certain [aggregate functions](abapselect_aggregate.md) in the [`SELECT` list](abapselect_list.md) and in the [`HAVING` clause](abaphaving_clause.md)

- As operands of [SQL conditions](abenasql_cond.md):

  - On the left side of an [SQL condition for statements](abenabap_sql_stmt_logexp.md)

  - On the left and right side of an [SQL condition for expressions](abenabap_sql_expr_logexp.md)

- As a grouping criterion after [`GROUP BY`](abapgroupby_clause.md)

- As a sort criterion after [`ORDER BY`](abaporderby_clause.md)

- As a window criterion after [`PARTITION BY`](abapselect_over.md)

Some expressions, such as `CAST` expressions, can also be specified at other positions and built-in functions can be specified on the right side of SQL conditions for statements. This is documented for the respective positions.

SQL expressions are passed to the database system, executed there, and the result is passed to the AS ABAP if requested.

In general, the operands of SQL expressions can also be SQL expressions whose result must have a suitable data type. There are restrictions to individual operand positions, which are described for these.

The following SQL expressions exist:

- [Elementary SQL expressions](abensql_elem.md)

- [Calls of built-in SQL functions](abenabap_sql_functions.md)

- [Arithmetic expressions](abensql_arith.md)

- [Cast expressions](abensql_cast.md)

- [String expressions](abensql_string.md)

- [Case distinctions](abensql_case.md)

- [Aggregate expressions](abapselect_aggregate.md)

- [Window expressions](abapselect_over.md)

- [Null expressions](abensql_null.md)

Every expression can be enclosed in [parentheses](abensql_exp_parentheses.md). The result of an expression is used in the ABAP SQL statement in accordance with the operand position, with the data type in nested expressions based on the outermost expression.

## Hints

- No alias names defined using [`AS`](abapselect_list.md) can be used as operands of SQL expressions. This also means that none of the expressions used in a `SELECT` list can be specified as operands using their alias names.

- SQL expressions cannot currently be used together with the addition [`FOR ALL ENTRIES`](abenwhere_all_entries.md). An exception to this rule are individual columns and an individually specified aggregate expression `COUNT( * )`.

- [Certain SQL expressions](abensql_engine_expr.md) can be calculated by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). If any other SQL expressions are used, [table buffering](../../abap-glossary/abentable_buffering_glosry.md) is bypassed and internal tables accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Syntax example for specifying SQL expressions in different operand positions in a [`SELECT`](abapselect.md) statement.

``` abap
SELECT FROM sflight 
       FIELDS CONCAT( carrid, connid )   AS key, 
              MAX( seatsmax - seatsocc ) AS max_free, 
              MIN( seatsmax - seatsocc ) AS min_free 
        GROUP BY carrid, connid 
        HAVING SUM( seatsmax - seatsocc ) > 100 
        ORDER BY key 
        INTO TABLE @FINAL(itab).
```
