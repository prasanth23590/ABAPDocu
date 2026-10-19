---
title: "RAP - Business Services (BS)"
source_file: abencds_business_services.html
section: "ABAP RAP Business Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Business Services (BS)

A [RAP business service](../abap-glossary/abenbusiness_service_glosry.md) is a [RESTful](../abap-glossary/abenrestful_glosry.md) service provided by [AS ABAP](../abap-glossary/abenas_abap_glosry.md) as part of [ABAP RAP](../abap-glossary/abenabap_rap_glosry.md). A RAP business service consists mainly of the following parts:

- [Service definition](../abap-core-data-services-abap-cds/abap-cds-service-definitions/abencds_service_definitions.md)

  A service definition exposes CDS entities that can be accessed by a business service.

- [Service binding](../abap-core-data-services-abap-cds/abap-cds-service-definitions/abencds_service_bindings.md)

  A service binding is a [repository object](../abap-glossary/abenrepository_object_glosry.md) that binds a service definition to a [RESTful](../abap-glossary/abenrestful_glosry.md) protocol, thereby publishing the business service for external consumption.

A business service can be used for both read and write access to AS ABAP. In the latter case, the CDS entity exposed by the service definition must be the root entity of a [RAP business object](../abap-glossary/abenrap_bo_glosry.md) for which there is a [RAP behavior definition](../abap-glossary/abencds_behavior_definition_glosry.md) and a behavior pool.

## Hint

A service definition can be published multiple times by different service bindings using different protocols.
