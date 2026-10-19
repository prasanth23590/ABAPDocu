---
title: "RAP - determination"
source_file: abenbdl_determinations.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - determination

## Syntax

``` abap
determination DetName {on modify { CUD1 | {field Field1}; 
                                 [ CUD2;  ...; ]  [field Field2; ...] } } 
                     |{on save   { CUD1 | {field Field1}; 
                                 [ CUD2;  ...; ]  [field Field2; ...] } }  
```

## Description

A [determination](../../abap-glossary/abenrap_determination_glosry.md) modifies instances of [RAP business objects](../../abap-glossary/abenrap_bo_glosry.md) based on trigger conditions. A determination is implicitly invoked by the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) if the trigger condition of the determination is fulfilled. Trigger conditions can be [modify operations](../../abap-glossary/abenrap_modify_operation_glosry.md) ([create, update, delete](abenbdl_standard_operations.md)) `CUD1; CUD2; ...`, or modified fields `Field1; Field2; ...`. Two types of determinations are distinguished, depending on the stage of the program flow the determination is executed: `on modify` determinations and `on save` determinations. A determination can compute data, modify entity instances, and return messages. On modify determinations and on save determinations must be implemented in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR DETERMINE`](../abap-for-rap-business-objects/abaphandler_meth_det.md) in the local [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md).

The name `DetName` must comply with the general naming rules for RAP behavior definitions described in the topic [RAP BDL - General Syntax Rules](abenbdl_general_syntax_rules.md). In particular, is can have a maximum of 30 characters.

Determinations can be carried out at different points in time during the program logic:

- On modify: The determination is executed immediately after data changes take place in the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) so that the result is available during the transaction.

- On save: The determination is executed during the [save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) at the end of an transaction, when changes from the transactional buffer are persistent on the database.

**Trigger Conditions**

There can be one or more trigger conditions. The trigger conditions can be changes of field values or the execution of one of the [standard operations](abenbdl_standard_operations.md) create, update, or delete. The determination is triggered if at least one trigger condition is fulfilled.

- `create`: Determination is executed when an instance is created.

- `update`: Determination is executed when an instance is updated. For determinations defined as `on save`, update works only in combination with the trigger operation `create`.

- `delete`: Determination is executed when an instance is deleted.

- `field`: Determination is executed when the value of the specified field(s) `Field1, Field2, ...` are changed by a create or update operation. The fields that are used for the trigger conditions must belong to the same entity the determination is assigned to.

  **Note:** If a field is tagged with the [RAP field characteristic](../../abap-glossary/abenrap_field_char_glosry.md) [`notrigger[:warn]`](abenbdl_field_char.md), it must not be used in a trigger condition.

## Availability

- [Managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) and [draft-enabled](../../abap-glossary/abendraft_rap_bo_glosry.md) RAP BOs.

  Not available for unmanaged, non-draft RAP BOs.

## Hints

- The determination result must not change if the determination is executed several times under the same conditions (idempotence).

- The execution order of determinations is not fixed. If there is more than one determination triggered by the same condition, the execution order is arbitrary.

- Once a determination has been triggered, it must run independently from other determinations.

- If an instance is created and deleted with the same request, it can happen that an [EML](../../abap-glossary/abeneml_glosry.md) read operation in a determination defined as `on modify` fails as instances with the given key cannot be found.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section about [Determinations](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/6edb0438d3e14d18b3c403c406fbe209?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF based on the CDS root view entity `DEMO_SALES_CDS_SO_2`. The root view entity represents a sales order and the child entity `DEMO_SALES_CDS_SO_I_2` represents a sales order item. Three determinations are defined in the [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md):

- `setID` assigns values to the semantic key field `SalesOrderId` during the save sequence. The technical key field `SoKey` is populated by means of internal numbering using the statement [`numbering:managed`](abenbdl_field_numbering.md).

- `setStatustoNew` sets the status of a newly created sales order to `O` for *open*. It is triggered whenever a new sales order is created. This status can be changed to *Accepted* or *Rejected* during further processing.

- `TotalPrice` sums up the price of all items of a sales order. It is triggered whenever a new sales order is created.

The child entity defines one `on modify` determination:

- `TotalPrice_1` is the counterpart to `TotalPrice`. If a sales order is created without any items, then this determination ensures that the overall price of a sales order is calculated as soon as sales order items are added.

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

The determinations are implemented in the behavior pool`BP_DEMO_SALES_CDS_SO_2`, see `BP_DEMO_SALES_CDS_SO_2========CCIMP`.

``` abap
The class `CL_DEMO_CDS_DETERMINATION` accesses the business object using EML\. It creates two BO instances, providing only a value for the field `BuyerID` for each\. 
Code snippet:
```abap
MODIFY ENTITIES OF demo_sales_cds_so_2 
      ENTITY SalesOrder 
        CREATE FIELDS ( buyerid ) WITH VALUE #( 
           ( %cid = '1' BuyerId = `AAA` ) 
           ( %cid = '2' BuyerId = `BBB` ) ).
```

Result: The values for the fields `so_key`, `id`, `lifecycle_status`, and `amount_sum` are determined by the RAP framework. ![figure](images_abdoc_determination.png)

## Executable Example

The example above is explained in detail in the executable example [RAP BDL - determination](abenbdl_determination_abexa.md).
