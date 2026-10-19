---
title: "RAP - define authorization context"
source_file: abenbdl_def_auth_context.html
section: "ABAP RAP Business Objects > RAP - Behavior Definitions > RAP - BDL for Behavior Definitions > RAP - Managed and Unmanaged Behavior Definitions > RAP - AuthorizationContext"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# RAP - define authorization context

## Syntax

``` abap
define authorization context ContextName 
      [{for disable( modify 
                    | read 
                    | determination 
                    | validation 
                    | save:early 
                    | save:late)}] 
 
{ 
   AuthObject1; 
  [AuthObject2;] 
  [...] 
}  
```

[`AuthObject1`](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md) · [`AuthObject2`](../../abap-programming-language/abap-authorizations/abenbc_authority_check.md)

### Addition

[1. `... for disable( Options ) ...`](abenbdl_def_auth_context.md#addition-1)

## Overview

### Description

A [RAP behavior definition](../../abap-glossary/abencds_behavior_definition_glosry.md) can define [authorization contexts for disable](../../abap-glossary/abencds_auth_context_glosry.md) using the statement `define authorization context`. Authorization contexts for disable list multiple [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md) that are used for the ABAP statement [`AUTHORITY-CHECK OBJECT`](../../abap-programming-language/abap-authorizations/abapauthority-check.md). When an authorization context for disable is activated, authority checks for all associated authorization objects are always successful; in other words, the respective authorization checks are skipped. This can be useful, for example, when a BDEF implements its own [authorization check](abenbdl_authorization.md) and then calls existing code, which again has its own authorization checks.

One RAP behavior definition can define one or more authorization contexts for disable. The contexts may be defined before, between, or after the entity behavior definitions. Each context can contain one or more [authorization objects](../../abap-glossary/abenauthorization_object_glosry.md) `AuthObject1`, `AuthObject2`, .... It is also possible to define an empty authorization context for disable. This can be useful when using [BDEF privileged mode](abenbdl_privileged_mode.md): to enable BDEF privileged mode, it is mandatory to specify at least one authorization context for disable. However, some RAP BOs use authority checks that do not rely on authorization objects. In this case, an empty authorization context for disable can be specified.

The optional addition `for disable( Options )` activates the authorization context for disable in question for certain [saver](../../abap-glossary/abenabp_saver_method_glosry.md) or [handler methods](../../abap-glossary/abenabp_handler_method_glosry.md). For details, see *Addition 1* below.

**Activating an Authorization Context for Disable**

An authorization context for disable can be activated and the corresponding authorization objects skipped in the following ways:

- By registering a context for use in privileged mode using the syntax statement [`with privileged mode disabling ContextName`](abenbdl_privileged_mode.md).

- By registering a context for a category of saver or handler method using the optional addition `for disable( Options )`, as described under *Addition 1* below.

## Availability

The following list shows the availability of the statement `define authorization context ContextName { ... }`. If the optional addition `for disable( Options )` is used, special rules apply. These rules are described under *Addition 1* below.

An authorization context for disable, without the addition `for disable( Options )`, can be specified in the following [BDEF implementation types](../../abap-glossary/abencds_bdef_impl_type_glosry.md):

- [Managed RAP BO](../../abap-glossary/abenmanaged_rap_bo_glosry.md)

- [Unmanaged RAP BO](../../abap-glossary/abenunmanaged_rap_bo_glosry.md)

- [Projection BDEF](../../abap-glossary/abenrap_projection_bo_glosry.md): A projection BDEF can define an authorization context for disable independently of the projected BDEF. This means that an authorization context for disable can be defined in the projection layer even if the projected entity does not have an authorization context for disable.

**Dependency**

If you define and activate an authorization context for disable which lists authorization objects (that means, it is not empty), you also need to specify a [RAP full authorization context](../../abap-glossary/abencds_own_ac_glosry.md) that lists all mentioned authorization objects, unless they are forbidden for use in full authorization contexts as per their classification. Otherwise, syntax check warnings occur. Further details are described in topic [RAP - `define own authorization context`](abenbdl_def_own_auth_context.md).

### Hint

The optional registration of an authorization context for a dedicated purpose using the syntax `for disable( ... )` does **not** generate an `AUTHORITY-CHECK DISABLE BEGIN CONTEXT` ... `AUTHORITY-CHECK DISABLE END` bracket within saver or handler methods that are introduced by [BDEF extensions](abenbdl_extension.md). The optional addition `for disable` has an effect only in the base BDEF implementation, but not in BDEF extensions.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following managed BDEF defines two authorization contexts for disable: `ac1` and `ac2` with the addition `for disable`. A full authorization context which lists all objects from `ac_1` is also required.

**Note:** This example is intentionally kept short and simple and serves demonstration purposes only. The [RAP handler method](../../abap-glossary/abenabp_handler_method_glosry.md) [`FOR GLOBAL AUTHORIZATION`](../abap-for-rap-business-objects/abaphandler_meth_global_auth.md) is not implemented here. In a real-life scenario, the authorization objects from the full authorization context would be implemented in this RAP handler method.

``` abap
managed implementation in class bp_demo_rap_auth_context unique;
strict ( 2 );

with privileged mode disabling ac_1;

define authorization context ac_1
{
  'AUTHOBJ1';
  'AUTHOBJ2';
  'AUTHOBJ3';
}

define authorization context ac_2
for disable ( modify, read ) ##warn_OK
{
  'AUTHOBJ4';
}

define own authorization context by privileged mode;

define behavior for DEMO_RAP_AUTH_CONTEXT alias Root
persistent table demo_dbtab_root
lock master
authorization master ( none )

{
  create;
  update;
  delete;
  association _child { create; }
  field ( readonly : update ) KeyField;
  mapping for demo_dbtab_root
    {
      KeyField   = key_field;
      DataField  = data_field;
      CharField  = char_field;
      CharField2 = char_field_2;
      DecField   = dec_field;
    }
}

define behavior for DEMO_RAP_AUTH_CONTEXT_CHILD alias Child
persistent table demo_dbtab_child
lock dependent by _parent
authorization dependent by _parent

{
  update;
  delete;
  field ( readonly ) KeyField;
  field ( readonly : update ) KeyFieldChild;
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

### Executable Example

The example [Using the addition `PRIVILEGED` with an ABAP EML Statement](../abap-for-rap-business-objects/abeneml_privileged_abexa.md) defines an authorization context and registers it for use in privileged mode. It then demonstrates access to the RAP BO, first without the addition `PRIVILEGED`, afterwards with using `PRIVILEGED`.

## Addition 1

`... for disable( Options ) ...`

### Description

The optional addition `for disable( Options )` activates the authorization context for disable in question for certain saver or handler methods. When a context is activated, then the corresponding methods automatically and implicitly skip the authorization objects listed in the associated authorization context.

Example:

``` abap
define authorization context ReadContext 
  for disable (read) 
...
```

in the BDEF has the effect that

``` abap
METHOD read FOR READ [....] 
... 
ENDMETHOD.
```

in the ABAP behavior pool behaves as if the code was

``` abap
METHOD read FOR READ [....]. 
AUTHORITY-CHECK DISABLE BEGIN CONTEXT demo_context~ReadContext. 
... 
AUTHORITY-CHECK DISABLE END. 
ENDMETHOD.
```

The following options `Options` can be specified after `for disable` in brackets `( ... )`:

- `modify`

  - Available for managed and unmanaged RAP BOs.

  - The RAP handler methods [`FOR MODIFY`](../abap-for-rap-business-objects/abaphandler_meth_modify.md) automatically skip the authorization objects listed in the associated authorization context `ContextName`.

- `read`

  - Available for managed and unmanaged RAP BOs.

  - The RAP handler methods [`FOR READ`](../abap-for-rap-business-objects/abaphandler_meth_read.md) automatically skip the authorization objects listed in the associated authorization context `ContextName`.

- `determination`

  - Available only for the [BDEF implementation type](../../abap-glossary/abencds_bdef_impl_type_glosry.md) `managed`.

  - The [determinations](abenbdl_determinations.md) that are invoked during the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md) automatically skip the authorization objects listed in the associated authorization context `ContextName`.

- `validation`

  - Available only for the implementation type `managed`.

  - The [validations](abenbdl_validations.md) that are invoked during the save sequence automatically skip the authorization objects listed in the associated authorization context `ContextName`.

- `save:early`

  - Available only for the [BDEF implementation type](../../abap-glossary/abencds_bdef_impl_type_glosry.md) `unmanaged`.

  - The RAP saver methods [`finalize`](../abap-for-rap-business-objects/abensaver_finalize.md) and [`check_before_save`](../abap-for-rap-business-objects/abensaver_check_before_save.md) of the [early save phase](../../abap-glossary/abenearly_rap_save_phase_glosry.md) automatically skip the authorization objects listed in the associated authorization context `ContextName`.

- `save:late`

  - Available for managed and unmanaged RAP BOs.

  - The RAP saver methods [`adjust_numbers`](../abap-for-rap-business-objects/abensaver_adjust_numbers.md), [`save`](../abap-for-rap-business-objects/abensaver_method_save.md), and [`save_modified`](../abap-for-rap-business-objects/abaprap_saver_meth_save_modified.md) of the [late save phase](../../abap-glossary/abenlate_rap_save_phase_glosry.md) automatically skip the authorization objects listed in the associated authorization context `ContextName`.

It is possible to specify one or more options `Options` within the brackets, divided a commas. Each option can only be assigned once within a RAP behavior definition.

## Restrictions

While an authorization context for disable can be specified in BDEF extensions, the optional addition `for disable( Options )` is not available in BDEF extensions. For details, see the topic [RAP - `extension`](abenbdl_extension_syntax.md).
