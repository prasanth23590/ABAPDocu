---
title: "CDS analytical projection view"
source_file: abencds_analytical_pv_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS analytical projection view

[CDS](../abap-core-data-services-abap-cds/abencds_glossary.md)

## Definition

Synonym for [CDS analytical query](abencds_analytic_query_glosry.md). [CDS projection view](abencds_projection_view_glosry.md) that is intended for modeling analytical queries within a CDS data model. It is processed by the [ABAP Analytical Engine](abenabap_ae_glosry.md) and has to be exposed as an [InA](abenina_protocol_glosry.md) service. A CDS analytical projection view is defined using the [CDS DDL](abencds_ddl_glosry.md) statement [`DEFINE TRANSIENT VIEW ENTITY AS PROJECTION ON`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_view_as_analytical.md) and it must have the [provider contract](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_pv_provider_contract.md) set to `ANALYTICAL_QUERY`. A CDS analytical projection view is a [CDS transient entity](abencds_non_sql_entity_glosry.md).

[***-\>* More about**](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_analytical_query_apv.md)
