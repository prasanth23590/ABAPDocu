---
title: "FOR INSTANCE FEATURES, FEATURES, RAP Handler Method"
source_file: abaphandler_meth_features.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Handler Classes and Methods > METHODS, FOR, RAP Handler Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR INSTANCE FEATURES, FEATURES, RAP Handler Method

## Syntax

``` abap
**Handler method definition:**

METHODS meth [FINAL] 
   FOR [INSTANCE] FEATURES 
   [IMPORTING  ] { REFERENCE  (im_par_feat) | im_par_feat } 
   REQUEST { REFERENCE  (req_feat) | req_feat } 
   FOR bdef 
   RESULT { REFERENCE  (res_feat) | res_feat } 
  [CHANGING   { [failed   TYPE data  ] [reported   TYPE data  ] }].  
```

[`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapmethods_abstract_final.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`CHANGING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`data `](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) · [`data `](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md)

## Description

[Handler method](../../abap-glossary/abenabp_handler_method_glosry.md) that is used for the [instance-based feature control](../rap-behavior-definitions/abenbdl_actions_fc.md). It must be defined and implemented in a [handler class](../../abap-glossary/abenabp_handler_class_glosry.md) of an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). The method name `meth` can be chosen freely. `bdef` is the name or the alias of the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md). The ABAP word `INSTANCE` is optional.

**Method Parameters**

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - `im_par_feat`: Internal table of type [`TYPE TABLE FOR INSTANCE FEATURES KEY`](abaptype_table_for.md).

    The importing parameter can also be passed by reference (see [`REFERENCE`](../../abap-programming-language/abap-declarations/abapmethods_parameters.md)). The use of the ABAP word `IMPORTING` is optional.

  - `req_feat`: Request parameter on which the information retrieval for instance-based feature control is based on. It is a structure of type [`TYPE STRUCTURE FOR INSTANCE FEATURES REQUEST`](abaptype_structure_for.md). The parameter can also be passed by reference.

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - `res_feat`: Used to store the result of the information retrieval. It is an internal table of type [`TYPE TABLE FOR INSTANCE FEATURES RESULT`](abaptype_table_for.md). The parameter can also be passed by reference.

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed` and `reported` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed` and `reported` explicitly following the ABAP word `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

**BDEF Requirements**

See the required BDEF notations for both variants in the topic [RAP - `feature control`](../rap-behavior-definitions/abenbdl_actions_fc.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Examples for RAP handler method definitions. Find demonstrations of method implementations in the executable examples further down.

``` abap
... 
METHODS get_instance_features FOR INSTANCE FEATURES 
    IMPORTING keys REQUEST requested_features FOR bdef 
    RESULT result. 
 
METHODS get_instance_features FOR FEATURES 
    keys REQUEST requested_authorizations FOR bdef RESULT result 
    CHANGING failed TYPE DATA reported TYPE DATA. 
...
```

## Executable Example

[Example for RAP Handler Methods](abenrap_handler_methods_abexa.md): Demonstrates this RAP handler method within a RAP handler class using a simple unmanaged RAP BO that is draft-enabled.
