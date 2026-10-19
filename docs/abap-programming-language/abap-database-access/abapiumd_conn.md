---
title: "INSERT, UPDATE, MODIFY, DELETE writable_obj, CONNECTION"
source_file: abapiumd_conn.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Write Access with DML > INSERT, UPDATE, MODIFY, DELETE writable_obj, OPTIONS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# INSERT, UPDATE, MODIFY, DELETE writable_obj, CONNECTION

## Syntax

``` abap
... CONNECTION @con_ref ...  
```

## Description

The ABAP SQL statement is executed on the specified [database connection](../../abap-glossary/abendatabase_connection_glosry.md).

The database connection is specified using an [ABAP SQL connection object](../../abap-glossary/abenabap_sql_conn_obj_glosry.md). The operand `con_ref` must be a reference variable of the [static type](../../abap-glossary/abenstatic_type_glosry.md) [`IF_ABAP_SQL_CONNECTION`](abenif_abap_sql_connection.md) or a class or interface that implements that interface. The reference variable must point to a valid ABAP SQL connection object that represents an open database connection, otherwise the uncatchable exception `DBSQL_INVALID_CONNECTION_OBJ` occurs.

## Hints

- The character `@` in front of `con_ref` demands that a [reference variable](../../abap-glossary/abenreference_variable_glosry.md) `con_ref` that can be cast to `IF_ABAP_SQL_CONNECTION` is available.

- ABAP SQL connection objects that represent valid database connections can only be created with APIs released by SAP, such as `CL_ABAP_SQL_CONNECTION_BUILDER`.

- Detailed information about database connections can be found under [Database Connections](abendb_connections.md).

- Any ABAP SQL statement that uses the standard connection accesses the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) only.

- The addition `CONNECTION` should always be specified behind the addition `OPTIONS`.

## Executable Example

See [ABAP SQL - Connection Objects](abenif_abap_sql_connection_abexa.md)
