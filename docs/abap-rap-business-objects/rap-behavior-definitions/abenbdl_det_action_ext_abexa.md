---
title: "RAP - Extend Determine Action"
source_file: abenbdl_det_action_ext_abexa.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension > RAP - EntityBehaviorExtension > RAP - ExtensionBody > RAP - Extending Elements > RAP - extend determine action"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Extend Determine Action

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a determine action is extended via a BDEF extension.

**Data model**

The CDS data model consists of the root entity `DEMO_RAP_EXTENSIBILITY_DET_ACT` and its child entity `DEMO_RAP_EXT_DET_ACT_CHILD`.

Root entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, so, RAP managed'
define root view entity DEMO_RAP_EXTENSIBILITY_DET_ACT
  as select from demo_sales_order
  composition of exact one to many DEMO_RAP_EXT_DET_ACT_CHILD as _child
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
     _child

}
```

CDS transactional interface, root entity:

``` abap
@EndUserText.label: 'CDS transactional interface'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define root view entity DEMO_RAP_EXT_DET_ACT_INT 
provider contract transactional_interface
as projection on DEMO_RAP_EXTENSIBILITY_DET_ACT
{
  key SoKey,
  SalesOrderId,
  BuyerId,
  Status,
  CreatedBy,
  CreatedOn,
  CreatedAt,
  LastChangedBy,
  LastChangedOn,
  LastChangedAt,
  ShipToId,
  QuantitySum,
  UomSum,
  AmountSum,
  CurrencySum,
  CompanyCode,
  /* Associations */
  _child: redirected to composition child DEMO_RAP_EXT_DET_ACT_INT_CH
}
```

Child entity:

``` abap
@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'CDS view entity, o_,i RAP managed'
define view entity DEMO_RAP_EXT_DET_ACT_CHILD
  as select from demo_sales_so_i
  association to parent DEMO_RAP_EXTENSIBILITY_DET_ACT as _parent 
    on _parent.SoKey = $projection.ParentKey
{
  key so_item_key  as SoItemKey,
      parent_key   as ParentKey,
      material     as Material,
      posnr        as Posnr,
      @Semantics.amount.currencyCode: 'Currency'
      gross_amount as GrossAmount,
      currency     as Currency,
      @Semantics.quantity.unitOfMeasure: 'Unit'
      quantity     as Quantity,
      unit         as Unit,
      _parent
}
```

CDS transactional interface, child entity:

``` abap
@EndUserText.label: 'CDS transactional interface, child'
@AccessControl.authorizationCheck: #NOT_REQUIRED
define view entity DEMO_RAP_EXT_DET_ACT_INT_CH 
as projection on DEMO_RAP_EXT_DET_ACT_CHILD
{
  key SoItemKey,
  ParentKey,
  Material,
  Posnr,
  GrossAmount,
  Currency,
  Quantity,
  Unit,
  /* Associations */
  _parent: redirected to parent DEMO_RAP_EXT_DET_ACT_INT
}
```

**Behavior definition**

The [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) `DEMO_RAP_EXTENSIBILITY_DET_ACT` is defined in [RAP BDL](../../abap-glossary/abencds_bdl_glosry.md) as shown below. It defines the determine action `trigger_all`, which triggers two determinations. The behavior definition is extensible and explicitly allows extensions to the determine action `trigger_all`.

``` abap
managed implementation in class bp_demo_rap_extensibility_det_ unique;
strict(2);
extensible
{ with determinations on modify;
  with determinations on save;
  with validations on save; }
with draft;

define behavior for DEMO_RAP_EXTENSIBILITY_DET_ACT alias Root
persistent table demo_sales_order
draft table demo_sales_draft
lock master
total etag LastChangedAt
authorization master ( instance, global )
extensible
{
  create;
  update;
  delete;
  association _child { create; with draft; }
  field(readonly:update) SoKey;
  field ( readonly ) LastChangedAt;

  draft action Activate optimized;
  draft action Discard;
  draft action Edit;
  draft action Resume;

  draft determine action Prepare extensible
  { determination (always) setID; }

  determination setID on save { create; }

determine action trigger_all extensible
  {
    determination ( always ) setID;
    determination ( always ) Child ~ TotalPrice;
  }

  mapping for DEMO_SALES_ORDER corresponding extensible
  {
    SoKey = so_key;
    SalesOrderId = id;
    BuyerId = buyer_id;
    Status = lifecycle_status;
    ShipToId = ship_to_id;
    QuantitySum = quantity_sum;
    UomSum = uom_sum;
    AmountSum = amount_sum;
    CurrencySum = currency_sum;
    CompanyCode = company_code;
    CreatedBy = created_by;
    CreatedOn = created_on;
    CreatedAt = created_at;
    LastChangedBy = last_changed_by;
    LastChangedOn = last_changed_on;
    LastChangedAt = last_changed_at;
  }
}

define behavior for DEMO_RAP_EXT_DET_ACT_CHILD alias Child
persistent table demo_sales_so_i
draft table sales_i_draft
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;

  field ( readonly : update ) ParentKey, SoItemKey;

  determination TotalPrice on save { create; }

  association _parent { with draft; }

  mapping for DEMO_SALES_SO_I corresponding
  {
    SoItemKey = so_item_key;
    ParentKey = parent_key;
    GrossAmount = gross_amount;
  }
}
```

**RAP BO interface**

The following RAP BO interface is used as stable public interface for extensions.

``` abap
interface;
use draft;
extensible;
use side effects;

define behavior for DEMO_RAP_EXT_DET_ACT_INT alias Root
{
  use create;
  use update;
  use delete;

  use action trigger_all;

  use action Activate;
  use action Discard;
  use action Edit;
  use action Resume;
  use action Prepare;

  use association _child { create; with draft; }
}

