---
title: "UPDATE writable_obj"
source_file: abapupdate.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# UPDATE writable_obj

## Syntax

``` abap
UPDATE target source 
       [OPTIONS] 
         [CONNECTION ...].  
```

[`target`](abapiumd_target.md) · [`source`](abapupdate_source.md) · [`OPTIONS`](abapiumd_options.md) · [`CONNECTION ...`](abapiumd_conn.md)

## Description

The [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statement `UPDATE` changes the content of one or more rows of the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) specified in [`target`](abapiumd_target.md). The specifications in [`source`](abapupdate_source.md) determine which columns of which rows are changed, and how they are changed.

If `OPTIONS` is not used, `CONNECTION` can also be specified behind `target`.

## System Fields

The statement `UPDATE` sets the values of the system fields `sy-subrc` and `sy-dbcnt`.

| **`sy-subrc`** | **Meaning**                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | When `SET` was specified in `source`, at least one row was changed. When a work area was specified in `source`, the specified row was changed. When an internal table was specified in `source`, all specified rows were changed, or the internal table is empty.                                                                                                                                                                                                               |
| 2              | If a [LOB handle](../../abap-glossary/abenlob_handle_structure_glosry.md) structure with a component for [writer streams](../../abap-glossary/abenwriter_stream_glosry.md) or a reference variable for writer streams was specified after `SET`, the components that are not linked with writer streams were not yet written to the database, and instead are passed when the stream is closed at latest. Whether this situation occurs or not depends on the database system. See [LOB handles](abenium_lob.md). |
| 4              | When `SET` or a work area was specified in `source`, no row was changed; or when an internal table was specified in `source`, not all specified rows were changed. This is either because no suitable row was found, or because the change would create a row that would lead to duplicate entries in the [primary key](../../abap-glossary/abenprimary_key_glosry.md) or a unique [secondary index](../../abap-glossary/abensecondary_index_glosry.md) in the database table.                                      |

The statement `UPDATE` sets `sy-dbcnt` to the number of changed rows. If an overflow occurs because the number of rows is greater than 2,147,483,647, `sy-dbcnt` is set to -1. If `sy-subrc` is 2, `sy-dbcnt` is also set to the value -1 (for undefined).

## Hints

- The changes are committed to the database at the next [database commit](../../abap-glossary/abendatabase_commit_glosry.md). Until that point, they can still be undone using a [database rollback](../../abap-glossary/abendatabase_rollback_glosry.md). The current [isolation level](abendb_isolation.md) defines whether the modified data can no longer be read into other [database LUWs](../../abap-glossary/abendatabase_luw_glosry.md) before or only after the database commit.

- The number of rows that can be modified in the tables of a database within a [database LUW](../../abap-glossary/abendatabase_luw_glosry.md) is limited, since a database system can only manage a limited amount of locks and data in the rollback area.

- The statement `UPDATE` sets a [database lock](../../abap-glossary/abendatabase_lock_glosry.md) as an [exclusive lock](../../abap-glossary/abenexclusive_lock_glosry.md) until the next database commit or rollback.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The statement `UPDATE` overwrites the content of the columns of a CDS table entity row specified by a key with values from a work area created using the value operator `VALUE`.

``` abap
DELETE FROM demo_cds_te. 
INSERT demo_cds_te FROM @( VALUE #( key_element = 'A' ) ). 
 
UPDATE demo_cds_te FROM @( VALUE #( key_element = 'A' 
                                    col1 = 'aaa' 
                                    col2 = 1 
                                    col3 = 'A' ) ).
```
