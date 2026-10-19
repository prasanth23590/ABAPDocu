---
title: "RAP - reorder action"
source_file: abenbdl_reorder_action.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - instance hierarchy"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - reorder action

## Syntax

``` abap
 
[managed] reorder action 
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
[field ( hierarchy-index ) FieldName;] 
[ascending association _AscendingAssoc;] 
[descending association _DescendingAssoc [{ with cascading delete; }]]  
```

[`features: {instance | global}`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:update`](abenbdl_actions_auth_update.md) · [`authorization:global`](abenbdl_actions_auth_global.md) · [`authorization:instance`](abenbdl_actions_auth_instance.md) · [`lock:none`](abenbdl_lock_none.md)

### Addition

[1. `... field ( hierarchy-index ) FieldName;`](abenbdl_reorder_action.md#addition-1)

[2. `... ascending association _AscendingAssoc;`](abenbdl_reorder_action.md#addition-2)

[3. `... descending association _DescendingAssoc ...`](abenbdl_reorder_action.md#addition-3)

## Overview

### Description

The [reorder action](../../abap-glossary/abenrap_reorder_action_glosry.md) is a [RAP hierarchy action](../../abap-glossary/abenrap_hierarchy_action_glosry.md) that moves a [hierarchy node](../../abap-glossary/abenhierarchy_node_glosry.md) to a dedicated position among its siblings in an editable [treeview](../../abap-glossary/abenrap_treeview_glosry.md) by recalculating the hierarchy index fields of all sibling instances. The reorder action can be managed or unmanaged.

Reorder actions are specified within curly brackets after the syntax [`instance hierarchy`](abenbdl_instance_hierarchy.md). They are optional and can be specified in the context of an instance hierarchy only.

**Managed Reorder Action**

The managed reorder action is provided by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md). For the framework to be able to provide a standard implementation, the following must also be defined:

- A hierarchy index field `FieldName` must be specified. It contains information about the position of a hierarchy node within its sibling group. The field acts as an index to facilitate the ordering of its siblings, that is, the hierarchy nodes under the same parent node. It can have an integer data type or the data type `NUMC`.

- An ascending association `_AscendingAssoc` must be declared using the syntax `ascending association`. The ascending association is defined as a self-association to the parent node of the same CDS view entity in the underlying data model. The ascending association and the descending association together describe the self-referencing hierarchy in the data in the underlying CDS view entities.

- A descending association `_DescendingAssoc` must be declared using the syntax `descending association`. The descending association is defined as a self-association to the child node of the same CDS view entity in the underlying data model. It is the reverse association of the ascending association. The ascending association and the descending association together describe the self-referencing hierarchy in the data in the underlying CDS view entities.

Optionally, you can use the addition `with cascading delete` to specify that, if a hierarchy node is deleted, all its descendant nodes are deleted from the database, too.

**Unmanaged Reorder Action**

The unmanaged reorder action is implemented by the [unmanaged RAP BO provider](../../abap-glossary/abenunmanaged_rap_bo_prov_glosry.md) in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR MODIFY`](../abap-for-rap-business-objects/abaphandler_meth_modify.md).

**RAP BDL Operation Additions**

The following [RAP BDL operation additions](abenbdl_operations_additions.md) are possible:

- Dynamic feature control with [`(features:instance)`](abenbdl_actions_fc.md). This enables or disables the reorder action depending on preconditions within the business object.

- Global feature control with [`(features:global)`](abenbdl_actions_fc.md) enables or disables the reorder action depending on BO-external preconditions.

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

- In a [projection BO](../../abap-glossary/abenrap_projection_bo_glosry.md) and in a [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md), reorder actions from the base BDEF can be reused using the syntax `use action ActionName`. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

### Hints

- In [OData](../../abap-glossary/abenodata_glosry.md), the reorder action is called `ChangeNextSiblingAction`.

- A reorder action can be triggered using the EML statement [`MODIFY ENTITY ... EXECUTE`](../abap-for-rap-business-objects/abapmodify_entity_entities_op.md), just like other [RAP actions](../../abap-glossary/abenrap_action_glosry.md). It changes the value of the hierarchy index field.

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Editable Treeviews with Draft Capabilities](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/718e0f84564043afad76cf56e03e1528?version=sap_cross_product_abap).

## Addition

`... field ( hierarchy-index ) FieldName;`

### Description

Defines the field `FieldName` as hierarchy index field. It contains information about the position of a hierarchy node within its sibling group. It can have an integer data type or the data type `NUMC`. When executing the managed reorder action, the value of the hierarchy index field is recalculated for all sibling nodes.

For a managed reorder action, it is mandatory to define a hierarchy index field.

## Addition

`... ascending association _AscendingAssoc;`

### Description

Defines the association `_AscendingAssoc` as ascending association. The ascending association is defined as a self-association to the parent node of the same CDS view entity in the underlying data model. The ascending association and the descending association together describe the self-referencing hierarchy in the data in the underlying CDS view entities. For a managed reorder action, it is mandatory to define an ascending association.

## Addition 3

`... descending association _DescendingAssoc...`

### Description

Defines the association `_DescendingAssoc` as descending association. The descending association is defined as a self-association to the child node of the same CDS view entity in the underlying data model. The ascending association and the descending association together describe the self-referencing hierarchy in the data in the underlying CDS view entities. For a managed reorder action, it is mandatory to define a descending association.

Optionally, you can use `with cascading delete` to specify that, if a hierarchy node is deleted, all its descendant nodes are deleted from the database, too.
