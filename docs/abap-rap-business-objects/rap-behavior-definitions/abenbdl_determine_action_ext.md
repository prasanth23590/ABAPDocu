---
title: "RAP - extend determine action"
source_file: abenbdl_determine_action_ext.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension > RAP - EntityBehaviorExtension > RAP - ExtensionBody > RAP - Extending Elements"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - extend determine action

## Syntax

``` abap
extend determine action DetermineActionName 
          { 
           determination [(always)] MyDetermination1; 
           determination [(always)] MyDetermination2; 
           validation [(always)] MyValidation1; 
           validation [(always)] MyValidation2; 
           determination [(always)] Child~ChildDetermination; 
           validation [(always)] Child~ChildValidation; 
           ... 
          }  
```

[`determination`](abenbdl_determinations.md) · [`determination`](abenbdl_determinations.md) · [`validation`](abenbdl_validations.md) · [`validation`](abenbdl_validations.md) · [`determination`](abenbdl_determinations.md) · [`validation`](abenbdl_validations.md)

## Prerequisites

- The respective determine action must allow extensions as described in topic [RAP - Extensibility Enabling for Base BOs](abenbdl_extensibility_enabling_m_u.md).

- The extended BDEF must be [draft-enabled](../../abap-glossary/abenrap_draft_handling_glosry.md). Determine actions can currently only be extended in draft-enabled RAP BOs.

## Description

Extends an existing [determine action](../../abap-glossary/abenrap_bo_det_action_glosry.md) `DetermineActionName` with extension [determinations](../../abap-glossary/abenrap_determination_glosry.md) and extension [validations](../../abap-glossary/abenrap_validation_glosry.md). At least one extension determination or extension validation must be specified within curly brackets.

If the optional addition `always` is used, then all determinations and validations that are part of the determine action are executed regardless of their trigger conditions. After a determination with the flag `always` has been executed, it can be triggered again by other determinations belonging to the same determine action.

Determinations and validations of [child entities](../../abap-glossary/abenchild_entity_glosry.md) can be included using the syntax `child~childDetermination` or `child~childValidation`, as long as these validations and determinations do not include the trigger operation `delete`.

Execution order: Determinations are executed first, validations afterwards. The execution order among determinations or validations themselves is defined by the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) and is independent of the specified order within the determine action.

[RAP authorization control](../../abap-glossary/abenrap_auth_control_glosry.md) from the extended BDEF is reused, if specified.

**Limitation:** Extensions for determine actions are currently not supported in unmanaged RAP BOs.

## Hint

[Internal](abenbdl_internal.md) determine actions cannot be extended.

**Related Information**

- [RAP BDL - determine action](abenbdl_determine_action.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following source code shows BDEF extension `DEMO_RAP_DET_ACT_EXT`. It extends BDEF `DEMO_RAP_EXTENSIBILITY_DET_ACT` by adding one further determination `setStatustoNew` to the determine action `trigger_all`.

The original BDEF explicitly allows extensions to the determine action `trigger_all`:

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

The extension adds one further determination `setStatustoNew` to the determine action `trigger_all`:

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

The ABAP class `CL_DEMO_CDS_EXT_DET_ACT` uses [EML](../../abap-glossary/abeneml_glosry.md) to access to [RAP business object](../../abap-glossary/abenrap_bo_glosry.md). It executes the determine action `trigger_all`.

The RAP framework executes the implementations in the original and extension ABAP behavior pools in the following order:

- `get_instance_authorizations`: check whether the operation on the root node is authorized.

- `setID`, a determination from the root node of the original BDEF.

- `setStatustoNew`, a determination from the root node extension.

- `get_instance_authorizations`: check whether the operation on the child node is authorized.

- `TotalPrice`, a determination from the child node of the original BDEF.

## Executable Example

The example above is explained in detail in the executable example [RAP - Extend Determine Action](abenbdl_det_action_ext_abexa.md).
