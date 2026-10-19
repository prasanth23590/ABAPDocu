---
title: "CDS SDL - EXTEND SERVICE"
source_file: abensrvd_extend_service.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Service Definitions > ABAP CDS - SDL for Service Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS SDL - EXTEND SERVICE

## Syntax

``` abap
EXTEND SERVICE name 
  WITH 
{ 
    EXPOSE cds_entity [AS alias]; 
  | EXPOSE METHOD class_name=>method_name AS alias; 
   ... 
}  
```

## Description

Extends an existing [CDS service definition](../../abap-glossary/abencds_service_definition_glosry.md) `name` using a [CDS service definition extension](../../abap-glossary/abencds_service_def_ext_glosry.md) in the [CDS SDL](../../abap-glossary/abencds_sdl_glosry.md). An existing CDS service definition can have one or more CDS service definition extensions.

## Prerequisite

As a prerequisite for service definition extensions, the service definition to be extended must explicitly allow extensions. The annotation [`@AbapCatalog.extensibility.extensible`](abencds_define_service_annos.md) must be set to ` true`.

**Rules for a Service Definition Extension**

Service definition extensions can make additions to the original service definition, but they cannot modify, overwrite, or delete elements from it. The following rules apply:

- One or more [CDS entities](../../abap-glossary/abencds_entity_glosry.md) `cds_entity` can be exposed using the keyword `EXPOSE`. The same rules apply as to the original service definition, see topic [CDS SDL - `DEFINE SERVICE`](abensrvd_define_service.md).

- One or more [AMDP procedure implementations](../../abap-glossary/abenamdp_procedure_method_glosry.md) `method_name` can be exposed using the keyword `EXPOSE METHOD`. The same rules apply as to the original service definition, see topic [CDS SDL - `DEFINE SERVICE`](abensrvd_define_service.md).

- Each exposed CDS entity or AMDP procedure implementation must have a unique name across the original service definition and all existing extensions. In case of naming conflicts, an alternative element `alias` must be assigned using the addition `AS`.

- The exposed entities `cds_entity1`, `cds_entity2`, ... can be entities from the original data model or extension entities. The names of the exposed entities must comply with the [namespace](../../abap-glossary/abennamespace_glosry.md) of the service definition extension. For example, if the name of a service definition extension starts with a `Z`, each exposed entity must also have a name that starts with `Z`. This can also be achieved by assigning an alias name with the addition `AS`.

- Each entity and method should be exposed only once in a service definition and any of its extensions. Even if a new alias name is assigned, a syntax check warning occurs if an entity or method is exposed more than once.

## Restrictions

- CDS service definition extensions themselves cannot be extended.

- [Service definition annotations](abencds_define_service_annos.md) are not supported. That means that no annotations are allowed in front of the statement `EXTEND SERVICE`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following CDS service definition extension

``` abap
extend service DEMO_CDS_ORIGINAL_SD with {
  expose DEMO_RAP_EXTENSIBLE_EXT;
}
```

adds one further entity to the service definition

``` abap
@EndUserText.label: 'CDS service definition for extension'
@AbapCatalog.extensibility.extensible: true
define service DEMO_CDS_ORIGINAL_SD {
  expose DEMO_RAP_EXTENSIBLE_ROOT;
}
```
