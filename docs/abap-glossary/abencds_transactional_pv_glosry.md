---
title: "CDS transactional query"
source_file: abencds_transactional_pv_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS transactional query

[CDS](../abap-core-data-services-abap-cds/abencds_glossary.md)

## Definition

A [CDS projection view](abencds_projection_view_glosry.md) that is intended for modeling transactional queries. A transactional query is typically used in the context of the [ABAP RESTful Application Programming Model](abenarap_glosry.md) to adapt a CDS data model for service-specific use cases. A transactional query is defined using the [CDS DDL](abencds_ddl_glosry.md) statement [`DEFINE VIEW ENTITY AS PROJECTION ON`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_view_as_projection.md) and it must have the [provider contract](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_pv_provider_contract.md) set to `TRANSACTIONAL_QUERY`. A CDS transactional query is a [CDS persistent entity](abencds_sql_entity_glosry.md).

[***-\>* More about**](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_pv_transactional_query.md)
