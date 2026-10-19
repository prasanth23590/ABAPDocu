---
title: "INSERT writable_obj"
source_file: abapinsert_dbtab.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INSERT writable_obj

## Syntax

``` abap
INSERT { INTO target VALUES @wa|@( expr ) }   
     | {      target FROM @wa|@( expr ) [indicators]   } 
     | {      target FROM TABLE @itab [indicators]   } 
     | {      target FROM ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ) } 
       [OPTIONS] 
         [CONNECTION ...].  
```

[`target`](abapiumd_target.md) · [`@wa|@( expr )`](abapinsert_source.md) · [`target`](abapiumd_target.md) · [`@wa|@( expr )`](abapinsert_source.md) · [`indicators`](abapselect_indicators.md) · [`target`](abapiumd_target.md) · [`TABLE @itab`](abapinsert_source.md) · [`indicators`](abapselect_indicators.md) · [`target`](abapiumd_target.md) · [`( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] )`](abapinsert_source.md) · [`OPTIONS`](abapiumd_options.md) · [`CONNECTION ...`](abapiumd_conn.md)

### Variant

[1. `INSERT INTO target VALUES @wa|@( expr ).`](abapinsert_dbtab.md#variant-1)

[2. `INSERT target FROM @wa|@( expr ) [indicators].`](abapinsert_dbtab.md#variant-2)

[3. `INSERT target FROM TABLE @itab [indicators].`](abapinsert_dbtab.md#variant-3)

[4. `INSERT target FROM ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] )`](abapinsert_dbtab.md#variant-4)

## Overview

### Description

The [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statement `INSERT` inserts one or more rows into the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) specified in `target`. The rows to be inserted are taken from a work area [`wa`](abapinsert_source.md), an internal table [`itab`](abapinsert_source.md), or the result set of an embedded subquery [`SELECT subquery_clauses`](abapinsert_source.md).

If `OPTIONS` is not used, `CONNECTION` can also be specified behind `target`.

If `VALUES` is used, `INTO` must be specified between `INSERT` and [`target`](abapiumd_target.md). If `FROM` is used, `INTO` must not be specified.

### System Fields

The statement `INSERT` sets the values of the system fields `sy-subrc` (see below) and `sy-dbcnt`. `sy-dbcnt` is set to the number of rows that are inserted. If an overflow occurs because the number of rows is greater than 2,147,483,647, `sy-dbcnt` is set to -1. If `sy-subrc` is 2 when inserting a [LOB handle structure](../../abap-glossary/abenlob_handle_structure_glosry.md) with a component for [writer streams](../../abap-glossary/abenwriter_stream_glosry.md), `sy-dbcnt` is also set to -1 (meaning undefined).

### Hints

- The inserted rows are included permanently in the table in the next [database commit](../../abap-glossary/abendatabase_commit_glosry.md). Until then, they can still be removed by a [database rollback](../../abap-glossary/abendatabase_rollback_glosry.md). The current [isolation level](abendb_isolation.md) defines whether the inserted data can be read into other [database LUWs](../../abap-glossary/abendatabase_luw_glosry.md) before or only after the database commit.

- The number of rows that can be inserted into the tables of a database within a [database LUW](../../abap-glossary/abendatabase_luw_glosry.md) is limited on a database-dependent level, since a database system can only manage a limited amount of locks and data in the rollback area.

- Once rows have been inserted into a [global temporary table](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_gtt.md), this table must be emptied again explicitly before the next implicit [database commit](../../abap-glossary/abendatabase_commit_glosry.md) using the ABAP SQL statement [`DELETE FROM`](abapdelete_dbtab.md) without `WHERE` or using an explicit [database commit](abendb_commit.md) or [database rollback](abendb_rollback.md), otherwise the runtime error `COMMIT_GTT_ERROR` is produced.

- The statement `INSERT` sets a [database lock](../../abap-glossary/abendatabase_lock_glosry.md) as an [exclusive lock](../../abap-glossary/abenexclusive_lock_glosry.md) until the next database commit or rollback.

## Variant 1

`INSERT INTO target VALUES @wa|@( expr ).`

## Variant 2

`INSERT target FROM @wa|@( expr )[indicators].`

### Description

These two variants insert a single row contained in a work area [`wa`](abapinsert_source.md). Both variants have the same behavior and only their syntax is different.

### System Fields

These variants of the statement `INSERT` set the value of the system field `sy-subrc` as follows:

| **`sy-subrc`** | **Meaning**                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | The row specified in the work area in [`wa`](abapinsert_source.md) was inserted.                                                                                                                                                                                                                                                                                                               |
| 2              | When a [LOB handle structure](../../abap-glossary/abenlob_handle_structure_glosry.md) was specified with a component for [writer streams](../../abap-glossary/abenwriter_stream_glosry.md), the non-LOB handle components were not yet written to the database, and are passed, at the latest, when the stream is closed instead. Whether this situation occurs or not depends on the database. See [LOB handles](abenium_lob.md). |
| 4              | The row specified in the work area in [`wa`](abapinsert_source.md) was not inserted, since a row with the same [primary key](../../abap-glossary/abenprimary_key_glosry.md) or a unique [secondary index](../../abap-glossary/abensecondary_index_glosry.md) already exists in the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md).                                                                                    |

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Insertion of two individual rows into a CDS table entity.

``` abap
DELETE FROM demo_cds_te. 
 
DATA wa TYPE demo_cds_te. 
 
wa = VALUE #( key_element = 'A' col1 = 'aaa' ). 
INSERT INTO demo_cds_te VALUES @wa. 
 
wa = VALUE #( key_element = 'B' col1 = 'bbb' ). 
INSERT demo_cds_te FROM @wa.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A [host expression](../../abap-glossary/abenhost_expression_glosry.md) with the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) can be used instead of an explicit work area.

``` abap
DELETE FROM demo_cds_te. 
 
INSERT INTO demo_cds_te VALUES @( 
  VALUE #( key_element = 'A' col1 = 'aaa' ) ). 
 
INSERT demo_cds_te FROM @( 
  VALUE #( key_element = 'B' col1 = 'bbb' ) ).
```

## Variant 3

`INSERT target FROM TABLE @itab [indicators].`

### Description

This variant inserts the rows contained in an internal table [`itab`](abapinsert_source.md).

### Hint

There is no syntax variant with `VALUES` for internal tables.

### System Fields

This variant of the statement `INSERT` can raise exceptions if an attempt is made to insert rows from the internal table for which there are already rows with the same key in the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md). If no exception is raised, the value of the system field `sy-subrc` is set as follows:

| **`sy-subrc`** | **Meaning**                                                                                                                                                                                                                                                                                                                                                 |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | All rows of the internal table [`itab`](abapinsert_source.md) were inserted or the internal table is empty.                                                                                                                                                                                                                                               |
| 4              | The addition [`ACCEPTING DUPLICATE KEYS`](abapinsert_source.md) is specified and not all rows of the internal table were inserted, since a row with the same [primary key](../../abap-glossary/abenprimary_key_glosry.md) or a unique [secondary index](../../abap-glossary/abensecondary_index_glosry.md) already exists in the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md). |

For more information about exceptions when inserting rows from internal tables, see [`TABLE itab`](abapinsert_source.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Insertion of two individual rows into a CDS table entity.

``` abap
DELETE FROM demo_cds_te. 
 
DATA itab TYPE TABLE OF demo_cds_te. 
 
itab = VALUE #( ( key_element = 'A' col1 = 'aaa' ) 
                ( key_element = 'B' col1 = 'bbb' ) ). 
INSERT demo_cds_te FROM TABLE @itab.
```

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

A [host expression](../../abap-glossary/abenhost_expression_glosry.md) with the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) can be used instead of an explicit internal table.

``` abap
DELETE FROM demo_cds_te. 
 
INSERT demo_cds_te FROM TABLE @( 
  VALUE #( ( key_element = 'A' col1 = 'aaa' ) 
           ( key_element = 'B' col1 = 'bbb' ) ) ).
```

## Variant 4

`INSERT target FROM ( SELECT subquery_clauses [UNION|INTERSECT|EXCEPT ...] ).`

### Description

This variant inserts the rows of the [result set](abapinsert_from_select.md) of an embedded [subquery](../../abap-glossary/abensubquery_glosry.md) [`SELECT subquery_clauses`](abapinsert_source.md), where multiple result sets can be joined with [`UNION`](abapunion.md), [`INTERSECT`](abapunion.md), or [`EXCEPT`](abapunion.md).

### System Fields

This variant of the statement `INSERT` sets the value of the system field `sy-subrc` as follows:

| **`sy-subrc`** | **Meaning**                                                                 |
|----------------|-----------------------------------------------------------------------------|
| 0              | All rows of the result set of the embedded subquery were inserted.          |
| 4              | The result set of the embedded subquery is empty and no rows were inserted. |

### Hints

- The statement `INSERT` with subquery cannot be used if [logging](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_protocol.md) is enabled for the table to be filled.

- If a row cannot be inserted when the result set of the embedded subquery was inserted, since a row with the same primary key or the same unique secondary index already exists, a catchable exception of the class `CX_SY_OPEN_SQL_DB` is always raised and the system field `sy-subrc` is not set.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Insertion of all rows of the CDS table entity `DEMO_CDS_JOIN1_TE` into the table `DEMO_CDS_JOIN3_TE`.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
DELETE FROM demo_cds_join1_te. 
INSERT demo_cds_join1_te 
  FROM TABLE @( VALUE #( ( a = 'a1' b = 'b1' c = 'c1' d = 'd1' ) 
                         ( a = 'a2' b = 'b2' c = 'c2' d = 'd2' ) 
                         ( a = 'a3' b = 'b3' c = 'd3' d = 'd3' ) ) ). 
 
DELETE FROM demo_cds_join3_te. 
INSERT demo_cds_join3_te  FROM ( SELECT * FROM demo_cds_join1_te ). 
 
SELECT * 
       FROM demo_cds_join3_te 
       INTO TABLE @FINAL(result). 
 
out->write( result ). 
 
out->display( ).
```
