---
title: "RAP - extend own authorization context"
source_file: abenbdl_extend_own_auth_context.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - BDEF Extension > RAP - Base BDEF Extension > RAP - extension"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - extend own authorization context

## Syntax

``` abap
extend own authorization context 
{ 
  [AuthObject1;] 
  [AuthObject2;] 
  [...] 
}  
```

[`AuthObject1`](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md) · [`AuthObject2`](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md)

## Description

Extends a [full authorization context](../../abap-glossary/abencds_own_ac_glosry.md) using the statement `extend own authorization context` by adding further [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md) `AuthObject1`, `AuthObject2`, ... to the context. If the original BDEF defines a full authorization context and the extension implementation uses authorization objects which are not used in the original implementation, you should extend the full authorization context to ensure a complete and exhaustive list. Like for the original BDEF, the full authorization context is evaluated by certain contract checks and if it is not complete, a runtime error occurs.

As a prerequisite, the original BDEF must define a full authorization context. If this is the case, the full authorization context can be extended without any explicit extensibility enabling. If the original BDEF does not define a full authorization context, it must not be added via an extension.

An extension full authorization context may be defined before, between, or after the other [components of an extension BDEF](abenbdl_extensibility_managed_unm.md). It is also possible to define an empty own authorization context.

For details on the concept of an own authorization context, see the topic [RAP - `define own authorization context`](abenbdl_def_own_auth_context.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following BDEF extension `DEMO_RAP_EXT_AUTH_CONTEXT` extends the RAP behavior definition `DEMO_RAP_OWN_AUTH_CONTEXT`. It adds one further authorization object to the context.

**Note:** This example is intentionally kept short and simple and serves demonstration purposes only. The [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) of the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) are not implemented here. In a real-life scenario, `AUTHOBJ5` would be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md).

``` abap
extension implementation in class bp_demo_rap_ext_auth_context unique;

extend own authorization context
{ 'AUTHOBJ5'; }
```
