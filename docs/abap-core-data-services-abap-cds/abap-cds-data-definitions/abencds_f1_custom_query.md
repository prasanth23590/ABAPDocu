---
title: "CDS DDL - DEFINE CUSTOM ENTITY, ABAP Class"
source_file: abencds_f1_custom_query.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Custom Entities > CDS DDL - DEFINE CUSTOM ENTITY"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE CUSTOM ENTITY, ABAP Class

## Syntax

``` abap
... @ObjectModel.query.implementedBy : 'ABAP:class_name' ...  
```

[`@ObjectModel.query.implementedBy : 'ABAP:class_name'`](abencds_f1_entity_annotations.md)

## Description

The annotation [`@ObjectModel.query.implementedBy`](abencds_f1_entity_annotations.md) binds an ABAP class `class_name` as a query provider class to a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md). When a CDS custom query is accessed via a framework, such as the [RAP query engine](../../abap-glossary/abenrap_query_engine_glosry.md), the annotation is evaluated and the ABAP implementation is called to perform the query. The ABAP class must implement the predefined ABAP interface `IF_RAP_QUERY_PROVIDER` to connect it to the [RAP query engine](../../abap-glossary/abenrap_query_engine_glosry.md).

In the context of the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md), CDS custom queries are referred to as [RAP unmanaged queries](../../abap-glossary/abenrap_unmanged_query_glosry.md).

For more information, see the ABAP RESTful Application Programming Model Developer guide, section [Implementing an Unmanaged Query](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/254f68c7d5374e94a88241b7ce3bd414?version=sap_cross_product_abap).

The annotation `ObjectModel.query.implementedBy` is mandatory for CDS custom entities when working in [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md).

## Hint

While the annotation `ObjectModel.query.implementedBy` must be used for CDS custom entities in order to bind an ABAP class, it also can be used for other CDS entities. Then it overrides the original query of an CDS entity when accessed by a framework that evaluates the annotation.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The custom entity `DEMO_CDS_CUSTOM_ENTITY` is bound to ABAP class `CL_DEMO_CUSTOM_ENTITY_QUERY`. This ABAP class implements the interface `IF_RAP_QUERY_PROVIDER` and it generates an internal table with random UUID values.

``` abap
@EndUserText.label: 'CDS custom entity, query implementation'
@ObjectModel.query.implementedBy: 'ABAP:CL_DEMO_CUSTOM_ENTITY_QUERY'
define custom entity DEMO_CDS_CUSTOM_ENTITY
  with parameters
    p_number : int1
  {
    key id   : int4;
        uuid : abap.char(32);
  }
```

## Executable Example

The executable example [Implementing a custom query](abencds_custom_query_abexa.md) executes the query implementation class and returns data.
