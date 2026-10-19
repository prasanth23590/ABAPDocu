---
title: "FOR DETERMINE, RAP Handler Method"
source_file: abaphandler_meth_det.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Handler Classes and Methods > METHODS, FOR, RAP Handler Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR DETERMINE, RAP Handler Method

## Syntax

``` abap
**Handler method definition:**

METHODS meth [FINAL] 
  FOR DETERMINE ON { SAVE | MODIFY } 
  [IMPORTING  ] { REFERENCE  (im_par_det) | im_par_det } 
   FOR bdef~det 
  [CHANGING   reported   TYPE data  ].  
```

[`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapmethods_abstract_final.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`CHANGING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`data `](abaptype_response_for.md)

### Variant

[1. `... SAVE ...`](abaphandler_meth_det.md#variant-1)

[2. `... MODIFY ...`](abaphandler_meth_det.md#variant-2)

## Overview

### Description

[Handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) that are used for [determinations](../rap-behavior-definitions/abenbdl_determinations.md). They must be defined and implemented in a [handler class](../../abap-glossary/abenabp_handler_class_glosry.md) of an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). The method name `meth` can be chosen freely. `bdef` is the name or the alias of the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md). `det` is the name of a [determination](../rap-behavior-definitions/abenbdl_determinations.md) specified in the BDEF.

**Method Parameters**

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_det`: Includes the keys of [RAP BO](../../abap-glossary/abenrap_bo_glosry.md) instances for which a determination should be executed. It is an internal table of type [`TYPE TABLE FOR DETERMINATION`](abaptype_table_for.md).

    The parameter can also be passed by reference (see [`REFERENCE`](../../abap-programming-language/abap-declarations/abapmethods_parameters.md)). The use of the ABAP word `IMPORTING` is optional.

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter `reported` ([RAP response parameter](../../abap-glossary/abenrap_response_param_glosry.md)) is implicitly available. It is possible to specify the parameter with the predefined name `reported` explicitly following the ABAP word `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameter implicitly has the BDEF derived type [`TYPE RESPONSE FOR REPORTED`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR REPORTED` can be specified.

**BDEF Requirements**

See the required BDEF notations for both variants in the topic [RAP BDL - determinations](../rap-behavior-definitions/abenbdl_determinations.md).

## Variant 1

`... SAVE ...`

### Description

Used for determinations that are executed during the [RAP save sequence](../../abap-glossary/abenrap_save_seq_glosry.md).

## Variant 2

`... MODIFY ...`

### Description

The method is called after data changes take place in the [transactional buffer](../../abap-glossary/abentransactional_buffer_glosry.md).

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Examples for RAP handler method definitions. Find demonstrations of method implementations in the executable examples further down.

``` abap
... 
    METHODS det_on_save FOR DETERMINE ON SAVE 
    IMPORTING keys FOR bdef~det_save. 
 
    METHODS det_on_modify FOR DETERMINE ON MODIFY 
    IMPORTING keys FOR bdef~det_mod. 
 
    METHODS det_on_save2 FOR DETERMINE ON SAVE 
    IMPORTING keys FOR bdef~det_save2 
    CHANGING reported TYPE DATA reported TYPE DATA. 
...
```

## Executable Examples

- [Example for RAP Handler Methods](abenrap_handler_methods_abexa.md): Demonstrates this RAP handler method within a RAP handler class using a simple unmanaged RAP BO that is draft-enabled.

- [RAP BDL - determination](../rap-behavior-definitions/abenbdl_determination_abexa.md)
