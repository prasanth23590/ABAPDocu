---
title: "MODIFY writable_obj"
source_file: abapmodify_dbtab.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MODIFY writable_obj

## Syntax

``` abap
MODIFY   target FROM source 
       [OPTIONS] 
         [CONNECTION ...] 
 ...  
```

[`target`](abapiumd_target.md) · [`source`](abapmodify_source.md) · [`OPTIONS`](abapiumd_options.md) · [`CONNECTION ...`](abapiumd_conn.md)

## Description

The [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statement `MODIFY` inserts one or more rows specified in `source` into the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) specified in `target`, or overwrites existing rows.

If `OPTIONS` is not used, `CONNECTION` can also be specified behind `target`.

## System Fields

The statement `MODIFY` sets the values of the system fields `sy-subrc` and `sy-dbcnt`.

| **`sy-subrc`** | **Meaning**                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | When a work area was specified in `source`, the specified row was inserted or modified. When an internal table was specified in `source`, all specified rows were inserted or modified, or the internal table is empty.                                                                                                                                                                        |
| 2              | When a [LOB handle structure](../../abap-glossary/abenlob_handle_structure_glosry.md) was specified with a component for [writer streams](../../abap-glossary/abenwriter_stream_glosry.md), the non-LOB handle components were not yet written to the database, and instead are passed when the stream is closed at the latest. Whether this situation occurs or not depends on the database. See [LOB handles](abenium_lob.md). |
| 4              | When a work area or a subquery was specified in `source`, no rows were processed, or when an internal table was specified in `source`, not all specified rows were processed because there is already a row with the same unique [secondary index](../../abap-glossary/abensecondary_index_glosry.md) in the database table.                                                                                     |

The statement `MODIFY` sets `sy-dbcnt` to the number of processed rows. If an overflow occurs because the number of rows is greater than 2,147,483,647, `sy-dbcnt` is set to -1. If `sy-subrc` is 2, `sy-dbcnt` is also set to the value -1 (for undefined).

## Hints

- The changes are finally applied to the database at the next [database commit](../../abap-glossary/abendatabase_commit_glosry.md). Until that point, they can still be undone using a [database rollback](../../abap-glossary/abendatabase_rollback_glosry.md). The current [isolation level](abendb_isolation.md) defines whether the modified data can no longer be read into other [database LUWs](../../abap-glossary/abendatabase_luw_glosry.md) before or only after the database commit.

- The number of rows that can be inserted or modified in the tables of a database within a [database LUW](../../abap-glossary/abendatabase_luw_glosry.md) is limited, since a database system can only manage a limited amount of locks and data in the rollback area.

- Once rows have been inserted into a [global temporary table](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_gtt.md), this table must be emptied again explicitly before the next implicit [database commit](../../abap-glossary/abendatabase_commit_glosry.md) using the ABAP SQL statement [`DELETE FROM`](abapdelete_dbtab.md) without `WHERE` or using an explicit [database commit](abendb_commit.md) or [database rollback](abendb_rollback.md). If not, the runtime error `COMMIT_GTT_ERROR` is produced.

- The statement `MODIFY writable_obj FROM wa` has the statement [`MODIFY itab FROM wa`](../abap-processing-internal-data/abapmodify_itab_single.md) with identical syntax. If an internal table has the same name as a [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md), a statement like this accesses the internal table.

- The statement `MODIFY` sets a [database lock](../../abap-glossary/abendatabase_lock_glosry.md) as an [exclusive lock](../../abap-glossary/abenexclusive_lock_glosry.md) until the next database commit or rollback.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first `MODIFY` statement inserts a row into an empty table. The second `MODIFY` statement modifies the values of the non-key fields of this row and inserts two additional rows.

``` abap
DELETE FROM demo_update. 
 
MODIFY demo_update FROM @( 
  VALUE #(  id = 'X' col1 = 10 col2 = 20 col3 = 30 col4 = 40 ) ). 
 
MODIFY demo_update FROM TABLE @( 
  VALUE #( ( id = 'X' col1 =  1 col2 =  2 col3 =  3 col4 =  4 ) 
           ( id = 'Y' col1 = 11 col2 = 12 col3 = 13 col4 = 14 ) 
           ( id = 'Z' col1 = 21 col2 = 22 col3 = 23 col4 = 24 ) ) ).
```
