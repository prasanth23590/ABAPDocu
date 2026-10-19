---
title: "CLASS-METHODS, FOR SQL SERVICE"
source_file: abapclass-methods_for_sql_service.html
section: "ABAP Programming Language > ABAP - Database Access > ABAP Managed Database Procedures (AMDP) > AMDP - Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CLASS-METHODS, FOR SQL SERVICE

## Syntax

``` abap
CLASS-METHODS meth FOR SQL SERVICE 
        AMDP OPTIONS READ-ONLY {CDS SESSION CLIENT DEPENDENT} | {CLIENT INDEPENDENT} 
        [IMPORTING parameters] 
         EXPORTING parameter1 [parameter2 ...]  .
```

[`AMDP OPTIONS`](abapmethods_amdp_options.md) · [`CDS SESSION CLIENT DEPENDENT} | {CLIENT INDEPENDENT`](abapmethods_amdp_options_client.md) · [`parameters`](../abap-declarations/abapmethods_parameters.md)

## Description

This statement declares the [static method](../../abap-glossary/abenstatic_method_glosry.md) `meth` as an [AMDP procedure implementation](abenamdp_procedure_methods.md) that is intended to be exposed for external SQL access using an [SQL service](../../abap-glossary/abenabap_sql_services_glosry.md) (see also [`DEFINE SERVICE`](../../abap-core-data-services-abap-cds/abap-cds-service-definitions/abensrvd_define_service.md)). Only AMDP `READ-ONLY` methods are allowed. Only [client-safe](../../abap-glossary/abenclient_safe_glosry.md) methods can be exposed.

This statement can only be specified in the [public](../../abap-glossary/abenpublic_glosry.md) [visibility section](../../abap-glossary/abenvisibility_section_glosry.md) of an [AMDP class](abenamdp_classes.md). The signature and implementation must be declared in the same class, that is, the method must neither be inherited nor be an interface implementation.

Since the static method defines an AMDP procedure, the method must be implemented using the addition [`BY DATABASE PROCEDURE FOR HDB LANGUAGE SQLSCRIPT`](abapmethod_by_db_proc.md).

## Use

The addition `FOR SQL SERVICE` in the method declaration serves to indicate that the AMDP procedure is intended for an exposure to external clients using a [CDS service definition](../../abap-glossary/abencds_service_definition_glosry.md) with a [CDS provider contract](../../abap-glossary/abencds_provider_contract_glosry.md) of type *SQL* and a [service binding](../../abap-glossary/abenservice_binding_glosry.md) of type *SQL - Web API*. Data exposure using an SQL service is the key element for data integration scenarios for cross-system analytics, for example.

## Restrictions

The restrictions for [AMDP procedure methods](abenamdp_procedure_methods.md) apply. In addition, the following restrictions apply:

- Only `IMPORTING` and `EXPORTING` parameters are allowed. There must be at least one `EXPORTING` parameter.

- Scalar or tabular input and output parameters can be used as follows:

  - Parameters can only be typed with DDIC data types ([DDIC data elements](../../abap-glossary/abendata_element_glosry.md) or [DDIC table types](../../abap-glossary/abenddic_table_type_glosry.md)).

  - The [built-in DDIC types](../../abap-glossary/abenbuiltin_ddic_type_glosry.md) `CURR`, `LANG`, `LCHR`, `LRAW`, and `VARC` are not allowed as scalar parameters.

  - Only standard tables [with empty keys](../abap-data-types-and-data-objects/abenitab_empty_key.md) are allowed as tabular parameters. The table line type must not have includes.

  - The data types `CURR` and `LANG` are not allowed as components of tabular parameters.

- It is not allowed to define a [start value](../../abap-glossary/abenstart_value_glosry.md) for a parameter using the addition [`DEFAULT`](../abap-declarations/abapmethods_parameters.md).

- Standard AMDP procedure implementations can be called using database hints, but such a parameter `call_hints` is not allowed here.

- The parameter name `connection` (used for database connections) is not allowed.

## Hint

There is no access control available for the output parameters of a procedure call. As a result, during a procedure call using the SQL service, all data is returned by a procedure output parameter.

## More Information

- *ABAP Integration and Connectivity* guide, section [Data Integration](https://help.sap.com/docs/ABAP_Cloud/eede1416d18c436e8810eaaeb20c38ae/84537caeb611420b9f3435efce209ef7).
