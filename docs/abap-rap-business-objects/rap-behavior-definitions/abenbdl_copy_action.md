---
title: "RAP - copy action"
source_file: abenbdl_copy_action.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - instance hierarchy"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - copy action

## Syntax

``` abap
copy action 
 [( 
   [features: {instance | global}] 
   [precheck] 
   [authorization:none] 
   [authorization:update] 
   [authorization:global] 
   [authorization:instance] 
   [lock:none] 
  )] 
  ActionName [external 'ExternalName'];  
```

[`features: {instance | global}`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:update`](abenbdl_actions_auth_update.md) · [`authorization:global`](abenbdl_actions_auth_global.md) · [`authorization:instance`](abenbdl_actions_auth_instance.md) · [`lock:none`](abenbdl_lock_none.md)

## Description

The copy action is a &#x202F;[RAP hierarchy action](../../abap-glossary/abenrap_hierarchy_action_glosry.md) that determines how a [hierarchy node](../../abap-glossary/abenhierarchy_node_glosry.md) can be duplicated in an editable scenario. It is useful for creating new hierarchy nodes based on an existing one in an editable [treeview scenarios](../../abap-glossary/abenrap_treeview_glosry.md).

Copy actions are specified within curly brackets after the syntax [`instance hierarchy`](abenbdl_instance_hierarchy.md). They are optional and can be specified in the context of an instance hierarchy only.

Copy actions are instance-bound [factory actions](../../abap-glossary/abenrap_factory_action_glosry.md), i.e. they offer [`%cid`](../abap-for-rap-business-objects/abapderived_types_cid.md)&#x202F; handling for the result instance. Copy actions are implemented by the [unmanaged RAP BO provider](../../abap-glossary/abenunmanaged_rap_bo_prov_glosry.md) in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR MODIFY`](../abap-for-rap-business-objects/abaphandler_meth_modify.md). They are user-implemented.

The following [RAP BDL operation additions](abenbdl_operations_additions.md) are possible:

- Dynamic feature control with [`(features:instance)`](abenbdl_actions_fc.md). This enables or disables the copy action depending on preconditions within the business object.

- Global feature control with [`(features:global)`](abenbdl_actions_fc.md) enables or disables the copy action depending on BO-external preconditions.

- [`precheck`](abenbdl_precheck.md) prevents unwanted changes from reaching the application buffer.

- [`authorization:none`](abenbdl_actions_auth.md) excludes the operation in question from [authorization checks](abenbdl_authorization.md).

- [`authorization:update`](abenbdl_actions_auth_update.md) delegates the [authorization control](abenbdl_authorization.md) to the authorization check that is implemented for the update operation.

- [`authorization:global`](abenbdl_actions_auth_global.md) replaces the [authorization control](abenbdl_authorization.md) that is specified in the [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) and applies global authorization checks instead.

- [`authorization:instance`](abenbdl_actions_auth_instance.md) replaces the [authorization control](abenbdl_authorization.md) that is specified in the [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) and applies instance authorization checks instead.

- [`lock:none`](abenbdl_lock_none.md) to prevent the [RAP locking](../../abap-glossary/abenrap_locking_glosry.md) mechanism for the entity instance for which the action is executed.

- [`external`](abenbdl_external.md): Optional addition to provide an alias name for external usage.

**Note:** If multiple RAP BO operation additions are used, they are separated by a comma.

## Availability

- [Managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- In a [projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md) and in a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), copy actions from the base BDEF can be reused using the syntax `use action ActionName`. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).
