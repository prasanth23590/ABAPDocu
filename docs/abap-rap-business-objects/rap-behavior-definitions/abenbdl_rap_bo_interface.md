---
title: "RAP - Interface Behavior Definition"
source_file: abenbdl_rap_bo_interface.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Interface Behavior Definition

A [RAP interface behavior definition](../../abap-glossary/abencds_interface_bdef_glosry.md) is created using the behavior definition language [RAP BDL](../../abap-glossary/abencds_ddl_glosry.md) in [BDL source code](../../abap-glossary/abenbdl_source_code_glosry.md).

A [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md) is a RAP business object that serves as interface for stable consumption. It is typically released as [released API](../../abap-glossary/abenreleased_api_glosry.md) under the [C1 contract](../../abap-glossary/abenc1_contract_glosry.md). It might also be released under the [C0 contract](../../abap-glossary/abenc0_contract_glosry.md) for extensibility. A RAP BO interface consists of a [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) and a RAP interface behavior definition. It does not have a runtime handler and cannot specify an implementation class for [ABAP behavior implementation](../../abap-glossary/abenbehavior_implement_glosry.md). Instead, it reuses or inherits the behavior and characteristics of the underlying base BO. Each RAP BO can have multiple interfaces.

RAP BO interfaces can only be consumed with [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md). It is not possible to expose a RAP BO interface directly as [RAP business service](../../abap-glossary/abenbusiness_service_glosry.md).

The following image shows the role of RAP interface behavior definitions in a CDS data model. ![figure](images_abdoc_interface_bdef.png)

A RAP interface behavior definition must always be based on a [CDS transactional interface](../../abap-glossary/abencds_trans_interface_glosry.md) and it defines the behavior that is included in the interface. Another projection layer ([CDS transactional query](../../abap-glossary/abencds_transactional_pv_glosry.md) and [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md)) can be built on top of a RAP BO interface.

## More Information

Development guide for the ABAP RESTful Application Programming Model, topic [Business Object Interface](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/7caa146ddc4b4f24a58efd33f0f789b4?version=sap_cross_product_abap).
