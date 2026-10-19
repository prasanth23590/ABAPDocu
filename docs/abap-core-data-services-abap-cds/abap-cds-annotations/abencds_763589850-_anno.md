---
title: "ObjectModel.query.implementedBy"
source_file: abencds_763589850-_anno.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Annotations > ABAP CDS - SAP Annotations > ABAP CDS - SAP Annotation Documentation > ABAP Annotations > ObjectModel"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ObjectModel.query.implementedBy

## Annotation Properties

The following table shows the [properties](abencds_sap_anno_props.md) of the annotation:

| **Kind**    | [ABAP annotation](../../abap-glossary/abenabap_annotation_glosry.md) |
|-------------|----------------------------------------------------|
| **Syntax**  | `ObjectModel.query.implementedBy`                  |
| **Scope**   | `#CUSTOM_ENTITY`, `#ENTITY`                        |
| **Type**    | `String(255)`                                      |
| **Enums**   | `-`                                                |
| **Default** | `-`                                                |
| **Text**    | `-`                                                |
| **MDE**     | `-`                                                |
| **API**     | `RELEASED_FOR_SAP_CLOUD_PLATFORM`                  |

## Annotation Documentation

The [annotation definition](../../abap-glossary/abencds_anno_definition_glosry.md) documentation ([KTD](../../abap-glossary/abenktd_glosry.md)) is shown below.

## ObjectModel

### Short Description

ObjectModel annotations provide definitions of text-related aspects of the CDS-based data model.

## query

Specifies query settings.

## implementedBy

## Evaluation Engine

Runtime

### Short Description

Binds an ABAP class to a CDS entity that overrides the entity's own data retrieval method. The data retrieval is performed at runtime by a method of the class.

### Annotation Value

ABAP:'class_name': The name of the ABAP class class_name must be specified in single quotation marks and it must be written in uppercase letters. It is introduced by the string ABAP:.

### Further Information

This annotation is currently supported in all CDS entities except for [CDS abstract entities](../../abap-glossary/abencds_abstract_entity_glosry.md). The annotation is evaluated by frameworks such as [SADL](../../abap-glossary/abensadl_glosry.md) and therefore, it is especially relevant for entities that can be used in [RAP business services](../../abap-rap-business-objects/abencds_business_services.md).

#### Hints

- This annotation is [framework specific](../../abap-glossary/abenfrmwrk_annotation_glosry.md). It is not evaluated by the ABAP runtime framework, but, e.g., by the [SADL](../../abap-glossary/abensadl_glosry.md) framework instead. The ABAP class must implement the predefined ABAP interface `IF_RAP_QUERY_PROVIDER` to connect it to SADL.

- This annotation was first made available for [CDS custom entities](../../abap-glossary/abencds_custom_entity_glosry.md) and this kind of data retrieval is typical for CDS custom entities. Only later it was also made available for other kinds of CDS entities.

- In CDS custom entities, the annotation `ObjectModel.query.implementedBy` is mandatory when working in [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md). In all other environments and for all other CDS entities, it is optional.

- If a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md) implements a [RAP unmanaged query](../../abap-glossary/abenrap_unmanged_query_glosry.md) using `ObjectModel.query.implementedBy` and it also contains a [CDS virtual element](../../abap-glossary/abencds_virtual_element_glosry.md), then the ABAP query is evaluated first and the CDS virtual element is calculated afterwards. The CDS virtual element can use values returned by the ABAP query. This can be useful, for example, in extensibility scenarios.

#### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The CDS view entity `DEMO_CDS_SCARR_FROM_ABAP_CLASS` is bound to ABAP class `CL_DEMO_GET_SCARR`. This ABAP class implements the interface `IF_RAP_QUERY_PROVIDER` and it implements the same SQL query as the view entity does via its `SELECT` statement.

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@ObjectModel.query.implementedBy: 'ABAP:CL_DEMO_GET_SCARR'
define view entity DEMO_CDS_SCARR_FROM_ABAP_CLASS
  with parameters
    p_carrid : s_carr_id
  as select from scarr
{
  key carrid,
      carrname,
      url
}
where
  carrid = $parameters.p_carrid
```

The class `CL_DEMO_CONSUME_BS_SCARR_ABAP` accesses the CDS view entity once via its [service binding](../../abap-glossary/abenservice_binding_glosry.md) `DEMO_SB_SCARR_FROM_ABAP`, which binds the service definition `DEMO_SD_SCARR_FROM_ABAP_CLASS` to an OData node in ICF. This is done using the demonstration class `CL_DEMO_BS_CONSUMPTION`, which accesses the OData service of the service binding by using an ICF client.

The program accesses the CDS view entity a second time using a `SELECT` statement. The result is the same, the only difference is that the query class returns the message *Nothing found* whereas the `SELECT` statement returns no entries in case the query does not return any values.
