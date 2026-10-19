---
title: "SELECT, FROM @itab"
source_file: abapselect_itab.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM > SELECT, FROM data_source"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM @itab

## Syntax

``` abap
... @itab  
```

## Description

Specifies an [internal table](../../abap-glossary/abeninternal_table_glosry.md) `itab` as a [host variable](abenabap_sql_host_variables.md) whose name must be prefixed with the `@` character as a [data source](abapselect_data_source.md) of a [query](../../abap-glossary/abenasql_query_glosry.md). The `SELECT` statement handles the internal table of the AS ABAP like a DDIC database table that is instantiated on the database. The ABAP types of the columns in the internal table are mapped to suitable [built-in data types](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) in the ABAP Dictionary. If a column is declared with reference to a type in the ABAP Dictionary, this type is used directly.

Two cases must be distinguished:

- The `SELECT` statement can be processed by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md).

  In this case, the data of the internal table is processed on the AS ABAP. This is possible for all database platforms.

- The `SELECT` statement contains elements that are [not supported](abensql_engine_restr.md) by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md).

  In this case, the data must be passed to a temporary table in the database before the query is actually executed. Here, only those columns are transported that need to be accessed. This option is not supported by all databases.

The following conditions apply:

- Only one internal table can be passed to the database for an ABAP SQL statement.

  - Multiple internal tables can be specified only if the ABAP SQL statement can be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md).

  - Only one internal table can be specified in an ABAP SQL statement that cannot be processed by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md).

- An alias name must be assigned to each internal table using [`AS`](abapfrom_clause.md).

- The row type of the internal tables can be elementary or structured.

  - An elementary row type represents a column that can be addressed in the other [clauses](abenselect_clauses.md) of the query using the name `table_line` or an alias name defined with [`AS`](abapselect_list.md) in the [`SELECT` list](abapselect_list.md).

  - A structured row type cannot contain any substructures.

- No deep row types are allowed. An elementary row type cannot be a string or a reference type and a structured row type cannot contain any strings, reference types, or internal tables as components, with the following exception: An elementary row type or a component can have the type [`string`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) if this is declared using a reference to the built-in dictionary type [`SSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- If the addition [`ORDER BY PRIMARY KEY`](abaporderby_clause.md) is used, the respective internal table must have a [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md).

- The key fields of a [primary table key](../../abap-glossary/abenprimary_table_key_glosry.md) in the internal tables must be contiguous columns that appear in the same order at the start of the row type.

- If the [`FROM`](abapfrom_clause.md) clause is specified statically, the internal tables cannot be a generically typed formal parameter, a generically typed field symbol or be specified by dereferencing a generically type data reference variable. Such tables can only be specified in a dynamic `FROM` clause and must represent a suitable internal table at runtime.

- The internal tables cannot contain any columns declared with reference to the obsolete dictionary types [`DF16_SCL`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) and [`DF34_SCL`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md).

- When an internal table with elementary row type is accessed in a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) after [`WITH`](abapwith.md), the [`SELECT` list](abapselect_list.md) cannot be `*` or contain `data_source~*`.

- The internal tables should have an explicitly defined primary key, which can also be empty. Generic primary keys and [standard keys](../../abap-glossary/abenstandard_key_glosry.md) are not evaluated in reads and a syntax check warning occurs.

- As a prerequisite for passing data from an internal table to the database, [FDA](../../abap-glossary/abenfast_data_access_glosry.md) write access must be available and switched on, otherwise an exception occurs.

The data in the internal tables is handled like data on the database even if it is not transported to the database:

- Data with the type [`string`](../abap-built-in-types-data-objects-functions-and-constructors/abenbuiltin_types_character.md) declared using a reference to the built-in dictionary type [`SSTRING`](../../abap-dictionary-ddic/ddic-built-in-data-types/abenddic_builtin_types.md) is handled like text fields with fixed lengths in which trailing blanks are ignored.

- [SQL expressions](abapsql_expr.md) are evaluated in the same way as on the database, for example:

  - Evaluations of the functions [`DIV`](abensql_arith_func.md) and [`MOD`](abensql_arith_func.md) differ from calculations with the identically named [ABAP operators](../abap-processing-internal-data/abenarith_operators.md).

  - Any [null values](../../abap-glossary/abennull_value_glosry.md) produced as results of nested expressions, for example, in the [`COALESCE`](abensql_coalesce.md) function or in [comparisons](abenabap_sql_expr_logexp.md), are handled as null values.

  - The result of a [relational expression](abenabap_sql_stmt_logexp.md) with operands that contain [null values](../../abap-glossary/abennull_value_glosry.md) is unknown, except in the case of the expression [`IS [NOT] NULL`](abenwhere_logexp_null.md).

Generally, the internal table `itab` is regarded as a client-independent table. The first column is not regarded as a client column, regardless of its data type. This behavior can be changed with the addition [`DECLARE CLIENT`](abapselect_declare_client.md). With that addition, any column of type `CHAR` with length 3 can be declared as a client column. Then, the internal table is handled as client-dependent and implicit client handling is applied.

## Hints

- If it is known statically that the statement cannot be processed by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) and if no database tables are accessed in the statement, a syntax check warning occurs that can be hidden by the pragma `##itab_db_select`.

- The data in internal tables should only be transported to the database system if it is actually needed there. In this case, the pragma `##itab_db_select` can be used to hide the corresponding syntax check warning.

- The use of an internal table as a data source of `SELECT` is mainly intended for joins with data sources from the database. Since joins with database tables or views are not supported by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md), this is possible for only one internal table within a `SELECT` statement that can be transported to the database. In contrast, joins between multiple internal tables only can be processed by the ABAP SQL in-memory engine.

