---
title: "FOR GLOBAL AUTHORIZATION, RAP Handler Method"
source_file: abaphandler_meth_global_auth.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Handler Classes and Methods > METHODS, FOR, RAP Handler Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR GLOBAL AUTHORIZATION, RAP Handler Method

## Syntax

``` abap
**Handler method definition:**

METHODS meth [FINAL] 
   FOR GLOBAL AUTHORIZATION 
   [IMPORTING  ] { REFERENCE  (im_par_gl_auth) | im_par_gl_auth } 
   REQUEST { REFERENCE  (req_gl_auth) | req_gl_auth } 
   FOR bdef 
   RESULT { REFERENCE  (res_gl_auth) | res_gl_auth } 
   [CHANGING   reported   TYPE data  ].  
```

[`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapmethods_abstract_final.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`CHANGING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`data `](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md)

## Description

[Handler method](../../abap-glossary/abenabp_handler_method_glosry.md) that is used for [global authorization](../rap-behavior-definitions/abenbdl_authorization.md) checks for accessing [RAP BO entities](../../abap-glossary/abenrap_bo_entity_glosry.md). It must be defined and implemented in a [handler class](../../abap-glossary/abenabp_handler_class_glosry.md) of an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). The method name `meth` can be chosen freely. `bdef` is the name or the alias of the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md).

**Method Parameters**

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - `req_gl_auth`: Request parameter on which the information retrieval for instance-based authorization is based on. It is a structure of type [`TYPE STRUCTURE FOR GLOBAL AUTHORIZATION REQUEST`](abaptype_structure_for.md).

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - `res_gl_auth`: Used to store the result of the permission information retrieval. It is a structure of type [`TYPE STRUCTURE FOR GLOBAL AUTHORIZATION RESULT`](abaptype_structure_for.md).

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter `reported` ([RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md)) is implicitly available. It is possible to specify the parameter with the predefined name `reported` explicitly following the ABAP word `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameter implicitly has the BDEF derived type [`TYPE RESPONSE FOR REPORTED`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR REPORTED` can be specified.

**BDEF Requirements**

See the required BDEF notations for both variants in the topic [RAP - Authorization](../rap-behavior-definitions/abenbdl_authorization.md).

## Hint

Authorization handler methods should be implemented using [`AUTHORITY-CHECK OBJECT`](../../abap-programming-language/abap-authorizations/abapauthority-check.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Example for a RAP handler method definition. Find demonstrations of method implementations in the executable examples further down.

``` abap
... 
METHODS get_global_authorizations FOR GLOBAL AUTHORIZATION 
    IMPORTING REQUEST requested_authorizations FOR bdef 
    RESULT result. 
...
```

## Executable Examples

- [Example for RAP Handler Methods](abenrap_handler_methods_abexa.md): Demonstrates this RAP handler method within a RAP handler class using a simple unmanaged RAP BO that is draft-enabled.

- [RAP BDL - global authorization](../rap-behavior-definitions/abenbdl_authorization_abexa.md)
