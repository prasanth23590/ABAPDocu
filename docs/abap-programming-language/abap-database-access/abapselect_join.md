---
title: "SELECT, FROM JOIN"
source_file: abapselect_join.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses > SELECT, FROM"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, FROM JOIN

## Syntax

``` abap
... [(] {data_source [AS tabalias]}|join 
          {[INNER [cardinality]] JOIN}|{LEFT|RIGHT [OUTER [cardinality]] JOIN}|{CROSS JOIN} 
             {data_source [AS tabalias]}|join [ON sql_cond] [)] ... .  
```

[`data_source`](abapselect_data_source.md) · [`data_source`](abapselect_data_source.md) · [`sql_cond`](abenabap_sql_stmt_logexp.md)

### Addition

[1. `... ON sql_cond`](abapselect_join.md#addition-1)

[2. `... cardinality`](abapselect_join.md#addition-2)

## Overview

### Description

Joins the columns of two or more [data sources](abapselect_data_source.md) in a result set of a [query](../../abap-glossary/abenasql_query_glosry.md) in a join expression. A join expression joins a left side with a right side, using

- `[INNER] JOIN` ([inner join](../../abap-glossary/abeninner_join_glosry.md))

- `LEFT|RIGHT [OUTER] JOIN` ([outer join](../../abap-glossary/abenouter_join_glosry.md))

- `CROSS JOIN` ([cross join](../../abap-glossary/abencross_join_glosry.md))

Every join expression for an inner or outer join must contain a join condition [`sql_cond`](abenabap_sql_stmt_logexp.md) after `ON` (see below). A join expression for a cross join cannot contain any join conditions.

The following applies to possible specifications on the left side and on the right side:

- [`data_source`](abapselect_data_source.md) is a single data source. DDIC database tables must be [transparent](../../abap-glossary/abentransparent_table_glosry.md). As with the individual specification after [`FROM`](abapfrom_clause.md) using `AS`, an alias name can be specified for the data source. A data source can exist more than once within a join expression and must then be given different names.

- A join expression can be specified for `join` on both sides. A join expression can therefore be nested recursively. The number of data sources linked to each other is limited. The maximum number is set to allow the `SELECT` statement to be executed on all supported database systems and is currently 50. More than 49 joins, if known statically, produce a syntax error. If they are not known statically, they produce a runtime error.

The priority in which nested join expressions are evaluated is specified as follows:

- For inner and outer joins, the priority is determined by the position of the `ON` conditions. From left to right, each `ON` condition is assigned to the directly preceding `JOIN` and creates a join expression. Join expressions of this type can optionally be enclosed in parentheses, `( )`. Explicitly specified parentheses must match the parentheses specified implicitly by the `ON` conditions.

- By default, cross joins are evaluated from left to right. The priority of the evaluation can be affected by parentheses `( )`.

  - If multiple cross joins are combined, the order of the evaluation is irrelevant. The result is always the same and the number of rows is the product of the number of rows of all involved data sources.

  - If cross joins are combined with inner and outer joins, the result can depend on the order of evaluation or the parentheses.

**Result set for inner joins**

An inner join joins the columns of the rows in the result set of the left side with the columns of the rows in the result set of the right side into a single result set. This result set contains all combinations of rows for whose columns the join condition [`sql_cond`](abenabap_sql_stmt_logexp.md) is jointly true. If there are no rows in the result set of the left and right sides that meet `sql_cond`, no row is created in the resulting result set.

**Result set for outer joins**

The outer join creates the same result set as the inner join. The difference is that, for each selected row on the left side as `LEFT OUTER JOIN` or on the right side as `RIGHT OUTER JOIN`, at least one row is created in the result set, even if no rows on the other side meet the condition `sql_cond`. The columns on the other side that do not meet the condition [`sql_cond`](abenabap_sql_stmt_logexp.md) are filled with [null values](../../abap-glossary/abennull_value_glosry.md).

**Result set for cross join**

The cross join forms a cross product of the result set of the left side and the result set of the right side. The cross join joins the columns of the rows in the result set of the left side with the columns of the rows in the result set of the right side. This result set contains all possible combinations of rows. The number of rows in the result set of the cross join is the product of the number of rows of both joined result sets.

### Hints

- Certain restrictions apply to other clauses in the current `SELECT` statement when join expressions are used. For example, a join expression cannot be used together with the addition [`ORDER BY PRIMARY KEY`](abaporderby_clause.md). These restrictions are documented in the corresponding clauses.

- A `WHERE` condition for a `SELECT` statement with joins affects the result set created using the joins.

- An inner join or a cross join between two individual data sources is commutative. If the left and right side are switched, the result remains the same.

- A cross join behaves like an inner or outer join whose `ON` condition is always true. A cross join with a `WHERE` condition has the same result as an inner join with an identical `ON` condition. Unlike the inner join, in a cross join all data is read first before the condition is evaluated. In an inner join only data that meets the `ON` condition is read.

- A cross join should only be used with extreme caution. Since it is not possible to specify an `ON` condition, all data of all involved data sources is read. In the case of very large datasets, the result set, whose number of rows is always the product of the number of all rows of both data sources, can quickly become very large.

- A cross join of two client-dependent data sources is converted internally to an inner join, whose `ON` condition checks whether the client columns of the left and right side are equal. If one side is not client-dependent, the cross join is executed completely.

- If the same column name appears in multiple data sources of a single join expression, these sources must be identified in all other additions of the `SELECT` statement using the [column selector](../../abap-glossary/abentable_comp_selector_glosry.md) `~`.

- Only join expressions that access only [internal tables](abapselect_itab.md) but no database tables can be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). If a database table is joined, the ABAP SQL statement bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

- Join expressions should not be applied to buffered tables. Instead the addition [`FOR ALL ENTRIES`](abenwhere_all_entries.md) should be used, which can be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md).

