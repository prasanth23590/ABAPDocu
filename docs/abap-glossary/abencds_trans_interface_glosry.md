---
title: "CDS transactional interface"
source_file: abencds_trans_interface_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS transactional interface

[CDS](../abap-core-data-services-abap-cds/abencds_glossary.md)

## Definition

A CDS transactional interface is a [CDS projection view](abencds_projection_view_glosry.md) that is intended to serve as stable public interface for consumption. A CDS transactional interface should be classified by a [release contract](abenrelease_contract_glosry.md) and thus serve as [released API](abenreleased_api_glosry.md). They are typically used in the context of the [ABAP RESTful Application Programming Model](abenarap_glosry.md) to provide the basis for a [RAP BO interface](abenrap_bo_interface_glosry.md). A CDS transactional interface is defined using the [CDS DDL](abencds_ddl_glosry.md) statement [`DEFINE VIEW ENTITY AS PROJECTION ON`](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_define_view_as_interface.md) and it must have its [provider contract](../abap-core-data-services-abap-cds/abap-cds-data-definitions/abencds_pv_provider_contract.md) set to `TRANSACTIONAL_INTERFACE`. A CDS transactional interface is a [CDS persistent entity](abencds_sql_entity_glosry.md).
