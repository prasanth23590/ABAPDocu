---
title: "RAP - action, Non-Factory"
source_file: abenbdl_action_nonfactory.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Non-Standard Operations > RAP - action"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - action, Non-Factory

## Syntax

``` abap
[internal][static] [repeatable] action 
                  [( 
                  [features: {instance | global}] 
                  [precheck] 
                  [authorization:none] 
                  [authorization:update] 
                  [authorization:global] 
                  [authorization:instance] 
                  [lock:none] 
                   )] 
                   ActionName [external 'ExternalName'] 
                  [InputParameter] 
                  [OutputParameter] 
                  [{default function GetDefaultsForActName [external 'GetDefaultsForExtName'];}]  
```

[`internal`](abenbdl_internal.md) · [`static`](abenbdl_static.md) · [`repeatable`](abenbdl_action_repeatable.md) · [`features: {instance | global}`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:update`](abenbdl_actions_auth_update.md) · [`authorization:global`](abenbdl_actions_auth_global.md) · [`authorization:instance`](abenbdl_actions_auth_instance.md) · [`lock:none`](abenbdl_lock_none.md) · [`external`](abenbdl_external.md) · [`InputParameter`](abenbdl_action_input_param.md) · [`OutputParameter`](abenbdl_action_output_para.md) · [`{default function GetDefaultsForActName`](abenbdl_default_function.md) · [`external 'GetDefaultsForExtName'];}`](abenbdl_external.html)

## Description

Defines a [RAP action](../../abap-glossary/abenrap_action_glosry.md) which offers non-standard behavior. The custom logic must be implemented in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR MODIFY`](../abap-for-rap-business-objects/abaphandler_meth_modify.md). An action per default relates to a [RAP BO entity instance](../../abap-glossary/abenrap_bo_entity_inst_glosry.md) and changes the state of the instance.

If the optional keyword [`static`](abenbdl_static.md) is used, the action is defined as [static action](../../abap-glossary/abenrap_static_operation_glosry.md). Static actions are not bound to any instance of a [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md) but relate to the complete entity. The default is that an action is related to an [instance](../../abap-glossary/abenrap_instance_operation_glosry.md), so the keyword `static` overwrites the default.

The optional addition [`repeatable`](abenbdl_action_repeatable.md) declares a non-factory, instance-bound action as [RAP repeatable action](../../abap-glossary/abenrap_repeatable_action_glosry.md). A repeatable action can be executed multiple times on the same [RAP BO entity instance](../../abap-glossary/abenrap_bo_entity_inst_glosry.md) within the same [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) or [OData](../../abap-glossary/abenodata_glosry.md) request. A RAP action without the addition `repeatable` must not be executed multiple times on the same entity instance within the same request. Otherwise, a runtime error occurs. For further details, see topic [RAP - `repeatable`](abenbdl_action_repeatable.md).

The following [RAP BDL operation additions](abenbdl_operations_additions.md) are possible:

- [`internal`](abenbdl_internal.md) to make the respective action accessible only from within the business object implementation.

- [`external`](abenbdl_external.md) to provide an alias name for external usage.

- [`lock:none`](abenbdl_lock_none.md) to prevent the [RAP locking](../../abap-glossary/abenrap_locking_glosry.md) mechanism for the entity instance for which the action is executed.

- Dynamic feature control with [`(features:instance)`](abenbdl_actions_fc.md). This enables or disables the action depending on preconditions within the business object. For example, the action `Accept_Order` might be offered only if the status is not *Rejected* already.

- Global feature control with [`(features:global)`](abenbdl_actions_fc.md) enables or disables the action depending on BO-external preconditions.

- [`precheck`](abenbdl_precheck.md) prevents unwanted changes from reaching the application buffer.

- [`authorization:none`](abenbdl_actions_auth.md) excludes the operation in question from [authorization checks](abenbdl_authorization.md).

  **Note:** For static actions, the addition `authorization:none` is available only in case of global authorization.

- [`authorization:update`](abenbdl_actions_auth_update.md) delegates the [authorization control](abenbdl_authorization.md) to the authorization check that is implemented for the update operation.

- [`authorization:global`](abenbdl_actions_auth_global.md) replaces the [authorization control](abenbdl_authorization.md) that is specified in the [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) and applies global authorization checks instead.

- [`authorization:instance`](abenbdl_actions_auth_instance.md) replaces the [authorization control](abenbdl_authorization.md) that is specified in the [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) and applies instance authorization checks instead.

- Input parameters [`InputParameter`](abenbdl_action_input_param.md) and output parameters [`OutputParameter`](abenbdl_action_output_para.md) can optionally be added to the action signature.

- [`{default function ... }`](abenbdl_default_function.md) defines a [RAP default values function](../../abap-glossary/abenrap_bo_defaulting_glosry.md) for the action in question. It is an optional addition that can be used to default values for the input parameter of the action. As a prerequisite, the action must specify an input parameter.

## Availability

- [Managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- In a [projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md), actions from the base BDEF can be reused. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md). It is also possible to specify new actions as described in topic [RAP BDL - actions and functions, projection BDEF](abenbdl_nonstandard_projection.md).

- In a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), actions from the base BDEF can be reused. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section about [Actions](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/83bad707a5a241a2ae93953d81d17a6b?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a managed [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md) based on the CDS root view entity `DEMO_CDS_PURCH_DOC_M`. The business object represents a purchase order with purchase order items. If an employee wants to order equipment, the manager can approve or reject this purchase. Therefore, the two actions `Approve_Order` and `Reject_Order` are defined.

``` abap
managed implementation in class bp_demo_cds_purch_doc_m unique;
strict(2);

define behavior for DEMO_CDS_PURCH_DOC_M alias PurchaseDocument
persistent table demo_purch_doc
lock master
etag master crea_date_time
authorization master (none)
{
  create;
  update;
  delete;
  association _PurchaseDocumentItem { create; }

  action Approve_Order result [1] $self;
  action Reject_Order  result [1] $self;

  field(readonly:update) PurchaseDocument;

  field ( readonly )  crea_uname , crea_date_time;

  mapping for demo_purch_doc corresponding;
}

define behavior for DEMO_CDS_PURCH_DOC_I_M alias PurchaseDocumentItem
persistent table DEMO_PURCH_DOC_I
lock dependent by _PurchaseDocument
authorization dependent by _PurchaseDocument
{
  update;
  delete;
  field ( readonly )  PurchaseDocumentItem , PurchaseDocument;
  field ( mandatory ) Price , Quantity , QuantityUnit;

  association _PurchaseDocument;

  mapping for DEMO_PURCH_DOC_I corresponding;
}
```

The actions are implemented in behavior pool `BP_DEMO_CDS_PURCH_DOC_M`. The class `CL_DEMO_CDS_PURCHASE` accesses the business object using [EML](../../abap-glossary/abeneml_glosry.md) and performs the `Approve_Order` action on one entity instance.

Result: column *Status* of the respective instance is filled with `A` for *Accepted*. ![figure](images_abdoc_action.png)

## Executable Example

The example above is explained in detail in the executable example [RAP BDL - action](abenbdl_action1_abexa.md).
