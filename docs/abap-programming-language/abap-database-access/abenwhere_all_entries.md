---
title: "SELECT, FOR ALL ENTRIES"
source_file: abenwhere_all_entries.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FOR ALL ENTRIES

## Syntax

``` abap
... FOR ALL ENTRIES IN @itab WHERE ... col operator @itab-comp ...  
```

[`operator`](abenwhere_logexp_compare.md)

## Description

If the addition `FOR ALL ENTRIES` is specified in front of the language element [`WHERE`](abapwhere.md) of the statement `SELECT` of a [main query](../../abap-glossary/abenmainquery_glosry.md), the components `comp` of the internal table [`itab`](abenabap_sql_host_variables.md) specified here as a [host variable](abenabap_sql_host_variables.md) can be used in [relational expressions](abenabap_sql_stmt_logexp.md) within [`sql_cond`](abenabap_sql_stmt_logexp.md) on the right side of a [comparison operator](abenwhere_logexp_compare.md) in comparisons with a [column](abenabap_sql_columns.md) `col`. The specified component `comp` must be compatible with the column `col`. The internal table `itab` can have a structured or an elementary row type. For an elementary row type, the [pseudo component](../../abap-glossary/abenpseudo_component_glosry.md) `table_line` must be specified for `comp`.

The entire logical expression [`sql_cond`](abenabap_sql_stmt_logexp.md) is evaluated for each individual row of the internal table `itab`. The result set of the `SELECT` statement is the union set of the result sets produced by the individual evaluations. Rows that occur more than once are removed from the result set automatically. The entire contents of a row are considered here.

**Caution**

If the internal table `itab` is empty, the entire `WHERE` condition is ignored. This means that none of the rows in the database table are skipped and are placed in the result set once any duplicate rows are removed.

The logical expression [`sql_cond`](abenasql_cond.md) of the `WHERE` condition can comprise multiple [relational expressions](abenabap_sql_stmt_logexp.md) using `AND` and `OR`. However, if `FOR ALL ENTRIES` is specified, there must be at least one [comparison](abenwhere_logexp_compare.md) with a column of the internal table `itab` that can be specified statically or dynamically.

The following restrictions apply when using the addition `FOR ALL ENTRIES` with other additions:

- The addition `FOR ALL ENTRIES` is only possible in front of `WHERE` conditions in a standalone [`SELECT`](abapselect.md) statement or in the [main query](../../abap-glossary/abenmainquery_glosry.md) after `OPEN CURSOR`, if no common table expressions are defined using [`WITH`](abapwith.md).

- The addition `FOR ALL ENTRIES` cannot be used with the addition [`SINGLE`](abapselect_single.md).

- The addition `FOR ALL ENTRIES` cannot be used in combination with [SQL expressions](abapsql_expr.md), except for columns specified individually or an aggregate expression `COUNT( * )` specified individually.

- If the addition `FOR ALL ENTRIES` is used, no [LOB handles](abenselect_into_lob_handles.md) can be created as [reader streams](../../abap-glossary/abenreader_stream_glosry.md) or as [locators](../../abap-glossary/abenlocator_glosry.md) in the [target area](abapinto_clause.md) of a standalone [`SELECT`](abapselect.md) statement.

- The addition `FOR ALL ENTRIES` cannot be combined with [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), and [`EXCEPT`](abapunion.md).

- In a `SELECT` statement with `FOR ALL ENTRIES`, no aggregate expressions except for `COUNT( * )` can be used in the [`SELECT` list](abapselect_list.md). In cases like these, the aggregate expression is not evaluated in the database, but is emulated on the AS ABAP.

- The addition `FOR ALL ENTRIES` should not be used with the addition [`GROUP BY`](abapgroupby_clause.md). The addition `GROUP BY` has no effect if `FOR ALL ENTRIES` is used.

- In a `SELECT` statement with `FOR ALL ENTRIES`, the addition [`ORDER BY`](abaporderby_clause.md) can only be used with the addition `PRIMARY KEY` and can only be used to access a single table or view. In this case, all columns of the primary key must be in the [`SELECT` list](abapselect_list.md), except for the client column in client-dependent tables.

- No [path expressions](abenabap_sql_path.md) can be used in a `SELECT` statement with `FOR ALL ENTRIES`.

- If the addition `FOR ALL ENTRIES` is used, the [`SELECT` list](abapselect_list.md) should not contain any database fields of the built-in types `STRING`, `RAWSTRING`, and `GEOM_EWKB` as well as `LCHR` and `LRAW`. These data types prevent rows that occur more than once on the database system from being removed. These rows are only removed from the result set on the AS ABAP. If listed in the `SELECT` list, a syntax check warning is raised that can be hidden by a pragma.

- If the addition `FOR ALL ENTRIES` is used, the `SELECT` list should not return records that differ only in `NULL` versus `INITIAL` values. Depending on whether duplicate elimination occurs before or after converting `NULL` to the ABAP representation, this may result in either one or two records in the result set. The specific behavior may change based on the applied filter conditions, configuration settings, and kernel release. If necessary, additional duplicate elimination in ABAP must be performed on the result.

