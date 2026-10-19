---
title: "client isolation"
source_file: abenclient_isolation_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# client isolation

[ABAP SQL](../abap-programming-language/abap-database-access/abensql_glossary.md) [CDS](../abap-core-data-services-abap-cds/abencds_glossary.md)

## Definition

Client isolation on an [AS ABAP](abenas_abap_glosry.md) means that an [ABAP user](abenabap_user_glosry.md) has access to data of the [current client](abencurrent_client_glosry.md) only. In [ABAP Cloud](abenabap_cloud_glosry.md), client isolation is enforced as follows:

- Implicit [client handling](abenclient_handling_glosry.md) in [ABAP SQL](abenabap_sql_glosry.md).

- [AMDP methods](abenamdp_method_glosry.md) can access [client-safe](abenclient_safe_glosry.md) [repository objects](abenrepository_object_glosry.md) only.

- [CDS entities](abencds_entity_glosry.md) that are [released APIs](abenreleased_api_glosry.md) must be [client-safe](abenclient_safe_glosry.md).

[***-\>* More about**](../abap-programming-language/abap-database-access/abenclient_isolation.md)
