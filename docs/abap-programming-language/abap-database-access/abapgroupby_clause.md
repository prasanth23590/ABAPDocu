---
title: "SELECT, GROUP BY"
source_file: abapgroupby_clause.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, GROUP BY

## Syntax

``` abap
... GROUP BY { { sql_exp1, sql_exp2 ... 
                 grouping_sets1, grouping_sets2, ...} 
             | (grouping_syntax) } ...  
```

[`sql_exp1`](abapsql_expr.md) · [`sql_exp2`](abapsql_expr.md) · [`grouping_sets1`](abapgrouping_sets_clause.md) · [`grouping_sets2`](abapgrouping_sets_clause.md)

### Addition

[1. `... sql_exp1, sql_exp2, ...`](abapgroupby_clause.md#addition-1)

[2. `... grouping_sets1, grouping_sets2, ...`](abapgroupby_clause.md#addition-2)

[3. `... (grouping_syntax)`](abapgroupby_clause.md#addition-3)

## Overview

### Description

The addition `GROUP BY` combines groups of rows of the result set of a [query](../../abap-glossary/abenasql_query_glosry.md) into one row. After `GROUP BY`, the grouping criteria are specified statically or dynamically. The static specification is a comma-separated list of the following:

- [SQL expressions](../../abap-glossary/abensql_expression_glosry.md) `sql_exp1`, `sql_exp2`, ...

- [Grouping sets](../../abap-glossary/abengrouping_set_glosry.md) `grouping_sets1`, `grouping_sets2`, ...

The order of the SQL expressions or grouping sets within the comma-separated list is not important. The dynamic specification is as a parenthesized data object `grouping_syntax`.

If used, `GROUP BY` demands that only individual elements [`col_spec`](abapselect_clause_col_spec.md) and not all the columns are specified in the [`SELECT` list](abapselect_list.md) using `*`. If `GROUP BY` is used, all columns that are specified directly after `SELECT` or as an argument of an [SQL expression](abapsql_expr.md) and not as the argument of an [aggregate function](../../abap-glossary/abenaggregate_function_glosry.md), except the [grouping function](abengrouping_function.md), must be specified in an [aggregate expression](abapselect_aggregate.md). This means that columns not specified after `GROUP BY` can only be specified after `SELECT` as the argument of an aggregate function of an aggregate expression, with the exception of the grouping function. The aggregate expressions determine how the content of these columns is determined in the combined row from the content of all the rows of a group. For the grouping function [`GROUPING`](abengrouping_function.md), the column that is specified as its argument must be listed after `GROUP BY`.

The SQL expressions specified after `GROUP BY` cannot have the type `STRING`, `RAWSTRING`, `LCHR`, `LRAW`, or `GEOM_EWKB`.

### Hints

- `GROUP BY` cannot be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). The ABAP SQL statement bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

- Using `GROUP BY` and aggregate functions ensures that aggregates and groups are already built by the database system, not AS ABAP. This can considerably reduce the volume of data that has to be transported from the database to AS ABAP.

## Addition 1

`... sql_exp1, sql_exp2, ...`

### Description

Specifies SQL expressions whose result is used for grouping. A group is formed by the rows that have the same result in all SQL expressions `sql_exp1`, `sql_exp2`, ... Every [SQL expression](abapsql_expr.md) specified after `GROUP BY` must also be specified somewhere in the [`SELECT` list](abapselect_list.md), with identical spelling. When specifying individual columns [`col`](abenabap_sql_columns.md), the same column names as in the [`SELECT` list](abapselect_list.md) must be specified. It is not possible to specify alias names defined with [`AS`](abapselect_list.md).

When a column [`col`](abenabap_sql_columns.md) is specified as the operand of an SQL expression after `GROUP BY`, the effect on the interaction with the `SELECT` list is the same as specifying the column individually. A column that is not the argument of an aggregate function in the `SELECT` list can be specified either individually after `GROUP BY` or as the operand of an SQL expression. If a column like this is specified as the operand of an SQL expression, it does not need to be specified individually.

All [SQL expressions](abapsql_expr.md), except for [aggregate expressions](abapselect_aggregate.md) and [window expressions](abapselect_over.md), possible in the `SELECT` list can be specified after `GROUP BY`, with the following restrictions:

- Each expression must contain at least one column of a [data source](abapselect_data_source.md) as its operand.

- The expressions cannot contain any [host variables](abenabap_sql_host_variables.md) or ABAP literals as operands, with the exception of statically known constants or literals with the data type `i` or with a flat character-like type. Only constants defined by [`CONSTANTS`](../abap-declarations/abapconstants.md) are allowed and no [enumerated constants](../../abap-glossary/abenenumerated_constant_glosry.md).

### Hints

- If a grouping criterion specified after `GROUP BY` contains [null values](../../abap-glossary/abennull_value_glosry.md) in the result set, these values are not part of the group of ABAP-specific initial values and form a distinct group instead.

- If individual columns [`col`](abenabap_sql_columns.md) that are grouped in the `SELECT` list in an [SQL expression](abapsql_expr.md) are specified directly after `GROUP BY`, multiple groups with the same result can arise. To prevent this, the columns must be grouped after the expression.

- The spelling of the expressions after `GROUP BY` and in the `SELECT` list must be identical. An identical result is not enough. An expression `col1 + col2` after `GROUP BY` does not have the same semantics as an expression `col2 + col1` in the `SELECT` list. An alias name defined with [`AS`](abapselect_list.md) in the `SELECT` list, however, is ignored.

- An SQL expression that is specified more than once outside of an aggregate expression in the `SELECT` list does not need to be specified more than once after `GROUP BY`. An SQL expression can be specified more than once after `GROUP BY` but has the same effect has specifying the expression once.

- After `GROUP BY`, it is not possible to specify, instead of an expression, the alias name defined in the rule with [`AS`](abapselect_list.md) for the expression.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The rows of the DDIC database table `SFLIGHT` that have the same content in column `CARRID` are combined. The lowest and highest values in column `PRICE` are determined for each of these groups and placed into the combined row.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT FROM sflight 
       FIELDS carrid, 
              MIN( price ) AS min_price, 
              MAX( price ) AS max_price 
       GROUP BY carrid 
       INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Grouping after a concatenation of the columns `CARRID` and `CONNID`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT FROM sflight 
       FIELDS CONCAT( carrid, connid ) AS key, 
              MIN( seatsocc ) AS min_seatsocc, 
              MAX( seatsocc ) AS max_seatsocc 
       GROUP BY CONCAT( carrid, connid ) 
       INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```

### Executable Example

[`SELECT`, `GROUP BY` for SQL expressions](abensql_expr_with_group_by_abexa.md)

## Addition 2

`... grouping_sets1, grouping_sets2, ...`

### Description

`GROUPING SETS` is an addition of the `GROUP BY` clause that can be used to define multiple grouping sets `grouping_sets1,` `grouping_sets2, ...` under a `GROUP BY` clause. The grouping sets are aggregated separately and grouped in a result set. For more information, see [`SELECT - GROUP BY, grouping_sets`](abapgrouping_sets_clause.md).

## Addition 3

`... (grouping_syntax)`

### Description

As an alternative to specifying columns statically, a parenthesized data object `grouping_syntax` can be specified, which either contains the syntax of the list of SQL expressions (with the exception of [host expressions](../../abap-glossary/abenhost_expression_glosry.md)) or is initial when the statement is executed. The same applies to `grouping_syntax` as when specifying columns dynamically as a [`SELECT` list](abapselect_list.md).

If the content of `grouping_syntax` is initial, either all the rows or no rows are grouped together. The columns in the [`SELECT` list](abapselect_list.md) must then be specified either solely as arguments of aggregate functions or only directly. If not, the catchable exception `CX_SY_OPEN_SQL_DB` is raised. Invalid syntax raises a catchable exception from the class `CX_SY_DYNAMIC_OSQL_ERROR`.

### Security Hint

If used incorrectly, dynamic programming techniques can present a serious security risk. Any dynamic content that is passed to a program from the outside must be checked thoroughly or escaped before it is used in dynamic statements. This can be done using the system class `CL_ABAP_DYN_PRG` or the built-in function [`escape`](../abap-processing-internal-data/abenescape_functions.md).

### Hints

- The conditions for specifying SQL expressions after `GROUP BY` are particularly relevant for dynamic tokens and a check at runtime verifies whether the expressions match those in the `SELECT` list.

- No host variables or ABAP literals can usually be specified in SQL expressions in `grouping_syntax`. In particular, static attributes or constants of a class cannot be accessed from outside if the class has a static constructor and the constructor was not yet executed.

- The class `CL_ABAP_DYN_PRG` contains methods that support the creation of correct and secure dynamically specified columns.

- The literals of the dynamically specified ABAP SQL statements can span multiple rows of a token specified dynamically as an internal table.

- When specified dynamically, ABAP SQL statements can contain the comment characters [`*`](../abap-syntax-elements-of-an-abap-program/abencomment.md) and [`"`](../abap-syntax-elements-of-an-abap-program/abencomment.md) as follows:

  - In a dynamic token specified as a character-like data object, all content is ignored from the first comment character `"`.

  - In a dynamic token specified as an internal table, all rows are ignored that start with the comment character `*`. In the row, all content is ignored from the first comment character `"`.

    Comment characters placed within literals are, however, part of the literal.

- The dynamic forms of the statements [`WITH`](abapwith.md) enable fully dynamic `SELECT` statements, where all clauses except the `INTO` clause and the ABAP-specific additions can be specified in one dynamic token.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After entering any column of DDIC database table `SPFLI` the selected data is organized according to this column, which means that similar entries are combined. In `count`, the number of flight connections for the different values in column `spflicol` is determined. If, for example, `CITYFROM` is entered as `spflicol`, the number of destinations for each departure city is determined in `count`. Various possible exceptions are handled in `TRY` control structures. In particular, user input is checked for validity using a method of the class `CL_ABAP_DYN_PRG`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA spflicol TYPE c LENGTH 20 VALUE 'CITYFROM'. 
cl_demo_input=>request( CHANGING field = spflicol ). 
 
TRY. 
    spflicol = 
      cl_abap_dyn_prg=>check_column_name( to_upper( spflicol ) ). 
  CATCH cx_abap_invalid_name. 
    out->display( 'Not allowed' ). 
    RETURN. 
ENDTRY. 
 
DATA dref TYPE REF TO data. 
TRY. 
    FINAL(name) = `SPFLI-`  && spflicol. 
    CREATE DATA dref TYPE (name). 
  CATCH cx_sy_create_data_error. 
    out->display( 'Not possible' ). 
    RETURN. 
ENDTRY. 
 
DATA count TYPE i. 
FINAL(fieldlist) = spflicol && `, count(*)`. 
TRY. 
    SELECT DISTINCT (fieldlist) 
           FROM spfli 
           GROUP BY (spflicol) 
           ORDER BY (spflicol) 
           INTO (@dref->*, @count). 
      out->write( |{ dref->* } { 
                     count }| ). 
    ENDSELECT. 
  CATCH cx_sy_dynamic_osql_error. 
    out->display( 'Not possible' ). 
    RETURN. 
ENDTRY. 
 
out->display( ).
```
