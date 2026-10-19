---
title: "Management of Database Connections"
source_file: abendb_connections_mngmnt.html
section: "ABAP Programming Language > ABAP - Database Access > Database Connections"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Management of Database Connections

Database connections are managed by the ABAP runtime framework. This is done at the [work process](../../abap-glossary/abenwork_process_glosry.md) level and the [internal session](../../abap-glossary/abeninternal_session_glosry.md) level. Each time an AS ABAP is started, a [standard connection](../../abap-glossary/abenstandard_db_connection_glosry.md) is opened for every [work process](../../abap-glossary/abenwork_process_glosry.md) and this connection cannot be closed. In addition to the standard connection, 15 further [service connections](../../abap-glossary/abenservice_connection_glosry.md) can be opened for each work process. A maximum of 16 database connections can be open for each work process. On certain databases, it may not be possible to reach this number. If more than 16 database connections are opened, the runtime error `DBSQL_NO_MORE_CONNECTION` occurs.

- [Opening and Closing Database Connections](abendb_connections_mngmnt.md#opening-and-closing-database-connections)

- [Active and Inactive Database Connections](abendb_connections_mngmnt.md#active-and-inactive-database-connections)

- [Database Connections in the Internal Session](abendb_connections_mngmnt.md#database-connections-in-the-internal-session)

## Opening and Closing Database Connections

ABAP SQL can request service connections. A service connection is requested as follows:

- In ABAP SQL:

  - By creating an [ABAP SQL connection object](../../abap-glossary/abenabap_sql_conn_obj_glosry.md) by using the method `SERVICE` of class `CL_ABAP_SQL_CONNECTION_BUILDER`.

If no inactive database connection can be activated for the specified name, it is opened for the current work process and activated for the current internal session.

A service connection can be closed explicitly as follows:

- In ABAP SQL:

  - Using the method `CLOSE` of the interface `IF_ABAP_SQL_CONNECTION` of the [ABAP SQL connection object](../../abap-glossary/abenabap_sql_conn_obj_glosry.md) that represents the connection.

If closed explicitly in ABAP SQL all database changes in the current database LUW of the connection that were not yet [committed on the database](abendb_commit.md) are discarded.

Any service connection that is inactive for a specific period of time (approximately 15 minutes by default) is closed by the ABAP runtime framework implicitly.

### Hints

- Generally speaking, database connections should only be closed implicitly by the ABAP runtime framework. Since it takes a significant amount of resources to restore a connection, database connections should only be closed explicitly in the following cases:

  - A database connection was used in such a way that unwanted side effects occur when reusing it.

  - The connections are not required for some time in the current process.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Opening and closing a service connection using an [ABAP SQL connection object](../../abap-glossary/abenabap_sql_conn_obj_glosry.md).

``` abap
    FINAL(conn) = 
           cl_abap_sql_connection_builder=>service( 
             `R/3*service_conn` )->create( ). 
 
    ... 
 
    conn->close( ).
```

## Active and Inactive Database Connections

An open service connection can be active or inactive. Once opened in ABAP SQL, a database connection is active and can be used by ABAP SQL. The service connection becomes inactive as soon as the current database LUW of this connection is ended. This can occur as follows:

- Using the statements [`COMMIT CONNECTION`](abapcommit_rollback_connection.md) or [`ROLLBACK CONNECTION`](abapcommit_rollback_connection.md) for this connection.

- Using the statements [`COMMIT WORK`](abapcommit.md) and [`ROLLBACK WORK`](abaprollback.md) for all connections

- In an implicit [database commit](abendb_commit.md) or [database rollback](abendb_rollback.md) for all connections

- When closing the internal session in which the connection was opened, where a `COMMIT CONNECTION` is executed for the connection implicitly.

An inactive open service connection is reused by the ABAP runtime framework if it is to be reopened for its work process. Once activated in an internal session, a service connection can be reused here regardless of whether it is active or inactive. It is not necessary to open it again explicitly. When an inactive connection is reused, it is activated implicitly and a new database LUW is opened.

### Hints

- When a database connection is closed explicitly it is actually closed and not just set to inactive. The next request must then reopen the connection for the current work process.

## Database Connections in the Internal Session

Active open service connections can only be used within the [internal session](../../abap-glossary/abeninternal_session_glosry.md) in which they are opened.

When the internal session is closed, any changes made using the connections are committed and the connections are set to inactive.
