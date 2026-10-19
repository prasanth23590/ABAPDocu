---
title: "client-safe"
source_file: abenclient_safe_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# client-safe

[ABAP Language](../abap-programming-language/abenabala_glossary.md) [CDS](../abap-core-data-services-abap-cds/abencds_glossary.md)

## Definition

A [repository object](abenrepository_object_glosry.md) that accesses [client-dependent](abenclient_dependent_glosry.md) [SQL data sources](abensql_data_source_glosry.md) is client-safe, if it can access data of one [client](abenclient_glosry.md) only. Such repository objects support the concept of [client isolation](abenclient_isolation_glosry.md) for [AMDP methods](abenamdp_method_glosry.md):

- AMDP methods that have the [ABAP language version](abenabap_version_glosry.md) [ABAP for Cloud Development](abenabap_for_cloud_dev_glosry.md) or are a [released API](abenreleased_api_glosry.md) with a [C1 contract](abenc1_contract_glosry.md) or a [C4 contract](abenc4_contract_glosry.md) must be [client-safe](../abap-programming-language/abap-database-access/abenamdp_client_safety.md) and must access client-safe objects only.

- For a [CDS entity](abencds_entity_glosry.md), an [annotation](abencds_annotation_glosry.md) [`ClientHandling.clientSafe`](../abap-core-data-services-abap-cds/abap-cds-annotations/abencds_1549616294_anno.md) can be specified that enforces checks that guarantee its client safety. For CDS entities that do not have this annotations but are [released APIs](abenreleased_api_glosry.md), the checks are done implicitly.

A repository object that accesses only [client-independent](abenclient_independent_glosry.md) SQL data sources is implicitly client-safe.
