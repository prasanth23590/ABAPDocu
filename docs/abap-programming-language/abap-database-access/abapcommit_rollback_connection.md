---
title: "COMMIT, ROLLBACK CONNECTION"
source_file: abapcommit_rollback_connection.html
section: "ABAP Programming Language > ABAP - Database Access > Data Consistency > Database LUW"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# COMMIT, ROLLBACK CONNECTION

## Syntax

``` abap
COMMIT|ROLLBACK CONNECTION @con_ref...  
```

### Variant

[1. `... @con_ref`](abapcommit_rollback_connection.md#variant-1)

[2. `... con|(con_syntax)`](abapcommit_rollback_connection.md#variant-2)

## Overview

### Description

This `COMMIT` or `ROLLBACK` statement performs a [database commit](abendb_commit.md) or [database rollback](abendb_rollback.md) on the specified [database connection](../../abap-glossary/abendatabase_connection_glosry.md).

### Hints

- Detailed information about database connections can be found under [Database Connections](abendb_connections.md).

- It is important to note that the statements `COMMIT CONNECTION` and `ROLLBACK CONNECTION` when used for the standard connection, perform a pure database commit or rollback. Unlike [`COMMIT WORK`](abapcommit.md) and [`ROLLBACK WORK`](abaprollback.md), they do not close the current [SAP LUW](../../abap-glossary/abensap_luw_glosry.md).

- The statements `COMMIT CONNECTION` and `ROLLBACK CONNECTION` change the state of an active [service connection](../../abap-glossary/abenservice_connection_glosry.md) to inactive. A subsequent use of such a connection in the same internal session opens a new database LUW.

- The statements `COMMIT CONNECTION` and `ROLLBACK CONNECTION` are suitable for a simple close of a database LUW.

- The statements `COMMIT CONNECTION` and `ROLLBACK CONNECTION` empty [global temporary tables](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables_gtt.md) on a service connection and prevent the runtime error `COMMIT_GTT_ERROR` in implicit [database commits](abendb_commit.md) on this connection.

## Variant 1

`... @con_ref`

### Description

In this variant, that is available in [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md), the database connection is specified using an [ABAP SQL connection object](../../abap-glossary/abenabap_sql_conn_obj_glosry.md). The operand `con_ref` must be a reference variable of the [static type](../../abap-glossary/abenstatic_type_glosry.md) [`IF_ABAP_SQL_CONNECTION`](abenif_abap_sql_connection.md) or a class or interface that implements that interface. The reference variable must point to a valid ABAP SQL connection object that represents an open database connection, otherwise the uncatchable exception `DBSQL_INVALID_CONNECTION_OBJ` occurs.

### Hints

- ABAP SQL connection objects that represent valid database connections can only be created with APIs released by SAP, such as `CL_ABAP_SQL_CONNECTION_BUILDER`.

- The statements `COMMIT|ROLLBACK CONNECTION @con_ref` have the same effect as calling the methods `COMMIT` or `ROLLBACK` of the connection object.

- The character `@` in front of `con_ref` demands that a [reference variable](../../abap-glossary/abenreference_variable_glosry.md) `con_ref` that can be cast to `IF_ABAP_SQL_CONNECTION` is available.

### Executable Example

See [ABAP SQL - Connection Objects](abenif_abap_sql_connection_abexa.md)

## Variant 2

`... con|(con_syntax)`

\*\* This syntax is not available in the current ABAP language version.\*\*
