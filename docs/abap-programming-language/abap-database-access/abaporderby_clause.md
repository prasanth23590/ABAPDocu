---
title: "SELECT, ORDER BY"
source_file: abaporderby_clause.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, ORDER BY

## Syntax

``` abap
... ORDER BY 
      { {PRIMARY KEY} 
      | { {col1|a1|n1|sql_exp1} [col_additions], 
          {col2|a2|n2|sql_exp2} [col_additions], ...} 
      | (column_syntax) } ...  
```

[`col1`](abenabap_sql_columns.md) · [`sql_exp1`](abapsql_expr.md) · [`[col_additions]`](abaporderby_clause_additions.md) · [`col2`](abenabap_sql_columns.md) · [`sql_exp2`](abapsql_expr.md) · [`[col_additions]`](abaporderby_clause_additions.md)

### Alternative

[1. `... ORDER BY PRIMARY KEY`](abaporderby_clause.md#alternative-1)

[2. `... ORDER BY {col1|a1|n1|sql_exp1} [col_additions],`](abaporderby_clause.md#alternative-2)

[` {col2|a2|n2|sql_exp2} [col_additions], ...`](abaporderby_clause.md#alternative-2)

[3. `... ORDER BY (column_syntax)`](abaporderby_clause.md#alternative-3)

## Overview

### Description

The addition `ORDER BY` sorts a multirow result set of a [query](../../abap-glossary/abenasql_query_glosry.md) by the content of the specified column. The order of the rows in the result set is undefined with respect to all columns that are not listed after `ORDER BY` and can be different in repeated executions of the same `SELECT` statement. If the addition `ORDER BY` is not specified, the order of the rows in the result set is undefined with respect to all its columns.

The following restrictions apply when using the addition `ORDER BY` with other additions:

- The addition `ORDER BY` cannot be used with the addition [`SINGLE`](abapselect_single.md).

- All columns specified after `ORDER BY` must also be specified after the addition [`GROUP BY`](abapgroupby_clause.md) at the same time.

- If [aggregate functions](../../abap-glossary/abenaggregate_function_glosry.md) are specified after `SELECT`, all columns that are specified after `ORDER BY` and that do not have an alias name for an aggregate function must also be specified after `SELECT` and after [`GROUP BY`](abapgroupby_clause.md).

- If an alias name defined using [`AS`](abapselect_list.md) is used for sorting, this name must be unique and cannot be the same name as a column to which no alias name is assigned.

- If the addition [`DISTINCT`](abapselect_clause.md) is used, only those columns can be specified after `ORDER BY` that are also listed after `SELECT`. The exception to this rule is the [client column](../../abap-glossary/abenclient_column_glosry.md) when `PRIMARY KEY` is specified. If not, other columns can also be used, as long as there are no restrictions by other additions such as [`GROUP BY`](abapgroupby_clause.md).

- If the addition [`FOR ALL ENTRIES`](abenwhere_all_entries.md) is used in front of the [`WHERE` condition](abapwhere.md), `ORDER BY` can only be used with the addition `PRIMARY KEY` and all columns of the primary key, except the client column of client-dependent tables, must be specified in the [`SELECT` list](abapselect_list.md).

### Hints

- The data is sorted in the database system, once all other actions are completed, such as determining the hit list using `WHERE`, calculating aggregate functions, and grouping using `GROUP BY`. Only the additions [`UP TO`](abapselect_up_to_offset.md) and [`OFFSET`](abapselect_up_to_offset.md) are executed on the sorted hits.

- Sorts in the database system are performed in accordance with the rules for [size comparisons](abenwhere_logexp_compare.md) and the restrictions with regard to platform dependencies apply. More specifically, sorts after character-like values can be platform-dependent under certain circumstances and produce different results than ABAP sorts.

- If a sorted resulting set is assigned to a sorted internal table, the internal table is sorted again according to the sorting instructions.

## Alternative 1

`... ORDER BY PRIMARY KEY`

### Description

The result set is sorted in ascending order by the content of the [primary key](../../abap-glossary/abenprimary_key_glosry.md) of a single [data source](abapselect_data_source.md). The following restrictions apply:

- The addition `PRIMARY KEY` cannot be specified if a [join expression](../../abap-glossary/abenjoin_expression_glosry.md) or a [path expression](abenabap_sql_path.md) is used in the `SELECT` statement to select the data of multiple data sources.

- The addition `PRIMARY KEY` cannot be specified in a [subquery](../../abap-glossary/abensubquery_glosry.md).

- The addition `PRIMARY KEY` cannot be specified for a result set joined with [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), or [`EXCEPT`](abapunion.md).

- The addition `PRIMARY KEY` cannot be used when accessing a common table expression defined using [`WITH`](abapwith.md).

- If a [CDS](../../abap-glossary/abencds_entity_glosry.md) entity is sorted by the `PRIMARY KEY`, its key elements must be defined at the start of the structure without any gaps.

### Hint

If `ORDER BY PRIMARY KEY` is used with the addition [`FOR ALL ENTRIES`](abenwhere_all_entries.md) in front of the [`WHERE` condition](abapwhere.md), all fields of the primary key, except for the client column in client-dependent table, must be in the [`SELECT` list](abapselect_list.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the data from the DDIC database table `SPFLI` for carrier Lufthansa sorted by the complete primary key.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM spfli 
       WHERE carrid = 'LH' 
       ORDER BY PRIMARY KEY 
       INTO TABLE @FINAL(result). 
 
out->display( result ).
```

## Alternative 2

`... ORDER BY {col1|a1|n1|sql_exp1} [col_additions],`

` {col2|a2|n2|sql_exp2} [col_additions], ...`

### Variant

[1. `... col|a|n`](abaporderby_clause.md#variant-1)

[2. `... sql_exp`](abaporderby_clause.md#variant-2)

### Description

With this variant, columns or expressions can be specified in a comma-separated list as a sort criterion. Optional additions [`col_additions`](abaporderby_clause_additions.md) determine the sort direction and the handling of [null values](../../abap-glossary/abennull_value_glosry.md).

## Variant 1

`... col|a|n`

### Description

Column specification via column name, alias, or position:

- With `col1`, `col2`, ..., any columns of the [`SELECT`](abapselect_list.md) list can be specified directly by their [column names](abenabap_sql_columns.md).

- With `a1`, `a2`, ..., columns can be specified using alias names defined with [`AS`](abapselect_list.md) in the `SELECT` list. This is necessary if sorting is to be done by columns of the result set that are defined in the `SELECT` list using non-elementary [SQL expressions](abapsql_expr.md).

- With `n1`, `n2`, ..., columns can be specified via their position in the result set as defined by the [`SELECT` list](abapselect_list.md). If `n` is a [literal](abenabap_sql_literals.md) or a [host constant](../../abap-glossary/abenhost_constant_glosry.md) with an [integer type](../../abap-glossary/abeninteger_type_glosry.md) that contains a number between 1 and the number of columns in the result set, the sort criterion is the respective column of the result set. If the number is outside this range, a syntax error occurs.

### Hints

- Column specifications `col1`, `col2`, ... can contain a [path expression](abenabap_sql_path.md) for [CDS associations](../../abap-glossary/abencds_association_glosry.md) or [CTE associations](../../abap-glossary/abencte_association_glosry.md).

- Alias names specified in the `SELECT` list must be handled with care. Especially, non-alphanumeric characters should be prevented. In the following example, the sorting is carried out based on three columns: 1, +, 1: `SELECT col1 as 1 col2 as + FROM ... ORDER BY 1 + 1 ...`

- The column specified by `n` is independent from the addition `CORRESPONDING FIELDS` of the [`INTO`](abapinto_clause.md) clause. The columns of the result set are counted independently from their assignment to the target area.

- If `n` is a variable or does not have an integer type, it does not specify a position but is handled as an SQL expression `sql_exp` that has no effect.

- When accessing [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md) data sources with `*` or `data_source~*` in the [select list](abapselect_list.md), the [client column](../../abap-glossary/abenclient_column_glosry.md) is part of the result set and relevant for counting the columns for `n`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the data from the DDIC database table `SFLIGHT` for Lufthansa flight 0400, sorted by the third key field, the flight date, in descending order.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT * 
       FROM sflight 
       WHERE carrid = 'LH' AND 
             connid = '0400' 
       ORDER BY fldate DESCENDING 
       INTO TABLE @FINAL(result). 
 
out->display( result ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The `SELECT` statements show usages of `ORDER BY n`. A literal or a constant of type `i` with value *3* order the rows descending by the third column `CURRCODE` of the result set.

``` abap
SELECT carrid, carrname, currcode 
       FROM scarr 
       ORDER BY 3 DESCENDING 
       INTO TABLE @DATA(result1). 
 
CONSTANTS n TYPE i VALUE 3. 
SELECT carrid, carrname, currcode 
       FROM scarr 
       ORDER BY @n DESCENDING 
       INTO TABLE @DATA(result2). 
 
ASSERT result1 = result2.
```

## Variant 2

`... sql_exp`

### Description

`sql_exp1`, `sql_exp2`, ..., can be used to specify [SQL expressions](../../abap-glossary/abensql_expression_glosry.md). [Alias names](abapselect_list.md) can be used as operands of the SQL expressions.

A SQL expression without a column specification as an operand. has no effect.

### Hints

- As a rule, a SQL expression should contain at least one column specification as an operand.

- A single literal or [host constant](../../abap-glossary/abenhost_constant_glosry.md) with an [integer type](../../abap-glossary/abeninteger_type_glosry.md) is not handled as a SQL expression but as a column position `n`.

- Columns that are specified in an SQL expression used in the `ORDER BY` clause need to be specified in the `GROUP BY` clause. If the same SQL expression is specified in the `GROUP BY` clause, the columns do not need to be specified there again.

- Alias names that are used in an SQL expression in the `ORDER BY` clause do not need to be specified in the `GROUP BY` clause.

- If only aggregate functions are specified after `SELECT` and in the `ORDER BY` clause, a `SELECT` statement that opens a loop must not be closed using the statements `ENDSELECT` or `ENDWITH` when reading into a non-table-like [target area](abapinto_clause.md).

- If a SQL expression appears identically in the `SELECT` list and behind `ORDER BY`, it makes no difference whether its alias from the `SELECT` list or the SQL expression is listed in the `ORDER BY` clause. But using SQL expressions directly in the `ORDER BY` clause allows ordering independent from the appearance in the `SELECT` list.

- Currently, SQL expressions are not supported in the `ORDER BY` clause of `SELECT` statements using [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), and [`EXCEPT`](abapunion.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The second `SELECT` statement shows the ordering by a SQL expression. The result is the same as when ordering by an alias for the same expression in the `SELECT` list.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT carrid, connid, fldate, seatsmax - seatsocc AS seatsfree 
       FROM sflight 
       WHERE carrid = 'LH' AND 
             connid = '0400' 
       ORDER BY seatsfree DESCENDING 
       INTO TABLE @FINAL(result1). 
 
SELECT carrid, connid, fldate, seatsmax - seatsocc AS seatsfree 
       FROM sflight 
       WHERE carrid = 'LH' AND 
             connid = '0400' 
       ORDER BY  seatsmax - seatsocc DESCENDING 
       INTO TABLE @FINAL(result2). 
 
ASSERT result1 = result2. 
 
out->display( result1 ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of data from the DDIC database table `SFLIGHT` by sorting the result table by the overall number of rows for each carrier using an aggregate expression.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT COUNT(*) AS cnt, carrid FROM spfli 
  GROUP BY carrid 
  ORDER BY COUNT(*) DESCENDING 
  INTO TABLE @FINAL(res). 
 
out->write( res ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Bad examples of how to order by `sql_exp`. In both cases, the expressions do not depend on the content of the data source and the `ORDER BY` clause has no effect. While in the first case, the SQL expression might be mixed up with a dynamic column specification, the second case looks like a position specification, but it is not. **Note:** If `n` were declared with `CONSTANTS` instead of `DATA`, it were a position specification.

``` abap
SELECT carrid, carrname, currcode 
       FROM scarr 
       INTO TABLE @DATA(result1). 
 
 
SELECT carrid, carrname, currcode 
       FROM scarr 
       ORDER BY 'CURRCODE' DESCENDING 
       INTO TABLE @DATA(result2). 
 
ASSERT result1 = result2. 
 
DATA n TYPE i VALUE 3. 
SELECT carrid, carrname, currcode 
       FROM scarr 
       ORDER BY @n DESCENDING 
       INTO TABLE @DATA(result3). 
 
ASSERT result1 = result3.
```

## Alternative 3

`... ORDER BY (column_syntax)`

### Description

As an alternative to specifying columns statically, a parenthesized data object `column_syntax` can be specified that contains the syntax of `PRIMARY KEY` or the list of columns or is initial when the statement is executed.

The same applies to `column_syntax` as when specifying the [`SELECT` list](abapselect_list.md) dynamically. If the content of `column_syntax` is initial, the addition `ORDER BY` is ignored. Invalid syntax raises a catchable exception from the class `CX_SY_DYNAMIC_OSQL_ERROR`.

### Security Hint

If used incorrectly, dynamic programming techniques can present a serious security risk. Any dynamic content that is passed to a program from the outside must be checked thoroughly or escaped before it is used in dynamic statements. This can be done using the system class `CL_ABAP_DYN_PRG` or the built-in function [`escape`](../abap-processing-internal-data/abenescape_functions.md).

### Hints

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

Dynamic sort by two columns that can be specified.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA(column1) = `carrid`. 
DATA(column2) = `connid`. 
 
cl_demo_input=>new( 
  )->add_field( CHANGING field = column1 
  )->add_field( CHANGING field = column2 )->request( ). 
 
FINAL(column_syntax) = column1 && `, ` && column2. 
 
TRY. 
    SELECT carrid, connid, cityfrom, cityto 
           FROM spfli 
           ORDER BY (column_syntax) 
           INTO TABLE @FINAL(result). 
    out->write( result ). 
  CATCH cx_sy_dynamic_osql_semantics. 
    out->write( 'Error' ). 
ENDTRY. 
 
out->display( ).
```

### Executable Example

[Dynamic `ORDER BY` Clause](abendynamic_order_by_abexa.md)