- If columns from the right side are specified as `LEFT OUTER JOIN` or columns from the left side are specified as `RIGHT OUTER JOIN`, after the addition [`ORDER BY`](abaporderby_clause.md), the sort order can depend on the database system in the case of null values.

- The function [`coalesce`](abensql_coalesce.md) can be used to replace null values created due to an external join with other values or the result of expressions.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Join of the columns `CARRNAME`, `CONNID`, and `FLDATE` of the DDIC database tables `SCARR`, `SPFLI`, and `SFLIGHT` using two inner joins. This creates a list of flights from `CITYFROM` to `CITYTO`. Alternative names are used for each table.

``` abap
DATA: 
  cityfr TYPE spfli-cityfrom VALUE 'FRANKFURT', 
  cityto TYPE spfli-cityto   VALUE 'NEW YORK'. 
 
cl_demo_input=>new( 
  )->add_field( CHANGING field = cityfr 
  )->add_field( CHANGING field = cityto )->request( ). 
 
SELECT c~carrname, p~connid, f~fldate 
       FROM ( ( scarr AS c 
         INNER JOIN spfli AS p ON p~carrid   = c~carrid 
                              AND p~cityfrom = @cityfr 
                              AND p~cityto   = @cityto ) 
         INNER JOIN sflight AS f ON f~carrid = p~carrid 
                                AND f~connid = p~connid ) 
       ORDER BY c~carrname, p~connid, f~fldate 
       INTO TABLE @FINAL(itab).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Join of the database tables `SCARR` and `SPFLI` using a left outer join. For all flights not departing from `CITYFROM`, the value of the column `CONNID` is the null value. Due to the `WHERE` condition, all airlines that do not fly from `CITYFROM` are output.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA cityfr TYPE spfli-cityfrom VALUE 'FRANKFURT'. 
cl_demo_input=>request( CHANGING field = cityfr ). 
 
SELECT s~carrid, s~carrname 
       FROM scarr AS s 
       LEFT OUTER JOIN spfli AS p ON s~carrid   =  p~carrid 
                                  AND p~cityfrom = @cityfr 
       WHERE p~connid IS NULL 
       ORDER BY s~carrid, s~carrname 
       INTO TABLE @FINAL(itab). 
 
out->write( itab ). 
 
out->display( ).
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Cross join of two database tables. Without the `WHERE` condition, the result set would be very large.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DATA BEGIN OF wa. 
DATA mandt TYPE t000-mandt. 
DATA mtext TYPE t000-mtext. 
INCLUDE TYPE t100. 
DATA END OF wa. 
DATA itab LIKE STANDARD TABLE OF wa WITH EMPTY KEY. 
 
SELECT t000~mandt, t000~mtext, t100~* 
       FROM t000 CROSS JOIN t100 
       WHERE t100~arbgb = 'SABAPDEMOS' 
       ORDER BY t000~mandt, t100~sprsl, t100~msgnr 
       INTO TABLE @itab. 
 
out->write( itab ). 
 
out->display( ).
```

## Addition 1

`... ON sql_cond`

### Description

Join condition. A join condition must be specified for an inner or outer join. A join condition must not be specified for a cross join.

The syntax of the [relational expressions](abenabap_sql_stmt_logexp.md) of a join condition [`sql_cond`](abenabap_sql_stmt_logexp.md) is subject to the following restrictions:

- After `ON`, at least one comparison must be specified.

- The expression [`[NOT] IN range_tab`](abenwhere_logexp_seltab.md) cannot be used.

- [Subqueries](../../abap-glossary/abensubquery_glosry.md) cannot be used.

- [Path expressions](abenabap_sql_path.md) cannot be used.

- Within a [subquery](../../abap-glossary/abensubquery_glosry.md), only columns of the [data sources](abapselect_data_source.md) of this subquery can be specified.

