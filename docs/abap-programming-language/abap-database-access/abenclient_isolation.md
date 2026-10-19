---
title: "Client Isolation"
source_file: abenclient_isolation.html
section: "ABAP Programming Language > ABAP - Database Access > Data Consistency"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Client Isolation

A [client](../../abap-glossary/abenclient_glosry.md) is an organizational unit of an [AS ABAP](../../abap-glossary/abenas_abap_glosry.md). Each [user session](../../abap-glossary/abenuser_session_glosry.md) is governed by its [current client](../../abap-glossary/abencurrent_client_glosry.md) whose [client ID](../../abap-glossary/abenclient_identifier_glosry.md) is set during [logon](../../abap-glossary/abenlogon_glosry.md).

Application data are stored in [application tables](../../abap-glossary/abenapplication_table_glosry.md) with a [client column](../../abap-glossary/abenclient_column_glosry.md). The client column contains client IDs. Each client ID uniquely assigns the data in the other columns to a client. [SQL data sources](../../abap-glossary/abensql_data_source_glosry.md) that are based on tables with a client column are [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md). [System tables](../../abap-glossary/abensystem_table_glosry.md), on the other hand, do not have a client column and thus are [client-independent](../../abap-glossary/abenclient_independent_glosry.md).

As a rule, ABAP application programs executed in a user session should access only data of the current client and no data of other clients. This so-called [client isolation](../../abap-glossary/abenclient_isolation_glosry.md) is enforced in ABAP Cloud as follows.

There are two ways how ABAP classes with ABAP language version [ABAP for Cloud Development](../../abap-glossary/abenabap_for_cloud_dev_glosry.md) can access [client-dependent](../../abap-glossary/abenclient_dependent_glosry.md) data sources:

- Directly with [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md).

  In ABAP SQL, implicit [client handling](../../abap-glossary/abenclient_handling_glosry.md) takes place that accesses data of the current client only. In ABAP for Cloud Development, it is not possible to change that behavior as it can be done in Standard ABAP.

- Indirectly by calling [AMDP methods](../../abap-glossary/abenamdp_method_glosry.md)

  AMDP methods that have ABAP language version ABAP for Cloud Development and/or are released as APIs with a [C1 contract](../../abap-glossary/abenc1_contract_glosry.md) or a [C4 contract](../../abap-glossary/abenc1_contract_glosry.md) must be [client-safe](../../abap-glossary/abenclient_safe_glosry.md). Client-dependent AMDP methods that are client-safe set the HANA session variable `CDS_CLIENT` when called and can access only client-safe objects where the result is filtered by that session variable. In order to support that, [CDS entities](../../abap-glossary/abencds_entity_glosry.md) that are [released APIs](../../abap-glossary/abenreleased_api_glosry.md) must also be [client-safe](../../abap-glossary/abenclient_safe_glosry.md).

Other ways for accessing client-dependent data are not supported in ABAP for Cloud Development.
