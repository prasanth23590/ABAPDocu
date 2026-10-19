---
title: "RAP - save action"
source_file: abenbdl_action_onsave.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Non-Standard Operations > RAP - action"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - save action

## Syntax

``` abap
[internal][static][factory] 
  save(finalize|adjustnumbers|finalize, adjustnumbers) action 
                  [( 
                  [features: global] 
                  [precheck] 
                  [authorization:none] 
                  [authorization:global] 
                  [authorization:instance] 
                   )] 
                   ActionName [external 'ExternalName'] 
                  [InputParameter] 
                  [OutputParameter]; 
                  [{default function GetDefaultsForActName [external 'GetDefaultsForExtName'];}]  
```

[`internal`](abenbdl_internal.md) · [`static`](abenbdl_static.md) · [`features: global`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:global`](abenbdl_actions_auth_global.md) · [`authorization:instance`](abenbdl_actions_auth_instance.md) · [`InputParameter`](abenbdl_action_input_param.md) · [`OutputParameter`](abenbdl_action_output_para.md) · [`{default function GetDefaultsForActName [external 'GetDefaultsForExtName'];}`](abenbdl_default_function.md)

## Description

Defines a [RAP save action](../../abap-glossary/abenrap_save_action_glosry.md). RAP save actions are [RAP actions](../../abap-glossary/abenrap_action_glosry.md) that can only be called during a specified [RAP saver method](../../abap-glossary/abenabp_saver_method_glosry.md) in the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md). Any call during the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md) leads to a [short dump](../../abap-glossary/abenshort_dump_glosry.md).

Save actions are characterized by the syntax addition `save`. The name of the [RAP saver method](../../abap-glossary/abenabp_saver_method_glosry.md) during which the action can be executed is specified in brackets. `finalize`, `adjustnumbers`, or both can be specified in brackets to indicate the saver method during which the action can be called.

[Non-factory actions](abenbdl_action_nonfactory.md) and [factory actions](abenbdl_action_factory.md) (instance-bound and static) can be defined as save action. A default factory action, however, cannot be a save action. The respective syntax rules of the kind of action apply (non-factory, static factory, instance-bound factory).

The following [RAP BDL operation additions](abenbdl_operations_additions.md) are allowed for save actions:

- [`internal`](abenbdl_internal.md) to make the respective action accessible only from within the business object implementation.

- Global feature control with [`(features:global)`](abenbdl_actions_fc.md) enables or disables the action depending on BO-external preconditions.

- [`precheck`](abenbdl_precheck.md) prevents unwanted changes from reaching the application buffer.

- [`authorization:none`](abenbdl_actions_auth.md) excludes the operation in question from [authorization checks](abenbdl_authorization.md).

- [`authorization:global`](abenbdl_actions_auth_global.md) replaces the [authorization control](abenbdl_authorization.md) that is specified in the [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) and applies global authorization checks instead.

- [`authorization:instance`](abenbdl_actions_auth_instance.md) replaces the [authorization control](abenbdl_authorization.md) that is specified in the [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) and applies instance authorization checks instead.

- Input parameters [`InputParameter`](abenbdl_action_input_param.md) and output parameters [`OutputParameter`](abenbdl_action_output_para.md) can optionally be added to the action signature.

- [`default function`](abenbdl_default_function.md) defines a [RAP default values function](../../abap-glossary/abenrap_bo_defaulting_glosry.md) for the action in question. It is an optional addition that can be used to default values for the input parameter of the action. As a prerequisite, the action must specify an input parameter.

**Calling RAP Save Actions**

A RAP save action can be called in the following contexts:

- From an external [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md).

- In the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md), from a [`finalize`](../abap-for-rap-business-objects/abensaver_finalize.md) or [`adjust_numbers`](../abap-for-rap-business-objects/abensaver_adjust_numbers.md) RAP saver method, according to the specification in brackets.

- A `save(finalize)` action can be called from the implementation of a [RAP determination](../../abap-glossary/abenrap_determination_glosry.md) `on save`.

  **Note:** This does not apply to `save(adjustnumbers)` actions. `save(adjustnumbers)` actions must not be called in determinations `on save`. Any attempt to do so results in a short dump. If a determination `on save` is executed as part of a [RAP BO determine action](../../abap-glossary/abenrap_bo_det_action_glosry.md), the execution takes place during the interaction phase. Therefore, if a RAP save action is called in a determination `on save` and the determination is executed as part of a determine action, a short dump occurs.

RAP save actions must not be called in the following contexts:

- A RAP saver method other than the one specified in brackets. For example, a `save(finalize)` action must not be called during the RAP saver method `adjust_numbers`. Any attempt to do so leads to a syntax check error.

- In the implementation of a [RAP determination](../../abap-glossary/abenrap_determination_glosry.md) `on modify`. If this is done, a short dump occurs.

- If called from the implementation of any other [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md), a short dump occurs.

  **Note:** Save actions cannot be called from other save actions of the same saver method. For example, a `save(adjustnumber)` cannot call another `save(adjustnumber)` action. Any attempt to do so results in a short dump.

## Availability

- [Managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- In a [projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md), save actions from the base BDEF can be reused. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

- In a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), save actions from the base BDEF can be reused. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

## Hints

- Save actions without a RAP saver method specification are obsolete. The following syntax is not valid: `save action MySaveAction`. Existing save actions that do not specify a RAP saver method in brackets are automatically interpreted as `save(finalize)`.

- RAP save actions are required for the RAP representation of certain existing functionality which does not maintain a [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md) but (from a RAP perspective) only has a save phase.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section about [Actions](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/83bad707a5a241a2ae93953d81d17a6b?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows an unmanaged BDEF with four save actions.

**Note:** This example is intentionally kept short and simple and focuses on specific RAP aspects. It does not fully meet the requirements of the [RAP BO contract](../../abap-glossary/abenrap_bo_contract_glosry.md).

``` abap
unmanaged implementation in class bp_demo_rap_save_action_u unique;
strict ( 2 );

define behavior for DEMO_RAP_SAVE_ACTION_U alias Root
late numbering
lock master
authorization master ( none )
{
  create;
  update;
  delete;

  field ( readonly ) key_field;

  save ( finalize ) action A1;
  static save ( adjustnumbers ) action A2;
  factory save ( finalize, adjustnumbers ) action A3 [1];
  static factory save ( finalize, adjustnumbers ) action A4 [1];
}
```

The save actions are implemented in behavior pool `BP_DEMO_RAP_SAVE_ACTION_U`.

The following calls are valid:

- The `save(finalize) action A1` can be called from an external EML consumer as demonstrated in the following code snippet:

``` abap
    MODIFY ENTITIES OF DEMO_RAP_SAVE_ACTION_U 
      ENTITY Root 
      EXECUTE A1 
      FROM VALUE #( ( %key-key_field = 1 ) ). 
    COMMIT ENTITIES.
```

- The `save(finalize) action A1` can be called from the implementation of a determination `on save` from another RAP BO, namely, `DEMO_RAP_SAVE_ACTION_M`.

``` abap
METHOD det_on_save. 
  MODIFY ENTITIES OF demo_rap_save_action_u 
    ENTITY Root 
    EXECUTE a1 
    FROM VALUE #( ( %key-key_field = 1 ) ) 
    FAILED DATA(failed). 
ENDMETHOD.
```
