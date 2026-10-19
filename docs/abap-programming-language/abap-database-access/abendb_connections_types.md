---
title: "Possible Database Connections"
source_file: abendb_connections_types.html
section: "ABAP Programming Language > ABAP - Database Access > Database Connections"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Possible Database Connections

When ABAP SQL is used in an ABAP program, the [database interface](../../abap-glossary/abendatabase_interface_glosry.md) uses a [database connection](../../abap-glossary/abendatabase_connection_glosry.md) of the current [work process](../../abap-glossary/abenwork_process_glosry.md) to access a database. Every work process always has a standard connection to the standard database. In addition, service connections to the standard database can be used.

- [Standard Connection](abendb_connections_types.md#standard-connection)

- [Service Connections to the Standard Database](abendb_connections_types.md#service-connections-to-the-standard-database)

## Hint

In order to access other database systems than the standard database, [CDS external entities](../../abap-glossary/abencds_external_entity_glosry.md) can be used.

## Standard Connection

Each AS ABAP work process always has a standard connection to the [standard database](../../abap-glossary/abenstandard_db_glosry.md) and this connection cannot be closed. It is shared by all [internal sessions](../../abap-glossary/abeninternal_session_glosry.md). If the standard connection is used, the work process acts as a [database user](../../abap-glossary/abendatabase_user_glosry.md) to which the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) is assigned.

- By default, [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statements use the standard connection to access the ABAP database schema of the standard AS ABAP database.

- In all places where a database connection can be specified explicitly in ABAP, the standard connection can also be specified as follows:

  - Using an [ABAP SQL connection object](../../abap-glossary/abenabap_sql_conn_obj_glosry.md) created with the method `DEFAULT` of class `CL_ABAP_SQL_CONNECTION_BUILDER`.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Specifies the standard connection using an [ABAP SQL connection object](../../abap-glossary/abenabap_sql_conn_obj_glosry.md) created with the method `DEFAULT` of class `CL_ABAP_SQL_CONNECTION_BUILDER`. It would not be necessary to specify the connection in the statements `DELETE` and `INSERT`. The statement [`COMMIT CONNECTION`](abapcommit_rollback_connection.md), however, makes an explicit [database commit](../../abap-glossary/abendatabase_commit_glosry.md) possible on the standard connection.

``` abap
FINAL(conn) = cl_abap_sql_connection_builder=>default( )->create( ). 
 
DELETE FROM demo_update OPTIONS CONNECTION @conn. 
INSERT demo_update 
  FROM @( VALUE #( id = 'X'  col1 = 1 col2 = 2 col3 = 3 col4 = 4 ) ) 
  OPTIONS CONNECTION @conn. 
COMMIT CONNECTION @conn.
```

## Service Connections to the Standard Database

A service connection is a database connection defined as follows:

- Using an [ABAP SQL connection object](../../abap-glossary/abenabap_sql_conn_obj_glosry.md) created with the method `SERVICE` of class `CL_ABAP_SQL_CONNECTION_BUILDER`. The name of the service connection must be passed to the method.

The name of a service connection is `R/3*name` and consists of the prefix `R/3*` in uppercase letters and a definable case-sensitive `name` that can have between 1 and 26 alphanumeric characters.

A service connection is always a database connection to the standard database and inherits all settings from the standard connection automatically.

When a service connection is requested in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md), it is opened for the current work process if possible or an existing inactive service connection with the same name is reused.

### Hints

- Service connections to the standard SAP database are useful for performing operations in a [database LUW](abendb_transaction.md) that are independent of the LUW of the standard connection. It should be noted that the current [isolation level](abendb_isolation.md) is responsible for determining whether a read from a database LUW can access data modified in a different database LUW, before this data is committed using a database commit.

- Service connections add to the number of open connections of the current work process. There can be a maximum of 16 open connections, including the standard connection itself.

- Service connections can be used for modifying data on external database systems using [writable CDS external entities](../../abap-glossary/abenwritable_ee_glosry.md). For details, see the topic [CDS DDL - `DEFINE EXTERNAL ENTITY`, `WRITABLE`](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_writable_ee.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Use of a service connection called `R/3*service_conn` represented by an [ABAP SQL connection object](../../abap-glossary/abenabap_sql_conn_obj_glosry.md) in ABAP SQL.

``` abap
FINAL(conn) = 
       cl_abap_sql_connection_builder=>service( 
         `R/3*service_conn` )->create( ). 
 
DELETE FROM demo_update OPTIONS CONNECTION @conn. 
INSERT demo_update 
  FROM @( VALUE #( id = 'X'  col1 = 1 col2 = 2 col3 = 3 col4 = 4 ) ) 
  OPTIONS CONNECTION @conn. 
COMMIT CONNECTION @conn.
```
