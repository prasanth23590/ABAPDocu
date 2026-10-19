---
title: "RAP - AuthorizationContext"
source_file: abenbdl_authorization_context.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - AuthorizationContext

## Syntax Forms

**[Full Authorization Context](abenbdl_def_own_auth_context.md)**

``` abap
1. define own authorization context by privileged mode; 
 | define own authorization context by privileged mode and 
  {[AuthObject1;] [AuthObject2;] [...]} 
 | define own authorization context 
  {[AuthObject1;] [AuthObject2;] [...]}
```

**[Authorization Context for Disable](abenbdl_def_auth_context.md)**

``` abap
2. define authorization context ContextName 
      [for disable( Options )] 
 
{ 
  [AuthObject1;] 
  [AuthObject2;] 
  [...] 
}
```

[`AuthObject1`](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md) · [`AuthObject2`](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md) · [`AuthObject1`](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md) · [`AuthObject2`](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md) · [`AuthObject1`](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md) · [`AuthObject2`](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md)

## Description

A [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) can define [authorization contexts](../../abap-glossary/abencds_auth_con_glosry.md) that list multiple [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md) that are used for the ABAP statement [`AUTHORITY-CHECK OBJECT`](../../abap-programming-language/abap-authorizations/abapauthority-check.md). There are different types of authorization contexts:

- [Full authorization context](../../abap-glossary/abencds_own_ac_glosry.md)

  - Defined using the statement [`define own authorization context [...]`](abenbdl_def_own_auth_context.md).

  - List of [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md) which are checked by the implementation methods of the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) itself, or by existing code that is called by the ABAP behavior pool implementation. The full authorization context documents the authorization objects used in the implementation of the RAP BO in question. It must be complete and exhaustive. Otherwise, a syntax check warning occurs.

- [Authorization context for disable](../../abap-glossary/abencds_auth_context_glosry.md)

  - Defined using the statement [`define authorization context`](abenbdl_def_auth_context.md).

  - List of [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md). When an authorization context for disable is activated, the [authorization checks](../../abap-glossary/abenauthorization_check_glosry.md) for all associated authorization objects always return the value *authorized*. That means, the respective authorization checks are skipped.

SAP has configured authorization objects to be allowed or forbidden for use in full authorization contexts or authorization contexts for disable. This configuration must be respected. Otherwise, a syntax check warning occurs. When using [strict mode version 2](abenbdl_strict_2.md), a syntax check error occurs.

If the authorization context for disable is used by the syntax [`with privileged mode disabling ContextName`](abenbdl_privileged_mode.md), then it must be ensured that this authorization context for disable does not contradict the full authorization context. This means:

- A full authorization context must be specified that contains all authorization objects of this particular authorization context for disable. Otherwise, a syntax check warning occurs.

- All authorization objects of the full authorization context must be specified in the authorization context for disable in question except for the authorization objects which are forbidden in authorization context for disable as per their classification. Otherwise, a syntax check warning occurs.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following managed BDEF defines three authorization contexts:

- Own authorization context: Lists all authorization objects used by the RAP BO implementation. It is modelled by privileged mode and adds two further authorization objects `AUTHOBJ5` and `AUTHOBJ6`. These two further authorization objects are not included in the own authorization context. This is OK in this case, since they are classified as `not allowed in BDEF privileged mode` by SAP.

- `NoCheckWhenPrivileged`: Lists authorization objects that are skipped by a RAP BO consumer with [privileged access](../abap-for-rap-business-objects/abapeml_privileged.md).

- `NoCheckWhenReadingorModifying`: Lists authorization objects that are skipped by the [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR READ`](../abap-for-rap-business-objects/abaphandler_meth_read.md) and [`FOR MODIFY`](../abap-for-rap-business-objects/abaphandler_meth_modify.md).

In this example, the authorization context `NoCheckWhenPrivileged` contains a subset of authorization objects of the own authorization context. The own authorization context documents all authorization objects that are used by a RAP BO implementation and `NoCheckWhenPrivileged` defines which ones of them are skipped in privileged mode.

**Note:** This example is intentionally kept short and simple and serves demonstration purposes only. The [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR INSTANCE AUTHORIZATION`](../abap-for-rap-business-objects/abaphandler_meth_auth.md) is not implemented here. In a real-life scenario, the authorization objects from the own authorization context would be implemented in this RAP handler method.

``` abap
managed implementation in class bp_demo_rap_own_auth_context unique;
strict ( 2 );
extensible;

with privileged mode disabling NoCheckWhenPrivileged;

define authorization context NoCheckWhenPrivileged
{
  'AUTHOBJ1';
}

define own authorization context by privileged mode and
{
  'AUTHOBJ5';
  'AUTHOBJ6';
}

define authorization context NoCheckWhenReadingorModifying
for disable ( modify, read ) ##warn_OK
{
  'AUTHOBJ4';
}

define behavior for DEMO_RAP_OWN_AUTH_CONTEXT alias Root
persistent table demo_dbtab_root
lock master
authorization master ( none )
extensible
{
  create;
  update;
  delete;
  association _child { create; }
  field ( readonly ) KeyField;

  mapping for demo_dbtab_root corresponding extensible
    {
      KeyField   = key_field;
      DataField  = data_field;
      CharField  = char_field;
      CharField2 = char_field_2;
      DecField   = dec_field;
    }
}

define behavior for DEMO_RAP_OWN_AUTH_CON_CHILD alias Child
persistent table demo_dbtab_child
lock dependent by _parent
authorization dependent by _parent
{
  update;
  delete;
  field ( readonly ) KeyField, KeyFieldChild;
  association _parent;

  mapping for demo_dbtab_child
    {
      KeyField      = key_field;
      KeyFieldChild = key_field_child;
      DataField     = data_field;
      CharField     = char_field;
    }
}
```
