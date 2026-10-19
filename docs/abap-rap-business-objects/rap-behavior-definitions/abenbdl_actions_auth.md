---
title: "RAP - authorization:none"
source_file: abenbdl_actions_auth.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - RAP BO Operation, Additions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - authorization:none

## Syntax

``` abap
... (authorization:none) ...  
```

## Description

The RAP BO operation addition `authorization:none` excludes the operation in question from [authorization checks](abenbdl_authorization.md). As a prerequisite, [authorization control](abenbdl_authorization.md) must be defined and implemented.

`authorization:none` can be used for the following operations:

- The [standard operations `create`, `update`, and `delete`](abenbdl_standard_operations.md)

  **Note:** For the standard operation `create`, the addition `authorization:none` is only available in case of global authorization.

- [Operations for associations](abenbdl_association.md)

- [Actions](abenbdl_action.md)

  **Note:** For static actions, the addition `authorization:none` is only available in case of global authorization.

- [Determine actions](abenbdl_determine_action.md)

- The [draft action `Edit`](abenbdl_draft_action.md)

- [RAP hierarchy actions](../../abap-glossary/abenrap_hierarchy_action_glosry.md)

- [Functions](abenbdl_function.md)

For actions and determine actions, the addition `(authorization:none)` can be used in authorization master and authorization dependent entities.

For standard operations, operations for associations, and the draft action `Edit`, this addition can be used in the [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) only.

## Hints

- For details on authorization control in RAP, see topic [RAP - Authorization](abenbdl_authorization.md).

- In managed, unmanaged, and projection RAP BOs, authorization control can be specified in the authorization master entity and applies to all actions. The operation additions `authorization:none`, [`authorization:update`](abenbdl_actions_auth_update.md), [`authorization:global`](abenbdl_actions_auth_global.md), and [`authorization:instance`](abenbdl_actions_auth_instance.md) are optional. However, in [base BDEF extensions](../../abap-glossary/abenrap_base_bdef_ext_glosry.md), authorization control must be specified for each action separately. The reason for this is that the authorization control of extension actions should be independent of the authorization control of the original RAP BO to ensure stability even if the original BO is changed.

## More Information

- Development guide for the ABAP RESTful Application Programming Model, section [Authorization Definition](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/2a26db5640364b46b843dca786c495d1?version=sap_cross_product_abap).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the notation in the RAP behavior definition.

- Standard operation: `delete (authorization:none);`

- Association: `association _MyAssoc { create(authorization:none); }`

- Action: `action (authorization:none) MyAction;`

- Determine action: ` determine action (authorization:none) MyDetAction{ ... }`

- Draft action: `draft action (authorization:none) Edit;`
