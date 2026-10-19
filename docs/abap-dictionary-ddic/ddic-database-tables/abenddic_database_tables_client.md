---
title: "DDIC - Client Dependency of Database Tables"
source_file: abenddic_database_tables_client.html
section: "ABAP Dictionary (DDIC) > DDIC - Database Tables > DDIC - Semantic Properties of Database Tables > DDIC - Table-Specific Semantic Properties of Database Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# DDIC - Client Dependency of Database Tables

If the first column of a DDIC database table is a key field with the [built-in type](../ddic-built-in-data-types/abenddic_builtin_types.md) `CLNT`, the table is client-dependent. In this case, the column contains the [client ID](../../abap-glossary/abenclient_identifier_glosry.md) evaluated in [client copies](https://help.sap.com/docs/ABAP_PLATFORM_NEW/4a368c163b08418890a406d413933ba7/4d8062ec095114afe10000000a42189c) and in [implicit client handling](../../abap-programming-language/abap-database-access/abenabap_sql_client_handling.md) in [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md).

## Hints

- Generally, tables in the [delivery class](abenddic_database_tables_delivery.md) *A* are client-dependent, whereas system tables in the delivery classes *E*, *S*, and *W* are client-independent.
