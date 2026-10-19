---
title: "CDS DDL - CDS Projection View, Expose Associations"
source_file: abencds_proj_view_assoc_abexa.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - CDS Entities > ABAP CDS - Projection Views > CDS DDL - CDS Projection View, Transactional Queries > CDS DDL - projection_list, Transactional Query > CDS DDL - proj_element, Transactional Query > CDS DDL - expose_assoc, Transactional Query > CDS DDL - redirected, Transactional Query"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - CDS Projection View, Expose Associations

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how to read fields via exposed associations in a [CDS projection view](../../abap-glossary/abencds_projection_view_glosry.md).

**CDS projection view**

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Projection View SO Item'
@Metadata.allowExtensions: true
define view entity DEMO_SALES_PV_SO_I
  as projection on
    DEMO_SALES_CDS_SO_I
    {
      key so_item_key                   as SalesOrderItemKey,
          parent_key                    as SalesOrderKey,
          posnr                         as PositionNumber,
          @ObjectModel.text.element: ['MaterialName']
          material                      as MaterialId,
          _Material._Text.material_name as MaterialName : localized,
          @Semantics.amount.currencyCode: 'Currency'
          gross_amount                  as GrossAmount,
          currency                      as Currency,
          @Semantics.quantity.unitOfMeasure: 'Unit'
          quantity                      as Quantity,
          unit                          as Unit,
          _SalesOrder   : 
                  redirected to parent DEMO_SALES_PV_SO,
          _SalesOrder.buyer_id          as BuyerID,
          _ScheduleLine : 
                  redirected to composition child DEMO_SALES_PV_SO_I_SL
    }
```

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_proj_view_read_assoc DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS 
      constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_proj_view_read_assoc IMPLEMENTATION. 
  METHOD main. 
    SELECT * 
      FROM demo_sales_pv_so_i 
      WHERE positionnumber > 10 
      ORDER BY materialname 
      INTO TABLE @FINAL(result). 
 
    out->write( result ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
 
    DELETE FROM demo_sales_bupa. 
    DELETE FROM demo_sales_mat. 
    DELETE FROM demo_sales_order. 
    DELETE FROM demo_sales_so_i. 
 
*  Create Material 
    DATA lt_materials TYPE TABLE OF demo_sales_mat. 
    lt_materials = VALUE #( 
      ( 
      matnr = 1 
      mtgrp = 'METAL' 
      mtart = 'METL' 
      ) 
      ( 
      matnr = 2 
      mtgrp = 'HEAVY_METAL' 
      mtart = 'METL' 
      ) 
      ( 
      matnr = 3 
      mtgrp = 'HEAVY_METAL' 
      mtart = 'METL' 
      ) 
      ( 
      matnr = 4 
      mtgrp = 'LIGHT_METAL' 
      mtart = 'METL' 
      ) 
    ). 
    MODIFY demo_sales_mat FROM TABLE @lt_materials. 
 
*  Create Sales Order 
 
    DATA lt_sales_order TYPE TABLE OF demo_sales_order. 
    TRY. 
        lt_sales_order = VALUE #( 
          ( 
            so_key           = cl_system_uuid=>create_uuid_c32_static( ) 
            id               = 'SO_ID0001' 
            created_at       = '000000' 
            created_by       = sy-uname 
            created_on       = '00010101' 
            last_changed_at  = '000000' 
            last_changed_by  = '000000' 
            last_changed_on  = '00010101' 
            ship_to_id       = cl_system_uuid=>create_uuid_c32_static( ) 
            buyer_id         = cl_system_uuid=>create_uuid_c32_static( ) 
            lifecycle_status = 'A' 
          ) 
          ( 
            so_key           = cl_system_uuid=>create_uuid_c32_static( ) 
            id               = 'SO_ID0002' 
            created_at       = '000000' 
            created_by       = sy-uname 
            created_on       = '00010101' 
            last_changed_at  = '000000' 
            last_changed_by  = '000000' 
            last_changed_on  = '00010101' 
            ship_to_id       = cl_system_uuid=>create_uuid_c32_static( ) 
            buyer_id         = cl_system_uuid=>create_uuid_c32_static( ) 
            lifecycle_status = 'A' 
          ) 
        ). 
      CATCH cx_uuid_error ##NO_HANDLER. 
    ENDTRY. 
    MODIFY demo_sales_order FROM TABLE @lt_sales_order. 
 
* Create Sales Order Items 
    DATA lt_sales_order_items TYPE TABLE OF demo_sales_so_i. 
 
    FINAL(lo_random_number) = cl_abap_random_int=>create( 
      min = 0 
      max = 100 
    ). 
    TRY. 
        DO 20 TIMES. 
 
          FINAL(lv_material_index) = 
              ( sy-index MOD lines( lt_materials ) ) + 1. 
          FINAL(lv_random_number)  = lo_random_number->get_next( ). 
 
 
          INSERT VALUE #( 
            so_item_key  = cl_system_uuid=>create_uuid_c32_static( ) 
            parent_key   = lt_sales_order[ 1 ]-so_key 
            posnr        = sy-index 
            material     = lt_materials[ lv_material_index ]-matnr 
            quantity     = lv_random_number 
            unit         = 'KG' 
            gross_amount = lv_random_number * '1.15' 
            currency     = 'EUR' 
          ) INTO TABLE lt_sales_order_items. 
 
          INSERT VALUE #( 
            so_item_key  = cl_system_uuid=>create_uuid_c32_static( ) 
            parent_key   = lt_sales_order[ 2 ]-so_key 
            posnr        = sy-index 
            material     = lt_materials[ 1 ]-matnr 
            quantity     = lv_random_number 
            unit         = 'KG' 
            gross_amount = lv_random_number * '1.15' 
            currency     = 'EUR' 
          ) INTO TABLE lt_sales_order_items. 
 
        ENDDO. 
      CATCH cx_uuid_error ##NO_HANDLER. 
    ENDTRY. 
    MODIFY demo_sales_so_i FROM TABLE @lt_sales_order_items. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The CDS projection view `DEMO_SALES_PV_SO_I` is based on the CDS view `DEMO_SALES_CDS_SO_I` and exposes a subset of its fields. It also redirects the to-parent association to a new target and exposes one of the parent entity's fields, namely, BuyerID. The `SELECT` statement reads all the fields, orders them and filters them.
