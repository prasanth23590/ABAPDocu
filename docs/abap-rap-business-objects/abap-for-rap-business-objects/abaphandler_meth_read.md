---
title: "FOR READ, RAP Handler Method"
source_file: abaphandler_meth_read.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Handler Classes and Methods > METHODS, FOR, RAP Handler Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR READ, RAP Handler Method

## Syntax

``` abap
**Handler method definitions:**

METHODS meth [FINAL] 
   FOR READ 
   [IMPORTING  ] { REFERENCE  (im_par_read) | im_par_read } 
   FOR { READ bdef RESULT { REFERENCE  (res_read) | res_read } } 
     | { READ bdef\_assoc FULL { REFERENCE  (full_rba) | full_rba } 
                          RESULT { REFERENCE  (res_rba) | res_rba } 
                          LINK { REFERENCE  (link_rba) | link_rba } } 
     | { FUNCTION bdef~function [REQUEST { REFERENCE  (req_func) | req_func }] 
                                 RESULT { REFERENCE  (res_func) | res_func }  } 
   [CHANGING   { [failed   TYPE data  ] [reported   TYPE data  ] }].  
```

[`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapmethods_abstract_final.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`CHANGING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`data `](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) · [`data `](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md)

### Variant

[1. `... READ bdef ...`](abaphandler_meth_read.md#variant-1)

[2. `... READ bdef\_assoc ...`](abaphandler_meth_read.md#variant-2)

[3. `... FUNCTION bdef~function ...`](abaphandler_meth_read.md#variant-3)

## Overview

### Description

[Handler method](../../abap-glossary/abenabp_handler_method_glosry.md) that is used for read operations in [RAP](../../abap-glossary/abenrap_glosry.md). It must be defined and implemented in a [handler class](../../abap-glossary/abenabp_handler_class_glosry.md) of an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). The method name `meth` can be chosen freely, except for the methods names in the context of [RAP default values functions](abaprap_handler_default_val_func.md). `bdef` is the name or the alias of the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md), `assoc` the name of the association, and `function` the name of a function.

The method parameters can be passed by reference (see [`REFERENCE`](../../abap-programming-language/abap-declarations/abapmethods_parameters.md)), except for the predefined parameters `failed` and `reported`.

**Note:** Find information about the handler methods to be implemented for [RAP default values functions](../../abap-glossary/abenrap_bo_defaulting_glosry.md) [here](abaprap_handler_default_val_func.md).

### Addition

[1. `... REQUEST ...`](abaphandler_meth_read.md#addition-1)

[2. `... CHANGING ...`](abaphandler_meth_read.md#addition-2)

## Variant 1

`... READ bdef ...`

### Description

Handles the read requests in RAP read operations. BDEF requirement for the read operations: The entities to be read from must be declared after the notation [`define behavior for`](../rap-behavior-definitions/abenbdl_define_beh.md).

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_read`: Includes the entities to be read. It is an internal table of type [`TYPE TABLE FOR READ IMPORT bdef`](abaptype_table_for.md).

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - `res_read`: Mandatory parameter used to store the read result. It must be specified after the ABAP word `RESULT` and is an internal table of type [`TYPE TABLE FOR READ RESULT bdef`](abaptype_table_for.md).

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed` and `reported` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed` and `reported` explicitly following the ABAP word `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Variant 2

`... READ bdef\_assoc ...`

### Description

Handles the read requests in [RAP read-by-association operations](../../abap-glossary/abenrap_rba_operation_glosry.md). BDEF requirement for read-by-association operations: The entities to be read from must be declared after the notation [`define behavior for`](../rap-behavior-definitions/abenbdl_define_beh.md).

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - `im_par_read`: Includes the entities to be read. It is an internal table of type [`TYPE TABLE FOR READ IMPORT bdef\_assoc`](abaptype_table_for.md).

  - `full_rba`: Used to indicate whether the `res_rba` parameter, i. e. all target instances, or just the links, i. e. the `link_rba` parameter, should be retrieved in the context of read-by-association operations. It is a Boolean value of type `c` with length 1. `full_rba` specified with `'X'` respects all target instances. Note that the explicit specification of the `FULL` parameter with ABAP EML is only possible for the dynamic form of the ABAP EML `READ` statement ([`READ ENTITIES OPERATIONS`](abapread_entities_operations.md)). With the short form ([`READ ENTITY`](abapread_entity_short.md)) and long form ([`READ ENTITIES`](abapread_entities_long.md)), the explicit specification of the `full_rba` parameter is not possible. In these cases, the specification is irrelevant because it applies anyway if the links (`link_rba` parameter) or the data are requested.

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters.

  - `res_rba`: Used to store the read result. It must be specified after the ABAP word `RESULT` and is an internal table of type [`TYPE TABLE FOR READ RESULT bdef\_assoc`](abaptype_table_for.md).

  - `link_rba`: Used to store the keys of the source and target entities. It is an internal table of type [`TYPE TABLE FOR READ LINK bdef\_assoc`](abaptype_table_for.md).

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed` and `reported` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed` and `reported` explicitly following the ABAP word `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

The parameters must be specified in the method definition in the following sequence: `... IMPORTING ... FULL ... RESULT ... LINK ... CHANGING ...`

## Variant 3

`... FUNCTION bdef~function ...`

### Description

Handles the read requests in the context of [functions](../rap-behavior-definitions/abenbdl_function.md). See the required BDEF notations for functions in topic [RAP BDL - function](../rap-behavior-definitions/abenbdl_function.md).

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - `im_par_read`: Includes the [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) to be read. It is an internal table of type [`TYPE TABLE FOR FUNCTION IMPORT bdef~function`](abaptype_table_for.md).

  - `req_func`: Additional parameter whose availability depends on the BDEF specification. See [`... REQUEST ...`](abaphandler_meth_modify.md)

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters.

  - `res_func`: Used to store the read result. It must be specified after the ABAP word `RESULT` and is an internal table of type [`TYPE TABLE FOR FUNCTION RESULT bdef\_assoc`](abaptype_table_for.md).

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed` and `reported` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed` and `reported` explicitly following the ABAP word `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

The parameters must be specified in the method definition in the following sequence: `... IMPORTING ... FULL ... RESULT ... LINK ... CHANGING ...`

## Addition 1

`... REQUEST ...`

### Description

The addition and the parameter `req_func` are only available in the context of functions that are specified with the notation [`result selective`](../rap-behavior-definitions/abenbdl_action_output_para.md) in the BDEF. `req_func` is a structure of type [`TYPE STRUCTURE FOR FUNCTION REQUEST bdef~function`](abaptype_structure_for.md).

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
METHODS read FOR READ 
    IMPORTING keys FOR READ bdef RESULT result. 
 
METHODS rba_assoc FOR READ 
    IMPORTING keys_rba FOR READ bdef\_assoc 
    FULL result_requested RESULT result LINK association_links. 
 
METHODS function1 FOR READ 
    IMPORTING keys FOR READ bdef~function1 RESULT result. 
 
METHODS function2 FOR READ 
    IMPORTING keys FOR READ bdef~function2 
    REQUEST requested_fields RESULT result. 
...
```

## Executable Examples

- [Example for RAP Handler Methods](abenrap_handler_methods_abexa.md): Demonstrates this RAP handler method within a RAP handler class using a simple unmanaged RAP BO that is draft-enabled.

- [RAP BDL - function](../rap-behavior-definitions/abenbdl_function_abexa.md)
