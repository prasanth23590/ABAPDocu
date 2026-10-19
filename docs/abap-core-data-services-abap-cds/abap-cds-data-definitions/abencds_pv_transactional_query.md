---
title: "CDS DDL - CDS Projection View, Transactional Queries"
source_file: abencds_pv_transactional_query.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Projection View, Transactional Queries

[CDS transactional queries](../../abap-glossary/abencds_transactional_pv_glosry.md) are intended for modelling the projection layer of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md). A transactional projection view must always be part of a business object. That means it must either be a [root entity](../../abap-glossary/abenroot_entity_glosry.md) itself, or it must be part of a composition tree that contains a root entity. The feature set focuses on specializing the [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md) of the underlying business object. The runtime for transactional queries is mainly the [RAP query engine](../../abap-glossary/abenrap_query_engine_glosry.md), but also the [RAP transactional engine](../../abap-glossary/abenrap_transac_engine_glosry.md).

As a global data type, a CDS transactional query represents a structured type with the [elements of the CDS projection view](abencds_proj_view_element_list.md) as components. Usage:

- Unlike other CDS entities, CDS transactional queries currently **cannot** be used as data source of other CDS entities.

- They can be used in ABAP programs as a data type for definitions and in ABAP SQL read statements.

## Hint

Transactional projection views have evolved from and will in the future replace [consumption views](https://help.sap.com/docs/ABAP_PLATFORM_NEW/cc0c305d2fab47bd808adcad3ca7ee9d/82a882a0d1de41fa949ea7cd186f15c0). Both serve the same purpose, namely, to simplify the access to business objects. While consumption views were used for data modelling in the obsolete [ABAP Programming Model for SAP Fiori](../../abap-glossary/abenabap_pm_for_fiori_glosry.md), projection views take over this role in its successor [RAP](../../abap-glossary/abenarap_glosry.md).

## More Information

- Development guide for the ABAP RESTful Application Programming Model, topic [CDS Projection View](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/448c144391764977aefea5e1984ced38?version=sap_cross_product_abap).

- ABAP Data Models guide, section about [CDS Transactional Queries](https://help.sap.com/docs/ABAP_Cloud/aaae421481034feab3e71dd9e0f643bf/1c37dbd17b484bf39cbc3fff145539c9?version=sap_cross_product_abap)