- An internal table as a data source of `SELECT` can be a potential alternative to the statements [`READ TABLE`](../abap-processing-internal-data/abapread_table.md) and [`LOOP AT`](../abap-processing-internal-data/abaploop_at_itab.md) in order to exploit ABAP SQL syntax that is not possible with the statements for internal tables.

  - If this solution is used, it should be ensured that the data is evaluated on the AS ABAP and that no data is transported to the database system to be evaluated. A corresponding syntax check warning is raised as a reminder.

  - The use of `SELECT` to access an internal table is usually less efficient than the statements for internal tables and should only be used in cases not covered by these statements.

- In internal tables with elementary row types, the name of the [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line` cannot be the name of a structure in ABAP. An inline declaration using [`@DATA|@FINAL (...)`](abapselect_into_target.md) can only be made in the [`INTO`](abapinto_clause.md) clause if the column `table_line` of the result set is assigned an alias name using [`AS`](abapselect_list.md).

- Currently, the access to multiple internal tables within one ABAP SQL statement is restricted to joins of internal tables. No database table can be accessed in the same statement in this case. Only one internal table can be accessed together with database tables.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of an internal table as the data source of an inner join of a [`SELECT`](abapselect.md) statement. The `SELECT` statement cannot be processed by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) and the internal table is transported to the database due to the join with a database table.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA itab TYPE HASHED TABLE OF scarr 
          WITH UNIQUE KEY mandt carrid. 
 
itab =  VALUE #( ( carrid = 'LH' carrname = 'L.H.' ) 
                 ( carrid = 'UA' carrname = 'U.A.' ) ). 
 
SELECT scarr~carrid, scarr~carrname, spfli~connid 
       FROM @itab AS scarr 
         INNER JOIN spfli ON scarr~carrid = spfli~carrid 
       INTO TABLE @FINAL(result) 
       ##itab_db_select. 
 
out->write( result ). 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Looping over an internal table in a sequence defined by the sort order of different columns using `SELECT` - `ENDSELECT`. Such a loop is not possible with [`LOOP AT itab`](../abap-processing-internal-data/abaploop_at_itab.md). The `SELECT` statement can be processed by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) on the AS ABAP.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
  BEGIN OF line, 
    col1 TYPE i, 
    col2 TYPE i, 
  END OF line, 
  itab TYPE TABLE OF line WITH EMPTY KEY. 
 
FINAL(itab) = VALUE itab( 
  ( col1 = 8 col2 = 8 ) 
  ( col1 = 3 col2 = 5 ) 
  ( col1 = 7 col2 = 4 ) 
  ( col1 = 2 col2 = 3 ) 
  ( col1 = 0 col2 = 1 ) 
  ( col1 = 4 col2 = 6 ) ). 
 
SELECT * 
       FROM @itab AS itab 
       ORDER BY col1 DESCENDING 
       INTO @FINAL(wa1). 
  out->write( wa1 ). 
ENDSELECT. 
 
out->line( ). 
 
SELECT * 
       FROM @itab AS itab 
       ORDER BY col2 ASCENDING 
       INTO @FINAL(wa2). 
  out->write( wa2 ). 
ENDSELECT. 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Looping over an internal table in a sequence defined by the sort order of a column using `SELECT` - `ENDSELECT`. One sequence is case-sensitive and the other is not because the function `UPPER` is used in the `ORDER BY` clause. Such a loop is not possible with [`LOOP AT itab`](../abap-processing-internal-data/abaploop_at_itab.md). The `SELECT` statement can be processed by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) on the AS ABAP.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: 
 c1 type c LENGTH 1, 
 itab TYPE TABLE OF c WITH EMPTY KEY. 
 
FINAL(itab) = VALUE itab( 
 ( 'B' ) 
 ( 'a' ) 
 ( 'A' ) 
 ( 'b' ) ). 
 
SELECT * 
       FROM @itab AS itab 
       ORDER BY table_line 
       INTO @FINAL(wa1). 
  out->write( wa1 ). 
ENDSELECT. 
 
out->line( ). 
 
SELECT * 
       FROM @itab AS itab 
       ORDER BY lower( table_line ) 
       INTO @FINAL(wa2). 
  out->write( wa2 ). 
ENDSELECT. 
 
out->display( ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a table with an elementary data type as the data source of two [`SELECT`](abapselect.md) statements. The `SELECT` statements can be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). In the second `SELECT` statement, a syntax error would occur without the alias name `number`, since the inline declaration after `INTO` cannot create an internal table with the column name `table_line`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA itab TYPE SORTED TABLE OF i WITH UNIQUE KEY table_line. 
itab =  VALUE #( ( 1 ) 
                 ( 2 ) 
                 ( 3 ) ). 
 
DATA result1 LIKE itab. 
SELECT table_line 
       FROM @itab AS numbers 
       INTO TABLE @result1. 
out->write( result1 ). 
 
SELECT table_line AS number 
       FROM @itab AS numbers 
       INTO TABLE @FINAL(result2). 
out->write( result2 ). 
 
out->display( ).
```

## Executable Examples

- [Internal Table as Data Source of a `SELECT` Statement](abenselect_from_itab_abexa.md)

- [Multiple Internal Tables as Data Sources of a `SELECT` Statement](abenselect_from_itab_multi_abexa.md)

- [Internal Table as a Data Source of the Hierarchy Generator](abenselect_from_itab_hiera_abexa.md)

See also:

- [ABAP SQL In-Memory Engine, Multiple Internal Tables](abenabap_sql_engine_abexa.md)

- [ABAP SQL In-Memory Engine, Restrictions](abenabap_sql_engine_restr_abexa.md)

- [ABAP SQL In-Memory Engine, Restriction to One Internal Table](abenabap_sql_engine_itab_abexa.md)
