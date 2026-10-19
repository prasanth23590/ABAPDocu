---
title: "ABAP RESTful Application Programming Model"
source_file: abenarap_glosry.html
section: "ABAP Glossary"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP RESTful Application Programming Model

[RAP](../abap-rap-business-objects/abenrap_glossary.md)

## Definition

Also ABAP RESTful Programming Model, ABAP RAP, or RAP for short. ABAP programming model that is [RESTful](abenrestful_glosry.md) or that meets the requirements of a [REST](abenrest_glosry.md) architecture. In ABAP RAP, [AS ABAP](abenas_abap_glosry.md) plays the role of a stateless Web server. [OData](abenodata_glosry.md) serves as the RESTful protocol for requests from Web clients and the state of a session can be saved to the [standard database](abenstandard_db_glosry.md). The modeling is based on [CDS entities](abencds_entity_glosry.md) and [RAP behavior definitions](abencds_behavior_definition_glosry.md).

For queries, CDS entities can be directly exposed by [business services](abenbusiness_service_glosry.md) and all data can be retrieved by the [RAP query engine](abenrap_query_engine_glosry.md). For transactional access to data, the model offers [RAP business objects](abenrap_bo_glosry.md), whose behavior is provided by the [managed RAP BO provider](abenmanaged_rap_bo_prov_glosry.md), or is implemented in [ABAP behavior implementations](abenbehavior_implement_glosry.md).

RAP is the transactional programming model for [ABAP Cloud](abenabap_cloud_glosry.md).

[***-\>* More about**](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/289477a81eec4d4e84c0302fb6835035?version=sap_cross_product_abap)
