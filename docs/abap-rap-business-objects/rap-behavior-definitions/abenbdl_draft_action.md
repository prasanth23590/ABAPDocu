---
title: "RAP - draft action"
source_file: abenbdl_draft_action.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - draft action

## Syntax

``` abap
[internal] draft action 
           {[([authorization:none][,features: instance])] 
           [Edit [with additional implementation];]} 
         | [Activate [optimized] [with additional implementation];] 
         | [Discard [with additional implementation];] 
         | [Resume [with additional implementation];] 
         | [draft determine action Prepare [extensible] 
              { 
               determination [(always)] DetName; 
               validation [(always)] ValName; 
               ... 
              }] 
         | [AdditionalSave;] 
         | [Share;]  
```

[`authorization:none`](abenbdl_actions_auth.md) · [`features: instance`](abenbdl_actions_fc.md) · [`extensible`](abenbdl_extensibility_enabling_m_u.md) · [`determination`](abenbdl_determinations.md) · [`validation`](abenbdl_validations.md)

### Variant

[1. `... draft action Edit;`](abenbdl_draft_action.md#variant-1)

[2. `... draft action Activate [optimized];`](abenbdl_draft_action.md#variant-2)

[3. `... draft action Discard;`](abenbdl_draft_action.md#variant-3)

[4. `... draft action Resume;`](abenbdl_draft_action.md#variant-4)

[5. `... draft determine action Prepare;`](abenbdl_draft_action.md#variant-5)

[6. `... draft action AdditionalSave;`](abenbdl_draft_action.md#variant-6)

[7. `... draft action Share;`](abenbdl_draft_action.md#variant-7)

### Addition

[1. `... with additional implementation`](abenbdl_draft_action.md#addition-1)

## Overview

### Description

[Draft actions](../../abap-glossary/abenrap_bo_draft_action_glosry.md) are available for [draft-enabled RAP BOs](../../abap-glossary/abendraft_rap_bo_glosry.md) only. They allow data to be manipulated on the [RAP draft table](../../abap-glossary/abendraft_table_glosry.md).

Draft actions must be specified for [lock master entities](../../abap-glossary/abenrap_lock_ma_ent_glosry.md) that are defined using the keyword `lock master` only, as they refer to the whole lockable subtree of a business object.

Draft actions are provided by the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) in all scenarios. An implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is not required. The draft life cycle is determined by the RAP draft-runtime as soon as the business object is draft-enabled. The application developer does not need to implement the creation, update, or saving of [draft instances](../../abap-glossary/abenrap_draft_instance_glosry.md). However, the optional addition `with additional implementation` is available for some draft actions. It allows an implementation of the respective draft action in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR MODIFY ... ACTION`](../abap-for-rap-business-objects/abaphandler_meth_modify.md) in the ABAP behavior pool.

The following [RAP BDL operation additions](abenbdl_operations_additions.md) are possible:

- [`internal`](abenbdl_internal.md): Available for all draft actions.

- [`(features:instance)`](abenbdl_actions_fc.md): Dynamic feature control is available only for `Edit`. For `Edit`, it is per default implicitly enabled.

- [`authorization:none`](abenbdl_actions_auth.md): Available only for `Edit`.

## Availability

- Managed and draft-enabled RAP BOs (mandatory).

- Unmanaged and draft-enabled RAP BOs (mandatory).

- In [projection BDEFs](../../abap-glossary/abencds_proj_bdef_glosry.md) that reuse RAP draft handling, the draft actions must be reused using the syntax `use action DraftActionName`. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

- In [RAP BO interfaces](../../abap-glossary/abenrap_bo_interface_glosry.md) that reuse RAP draft handling, the draft actions must be reused using the syntax `use action DraftActionName`. For details on reuse, see topic [RAP - `use`, Projection and Interface BDEF](abenbdl_use_projection.md).

### Hint

In draft-enabled scenarios, the names of the draft actions are reserved for the draft actions. Entities that are not draft-enabled can use the names `Edit`, `Activate`, and so on, as names for [actions](abenbdl_action.md). But when the addition `with draft;` or `with collaborative draft;` is used to draft-enable a business object, the names of draft actions are forbidden as names for actions.

## More Information

Development guide for the ABAP RESTful Application Programming Model, topic [Draft Actions](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/707c7e93ecab48ea9e6b9c3c893a792e?version=sap_cross_product_abap).

### Executable Example

- The example above is explained in detail in the topic [RAP - Draft Actions Edit, Discard, Prepare](abenbdl_draft_action2_abexa.md).

- Another executable example for the draft action `Activate` can be found in the topic [RAP - Draft Action `Activate`](abenbdl_draft_action1_abexa.md).

## Variant 1

`... draft action Edit`

### Description

The draft action `Edit` copies an active instance to the draft database table. [Feature](../../abap-glossary/abenrap_feature_control_glosry.md) and [authorization control](../../abap-glossary/abenrap_auth_control_glosry.md) is available for `Edit`, which can optionally be defined to restrict the usage of the action. The optional addition `with additional implementation` is available.

## Variant 2

`... draft action Activate [optimized]`

### Description

The draft action `Activate` is the inverse action to `Edit`. It copies the content of the draft database table to the [persistent database table](../../abap-glossary/abenrap_persistent_table_glosry.md) and clears the draft database table. It includes all changes that were done on the draft application buffer. `Activate` includes an implicit execution of the draft determine action `Prepare`.

It is recommended that you always use the optional addition `optimized`:

- `optimized` speeds up the activation of draft instances considerably by reducing the number of determination and validation executions in a RAP transaction.

- As a prerequisite, determinations and validations must be modeled according to the guidelines described in the [development guide for the ABAP RESTful Application Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/289477a81eec4d4e84c0302fb6835035?version=sap_cross_product_abap), section [*Determination and Validation Modelling*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/86a21be150db463a9c687e3ad34c308a?version=sap_cross_product_abap). For example, it must be ensured that the validations and determinations handle draft and active instances identically.

- Further details are described in the [development guide for the ABAP RESTful Application Programming Model](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/289477a81eec4d4e84c0302fb6835035?version=sap_cross_product_abap) in the following topics:

  - [*Draft Action Activate Optimized*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/7952cccd228444f383875d2fbbcd4b1e?version=sap_cross_product_abap)

  - [*Runtime Activate Optimized Action*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/9b7a3b482af04772ad6902e9e25ce300?version=sap_cross_product_abap)

  - [*Determination and Validation Modelling*](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/86a21be150db463a9c687e3ad34c308a?version=sap_cross_product_abap)

The optional addition `with additional implementation` is available.

## Variant 3

`... draft action Discard`

### Description

The draft action `Discard` deletes the draft instance from the draft database table. The optional addition `with additional implementation` is available.

## Variant 4

`... draft action Resume`

### Description

The draft action `Resume` is executed when a user continues to work on a draft instance whose exclusive lock for the active data has already expired. It re-creates the lock for the corresponding entity instance on the active database table. It is executed automatically whenever there is a modification on a draft instance whose exclusive lock has expired.

In case of [new draft instances](../../abap-glossary/abenrap_new_draft_inst_glosry.md), the same feature and authorization control is executed as defined for the [standard operation `create`](abenbdl_standard_operations.md). In case of [edit-draft instances](../../abap-glossary/abenrap_edit_draft_inst_glosry.md), the same feature and authorization control is executed as defined for the draft action `Edit`.

The optional addition `with additional implementation` is available.

### Hint

In case of an edit draft, if a [RAP BO precheck](../../abap-glossary/abenrap_bo_precheck_glosry.md) is required, this precheck implementation must be triggered explicitly during the draft action `Resume`. For this, the addition `with additional implementation` is required and the respective [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) must trigger the precheck method. For further details and an example, see the development guide for the ABAP RESTful Application Programming Model, topic [Implementing Prechecks](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/5a24e181eb994fffb59a186a2fdb3ef2?version=sap_cross_product_abap).

## Variant 5

`... draft determine action Prepare`

### Description

The draft determine action `Prepare` executes the [determinations](../../abap-glossary/abenrap_determination_glosry.md) and [validations](../../abap-glossary/abenrap_validation_glosry.md) that are assigned to it in the behavior definition. The `Prepare` enables validating draft data before the transition to active data. `Prepare` is the draft-equivalent to the [determine actions](abenbdl_determine_action.md) for active instances and the rules described in the [topic about determine actions](abenbdl_determine_action.md) apply to `Prepare` as well, in particular the following:

- Only [validations](abenbdl_validations.md) and [determinations defined as `on save`](abenbdl_determinations.md) can be assigned.

- The assignment of determinations and validations must be done explicitly in the BDEF. Only determinations and validations that are defined and implemented for the BO can be used.

- It is also possible to not define any determinations or validations to the draft determine action `Prepare`.

- The optional addition [(always)](abenbdl_determine_action.md) can be used.

- Determinations and validations of child entities can be included.

- Available for managed scenarios and for unmanaged and draft-enabled scenarios.

- The optional addition [`extensible`](abenbdl_extensible.md) allows validations and determinations to be added to the draft determine action `Prepare` in question by means of [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md). For further details on extensibility enabling, see topic [RAP - Extensibility Enabling for Base BOs](abenbdl_extensibility_enabling_m_u.md).

## Variant 6

`... draft action AdditionalSave`

### Description

The draft action `AdditionalSave` can be used to define an additional draft save for [draft instances](../../abap-glossary/abenrap_draft_instance_glosry.md). It is intended in particular for draft actions with the addition `with additional implementation`. For these draft actions, an additional save allows additional functionality to be called during the standard [save sequence](../../abap-glossary/abenrap_save_seq_glosry.md). An implementation in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR MODIFY ... FOR ACTION`](../abap-for-rap-business-objects/abaphandler_meth_modify.md) is required. The name of this method is `AdditionalSave` by default.

It is recommended that the draft action `AdditionalSave` is defined as [`internal`](abenbdl_internal.md), as it is called internally by the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) only. It is not possible to execute this action using [`MODIFY ENTITIES ... EXECUTE`](../abap-for-rap-business-objects/abapmodify_entity_entities_op.md) in ABAP EML, not even when using the addition [`IN LOCAL MODE`](../abap-for-rap-business-objects/abapin_local_mode.md) and not from the current RAP BO's [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). The draft action `AdditionalSave` is not exposed in an OData service.

The draft action `AdditionalSave` can be specified in managed and unmanaged BDEFs. Reuse in a projection BDEF or in an interface BDEF with the keyword [`use`](abenbdl_use_projection.md) is not possible.

### Hint

The draft action `AdditionalSave` is a [static](../../abap-glossary/abenrap_static_operation_glosry.md) action, this means, the [BDEF derived type](../../abap-glossary/abenrap_derived_type_glosry.md) for the importing parameter of the corresponding RAP handler method has a component [`%cid`](../abap-for-rap-business-objects/abapderived_types_cid.md).

## Variant 7

`... draft action Share`

### Description

In relation to the collaborative draft, the draft action `Share` is executed as soon as other users are added to the user list or the user attempts to join the user list of a [draft instance](../../abap-glossary/abenrap_draft_instance_glosry.md). It checks if the respective users are allowed to be added to the user list of the draft instance. In addition, the draft action `Share` switches an [exclusive draft](../../abap-glossary/abenrap_exclusive_draft_glosry.md) into [collaborative draft](../../abap-glossary/abenrap_collaborative_draft_glosry.md) if not done before.

## Addition 1

`... with additional implementation`

### Description

The optional addition `with additional implementation` is available for `Edit`, `Activate`, `Discard`, and `Resume`. If it is specified, an implementation for the respective draft action in the [RAP handler method](../abap-for-rap-business-objects/abapmethods_for_rap_behv.md) `FOR MODIFY` in the local ABAP behavior pool is required.
