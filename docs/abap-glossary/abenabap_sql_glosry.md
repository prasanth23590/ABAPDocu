---
title: "ABAP SQL"
source_file: abenabap_sql_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL

[ABAP SQL](../abap-programming-language/abap-database-access/abensql_glossary.md)

## Definition

ABAP SQL is a subset of [SQL](abensql_glosry.md) implemented by [ABAP statements](abenabap_statement_glosry.md), which includes the [DQL](abendql_glosry.md) and [DML](abendml_glosry.md) parts for [CRUD](abencrud_glosry.md) operations. ABAP SQL statements are processed by the [ABAP SQL engine](abenabap_sql_engine_glosry.md) that either uses

- the [ABAP SQL interface](abenabap_sql_interface_glosry.md) of the [database interface](abendatabase_interface_glosry.md) to access the [standard database](abenstandard_db_glosry.md) of an [AS ABAP](abenas_abap_glosry.md) or a secondary database.

- or the [ABAP SQL in-memory engine](abenabap_sql_inmemeng_glosry.md) to access the [table buffer](abentable_buffer_glosry.md) or [internal tables](abeninternal_table_glosry.md)

ABAP SQL can be used to read ([`SELECT`](../abap-programming-language/abap-database-access/abapselect.md), [`WITH`](../abap-programming-language/abap-database-access/abapwith.md). `FETCH`) and modify ([`INSERT`](../abap-programming-language/abap-database-access/abapinsert_dbtab.md), [`UPDATE`](../abap-programming-language/abap-database-access/abapupdate.md), [`MODIFY`](../abap-programming-language/abap-database-access/abapmodify_dbtab.md), or [`DELETE`](../abap-programming-language/abap-database-access/abapdelete_dbtab.md)) data in [DDIC database tables](abenddic_db_table_glosry.md) defined in the [ABAP Dictionary](abenabap_dictionary_glosry.md). [DDIC database tables](abenddic_db_table_glosry.md) and all [CDS persistent entities](abencds_sql_entity_glosry.md) can be used directly as [data sources](abensql_data_source_glosry.md) in ABAP SQL.

[***-\>* More about**](../abap-programming-language/abap-database-access/abenabap_sql.md)
