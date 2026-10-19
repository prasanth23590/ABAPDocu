---
title: "sql_win - win_func"
source_file: abensql_win_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_win"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_win - win_func

## Syntax

``` abap
... AVG( col [AS dtype] ) 
  | MEDIAN( sql_exp ) 
  | MAX( sql_exp ) 
  | MIN( sql_exp ) 
  | SUM( sql_exp ) 
  | STDDEV( sql_exp ) 
  | VAR( sql_exp ) 
  | CORR( sql_exp1,sql_exp2 ) 
  | CORR_SPEARMAN( sql_exp,sql_exp2 ) 
  | COUNT( sql_exp ) 
  | COUNT( * ) 
  | COUNT(*) 
  | ROW_NUMBER( ) 
  | RANK( ) 
  | DENSE_RANK( ) 
  | NTILE( n ) 
  | LEAD|LAG( sql_exp1[, diff[, sql_exp2]] ) 
  | FIRST_VALUE|LAST_VALUE( col|sql_null ) ...  
```

[`AVG`](abapselect_aggregate.md) · [`col`](abenabap_sql_columns.md) · [`AS dtype`](abapselect_avg_as.md) · [`MEDIAN`](abapselect_aggregate.md) · [`sql_exp`](abapsql_expr.md) · [`MAX`](abapselect_aggregate.md) · [`sql_exp`](abapsql_expr.md) · [`MIN`](abapselect_aggregate.md) · [`sql_exp`](abapsql_expr.md) · [`SUM`](abapselect_aggregate.md) · [`sql_exp`](abapsql_expr.md) · [`STDDEV`](abapselect_aggregate.md) · [`sql_exp`](abapsql_expr.md) · [`VAR`](abapselect_aggregate.md) · [`sql_exp`](abapsql_expr.md) · [`CORR`](abapselect_aggregate.md) · [`sql_exp1`](abapsql_expr.md) · [`sql_exp2`](abapsql_expr.md) · [`CORR_SPEARMAN`](abapselect_aggregate.md) · [`sql_exp`](abapsql_expr.md) · [`sql_exp2`](abapsql_expr.md) · [`COUNT`](abapselect_aggregate.md) · [`sql_exp`](abapsql_expr.md) · [`COUNT`](abapselect_aggregate.md) · [`COUNT`](abapselect_aggregate.md) · [`sql_exp1`](abapsql_expr.md) · [`sql_exp2`](abapsql_expr.md) · [`col`](abenabap_sql_columns.md) · [`sql_null`](abensql_null.md)

### Variant

