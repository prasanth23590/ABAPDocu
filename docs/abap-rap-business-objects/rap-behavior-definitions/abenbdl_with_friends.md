---
title: "RAP - with friends"
source_file: abenbdl_with_friends.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - BDEF Extension, Extensibility Enabling > RAP - Extensibility Enabling for Base BOs"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - with friends

## Syntax

``` abap
... with friends BDEFExtension1 [, BDEFExtension2] [,...]...  
```

## Description

Optional addition that can be used to declare one or more [BDEF extensions](../../abap-glossary/abenrap_extension_glosry.md) `BDEFExtension1`, `BDEFExtension2`, ... as [friends](../../abap-glossary/abenrap_bdef_friend_glosry.md) of the current behavior definition `RootEntity`. At least one BDEF extension must be specified. `BDEFExtension1`, `BDEFExtension2`, ... must be BDEF extensions of the current BDEF. Otherwise, there is no effect. Only BDEF extensions of the current BDEF can be specified as friends.

The friends of a BDEF have unrestricted access to all components of the BDEF. They are not handled as external [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md), but have the same access rights as the original RAP BO. In particular, a friend has the following rights:

- Access to [internal RAP BO operations](../../abap-glossary/abenrap_internal_operation_glosry.md).

- Privileged access rights using the addition [`IN LOCAL MODE`](../abap-for-rap-business-objects/abapin_local_mode.md).

- Access to [RAP BO fields](../../abap-glossary/abenrap_bo_field_glosry.md) from the original RAP BO.

If a friend of the BDEF `RootEntity` defines friends, these friends are not automatically friends of the original BDEF. This means that the friend relationship is not transitive.

## Hint

The concept of declaring BDEF extensions as friends can be useful, for example, for modularization purposes.

## Availability

- [Managed RAP BOs](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BOs](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- BDEF extensions to managed and unmanaged RAP BOs. For details, see the topic [RAP - Extensibility Enabling for Base BDEF Extensions](abenbdl_ext_enabl_ext_base.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example demonstrates the different handling of BDEF friends and non-friends.

The managed behavior definition `DEMO_RAP_FRIENDS` is defined as `extensible with friends`. It defines two actions:

- An internal action `internalAction` that can be accessed from within the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) only.

- The action `myAction` that is available also to external [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md).

``` abap
managed implementation in class bp_demo_rap_friends unique;
strict ( 2 );

extensible
with friends demo_rap_friends_x1;

define behavior for DEMO_RAP_FRIENDS
persistent table demo_dbtab_root
lock master
authorization master ( instance, global )
extensible

{
  create;
  update;
  delete;

  field(readonly:update) key_field;

  internal action internalAction;

  action myAction;
}
```

Two extensions are defined:

- `DEMO_RAP_FRIENDS_X1` -\> defined as BDEF friend.

- `DEMO_RAP_FRIENDS_X2` -\> not defined as BDEF friend.

**Enhanced Access Rights for BDEF Friends**

`DEMO_RAP_FRIENDS_X1` defines an extension action that executes the internal action of the original RAP BO. This is allowed, since `DEMO_RAP_FRIENDS_X1` is a BDEF friend of the original RAP BO.

Definition:

``` abap
extension implementation in class bp_demo_rap_friends_x1 unique;

extend behavior for DEMO_RAP_FRIENDS
{
action (authorization : instance) x1_call_static_internal;
}
```

Implementation of the extension action in the ABP: An internal action of the extended RAP BO is executed.

``` abap
METHOD x1_call_static_internal. 
  MODIFY ENTITIES OF demo_rap_friends IN LOCAL MODE 
  ENTITY demo_rap_friends 
  EXECUTE internalAction 
  FROM CORRESPONDING #( keys ). 
ENDMETHOD.
```

Executing the extension action using ABAP EML:

``` abap
MODIFY ENTITY demo_rap_friends 
     EXECUTE x1_call_static_internal 
     FROM VALUE #( ( key_field = 1 ) ) 
        FAILED DATA(failed) 
        REPORTED DATA(reported) 
        MAPPED DATA(mapped).
```

The ABAP EML consumer triggers the extension action `X1_CALL_STATIC_INTERNAL`. This leads to the following call stack: First, the authorization control of the BDEF extension `DEMO_RAP_FRIENDS_X1` is called. Then, the extension action is called. The extension action, in turn, calls the internal action `internalAction` of the extended RAP BO. The authorization control of the extended RAP BO is **not** called and the internal action can be executed, since the BDEF extension `DEMO_RAP_FRIENDS_X1` is defined as a friend of `DEMO_RAP_FRIENDS`.

**Access to Internal Actions Forbidden for Non-Friends**

`DEMO_RAP_FRIENDS_X2` defines an extension action that executes the internal action of the original RAP BO. This is not allowed, since `DEMO_RAP_FRIENDS_X2` is not a BDEF friend of the original RAP BO.

Definition:

``` abap
extension implementation in class bp_demo_rap_friends_x2 unique;

extend behavior for DEMO_RAP_FRIENDS
{
  action ( authorization : instance ) x2_dump_static_internal_local;
  action ( authorization : instance ) x2_dump_dynamic_internal_local;
}
```

Implementation of the extension action `X2_DUMP_STATIC_INTERNAL_LOCAL` in the ABP:

``` abap
METHOD x2_dump_static_internal_local. 
  MODIFY ENTITIES OF demo_rap_friends IN LOCAL MODE 
    ENTITY demo_rap_friends 
    EXECUTE internalAction 
    FROM CORRESPONDING #( keys ). 
ENDMETHOD.
```

Executing the extension action using ABAP EML: An internal action of the extended RAP BO is executed.

``` abap
MODIFY ENTITY demo_rap_friends 
     EXECUTE x2_dump_static_internal_local 
     FROM VALUE #( ( key_field = 1 ) ) 
        FAILED DATA(failed) 
        REPORTED DATA(reported) 
        MAPPED DATA(mapped).
```

The ABAP EML consumer triggers the extension action `X2_DUMP_STATIC_INTERNAL_LOCAL`. This leads to the following call stack: First, the authorization control of the BDEF extension `DEMO_RAP_FRIENDS_X2` is called. Then, the extension action is called. The extension action, in turn, calls the internal action `internalAction` of the extended RAP BO. This is not allowed and a runtime error occurs, since the BDEF extension `DEMO_RAP_FRIENDS_X2` is **not** a friend of `DEMO_RAP_FRIENDS`.
