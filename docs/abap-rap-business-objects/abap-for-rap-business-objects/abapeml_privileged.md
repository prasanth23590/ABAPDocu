---
title: "ABAP EML - PRIVILEGED"
source_file: abapeml_privileged.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Consuming RAP Business Objects > ABAP EML - Consuming RAP BOs > ABAP EML - Common EML Statements and Operands"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP EML - PRIVILEGED

## Syntax Forms

**Short Forms of ABAP EML Statements**

``` abap
1. MODIFY ENTITY [FORWARDING] PRIVILEGED bdef ...
   READ ENTITY [FORWARDING] PRIVILEGED bdef ...
   GET PERMISSIONS [FORWARDING] PRIVILEGED ... ENTITY bdef ...
```

**Long Forms of ABAP EML Statements**

``` abap
2. MODIFY ENTITIES OF bdef [FORWARDING] PRIVILEGED ENTITY ...
   READ ENTITIES OF bdef [FORWARDING] PRIVILEGED ENTITY ...
   GET PERMISSIONS [FORWARDING] PRIVILEGED ... OF bdef ENTITY ...
```

**Dynamic Forms of ABAP EML Statements**

``` abap
3. MODIFY ENTITIES [FORWARDING] PRIVILEGED OPERATIONS ...
   READ ENTITIES [FORWARDING] PRIVILEGED OPERATIONS ...
   GET PERMISSIONS [FORWARDING] PRIVILEGED ... OPERATIONS ...
```

[`MODIFY ENTITY [FORWARDING] PRIVILEGED bdef ...`](abapmodify_entity_short.md) · [`READ ENTITY [FORWARDING] PRIVILEGED bdef ...`](abapread_entity_short.md) · [`GET PERMISSIONS [FORWARDING] PRIVILEGED ... ENTITY bdef ...`](abapget_permissions_short.md) · [`MODIFY ENTITIES OF bdef [FORWARDING] PRIVILEGED ENTITY ...`](abapmodify_entities_long.md) · [`READ ENTITIES OF bdef [FORWARDING] PRIVILEGED ENTITY ...`](abapread_entities_long.md) · [`GET PERMISSIONS [FORWARDING] PRIVILEGED ... OF bdef ENTITY ...`](abapget_permissions_long.md) · [`MODIFY ENTITIES [FORWARDING] PRIVILEGED OPERATIONS ...`](abapmodify_entities_operations_dyn.md) · [`READ ENTITIES [FORWARDING] PRIVILEGED OPERATIONS ...`](abapread_entities_operations.md) · [`GET PERMISSIONS [FORWARDING] PRIVILEGED ... OPERATIONS ...`](abapget_permissions_dyn.md)

### Alternative

