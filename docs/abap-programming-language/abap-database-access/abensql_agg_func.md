---
title: "sql_agg - agg_func"
source_file: abensql_agg_func.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Operands and Expressions > ABAP SQL - SQL Expressions sql_exp > sql_exp - sql_agg"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# sql_agg - agg_func

## Syntax

``` abap
... AVG( [DISTINCT] sql_exp [AS dtype] ) 
  | MEDIAN( [DISTINCT] sql_exp ) 
  | MAX( [DISTINCT] sql_exp ) 
  | MIN( [DISTINCT] sql_exp ) 
  | SUM( [DISTINCT] sql_exp ) 
  | PRODUCT( col ) 
  | STDDEV( [DISTINCT] sql_exp ) 
  | VAR( [DISTINCT] sql_exp ) 
  | CORR( sql_exp1,sql_exp2 ) 
  | CORR_SPEARMAN( sql_exp1,sql_exp2  ) 
  | STRING_AGG( sql_exp[, sep] [ORDER BY col1 [ASCENDING|DESCENDING], 
                                         col2 [ASCENDING|DESCENDING], ...] ) 
  | COUNT( [DISTINCT] sql_exp ) 
  | COUNT( * ) 
  | COUNT(*) 
  | GROUPING( col ) ... 
  | ALLOW_PRECISION_LOSS  ( ... )  
```

[`sql_exp`](abapsql_expr.md) · [`AS dtype`](abapselect_avg_as.md) · [`sql_exp`](abapsql_expr.md) · [`sql_exp`](abapsql_expr.md) · [`sql_exp`](abapsql_expr.md) · [`sql_exp`](abapsql_expr.md) · [`sql_exp`](abapsql_expr.md) · [`sql_exp`](abapsql_expr.md) · [`sql_exp1`](abapsql_expr.md) · [`sql_exp2`](abapsql_expr.md) · [`sql_exp1`](abapsql_expr.md) · [`sql_exp2`](abapsql_expr.md) · [`sql_exp`](abapsql_expr.md) · [`col1`](abenabap_sql_columns.md) · [`col2`](abenabap_sql_columns.md) · [`sql_exp`](abapsql_expr.md) · [`GROUPING`](abengrouping_function.md) · [`col`](abenabap_sql_columns.md) · [`ALLOW_PRECISION_LOSS ( ... )`](abapselect_allow_precision_loss.md)

### Variant

