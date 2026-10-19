---
title: "CDS SDL - DEFINE SERVICE"
source_file: abensrvd_define_service.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Service Definitions > ABAP CDS - SDL for Service Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS SDL - DEFINE SERVICE

## Syntax

``` abap
[@service_annot1] 
[@service_annot2] 
  ... 
[DEFINE] SERVICE service 
[PROVIDER CONTRACTS contract] 
{ 
    EXPOSE cds_entity [AS alias]; 
  | EXPOSE METHOD class_name=>method_name AS alias; 
   ... 
}  
```

[`@service_annot1`](abencds_define_service_annos.md) · [`@service_annot2`](abencds_define_service_annos.md) · [`PROVIDER CONTRACTS contract`](abensrvd_provider_contract.md)

## Description

The statement `DEFINE SERVICE` implements a [CDS service definition](../../abap-glossary/abencds_service_definition_glosry.md) with the name `service` in [CDS SDL](../../abap-glossary/abencds_sdl_glosry.md). The name `service` is in the same namespace as the [CDS entities](../../abap-glossary/abencds_entity_glosry.md) defined with [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md) and must satisfy the appropriate naming conventions.

The service definition can expose the following objects for a [business service](../../abap-glossary/abenbusiness_service_glosry.md):

- One or more CDS entities `cds_entity`. Each CDS entity is exposed using its own statement `EXPOSE` within the curly brackets. Each statement must be closed by a semicolon `;`. Possible CDS entities are [CDS views](../../abap-glossary/abencds_view_glosry.md), [CDS abstract entities](../../abap-glossary/abencds_abstract_entity_glosry.md), or [CDS custom entities](../../abap-glossary/abencds_custom_entity_glosry.md). For each CDS entity, the addition `AS` can be used to specify an optional alias name `alias`. The CDS entity is exposed under this alias name and it must be used when the business service is accessed.

- One or more [AMDP procedure implementations](../../abap-glossary/abenamdp_procedure_method_glosry.md) `method_name`. Each AMDP procedure implementation is exposed after the statement `EXPOSE METHOD`. First, the class name `class_name` is specified, followed by the [class component selector](../../abap-glossary/abenclass_component_select_glosry.md) `=>` and the name of the AMDP procedure implementation `method_name`. An alias name `alias` is mandatory. Each statement must be closed by a semicolon `;`.

  The following prerequisites must be met to expose an AMDP procedure implementation:

  - The service definition must have the [provider contract](../../abap-glossary/abencds_provider_contract_glosry.md) [`SQL`](abensrvd_provider_contract.md).

  - The procedure to be exposed must be specified as [`FOR SQL SERVICE`](../../abap-programming-language/abap-database-access/abapclass-methods_for_sql_service.md) in the class declaration part.

At least one object (CDS entity or AMDP procedure implementation) must be exposed within the curly brackets.

The optional annotations [`@service_annot1`](abencds_define_service_annos.md), [`@service_annot2`](abencds_define_service_annos.md), ... can be specified in front of the statement `DEFINE SERVICE`.

The optional addition [`PROVIDER CONTRACTS`](abensrvd_provider_contract.md) can be used to define a provider contract ` contract` for the service definition in question. A provider contract defines the scenario for which the service definition in question is intended. It is a prerequisite for releasing the service definition in question under the [C0 release contract for extensibility](../../abap-glossary/abenc0_contract_glosry.md).

## Hints

- If a service definition exposes multiple CDS entities, these entities should be related semantically. For example, if a CDS view with CDS associations is exposed in a service definition, it is recommended that the association targets of each CDS association are exposed as well. Together with the [root entity](../../abap-glossary/abenroot_entity_glosry.md) of a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) all other CDS entities of the [composition tree](../../abap-glossary/abencds_composition_tree_glosry.md) should also be exposed. However, there is no syntax check to verify the relationship between the exposed entities.

- If a service definition is used in a business service, it must be linked with a [RESTful](../../abap-glossary/abenrestful_glosry.md) protocol using a [service binding](../../abap-glossary/abenservice_binding_glosry.md). The service definition itself, however, is independent of the protocol in question and can be used with different protocols in multiple service bindings.

- Further restrictions apply to the CDS entities in question when using a service definition in a service binding. For example, the definition must have at least one key field or the cardinalities of the CDS associations must be defined correctly.

- No service bindings can be defined for service definitions that expose CDS abstract entities.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following service definition exposes CDS views that are related to each other under their own names by CDS associations.

``` abap
define service demo_sd_assoc_scarr_spfli {
  expose demo_cds_assoc_scarr;
  expose demo_cds_assoc_spfli;
  expose demo_cds_sflight;
  expose demo_cds_sairport;
}
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following service definition exposes a CDS view under an alias name.

``` abap
@EndUserText.label: 'Expose demo_cds_cross_join'
define service DEMO_SD_CROSS_JOIN {
  expose demo_cds_cross_join as demo_t000_t100;
}
```

## Executable Example

See [Consuming Business Services](abenconsume_bs_abexa.md).
