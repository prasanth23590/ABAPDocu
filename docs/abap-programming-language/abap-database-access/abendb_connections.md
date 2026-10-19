---
title: "Database Connections"
source_file: abendb_connections.html
section: "ABAP Programming Language > ABAP - Database Access"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Database Connections

An [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) uses database connections to access databases. A database connection defines the address of the database system (database host), the [database user](../../abap-glossary/abendatabase_user_glosry.md), and hence the assigned [database schema](../../abap-glossary/abendatabase_schema_glosry.md) that is accessed. The [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) use a database connection of the current [work process](../../abap-glossary/abenwork_process_glosry.md) to access a database. By default, the [standard connection](../../abap-glossary/abenstandard_db_connection_glosry.md) is used to access the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) of the [standard AS ABAP database](../../abap-glossary/abenstandard_db_glosry.md). Connections called [service connections](../../abap-glossary/abenservice_connection_glosry.md) can also be used to access the standard database.

- [Possible Database Connections](abendb_connections_types.md)

- [Management of Database Connections](abendb_connections_mngmnt.md)

- [Database Access Using Secondary Connections](abendb_connections_using.md)

- [Database Connections and Transactions](abendb_connections_trans.md)
