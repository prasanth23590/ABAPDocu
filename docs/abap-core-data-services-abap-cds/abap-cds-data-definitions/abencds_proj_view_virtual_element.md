---
title: "CDS DDL - VIRTUAL"
source_file: abencds_proj_view_virtual_element.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries > CDS DDL - projection_list, Transactional Query > CDS DDL - proj_element, Transactional Query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - VIRTUAL

## Syntax

``` abap
... VIRTUAL elem_name : typing  
```

[`typing`](abencds_typing.md)

## Description

Defines a [virtual element](../../abap-glossary/abencds_virtual_element_glosry.md) in the [projection list](abencds_proj_view_element_list.md) of a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md). Virtual elements are read-only elements of a CDS projection view which are not part of the [projected entity](../../abap-glossary/abencds_pv_projected_entity_glosry.md). Reading the virtual elements of a projection view with ABAP SQL delivers initial values. In order to fill and analyze the virtual elements of projection views, special frameworks like the [RAP query engine](../../abap-glossary/abenrap_query_engine_glosry.md) have to be involved.

In [RAP](../../abap-glossary/abenarap_glosry.md), for example, a virtual element can be connected to an ABAP class that implements a special virtual element interface by using the [framework-specific](../../abap-glossary/abenfrmwrk_annotation_glosry.md) annotation [`ObjectModel.virtualElementCalculatedBy`](abencds_f1_element_annotation.md). In that case the value of the virtual element is calculated during runtime by the [RAP query engine](../../abap-glossary/abenrap_query_engine_glosry.md). For more information, see the development guide for the ABAP RESTful Application Programming Model, section [Using Virtual Elements in CDS Projection Views](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/319380e0cef94051ae9aa292ffadb59a?version=sap_cross_product_abap).

## Hint

Virtual elements are also supported in CDS projection views that implement data retrieval via an ABAP class using the annotation [`ObjectModel.query.implementedBy`](abencds_f1_entity_annotations.md). This can be useful, for example, in extensibility scenarios. In this case, the ABAP query is evaluated first and the virtual element can use the returned values.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The projection view `DEMO_SALES_PV_SO_EXP` is based on the CDS view `DEMO_SALES_CDS_SO`. It contains a virtual element `expiry_date` that is bound to ABAP class `CL_DEMO_SALES_VIRT_ELEM_EXIT` that calculates the expiry date of an item during runtime if the view is accessed by the [RAP query engine](../../abap-glossary/abenrap_query_engine_glosry.md).

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Exposure of SO Projection View'
define root view entity DEMO_SALES_PV_SO_EXP
  as projection on DEMO_SALES_CDS_SO
  {
    key     so_key,
            id,
            lifecycle_status as LifecycleStatus,
            buyer_id         as BuyerId,
            created_by,
            @ObjectModel.virtualElementCalculatedBy:
                        'ABAP:CL_DEMO_SALES_VIRT_ELEM_EXIT'
    virtual expiry_date : abap.dats(8),
            _Buyer : redirected to DEMO_SALES_PV_BUPA_EXP
  }
```

## Executable Example

The executable example Calculating a virtual element accesses the CDS projection view shown above and returns the result of the virtual element.
