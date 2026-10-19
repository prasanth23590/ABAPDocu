---
title: "RAP - Operations for Associations"
source_file: abenbdl_association.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Operations for Associations

## Syntax

``` abap
... [internal] [AssocImplType] association _Assoc[;] 
               [abbreviation newName] 
               [without response] 
               [using TargetEntity {\_ReverseAssoc |~TargetAltKey}] 
       [{ 
       [StandardOperationsForAssoc]; 
       [NonStandardOperationsForAssoc]; 
       [with draft]; 
        }]  
```

[`internal`](abenbdl_internal.md) · [`AssocImplType`](abenbdl_assoc_impl_type.md) · [`StandardOperationsForAssoc`](abenbdl_assoc_stand_ops.md) · [`NonStandardOperationsForAssoc`](abenbdl_assoc_nonstand_ops.md)

### Addition

[1. `... abbreviation newName ...`](abenbdl_association.md#addition-1)

[2. `... without response ...`](abenbdl_association.md#addition-2)

[3. `... using TargetEntity {\_ReverseAssoc |~TargetAltKey}...`](abenbdl_association.md#addition-3)

[4. `... with draft; ...`](abenbdl_association.md#addition-4)

## Overview

### Description

A RAP BO operation for associations operates along an [association path](../../abap-glossary/abencds_association_path_glosry.md) and affects the [association target](../../abap-glossary/abenassociation_target_glosry.md). These operations are defined in the entity behavior body of a [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md). There are [standard operations for associations](../../abap-glossary/abenrap_standard_op_assoc_glosry.md) and [non-standard operations for associations](../../abap-glossary/abenrap_nonst_op_assoc_glosry.md).

- [**Standard Operation for Associations**](abenbdl_assoc_stand_ops.md):

  An operation that provides canonical behavior along an [association path](../../abap-glossary/abencds_association_path_glosry.md) from an [association source](../../abap-glossary/abenassociation_source_glosry.md) to an [association target](../../abap-glossary/abenassociation_target_glosry.md). [Create-by-association](../../abap-glossary/abenrap_cba_operation_glosry.md) and [read-by-association](../../abap-glossary/abenrap_rba_operation_glosry.md) are standard operations for associations.

- [**Non-Standard Operation for Associations**](abenbdl_assoc_nonstand_ops.md):

  An operation that provides noncanonical behavior along an [association path](../../abap-glossary/abencds_association_path_glosry.md) from an [association source](../../abap-glossary/abenassociation_source_glosry.md) to an [association target](../../abap-glossary/abenassociation_target_glosry.md). For example, the [link action](../../abap-glossary/abenrap_link_action_glosry.md), the [unlink action](../../abap-glossary/abenrap_unlink_action_glosry.md), the [inverse function](../../abap-glossary/abenrap_inverse_function_glosry.md) are predefined nonstandard operations for associations.

The [read-by-association operation](../../abap-glossary/abenrap_rba_operation_glosry.md) is automatically enabled when the association is specified in the behavior definition. There is no dedicated syntax element.

Example: `association _Assoc;`

[Read-by-association](../../abap-glossary/abenrap_rba_operation_glosry.md) allows [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md) read access to the [association target](../../abap-glossary/abenassociation_target_glosry.md) of a RAP BO entity.

The following rules apply:

- The read-by-association operation can be defined for [intra BO associations](../../abap-glossary/abencds_intra_bo_assoc_glosry.md) and for [cross-BO associations](../../abap-glossary/abencds_cross_bo_assoc_glosry.md).

- The association target entity must be behavior enabled, in other words, the association target entity must have its own behavior definition.

- In the case of intra-BO associations, it is mandatory to define at least read access to the associations to RAP BO entities that are also behavior-enabled.

**RAP BDL Operation Additions**

The following [RAP BDL operation additions](abenbdl_operations_additions.md) are possible:

- [`internal`](abenbdl_internal.md): Every defined operation for association can only be accessed internally, including the implicitly defined read-by-association operation.

## Availability

- Managed RAP BO: In a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md), operations for associations are provided by the [managed RAP BO provider](../../abap-glossary/abenmanaged_rap_bo_prov_glosry.md).

- Unmanaged RAP BO: In an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), operations for associations must be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) in the [RAP handler method](../abap-for-rap-business-objects/abapmethods_for_rap_behv.md) [`FOR MODIFY`](../abap-for-rap-business-objects/abaphandler_meth_modify.md).

- Projection BDEF: In a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md), operations for associations can be reused from the [base BDEF](../../abap-glossary/abenrap_base_bdef_glosry.md). This can be done using the keyword `use`. For further details, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

