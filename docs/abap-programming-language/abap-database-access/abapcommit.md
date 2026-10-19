---
title: "COMMIT WORK"
source_file: abapcommit.html
section: "ABAP Programming Language > ABAP - Database Access > Data Consistency > SAP LUW"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# COMMIT WORK

## Syntax

``` abap
 COMMIT WORK [AND WAIT].  
```

## Description

The statement `COMMIT WORK` closes the current [SAP LUW](../../abap-glossary/abensap_luw_glosry.md) and opens a new one.

## Hints

- An SAP LUW not closed by `COMMIT WORK` but by ending the current program or closing the [internal session](../../abap-glossary/abeninternal_session_glosry.md) is ignored by the registered procedures. Registered update function modules remain on the database but can no longer be executed.

- `COMMIT WORK` empties [global temporary tables](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_gtt.md) of all currently open [database connections](../../abap-glossary/abendatabase_connection_glosry.md) when the database transaction ends. It is still advisable to explicitly clear global temporary tables before executing `COMMIT WORK`. This prevents code in perform-on-commit routines from triggering implicit [database commits](abendb_commit.md) that could cause the `COMMIT_GTT_ERROR` runtime error.

- The statement `COMMIT WORK` closes all [database cursors](../../abap-glossary/abendatabase_cursor_glosry.md). ABAP SQL statements that access a database cursor later ([`SELECT`](abapselect.md) loop) raise a uncatchable exception.

- Using `COMMIT WORK` and `COMMIT WORK AND WAIT` in [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md): `COMMIT WORK` and `COMMIT WORK AND WAIT` are primarily used in [classic ABAP](../../abap-glossary/abenclassic_abap_glosry.md), where update function modules are available, among others. In ABAP Cloud, local updates are always enforced implicitly and automatically, meaning updates occur in the same [work process](../../abap-glossary/abenwork_process_glosry.md) and are always synchronous. As a result, `COMMIT WORK` and `COMMIT WORK AND WAIT` function identically in ABAP Cloud, making the choice between them irrelevant. Typically, `COMMIT WORK` in ABAP Cloud returns a value of *0* for `sy-subrc`. Any other value would mean a runtime error.
