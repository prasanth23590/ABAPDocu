---
title: "RAP - authorization:global"
source_file: abenbdl_actions_auth_global.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - EntityBehaviorDefinition > RAP - EntityBehaviorBody > RAP - RAP BO Operations > RAP - RAP BO Operation, Additions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - authorization:global

## Syntax

``` abap
... (authorization:global) ...  
```

## Description

The [RAP BO operation addition](abenbdl_operations_additions.md) `authorization:global` replaces the [authorization control](abenbdl_authorization.md) that is specified in the [authorization master entity](../../abap-glossary/abenrap_auth_ma_ent_glosry.md) and applies global authorization checks instead. It can be used for [actions](abenbdl_action.md), [determine actions](abenbdl_determine_action.md), and [functions](abenbdl_function.md) in authorization master and authorization dependent entities. It can also be used for [create-by-association operations](../../abap-glossary/abenrap_cba_operation_glosry.md) for [to-child associations](../../abap-glossary/abento_child_association_glosry.md).

It is possible to combine the additions `authorization:global` and [`authorization:instance`](abenbdl_actions_auth_instance.md) for an action, a determine action, a function, or a create-by-association. Then, both [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md), [`FOR GLOBAL AUTHORIZATION`](../abap-for-rap-business-objects/abaphandler_meth_global_auth.md) and [`FOR INSTANCE AUTHORIZATION`](../abap-for-rap-business-objects/abaphandler_meth_auth.md), are checked before the action is executed. Examples:

`action ( authorization : global, authorization : instance ) MyAction`;

`function (authorization : global, authorization : instance) MyFunction result [1] $self;`

`association _child { create (authorization : global, authorization : instance); }`

If no authorization control is specified for an action, function or create-by-association, the authorization mode of the [authorization master](abenbdl_authorization.md) (`global`, `instance`, or both) is used for the operation by default.

## Hints

- In managed, unmanaged, and projection RAP BOs, authorization control can be specified in the authorization master entity and applies to all operations. The operation additions [`authorization:none`](abenbdl_actions_auth.md), [`authorization:update`](abenbdl_actions_auth_update.md), `authorization:global`, and [`authorization:instance`](abenbdl_actions_auth_instance.md) are optional. However, in [base BDEF extensions](../../abap-glossary/abenrap_base_bdef_ext_glosry.md), authorization control must be specified for each operation separately. The reason for this is that the authorization control of extension operations should be independent of the authorization control of the original RAP BO to ensure stability even if the original BO is changed.

- The addition `authorization:global` cannot be used for [internal operations](abenbdl_internal.md).

## More Information

- Development guide for the ABAP RESTful Application Programming Model, [Action Definition](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/14ddc6b2442b4b97842af9158a1c9c44?version=sap_cross_product_abap), [Function Definition](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/30708173550d4a358f87f38bcc77f6d2?version=sap_cross_product_abap) and [Authorization Definition](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/2a26db5640364b46b843dca786c495d1?version=sap_cross_product_abap)

- For more information about authorization control in RAP, see [RAP - Authorization](abenbdl_authorization.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates authorization control for RAP actions in a BDEF extension. The base behavior definition `DEMO_RAP_AUTH_GLOBAL` defines instance-based authorization control in the authorization master entity.

``` abap
managed implementation in class bp_demo_rap_auth_global unique;
strict ( 2 );
extensible;

define behavior for DEMO_RAP_AUTH_GLOBAL alias Root
persistent table demo_dbtab_root
lock master
authorization master ( instance, global )
extensible

{
  create;
  update;
  delete;

  field ( readonly ) key_field;
}
```

The BDEF extension `DEMO_RAP_AUTH_GLOBAL_X1` defines new extension actions with an authorization control that replaces the authorization control from the original BDEF. The extension actions and the respective authorization control are implemented in the extension ABAP behavior pool.

``` abap
extension using interface DEMO_RAP_GLOBAL_AUTH_INT
implementation in class bp_demo_rap_auth_global_x1 unique;

extend behavior for Root
{

  action ( authorization : instance ) ext1AuthInstance;
  action ( authorization : global ) ext1AuthGlobal;
  action ( authorization : global, authorization : instance )
    ext1AuthGlobalInstance;
  action ( authorization : none ) ext1AuthNone;

  association _child { create; }
}
define behavior for DEMO_RAP_AUTH_GLOBAL_CH alias Child
  using DEMO_RAP_GLOBAL_AUTH_INT_CH
persistent table demo_dbtab_child
lock dependent
authorization dependent
{
  update;
  delete;
  field ( readonly ) key_field, key_field_child;
  association _parent;

  action ( authorization : update ) ext1AuthUpdate;
}
```
