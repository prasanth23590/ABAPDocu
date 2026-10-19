---
title: "FOR GLOBAL FEATURES, RAP Handler Method"
source_file: abaphandler_meth_global_features.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Handler Classes and Methods > METHODS, FOR, RAP Handler Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR GLOBAL FEATURES, RAP Handler Method

## Syntax

``` abap
**Handler method definition:**

METHODS meth [FINAL] 
   FOR GLOBAL FEATURES 
   [IMPORTING  ] REQUEST { REFERENCE  (req_gl_feat) | req_gl_feat } 
   FOR bdef 
   RESULT { REFERENCE  (res_gl_feat) | res_gl_feat } 
   [CHANGING   reported   TYPE data  ].  
```

[`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapmethods_abstract_final.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`CHANGING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`data `](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md)

## Description

[Handler method](../../abap-glossary/abenabp_handler_method_glosry.md) that is used for the [global feature control](../rap-behavior-definitions/abenbdl_actions_fc.md) of [RAP BO entities](../../abap-glossary/abenrap_bo_entity_glosry.md). It must be defined and implemented in a [handler class](../../abap-glossary/abenabp_handler_class_glosry.md) of an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). The method name `meth` can be chosen freely. `bdef` is the name or the alias of the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md).

**Method Parameters**

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - `req_gl_feat`: Request parameter on which the information retrieval for global feature control is based on. It is a structure of type [`TYPE STRUCTURE FOR GLOBAL FEATURES REQUEST bdef`](abaptype_structure_for.md).

    The parameter can also be passed by reference (see [`REFERENCE`](../../abap-programming-language/abap-declarations/abapmethods_parameters.md)). The use of the ABAP word `IMPORTING` is optional.

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - `res_gl_feat`: Used to store the result of the information retrieval. It is a structure of type [`TYPE STRUCTURE FOR GLOBAL FEATURES RESULT bdef`](abaptype_structure_for.md). The parameter can also be passed by reference.

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter `reported` ([RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md)) is implicitly available. It is possible to specify the parameter with the predefined name `reported` explicitly following the ABAP word `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameter implicitly has the BDEF derived type [`TYPE RESPONSE FOR REPORTED`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR REPORTED` can be specified.

**BDEF Requirements**

See the required BDEF notations for both variants in the topic [RAP - `feature control`](../rap-behavior-definitions/abenbdl_actions_fc.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Example for a RAP handler method definition. Find a demonstration of a method implementation in the executable example further down.

``` abap
... 
METHODS get_global_features FOR GLOBAL FEATURES 
    IMPORTING REQUEST requested_features FOR bdef RESULT result. 
...
```

## Executable Example

[Example for RAP Handler Methods](abenrap_handler_methods_abexa.md): Demonstrates this RAP handler method within a RAP handler class using a simple unmanaged RAP BO that is draft-enabled.