[1. `... AVG( [DISTINCT] sql_exp [AS dtype] )`](abensql_agg_func.md#variant-1)

[2. `... MEDIAN( [DISTINCT] sql_exp )`](abensql_agg_func.md#variant-2)

[3. `... MAX( [DISTINCT] sql_exp )`](abensql_agg_func.md#variant-3)

[4. `... MIN( [DISTINCT] sql_exp )`](abensql_agg_func.md#variant-4)

[5. `... SUM( [DISTINCT] sql_exp )`](abensql_agg_func.md#variant-5)

[6. `... PRODUCT( col )`](abensql_agg_func.md#variant-6)

[7. `... STDDEV( [DISTINCT] sql_exp )`](abensql_agg_func.md#variant-7)

[8. `... VAR( [DISTINCT] sql_exp )`](abensql_agg_func.md#variant-8)

[9. `... CORR( sql_exp1,sql_exp2 )`](abensql_agg_func.md#variant-9)

[10. `... CORR_SPEARMAN( sql_exp1,sql_exp2 )`](abensql_agg_func.md#variant-10)

[11. `... STRING_AGG( sql_exp[, sep] [ORDER BY ...] )`](abensql_agg_func.md#variant-11)

[12. `... COUNT( [DISTINCT] sql_exp )`](abensql_agg_func.md#variant-12)

[13. `... COUNT( * )`](abensql_agg_func.md#variant-13)

[14. `... COUNT(*)`](abensql_agg_func.md#variant-14)

[15. `... GROUPING( col )`](abensql_agg_func.md#variant-15)

[16. `... ALLOW_PRECISION_LOSS( ... )`](abensql_agg_func.md#variant-16)

## Overview

### Description

[Aggregate function](../../abap-glossary/abenaggregate_function_glosry.md) in ABAP SQL. An aggregate function aggregates the values of the rows in a specific set of rows to a single value. Aggregate functions can be used in the following places:

- As a standalone [aggregate expression](../../abap-glossary/abenaggregate_expression_glosry.md) [`agg_exp`](abapselect_aggregate.md) in specific operand positions of a query. The evaluated row set is the full result set of the query or a group created using the addition [`GROUP BY`](abapgroupby_clause.md). The general rules described here apply.

- As a [window function](../../abap-glossary/abenwindow_function_glosry.md) [`win_func`](abensql_win_func.md) in a [window expression](abapselect_over.md). The evaluated row set is the current [window](../../abap-glossary/abenwindow_glosry.md) or a box inside the window. The general rules apply in addition to the rules for window functions.

- As an aggregate function in a [hierarchy aggregate navigator](abenselect_hierarchy_agg_navis.md). The evaluated row set consists of the [hierarchy nodes](../../abap-glossary/abenhierarchy_node_glosry.md) determined by the navigator. The general rules apply in addition to the rules for hierarchy aggregate navigators.

The following table shows which aggregate functions can be used in which places:

\|**-**\|[`agg_exp`](abapselect_aggregate.md)\| [`win_exp`](abapselect_over.md)\|[`HIERARCHY_DESCENDANTS_AGGREGATE`](abenselect_hierarchy_desc_agg.md)\|[`HIERARCHY_ANCESTORS_AGGREGATE`](abenselect_hierarchy_ancs_agg.md) \| \|:---\| \|`AVG`\|x\|x\|x\|x \| \|`MEDIAN`\|x\|x\|-\|- \| \|`MAX`\|x\|x\|x\|x \| \|`MIN`\|x\|x\|x\|x \| \|`SUM`\|x\|x\|x\|x \| \|`PRODUCT`\|-\|-\|-\|x \| \|`STDDEV`\|x\|x\|-\|- \| \|`VAR`\|x\|x\|-\|- \| \|`CORR`\|x\|x\|-\|- \| \|`CORR_SPEARMAN`\|x\|x\|-\|- \| \|`STRING_AGG`\|x\|-\|-\|x \| \|`COUNT`\|x\|x\|x\|x \| \|`COUNT(*)`\|x\|x\|x\|x \| \|`GROUPING`\|x\|-\|-\|- \| \|`ALLOW_PRECISION_LOSS`\|x\|-\|-\|-\|

The following shared properties apply here:

- The addition `DISTINCT` excludes duplicate values from the calculation in any operand positions in which it is specified.

- If the argument of an aggregate function (except `COUNT(*)`) has the [null value](../../abap-glossary/abennull_value_glosry.md), it is ignored when the function is evaluated. The result is a null value only if all the rows in the column in question contain a null value.

- The aggregate function `COUNT` counts rows and never produces the [null value](../../abap-glossary/abennull_value_glosry.md).

- Arguments of type `STRING`, `RAWSTRING`, `LCHR`, `LRAW`, and `GEOM_EWKB` cannot be handled using aggregate functions.

### Hint

The database platform determines whether an overflow occurs if the result of an aggregate function exceeds its value range. On some database platforms, intermediate results outside the value range are allowed. The overflow behavior of SQL expressions, on the other hand, is platform-independent. If an SQL expression in an aggregate expression produces an overflow, an exception is raised on every platform, even if a corresponding result of the aggregate function would not raise an exception on every platform.

For further details on the calculation on SAP HANA Platform, see the [SAP HANA SQL Reference Guide](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f).

## Variant 1

`... AVG( [DISTINCT] sql_exp [AS dtype] )`

### Description

Determines the average value of the content of an SQL expression [`sql_exp`](abapsql_expr.md) in a row set. The optional addition [`AS dtype`](abapselect_avg_as.md) can be used to define the result type explicitly.

The data type of the column must be numeric. The data types `DF16_RAW` and `DF34_RAW` are not allowed. The data type `INT8` is only allowed together with the addition [`AS dtype`](abapselect_avg_as.md).

The implicit data type of the result for [decimal floating point numbers](../../abap-glossary/abendecfloat_glosry.md) is the corresponding data type (`DECFLOAT16` or `DECFLOAT34` or `DF16_DEC` or `DF34_DEC`) and is otherwise the type `FLTP`, a platform-dependent intermediate result, or is determined by the addition [`AS dtype`](abapselect_avg_as.md).

### Hints

- The aggregate function `AVG` can be used in [aggregate expressions](abapselect_aggregate.md), in [window expressions](abapselect_over.md), and in the [hierarchy aggregate navigators](../../abap-glossary/abenhierarchy_agg_navi_glosry.md) [`HIERARCHY_DESCENDANTS_AGGREGATE`](abenselect_hierarchy_desc_agg.md) and [`HIERARCHY_ANCESTORS_AGGREGATE`](abenselect_hierarchy_ancs_agg.md).

- The addition `DISTINCT` can only be used in the `SELECT` list.

- The `sql_exp` can only be used in `SELECT` list positions.

- The result of the aggregate functions `AVG` in the data type `FLTP` is platform-dependent. The type of platform also determines whether the result of an aggregate expression `AVG`, which is used in a `HAVING` clause as an intermediate result, is of type `FLTP`. The addition [`AS dtype`](abapselect_avg_as.md) can be used to force the type `FLTP`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Determination of the average value of all values in a column and checking of the result.

``` abap
FINAL(n) = 9. 
 
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM TABLE @( VALUE #( 
  FOR i = 0 UNTIL i > n 
  ( id = CONV #( i ) num1 = i ) ) ). 
 
SELECT AVG( num1 ) 
       FROM demo_expressions 
       INTO (@FINAL(avg)). 
 
ASSERT avg =  n / 2.
```

## Variant 2

`... MEDIAN( [DISTINCT] sql_exp )`

### Description

Determines the statistical median of an input expression. Null values are ignored. If the number of non-null values is even, then the return value is the average of the two middle elements. Otherwise, the middle element is returned. The data type of the result is the DDIC data type of the result of the SQL expression.

The result of the SQL expression `sql_exp` must have one of the [numeric data types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) `INT1`, `INT2`, `INT4`, `INT8`, `DEC`, `DECFLOAT16`, `DECFLOAT34`, or `FLTP`.

### Hint

The aggregate function `MEDIAN` cannot be used in the [hierarchy aggregate navigators](../../abap-glossary/abenhierarchy_agg_navi_glosry.md) [`HIERARCHY_DESCENDANTS_AGGREGATE`](abenselect_hierarchy_desc_agg.md) and [`HIERARCHY_ANCESTORS_AGGREGATE`](abenselect_hierarchy_ancs_agg.md).

- The aggregate function `MEDIAN` can be used in [aggregate expressions](abapselect_aggregate.md) and in [window expressions](abapselect_over.md).

- The addition `DISTINCT` can only be used in the `SELECT` list.

- The `sql_exp` can only be used in `SELECT` list positions.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Determination of the median value of all values in a column. As the number of non-null values is even, the average of the two middle values is calculated. Since the data type of the result is `INT4`, the integer is rounded. The value returned is 6.

``` abap
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM TABLE @( 
VALUE #( 
( id = 'A' num1 = 2 dats1 = '20200504' ) 
( id = 'B' num1 = 20 dats1 = '20200505' ) 
( id = 'C' num1 = 4 dats1 = '20200506' ) 
( id = 'D' num1 = 6 dats1 = '20200507' ) 
( id = 'E' num1 = 5 dats1 = '20200508' ) 
( id = 'F' num1 = 8 dats1 = '20200509' ) ) ). 
 
SELECT 
  FROM demo_expressions 
  FIELDS 
    MEDIAN( num1 ) AS median_value 
    INTO @FINAL(result).
```

## Variant 3

`... MAX( [DISTINCT] sql_exp )`

## Variant 4

`... MIN( [DISTINCT] sql_exp )`

### Description

Determines the maximum value or minimum value of the results of the SQL expression [`sql_exp`](abapsql_expr.md) in a row set. The data type of the result is the DDIC data type of the result of the SQL expression.

The result of the SQL expression `sql_exp` must be numeric except for:

- the [replacement types for decimal floating point numbers](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_decimal_floating_point.md),

- [window expressions](abapselect_over.md),

- and [hierarchy aggregate navigators](abenselect_hierarchy_desc_agg.md).

If a single column [`col`](abenabap_sql_columns.md) is specified for the expression, this column can also have any data type.

The [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) can process the `MAX` and `MIN` functions in the `SELECT` list.

### Hints

- The aggregate functions `MAX` and `MIN` can be used in [aggregate expressions](abapselect_aggregate.md), in [window expressions](abapselect_over.md), and in the [hierarchy aggregate navigators](../../abap-glossary/abenhierarchy_agg_navi_glosry.md) [`HIERARCHY_DESCENDANTS_AGGREGATE`](abenselect_hierarchy_desc_agg.md) and [`HIERARCHY_ANCESTORS_AGGREGATE`](abenselect_hierarchy_ancs_agg.md).

- The addition `DISTINCT` can only be used in the `SELECT` list.

- The `sql_exp` can only be used in `SELECT` list positions.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Determination of the minimum value and maximum value of all values in a column and checking of the result.

``` abap
FINAL(n) = 9. 
 
DELETE FROM demo_expressions. 
 
INSERT demo_expressions FROM TABLE @( VALUE #( 
  FOR i = 0 UNTIL i > n 
  ( id = CONV #( i ) num1 = i ) ) ). 
 
SELECT MIN( num1 ) AS min, MAX( num1 ) AS max 
       FROM demo_expressions 
       INTO (@FINAL(min),@FINAL(max)). 
 
ASSERT min = 0. 
ASSERT max = n.
```

## Variant 5

`... SUM( [DISTINCT] sql_exp )`

### Description

Determines the sum of the results of the SQL expression [`sql_exp`](abapsql_expr.md) in a row set. The data type of the result is the DDIC data type of the result of the SQL expression.

The result of the SQL expression `sql_exp` must be numeric except for the [replacement types for decimal floating point numbers](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_decimal_floating_point.md). If a single column [`col`](abenabap_sql_columns.md) is specified for the expression, this column can have any numeric data type except `DF16_RAW` and `DF34_RAW`.

The [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) can process the `SUM` function in the `SELECT` list.

### Hints

- The aggregate function `SUM` can be used in [aggregate expressions](abapselect_aggregate.md), in [window expressions](abapselect_over.md), and in the [hierarchy aggregate navigators](../../abap-glossary/abenhierarchy_agg_navi_glosry.md) [`HIERARCHY_DESCENDANTS_AGGREGATE`](abenselect_hierarchy_desc_agg.md) and [`HIERARCHY_ANCESTORS_AGGREGATE`](abenselect_hierarchy_ancs_agg.md).

- The addition `DISTINCT` can only be used in the `SELECT` list.

- The `sql_exp` can only be used in `SELECT` list positions.

- If the aggregate function `SUM` is used for columns of types `DECFLOAT16` or `DF16_DEC`, it is best to use a target field with the data type `decfloat34` to avoid overflows.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Summation of all values in a column and checking the result.

``` abap
FINAL(n) = 9. 
 
DELETE FROM demo_expressions. 
 
INSERT demo_expressions FROM TABLE @( VALUE #( 
  FOR i = 0 UNTIL i > n 
  ( id = CONV #( i ) num1 = i ) ) ). 
 
SELECT SUM( num1 ) 
       FROM demo_expressions 
       INTO (@FINAL(sum)). 
 
ASSERT sum = ( n * ( n + 1 ) ) / 2.
```

## Variant 6

`... PRODUCT( col )`

### Description

Determines the product of the values of a column `col` in a row set. The data type of the result is the DDIC data type of the column. The column must have a numeric type except for the [replacement types for decimal floating point numbers](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_decimal_floating_point.md).

### Hint

The aggregate function `PRODUCT` can only be used in the [hierarchy aggregate navigator](../../abap-glossary/abenhierarchy_agg_navi_glosry.md)[`HIERARCHY_ANCESTORS_AGGREGATE`](abenselect_hierarchy_ancs_agg.md).

### Executable Example

See [Hierarchy Navigator `HIERARCHY_ANCESTORS_AGGREGATE`](abenhier_ancs_agg_abexa.md)

## Variant 7

`... STDDEV( [DISTINCT] sql_exp )`

### Description

Determines the standard deviation of a given expression as the square root of the `VAR` function. The result of the SQL expression `sql_exp` can have either the data type `FLTP` or `DECFLOAT34`. To use `STDDEV` with other data types, a conversion must first be performed using the SQL function [`CAST`](abensql_cast.md). The data type of the result is the DDIC data type of the result of the SQL expression, that is, either `FLTP` or `DECFLOAT34`.

The [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) can process the `STDDEV` function in the `SELECT` list.

See Variant 8 below for an example.

### Hints

- The aggregate function `STDDEV` can be used in [aggregate expressions](abapselect_aggregate.md) and in [window expressions](abapselect_over.md).

- The addition `DISTINCT` can only be used in the `SELECT` list.

- The `sql_exp` can only be used in `SELECT` list positions.

## Variant 8

`... VAR( [DISTINCT] sql_exp )`

### Description

Determines the variance of a given expression as the square of the standard deviation. The SQL expression `sql_exp` can only be `FLTP` or `DECFLOAT34`. To use `VAR` with other data types, a conversion must first be performed using the SQL function [`CAST`](abensql_cast.md). The data type of the result is the DDIC data type of the result of the SQL expression, that is, either `FLTP` or `DECFLOAT34`.

### Hints

- The aggregate function `VAR` can be used in [aggregate expressions](abapselect_aggregate.md) and in [window expressions](abapselect_over.md).

- The addition `DISTINCT` can only be used in the `SELECT` list.

- The `sql_exp` can only be used in `SELECT` list positions.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Determination of the average, the standard deviation, and the variance of the salaries of all employees listed in table `DEMO_EMPLOYEES`. The data type of column `SALARY` is `DEC` and to calculate the standard deviation and variance, the column is converted to type `DECFLOAT34`.

``` abap
SELECT 
  FROM demo_employees 
  FIELDS 
  AVG(  salary as dec( 10,2 ) ) AS average, 
  STDDEV( CAST( salary AS D34N ) ) AS stddev, 
  VAR( CAST( salary AS D34N ) ) AS variance 
  INTO @FINAL(result).
```

## Variant 9

`... CORR( sql_exp1,sql_exp2 )`

### Description

Determines the Pearson product-moment correlation coefficient between two columns. In other words, it measures the linear correlation of two value sets. The result of the SQL expressions `sql_exp1` and `sql_exp2` can have any [numeric data type](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_numeric.md). The data type of the result is always `FLTP`. The result ranges from -1 to 1. If a correlation cannot be computed, the result is null.

See Variant 10 below for an example.

### Hints

- The aggregate function `CORR` can be used in [aggregate expressions](abapselect_aggregate.md) and in [window expressions](abapselect_over.md). If the aggregate function `CORR` is used as a [window function](abensql_win_func.md), the `ROWS BETWEEN` addition is only supported with `UNBOUNDED PRECEDING` and `UNBOUNDED FOLLOWING`. Otherwise, a syntax warning occurs, if detected at compile time, or a catchable exception of class `CX_SY_OPEN_SQL_DB` occurs, if detected at runtime.

- The `sql_exp` can only be used in `SELECT` list positions.

## Variant 10

`... CORR_SPEARMAN( sql_exp1,sql_exp2 )`

### Description

Determines the Spearman's rank correlation coefficient of the values found in the corresponding rows of two columns. In other words, it measures the monotonous correlation of two value sets. The result of the SQL expressions `sql_exp1` and `sql_exp2` can have any numeric data type. The data type of the result is always `FLTP`. The result ranges from -1 to 1.

### Hints

- The aggregate function `CORR_SPEARMAN` can be used in [aggregate expressions](abapselect_aggregate.md) and in [window expressions](abapselect_over.md). If the aggregate function `CORR_SPEARMAN` is used as a [window function](abensql_win_func.md), the `ROWS BETWEEN` addition is only supported with `UNBOUNDED PRECEDING` and `UNBOUNDED FOLLOWING`. Otherwise, a syntax warning occurs, if detected at compile time, or a catchable exception of class `CX_SY_OPEN_SQL_DB` occurs, if detected at runtime.

- The `sql_exp` can only be used in `SELECT` list positions.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Determination of the Pearson product-moment and the Spearman's rank correlation for columns `NUM1` and `NUM2` of table `DEMO_EXPRESSIONS`. `CORR` is 0.959, since the correlation is not linear. `CORR_SPEARMAN` is 1, since the value sets are correlated monotonously.

``` abap
DELETE FROM demo_expressions. 
INSERT demo_expressions FROM TABLE @( 
VALUE #( 
( id = 'A' num1 = 1 num2 = 2 ) 
( id = 'B' num1 = 2 num2 = 4 ) 
( id = 'C' num1 = 3 num2 = 8 ) 
( id = 'D' num1 = 4 num2 = 16 ) ) ). 
 
SELECT 
  CORR( num1,num2 ) AS corr, 
  CORR_SPEARMAN( num1, num2 ) AS corr_spearman 
  FROM demo_expressions 
  INTO @FINAL(result).
```

## Variant 11

`... STRING_AGG( sql_exp[, sep] [ORDER BY ...] )`

### Description

Chains the results of the SQL expression [`sql_exp`](abapsql_expr.md) in a row set. The data type of the result is `SSTRING` with the length 1333. If the string in question is greater than 1333, a catchable exception of the class `CX_SY_OPEN_SQL_DB` is raised. The results of the SQL expression `sql_exp` must be a flat character-like data type like `CHAR`, `SSTRING`, `DATS`, or `TIMS`.

An optional separator `sep` separated by a comma can be specified after the SQL expression. If `sep` is specified, its content is inserted into the string between consecutive results of the SQL expression. If `sep` is not specified, these results are appended to each other directly. `sep` can be a [literal](abenabap_sql_literals.md), a [host constant](abenabap_sql_host_variables.md), or a [host variable](abenabap_sql_host_variables.md) with the [ABAP type](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_complete.md) `c`, `d`, `t`, or `n` with a maximum of 1333 characters. In `sep`, all trailing blanks are respected.

The optional addition `ORDER BY` can be used to define the order in which the results of the SQL expression are chained. If `ORDER BY` is not specified, the order is undefined. `ORDER BY` is followed by a comma-separated list of columns of the data sources of the current query. These columns are used to sort the rows of the row set. A column can only be specified directly using the column name [`col1`](abenabap_sql_columns.md), [`col2 ...`](abenabap_sql_columns.md). Alias names defined using [`AS`](abapselect_list.md) and column positions cannot be specified. The additions `ASCENDING` and `DESCENDING` determine whether the rows are sorted in ascending or descending order by the column in question. The default is `ASCENDING`.

### Hints

- The aggregate function `STRING_AGG` can be used in [aggregate expressions](abapselect_aggregate.md).

- The `sql_exp` can only be used in `SELECT` list positions.

- The restriction of the result length to 1333 can be removed by using the built-in function [`TO_CLOB`](abensql_type_conv_func.md). The use of `TO_CLOB` for `STRING_AGG` is recommended if the result length is expected to exceed 1333.

- Respecting all trailing blanks in `sep` is different to the behavior of [`&&`](abensql_string.md), where a truncation occurs.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

While the first `SELECT` statement most probably will fail due to the restriction of the result length of `STRING_AGG` to 1333, the second `SELECT` statement will be successful because of [`TO_CLOB`](abensql_type_conv_func.md).

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
out->next_section( 'Without TO_CLOB' ). 
TRY. 
    SELECT arbgb, STRING_AGG( text,' - ' ) AS texts 
           FROM t100 
           WHERE sprsl = 'E' 
           GROUP BY arbgb 
           ORDER BY arbgb 
           INTO TABLE @DATA(t100_texts) 
           UP TO 100 ROWS. 
    out->write( t100_texts ). 
  CATCH cx_sy_open_sql_db INTO FINAL(exc1). 
    out->write( exc1->get_text( ) ). 
ENDTRY. 
 
out->next_section( 'With TO_CLOB' ). 
TRY. 
    SELECT arbgb, to_clob( STRING_AGG( text,' - ' ) ) AS texts 
           FROM t100 
           WHERE sprsl = 'E' 
           GROUP BY arbgb 
           ORDER BY arbgb 
           INTO TABLE @t100_texts 
           UP TO 100 ROWS. 
    out->write( t100_texts ). 
  CATCH cx_sy_open_sql_db INTO FINAL(exc2). 
    out->write( exc2->get_text( ) ). 
ENDTRY. 
 
out->display( ).
```

### Executable Example

[SQL Expressions, Aggregate Function `string_agg`](abensql_expr_string_agg_abexa.md)

## Variant 12

`... COUNT( [DISTINCT] sql_exp )`

### Description

Determines the number of distinct values of the results of the SQL expression [`sql_exp`](abapsql_expr.md) in a row set.

- If the addition `DISTINCT` is not specified, `COUNT` determines all rows in which the result of the SQL expression [`sql_exp`](abapsql_expr.md) is not the [null value](../../abap-glossary/abennull_value_glosry.md).

- If the addition `DISTINCT` is specified, `COUNT` determines the number of distinct values of the results of the SQL expression [`sql_exp`](abapsql_expr.md). [Null values](../../abap-glossary/abennull_value_glosry.md) are ignored here.

The data type of the result is `INT8`. The SQL expression `sql_exp` can be a result with any type except for the [replacement types for decimal floating point numbers](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_decimal_floating_point.md). If a single column [`col`](abenabap_sql_columns.md) is specified for the expression, this column can have any data type.

### Hints

- The aggregate function `COUNT` can be used in [aggregate expressions](abapselect_aggregate.md), in [window expressions](abapselect_over.md), and in the [hierarchy aggregate navigators](../../abap-glossary/abenhierarchy_agg_navi_glosry.md) [`HIERARCHY_DESCENDANTS_AGGREGATE`](abenselect_hierarchy_desc_agg.md) and [`HIERARCHY_ANCESTORS_AGGREGATE`](abenselect_hierarchy_ancs_agg.md).

- The addition `DISTINCT` can only be used in the `SELECT` list.

- The `sql_exp` can only be used in `SELECT` list positions.

- A target object of the type `INT8`, `p`, or `decfloat34` must be specified if a function `COUNT( * )` or `COUNT(*)` is expected to return a value greater than the value range of `INT4`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Determination of the number of airlines flying to New York.

``` abap
SELECT COUNT( DISTINCT carrid ) 
       FROM spfli 
       WHERE cityto = 'NEW YORK' 
       INTO @FINAL(count).
```

## Variant 13

`... COUNT( * )`

## Variant 14

`... COUNT(*)`

### Description

The two spellings have the same meaning and return the number of rows in a row set independent from the column content. The data type of the result is `INT8`.

### Hints

- The aggregate functions `COUNT( * )` and `COUNT(*)` can be used in [aggregate expressions](abapselect_aggregate.md), in [window expressions](abapselect_over.md), and in the [hierarchy aggregate navigators](../../abap-glossary/abenhierarchy_agg_navi_glosry.md) [`HIERARCHY_DESCENDANTS_AGGREGATE`](abenselect_hierarchy_desc_agg.md) and [`HIERARCHY_ANCESTORS_AGGREGATE`](abenselect_hierarchy_ancs_agg.md).

- A target object of the type `INT8`, `p`, or `decfloat34` must be specified if a function `COUNT( * )` or `COUNT(*)` is expected to return a value greater than the value range of `INT4`.

- Using `COUNT( * )` or `COUNT(*)` standalone in the [`SELECT` list](abapselect_list.md), that is not together with other columns, can be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) for accessing the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and for accessing internal tables with [`FROM @itab`](abapselect_itab.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Example for counting rows using `COUNT`. The single-row result contains the values 7, 2, and 10 in its columns.

- 10 is the total number of rows in the result set determined using `COUNT(*)` and is independent of a single value.

- 7 is the number of rows determined using `COUNT` without `DISTINCT` in which [case distinction](abensql_simple_case.md) does not produce the null value.

- 2 is the number of distinct results *X* and *Y* determined using `COUNT` and `DISTINCT` of the [case distinction](abensql_simple_case.md) while ignoring the null value.

The difference 3 of the results of `COUNT(*)` and `COUNT` without `DISTINCT` is the number of rows in which the [case distinction](abensql_simple_case.md) produces the null value.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DELETE FROM demo_expressions. 
INSERT demo_expressions 
       FROM TABLE @( VALUE #( 
        FOR i = 1 UNTIL i > 10 ( id = CONV #( i ) num1 = i ) ) ). 
 
SELECT FROM demo_expressions 
       FIELDS 
         COUNT( 
           CASE WHEN num1 < 4 THEN 'X' 
                WHEN num1 BETWEEN 4 AND 7 THEN 'Y' END ) AS cnt, 
         COUNT( DISTINCT 
            CASE WHEN num1 < 4 THEN 'X' 
                 WHEN num1 BETWEEN 4 AND 7 THEN 'Y' END ) AS cntdist, 
         COUNT(*) AS cntstar 
       INTO TABLE @FINAL(result). 
 
out->display( result ).
```

## Variant 15

`... GROUPING( col )`

### Description

The grouping function [`GROUPING`](abengrouping_function.md) can be used to verify whether a column [`col`](abenabap_sql_columns.md) is part of the aggregation. The grouping function can be used only if the `GROUP BY` clause contains the addition `GROUPING SETS`. The data type of the result of the grouping function is [`INT1`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md). [SQL expressions](abapsql_expr.md) cannot be specified as arguments for `GROUPING`. For more information, see [`sql_agg - GROUPING`](abengrouping_function.md).

### Hint

The aggregate function `GROUPING` can be used in [aggregate expressions](abapselect_aggregate.md).

### Executable Example

[`GROUPING`, Aggregate Function](abengrouping_function_abexa.md)

## Variant 16

`ALLOW_PRECISION_LOSS( ... )`

### Description

The `ALLOW_PRECISION_LOSS` statement improves the performance of an [aggregate expression](../../abap-glossary/abenaggregate_expression_glosry.md) [`agg_exp`](abapselect_aggregate.md) at the cost of accuracy of the result. This function should only be used on decimal values and when loss of precision is acceptable. Currently, `SUM` is the only supported aggregate expression.

For more information, see [`sql_agg - ALLOW_PRECISION_LOSS`](abapselect_allow_precision_loss.md).

### Hint

The aggregate function `ALLOW_PRECISION_LOSS` can be used in [aggregate expressions](abapselect_aggregate.md).

### Executable Example

[`sql_agg` - Aggregate Function `ALLOW_PRECISION_LOSS`](abensql_expr_aggr_prec_loss_abexa.md)
