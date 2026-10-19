---
title: "IF_ABAP_SQL_CONNECTION, ABAP SQL Connection Object"
source_file: abenif_abap_sql_connection.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - System Interfaces and Classes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# IF_ABAP_SQL_CONNECTION, ABAP SQL Connection Object

The system interface `IF_ABAP_SQL_CONNECTION` is used for accessing [ABAP SQL connection objects](../../abap-glossary/abenabap_sql_conn_obj_glosry.md) that represent [database connections](../../abap-glossary/abendatabase_connection_glosry.md). [Interface reference variables](../../abap-glossary/abeninterface_ref_variable_glosry.md) pointing to valid connection objects can be used in the following statements:

- `SELECT`, `WITH` `...` [`CONNECTION`](abapselect_connection.md)

- `INSERT`, `UPDATE`, `MODIFY`, `DELETE` `...` [`CONNECTION`](abapiumd_conn.md)

- `COMMIT`, `ROLLBACK` [`CONNECTION`](abapcommit_rollback_connection.md)

The interface methods allow handling the database connection:

- `DESCRIBE` returns an internal table that contains a description of the database connection.

- `COMMIT` commits all previous write accesses using that connection.

- `ROLLBACK` rolls back all previous write accesses using that connection.

- `HAS_UNCOMMITED_CHANGES` returns an initial value if all previous write accesses using that connection are committed.

- `CLOSE` rolls back any uncommitted changes and closes the connection.

- `SET_BLOCK_COMMIT` prevents implicit and explicit commits.

Valid connection objects can only be created using system classes such as `CL_ABAP_SQL_CONNECTION_BUILDER`. Currently, this class offers the following methods to create connection objects:

- `DEFAULT` returns a connection object for the [standard connection](../../abap-glossary/abenstandard_db_connection_glosry.md).

- `SERVICE` creates a [service connection](../../abap-glossary/abenservice_connection_glosry.md) and returns a connection object for that connection. It must be passed a name of the service connection that must start with *R/3\**.

- `WRITE_ENABLED_4_LOGICAL_SCHEMA` creates a [service connection](../../abap-glossary/abenservice_connection_glosry.md) and returns a connection object for a [logical external schema](../../abap-glossary/abencds_logical_schema_glosry.md). This connection object enables write access on [dynamic external entities](../../abap-glossary/abencds_dynamic_ee_glosry.md). It must be passed a name for the service connection that must start with *R3\** and the name of the logical external schema that is to be write enabled. Note that a connection object can be write-enabled for exactly one logical external schema.

Different connection objects for service connections always represent different connections, even if they are created with the same name.

## Hint

The interface methods `COMMIT` and `ROLLBACK` are internally called when the statements [`COMMIT|ROLLBACK CONNECTION`](abapcommit_rollback_connection.md) are used with a connection object.

## Executable Example

See [ABAP SQL - Connection Objects](abenif_abap_sql_connection_abexa.md)
