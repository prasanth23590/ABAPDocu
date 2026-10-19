---
title: "RAP - Authorization"
source_file: abenbdl_authorization.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorCharacteristics"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - Authorization

## Syntax

``` abap
... authorization master {( global ) 
                         |( instance ) 
                         |( global, instance ) 
                         |( none )} 
  | authorization dependent by _Assoc ...  
```

## Description

[Authorization control](../../abap-glossary/abenrap_auth_control_glosry.md) in RAP protects your business object against unauthorized access to data. Authorization control is defined in the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md) for each [entity behavior definition](../../abap-glossary/abencds_entity_bdef_glosry.md) separately and it must be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md).

Authorization control in RAP manages access to various RAP operations: create, update, delete, [create-by-association operations](../../abap-glossary/abenrap_cba_operation_glosry.md), [RAP actions](../../abap-glossary/abenrap_action_glosry.md) and [RAP functions](../../abap-glossary/abenrap_function_glosry.md). The read operation is provided by CDS and governed by CDS access control. There are different methods for implementing various types of authorization control.

Authorization control is declared in several locations. First, it is defined in the [entity behavior characteristics](../../abap-glossary/abencds_entity_properties_glosry.md) for each RAP BO entity. This declaration defines the default authorization control for that entity: instance, global, instance and global, or none. The authorization control that is defined for a RAP BO entity applies to all [RAP BO operations](../../abap-glossary/abenrap_bo_operation_glosry.md) of that particular entity.

Then, within the entity behavior body, exceptions to the rule can be defined in the behavior characteristics for each RAP BO operation in a behavior. For example, a RAP action might have global authorization, while all other actions default to instance authorization. Alternatively, an operation might have none, meaning no authorization control is applied.

The following RAP BO operation additions can be used to control authorization checks for individual RAP BO operations:

- [`authorization:none`](abenbdl_actions_auth.md)

- [`authorization:update`](abenbdl_actions_auth_update.md)

- [`authorization:global`](abenbdl_actions_auth_global.md)

- [`authorization:instance`](abenbdl_actions_auth_instance.md)

RAP BO entities must be specified either as authorization master or authorization-dependent entities:

- [RAP authorization master entities](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) have their own authorization implementation in the ABAP behavior pool in the corresponding method for authorization (global or instance). The implementation is used when requesting access to the authorization master entity or to any of its authorization-dependent entities.

- [RAP authorization dependent entities](../../abap-glossary/abenrap_auth_dep_ent_glosry.md) use the authorization control that is defined on the related authorization master entity. Authorization requests are delegated to the implementation of the authorization master entity. For update, delete, and create-by-association operations on an authorization-dependent entity, the authorization check for update of the authorization master entity is applied. For [CDS to-child associations](../../abap-glossary/abento_child_association_glosry.md), you can deviate from this default by specifying separate authorizations for create-by-association operations.

The following rules apply:

- Each RAP BO entity must be declared as [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) or as [authorization dependent entity](../../abap-glossary/abenrap_auth_dep_ent_glosry.md) using the syntax `authorization master (...)` or `authorization dependent by _Assoc`.

- The [RAP BO root entity](../../abap-glossary/abenrap_bo_root_entity_glosry.md) must be defined as authorization master entity. All other RAP BO entities can be either authorization master or authorization-dependent entities.

- If the authorization master entity is not the parent entity of the authorization-dependent entity, then the association to the authorization master entity must be explicitly defined in the entity behavior definition using the syntax `association _AssocToAuthMaster { }`.

- In the following cases, the authorization control must be implemented in separate methods for authorization in the behavior pool of the authorization-dependent entity:

  - [actions](abenbdl_action.md) and [functions](abenbdl_function.md) of authorization dependent entities

  - create-enabled [cross-BO associations](../../abap-glossary/abencds_cross_bo_assoc_glosry.md)

  - create-enabled associations that are not to-child associations

The following types of authorization control are available:

- `global`

  - Limits access to data or the permission to perform certain operations for a complete RAP BO, independent of individual instances, for example, depending on user roles.

  - Can be specified for the following operations of an entity: [create](abenbdl_standard_operations.md), [create by association](../../abap-glossary/abenrap_cba_operation_glosry.md), [update](abenbdl_standard_operations.md), [delete](abenbdl_standard_operations.md), [static actions](abenbdl_action.md), [instance actions](abenbdl_action.md), [static functions](abenbdl_function.md), [instance functions](abenbdl_function.md).

  - Must be implemented in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR GLOBAL AUTHORIZATION`](../abap-for-rap-business-objects/abaphandler_meth_global_auth.md).

- `instance`

  - Authorization check that is dependent on the state of an entity instance.

  - Can be specified for the following operations of an entity: [create by association](abenbdl_association.md), [update](abenbdl_standard_operations.md), [delete](abenbdl_standard_operations.md), [instance actions](abenbdl_action.md), [instance functions](abenbdl_function.md).

  - Must be implemented in the [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR INSTANCE AUTHORIZATION`](../abap-for-rap-business-objects/abaphandler_meth_auth.md).

