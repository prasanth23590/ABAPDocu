---
title: "RAP - determine action"
source_file: abenbdl_determine_action.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - determine action

## Syntax

``` abap
[internal] determine action 
          [(authorization:none] 
           |[authorization:update] 
           |[authorization:global] 
           |[authorization:instance)] 
           DetermineActionName [external 'ExternalName'][extensible] 
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

[`internal`](abenbdl_internal.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:update`](abenbdl_actions_auth_update.md) · [`authorization:global`](abenbdl_actions_auth_global.md) · [`authorization:instance`](abenbdl_actions_auth_instance.md) · [`external`](abenbdl_external.md) · [`extensible`](abenbdl_extensibility_enabling_m_u.md) · [`determination`](abenbdl_determinations.md) · [`determination`](abenbdl_determinations.md) · [`validation`](abenbdl_validations.md) · [`validation`](abenbdl_validations.md) · [`determination`](abenbdl_determinations.md) · [`validation`](abenbdl_validations.md)

## Description

[Determine actions](../../abap-glossary/abenrap_bo_det_action_glosry.md) allow the [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) to execute [determinations](abenbdl_determinations.md) and [validations](abenbdl_validations.md) on request. Whenever a determine action is executed, the determinations and validations assigned to it are evaluated and then only those determinations and validations are executed whose trigger conditions are fulfilled.

A determine action can include on-save determinations and validations. On-modify determinations are not allowed. The determinations and validations are specified within curly brackets `{ }` and they are separated by semicolons (`;`). It is possible to specify a determine action without any determinations and validations. Determinations and validations of [child entities](../../abap-glossary/abenchild_entity_glosry.md) can be included using the syntax `child~childDetermination` or `child~childValidation`, as long as these validations and determinations do not include the trigger operation `delete`.

If the optional addition `always` is used, then all determinations and validations that are part of the determine action are executed regardless of their trigger conditions. After a determination with the flag `always` has been executed, it can be triggered again by other determinations belonging to the same determine action.

Execution order: Determinations are executed first, validations afterwards. The execution order among determinations or validations themselves is defined by the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) and is independent of the specified order within the determine action.

The following [RAP BDL operation additions](abenbdl_operations_additions.md) are possible:

- [`internal`](abenbdl_internal.md) to make the respective determine action accessible only from within the business object implementation.

- [`authorization:none`](abenbdl_actions_auth.md) excludes the operation in question from [authorization checks](abenbdl_authorization.md).

- [`authorization:update`](abenbdl_actions_auth_update.md) delegates the [authorization control](abenbdl_authorization.md) to the authorization check that is implemented for the update operation.

- [`authorization:global`](abenbdl_actions_auth_global.md) replaces the [authorization control](abenbdl_authorization.md) that is specified in the [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) and applies global authorization checks instead.

- [`authorization:instance`](abenbdl_actions_auth_instance.md) replaces the [authorization control](abenbdl_authorization.md) that is specified in the [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) and applies instance authorization checks instead.

- An external name can be defined for a determine action on base level, as well as on interface- and projection level of the [behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) using the addition [external](abenbdl_external.md). The external name `ExternalName` is specified in single quotes(').

- A determine action can be declared as extensible using the addition [`extensible`](abenbdl_extensible.md). This makes it possible to add validations or determinations to the determine action in question via a [BDEF extension](../../abap-glossary/abenrap_extension_glosry.md).

  **Note:** A determine action can be declared as `extensible` only if the following prerequisites are met: The RAP BO must allow for extensions and the RAP BO must be [draft-enabled](../../abap-glossary/abendraft_rap_bo_glosry.md). For further details on extensibility enabling, see the topic [RAP - Extensibility Enabling for Base BOs](abenbdl_extensibility_enabling_m_u.md).

## Availability

- [Managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md): In a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md), determine actions do not require an implementation in the [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md), but the determinations and validations included in a determine action must be implemented.