[1. `... PRIVILEGED ...`](abapeml_privileged.md#alternative-1)

[2. `... FORWARDING PRIVILEGED ...`](abapeml_privileged.md#alternative-2)

## Overview

### Description

The statements allow privileged access to [RAP business objects](../../abap-glossary/abenrap_bo_glosry.md). They can only be used if the [RAP BO entity](../../abap-glossary/abenrap_bo_entity_glosry.md) is defined with `with privileged mode ...`. Refer to the RAP BDL specification [`with privileged mode`](../rap-behavior-definitions/abenbdl_privileged_mode.md) for more details.

The `PRIVILEGED` and `FORWARDING PRIVILEGED` additions are currently possible for the `READ`, `MODIFY`, and `GET PERMISSIONS` ABAP EML statements.

## Alternative 1

`... PRIVILEGED ...`

### Description

The `PRIVILEGED` addition is used for a privileged access to a [RAP business object](../../abap-glossary/abenrap_bo_glosry.md), allowing bypassing authority checks.

### Hint

You can use the method `get_current_context` of class `CL_ABAP_BEHV_AUX` to obtain context information. Among others, you can determine if the running handler is running in privileged mode, e. g. as follows:

` cl_abap_behv_aux=>get_current_context( IMPORTING privileged = FINAL(priv) ).`

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following ABAP EML modify request shows the use of the `PRIVILEGED` addition.

``` abap
MODIFY ENTITY PRIVILEGED demo_managed_privileged 
  EXECUTE forwarding_privileged 
  FROM ... 
  FAILED FINAL(f2) 
  REPORTED FINAL(r2).
```

## Alternative 2

`... FORWARDING PRIVILEGED ...`

### Description

The addition has the effect of forwarding privileged access, i.e. if an ABAP EML request is performed in a privileged context, you can pass on the privileged context and therefore retain the privileged context in subsequent ABAP EML requests, which is, for example, valid if another behavior implementation is called inside a behavior implementation.

### Hints

- The use of `FORWARDING PRIVILEGED` will have no effect if the targeted RAP BO entity is not defined with `with privileged mode`.

- A syntax warning occurs if ABAP EML requests on external RAP BO entities are used inside a behavior implementation without the additions `PRIVILEGED` or `FORWARDING PRIVILEGED`. You can remove the warning using the pragma `##NO_PRIVILEGED`. The warning does not occur when used with dynamic statements as it cannot be determined which entity the request refers to.

- Statements with the `FORWARDING PRIVILEGED` addition are a shorter form of first querying the privileged context using the `GET_CURRENT_CONTEXT` method of the `CL_ABAP_BEHV_AUX` class, and then perform an ABAP EML request with or without the `PRIVILEGED` addition based on the value of the `privileged` parameter.

- Specifying the `FORWARDING PRIVILEGED` addition results in the following effect: When a RAP BO is called with privileged access, subsequent ABAP EML requests that specify [`IN LOCAL MODE`](abapin_local_mode.md) retain this access. Eventually, an ABAP EML request with the `FORWARDING PRIVILEGED` addition triggers the calling of another RAP BO. In such a case, the original privileged access is forwarded, and intermediate ABAP EML requests with `IN LOCAL MODE` also retain this privileged access.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The first statement in the following example shows an ABAP EML modify request with the `FORWARDING PRIVILEGED` addition. It is followed by an ABAP EML modify request with the `PRIVILEGED` addition and a prior call of the `GET_CURRENT_CONTEXT` method of the `CL_ABAP_BEHV_AUX` class.

``` abap
MODIFY ENTITY FORWARDING PRIVILEGED demo_managed_privileged_t 
  EXECUTE act 
  FROM ... 
  FAILED FINAL(f) 
  REPORTED FINAL(r). 
 
"The following statement has basically the same semantics as the 
"previous statement. 
cl_abap_behv_aux=>get_current_context( 
         IMPORTING privileged = FINAL(priv) ). 
 
    IF priv = abap_true. 
      MODIFY ENTITY PRIVILEGED demo_managed_privileged_t 
       EXECUTE act 
       FROM ... 
       FAILED FINAL(f1) 
       REPORTED FINAL(r1). 
    ELSE. 
      MODIFY ENTITY demo_managed_privileged_t ##NO_PRIVILEGED 
       EXECUTE act 
       FROM ... 
       FAILED FINAL(f2) 
     REPORTED FINAL(r2). 
    ENDIF.
```

## Executable Examples

- The example [Using the `PRIVILEGED` Addition with an ABAP EML Statement](abeneml_privileged_abexa.md) demonstrates the addition `PRIVILEGED` using an [action](../../abap-glossary/abenrap_action_glosry.md) and a managed [RAP BO](../../abap-glossary/abenrap_bo_glosry.md).

- The example [Using the `FORWARDING PRIVILEGED` Addition with an ABAP EML Statement](abeneml_forwarding_priv_abexa.md) demonstrates ABAP EML `MODIFY` statements executing [actions](../../abap-glossary/abenrap_action_glosry.md) with the addition `FORWARDING PRIVILEGED` using a managed RAP BO.