The internal table `itab` is evaluated once for each query. Any changes made to the contents of the internal table in a `SELECT` loop or `WITH` loop are ignored by the logical expression.

## Hints

- The same internal table can be specified after `FOR ALL ENTRIES` and after [`INTO`](abapinto_clause.md). The contents of the table are evaluated by `FOR ALL ENTRIES` and then overwritten by the [`INTO` clause](abapinto_clause.md).

- A comparison with a column of an internal table can also be performed using the `WHERE` condition of a [subquery](../../abap-glossary/abensubquery_glosry.md) for the same [data source](abapselect_data_source.md).

- `FOR ALL ENTRIES` attempts to eliminate duplicate row values from the result set through a combination of applying distinct semantics on the database query, using declared primary key information, and optional post-filtering on the result set on the application server. This post-filtering occurs, for example, when fields of types `STRING`, `RAWSTRING`, `LCHR` or `LRAW` are selected, or when the statement is distributed to multiple SQL statements. If primary key definitions are effectively unique, the select fields content follows ABAP semantics and contain or produce no null values (even with Access Control Lists present), and results match `DISTINCT` database behavior.

- If duplicate rows are only removed from AS ABAP, all rows specified by the `WHERE` condition (in some cases) are passed to an internal system table and then aggregated. The [maximum size](../abap-data-types-and-data-objects/abenmemory_consumption_2.md) of this system table is restricted to that of regular internal tables. More specifically, the system table is always required if one of the additions [`PACKAGE SIZE`](abapinto_clause.md), [`UP TO`](abapselect_up_to_offset.md), or [`OFFSET`](abapselect_up_to_offset.md) is used simultaneously. These then have no effect on the number of rows passed from the database server to AS ABAP but are only used when the rows are passed from the system table to the actual target area. If the maximum size of the internal system table is exceeded, a runtime error occurs.

- If the column types allow it, the addition [`DISTINCT`](abapselect_clause.md) might be used together with `FOR ALL ENTRIES` in order to explicitly express the behavior.

- The addition `FOR ALL ENTRIES` can be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md) for

- accessing the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table with [`FROM @itab`](abapselect_itab.md). The [table buffer](../../abap-glossary/abentable_buffer_glosry.md) is bypassed only for tables with generic buffering if the condition after `FOR ALL ENTRIES` prevents a single generic area from being specified exactly.

- For buffered tables, the addition `FOR ALL ENTRIES` can be a more efficient alternative to [join expressions](../../abap-glossary/abenjoin_expression_glosry.md).

- It is strongly recommended that the internal table `itab` is not initial before using it after `FOR ALL ENTRIES`. In case of an initial internal table, all rows are read from the database regardless of any further conditions specified after `WHERE`, which is generally not desired.

- It depends on the database platform and different settings, how the contents of the internal table are passed to the database and where they are transformed into conditions. If [FDA](../../abap-glossary/abenfast_data_access_glosry.md) write access is available, it can be used by `FOR ALL ENTRIES`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Gets all flight data for a specified departure city. The relevant airlines and flight numbers are first passed to an internal table `entry_tab`, which is evaluated in the `WHERE` condition of the subsequent `SELECT` statement. This selection could also be carried out in a single `SELECT` statement by using a join in the [`FROM` clause](abapfrom_clause.md). The table `entry_tab` must not be initial before the `SELECT` statement is executed using `FOR ALL ENTRIES`. The addition [`DISTINCT`](abapselect_clause.md) is used to explicitly express the implicit behavior.

``` abap
DATA city TYPE spfli-cityfrom VALUE 'FRANKFURT'. 
cl_demo_input=>request( CHANGING field = city ). 
 
SELECT carrid, connid 
       FROM spfli 
       WHERE cityfrom = @( to_upper( city ) ) 
       INTO TABLE @FINAL(entry_tab). 
 
IF entry_tab IS NOT INITIAL. 
  SELECT DISTINCT 
         carrid, connid, fldate 
         FROM sflight 
         FOR ALL ENTRIES IN @entry_tab 
         WHERE carrid = @entry_tab-carrid AND 
               connid = @entry_tab-connid 
         ORDER BY PRIMARY KEY 
         INTO TABLE @FINAL(result_tab). 
  cl_demo_output=>display( result_tab ). 
ENDIF.
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of `FOR ALL ENTRIES` with an empty internal table. All rows of the DDIC database table are read. The number of read rows is usually smaller in the second `SELECT` statement than in the first statement. This is because only one column is read, and hence more duplicate rows can be removed. The first `SELECT` statement, on the other hand, reads all rows of the DDIC database table to the result set, since the columns cover the entire table key.

``` abap
DATA carriers TYPE TABLE OF scarr. 
 
SELECT carrid, connid 
       FROM spfli 
       FOR ALL ENTRIES IN @carriers 
       WHERE carrid = @carriers-carrid 
       INTO TABLE @FINAL(result1). 
cl_demo_output=>write( result1 ). 
 
SELECT carrid 
       FROM spfli 
       FOR ALL ENTRIES IN @carriers 
       WHERE carrid = @carriers-carrid 
       INTO TABLE @FINAL(result2). 
cl_demo_output=>display( result2 ).
```
