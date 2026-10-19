---
title: "RAP - Determination"
source_file: abenbdl_determination_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - determination"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Determination

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how determinations are defined, implemented, and consumed in a managed RAP BO.

**Data model**

The CDS data model consists of the root entity `DEMO_SALES_CDS_SO_2` and its child entity `DEMO_SALES_CDS_SO_I_2`. The root entity represents a sales order and the child entity represents a sales order item.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, so, RAP managed'
define root view entity DEMO_SALES_CDS_SO_2
  as select from demo_sales_order
  composition of exact one to many DEMO_SALES_CDS_SO_I_2 as _SalesOrderItem
{
  key so_key           as SoKey,
      id               as SalesOrderId,
      buyer_id         as BuyerId,
      lifecycle_status as Status,
      created_by       as CreatedBy,
      created_on       as CreatedOn,
      created_at       as CreatedAt,
      last_changed_by  as LastChangedBy,
      last_changed_on  as LastChangedOn,
      last_changed_at  as LastChangedAt,
      ship_to_id       as ShipToId,
      quantity_sum     as QuantitySum,
      uom_sum          as UomSum,
      amount_sum       as AmountSum,
      currency_sum     as CurrencySum,
      company_code     as CompanyCode,
      _SalesOrderItem // Make association public

}
```

Child entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, o_,i RAP managed'
define view entity DEMO_SALES_CDS_SO_I_2 
as select from demo_sales_so_i 
association to parent DEMO_SALES_CDS_SO_2 as _SalesOrder 
on _SalesOrder.SoKey = $projection.ParentKey
{
  key so_item_key as SoItemKey,
  parent_key as ParentKey,
  material as Material,
  posnr as Posnr,
  @Semantics.amount.currencyCode: 'Currency'
  gross_amount as GrossAmount,
  currency as Currency,
  @Semantics.quantity.unitOfMeasure: 'Unit'
  quantity as Quantity,
  unit as Unit,
  _SalesOrder
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_SALES_CDS_SO_2` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as follows:

``` abap
managed implementation in class bp_demo_sales_cds_so_2 unique;
strict ( 2 );

define behavior for DEMO_SALES_CDS_SO_2 alias SalesOrder
persistent table demo_sales_order
lock master
authorization master ( none )
{
  create;
  update;
  association _SalesOrderItem { create; }

  field ( readonly, numbering : managed ) SoKey;
  field ( readonly ) AmountSum;

  determination setID on save { create; }
  determination setStatustoNew on modify { create; }
  determination TotalPrice on modify { create; }

  mapping for demo_sales_order
    {
      SoKey         = so_key;
      SalesOrderId  = id;
      BuyerId       = buyer_id;
      Status        = lifecycle_status;
      ShipToId      = ship_to_id;
      QuantitySum   = quantity_sum;
      UomSum        = uom_sum;
      AmountSum     = amount_sum;
      CurrencySum   = currency_sum;
      CompanyCode   = company_code;
      CreatedBy     = created_by;
      CreatedAt     = created_at;
      CreatedOn     = created_on;
      LastChangedBy = last_changed_by;
      LastChangedOn = last_changed_on;
      LastChangedAt = last_changed_at;
    }
}

define behavior for DEMO_SALES_CDS_SO_I_2 alias SalesOrderItem
persistent table demo_sales_so_i
lock dependent by _SalesOrder
authorization dependent by _SalesOrder
{
  update;
  delete;

  field ( readonly : update ) ParentKey;
  field ( readonly, numbering : managed ) SoItemKey;

  association _SalesOrder { }

  determination TotalPrice_1 on modify { field Quantity, GrossAmount; }

  mapping for demo_sales_so_i corresponding
    {
      SoItemKey   = so_item_key;
      ParentKey   = parent_key;
      GrossAmount = gross_amount;
    }
}
```

**Definition of determinations**

The following determinations are defined in the root entity:

- `setID` is a determination on save that is triggered whenever a new instance of the root entity is created. It assigns values to the semantic key field `SalesOrderId` during the [save sequence](../../abap-glossary/abenrap_save_seq_glosry.md). The technical key field `SoKey` is populated by means of internal numbering using the statement [`numbering:managed`](abenbdl_field_numbering.md).

- `setStatustoNew` sets the status of a newly created sales order to `O` for *open*. It is triggered whenever a new sales order is created.

- `TotalPrice` sums up the price of all items of a sales order. It is triggered whenever a new sales order is created.

The child entity defines one determination on modify:

- `TotalPrice_1` is the counterpart to `TotalPrice`. If a sales order is created without any items, then this determination ensures that the overall price of a sales order is calculated as soon as sales order items are added.

**Behavior implementation**

For the above RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_SALES_CDS_SO_2`. The actual implementation takes place in the `BP_DEMO_SALES_CDS_SO_2========CCIMP` and it works as follows:

- `setID` generates a random value of type `i` for the field `SalesOrderId` of each BO instance.

- `setStatustoNew` inserts the value `O` for *Open* into column `Status` for each newly created BO instance.

- `TotalPrice` reads the fields `GrossAmount` and `Quantity` from the child entity via a [read-by-association operation](abenbdl_association.md). It first calculates the total price per item and then sums up the prices of all items for each sales order to get the overall price.

- `TotalPrice_1` works exactly like `TotalPrice`, but it has different trigger conditions.

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
CLASS cl_demo_cds_determination DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_determination IMPLEMENTATION. 
  METHOD main. 
 
    DELETE FROM demo_sales_order. 
    DELETE FROM demo_sales_so_i. 
 
    MODIFY ENTITIES OF demo_sales_cds_so_2 
      ENTITY SalesOrder 
        CREATE FIELDS ( BuyerId Status ) WITH VALUE #( 
           ( %cid = '1' BuyerId = `AAA` ) 
           ( %cid = '2' BuyerId = `BBB` ) ) 
 
     ENTITY SalesOrder 
        CREATE BY \_SalesOrderItem 
          FIELDS ( Material GrossAmount Quantity ) WITH VALUE #( 
          ( %cid_ref  = '1' 
            %target   = VALUE #( 
            ( %cid = 'cid_child1' material = 'aaa' 
              GrossAmount = 123 Quantity = 5 ) 
            ( %cid = 'cid_child2' material = 'bbb' 
              GrossAmount = 40 Quantity = 1 ) ) ) 
          ( %cid_ref  = '2' 
            %target   = VALUE #( 
            ( %cid = 'cid_child3' material = `xxx` 
              GrossAmount = 50 Quantity = 2 ) 
            ( %cid = 'cid_child4' material = `yyy` 
              GrossAmount = 12 Quantity = 1 ) ) ) ). 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT so_key, id, lifecycle_status, buyer_id, amount_sum 
    FROM demo_sales_order 
    INTO TABLE @FINAL(determination). 
 
    out->next_section( 'Determination result' 
        )->write( determination ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses [EML](../../abap-glossary/abeneml_glosry.md) to access the RAP business object from an ABAP class:

- Two BO instances are created with the statement `MODIFY ENTITY`. Two child entities are created for each root entity instance so both sales orders have two sales order items.

- All three determinations of the root entity are triggered by the creation of new instances and they insert values into the fields `ID`, `LIFECYCLE_STATUS`, and `AMOUNT_SUM`.

- The technical key field `SO_KEY` is filled by means of internal numbering.
