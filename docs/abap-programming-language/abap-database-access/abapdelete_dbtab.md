---
title: "DELETE writable_obj"
source_file: abapdelete_dbtab.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DELETE writable_obj

## Syntax

``` abap
DELETE { FROM target [WHERE sql_cond] [db_hints] 
                     [ORDER BY ... [OFFSET o]] [UP TO n ROWS]   } 
     | { target FROM source } 
         [OPTIONS] 
         [CONNECTION ...].  
```

[`target`](abapiumd_target.md) · [`WHERE sql_cond`](abapdelete_where.md) · [`db_hints`](abenabap_sql_db_hints.md) · [`[ORDER BY ... [OFFSET o]] [UP TO n ROWS`](abapdelete_where.md) · [`target`](abapiumd_target.md) · [`source`](abapdelete_source.md) · [`OPTIONS`](abapiumd_options.md) · [`CONNECTION ...`](abapiumd_conn.md)

### Variant

[1. `DELETE FROM target ...`](abapdelete_dbtab.md#variant-1)

[2. `DELETE target FROM source ...`](abapdelete_dbtab.md#variant-2)

## Overview

### Description

The [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statement `DELETE` deletes one or more rows from the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) specified in `target`. The rows to be deleted can be specified as follows:

- In a variant `DELETE FROM target` using [conditions](abapdelete_where.md)

- In a variant `DELETE target FROM` using data objects in [`source`](abapdelete_source.md)

If `OPTIONS` is not used, `CONNECTION` can also be specified behind `target`.

### System Fields

The statement `DELETE` sets the values of the system fields `sy-subrc` and `sy-dbcnt`.

| **`sy-subrc`** | **Meaning**                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0              | In the variant `DELETE FROM target`, at least one row was deleted if a `WHERE` condition was specified and all or `n` rows were deleted if no condition was specified. In the variant `DELETE target FROM`, the specified row was deleted if a work area was specified in `source` and all specified rows were deleted if an internal table was specified in `source` or the internal table is empty. |
| 4              | In the variant `DELETE FROM target`, no row was deleted if a `WHERE` condition was specified or no row was deleted if no condition was specified, since the database table was already empty. In the variant `DELETE target FROM`, no row was deleted if a work area was specified in `source` or not all specified rows were deleted if an internal table was specified in `source`.                 |

The statement `DELETE` sets `sy-dbcnt` to the number of deleted rows. If an overflow occurs because the number of rows is greater than 2,147,483,647, `sy-dbcnt` is set to -1.

### Hints

- The rows are deleted permanently from the [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md) in the next [database commit](../../abap-glossary/abendatabase_commit_glosry.md). Until that point, they can still be undone using a [database rollback](../../abap-glossary/abendatabase_rollback_glosry.md). The current [isolation level](abendb_isolation.md) defines whether the deleted data can no longer be read into other [database LUWs](../../abap-glossary/abendatabase_luw_glosry.md) before or only after the database commit.

- The number of rows that can be deleted from the tables of a database within a [database LUW](../../abap-glossary/abendatabase_luw_glosry.md) is limited, since a database system can only manage a limited amount of locks and data in the rollback area.

- The statement `DELETE FROM writable_obj` has the statement [`DELETE FROM itab`](../abap-processing-internal-data/abapdelete_itab_lines.md) with identical syntax. If an internal table has the same name as a [writable database object](../../abap-glossary/abenwritable_db_obj_glosry.md), a statement like this accesses the internal table.

- The statement `DELETE` sets a [database lock](../../abap-glossary/abendatabase_lock_glosry.md) as an [exclusive lock](../../abap-glossary/abenexclusive_lock_glosry.md) until the next database commit or rollback.

## Variant 1

`DELETE FROM target ...`

### Description

In the variant `DELETE FROM target`, either all rows are deleted or the rows to be deleted are restricted using a [`WHERE` condition](abapdelete_where.md) or additions [`ORDER BY`](abapdelete_where.md), [`OFFSET`](abapdelete_where.md), and [`UP TO`](abapdelete_where.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deletion of a row in a CDS table entity. The row is specified using a `WHERE` condition.

``` abap
DELETE FROM demo_cds_update_te WHERE id = 'X'.
```

## Variant 2

`DELETE target FROM source ...`

### Description

In the variant `DELETE target FROM`, either a row specified by a [work area](abapdelete_source.md) is deleted or multiple rows specified by an [internal table](abapdelete_source.md) are deleted.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Deletion of a row in a CDS table entity. The row is specified using a work area.

``` abap
DELETE demo_cds_update_te FROM @( VALUE #( id = 'X' ) ).
```
