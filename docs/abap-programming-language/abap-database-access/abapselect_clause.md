---
title: "SELECT, select_clause"
source_file: abapselect_clause.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Read Access with DQL > SELECT, clauses"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# SELECT, select_clause

## Syntax

``` abap
... [DISTINCT] select_list ...  
```

[`select_list`](abapselect_list.md)

### Addition

[`... DISTINCT`](abapselect_clause.md#addition)

## Overview

### Description

`SELECT` clause of a [query](../../abap-glossary/abenasql_query_glosry.md). The `SELECT` clause defines the structure of the result set of the `SELECT` statement. It consists of a [`SELECT` list](abapselect_list.md), which defines the columns of the result set, and an optional addition `DISTINCT`, which removes duplicative rows from the result set.

The `SELECT` list [`select_list`](abapselect_list.md) can indicate all columns of a data source using `*` or it defines the individual columns of the result set using an [SQL expression](abapsql_expr.md). It defines the names of the columns in the result set, using optional or mandatory alias names.

### Hint

The `SELECT` clause must either be listed as the first clause after the keyword `SELECT`, or after the optional addition `SINGLE`, or after the `FROM` clause. After the `FROM` clause, the `SELECT` clause must be introduced using the addition [`FIELDS`](abapselect.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

`SELECT` clause after `FIELDS`, whose `SELECT` list contains individual columns as well as aggregate expressions with SQL expressions used as arguments.

``` abap
SELECT FROM sflight 
       FIELDS carrid, 
              connid, 
              MAX( seatsmax - seatsocc ) AS seatsfree_max, 
              MIN( seatsmax - seatsocc ) AS seatsfree_min 
       GROUP BY carrid, connid 
       HAVING carrid = CHAR`LH` 
       INTO TABLE @FINAL(result).
```

## Addition

`... DISTINCT`

### Description

The addition `DISTINCT` removes rows that occur more than once in a multirow result set. Here, the entire row content is respected.

The addition `DISTINCT` must not be used in the following cases:

- If the addition [`SINGLE`](abapselect_single.md) is used.

- If a column specified in the `SELECT` list [`select_list`](abapselect_list.md) has the type `STRING`, `RAWSTRING`, `LCHR`, `LRAW`, or `GEOM_EWKB`.

`DISTINCT` cannot be processed by the [ABAP SQL in-memory engine](abenabap_sql_inmemeng.md). The ABAP SQL statement bypasses the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) and an internal table accessed by [`FROM @itab`](abapselect_itab.md) must be transported to the database. This is only possible for one internal table per ABAP SQL statement.

### Hints

- For the addition `DISTINCT`, it is not important which columns of the result set are key fields of the associated DDIC database tables, views, or CDS entities.

- The comparison is based on the entire row content that is needed to identify a row. That means that the number of rows in the result set depends on the [`SELECT` list](abapselect_list.md). If, for example, all key fields of a DDIC database table are specified directly as `columns` in a [`SELECT`](abenabap_sql_columns.md) list, there can be no rows that occur more than once. The other extreme is the case where a `SELECT` list contains a single [host variable](abenabap_sql_host_variables.md) or a single literal. Here, all rows are deleted except one.

- While for an access to a single data sources it is sufficient to evaluate the key fields, for an access to joined data sources, a comparison of all columns of the result set can be needed.

- As a part of the `SELECT` clause, the addition `DISTINCT` has an effect before the additions [`UP TO`](abapselect_up_to_offset.md) and [`OFFSET`](abapselect_up_to_offset.md) are evaluated.

- If `DISTINCT` is specified, it should be noted that this requires the execution of sort operations in the database system, and the statement `SELECT` therefore bypasses [table buffering](../../abap-glossary/abentable_buffering_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Output of all destinations to which Lufthansa flies from Frankfurt.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
SELECT DISTINCT cityto 
       FROM spfli 
       WHERE carrid   = 'LH' AND 
             cityfrom = 'FRANKFURT' 
       INTO TABLE @FINAL(destinations). 
 
out->write( destinations ). 
 
out->display( ).
```
