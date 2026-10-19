---
title: "SELECT, select_list"
source_file: abapselect_list.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, select_clause"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, select_list

## Syntax

``` abap
... *   
  | {..., data_source~*, ..., col_spec [AS alias], ...}   
  | (column_syntax) ...  
```

[`data_source`](abapselect_data_source.md) · [`col_spec`](abapselect_clause_col_spec.md)

### Alternative

[1. `... *`](abapselect_list.md#alternative-1)

[2. `..., data_source~*, ..., col_spec [AS alias], ...`](abapselect_list.md#alternative-2)

[3. `... (column_syntax)`](abapselect_list.md#alternative-3)

## Overview

### Description

`SELECT` list of the [`SELECT` clause](abapselect_clause.md) of a [query](../../abap-glossary/abenasql_query_glosry.md). The specifications determine which columns are used to construct the result set of the `SELECT` statement and how their values are obtained. There are two static variants and one dynamic variant.

The `SELECT` list actually passed to the database is determined by the addition [`INTO CORRESPONDING`](abapinto_clause.md). If one or more names match, all the columns for which there are no name matches are removed from the `SELECT` list implicitly and therefore from the result set as well. If there are no name matches, none of the columns are removed from the result set.

## Alternative 1

`... *`

### Description

Defines all columns of the result set using `*`. The result set is constructed from all columns in the [data sources](abapselect_data_source.md) specified after [`FROM`](abapfrom_clause.md), in the order specified there. The columns of the result set inherit their names and data types from the data sources. Only a single data object can be specified after [`INTO`](abapinto_clause.md) and lists of data objects cannot be specified.

### Hints

- If multiple DDIC database tables are specified after `FROM`, it is not possible to prevent multiple columns from inheriting the same name when `*` is specified.

- For performance reasons, only those columns that are actually needed should be specified. `*` should only be specified if the content of all columns is actually needed.

- If the addition [`INTO CORRESPONDING`](abapinto_clause.md) is used, `*` can be transformed implicitly to a list of columns for which there is a name match.

- When an internal table [`@itab`](abapselect_data_source.md) with elementary row type is accessed in the [`FROM`](abapfrom_clause.md) clause of a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) after [`WITH`](abapwith.md), `*` cannot be specified as a `SELECT` list.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of all columns with multiple rows.

``` abap
SELECT * 
       FROM spfli 
       WHERE carrid = 'LH' 
       INTO TABLE @FINAL(wa).
```

## Alternative 2

`..., data_source~*, ..., col_spec [AS alias], ...`

### Variant

[1. `... data_source~* ...`](abapselect_list.md#variant-1)

[2. `... col_spec [AS alias] ...`](abapselect_list.md#variant-2)

### Description

Comma-separated list with

- `data_source~*` specifying all columns of a data source [`data_source`](abapselect_data_source.md) or

- the definition of individual columns [`col_spec`](abapselect_clause_col_spec.md) of the result set.

The individual specifications can be combined in any way, with the exception that `data_source~*` cannot be used together with [aggregate expressions](abapselect_aggregate.md).

## Variant 1

`... data_source~* ...`

### Description

Defines multiple columns of the result set using `data_source~*`, where `data_source` stands for an individual DDIC database table [`dbtab`](abapselect_data_source.md), a [CDS persistent entity](../../abap-glossary/abencds_sql_entity_glosry.md) [`cds_entity`](abapselect_data_source.md), or an [internal table](abapselect_itab.md). The result set contains all columns of the specified data source `data_source` at the relevant positions and in the order of the columns. The names of the database sources or their alias names can be specified for `data_source` that are also specified as [`data_source`](abapselect_data_source.md) after [`FROM`](abapfrom_clause.md). A data source can also be specified more than once. If `data_source~*` is used, only a structure can be specified after [`INTO`](abapinto_clause.md), no elementary data objects or lists of data objects.

The following special conditions should be noted:

- If specified, `data_source~*` cannot be specified together with [aggregate expressions](abapselect_aggregate.md). It can, however, be combined with [window expressions](abapselect_aggregate.md).

- When an internal table [`@itab`](abapselect_itab.md) with elementary row type is accessed in the [`FROM`](abapfrom_clause.md) clause of a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) after [`WITH`](abapwith.md), `data_source~*` cannot be specified in the `SELECT` list.

### Hints

- For performance reasons, only those columns that are actually needed should be specified. `data_source~*` should, therefore, only be specified if the content of all columns is actually needed.

- The definition of the result set can also be produced by specifying a single data source `data_source~*`. This defines the same result set as specifying `*` but can be different if information is specified after [`INTO`](abapinto_clause.md) and the resulting behavior.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of the columns of two DDIC database tables in a [join](abapselect_join.md) into an internal table. Two columns are read from `SCARR` and all columns are read from `SPFLI`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES BEGIN OF structure. 
TYPES carrname TYPE scarr-carrname. 
INCLUDE TYPE spfli AS spfli. 
TYPES url TYPE scarr-url. 
TYPES END OF structure. 
 
DATA itab TYPE STANDARD TABLE OF structure WITH EMPTY KEY. 
 
SELECT scarr~carrname, spfli~*, scarr~url 
       FROM scarr INNER JOIN spfli ON scarr~carrid = spfli~carrid 
       INTO TABLE @itab. 
 
out->write( itab ). 
 
out->display( ).
```

## Variant 2

`... col_spec [AS alias] ...`

### Addition

[`... AS alias`](abapselect_list.md#addition)

### Description

Definition of individual columns of the result set via specified columns [`col_spec`](abapselect_clause_col_spec.md), which can be defined using any [SQL expressions](abapsql_expr.md). The order in which the columns are specified is arbitrary and defines the order of the columns in the result set. Only if a column of the type `LCHR` or `LRAW` is specified explicitly as [`col`](abenabap_sql_columns.md) must the corresponding length field also be listed directly in front of it. Different specifications can be made after [`INTO`](abapinto_clause.md), the interaction of which is described by the column specified there.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Reading of two columns from a cell in the DDIC database table `SCARR`.

``` abap
SELECT SINGLE 
       FROM scarr 
       FIELDS carrname, url 
       WHERE carrid = 'UA' 
       INTO @FINAL(result).
```

## Addition

`... AS alias`

### Description

The addition `AS` can be used to define an alias name `alias` with a maximum of thirty characters in the result set for every specified column `col_spec`. The alias name `alias` must follow the [naming conventions](../abap-syntax-elements-of-an-abap-program/abennaming_conventions.md) for internal program names and the name `table_line` cannot be used.

An alias name cannot be assigned more than once and should not be the name of a column that does not have any alias names assigned to it. The alias name is used implicitly in the addition [`INTO|APPENDING CORRESPONDING FIELDS OF`](abapinto_clause.md). An alias name can only be specified after [`ORDER BY`](abaporderby_clause.md). A non-unique column name used after `ORDER BY` causes a syntax error or an exception.

### Hints

- If multiple DDIC database tables are specified after `FROM`, alternative names can be used when specifying single columns to avoid having multiple columns with the same name.

- In particular, an alias name cannot be used as the operand of an [SQL expression](abapsql_expr.md).

- If an alias name is to be named exactly like an addition of the `SELECT` statement, it may be necessary to prefix it with the [escape character `!`](../abap-operands/abennames_escaping.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Display of the flight date and average fare of all customers on Lufthansa flights with flight number 0400. The alternative name `avg` of the aggregate expression is required for the [`ORDER BY`](abaporderby_clause.md) clause and the inline declaration using [`@DATA(...)`](abapselect_into_target.md) in the [`INTO`](abapinto_clause.md) clauses.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT fldate, AVG( loccuram as DEC( 31,2 ) ) AS avg 
       FROM sbook 
       WHERE sbook~carrid = 'LH' AND 
             sbook~connid = '0400' 
       GROUP BY fldate 
       ORDER BY avg DESCENDING 
       INTO TABLE @FINAL(itab). 
 
out->write( itab ). 
 
out->display( ).
```

## Alternative 3

`... (column_syntax)`

### Description

Instead of the previous two static specifications, a data object `column_syntax` in parentheses can be specified. When the statement is executed, this data object either contains the syntax shown in static cases with the exception of [host expressions](../../abap-glossary/abenhost_expression_glosry.md) or is initial.

The data object `column_syntax` can be a character-like data object or a [standard table](../../abap-glossary/abenstandard_table_glosry.md) with a character-like row type. The syntax in `column_syntax` is not case-sensitive, as in the static syntax. When an internal table is specified, the syntax can be distributed across multiple rows.

If `column_syntax` is initial when the statement is executed, `select_list` is set implicitly to `*` and all columns are read.

If columns are specified dynamically without the addition `SINGLE`, the result set is always regarded as having multiple rows.

Invalid syntax raises a catchable exception from the class `CX_SY_DYNAMIC_OSQL_ERROR`.

### Security Hint

If used incorrectly, dynamic programming techniques can present a serious security risk. Any dynamic content that is passed to a program from the outside must be checked thoroughly or escaped before it is used in dynamic statements. This can be done using the system class `CL_ABAP_DYN_PRG` or the built-in function [`escape`](../abap-processing-internal-data/abenescape_functions.md).

### Hints

- If `column_syntax` is an internal table with a [header line](../../abap-glossary/abenheader_line_glosry.md), the [table body](../../abap-glossary/abentable_body_glosry.md) is evaluated, and not the header line.

- The class `CL_ABAP_DYN_PRG` contains methods that support the creation of correct and secure dynamic column specifications.

- In dynamically specified columns, static attributes or constants of a class cannot be accessed from outside in cases where the class has a static constructor and the constructor has not yet been executed.

- The literals of the dynamically specified ABAP SQL statements can span multiple rows of a token specified dynamically as an internal table.

- When specified dynamically, ABAP SQL statements can contain the comment characters [`*`](../abap-syntax-elements-of-an-abap-program/abencomment.md) and [`"`](../abap-syntax-elements-of-an-abap-program/abencomment.md) as follows:

  - In a dynamic token specified as a character-like data object, all content is ignored from the first comment character `"`.

  - In a dynamic token specified as an internal table, all rows are ignored that start with the comment character `*`. In the row, all content is ignored from the first comment character `"`.

    Comment characters placed within literals are, however, part of the literal.

- The dynamic forms of the statements [`WITH`](abapwith.md) enable fully dynamic `SELECT` statements, where all clauses except the `INTO` clause and the ABAP-specific additions can be specified in one dynamic token.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

All departure or destination cities of Lufthansa flights are produced, depending on whether `'CITYFROM'` or `'CITYTO'` is specified. A method of the class `CL_ABAP_DYN_PRG` is used to check whether the input values are valid.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA column TYPE c LENGTH 16 VALUE 'cityfrom'. 
cl_demo_input=>request( CHANGING field = column ). 
TRY. 
    column = 
      cl_abap_dyn_prg=>check_whitelist_tab( 
        val = to_upper( column ) 
        whitelist = VALUE string_hashed_table( ( `CITYFROM` ) 
                                               ( `CITYTO` ) ) ). 
  CATCH cx_abap_not_in_whitelist. 
    out->write( 'Not allowed' ). 
ENDTRY. 
 
FINAL(name) = `SPFLI-` && column. 
DATA dref TYPE REF TO data. 
CREATE DATA dref TYPE (name). 
 
DATA output TYPE TABLE OF string WITH EMPTY KEY. 
SELECT DISTINCT (column) 
       FROM spfli 
       WHERE carrid = 'LH' 
       INTO @dref->*. 
  output = VALUE #( BASE output ( |{ dref->* }| ) ). 
ENDSELECT. 
out->write( output ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Comment character in a dynamically specified token. The rows introduced using `*` and the content from the character `"` are ignored.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA: itab    TYPE TABLE OF scarr, 
      columns TYPE TABLE OF string. 
 
columns = VALUE #( ( `* Comment` ) 
                  ( `carrid, "comment` ) 
                  ( `* Comment` ) 
                  ( `carrname "comment` ) ). 
 
SELECT (columns) 
       FROM scarr 
       INTO CORRESPONDING FIELDS OF TABLE @itab. 
 
out->write( itab ). 
 
out->display( ).
```

### Executable Example

[Remove Columns from the `SELECT` List](abenselect_except_columns_abexa.md).