- RAP BO interface: In a RAP BO interface, operations for associations can be reused from the base BDEF. This can be done using the keyword `use`. For further details, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

## More Information

Development guide for the ABAP RESTful Application Programming Model, topic [Read by Association](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/1f518ea257f6455380384f3810e67ba5?version=sap_cross_product_abap).

### Hint

In [cross-BO](../../abap-glossary/abencds_cross_bo_assoc_glosry.md) scenarios, when association-related ABAP EML requests on the [association source](../../abap-glossary/abenassociation_source_glosry.md)&#x00A0;are performed and specify `IN LOCAL MODE` (such as [read-by-association](../../abap-glossary/abenrap_rba_operation_glosry.md) or [create-by-association](../../abap-glossary/abenrap_cba_operation_glosry.md) operations), the [association target](../../abap-glossary/abenassociation_target_glosry.md)'s implementation of the operation is accessed in privileged mode (not in local mode), bypassing the association target's authorization checks. This applies only if the association target is specified with a [privileged](../../abap-glossary/abenrap_privileged_mode_glosry.md) context.

## Addition 1

`... abbreviation newName`

### Description

Defines an alternative name for an association. The abbreviation `newName` can have a maximum of 16 characters. Associations are in the namespace of their root entity and can have up to 30 characters. This is under certain circumstances too long to be processed in [ABAP RAP](../../abap-glossary/abenabap_rap_glosry.md). Whenever a shorter name is required, you are prompted to assign an abbreviation to the association with no more that 16 characters. The abbreviation should start with a character, not with an underscore.

## Addition 2

`... without response`

### Description

The optional addition `without response` is for cross-BO associations that have an association target from another BO. The association target entity of cross-BO associations is automatically included in the response types of the current RAP BO as [foreign entity](abenbdl_foreign.md). In this way, issues with the target entity can become part of the response types during read-by-association or create-by-association operations. `without response` prevents the default behavior. It excludes the [foreign entity](../../abap-glossary/abenrap_foreign_entity_glosry.md) from the response types.

Notation: `association _ext without response { create; }`

## Addition 3

`... using TargetEntity {\_ReverseAssoc |~TargetAltKey}...`

### Description

The optional addition `...using...` is relevant for [target-resolved associations](../../abap-glossary/abentarget_resolved_assoc_glosry.md) in cross-BO scenarios. It defines the option of how to determine the [primary key](../../abap-glossary/abenprimary_key_glosry.md) fields of the associated target entity instances. The target primary key must be identified to read the target instances, for example, in a [read-by-association operation](../../abap-glossary/abenrap_rba_operation_glosry.md).

There are two options to retrieve the primary key of the target entity:

- Via the declaration of its reverse association:

  When declaring the reverse association of the association at hand, the primary key of the associated target instances is retrieved by executing the [inverse function](../../abap-glossary/abenrap_inverse_function_glosry.md), which is defined for the reverse association in the target entity. The inverse function receives the primary key of the source entity as input parameter and returns the primary key of the target entity. Notation: `... using TargetEntity \_ReverseAssoc`

- Via the alternative key and the key function of the target entity

  When declaring the [alternative key](../../abap-glossary/abenrap_alternative_key_glosry.md) in the using addition, the primary key of the associated target instances is retrieved by executing the [key function](../../abap-glossary/abenrap_key_function_glosry.md), which is defined in the target entity. A prerequisite for the is the declaration of an [alternative key](../../abap-glossary/abenrap_alternative_key_glosry.md) in the target entity, which must be the primary key of the source entity. The target entity's key function receives the primary key of the source entity as input parameter and returns the target entity's primary key. This option is mainly used in cross-BO scenarios with reuse objects, where the reverse association is not available. Notation: `... using TargetEntity ~TargetAltKey`

## Addition

`... with draft; ...`

### Description

Draft-enables an association. A draft-enabled association retrieves active data if it is followed from an [active instance](../../abap-glossary/abenrap_active_instance_glosry.md) and draft data if it is followed from a [draft instance](../../abap-glossary/abenrap_draft_instance_glosry.md) (for details about RAP draft handling, see [RAP BDL - managed, with draft](abenbdl_with_draft.md)).

If a [BO](../../abap-glossary/abenbusiness_object_glosry.md) is draft-enabled, then all associations should be draft-enabled, so that the associations always lead to the target instance with the same state (draft or active).

As soon as you draft-enable a BO by adding `with draft`, all BO-internal associations are automatically draft-enabled. To make this behavior explicit, the behavior prompts you to specify the to-child associations within a draft BO with `with draft`.
