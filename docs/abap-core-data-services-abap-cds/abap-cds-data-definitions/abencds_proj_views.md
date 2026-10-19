---
title: "ABAP CDS - Projection Views"
source_file: abencds_proj_views.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Projection Views

A [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md) is defined in the [DDL source code](../../abap-glossary/abenddl_source_code_glosry.md) of a [CDS data definition](../../abap-glossary/abencds_data_definition_glosry.md) using the statement `DEFINE [TRANSIENT] VIEW ENTITY AS PROJECTION ON` in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) of the [ABAP Core Data Services (CDS)](../abencds.md).

A CDS projection view is based on another [CDS view entity](../../abap-glossary/abencds_v2_view_glosry.md) (called [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md)). CDS projection views adapt a CDS data model for service-specific use cases.

The name of a CDS projection view is in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP.

[Client handling](../../abap-glossary/abenclient_handling_glosry.md) is done implicitly and automatically for CDS projection views. The rules are the same as for CDS view entities, see section [ABAP CDS - Client Handling in CDS View Entities](abencds_v2_view_client_handling.md). A projection view is [client-safe](../../abap-glossary/abenclient_safe_glosry.md) when the underlying [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md) is client-safe and as long as no client-critical functions are used.

[Table buffering](../../abap-glossary/abentable_buffering_glosry.md) for CDS projection views works in the same way as for CDS view entities. Table buffering settings can be defined in a separate repository object called [CDS entity buffer](../../abap-glossary/abencds_entity_buffer_glosry.md). [CDS view entity buffers](../../abap-glossary/abencds_view_entity_b_glosry.md) and [CDS propagated buffers (obsolete)](../../abap-glossary/abencds_prop_buffer_glosry.md) can be defined for a CDS projection view. For details, see the following topics:

- [ABAP CDS - Table Buffering of CDS View Entities](abencds_v2_view_buffering.md)

- [CDS DDL - `DEFINE VIEW | TABLE ENTITY BUFFER`](../abap-cds-tuning-objects/abencds_define_view_entity_buffer.md)

- [CDS DDL - `PROPAGATE VIEW ENTITY BUFFER (Obsolete)`](../abap-cds-obsolete-language-elements/abencds_propagate_buffer.md)

There are different types of projection views available, depending on the purpose and use case of the projection view. The type of projection view is specified using the syntax addition [`PROVIDER CONTRACT`](abencds_pv_provider_contract.md). The following types of CDS projection views are available:

- [CDS transactional queries](../../abap-glossary/abencds_transactional_pv_glosry.md)

  Transactional queries define the projection layer of a RAP business object. They are [CDS SQL entities](../../abap-glossary/abencds_sql_entity_glosry.md). For details, see the section about [Transactional Queries](abencds_pv_transactional_query.md).

- [CDS transactional interfaces](../../abap-glossary/abencds_trans_interface_glosry.md)

  CDS transactional interfaces serve as stable public interface layer in a CDS data model. They are typically used in the context of the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md) to provide the basis for a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md). CDS transactional interfaces are [SQL entities](../../abap-glossary/abencds_sql_entity_glosry.md). For details, see the section about [CDS Transactional Interfaces](abencds_pv_transactional_interface.md).

- [CDS analytical queries](../../abap-glossary/abencds_analytical_pv_glosry.md)

  [CDS analytical queries](../../abap-glossary/abencds_analytical_pv_glosry.md) are intended for modelling analytical queries within the CDS data model. They are evaluated by an analytical engine. Analytical queries are [CDS transient entities](../../abap-glossary/abencds_non_sql_entity_glosry.md). For details, see the section about [Analytical Queries](abencds_analytical_query_apv.md).

- no provider contract specified

  Deprecated. It is strongly recommended that a provider contract is specified. If no provider contract is specified, the same features are available as for transactional queries. There are only a few differences in the syntax checks to transactional queries. The differences are listed in topic [no contract](abencds_pv_no_contract.md).

## Hint

A CDS projection view can be extended using a [CDS view entity extension](../../abap-glossary/abencds_view_entity_extend_glosry.md) `EXTEND VIEW ENTITY`. For details, see topic [CDS DDL - `EXTEND VIEW ENTITY`](abencds_extend_view_entity.md).

## Restrictions

CDS projection views cannot be used as base objects for reports. More information can be found in the [data source matrix](abencds_data_source_matrix.md).

## More Information

For more information about CDS projection views, see [*CDS Projection Views*](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/f6e118ed57374f96984d55e78d1f9871?version=sap_cross_product_abap) in the ABAP Data Models guide on SAP Help Portal.
