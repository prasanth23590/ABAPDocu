---
title: "RAP - StandardOperationsForAssoc"
source_file: abenbdl_assoc_stand_ops.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - Operations for Associations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - StandardOperationsForAssoc

## Syntax

``` abap
...       {[ [internal] create 
              [{(features:instance | features:global}] 
              [,precheck] 
              [,authorization:none] 
              [,authorization:update] 
              [,authorization:global] 
              [,authorization:instance]); 
              [{default function GetDefaultsFor_Assoc [external 'GetDefaultsForCBA'];}] 
               ]}  
```

[`internal`](abenbdl_internal.md) · [`features:instance`](abenbdl_actions_fc.md) · [`features:global`](abenbdl_actions_fc.md) · [`precheck`](abenbdl_precheck.md) · [`authorization:none`](abenbdl_actions_auth.md) · [`authorization:update`](abenbdl_actions_auth_update.md) · [`authorization:global`](abenbdl_actions_auth_global.md) · [`authorization:instance`](abenbdl_actions_auth_instance.md) · [`{default function GetDefaultsFor_Assoc [external 'GetDefaultsForCBA'];}`](abenbdl_default_function.md)

## Description

A [standard operation for associations](../../abap-glossary/abenrap_standard_op_assoc_glosry.md) provides canonical behavior along an [association path](../../abap-glossary/abencds_association_path_glosry.md) from an [association source](../../abap-glossary/abenassociation_source_glosry.md) to an [association target](../../abap-glossary/abenassociation_target_glosry.md). [Create-by-association](../../abap-glossary/abenrap_cba_operation_glosry.md) and [read-by-association](../../abap-glossary/abenrap_rba_operation_glosry.md) are [standard operations for associations](../../abap-glossary/abenrap_standard_op_assoc_glosry.md).

**Read by association**

The declaration of an [association](../../abap-glossary/abencds_association_glosry.md) in the BDEF enables the standard operation [read-by-association](../../abap-glossary/abenrap_rba_operation_glosry.md), as described in [Operations for Associations](abenbdl_association.md).

**Create by association**

The addition `create` enables [create-by-association operations](../../abap-glossary/abenrap_cba_operation_glosry.md) for [associations](../../abap-glossary/abencds_association_glosry.md):

- [Create-by-association](../../abap-glossary/abenrap_cba_operation_glosry.md) allows RAP BO consumers creating new instances of the association target entity.

The following rules apply:

- The create-by-association operations can be defined for [intra BO associations](../../abap-glossary/abencds_intra_bo_assoc_glosry.md) and for [cross-BO associations](../../abap-glossary/abencds_cross_bo_assoc_glosry.md).

- The association target entity must be behavior enabled, in other words, the association target entity must have its own behavior definition.

- For intra-BO associations, create-by-association is only available for to-child associations. It is not allowed for to-parent associations. In other words, [child nodes](../../abap-glossary/abenchild_entity_glosry.md) can be created via their [parent node](../../abap-glossary/abenparent_entity_glosry.md), but parents cannot be created via their child nodes.

The syntax for enabling create access to an association target entity is as follows:

`association _Assoc { create; }`

**RAP BDL Operation Additions**

The following [RAP BDL operation additions](abenbdl_operations_additions.md) are possible:

- [`internal`](abenbdl_internal.md): The create-by-association operation can only be accessed internally.

- [`features:instance`](abenbdl_actions_fc.md): Enables dynamic feature control for the association in question.

- [`features:global`](abenbdl_actions_fc.md): Enables global feature control for the association in question.

- [`precheck`](abenbdl_precheck.md): Prevents illegal changes from reaching the application buffer by prechecking [modify operations](../../abap-glossary/abenrap_modify_operation_glosry.md).

- [`authorization:none`](abenbdl_actions_auth.md): Excludes the association in question from [authorization checks](abenbdl_authorization.md).

- [`authorization:update`](abenbdl_actions_auth_update.md): Delegates the [authorization control](abenbdl_authorization.md) to the authorization check that is implemented for the update operation.

- [`authorization:global`](abenbdl_actions_auth_global.md): Enables global authorization for the create-by-association in question.

- [`authorization:instance`](abenbdl_actions_auth_instance.md): Enables instance authorization for the create-by-association in question.

- [`{default function GetDefaultsFor_Assoc [external 'GetDefaultsForCBA'];}`](abenbdl_default_function.md): Defines a [RAP default values function](../../abap-glossary/abenrap_bo_defaulting_glosry.md) for the [create-by-association operation](../../abap-glossary/abenrap_cba_operation_glosry.md). The effect is that field values are defaulted on the user interface.

## Restriction

In a managed RAP BO of an intra-BO scenario, create-by-association works only on direct child entities. Entities that are part of the same composition tree, but more than one level below the [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md), can be read enabled, but not create enabled. In an unmanaged RAP BO, this limitation does not apply.

## Availability

- Managed RAP BO: In a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md), operations for associations are provided by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md).

- Unmanaged RAP BO: In an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), operations for associations must be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) in the [RAP handler method](../abap-for-rap-business-objects/abapmethods_for_rap_behv.md) [`FOR MODIFY`](../abap-for-rap-business-objects/abaphandler_meth_modify.md).

- Projection BDEF: In a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md), operations for associations can be reused from the [base BDEF](../../abap-glossary/abenrap_base_bdef_glosry.md). This can be done using the keyword `use`. For further details, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

- RAP BO interface: In a RAP BO interface, operations for associations can be reused from the base BDEF. This can be done using the keyword `use`. For further details, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

## Hints

- For create-by-association operations, the optional addition [`AUTO FILL CID`](../abap-for-rap-business-objects/abapmodify_entity_entities_fields.md) can be used to automatically fill the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) component [`%cid`](../abap-for-rap-business-objects/abapderived_types_cid.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, topic [Create by Association Operation](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/ede2f6485d0e44a5b88e21272c462a12?version=sap_cross_product_abap).
