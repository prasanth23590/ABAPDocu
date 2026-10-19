---
title: "CDS SDL - PROVIDER CONTRACTS"
source_file: abensrvd_provider_contract.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Service Definitions > ABAP CDS - SDL for Service Definitions > CDS SDL - DEFINE SERVICE"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS SDL - PROVIDER CONTRACTS

## Syntax

``` abap
... PROVIDER CONTRACTS INA 
                     | ODATA_V2_UI 
                     | ODATA_V4_UI 
                     | ODATA_V2_WEBAPI 
                     | ODATA_V4_WEBAPI 
                     | SQL ...  
```

### Variant

[1. `... PROVIDER CONTRACTS INA ...`](abensrvd_provider_contract.md#variant-1)

[2. `... PROVIDER CONTRACTS ODATA ...`](abensrvd_provider_contract.md#variant-2)

[3. `... PROVIDER CONTRACTS SQL ...`](abensrvd_provider_contract.md#variant-3)

## Overview

### Description

A [CDS provider contract](../../abap-glossary/abencds_provider_contract_glosry.md) can optionally be specified in a [CDS service definition](../../abap-glossary/abencds_service_definition_glosry.md) using the statement `PROVIDER CONTRACTS`. It defines the scenario for which the service definition in question is intended. The effect is that stricter syntax checks are applied. Each type of provider contract has a dedicated set of rules that it must follow.

Changing the value defined after `PROVIDER CONTRACTS` is possible, even after activation and transport of the respective service definition, as long as the corresponding service binding is not affected.

**Use Case**

A provider contract is a prerequisite for releasing a CDS service definition under the [C0 contract, extend](../../abap-glossary/abenc0_contract_glosry.md). It enforces strict rules that match the rules of a type of [service binding](../../abap-glossary/abenservice_binding_glosry.md). This ensures stability of [business services](../../abap-glossary/abenbusiness_service_glosry.md) and prevents service definition extensions from causing errors in the associated service bindings.

## More Information

- Further details on the different types of service binding protocols are described in the development guide for the ABAP RESTful Application Programming Model, section [*Service Binding*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/b58a3c27df4e406f9335d4b346f6be04?version=sap_cross_product_abap).

### Hints

- The provider contract specified in a CDS service definition and the service binding which is defined for the CDS service definition in question must match. Otherwise, an error occurs.

- Exactly one provider contract can be specified in a CDS service definition, except for OData providers. Multiple OData providers can be specified in a comma-separated list. However, OData provider contracts of type `UI` and `WEBAPI` cannot be combined.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following service definition specifies the provider contract `INA` and meets all corresponding requirements.

``` abap
@EndUserText.label: 'SD with provider contract'
@AbapCatalog.extensibility.extensible: true
define service DEMO_CDS_SD_PROVIDER_CONTRACT
  provider contracts ina {
  expose DEMO_CDS_ANALYTIC_CASE;
  expose DEMO_CDS_ANALYTIC_PARAMETER;
}
```

## Variant 1

`... PROVIDER CONTRACTS INA ...`

### Description

Switches on syntax checks that are needed if the service definition is published with the [Information Access (InA) protocol](../../abap-glossary/abenina_protocol_glosry.md). When this provider contract is specified, the following additional rules apply:

- The CDS entities exposed must be analytical queries. Two kinds of analytical query are acceptable:

  - Analytical queries with the annotation `@Analytics.query` set to `true`

  - [CDS projection views with the provider contract `analytical_query`](../../abap-glossary/abencds_analytical_pv_glosry.md).

- If the exposed CDS entity is an analytical query with the annotation `@Analytics.query: true`, exactly one entity must be exposed. Otherwise, a syntax check error occurs.

- If the exposed CDS entity is a CDS projection view with the provider contract `analytical_query`, then multiple entities can be exposed.

## Variant 2

`... PROVIDER CONTRACTS ODATA ...`

### Description

Switches on syntax checks that are needed if the service definition is bound to the OData protocol. The following provider contracts are related to the OData protocol:

- `ODATA_V2_UI`

- `ODATA_V4_UI`

- `ODATA_V2_WEBAPI`

- `ODATA_V4_WEBAPI`

## Variant 3

`... PROVIDER CONTRACTS SQL ...`

### Description

Switches on syntax checks that are needed if the service definition is published with the [SQL services](../../abap-glossary/abenabap_sql_services_glosry.md) protocol. The same checks are performed as for [service bindings](../../abap-glossary/abenservice_binding_glosry.md) of type SQL. The checks are documented on SAP Help Portal in the Developer Extensibility Guide, topic [Constraints](https://help.sap.com/docs/SAP_S4HANA_CLOUD/6aa39f1ac05441e5a23f484f31e477e7/e5e007357a794a3dad1925ef6acfb6f1).