- A dynamic condition [`(cond_syntax)`](abenwhere_logexp_dynamic.md) can be specified only if the [`FROM` clause](abapfrom_clause.md) is specified statically and is not specified dynamically as `(source_syntax)`.

A join condition is met if the logical expression `sql_cond` is true.

[Implicit ABAP SQL client handling](abenabap_sql_client_handling.md) applies. In joins between client-dependent tables, a comparison for equality between the client columns is added to the `ON` condition implicitly. The [client column](../../abap-glossary/abenclient_column_glosry.md) of a client-dependent data source cannot be used as an operand in the `ON` condition.

### Hints

- Comparisons between database columns or SQL expressions and database columns are performed on the database, which means it is essential that appropriate join conditions are formulated only between operands of the same type and the same length. This avoids the need for platform-dependent conversions.

- If the pattern consists of exactly one *%* character in a comparison using [`LIKE`](abenwhere_logexp_like.md), the same optimization takes place as for `WHERE`. The condition `col LIKE '%'` is always true, even if the column `col` contains [null values](../../abap-glossary/abennull_value_glosry.md).

- If one of the following two conditions apply:

  - [SQL expressions](../../abap-glossary/abensql_expression_glosry.md) are used on the left side of the `ON` condition of any join.

  - The expression [`IS [NOT] NULL`](abenwhere_logexp_null.md) is used in the `ON` condition of an outer join.

## Executable Examples

- [Inner, outer, and cross joins](abenjoins_abexa.md)

- [Multiple joins](abenjoin_joins_abexa.md)

## Addition 2

`cardinality`

### Description

Specifies the [cardinality](../../abap-glossary/abencardinality_glosry.md) `cardinality` of an inner, left outer, or right outer join. It has an effect only on certain specific database systems.

The following cardinality specifications are possible:

- `ONE TO ONE`

- `ONE TO MANY`

- `ONE TO EXACT ONE`

- `EXACT ONE TO ONE`

- `EXACT ONE TO MANY`

- `EXACT ONE TO EXACT ONE`

- `MANY TO ONE`

- `MANY TO MANY`

- `MANY TO EXACT ONE`

The cardinality specification documents the semantics of the data model. It is used by the [SAP HANA SQL Optimizer](../../abap-glossary/abenquery_optimizer_glosry.md) for performance optimizations by suppressing surplus joins on any databases that support this addition. It is important that the cardinality specification matches the data in question. Otherwise, the result is undefined and can depend on the entries in the [`SELECT` list](abapselect_list.md).

If no cardinality is specified, the implicit default cardinality is *many-to-many*.

### Hints

- For more information, see the documentation of the current database system. The [SAP HANA database](../../abap-glossary/abenhana_database_glosry.md), for example, supports the cardinality specification and its description is part of the documentation of [HANA-specific SQL](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/b4b0eec1968f41a099c828a4a6c8ca0f).

- To avoid undefined and platform-dependent behavior, a cardinality should be specified only if the data to be read meets the relevant prerequisites.

- The cardinality is mainly descriptive, not prescriptive. It does not force a matching result set.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Incorrect use of the cardinality `MANY TO ONE`. The data in the DDIC database tables `SCARR` and `SPFLI` do not have the [cardinality](../../abap-glossary/abencardinality_glosry.md) `MANY TO ONE`, but the reverse cardinality. On an SAP HANA database, for example, the result depends on the [`SELECT` list](abapselect_list.md). If the left and right side are specified here, no optimization takes place. If no columns are specified on the right side and the aggregate function [`COUNT(*)`](abensql_agg_func.md) is used as an aggregate expression, an optimization takes place. Here, only that data is read that meets the prerequisite cardinality.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
out->next_section( `Fields of left and right table` ). 
SELECT FROM scarr AS c 
              LEFT OUTER MANY TO ONE JOIN spfli AS p 
                ON c~carrid = p~carrid 
       FIELDS c~carrid   AS carrid, 
              c~carrname AS carrname, 
              p~connid   AS connid 
       ORDER BY c~carrid 
       INTO TABLE @DATA(itab). 
out->write( itab ). 
out->write( sy-dbcnt ). 
 
out->next_section( `Fields of left table only` ). 
SELECT FROM scarr AS c 
              LEFT OUTER MANY TO ONE JOIN spfli AS p 
                ON c~carrid = p~carrid 
       FIELDS c~carrid   AS carrid, 
              c~carrname AS carrname 
       ORDER BY c~carrid 
       INTO CORRESPONDING FIELDS OF TABLE @itab. 
out->write( itab ). 
out->write( sy-dbcnt ). 
 
out->next_section( `COUNT(*)` ). 
SELECT FROM scarr AS c 
              LEFT OUTER MANY TO ONE JOIN spfli AS p 
                ON c~carrid = p~carrid 
       FIELDS COUNT( * ) AS count 
       INTO @FINAL(count). 
out->write( count ). 
 
out->display( ).
```
