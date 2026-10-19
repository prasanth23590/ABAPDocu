---
title: "RAP - Standard Operations"
source_file: abenbdl_standard_operations.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Standard Operations

## Syntax

``` abap
... [internal] create [([features:global] 
                      [,precheck] 
                      [,authorization:none]);] 
                      [{default function [GetDefaultsForCreate];}] 
  | [internal] update [({features:instance | features:global} 
                      [,precheck] 
                      [,authorization:none])]; 
  | [internal] delete [({features:instance | features:global} 
                      [,precheck] 
                      [,authorization:none] 
                      [,authorization:update])];  
```

[`internal`](abenbdl_internal.md) · [`([features:global]`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`{default function [GetDefaultsForCreate];}`](abenbdl_default_function.md) · [`internal`](abenbdl_internal.md) · [`({features:instance | features:global`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`internal`](abenbdl_internal.md) · [`({features:instance | features:global`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:update`](abenbdl_actions_auth_update.md)

## Description

[Create](../../abap-glossary/abenrap_create_operation_glosry.md), [update](../../abap-glossary/abenrap_update_operation_glosry.md), and [delete](../../abap-glossary/abenrap_delete_operation_glosry.md) are standard operations. They are also known as [CUD operations](../../abap-glossary/abencud_glosry.md), which is an acronym for create, read, update, delete. The [read operation](../../abap-glossary/abenrap_read_operation_glosry.md) is always implicitly enabled for each entity listed in a [RAP behavior definition (BDEF)](../../abap-glossary/abencds_behavior_definition_glosry.md) and it mustn't be declared explicitly.

- `create` is a modifying operation that creates new [instances](../../abap-glossary/abenrap_bo_entity_inst_glosry.md) of a [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md).

  - In a managed RAP BO, `create` can only be declared for [root nodes](../../abap-glossary/abenroot_node_glosry.md). Child nodes are implicitly create-enabled for [internal usage](abenbdl_internal.md). That means, an external consumer can only create a new instance of a child entity via its parent, see [create-by-association](abenbdl_association.md) operation. A direct create can only take place from the BO's own implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md).

  - In an unmanaged RAP BO, direct creates on child entities are possible but not recommended.

- `update` is a modifying operation that changes one or more instances of a business object entity.

- `delete` is a modifying operation that deletes one or more instances of a business object entity.

  **Note:** In a managed RAP BO, if a parent entity instance is deleted, all child entity instances that belong to the parent entity instance in question are deleted automatically. In an unmanaged RAP BO, it is recommended that you implement the delete operation in this way as well.

`create`, `update`, and `delete` are optional components of a BDEF. If, for example, `update` is defined for an entity, then it is allowed to update this entity. If `update` is not defined, then a [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) is not allowed to perform update calls.

The following [RAP BDL operation additions](abenbdl_operations_additions.md) are possible:

- [`internal`](abenbdl_internal.md): `create`, `update`, and `delete` can be defined as internal operations.

- [`(features:instance)`](abenbdl_actions_fc.md): Dynamic feature control can be specified for `update` or `delete`, but not for `create`.

- [`(features:global)`](abenbdl_actions_fc.md): Global feature control can be specified for `create`, `update`, or `delete`.

- [`precheck`](abenbdl_precheck.md): A [RAP BO precheck](../../abap-glossary/abenrap_bo_precheck_glosry.md) can be specified for `create`, `update`, or `delete`.

- [`authorization:none`](abenbdl_actions_auth.md): Excludes the operation in question from [authorization checks](abenbdl_authorization.md).

- [`authorization:update`](abenbdl_actions_auth_update.md)

  \- Delegates the [authorization control](abenbdl_authorization.md) for the authorization in question to the authorization check that is implemented for the update operation. - Only available for `delete`.

- [`{default function [GetDefaultsForCreate];}`](abenbdl_default_function.md)

  \- Defines a [RAP default values function](../../abap-glossary/abenrap_bo_defaulting_glosry.md) for the operation in question. The effect is that field values are defaulted on the user interface. - Only available for `create`.

## Availability

- Managed RAP BO

  In a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md), the CRUD operations do not require an [ABAP behavior pool (ABP)](../../abap-glossary/abenbehavior_pool_glosry.md), since they are completely handled by the managed RAP BO provider. (However, some of the optional additions do require implementation. This is documented in the respective topics.)

- Unmanaged RAP BO

  In an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), each standard operation must be implemented in the ABAP behavior pool in the [RAP handler method](../abap-for-rap-business-objects/abapmethods_for_rap_behv.md) [`FOR MODIFY`](../abap-for-rap-business-objects/abaphandler_meth_modify.md).

- Projection BO and RAP BO Interface

  In a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md) and in a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), the standard operations can be reused from the [base BDEF](../../abap-glossary/abenrap_base_bdef_glosry.md). This can be done using the keyword `use`. For further details, see topic [RAP BDL - use, projection BDEF](abenbdl_use_projection.md).

## Hint

For create operations, the optional addition [`AUTO FILL CID`](../abap-for-rap-business-objects/abapmodify_entity_entities_fields.md) can be used to automatically fill the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) component [`%cid`](../abap-for-rap-business-objects/abapderived_types_cid.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, section about [Standard Operations](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/9a701fe447e74e798db0f2a4ef10bc04?version=sap_cross_product_abap).

## Executable Example

[ABAP EML - `MODIFY`, Standard Operations (Managed)](../abap-for-rap-business-objects/abeneml_modify_op_abexa.md)

## Executable Example

[ABAP EML - `MODIFY`, Standard Operations (Unmanaged)](../abap-for-rap-business-objects/abeneml_modify_op_u_abexa.md)
