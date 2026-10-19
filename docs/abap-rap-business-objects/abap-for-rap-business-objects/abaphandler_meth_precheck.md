---
title: "FOR PRECHECK, RAP Handler Method"
source_file: abaphandler_meth_precheck.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Handler Classes and Methods > METHODS, FOR, RAP Handler Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR PRECHECK, RAP Handler Method

## Syntax

``` abap
**Handler method definitions:**

METHODS meth [FINAL] 
   FOR PRECHECK 
   [IMPORTING  ] { REFERENCE  (im_par_pre) | im_par_pre } 
   FOR { CREATE bdef } 
     | { CREATE bdef\_assoc } 
     | { UPDATE bdef } 
     | { DELETE bdef } 
     | { ACTION bdef~action 
         [REQUEST { REFERENCE  (req_act_pre) | req_act_pre } ] } 
   [CHANGING   { [failed   TYPE data  ] [reported   TYPE data  ] }].  
```

[`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapmethods_abstract_final.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`CHANGING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`data `](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) · [`data `](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md)

### Variant

[1. `... CREATE bdef ...`](abaphandler_meth_precheck.md#variant-1)

[2. `... CREATE bdef\_assoc ...`](abaphandler_meth_precheck.md#variant-2)

[3. `... UPDATE ...`](abaphandler_meth_precheck.md#variant-3)

[4. `... DELETE ...`](abaphandler_meth_precheck.md#variant-4)

[5. `... ACTION bdef~action ...`](abaphandler_meth_precheck.md#variant-5)

### Addition

[1. `... REQUEST ...`](abaphandler_meth_precheck.md#addition-1)

[2. `... CHANGING ...`](abaphandler_meth_precheck.md#addition-2)

## Overview

### Description

[Handler method](../../abap-glossary/abenabp_handler_method_glosry.md) that is used for the [precheck](../rap-behavior-definitions/abenbdl_precheck.md). It must be defined and implemented in a [handler class](../../abap-glossary/abenabp_handler_class_glosry.md) of an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). The method name `meth` can be chosen freely. `bdef` is the name or the alias of the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md), `assoc` the name of the association, and `action` the name of the action.

See the required BDEF notations in the following topic: [RAP BDL - precheck](../rap-behavior-definitions/abenbdl_precheck.md).

## Variant 1

`... CREATE bdef ...`

### Description

Handles the precheck for [create operations](../rap-behavior-definitions/abenbdl_standard_operations.md).

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_pre`: Includes the entities to be created. It is an internal table of type [`TYPE TABLE FOR CREATE bdef`](abaptype_table_for.md). The parameter can also be passed by reference (see [`REFERENCE`](../../abap-programming-language/abap-declarations/abapmethods_parameters.md)).

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed` and `reported` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed` and `reported` explicitly following the ABAP word `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Variant 2

`... CREATE bdef\_assoc ...`

### Description

Handles the precheck for [create-by-association operations](../rap-behavior-definitions/abenbdl_association.md).

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_pre`: Includes the entities to be created. It is an internal table of type [`TYPE TABLE FOR CREATE bdef\_assoc`](abaptype_table_for.md). The parameter can also be passed by reference (see [`REFERENCE`](../../abap-programming-language/abap-declarations/abapmethods_parameters.md)).

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed` and `reported` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed` and `reported` explicitly following the ABAP word `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Variant 3

`... UPDATE bdef ...`

### Description

Handles the precheck for [update operations](../rap-behavior-definitions/abenbdl_standard_operations.md).

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_pre`: Includes the entities to be updated. It is an internal table of type [`TYPE TABLE FOR UPDATE bdef`](abaptype_table_for.md). The parameter can also be passed by reference (see [`REFERENCE`](../../abap-programming-language/abap-declarations/abapmethods_parameters.md)).

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed` and `reported` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed` and `reported` explicitly following the ABAP word `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Variant 4

`... DELETE bdef ...`

### Description

Handles the precheck for [delete operations](../rap-behavior-definitions/abenbdl_standard_operations.md).

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_pre`: Includes the keys of the entities to be deleted. It is an internal table of type [`TYPE TABLE FOR DELETE bdef`](abaptype_table_for.md). The parameter can also be passed by reference (see [`REFERENCE`](../../abap-programming-language/abap-declarations/abapmethods_parameters.md)).

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed` and `reported` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed` and `reported` explicitly following the ABAP word `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Variant 5

`... ACTION bdef~action ...`

### Description

Handles the precheck for [actions](../rap-behavior-definitions/abenbdl_action.md).

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_pre`: Includes the keys of the entities for which the action should be processed. It is an internal table of type [`TYPE TABLE FOR ACTION IMPORT bdef~action`](abaptype_table_for.md). The parameter can also be passed by reference (see [`REFERENCE`](../../abap-programming-language/abap-declarations/abapmethods_parameters.md)).

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed` and `reported` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed` and `reported` explicitly following the ABAP word `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Addition 1

`... REQUEST ...`

### Description

The addition and the parameter `req_act_pre` are only available in the context of actions that are specified with a parameter in the BDEF.

`req_act_pre` is an importing parameter and specifies Request parameter on which the information retrieval ... is based on. It is a structure of type [`TYPE STRUCTURE FOR ACTION REQUEST bdef`](abaptype_structure_for.md).

## Addition 2

`... CHANGING ...`

### Description

See the details regarding the RAP response parameters that can be specified above.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Examples for RAP handler method definitions. Find demonstrations of method implementations in the executable examples further down.

``` abap
... 
METHODS precheck_create FOR PRECHECK 
    IMPORTING entities FOR CREATE bdef. 
 
METHODS precheck_cba_assoc FOR PRECHECK 
    IMPORTING entities_cba FOR CREATE bdef\_assoc. 
 
METHODS precheck_update FOR PRECHECK 
    IMPORTING entities FOR UPDATE bdef. 
 
METHODS precheck_delete FOR PRECHECK 
    IMPORTING keys FOR DELETE bdef. 
 
METHODS precheck_action FOR PRECHECK 
    IMPORTING entities FOR CREATE bdef~action. 
...
```

## More Information

Development guide for the ABAP RESTful Application Programming Model, section [Operation Precheck](https://help.sap.com/docs/ABAP_Cloud/f055b8bf582d4f34b91da667bc1fcce6/f6e3880b641649b1b8247486579a1c9b?version=sap_cross_product_abap).

### Executable Example

[Example for RAP Handler Methods](abenrap_handler_methods_abexa.md): Demonstrates this RAP handler method for an action within a RAP handler class using a simple unmanaged RAP BO that is draft-enabled.
