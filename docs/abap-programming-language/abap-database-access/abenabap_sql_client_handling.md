---
title: "ABAP SQL - Client Handling"
source_file: abenabap_sql_client_handling.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP SQL > ABAP SQL - Overview"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP SQL - Client Handling

The term [client handling](../../abap-glossary/abenclient_handling_glosry.md) means the handling of the application data of a [client](../../abap-glossary/abenclient_glosry.md). The aim of client handling is generally that an [ABAP user](../../abap-glossary/abenabap_user_glosry.md) can only have access to the application data of the [current client](../../abap-glossary/abencurrent_client_glosry.md) whose [client ID](../../abap-glossary/abenclient_identifier_glosry.md) was specified in the logon. ABAP SQL uses implicit client handling. This method of client handling has the effect that ABAP SQL statements handle the [client column](../../abap-glossary/abenclient_column_glosry.md) in a special way when [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md) data sources are accessed:

- The client column cannot be evaluated in the [SQL conditions](../../abap-glossary/abensql_cond_glosry.md) of the [`SELECT`](abapselect.md) statements of [queries](../../abap-glossary/abenasql_query_glosry.md) and of the write statements [`UPDATE SET`](abapupdate.md) and [`DELETE FROM`](abapdelete_dbtab.md).

  - Instead, the SQL statements passed to the database by the [ABAP SQL interface](../../abap-glossary/abenabap_sql_interface_glosry.md) contain an additional condition for the client column.

  - Furthermore, joins between client-dependent data sources insert an `ON` condition that checks the client columns for equality.

- The variants of the write statements [`INSERT`](abapinsert_dbtab.md), [`UPDATE`](abapupdate.md), [`MODIFY`](abapmodify_dbtab.md), and [`DELETE`](abapdelete_dbtab.md), which use data from work areas, internal tables, or subqueries specified after `FROM`, ignore their client columns and the value is set by ABAP SQL instead.

Implicit client handling uses the [client ID](../../abap-glossary/abenclient_identifier_glosry.md) of the [current client](../../abap-glossary/abencurrent_client_glosry.md) by default. This ID is also contained in the [system field](../../abap-glossary/abensystem_field_glosry.md) `sy-mandt`.

- The condition passed implicitly in selections checks the content of the client column for equality with the client ID of the current client.

- In write statements, ABAP SQL uses the client ID of the current client for the client column of the target instead of the values of the client column of the work areas, internal tables, or subqueries specified after `FROM`.

This means that ABAP SQL uses only the data of the current data by default and this does not need to be specified explicitly by the developer.

## Hints

- The implicit client handling of ABAP SQL does not concern the [`INTO` clause](abapinto_clause.md) and the rules described there. In particular, the client column of a target structure can be filled with other values than the client ID, for example when assigning individually specified columns of a [select list](abapselect_list.md).

- For information about accessing client-dependent [CDS entities](../../abap-glossary/abencds_entity_glosry.md), see the following descriptions:

  - [ABAP CDS - Client Handling in CDS Table Entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_table_entity_client.md)

  - [Client Handling in CDS View Entities](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_v2_view_client_handling.md)

  - [Client Handling in CDS DDIC-Based Views](../../abap-core-data-services-abap-cds/abap-cds-obsolete-language-elements/abencds_view_client_handling_v1.md)

  - [Client Handling in CDS Table Functions](../../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_func_client_handling.md).

- The DDIC database table `T000` contains the potential [client IDs](../../abap-glossary/abenclient_identifier_glosry.md) in [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). Client columns of application tables should contain only those client IDs specified in `T000`. This is not, however, checked by ABAP SQL.

- The client data from an AS ABAP is represented in self-contained units. No client-independent access to databases should take place in application programs.

- For [client-independent](../../abap-glossary/abenclient_independent_glosry.md) data sources, any column of type `CHAR` with length 3 can be declared as a client column with the addition [`DECLARE CLIENT`](abapselect_declare_client.md) in ABAP SQL Queries. Then, the data source is handled as client-dependent and implicit client handling is applied.