- [Unmanaged](../../abap-glossary/abenunmanaged_rap_bo_glosry.md) and [draft-enabled](../../abap-glossary/abendraft_rap_bo_glosry.md) RAP BOs: In an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), determine actions require an implementation in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR MODIFY ... ACTION`](../abap-for-rap-business-objects/abaphandler_meth_modify.md) in the ABAP behavior pool.

  Not available for unmanaged, non-draft RAP BOs.

- In a [projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md), determine actions from the base BDEF can be reused using the syntax [`use action`](abenbdl_use_projection.md). For details on reuse, see the topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

- In a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), determine actions from the base BDEF can be reused using the syntax [`use action`](abenbdl_use_projection.md). For details on reuse, see the topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

## Hint

The [draft determine action](abenbdl_draft_action.md) `Prepare` is the draft pendant to determine actions. It is documented in topic [RAP BDL - draft actions](abenbdl_draft_action.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, topic [Action Definition](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/14ddc6b2442b4b97842af9158a1c9c44?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed BDEF based on the on the CDS root view entity `DEMO_SALES_CDS_SO_3`. The root view entity represents a sales order and the child entity represents a sales order item. The determine action `trigger_all` includes the following two determinations, one from in the root entity and one from the child entity:

- `setID` assigns values to the semantic key field `SalesOrderId` during the [save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) whenever a new entity instance is created.

- `TotalPrice` sums up the price of all items of a sales order. It is triggered whenever a new sales order is created.

``` abap
managed implementation in class bp_demo_sales_cds_so_3 unique;
strict ( 2 );

define behavior for DEMO_SALES_CDS_SO_3 alias SalesOrder
persistent table demo_sales_order
lock master
authorization master ( none )
{
  create;
  update;
  association _SalesOrderItem { create; }
  field ( readonly : update ) SoKey;

  determination setID on save { create; }

  determine action trigger_all
  {
    determination ( always ) setID;
    determination ( always ) SalesOrderItem~TotalPrice;
  }

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

define behavior for DEMO_SALES_CDS_SO_I_3 alias SalesOrderItem
persistent table demo_sales_so_i
lock dependent by _SalesOrder
authorization dependent by _SalesOrder
{
  update;
  delete;

  field ( readonly : update ) ParentKey;

  determination TotalPrice on save { create; }

  association _SalesOrder { }
  field ( readonly : update ) SoItemKey;

  mapping for demo_sales_so_i corresponding
    {
      SoItemKey   = so_item_key;
      ParentKey   = parent_key;
      GrossAmount = gross_amount;
    }
}
```

The determinations are implemented in the behavior pool `BP_DEMO_SALES_CDS_SO_3`.

The class `CL_DEMO_CDS_DETERMINE_ACTION` accesses the business object using [EML](../../abap-glossary/abeneml_glosry.md) and carries out the following steps:

- It first inserts data into the BO's [persistent database tables](../../abap-glossary/abenrap_persistent_table_glosry.md) using [ABAP SQL](../../abap-glossary/abenabap_sql_glosry.md). That means that BO entity instances are available in the database, but the determinations haven't yet been triggered.

- The determine action `trigger_all` is executed with the statement `MODIFY ENTITIES` for two entity instances. For these two entity instances, the fields `ID` and `TotalPrice` are determined.

  Code snippet:

``` abap
MODIFY ENTITIES OF demo_sales_cds_so_3 
       ENTITY SalesOrder 
       EXECUTE trigger_all 
       FROM VALUE #( ( sokey = '0894EF1643A01EDB90EE45FBFB0C7DAA' ) 
                     ( sokey = '0894EF1643A01EDB90EE45FBFB0C9DAA'   ) ) 
       MAPPED FINAL(mapped) 
       FAILED FINAL(failed) 
       REPORTED FINAL(reported). 
 
    COMMIT ENTITIES.
```

- The determined values are committed to the database with the statement `COMMIT ENTITIES`.

Result: values for the fields `ID` and `TotalPrice` are determined. ![figure](images_abdoc_det_action.png)
