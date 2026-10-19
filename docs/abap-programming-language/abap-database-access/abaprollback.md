---
title: "ROLLBACK WORK"
source_file: abaprollback.html
section: "ABAP Programming Language > ABAP - Database Access > Data Consistency > SAP LUW"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ROLLBACK WORK

## Syntax

``` abap
ROLLBACK WORK.  
```

## Description

The statement `ROLLBACK WORK` closes the current [SAP LUW](../../abap-glossary/abensap_luw_glosry.md) and opens a new one.

## Hints

- After a `ROLLBACK` statement is executed, `sy-subrc` is always zero. It is not necessary to query whether `sy-subrc` is not equal to zero after `ROLLBACK`.

- The `ROLLBACK WORK` statement is executed implicitly if a [message](../../abap-glossary/abenmessage_glosry.md) of type A is handled by the addition `error_message` when calling a function module with `CALL FUNCTION`.

- `ROLLBACK WORK` empties [global temporary tables](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_gtt.md) of all currently open [database connections](../../abap-glossary/abendatabase_connection_glosry.md) and prevents the runtime error `COMMIT_GTT_ERROR` in the case of implicit [database commits](abendb_commit.md).

- All open [database cursors](../../abap-glossary/abendatabase_cursor_glosry.md) in the database connections concerned are closed during a `ROLLBACK`, which means that a runtime error occurs when the system attempts to continue a `SELECT` loop after a `ROLLBACK`. It must therefore be ensured that cursors that are still open are no longer used after the `ROLLBACK`.

## Executable Example

The example Demonstrating the SAP LUW demonstrates the SAP LUW, covering the `ROLLBACK WORK` statement.
