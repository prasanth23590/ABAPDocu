---
title: "RAP - with privileged mode"
source_file: abenbdl_privileged_mode.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - BehaviorDefinitionHeader"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - with privileged mode

## Syntax Forms

**BDEF Privileged Mode for Managed and Unmanaged RAP BOs**

``` abap
... 
with privileged mode disabling ContextName; 
 ...
```

**BDEF Privileged Mode for RAP Projection BOs**

``` abap
... 
with privileged mode disabling base context 
  [and ContextName]; 
 ...
```

**BDEF Privileged Mode for RAP Interface Behavior Definitions**

``` abap
... 
with privileged mode; 
 ...
```

### Alternative

[1. `with privileged mode disabling ContextName`](abenbdl_privileged_mode.md#alternative-1)

[2. `with privileged mode disabling base context [and]`](abenbdl_privileged_mode.md#alternative-2)

[3. `with privileged mode`](abenbdl_privileged_mode.md#alternative-3)

## Overview

### Description

Enables the [BDEF privileged mode](../../abap-glossary/abenrap_privileged_mode_glosry.md) for a RAP BO. With BDEF privileged mode, [RAP BO consumers](../../abap-glossary/abenrap_bo_consumer_glosry.md) can circumvent [authorization checks](../../abap-glossary/abenauthorization_check_glosry.md), such as&#x00A0; [RAP authorization control](../../abap-glossary/abenrap_auth_control_glosry.md). BDEF privileged mode is prerequisite to use the addition [`PRIVILEGED`](../abap-for-rap-business-objects/abapeml_privileged.md) in [EML](../../abap-glossary/abeneml_glosry.md) when consuming the [RAP BO](../../abap-glossary/abenrap_bo_glosry.md). The BDEF privileged mode is available for BDEFs of the types [managed](../../abap-glossary/abenmanaged_rap_bo_glosry.md), [unmanaged](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), [projection](../../abap-glossary/abencds_proj_bdef_glosry.md), and [interface](../../abap-glossary/abenrap_bo_interface_glosry.md). The syntax for the different [BDEF implementation types](../../abap-glossary/abencds_bdef_impl_type_glosry.md) varies. Details are described below.

### Executable Example

The example [Using the addition `PRIVILEGED` with an ABAP EML Statement](../abap-for-rap-business-objects/abeneml_privileged_abexa.md) defines an [authorization context for disable](../../abap-glossary/abencds_auth_context_glosry.md) and registers it for use in privileged mode. It then demonstrates access to the RAP BO, first without the addition `PRIVILEGED`, afterwards using `PRIVILEGED`.

## Alternative 1

`with privileged mode disabling ContextName`

### Description

This syntax variant is available for managed and unmanaged RAP BOs only.

In the [header part of a behavior definition](../../abap-glossary/abencds_bdef_header_glosry.md) of a managed or unmanaged RAP BO, it is possible to specify `with privileged mode disabling ContextName`. The effect is that the [authorization context for disable](../../abap-glossary/abencds_auth_context_glosry.md) `ContextName` is automatically disabled when a [RAP BO consumer](../../abap-glossary/abenrap_bo_consumer_glosry.md) uses [privileged access](../abap-for-rap-business-objects/abapeml_privileged.md) to the [RAP BO](../../abap-glossary/abenrap_bo_glosry.md) in question. `ContextName` must be an authorization context for disable defined in the same BDEF. Not more than one authorization context can be specified.

Example:

`with privileged mode disabling DemoContextBdl`

in the BDEF has the effect that the [EML statement](../../abap-glossary/abenaeml_glosry.md)

``` abap
read entity privileged DemoContextBdl 
   all fields with value #( ( name = field1 ) ) 
   result data(result) 
   failed data(failed).
```

behaved as if

``` abap
authority-check disable begin context DemoContextBdl~privileged context. 
   read entity privileged DemoContextBdl 
   all fields with value #( (name = field1 ) ) 
   result data(result) 
   failed data(failed). 
authority-check disable end.
```

had been written.

So with the syntax `with privileged mode disabling`, the [RAP framework](../../abap-glossary/abenrap_framework_glosry.md) leaves out calls to [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md). No implementation in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is required.

There are other kinds of authority checks, such as [CDS access control](../../abap-glossary/abencds_access_control_glosry.md). If a business object is protected from unauthorized access using any other method than authorization objects, the BDEF can define an empty authorization context that is referred to in `ContextName`.

Example:

BDEF header: `with privileged mode disabling EmptyContext`

BDEF body: `define authorization context EmptyContext { }`

In the case of empty authorization contexts, privileged EML calls are handled as follows:

- In a [managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md), the RAP framework automatically and implicitly checks for other authorizations, such as CDS access control.

- In an [unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md), rules for the handling of a privileged access can be defined in the respective [RAP handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) in the ABAP behavior pool.

### Hints

- The syntax `with privileged mode;` has been deprecated for managed and unmanaged RAP BOs. For compatibility reasons, it can still be used, but it is not recommended and if used, a syntax check warning occurs.

- There are several ways to enable an authorization context for disable. They are described in the topic [RAP - `define authorization context`](abenbdl_def_auth_context.md). One of them is to register an authorization context for a category of [handler method](../../abap-glossary/abenabp_handler_method_glosry.md) using the syntax

  `define authorization context ContextName for disable( Options )` The difference between this and `with privileged mode disabling ContextName` is that in the first case, the context is active *within* the handler method. In the latter case, the context is active *around* the EML statement and that means it is also active during calls to the handler method that might be performed by the RAP framework implicitly before calling the actual handler targeted by the EML statement.

## Alternative 2

`with privileged mode disabling base context`

### Description

This syntax variant is available for [projection BDEFs](../../abap-glossary/abencds_proj_bdef_glosry.md) only. It enables BDEF privileged mode for a [projection BDEF](../../abap-glossary/abencds_proj_bdef_glosry.md). As a prerequisite, the underlying [projected BDEF](../../abap-glossary/abenrap_projection_bo_glosry.md) must define privileged mode. The syntax for enabling privileged mode in a projection BDEF is as follows:

``` abap
with privileged mode disabling base context 
  [and ContextName]
```

`base context` refers to the [authorization context for disable](abenbdl_def_auth_context.md) that is specified in the projected BDEF. It is mandatory to reuse the authorization context from the projected BDEF.

If the projected BDEF specifies an empty authorization context, this can also be reused by the projection BDEF.

With the optional addition `and ContextName`, it is possible to specify an additional authorization context for disable in the projection BDEF. `ContextName` must be an authorization context for disable defined in the same projection BDEF. For all [privileged](../abap-for-rap-business-objects/abapeml_privileged.md) operations on the projection BDEF, both the authorization context of the projected BDEF and the context of the projection BDEF are disabled.

### Hint

Privileged mode can only be reused in a projection BDEF if the syntax `with privileged mode disabling ContextName` is specified in the projected BDEF. If the projected BDEF uses the deprecated syntax form `with privileged mode;`, then BDEF privileged mode is not available in the projection BO.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following example shows a projection BDEF based on the projected BDEF `DEMO_RAP_AUTH_CONTEXT`. It enables privileged mode, reuses the authorization context for disable from the projected BDEF and adds one further authorization context to the projection layer.

**Note:** This example is intentionally kept short and simple and serves demonstration purposes only. The [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md) is not implemented here. In a real-life scenario, `AUTHOBJ1` would be implemented in the [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md).

``` abap
projection implementation in class BP_DEMO_RAP_AUTH_CONTEXT_PROJ unique;
strict(2);
with privileged mode disabling base context and ac_3;

define authorization context ac_3
{
'AUTHOBJ1' ;
}

define behavior for DEMO_RAP_AUTH_CONTEXT_PROJ
{
  use create;
  use update;
  use delete;
}

define own authorization context by privileged mode;
```

## Alternative 3

`with privileged mode`

### Description

This syntax variant is available for [interface BDEFs](../../abap-glossary/abenrap_bo_interface_glosry.md) only. It enables BDEF privileged mode for an interface BDEF, so that access with [EML](../../abap-glossary/abenabap_eml_glosry.md) can take place in privileged mode using the addition [`PRIVILEGED`](../abap-for-rap-business-objects/abapeml_privileged.md). Since interface BDEFs cannot define any access restrictions or authorization contexts themselves, it is a prerequisite that the underlying [projected BDEF](../../abap-glossary/abenrap_projection_bo_glosry.md) defines privileged mode. A privileged access is then delegated to the implementation of the underlying base RAP BO. The syntax for enabling privileged mode in an interface BDEF is as follows:

`with privileged mode;`

### Hint

Privileged mode can only be reused in an interface BDEF if the syntax `with privileged mode disabling ContextName` is specified in the projected BDEF.
