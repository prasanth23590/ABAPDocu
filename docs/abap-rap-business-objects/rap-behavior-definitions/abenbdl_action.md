---
title: "RAP - action"
source_file: abenbdl_action.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Non-Standard Operations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - action

## Syntax Forms

**[Non-Factory Actions](abenbdl_action_nonfactory.md)**

``` abap
1. [internal][static] [repeatable] action 
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
                  [OutputParameter]; 
                  [{default function GetDefaultsForActName [external 'GetDefaultsForExtName'];}]
```

**[Factory Actions](abenbdl_action_factory.md)**

``` abap
2. [internal][static [default]] factory action 
                  [( 
                  [features: {instance | global}] 
                  [precheck] 
                  [authorization:none] 
                  [authorization:update] 
                  [authorization:global] 
                  [authorization:instance] 
                  [lock:none] 
                   )] 
                   ActionName [ external 'ExternalName'] 
                  [InputParameter] 
                   [cardinality]; 
                   [{default function GetDefaultsForActName [external 'GetDefaultsForExtName'];}]
```

**[Save Actions](abenbdl_action_onsave.md)**

``` abap
3. [internal][static][factory] 
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

[`internal`](abenbdl_internal.md) · [`static`](abenbdl_static.md) · [`repeatable`](abenbdl_action_repeatable.md) · [`features: {instance | global}`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:update`](abenbdl_actions_auth_update.md) · [`authorization:global`](abenbdl_actions_auth_global.md) · [`authorization:instance`](abenbdl_actions_auth_instance.md) · [`lock:none`](abenbdl_lock_none.md) · [`InputParameter`](abenbdl_action_input_param.md) · [`OutputParameter`](abenbdl_action_output_para.md) · [`{default function GetDefaultsForActName [external 'GetDefaultsForExtName'];}`](abenbdl_default_function.md) · [`internal`](abenbdl_internal.md) · [`static`](abenbdl_static.md) · [`default`](abenbdl_action_default_factory.md) · [`features: {instance | global}`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:update`](abenbdl_actions_auth_update.md) · [`authorization:global`](abenbdl_actions_auth_global.md) · [`authorization:instance`](abenbdl_actions_auth_instance.md) · [`lock:none`](abenbdl_lock_none.md) · [`InputParameter`](abenbdl_action_input_param.md) · [`{default function GetDefaultsForActName [external 'GetDefaultsForExtName'];}]`](abenbdl_default_function.html) · [`internal`](abenbdl_internal.md) · [`static`](abenbdl_static.md) · [`features: global`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:global`](abenbdl_actions_auth_global.md) · [`authorization:instance`](abenbdl_actions_auth_instance.md) · [`InputParameter`](abenbdl_action_input_param.md) · [`OutputParameter`](abenbdl_action_output_para.md) · [`{default function GetDefaultsForActName [external 'GetDefaultsForExtName'];}]`](abenbdl_default_function.html)

## Description

[RAP actions](../../abap-glossary/abenrap_action_glosry.md) are [non-standard RAP BO operations](../../abap-glossary/abenrap_nstandard_operation_glosry.md) that modify the state of an [entity instance](../../abap-glossary/abenrap_bo_instance_glosry.md). The custom logic must be implemented in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR MODIFY`](../abap-for-rap-business-objects/abaphandler_meth_modify.md).

The following kinds of actions are available:

- [Non-factory actions](abenbdl_action_nonfactory.md)

  - [Non-factory actions](../../abap-glossary/abenrap_factory_action_glosry.md) implement custom logic that changes existing entity instances.

  - Instance-bound non-factory actions can be declared as [repeatable](abenbdl_action_repeatable.md). A [repeatable action](../../abap-glossary/abenrap_repeatable_action_glosry.md) can be executed multiple times on the same [RAP BO entity instance](../../abap-glossary/abenrap_bo_entity_inst_glosry.md) in the same [ABAP EML](../../abap-glossary/abenabap_eml_glosry.md) or [OData](../../abap-glossary/abenodata_glosry.md) request.

- [Factory actions](abenbdl_action_factory.md)

  - [Factory actions](../../abap-glossary/abenrap_factory_action_glosry.md) can be used to create RAP BO entity instances.

  - A [default factory action](abenbdl_action_default_factory.md) is a special kind of factory action.

- [Save actions](abenbdl_action_onsave.md)

  - [RAP save actions](../../abap-glossary/abenrap_save_action_glosry.md) can be non-factory actions or factory actions. RAP save actions are characterized by the syntax addition `save`, which has the effect that the action in question can only be executed during the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md). Any attempt to execute a RAP save action during the [RAP interaction phase](../../abap-glossary/abenrap_int_phase_glosry.md) results in a [short dump](../../abap-glossary/abenshort_dump_glosry.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section about [Actions](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/83bad707a5a241a2ae93953d81d17a6b?version=sap_cross_product_abap).
