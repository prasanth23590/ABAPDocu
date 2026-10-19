---
title: "CDS DDL - CDS Projection View, Analytical Queries"
source_file: abencds_analytical_query_apv.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Projection View, Analytical Queries

[CDS analytical projection views](../../abap-glossary/abencds_analytical_pv_glosry.md) are intended for modeling analytical queries within a CDS data model. The [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) must be an [analytical cube view](../../abap-glossary/abencds_analytical_cube_glosry.md) or an [analytical dimension view](../../abap-glossary/abencds_anal_dim_view_glosry.md). The feature set is restricted to the capabilities of the runtime of the analytical engine. The runtime for analytical queries are analytical engines, such as [ABAP Analytical Engine](../../abap-glossary/abenabap_ae_glosry.md). The protocol for CDS analytical queries is the [Information Access protocol](../../abap-glossary/abenina_protocol_glosry.md) (InA). InA is available as [service binding](../abap-cds-service-definitions/abencds_service_bindings.md) type.

Analytical projection views are [CDS transient entities](../../abap-glossary/abencds_non_sql_entity_glosry.md) defined with the keyword [`DEFINE TRANSIENT VIEW ENTITY AS PROJECTION ON`](abencds_define_view_as_analytical.md). That means that only a runtime object on the ABAP server is generated. No [SQL view](../../abap-glossary/abensql_view_glosry.md) is created on the database. Therefore, an analytical query can be used only by the analytical runtime. An analytical query cannot be used as data source of other CDS entities. Access with [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md) is not possible.

## Hint

CDS analytical projection views improve on the previous version of CDS Analytical Queries. They offer advantages such as avoiding the generation of an SQL artefact, reducing the need for annotations, and an improved syntax check. Moreover, they use the new features of CDS view entities, such as [typed literals](abencds_typed_literal_v2.md) and [improved amount and quantity handling](../abap-cds-data-types/abencds_calc_quan.md).

## More Information

- Development guide for [ABAP Analytics](https://help.sap.com/docs/ABAP_Cloud/67127c83ae1a4917b6b65ec222416894/4ae5db4d9bfd472ba70613b358dbb16b?version=sap_cross_product_abap).

- ABAP Data Models guide, section about [CDS analytical queries](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/f7d36ce7db234c69934d40afa3e5b32c?version=sap_cross_product_abap).
