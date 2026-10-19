---
title: "CDS DDL - DEFINE CUSTOM ENTITY"
source_file: abencds_f1_define_custom_entity.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Custom Entities"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - DEFINE CUSTOM ENTITY

## Syntax

``` abap
[@entity_annot1] 
[@entity_annot2] 
... 
[@ObjectModel.query.implementedBy : 'class_name'] 
[DEFINE] [ROOT] CUSTOM ENTITY custom_entity 
         [parameter_list] 
          element_list[;]  
```

[`@entity_annot1`](abencds_f1_entity_annotations.md) · [`@entity_annot2`](abencds_f1_entity_annotations.md) · [`@ObjectModel.query.implementedBy : 'class_name'`](abencds_f1_custom_query.md) · [`parameter_list`](abencds_f1_custom_parameter_list.md) · [`element_list`](abencds_f1_custom_element_list.md)

### Addition

[1. `... ROOT ...`](abencds_f1_define_custom_entity.md#addition-1)

## Overview

### Description

Defines a [CDS custom entity](../../abap-glossary/abencds_custom_entity_glosry.md) `custom_entity` in the [CDS DDL](../../abap-glossary/abencds_ddl_glosry.md). When a CDS custom entity is activated, its metadata is created but no other object instances are created on the database or in AS ABAP. The name `custom_entity` must comply with the naming conventions for [dictionary types](../../abap-dictionary-ddic/ddic-data-types/abenddic_data_types.md) and can have a maximum of 30 characters.

- [`@entity_annot`](abencds_f1_entity_annotations.md) can be used to specify optional [annotations](../../abap-glossary/abencds_annotation_glosry.md) for the CDS custom entity.

- The annotation [`@ObjectModel.query.implementedBy`](abencds_f1_custom_query.md) binds an ABAP class which implements an ABAP query. This query is not called by the ABAP runtime framework but by a framework like the [RAP query engine](../../abap-glossary/abenrap_query_engine_glosry.md).

- [`parameter_list`](abencds_f1_entity_parameter_list.md) is used to declare a list of optional input parameters for the CDS custom entity.

- [`element_list`](abencds_f1_absent_element_list.md) is used to declare elements, CDS associations, CDS to-child associations, and CDS-to-parent associations of the CDS custom entity.

A CDS custom entity can be used as a global structured type in ABAP programs. The entity is located in the namespace of all [global types](../../abap-glossary/abenglobal_type_glosry.md) of an AS ABAP. The elements of the CDS custom entity define the components of the global structured type that can be referenced in ABAP programs using `TYPE`. As is the case for any CDS entity, the annotations of a CDS custom entity can be evaluated.

### Hints

- A CDS custom entity cannot be used as a data source in other CDS entities or in ABAP SQL.

- CDS custom entities can be used as values for the CDS annotations `AssociationRef` and `ElementRef`.

- The annotation `ObjectModel.query.implementedBy` is mandatory when working in [ABAP Cloud](../../abap-glossary/abenabap_cloud_glosry.md).

- In the context of the [ABAP RESTful Application Programming Model](../../abap-glossary/abenarap_glosry.md), custom entities are used as a data model basis for [RAP unmanaged queries](../../abap-glossary/abenrap_unmanged_query_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following DDL source code shows a CDS custom entity:

``` abap
@EndUserText.label: 'Custom Entity for Sales Order'
define root custom entity DEMO_SALES_SO_CUSTOM_ANALYTICS
  {
    key SalesOrderKey       : DEMO_BT_RAW_16;
        @EndUserText.label  : 'Sales Order Item Count'
        SalesOrderItemCount : int4;
        TypeCode            : abap.char(5);
  }
```

## Addition 1

`... ROOT`

### Description

In ABAP CDS, the keyword `ROOT` is used to define the CDS custom entity `custom_entity` as a [root entity](../../abap-glossary/abenroot_entity_glosry.md) of the hierarchy of a [business object](../../abap-glossary/abenbusiness_object_glosry.md). The following applies to the root entity:

- There is exactly one root entity in the structure of a business object.

- A root entity can have [child entities](../../abap-glossary/abenchild_entity_glosry.md) defined by means of [to-child associations](../../abap-glossary/abento_child_association_glosry.md) using the keyword [`COMPOSITION`](abencds_f1_custom_composition.md), but this is not mandatory. A root entity can also be a [leaf entity](../../abap-glossary/abenleaf_entity_glosry.md).

- A root entity does not have a [parent entity](../../abap-glossary/abenparent_entity_glosry.md). [To-parent](abencds_f1_custom_tp_association.md) associations are not allowed in root entities.
