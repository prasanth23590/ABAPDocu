---
title: "SELECT, col_spec"
source_file: abapselect_clause_col_spec.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, select_clause > SELECT, select_list"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, col_spec

## Syntax

``` abap
... sql_exp ...  
```

[`sql_exp`](abapsql_expr.md)

### Alternative

[1. `... col`](abapselect_clause_col_spec.md#alternative-1)

[2. `... literal | @dobj | @( expr )`](abapselect_clause_col_spec.md#alternative-2)

[3. `... sql_func | cds_scalar_func | sql_arith | sql_cast | sql_string | sql_case`](abapselect_clause_col_spec.md#alternative-3)

[4. `... sql_agg`](abapselect_clause_col_spec.md#alternative-4)

[5. `... sql_win`](abapselect_clause_col_spec.md#alternative-5)

## Overview

### Description

Specifies columns in the [`SELECT` list](abapselect_list.md) of the [`SELECT` clause](abapselect_clause.md) of a [query](../../abap-glossary/abenasql_query_glosry.md). The specified columns are used to construct the result set of a [query](../../abap-glossary/abenasql_query_glosry.md) from individual columns. Each column is specified using an [SQL expression](../../abap-glossary/abensql_expression_glosry.md) [`sql_exp`](abapsql_expr.md). Any SQL expressions and [parentheses](abensql_exp_parentheses.md) can be used.

For each SQL expression a value is calculated from its arguments. Its data type that depends on the expression and places this value in the column of the result set. The corresponding data host variable after `INTO` or `APPENDING` must be a [suitable](abenselect_into_conversion.md) choice.

To be able to evaluate the result of SQL expressions except for individual column specifications in [`INTO|APPENDING CORRESPONDING FIELDS`](abapinto_clause.md), [`INTO ...@DATA(...)`](abapinto_clause.md), and [`ORDER BY`](abaporderby_clause.md), an alias name must be defined using [`AS`](abapselect_list.md), which is then used by these additions.

The following sections discuss the special characteristics of the various SQL expressions.

### Hint

[Certain SQL expressions](abensql_engine_expr.md) can be calculated by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). If any other SQL expressions are used, [table buffering](../../abap-glossary/abentable_buffering_glosry.md) is bypassed and internal tables accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

## Alternative 1

`... col`

### Description

Direct specification [`col`](abenabap_sql_columns.md) of an individual column of a [data source](abapselect_data_source.md) as an [elementary SQL expression](abensql_elem.md). If the name of a data source is specified directly, its content is placed directly in the associated column of the result set. The data type of a column in the result set is the data type of the corresponding component in the ABAP Dictionary.

The following special conditions apply:

- If required, the specified column can contain a [path expression](abenabap_sql_path.md) for [CDS associations](../../abap-glossary/abencds_association_glosry.md) or [CTE associations](../../abap-glossary/abencte_association_glosry.md). If the addition `CORRESPONDING` or an inline declaration `@DATA(...)` or `@FINAL(...)` is used in the [`INTO`](abapinto_clause.md) clause, any columns specified using a path expression must have an alias name `alias` defined using [`AS`](abapselect_list.md).

- If the value of a column of type `LRAW` or `LCHR` is read, the associated length field of type `INT2` or `INT4` must also be read and specified in the list in front of the column of type `LRAW` or `LCHR`.

### Hints

- A column can be specified more than once.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Direct specification of the columns `CARRID`, `CARRNAME`, and `URL` of the DDIC database table `SCARR`.

``` abap
SELECT FROM   scarr 
       FIELDS carrid, carrname, url 
       INTO   TABLE @FINAL(itab).
```

## Alternative 2

`... literal | @dobj | @( expr )`

### Description

Specification of a literal [`literal`](abenabap_sql_literals.md), host variable [`@dobj`](abenabap_sql_host_variables.md), host expression [`@( expr )`](abenabap_sql_host_expressions.md), or as an [elementary SQL expression](abensql_elem.md). These are values of the ABAP program that are determined before the query is executed in ABAP and are transferred to the database system, where they are inserted into the result set as a column. A column defined in this way contains the same value in all rows of the result set.

### Hints

- The restrictions on [elementary SQL expressions](abensql_elem.md) apply with respect to the data types that can be used. More specifically, any host variables specified as field symbols or formal parameters cannot have generic data types.

- It can be a good idea to specify a literal, a host variable, or a host expression as an elementary expression of a `SELECT` list to assign a defined value to a column of a result set that is not read from the database.

- Specifying a constant or a literal as the only element of a `SELECT` list is one way of defining whether data in a selection exists without having to read data from the database.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specification of the constant `abap_true` from the type pool `ABAP` to determine whether a specific row exists.

``` abap
SELECT SINGLE 
       FROM scarr 
       FIELDS @abap_true 
       WHERE carrid = '...' 
       INTO @FINAL(flag). 
IF flag IS INITIAL. 
  RETURN. 
ENDIF.
```

## Alternative 3

`... sql_func | cds_scalar_func | sql_arith | sql_cast | sql_string | sql_case`

### Description

Specification of a non-elementary SQL expression in the form of a built-in function [`sql_func`](abensql_builtin_func.md), of a [CDS scalar function](../../abap-glossary/abencds_scalar_function_glosry.md) `cds_scalar_func` of an arithmetic expression [`sql_arith`](abensql_arith.md), cast expression [`sql_cast`](abensql_cast.md), string expression [`sql_string`](abensql_string.md), or case distinction [`sql_case`](abensql_case.md). The values of these expressions are calculated in the database. The rules and restrictions described for these apply. The values of the data source columns specified as operands are the selected values of the current row.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a non-elementary SQL expression as a column specification.

``` abap
SELECT CONCAT_WITH_SPACE( carrname && ' (' && carrid && '),', url, 1 ) 
       FROM scarr 
       INTO TABLE @FINAL(itab).
```

## Alternative 4

`... sql_agg`

### Description

Specifies an aggregate expression [`sql_agg`](abapselect_aggregate.md), in which a column of a [data source](abapselect_data_source.md) or an [SQL expression](abapsql_expr.md) is specified as an argument of an [aggregate function](../../abap-glossary/abenaggregate_function_glosry.md). An aggregate function uses the values from multiple rows of the specified column or SQL expression to calculate a single value with a data type that depends on the aggregate function, and then places this value in the column of the result set.

The following rules apply when aggregate expressions are used in the `SELECT` list:

- If aggregate expressions are used, all column names that are not specified within an aggregate expression must be specified after the addition [`GROUP BY`](abapgroupby_clause.md). The aggregate functions evaluate the content of the groups defined by `GROUP BY` in the database system and pass the result to the merged rows of the result set.

- If the addition `FOR ALL ENTRIES` is used before [`WHERE`](abapwhere.md), no aggregate expressions can be used except `COUNT( * )`. In cases like these, the aggregate expression is not evaluated in the database, but is emulated on the AS ABAP.

- If columns are only used within aggregate expressions in the `SELECT` list, the result set has just one row and the addition `GROUP BY` is not required. If a non-table-like target area is specified after `INTO` for aggregated-only columns and without the addition `GROUP BY` after a single `SELECT` statement, that is, not in the case of multiple statements joined using [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), or [`EXCEPT`](abapunion.md), the statement `ENDSELECT` cannot be specified, as is also the case when using the addition `SINGLE`. If the aggregate expression `COUNT( * )` is not used, an internal table can be specified after `INTO` regardless of the addition `GROUP BY` and the first row of this table filled.

- In the case of exclusively aggregated columns without `GROUP BY`, the result set also contains a row if no data is found in the database. If `COUNT( * )` is used, the column in question contains the value 0. The columns of the other aggregate functions contain initial values. This row is assigned to the data object specified after `INTO` and, unless `COUNT( * )` is used only statically and an alias name is not specified, `sy-subrc` is set to 0 and `sy-dbcnt` is set to 1.

- If `COUNT( * )` is used as the only static column specified and an alias name is not specified using [`AS`](abapselect_list.md) and `GROUP BY` is not specified at the same time, the addition `INTO` can be omitted. The number of selected rows can then be taken from the system field `sy-dbcnt`. If more than 2,147,483,647 rows are selected, `sy-dbcnt` contains the value -1. If no data is found on the database, `sy-dbcnt` is set to 0 and `sy-subrc` is set to 4.

### Hints

- Aggregate expressions cannot be specified together with [`data_source~*`](abapselect_list.md) in the comma-separated list.

- If [aggregate expressions](abapselect_aggregate.md) are used as operands of SQL expressions, the same rules apply as if they were specified directly.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Determination of the number of rows in the DDIC database table `SCARR`.

``` abap
SELECT FROM   scarr 
       FIELDS COUNT( * ) 
       INTO   @FINAL(wa).
```

## Alternative 5

`... sql_win`

### Description

Specifies a window expression [`sql_win`](abapselect_over.md) in which a [window function](../../abap-glossary/abenwindow_function_glosry.md) is applied to a [window](../../abap-glossary/abenwindow_glosry.md) of the result set. Window expressions can only be specified in the `SELECT` list.
