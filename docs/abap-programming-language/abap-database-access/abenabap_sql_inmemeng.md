---
title: "ABAP SQL - ABAP SQL In-Memory Engine"
source_file: abenabap_sql_inmemeng.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - ABAP SQL In-Memory Engine

The [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) is a part of the [ABAP SQL engine](../../abap-glossary/abenabap_sql_engine_glosry.md) for processing [read accesses](abenabap_sql_reading.md) to tabular data in the memory of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) with [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) statements. The following tabular data can be accessed:

- Data from [database tables](../../abap-glossary/abendatabase_table_glosry.md) buffered in the [table buffer](../../abap-glossary/abentable_buffer_glosry.md).

- [Internal tables](../../abap-glossary/abeninternal_table_glosry.md) of [internal sessions](../../abap-glossary/abeninternal_session_glosry.md) accessed with [`SELECT ... FROM @itab`](abapselect_itab.md).

The ABAP SQL in-memory engine produces the same results as if the ABAP SQL statements were processed on the database, for example:

- [Null values](../../abap-glossary/abennull_value_glosry.md) of database tables stored in able buffer are handled as null values. They are not transformed to type-dependent initial values.

- [Supported SQL expressions](abensql_engine_expr.md) produce the same results as on the database, even for internal tables accessed with [`SELECT ... FROM @itab`](abapselect_itab.md).

The ABAP SQL in-memory engine supports a large subset of [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) but there are some [restrictions](abensql_engine_restr.md). If an ABAP SQL statement cannot be processed by the ABAP SQL in-memory engine, the following situations can occur:

- When accessing buffered database tables in the table buffer, the buffer is bypassed and the ABAP SQL statement is converted to database-specific SQL, passed to the database and used for the actual database tables.

- When accessing internal tables with [`SELECT ... FROM @itab`](abapselect_itab.md):

  - If only one internal table is accessed in the ABAP SQL statement, the data of the table can be passed to a temporary table in the database before the query is actually executed. Only the columns that are to be accessed are transported. Then the SQL statement is passed to the database and processed there. This option is not supported by all databases. If it is known statically that data is required on the database, a syntax check warning occurs that can be hidden by the pragma `##itab_db_select`.

  - If more than one internal table is accessed in the ABAP SQL statement, their content cannot be passed to the database. The statement cannot be executed and a syntax error or a catchable exception occurs.

If an ABAP SQL statement can be processed by the ABAP SQL in-memory engine, there are no further restrictions for internal tables accessed with [`SELECT ... FROM @itab`](abapselect_itab.md) and database tables with the buffering type [full buffering](abenbuffer_complete_buffering.md). They can be processed on the AS ABAP. For database tables with other [buffering types](abenbuffer_type.md), there are further [restrictions](abenbuffer_restrictions.md) that can cause the buffer to be bypassed and the statement to be processed on the database. In this case, only one internal table can be accessed within the SQL statement.

## Hints

- The above rule about accessing only one internal table in an ABAP SQL statement that is processed on the database currently means that even the same internal table cannot be accessed more than once within one statement. As a workaround, the access to an internal table can be placed in a [common table expression](../../abap-glossary/abencommon_table_expression_glosry.md) that then can be accessed multiple times in following subqueries.

- Generally, only one internal table can be accessed together with database tables within one ABAP SQL statement. All multiple accesses are obtained using joins or subqueries which are currently not supported by the ABAP SQL in-memory engine.

## Executable Examples

- [ABAP SQL In-Memory Engine, Multiple Internal Tables](abenabap_sql_engine_abexa.md)

- [ABAP SQL In-Memory Engine, Restrictions](abenabap_sql_engine_restr_abexa.md)

- [ABAP SQL In-Memory Engine, Restriction to One Internal Table](abenabap_sql_engine_itab_abexa.md)
