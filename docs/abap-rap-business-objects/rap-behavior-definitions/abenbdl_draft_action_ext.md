---
title: "RAP - extend draft determine action Prepare"
source_file: abenbdl_draft_action_ext.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension > RAP - EntityBehaviorExtension > RAP - ExtensionBody > RAP - Extending Elements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - extend draft determine action Prepare

## Syntax

``` abap
extend draft determine action Prepare 
             { 
             [determination [(always)] DetName;] 
             [validation [(always)] ValName;] 
             [determination [(always)] Child~ChildDetermination;] 
             [validation [(always)] Child~ChildValidation;] 
             ... 
              }  
```

[`determination`](abenbdl_determinations.md) · [`validation`](abenbdl_validations.md) · [`determination`](abenbdl_determinations.md) · [`validation`](abenbdl_validations.md)

## Prerequisites

- The respective draft determine action must be enabled for extensions in the extended BDEF as described in topic [RAP - Extensibility Enabling for Base BOs](abenbdl_extensibility_enabling_m_u.md).

## Description

Extends an existing [draft determine action Prepare](../../abap-glossary/abenrap_bo_draft_action_glosry.md) with extension [determinations](../../abap-glossary/abenrap_determination_glosry.md) and extension [validations](../../abap-glossary/abenrap_validation_glosry.md). At least one extension determination or extension validation must be specified within curly brackets. The optional addition [(always)](abenbdl_determine_action.md) can be used. Determinations and validations of child entities can be included.

**Limitation:** Extensions for the draft determine action `Prepare` are currently not supported in unmanaged RAP BOs.

## Hint

An [internal](abenbdl_internal.md) draft determine action Prepare cannot be extended.

**Related Information**

- [RAP - `draft action`](abenbdl_draft_action.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code shows BDEF extension `DEMO_RAP_PREPARE_EXT`. It extends the base BDEF `DEMO_RAP_EXTENSIBILITY_DET_ACT` by adding one further determination `myDet` to the draft determine action `Prepare`.

The base BDEF is draft-enabled and explicitly allows extensions to the draft determine action Prepare:

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

The BDEF extension adds one further determination to the draft determine action Prepare:

``` abap
extension using interface DEMO_RAP_EXT_DET_ACT_INT
implementation in class bp_demo_rap_prepare_ext unique;

extend behavior for Root
{
  determination myDet on save { create; }

  extend draft determine action Prepare
  {
    determination ( always ) myDet;
  }
}
```