define behavior for DEMO_RAP_EXT_DET_ACT_INT_CH alias Child
{
  use update;
  use delete;

  use association _parent { with draft; }
}
```

**Behavior extension**

The BDEF extension `DEMO_RAP_DET_ACT_EXT` extends the determine action `trigger_all` by adding a new determination on save.

``` abap
extension using interface DEMO_RAP_EXT_DET_ACT_INT
implementation in class bp_demo_rap_det_act_ext unique;

extend behavior for Root
{
  determination setStatustoNew on save { create; }

  extend determine action trigger_all
  {
    determination (always) setStatustoNew;
  }
}
```

**Behavior implementation**

For the RAP behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_RAP_EXTENSIBILITY_DET_`, see `BP_DEMO_RAP_EXTENSIBILITY_DET_CCIMP`. This global class implements three methods:

- `get_instance_authorizations`: Checks the value of field `CompanyCode`. If the company code is `ABCD`, update requests are not allowed. If the company code has any other value, updates are allowed.

- `setID`: determination on save that inserts a randomly generated integer into field `SalesOrderId`.

- `TotalPrice`: determination on save that multiplies the number of sales order items with the price and adds the result of all categories, thus calculating the total price of all items of a sales order.

For the RAP extension behavior definition, one [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md) is created. The global class of the behavior pool is `BP_DEMO_RAP_DET_ACT_EXT`, see `BP_DEMO_RAP_DET_ACT_EXT=======CCIMP`. This global class implements the determination `setStatustoNew`. When called, this determination inserts value `O` (meaning `open`), into the field `Status`.

**Note:** This is a simple example that serves demonstration purposes.

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
CLASS cl_demo_cds_ext_det_act DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    METHODS: 
      initialize_dbtabs, 
      fill_dbtabs. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_cds_ext_det_act IMPLEMENTATION. 
  METHOD main. 
 
    SELECT so_key, id, buyer_id, amount_sum, lifecycle_status 
      FROM demo_sales_order 
      INTO TABLE @FINAL(before_determination). 
 
    MODIFY ENTITIES OF demo_rap_ext_det_act_int 
       ENTITY root 
       EXECUTE trigger_all 
       FROM VALUE #( ( sokey = '0894EF1643A01EDB90EE45FBFB0C7DAA' ) 
                     ( sokey = '0894EF1643A01EDB90EE45FBFB0C9DAA' ) ) 
       MAPPED FINAL(mapped) 
       FAILED FINAL(failed) 
       REPORTED FINAL(reported) . 
 
    COMMIT ENTITIES. 
 
    IF sy-subrc <> 0. 
      out->write_doc( `An issue occurred in the RAP save sequence.` ). 
    ENDIF. 
 
    SELECT so_key, id, buyer_id, amount_sum, lifecycle_status 
    FROM demo_sales_order 
    INTO TABLE @FINAL(determination_successful). 
 
    out->next_section( 'Before determine action' 
     )->write( before_determination 
     )->next_section( 'Determine action successful' 
     )->write( determination_successful ). 
  ENDMETHOD. 
  METHOD fill_dbtabs. 
    INSERT demo_sales_order FROM TABLE @(  VALUE #( 
    ( so_key = '0894EF1643A01EDB90EE45FBFB0C7DAA' buyer_id = 'aa' ) 
    ( so_key = '0894EF1643A01EDB90EE45FBFB0C9DAA' buyer_id = 'bb' ) 
    ) ). 
 
    INSERT demo_sales_so_i FROM TABLE @(  VALUE #( 
    ( so_item_key = '0894EF1643A01EEB90EFE37277630A36' 
      parent_key = '0894EF1643A01EDB90EE45FBFB0C7DAA' 
      gross_amount = 123 
      quantity = 5 ) 
    ( so_item_key = '0894EF1643A01EEB90EFE37277630A37' 
      parent_key = '0894EF1643A01EDB90EE45FBFB0C9DAA' 
      gross_amount = 40 
      quantity = 1 ) 
    ) ). 
  ENDMETHOD. 
  METHOD initialize_dbtabs. 
    DELETE FROM demo_sales_order. 
    DELETE FROM demo_sales_so_i. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    initialize_dbtabs( ). 
    fill_dbtabs(  ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

**Access with ABAP using EML**

The above source code uses ABAP SQL and [ABAP EML](../../abap-glossary/abeneml_glosry.md) to access the [RAP business object](../../abap-glossary/abenrap_bo_glosry.md) from an ABAP class:

- It inserts two parent instances and two child instances directly into the database tables using ABAP SQL [`INSERT`](../../abap-programming-language/abap-processing-internal-data/abapinsert_itab.md). This is done to avoid triggering the determinations (all three of them are triggered by EML [`MODIFY ENTITIES CREATE`](../abap-for-rap-business-objects/abapmodify_entity_entities_op.md)).

- It executes the determine action `trigger_all`.

- Using the ABAP SQL [`SELECT`](../../abap-programming-language/abap-database-access/abapselect.md) statement, the content of the parent table before and after executing the determine action is displayed. The fields `SalesOrderId`, `AmountSum`, and `Status` have values that were inserted via the determinations.

The RAP framework executes the implementations in the original and extension ABAP behavior pools in the following order:

- `get_instance_authorizations`: Checks whether the operation on the root node is authorized.

- `setID`, a determination from the root node of the original BDEF.

- `setStatustoNew`, a determination from the root node extension.

- `get_instance_authorizations`: Checks whether the operation on the child node is authorized.

- `TotalPrice`, a determination from the child node of the original BDEF.
