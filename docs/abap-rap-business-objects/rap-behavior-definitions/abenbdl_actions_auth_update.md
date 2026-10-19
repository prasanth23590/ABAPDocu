---
title: "RAP - authorization:update"
source_file: abenbdl_actions_auth_update.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - RAP BO Operation, Additions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - authorization:update

## Syntax

``` abap
... (authorization:update) ...  
```

## Description

The RAP BO operation addition `authorization:update` delegates the [authorization check](abenbdl_authorization.md) for the operation in question to the update operation. That means that an operation specified as `authorization:update` has the same authorization control that is specified for the update operation.

As a prerequisite, [authorization control](abenbdl_authorization.md) must be defined and implemented. However, it is not required that the update operation is enabled for the entity in question. You can delegate the authorization for operations to the update operation even though the update operation is not enabled for this entity.

The addition `authorization:update` can be used for the following operations:

- The [standard operation `delete`](abenbdl_standard_operations.md)

- The [create-by-association](../../abap-glossary/abenrap_cba_operation_glosry.md) operation

- [Actions](abenbdl_action.md)

- [Determine actions](abenbdl_determine_action.md)

- [RAP hierarchy actions](../../abap-glossary/abenrap_hierarchy_action_glosry.md)

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [Authorization Definition](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/2a26db5640364b46b843dca786c495d1?version=sap_cross_product_abap).

## Hints

- For details on authorization control in RAP, see topic [RAP - Authorization](abenbdl_authorization.md).

- Standard operations in authorization-dependent entities are automatically delegated to the update operation of the [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md).

- If you delegate the authorization for an [action](../../abap-glossary/abenrap_action_glosry.md) in an authorization-dependent entity to the update operation, it will be delegated to the update operation of the authorization master entity in the end.

- In managed, unmanaged, and projection RAP BOs, authorization control can be specified in the authorization master entity and applies to all actions. The operation additions [`authorization:none`](abenbdl_actions_auth.md), `authorization:update`, [`authorization:global`](abenbdl_actions_auth_global.md), and [`authorization:instance`](abenbdl_actions_auth_instance.md) are optional. However, in [base BDEF extensions](../../abap-glossary/abenrap_base_bdef_ext_glosry.md), authorization control must be specified for each action separately. The reason for this is that the authorization control of extension actions should be independent of the authorization control of the original RAP BO to ensure stability even if the original BO is changed.

- `authorization:update` cannot be used for [internal operations](abenbdl_internal.md). Internal actions do not have authorization checks in general, as they are only invoked internally.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

An example for `authorization:update` in a projection BDEF is provided in the topic about authorization control in projection BDEFs, see [RAP BDL - authorization, projection BDEF](abenbdl_authorization_projection.md).
