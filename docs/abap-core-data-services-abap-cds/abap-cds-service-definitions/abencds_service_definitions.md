---
title: "ABAP CDS - Service Definitions"
source_file: abencds_service_definitions.html
section: "ABAP Core Data Services (ABAP CDS)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP CDS - Service Definitions

A [CDS service definition](../../abap-glossary/abencds_service_definition_glosry.md) exposes [CDS entities](../../abap-glossary/abencds_entity_glosry.md) for a [RAP business service](../../abap-glossary/abenbusiness_service_glosry.md). Service definitions are created in [SDL source code](../../abap-glossary/abensdl_source_code_glosry.md) using [CDS SDL](../../abap-glossary/abencds_sdl_glosry.md).

- [SDL for Service Definitions](abencds_f1_sdl_syntax.md)

Service definitions can expose regular CDS entities and root entities of [RAP business objects](../../abap-glossary/abenrap_bo_glosry.md):

- [Service bindings](abencds_service_bindings.md) can be used to bind a CDS service definition to a communication protocol and publish it as a [business service](../../abap-glossary/abenbs_glosry.md).

- The publication of a regular CDS entity as a business service enables queries to be made from outside AS ABAP on the associated data using the protocol from the service binding.

- The publication of root entities of [RAP business objects](../../abap-glossary/abenrap_bo_glosry.md) also enables transactional writes to be made on the associated data.
