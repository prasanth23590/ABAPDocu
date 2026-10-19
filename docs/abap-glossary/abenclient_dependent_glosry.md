---
title: "client-dependent"
source_file: abenclient_dependent_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# client-dependent

[ABAP SQL](../abap-programming-language/abap-database-access/abensql_glossary.md) [CDS](../abap-core-data-services-abap-cds/abencds_glossary.md) [DDIC](../abap-dictionary-ddic/abenddic_glossary.md)

## Definition

A [SQL data source](abensql_data_source_glosry.md) for which an implicit [client handling](abenclient_handling_glosry.md) takes place when accessed with [ABAP SQL](abenabap_sql_glosry.md).

- A [DDIC database table](abenddic_db_table_glosry.md) [ABAP Dictionary](abenabap_dictionary_glosry.md) is client-dependent if the first column is a [client column](abenclient_column_glosry.md). The system table `T000`, which contains the [AS ABAP](abenas_abap_glosry.md) [client IDs](abenclient_identifier_glosry.md), is an exception to this rule.

- The client dependency of a [CDS entity](abencds_entity_glosry.md) is determined by its data sources. Client handling is by done implicitly by filtering the [session variable](abensession_variable_glosry.md) `$session.client`.

- The client dependency of [CDS DDIC-based views (obsolete)](abencds_v1_view_glosry.md) is declared in the [CDS source code](abencds_source_code_glosry.md) by the [ABAP annotation](abenabap_annotation_glosry.md) `@CLientHandling.type`.

See also: [client-independent](abenclient_independent_glosry.md).
