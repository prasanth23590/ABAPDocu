---
title: "ABAP SQL - Overview"
source_file: abenabap_sql_oview.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Overview

ABAP SQL defines the subset of ABAP statements that enable direct access to data in the [standard database](../../abap-glossary/abenstandard_db_glosry.md) of the current [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). The ABAP SQL statements represent the [DQL](../../abap-glossary/abendql_glosry.md) and [DML](../../abap-glossary/abendml_glosry.md) parts of [SQL](../../abap-glossary/abensql_glosry.md) in ABAP, which is supported by all database systems. ABAP SQL statements are processed by the [ABAP SQL engine](../../abap-glossary/abenabap_sql_engine_glosry.md). There are two possibilities:

- The statements are passed to the [ABAP SQL interface](../../abap-glossary/abenabap_sql_interface_glosry.md), where they are converted to database-specific SQL and then transferred to the database system and executed there.

- The statements are executed by the [ABAP SQL in-memory engine](../../abap-glossary/abenabap_sql_inmemeng_glosry.md) for tabular data in the [table buffer](../../abap-glossary/abentable_buffer_glosry.md) or in [internal tables](../../abap-glossary/abeninternal_table_glosry.md) specified in the [`FROM`](abapselect_itab.md) clause.

By default, ABAP SQL statements use [implicit client handling](abenabap_sql_client_handling.md) to access only the data of the [current client](../../abap-glossary/abencurrent_client_glosry.md). To improve performance when accessing the database, [table buffering](abensap_puffering.md) can be activated for individual DDIC database tables, or CDS views to avoid accessing the database directly each time.

ABAP SQL is closely linked with the [ABAP Dictionary](../../abap-glossary/abenabap_dictionary_glosry.md) and [ABAP CDS](../../abap-glossary/abenabap_cds_glosry.md). ABAP SQL statements can be used only to access [DDIC database tables](../../abap-dictionary-ddic/ddic-database-tables/abenddic_database_tables.md) of the ABAP Dictionary, and [CDS persistent entities](../../abap-glossary/abencds_sql_entity_glosry.md). These are specified directly in ABAP SQL statements without specifying a [database schema](../../abap-glossary/abendatabase_schema_glosry.md). By default, the ABAP SQL interface of the database interface accesses the associated database objects in the [ABAP database schema](../../abap-glossary/abenabap_db_schema_glosry.md) of the [standard database](../../abap-glossary/abenstandard_db_glosry.md).

The ABAP SQL interface of the database interface respects the fact that the order of the columns of a data source in the database system can differ from the order in the definition of the data source in the ABAP Dictionary. If ABAP SQL is used, the order in the ABAP Dictionary applies and the database interface performs a transformation if necessary.

Each non-buffered ABAP SQL statement is equivalent to one access to the database. This applies in particular to [`SELECT`](abapselect.md) statements that end with [`ENDSELECT`](abapendselect.md). Data to be read and to be modified is transported in packages between the database server and the current AS instance.

- [ABAP SQL - Client Handling](abenabap_sql_client_handling.md)

- [ABAP SQL - Null Values](abenabap_sql_null_values.md)

- [ABAP SQL - Table Buffering](abensap_puffering.md)

In [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md), ABAP SQL statements are checked in the strictest syntax check mode that is currently available. This is different to [Standard ABAP](../../abap-glossary/abenstandard_abap_glosry.md), where the strict modes of the syntax check are coupled to the usage of features introduced in different releases.

## Hint

If more than approximately 2^32 entries are addressed in a single database access, the behavior of the database is undefined.
