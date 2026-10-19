---
title: "ABAP CDS - Service Bindings"
source_file: abencds_service_bindings.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Service Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Service Bindings

A service binding is a [repository object](../../abap-glossary/abenrepository_object_glosry.md) defined in a form-based tool in [ABAP Development Tool (ADT)](../../abap-glossary/abenadt_glosry.md) that binds a [CDS service definition](../../abap-glossary/abencds_service_definition_glosry.md) to a communication protocol and provides it as a [business service](../../abap-glossary/abenbs_glosry.md) to be used outside of [AS ABAP](../../abap-glossary/abenas_abap_glosry.md).

The following service binding types are currently available:

- Different variants of [OData](../../abap-glossary/abenodata_glosry.md) can be used as the [RESTful](../../abap-glossary/abenrestful_glosry.md) protocol:

  - OData in versions 2 and 4

  - OData for UIs or Web APIs

    OData for UIs is designed for access to business services using UI technologies like [SAPUI5](../../abap-glossary/abensapui5_glosry.md). The data provided by a business service contains control elements for user interfaces. These elements are themselves defined by [framework-specific annotations](../../abap-glossary/abenfrmwrk_annotation_glosry.md) in the [CDS entities](../../abap-glossary/abencds_entity_glosry.md) in question. OData for [Web APIs](../../abap-glossary/abenweb_api_glosry.md) is limited to the data-only content of the business services and does not contain any control elements for user interfaces.

- The [Information Access (InA) protocol](../../abap-glossary/abenina_protocol_glosry.md) can be used for [analytical queries](../../abap-glossary/abencds_analytical_pv_glosry.md).

- [SQL services](../../abap-glossary/abenabap_sql_services_glosry.md)

When a service binding is activated, it makes the business service accessible in accordance with the protocol used. This involves technologies such as [SAP Gateway](../../abap-glossary/abensap_gateway_glosry.md) and the [RAP query engine](../../abap-glossary/abenrap_query_engine_glosry.md).

## Hints

- Once a service binding is activated, the form-based tool of [ABAP Development Tool (ADT)](../../abap-glossary/abenadt_glosry.md) shows the associated URL and enables comprehensive testing of the service.

- [SAP Gateway](../../abap-glossary/abensap_gateway_glosry.md) offers [OData client proxies](https://help.sap.com/docs/ABAP_PLATFORM_NEW/68bf513362174d54b58cddec28794093/bb778da49bf34e03a699eb476d4bb316) in order to access OData data of an AS ABAP. These are of special use for OData data of business services.

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [*Service Binding*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/b58a3c27df4e406f9335d4b346f6be04?version=sap_cross_product_abap).

## Executable Examples

See [Consuming Business Services](abenservice_bindings_abexas.md).
