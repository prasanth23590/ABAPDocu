---
title: "Database Connections and Transactions"
source_file: abendb_connections_trans.html
section: "ABAP Programming Language > ABAP - Database Access > Database Connections"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Database Connections and Transactions

Every active database connection creates a separate transaction context or is linked with its own [database LUW](../../abap-glossary/abendatabase_luw_glosry.md). This means that database changes on one connection can be committed or rolled back independently of changes on other database connections. In this way, for example, log data can be stored in and committed on a service connection without modifying the database LUW of the standard connection.

Database changes can be committed or rolled back as follows specifically for database connections:

- The statements [`COMMIT CONNECTION`](abapcommit_rollback_connection.md) and [`ROLLBACK CONNECTION`](abapcommit_rollback_connection.md) trigger targeted [database commits](../../abap-glossary/abendatabase_commit_glosry.md) or [database rollbacks](../../abap-glossary/abendatabase_rollback_glosry.md) on specific connections.

- When a database connection is made inactive implicitly at the end of an internal session, a [database commit](../../abap-glossary/abendatabase_commit_glosry.md) is triggered.

- When a database connection is closed explicitly, a [database rollback](../../abap-glossary/abendatabase_rollback_glosry.md) is triggered.

In addition, there are the statements [`COMMIT WORK`](abapcommit.md) and [`ROLLBACK WORK`](abaprollback.md), as well as the implicit [database commits](abendb_commit.md) and [database rollbacks](abendb_rollback.md), that act on all active connections.

A service connection is always set to inactive when its database changes are committed or rolled back. A connection deactivated in this way can, however, still be used in the same internal session without being opened explicitly. The first time an inactive service connection previously active in the current internal session is reused, it is made active again and a new database LUW is opened.

## Hints

- Service connections can be used to implement independent database LUWs on the standard database. Care must be taken to avoid lock situations here.

- Working with multiple database connections, namely independent database LUWs, can produce lock situations where only one work process is involved: a program changes a database row on the first connection and tries to change the same row on a second connection. This results in the program waiting for the lock of the first database LUW, without this first LUW ever being able to continue. This situation can only be resolved by ending the work process. This is done automatically for dialog processes, but it must be done manually for background jobs. It is therefore not advisable to change the same table within the a single program using multiple database connections.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

If the statement `COMMIT CONNECTION` were not used for the standard connection represented by a connection object referred by the reference variable `conn_default`, the following program section would produce a lock situation because the standard connection and a service connection represented by a connection object referred by the reference variable `conn_service` would be used in independent database LUWs to access the same row of a database table.

``` abap
FINAL(conn_default) = 
  cl_abap_sql_connection_builder=>default( )->create( ). 
 
FINAL(conn_service) = 
  cl_abap_sql_connection_builder=>service( 
    `R/3*DEMO` )->create( ). 
 
INSERT demo_update FROM @( VALUE #( id = 'X' ) ). 
DELETE FROM demo_update. 
COMMIT CONNECTION @conn_default. 
 
INSERT demo_update 
       FROM @( VALUE #( id =  'X' 
                        col1 = 1 
                        col2 = 2 
                        col3 = 3 
                        col4 = 4 ) ) 
       OPTIONS 
         CONNECTION @conn_service.
```
