---
title: "RAP - define own authorization context"
source_file: abenbdl_def_own_auth_context.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - AuthorizationContext"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - define own authorization context

## Syntax

``` abap
  define own authorization context by privileged mode; 
| define own authorization context by privileged mode and 
  { 
  [AuthObject1;] 
  [AuthObject2;] 
  [...] 
  } 
| define own authorization context 
  { 
  [AuthObject1;] 
  [AuthObject2;] 
  [...] 
  }  
```

[`AuthObject1`](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md) · [`AuthObject2`](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md) · [`AuthObject1`](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md) · [`AuthObject2`](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md)

## Description

Defines a [full authorization context](../../abap-glossary/abencds_own_ac_glosry.md) for a RAP BO. A full authorization context lists one or multiple [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md) which are checked by the implementation methods of the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) itself, by existing code that is called by the ABAP behavior pool implementation, or by [CDS access control](../../abap-glossary/abencds_access_control_glosry.md) defined for the related [RAP BO entities](../../abap-glossary/abenrap_bo_entity_glosry.md) in the data modeling layer. The full authorization context documents the authorization objects used in the implementation of the RAP BO in question. It must be complete and exhaustive.

Three different notation options exist:

- `define own authorization context by privileged mode;`

  When using this option, the authorization context `ContextName` specified after [`with privileged mode disabling ContextName`](abenbdl_privileged_mode.md) is copied to the full authorization context. In other words, the authorization objects which are disabled in [BDEF privileged mode](../../abap-glossary/abenrap_privileged_mode_glosry.md) are automatically reused for the full authorization context. You can use this notation when the full authorization context is identical to the context used for the privileged mode, meaning when privileged mode disables all authorization objects without exception.

- `define own authorization context by privileged mode and {...}`

  This syntax variant copies all authorization objects which are disabled in BDEF privileged mode and it allows you to specify further authorization objects `AuthObject1, AuthObject2, ...` after `and` for the full authorization context.

- `define own authorization context {...}`

  When using this option, you must individually list all authorization objects `AuthObject1`, `AuthObject2`, .... that are checked in the ABAP behavior pool. This syntax variant is useful for a BDEF without privileged mode.

A full authorization context may be defined before, between, or after the [entity behavior definitions](../../abap-glossary/abencds_entity_bdef_glosry.md). It is possible to define an empty full authorization context `define own authorization context { ... }`. One RAP behavior definition can have no more than one full authorization context.

**Dependency**

All authorization objects listed in a full authorization context which are allowed in a privileged authorization context as per their configuration must be listed in a privileged context. Otherwise, a syntax check warning occurs.

## Availability

- [Managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- [Projection BDEF](../../abap-glossary/abenrap_projection_bo_glosry.md): A projection BDEF can define a full authorization context independently of the projected BDEF. This means that a full authorization context can be defined in the projection layer even if the projected entity does not have a full authorization context.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following managed BDEF defines three authorization contexts:

- `ac_2`

- `ac_priv`

- A full authorization context

`with privileged mode disabling` disables `ac_priv` and the full authorization context reuses the authorization objects listed in `ac_priv`. It adds one further authorization object to the full authorization context.

**Note:** This example is intentionally kept short and simple and serves demonstration purposes only. The [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR INSTANCE AUTHORIZATION`](../abap-for-rap-business-objects/abaphandler_meth_auth.md) is not implemented here. In a real-life scenario, the authorization objects from the full authorization context would be implemented in this RAP handler method.

``` abap
managed implementation in class bp_demo_rap_own_ac_short unique;
strict(2);

with privileged mode disabling ac_priv;


define behavior for DEMO_RAP_OWN_AC_SHORT alias Root
persistent table demo_dbtab_root
lock master
authorization master ( none )
{
  create;
  update;
  delete;
  field ( readonly ) key_field;
}

define authorization context ac_2
{
  'AUTHOBJ1';
  'AUTHOBJ2';
}

define authorization context ac_priv
{
  'AUTHOBJ3';
}

define own authorization context by privileged mode and
{
  'AUTHOBJ5';
}
```
