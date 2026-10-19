---
title: "sql_exp - sql_win"
source_file: abapselect_over.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_exp - sql_win

## Syntax

``` abap
... win_func OVER( [PARTITION BY sql_exp1, sql_exp2 ...] 
                   [ORDER BY col1 [ASCENDING|DESCENDING], 
                             col2 [ASCENDING|DESCENDING] 
                         [ROWS BETWEEN {UNBOUNDED PRECEDING} 
                                      |{CURRENT ROW} 
                                      |{n PRECEDING} 
                                      |{n FOLLOWING} 
                               AND     {UNBOUNDED FOLLOWING} 
                                      |{CURRENT ROW} 
                                      |{n PRECEDING} 
                                      |{n FOLLOWING}]] ) ...  
```

[`win_func`](abensql_win_func.md) · [`sql_exp1`](abapsql_expr.md) · [`sql_exp2`](abapsql_expr.md) · [`col1`](abenabap_sql_columns.md) · [`col2`](abenabap_sql_columns.md)

### Addition

[1. `... ORDER BY col1 [ASCENDING|DESCENDING], col2 [ASCENDING|DESCENDING], ...`](abapselect_over.md#addition-1)

[2. `... ROWS BETWEEN ...`](abapselect_over.md#addition-2)

## Overview

### Description

[Window expression](../../abap-glossary/abenwindow_expression_glosry.md) in ABAP SQL. A window expression uses a [window function](../../abap-glossary/abenwindow_function_glosry.md) to determine an individual value from the rows of a [window](../../abap-glossary/abenwindow_glosry.md) of the result set of a [query](../../abap-glossary/abenasql_query_glosry.md). A window expression can be specified as an [SQL expression](abapsql_expr.md) or as an argument of any SQL expressions for defining a column [`col_spec`](abapselect_clause_col_spec.md) of the result set in the [`SELECT` list](abapselect_list.md) of a query. [Aggregate](abapselect_aggregate.md) expressions can also be nested if there is interest in both the aggregation and windowing in the same query. In each row of the result set, the result of the calculation is placed in the column defined in this way.

A window expression consists of a window function [`win_func`](abensql_win_func.md) followed by the addition `OVER( ... )` in whose parentheses the [window](../../abap-glossary/abenwindow_glosry.md) on the result set is defined for whose rows the window function is evaluated:

- PARTITION BY [`sql_exp1`](abapsql_expr.md), [`sql_exp2`](abapsql_expr.md) ...

  The optional addition `PARTITION BY` defines the windows using a comma-separated list of SQL expressions `sql_exp1`, `sql_exp2`, ... A window is constructed by the rows of the result set for which all SQL expressions have the same result. All [SQL expressions](abapsql_expr.md) except for [aggregate expressions](abapselect_aggregate.md) and window expressions can be used. The window function is calculated for the rows of the respective current window. If `PARTITION BY` is not specified, a single window is constructed that comprises all rows of the result set.

- `ORDER BY`

  The optional addition `ORDER BY` introduces both an order and a frame within the current window, which further restricts the rows for which the window function is calculated. It is also a prerequisite for certain [ranking functions](../../abap-glossary/abenranking_function_glosry.md).

If a window expression is used in the `SELECT` list of a `SELECT` statement with [`GROUP BY`](abapgroupby_clause.md) clause, the windows are defined in the merged result list and aggregate expressions can be used as arguments of the window functions. Each column that is specified in any position in the window expression must also be specified in the `GROUP BY` clause.

### Hints

- A window expression works in a similar way to an [aggregate expression](abapselect_aggregate.md), whereby the addition `PARTITION BY` assumes the role of the [`GROUP BY`](abapgroupby_clause.md) clause. Unlike aggregate expressions, however, there is no aggregation of the rows defined using `PARTITION BY`. Instead, these are retained and are all assigned the value calculated using the window expression.

- The window functions of a window expression work with the rows of a virtual table, which is defined by the specifications after `OVER`. Using the addition [`ORDER BY`](abaporderby_clause.md) of the `SELECT` statement has no effect on the result of a window expression. However, the rows of the result set can themselves be sorted according to the results of window expressions by using their alias name.

- A window expression can only be specified in the result set in the [`SELECT` list](abapselect_list.md) of a query. It cannot be used like an [aggregate expression](../../abap-glossary/abenaggregate_expression_glosry.md) in the [`GROUP BY`](abapgroupby_clause.md) or [`HAVING`](abaphaving_clause.md) clause.

- By using window expressions in other SQL expressions, calculations can be performed, which combine values of the current row with the results of window expressions, for example, the percentage of a column in the current window, or the distance to the minimum or maximum value of the current window.

## Executable Examples

- [Window Expressions](abensql_expr_over_abexa.md)

- [Window Expressions without Partition](abensql_expr_over_all_abexa.md)

## Addition 1

`... ORDER BY col1 [ASCENDING|DESCENDING], col2 [ASCENDING|DESCENDING], ...`

### Description

The optional addition `ORDER BY`, which can be specified independently of `PARTITION BY`, defines an order in the current window and an evaluation framework for the window function. `ORDER BY` is followed by a comma-separated list of columns of the data sources of the current query. These columns are used to sort the rows of the window. A column can only be specified directly using the column name [`col1`](abenabap_sql_columns.md), [`col2 ...`](abenabap_sql_columns.md) Alias names defined using [`AS`](abapselect_list.md) or column positions cannot be specified. The additions `ASCENDING` and `DESCENDING` determine whether the rows are sorted in ascending or descending order by the column in question. The default is `ASCENDING`.

Specifying the order using `ORDER BY` causes the following:

- The rows of the window are processed by the window function in the order defined by the sort order. The order of the processing of rows that appear more than once regarding the sort criterion is not defined. If the addition `ORDER BY` is not specified, this applies to all rows of the window.

- The rows processed by the window function are additionally restricted by a frame. Only the rows of the window that are in front of the current row in the sorting, or that have the same values in the columns of the sort criterion are respected.

While the restricted frame mainly affects the results of [aggregate functions](../../abap-glossary/abenaggregate_function_glosry.md) specified as a [window function](abensql_win_func.md), the processing sequence primarily affects the [ranking functions](../../abap-glossary/abenranking_function_glosry.md). The addition `ORDER BY` must be specified for the ranking functions `RANK` and `DENSE_RANK`.

### Hint

The definition of the window, the processing sequence, and the frame by `ORDER BY` following `OVER` is totally independent of the addition [`ORDER BY`](abaporderby_clause.md) clause of the `SELECT` statement.

### Executable Example

[Window Expressions with Sort](abensql_expr_over_order_by_abexa.md)

## Addition 2

`... ROWS BETWEEN ...`

### Description

The window frame specification is an optional addition within the `OVER( ... ORDER BY ... )` clause. It allows the definition of a subset of rows inside a window, which is also referred to as a frame. Frames are determined with respect to the current row, which enables the frame to move within a window.

A frame is defined by a starting frame boundary and an ending frame boundary. There are three options for the starting and ending frame boundaries:

- `{UNBOUNDED PRECEDING}` or `{UNBOUNDED FOLLOWING}`

  - `UNBOUNDED PRECEDING` as starting frame boundary specifies that the frame starts at the first row of the window.

  - `UNBOUNDED FOLLOWING` as ending frame boundary specifies that the frame ends at the last row of the partition.

- `CURRENT ROW` can be used as both starting and ending frame boundary. It specifies that the window starts or ends at the current row, including the current row in the frame.

- `{n PRECEDING}` or `{n FOLLOWING}`

  - `n PRECEDING` can be used as both starting and ending frame boundary. It specifies that the frame starts or ends `n` rows above the current row.

  - `n FOLLOWING` can be used as both starting and ending frame boundary. It specifies that the frame starts or ends `n` rows beneath the current row.

  - `n` must be 0, a positive [integer literal](../../abap-glossary/abeninteger_literal_glosry.md), or a [host expression](abenabap_sql_host_expressions.md) that can be resolved into a [constant](../../abap-glossary/abenconstant_glosry.md) of type `b`, `s`,`i`, or `int8`.

`ORDER BY` is mandatory.

### Hints

- The ending frame boundary cannot be smaller than the starting frame boundary.

- If no window frame is used, the default window frame is `BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`. That is to say that the window function computes all rows up to the current row. As a result, the function returns cumulative values.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates how different [window functions](../../abap-glossary/abenwindow_function_glosry.md) are applied to frames inside a window.

- `count` sorts the rows by column `ID` and counts the number of rows from the first row of the window to the current row. The result is the same as that returned by the [`ROW_NUMBER( )`](abensql_win_func.md) function.

- `count_reverse` sorts the rows by column `ID` and counts the number of rows from the current row to the last row of the window. The result is reverse numbering.

- `average` sorts the rows by column `ID` and calculates the rolling averages of a subset of rows from column `COL1`. The subset consists of the current row plus one preceding and one following row. With this function, it is possible, for example, to calculate the 3-day-average temperature for every day from a list of temperature data.

- `accumulate` sorts the rows by column `ID` and accumulates the values from the first row of the window up to the current row, thus computing the running total of column `COL1`.

``` abap
SELECT id, col1, col2, 
       COUNT( * ) OVER( ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING 
                                    AND CURRENT ROW ) 
                                    AS count, 
       COUNT( * ) OVER( ORDER BY id ROWS BETWEEN CURRENT ROW 
                                    AND UNBOUNDED FOLLOWING ) 
                                    AS count_reverse, 
       AVG( col1 ) OVER( ORDER BY id ROWS BETWEEN 1 PRECEDING 
                                     AND 1 FOLLOWING ) 
                                     AS average, 
       SUM( col1 ) OVER( ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING 
                                     AND CURRENT ROW ) 
                                     AS accumulate 
       FROM demo_update 
       INTO TABLE @FINAL(result).
```

### Executable Example

[Window Frame Specification](abensql_expr_over_win_frame_abexa.md)