- `global, instance`

  - Global and instance authorization control can be combined. In this case, instance-based operations are checked in the global and in the instance authority check. Both RAP handler methods, [`FOR GLOBAL AUTHORIZATION`](../abap-for-rap-business-objects/abaphandler_meth_global_auth.md) and [`FOR INSTANCE AUTHORIZATION`](../abap-for-rap-business-objects/abaphandler_meth_auth.md), must be implemented. The checks are executed at different points in time during runtime.

- `none`

  - Can be specified for an authorization master entity to define that there are no authorization checks for the entire RAP BO. When `none` is specified, it is not possible to implement [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) for authorizations.

Authorization checks can be implemented, for example, using [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md).

## Availability

- Managed RAP BO

  In a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md), if the root entity is specified as `authorization master`, the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) checks each [RAP BO operation](../../abap-glossary/abenrap_bo_operation_glosry.md) for any access restrictions.

- Unmanaged RAP BO

  In an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), and if global authorization control is specified, the RAP framework checks each RAP BO operation for any access restrictions.

- Draft-enabled RAP BO

  In a [draft-enabled RAP BO](abenbdl_with_draft.md), the RAP framework checks for each [standard operation](abenbdl_standard_operations.md) on a draft instance whether there are any access restrictions. For the [draft actions](abenbdl_draft_action.md) `Resume` and `Edit`, the authorization control for [create](abenbdl_standard_operations.md) is checked. For the draft actions `Activate`, `Discard`, and `Prepare`, the authorization methods are not called. To prevent a draft instance from activation, the authorization check has to be implemented in a [validation](abenbdl_validations.md).

- Projection BO

  In a [projection business object](../../abap-glossary/abenrap_projection_bo_glosry.md), the authorization from the [base business object](../../abap-glossary/abenrap_projected_bo_glosry.md) is automatically inherited. If [new actions or functions](abenbdl_nonstandard_projection.md) are defined in the projection layer, a new authorization control for these actions and functions can be defined. For further details, see topic [RAP - `authorization`, Projection BDEF](abenbdl_authorization_projection.md).

- [RAP BO interface](../../abap-glossary/abenrap_bo_interface_glosry.md)

  In a RAP BO interface, the authorization control from the base BO is automatically inherited.

## Hints

- The EML statement [`IN LOCAL MODE`](../abap-for-rap-business-objects/abapin_local_mode.md) can be used to skip authorization control.

- A [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) can use the EML statement [`GET PERMISSIONS`](../abap-for-rap-business-objects/abapget_permissions.md) to check whether a RAP BO has authorization control implemented.

- To limit read access to a business object, [Data Control Language (DCL)](../../abap-glossary/abendcl_glosry.md) can be used. These CDS access controls defined in [Data Control Language (DCL)](../../abap-glossary/abendcl_glosry.md) are passed on from the base layer to the RAP BO projection and the RAP BO interface. An executable example that demonstrates how read access control is implemented and evaluated can be found in topic [RAP BDL - RAP BO with DCL Access Control](abenbdl_draft_query_abexa.md).

- Authorizations can also be checked in other ABP methods, for example, in [validations](abenbdl_validations.md).

- In UI scenarios, authorization control is displayed as RAP consumer hint.

- In [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md) to managed and unmanaged RAP BOs, authorization control must be specified for each action separately. The reason for this is that the authorization control of extension actions should be independent of the authorization control of the original RAP BO to ensure stability even if the original BO is changed.

- The following syntax short form is available to summarize lock dependent, ETag dependent, and authorization dependent:

  `([lock][, authorization][, etag]) dependent by _assoc` For details, see topic [RAP - `SyntaxShortForm`](abenbdl_short_syntax.md).

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [Authorization Control](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/375a8124b22948688ac1c55297868d06?version=sap_cross_product_abap).

## Executable Example

The example above is explained in detail in the executable example [RAP BDL - global authorization](abenbdl_authorization_abexa.md).