[1. `... AVG( ... ) | ... | COUNT(*)`](abensql_win_func.md#variant-1)

[2. `... ROW_NUMBER( )`](abensql_win_func.md#variant-2)

[3. `... RANK( )`](abensql_win_func.md#variant-3)

[4. `... DENSE_RANK( )`](abensql_win_func.md#variant-4)

[5. `... NTILE( n )`](abensql_win_func.md#variant-5)

[6. `... LEAD|LAG( sql_exp1[, diff[, sql_exp2]] )`](abensql_win_func.html#variant-6)

[7. `... FIRST_VALUE|LAST_VALUE( col|sql_null )`](abensql_win_func.md#variant-7)

## Overview

### Description

[Window function](../../abap-glossary/abenwindow_function_glosry.md) in a [window expression](abapselect_over.md). Window functions are:

- [Aggregate functions](../../abap-glossary/abenaggregate_function_glosry.md) `AVG( ... )`, ..., `COUNT(*)` that can also be used in [aggregate expressions](abapselect_aggregate.md).

- [Ranking functions](../../abap-glossary/abenranking_function_glosry.md) `ROW_NUMBER( )`, `RANK( )`, `DENSE_RANK( )`, and `NTILE (n)` that can only be used in [window expressions](abapselect_over.md).

- [Value functions](../../abap-glossary/abenvalue_function_glosry.md) `LEAD( ... )`, `LAG( ... )`, `FIRST_VALUE ( ... )`, `LAST_VALUE ( ... )` that can be used only in [window expressions](abapselect_over.md).

## Variant 1

`... AVG( ... ) | ... | COUNT(*)`

### Description

Specifies one of the aggregate functions [`AVG`](abensql_agg_func.md), [`MEDIAN`](abensql_agg_func.md), [`MAX`](abensql_agg_func.md), [`MIN`](abensql_agg_func.md), [`STDDEV`](abensql_agg_func.md), [`VAR`](abensql_agg_func.md), [`CORR`](abensql_agg_func.md), [`CORR_SPEARMAN`](abensql_agg_func.md), [`SUM`](abensql_agg_func.md), [`COUNT`](abensql_agg_func.md), or [`COUNT(*)`](abensql_agg_func.md) as a window function. The aggregate functions evaluate the rows of the current window or of the frame defined by an addition `ORDER BY` after [`OVER`](abapselect_over.md). The aggregate functions are applied as in the [general description](abensql_agg_func.md), with the following differences:

- The addition `DISTINCT` is only allowed for the aggregate function `COUNT` in a window expression.

- The result of the function `COUNT` has the data type `INT8` and not `INT4`.

- When used in window expressions, `STDDEV` and `VAR` can have only data type `FLTP` as argument.

The same applies to the arguments of aggregate functions as in the [general description](abensql_agg_func.md), with the difference that the argument of an aggregate function in a window expression can itself, as a window function, be an aggregate function. This is the precise case when a grouping is made using the [`GROUP BY`](abapgroupby_clause.md) clause in the current query. The windows on the combined result set are then defined and the aggregate expressions allowed as specified columns of the current [`SELECT` list](abapselect_list.md) can be used either as standalone expressions or as part of an SQL expression as an argument of window functions of the window expressions there. A window function then determines its result from the aggregated values of the rows of the current window.

### Executable Example

[Window Expressions with Grouping](abensql_expr_over_group_abexa.md)

## Variant 2

`... ROW_NUMBER( )`

### Description

Specifies the ranking function `ROW_NUMBER` as a window function. This ranking function assigns each row a row number of the data type `INT8` and does not have an argument. The rows of each window are numbered starting with 1. This numbering takes place in the order in which the rows of a window are processed. The order is either undefined or can be defined by specifying the addition `ORDER BY` after [`OVER`](abapselect_over.md).

### Hint

If `ORDER BY` is not specified after [`OVER`](abapselect_over.md), `ROW_NUMBER` still assigns a unique row number, but these numbers are not sorted.

## Executable Examples

[Examples of Window Expressions](abensql_expr_over_abexas.md)

## Variant 3

`... RANK( )`

### Description

Specifies the ranking function `RANK` as a window function. This ranking function assigns each row a rank of the data type `INT8` and does not have an argument. It can only be specified together with `ORDER BY` after [`OVER`](abapselect_over.md).

The rank of a row is the position of this row in the ranking defined by the addition `ORDER BY` after `OVER` and is defined as follows:

- All rows that occur more than once with respect to the sort criterion have the same rank. This rank is the lowest row number in this group, as determined by the function `ROW_NUMBER`.

- The first group of each window starts with the value 1.

### Hint

If a window does not contain any multiple rows with respect to the sort criterion, `RANK` produces the same result as `ROW_NUMBER`. If any other cases, a ranking determined by `RANK` is not gap-free. `DENSE_RANK` can be used to remove gaps.

### Executable Example

[Window Expressions with Sort](abensql_expr_over_order_by_abexa.md)

## Variant 4

`... DENSE_RANK( )`

### Description

Specifies the ranking function `DENSE_RANK` as a window function. This ranking function assigns each row a rank of the data type `INT8` and does not have an argument. It can only be specified together with `ORDER BY` after [`OVER`](abapselect_over.md).

`DENSE_RANK` works in largely the same way as `RANK`, but counts without any gaps, starting from the first group, and does not determine the rank using the lowest row number of groups of identical values with respect to the sort criterion.

### Hint

If a window does not contain any multiple rows with respect to the sort criterion, `DENSE_RANK` produces the same result as `RANK`.

### Executable Example

[Window Expressions with Sort](abensql_expr_over_order_by_abexa.md)

## Variant 5

`... NTILE( n ) OVER( [PARTITION BY sql_exp1] ORDER BY col [ASCENDING|DESCENDING]) ...`

### Description

Specifies the ranking function `NTILE` as a window function. This window function divides the rows of a window into `n` buckets. The goal is to fill all buckets with the same number of rows by following the rule specified after `ORDER BY`.

If the number of rows of the window `m` cannot be distributed equally between the number of buckets `n`, the remainder `r` is distributed in such a way that the first (m [`MOD`](../abap-processing-internal-data/abenarith_operators.md) n) buckets each contain one element more. The buckets are numbered starting with the start value 1 and the result of the `NTILE` function is the number of the bucket a particular row belongs to.

`n` must be a [host variable](abenabap_sql_host_variables.md), a [host expression](abenabap_sql_host_expressions.md), or a [literal](abenabap_sql_literals.md) of type `b`, `s`,`i`, or `int8` which represents a positive integer. The [`OVER`](abapselect_over.md) clause including `ORDER BY` is mandatory.

If `n` is negative, for literals and host constants, a syntax error occurs. If `n` is a variable or an expression, instead of a syntax error, a database error and its respective exception `CX_SY_OPEN_SQL_DB` can occur. The result of the `NTILE` function is always of type `INT8`.

### Hint

Since the maximum number of rows in a bucket can vary by 1, rows with the same value can also be in different buckets.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Sorting of all employees listed in table `DEMO_EMPLOYEES` by their salary and distributes them into five salary groups. Group 1 has one entry more, as the number of employees (11) cannot be distributed into five groups of equal size.

``` abap
SELECT name, 
       salary, 
       NTILE( 5 ) OVER( ORDER BY salary ) AS ntile 
       FROM demo_employees 
       INTO TABLE @FINAL(result).
```

### Executable Example

[Window Function `NTILE`](abensql_expr_over_ntile_abexa.md)

## Variant 6

`... LEAD|LAG( sql_exp1[, diff[, sql_exp2]]`

### Description

Specifies one of the value functions `LEAD` or `LAG` as a window function. They can only be specified together with `ORDER BY` after [`OVER`](abapselect_over.md).

The result of the functions is the value of the SQL expression [`sql_exp1`](abapsql_expr.md) for the row of the current window defined by the addition `diff` or the box defined by the addition `ORDER BY` after [`OVER`](abapselect_over.md). For `diff`, a [literal](abenabap_sql_literals.md) or a [host constant](abenabap_sql_host_variables.md) with the ABAP type `b`, `s`, `i`, `int8` can be specified, whose value is a positive number other than 0.

- For the function `LEAD`, `diff` determines the row positioned in a corresponding distance after the current row.

- For the function `LAG`, `diff` determines the row positioned in a corresponding distance in front of the current row.

If `diff` is not specified, the value 1 is used implicitly. In the case of `LEAD`, this is the row that follows directly and in the case of `LAG`, the directly preceding row. If the row determined by `diff` is not in the current window, the result is the [null value](../../abap-glossary/abennull_value_glosry.md) by default. If the optional SQL expression [`sql_exp2`](abapsql_expr.md) is specified, it is evaluated and returned for the current row in cases where the row does not exist.

The result of the functions `LEAD` and `LAG` has the following data type:

- If [`sql_exp2`](abapsql_expr.md) is not specified, the data type is determined by [`sql_exp1`](abapsql_expr.md).

- If [`sql_exp2`](abapsql_expr.md) is specified, the results of `sql_exp1` and `sql_exp2` must match in a way that a common result type can be determined: The data types must either be the same or the data type of an expression must represent the value of the other expression. The result has the dictionary type of the expression with the largest value range.

### Hints

- The window functions `LEAD` or `LAG` are suitable for calculations, such as determining the difference between values in the current row and values of the preceding or following rows.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

`SELECT` statement with the window functions `LEAD` and `LAG` as operands of an [arithmetic expression](abensql_arith.md). The addition [`PARTITION BY`](abapselect_over.md) is not specified, which means there is only one window with all rows of the result set. Both `LEAD` and `LAG` have only one argument each, which means that the difference between the values of the column `NUM1` is calculated using the directly following or preceding row, and any nonexistent rows produce null values. The latter are defined using a [null indicator](../../abap-glossary/abennull_indicator_glosry.md). The class `CL_DEMO_SELECT_OVER_LEAD_LAG_D` uses this `SELECT` statement and displays the result.

``` abap
SELECT num1 AS number, 
       num1 - LEAD( num1 ) OVER( ORDER BY id ) AS diff_lead, 
       num1 - LAG(  num1 ) OVER( ORDER BY id ) AS diff_lag 
       FROM demo_expressions 
       ORDER BY id 
       INTO TABLE @FINAL(lead_lag_diffs) 
                  INDICATORS NULL STRUCTURE null_ind.
```

### Executable Example

[Window Functions `LEAD` and `LAG`](abensql_expr_over_lead_lag_abexa.md)

## Variant 7

`... FIRST_VALUE|LAST_VALUE( col|sql_null )`

### Description

Specifies one of the value functions `FIRST_VALUE` or `LAST_VALUE` as a window function. The `FIRST_VALUE` function returns the first value of a sorted set of values, the `LAST_VALUE` function returns the last value of a sorted set of values.

If the value is null or if the expression is empty, null is returned (see example, row `H`).

`OVER` and `ORDER BY` are mandatory. `PARTITION BY` is optional. If a window is divided into partitions, the `FIRST_VALUE`/`LAST_VALUE` function returns a result for each partition (see example). If there is no `PARTITON BY` clause, the functions work on the entire window.

With the `LAST_VALUE` function, framing is an important aspect to consider. The default frame is [`ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`](abapselect_over.md), so the `LAST_VALUE` function always returns the value from the current row. To find the last value for a partition or a window, the correct frame has to be specified explicitly: [`ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`](abapselect_over.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The class `CL_DEMO_SELECT_FIRST_LAST` divides the rows from the `DEMO_UPDATE` table into three partitions, depending on their value in `COL1`. Within the partitions, the rows are ordered by their value in `COL3`.

The column `FIRST_VALUE` returns the first value of `COL2` for each partition.

The column `LAST_VALUE` does not return the last value. As described above, the default frame is from the first row to the current row. If `COL3` contains duplicate values, the rows are considered equal and the last value from the group of equals is returned. To get the last value of `COL2` of the partition, the frame size has to be specified explicitly, as demonstrated in `LAST_VALUE_CORRECT`.

In this example, `COL3` has multiple duplicate values. The key field - here the field `ID` - is used to sort rows with the same value.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT 
      id, 
      col1, 
      col2, 
      col3, 
      FIRST_VALUE( col2 ) OVER( PARTITION BY col1 ORDER BY col3 ) 
                  AS first_value, 
      LAST_VALUE( col2 ) OVER( PARTITION BY col1 ORDER BY col3 ) 
                  AS last_value, 
      LAST_VALUE( col2 ) OVER( PARTITION BY col1 ORDER BY col3 
                  ROWS BETWEEN UNBOUNDED PRECEDING 
                  AND UNBOUNDED FOLLOWING ) 
                  AS last_value_correct 
      FROM demo_update 
      INTO TABLE @FINAL(result). 
 
out->display( result ).
```

  
![figure](images_abdoc_first_last_value.png)
