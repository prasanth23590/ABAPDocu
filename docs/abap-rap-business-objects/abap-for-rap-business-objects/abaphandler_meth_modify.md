---
title: "FOR MODIFY, RAP Handler Method"
source_file: abaphandler_meth_modify.html
section: "ABAP RAP Business Objects > ABAP for RAP Business Objects > ABAP for Providing RAP Business Objects > ABAP Behavior Pools (ABP) > RAP Handler Classes and Methods > METHODS, FOR, RAP Handler Methods"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FOR MODIFY, RAP Handler Method

## Syntax

``` abap
**Handler method definitions:**

METHODS meth [FINAL] 
   FOR MODIFY 
   [IMPORTING  ] { REFERENCE  (im_par_mod) | im_par_mod } 
   FOR { CREATE bdef } 
     | { CREATE bdef\_assoc } 
     | { UPDATE bdef } 
     | { DELETE bdef } 
     | { ACTION bdef~action 
          [REQUEST { REFERENCE  (req_act) | req_act } ] 
          [RESULT { REFERENCE  (res_act) | res_act }] } 
     | { ACTION { bdef~activate 
                | bdef~additionalsave 
                | bdef~edit 
                | bdef~discard 
                | bdef~resume } } 
   [CHANGING   { [failed   TYPE data  ] [reported   TYPE data  ] [mapped   TYPE data  ] }].  
```

[`METHODS`](../../abap-programming-language/abap-declarations/abapmethods.md) · [`FINAL`](../../abap-programming-language/abap-declarations/abapmethods_abstract_final.md) · [`IMPORTING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`REFERENCE `](../../abap-programming-language/abap-declarations/abapmethods_parameters.md) · [`CHANGING `](../../abap-programming-language/abap-declarations/abapmethods_general.md) · [`data `](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) · [`data `](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) · [`data `](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md)

### Variant

[1. `... CREATE bdef ...`](abaphandler_meth_modify.md#variant-1)

[2. `... CREATE bdef\_assoc ...`](abaphandler_meth_modify.md#variant-2)

[3. `... UPDATE ...`](abaphandler_meth_modify.md#variant-3)

[4. `... DELETE ...`](abaphandler_meth_modify.md#variant-4)

[5. `... ACTION bdef~action ...`](abaphandler_meth_modify.md#variant-5)

[6. `... ACTION bdef~additionalsave ...`](abaphandler_meth_modify.md#variant-6)

[7. `... ACTION bdef~activate ...`](abaphandler_meth_modify.md#variant-7)

[8. `... ACTION bdef~edit ...`](abaphandler_meth_modify.md#variant-8)

[9. `... ACTION bdef~discard ...`](abaphandler_meth_modify.md#variant-9)

[10. `... ACTION bdef~resume ...`](abaphandler_meth_modify.md#variant-10)

### Addition

[1. `... REQUEST ...`](abaphandler_meth_modify.md#addition-1)

[2. `... RESULT ...`](abaphandler_meth_modify.md#addition-2)

[3. `... CHANGING ...`](abaphandler_meth_modify.md#addition-3)

## Overview

### Description

[Handler methods](../../abap-glossary/abenabp_handler_method_glosry.md) that are used for changing operations on [RAP BO entities](../../abap-glossary/abenrap_bo_entity_glosry.md) and [operation augmentation](../rap-behavior-definitions/abenbdl_augment_projection.md). They must be defined and implemented in a [handler class](../../abap-glossary/abenabp_handler_class_glosry.md) of an [ABAP behavior pool](../../abap-glossary/abenbehavior_pool_glosry.md). A single method can include multiple, different operations during one processing step. The method name `meth` can be chosen freely except for the draft-related methods. `bdef` is the name or the alias of the [BDEF](../../abap-glossary/abencds_behavior_definition_glosry.md), `assoc` the name of the association, and `action` the name of an action. It is possible to combine operations in one method.

## Variant 1

`... CREATE bdef ...`

### Description

Handles create operations.

See more details and the required BDEF specifications for the variant in the following topics:

- [RAP BDL - operations for associations](../rap-behavior-definitions/abenbdl_association.md)

- [RAP BDL - `augment`, projection](../rap-behavior-definitions/abenbdl_augment_projection.md)

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_mod`: Includes the [RAP BO instances](../../abap-glossary/abenrap_bo_instance_glosry.md) to be created. It is an internal table of type [`TYPE TABLE FOR CREATE bdef`](abaptype_table_for.md). The parameter can also be passed by reference (see [`REFERENCE`](../../abap-programming-language/abap-declarations/abapmethods_parameters.md)).

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed`, `reported` and `mapped` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed`, `reported` and `mapped` explicitly following the addition `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Variant 2

`... CREATE bdef\_assoc ...`

### Description

Handles [create-by-association operations](../../abap-glossary/abenrap_cba_operation_glosry.md).

See more details and the required BDEF specifications for the variant in the following topics:

- [RAP BDL - operations for associations](../rap-behavior-definitions/abenbdl_association.md)

- [RAP BDL - `augment`, projection](../rap-behavior-definitions/abenbdl_augment_projection.md)

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_mod`: Includes the RAP BO instances to be created. It is an internal table of type [`TYPE TABLE FOR CREATE bdef\_assoc`](abaptype_table_for.md). The parameter can also be passed by reference.

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed`, `reported` and `mapped` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed`, `reported` and `mapped` explicitly following the addition `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Variant 3

`... UPDATE bdef ...`

### Description

Handles update operations.

See more details and the required BDEF specifications for the variant in the following topics:

- [RAP BDL - operations for associations](../rap-behavior-definitions/abenbdl_association.md)

- [RAP BDL - `augment`, projection](../rap-behavior-definitions/abenbdl_augment_projection.md)

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_mod`: Includes the RAP BO instances to be updated. It is an internal table of type [`TYPE TABLE FOR UPDATE bdef`](abaptype_table_for.md). The parameter can also be passed by reference.

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed`, `reported` and `mapped` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed`, `reported` and `mapped` explicitly following the addition `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Variant 4

`... DELETE bdef ...`

### Description

Handles delete operations.

See more details and the required BDEF specifications for the variant in the following topic: [RAP BDL - standard operations](../rap-behavior-definitions/abenbdl_standard_operations.md).

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_mod`: Includes the keys of the RAP BO instances to be deleted. It is an internal table of type [`TYPE TABLE FOR DELETE bdef`](abaptype_table_for.md). The parameter can also be passed by reference.

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed`, `reported` and `mapped` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed`, `reported` and `mapped` explicitly following the addition `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Variant 5

`... ACTION bdef~action ...`

### Description

Handles actions.

See more details and the required BDEF specifications for the variant in the following topics:

- [RAP BDL - action](../rap-behavior-definitions/abenbdl_action.md)

- [RAP BDL - determine actions](../rap-behavior-definitions/abenbdl_determine_action.md)

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_mod`: Includes the keys of the RAP BO instances for which an action should be executed. It is an internal table of type [`TYPE TABLE FOR ACTION IMPORT bdef~action`](abaptype_table_for.md). The parameter can also be passed by reference.

  - `req_act`: See the details in section [`... REQUEST ...`](abaphandler_meth_modify.md).

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - `res_act`: See the details in section [`... RESULT ...`](abaphandler_meth_modify.md).

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed`, `reported` and `mapped` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed`, `reported` and `mapped` explicitly following the addition `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Variant 6

`... ACTION bdef~additionalsave ...`

### Description

Handles the [RAP BO draft action](../../abap-glossary/abenrap_bo_draft_action_glosry.md) `additionalsave`. The name `additionalsave` is predefined. The method cannot be directly called using an ABAP EML statement and is not exposed with OData. It is called on commit.

The method implementation provides a dedicated save exit for draft instances, for example, for external draft persistencies that are available in parallel with the internally managed draft persistence.

The following restrictions currently apply:

- Only the instance key values of created, updated and deleted instances (indicated by [`%chg`](abapderived_types_chg.md)) are available.

- Information about which fields of instances were updated in the transaction can be obtained by selecting from the CDS view and comparing this data with the read result of an ABAP EML read request.

- Information about which fields of instances were updated or created at the end of a transaction can be obtained by selecting from the CDS view and comparing this data with the read result of an ABAP EML read request.

- Information about whether draft instances were deleted after the `activate` or `discard` method calls must be stored appropriately by you for use in the `additionalsave` method.

See the required BDEF specifications for the variant in the topic [draft action](../rap-behavior-definitions/abenbdl_draft_action.md).

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_mod`: Contains [`%cid`](abapderived_types_cid.md) and [`%param`](abapderived_types_param.md). `%param` is a deep structure here. It has the [absolute type name](../../abap-glossary/abenabsolute_typename_glosry.md) `\BDEF=NAME\TYPE=%CHANGEOP` and internal tables as components for each core entity of the RAP BO. The names of the components correspond to the entities. The line type of these internal tables contains the key (component groups: [`%key`](abapderived_types_key.md), [`%pky`](abapderived_types_pky.md)) and [`%chg`](abapderived_types_chg.md). The internal tables do not have an associated concrete type. The types are dynamically available. The absolute type name is `\BDEF=NAME\ENTITY=NAME\TYPE=CHANGEOP`.

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed`, `reported` and `mapped` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed`, `reported` and `mapped` explicitly following the addition `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Variant 7

`... ACTION bdef~activate ...`

### Description

Handles the `activate` action in [draft](../rap-behavior-definitions/abenbdl_with_draft.md) scenarios.

See more details and the required BDEF specifications for the variant in the following topic: [RAP BDL - draft actions](../rap-behavior-definitions/abenbdl_draft_action.md).

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_mod`: Includes the keys of the RAP BO instances for which the `activate` action should be executed. It is an internal table of type [`TYPE TABLE FOR ACTION IMPORT bdef~activate`](abaptype_table_for.md). The parameter can also be passed by reference.

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed`, `reported` and `mapped` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed`, `reported` and `mapped` explicitly following the addition `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Variant 8

`... ACTION bdef~edit ...`

### Description

Handles the `edit` action in draft scenarios.

See more details and the required BDEF specifications for the variant in the following topic: [RAP BDL - draft actions](../rap-behavior-definitions/abenbdl_draft_action.md).

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_mod`: Includes the keys of the RAP BO instances for which the `edit` action should be executed. It is an internal table of type [`TYPE TABLE FOR ACTION IMPORT bdef~edit`](abaptype_table_for.md). The parameter can also be passed by reference.

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed`, `reported` and `mapped` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed`, `reported` and `mapped` explicitly following the addition `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Variant 9

`... ACTION bdef~discard ...`

### Description

Handles the `discard` action in draft scenarios.

See more details and the required BDEF specifications for the variant in the following topic: [RAP BDL - draft actions](../rap-behavior-definitions/abenbdl_draft_action.md).

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_mod`: Includes the keys of the RAP BO instances for which the `discard` action should be executed. It is an internal table of type [`TYPE TABLE FOR ACTION IMPORT bdef~discard`](abaptype_table_for.md). The parameter can also be passed by reference.

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed`, `reported` and `mapped` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed`, `reported` and `mapped` explicitly following the addition `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Variant 10

`... ACTION bdef~resume ...`

### Description

Handles the `resume` action in draft scenarios.

See the required BDEF specifications for the variant in the following topic: [RAP BDL - draft actions](../rap-behavior-definitions/abenbdl_draft_action.md).

Method parameters:

- [`IMPORTING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameter:

  - `im_par_mod`: Includes the keys of the RAP BO instances for which the `resume` action should be executed. It is an internal table of type [`TYPE TABLE FOR ACTION IMPORT bdef~resume`](abaptype_table_for.md). The parameter can also be passed by reference.

- [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters:

  - The [`CHANGING`](../../abap-programming-language/abap-declarations/abapmethods_general.md) parameters `failed`, `reported` and `mapped` ([RAP response parameters](../../abap-glossary/abenrap_response_param_glosry.md)) are implicitly available. It is possible to specify the parameters with the predefined names `failed`, `reported` and `mapped` explicitly following the addition `CHANGING`. The generic type [`DATA`](../../abap-programming-language/abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_types_generic.md) can be specified. At runtime, the typed parameters implicitly have the BDEF derived type [`TYPE RESPONSE FOR`](abaptype_response_for.md). Instead of `DATA`, a data type of type `TYPE RESPONSE FOR` can be specified.

## Addition 1

`... REQUEST ...`

### Description

The addition and the parameter `req_act` are only available in the context of non-draft actions that are specified with a parameter in the BDEF. `req_act` is a structure of type [`TYPE STRUCTURE FOR GLOBAL FEATURES REQUEST bdef~action`](abaptype_structure_for.md).

See more details and the required BDEF specifications for the variant in the following topics:

- [RAP BDL - action](../rap-behavior-definitions/abenbdl_action.md)

- [RAP BDL - determine actions](../rap-behavior-definitions/abenbdl_determine_action.md)

## Addition 2

`... RESULT ...`

### Description

The addition and the parameter `res_act` are only available in the context of non-draft actions that are specified with a result in the BDEF. `res_act` is an internal table of type [`TYPE TABLE FOR ACTION RESULT bdef~action`](abaptype_table_for.md). The parameter can also be passed by reference.

See more details and the required BDEF specifications for the variant in the following topics:

- [RAP BDL - action](../rap-behavior-definitions/abenbdl_action.md)

- [RAP BDL - determine actions](../rap-behavior-definitions/abenbdl_determine_action.md)

## Addition 3

`... CHANGING ...`

### Description

See the details regarding the RAP response parameters that can be specified above.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Examples for RAP handler method definitions. Find demonstrations of method implementations in the executable examples further down. The first example in the code below shows a handler method definition combining multiple operations in one method.

``` abap
... 
METHODS modify FOR MODIFY 
    IMPORTING ent_cr FOR CREATE bdef 
              ent_upd FOR UPDATE bdef 
              keys FOR DELETE bdef. 
 
METHODS create FOR MODIFY 
    IMPORTING entities FOR CREATE bdef. 
 
METHODS cba_child FOR MODIFY 
    IMPORTING entities_cba FOR CREATE bdef\_child. 
 
METHODS update FOR MODIFY 
    IMPORTING entities FOR UPDATE bdef. 
 
METHODS delete FOR MODIFY 
    IMPORTING keys FOR DELETE bdef. 
 
METHODS action1 FOR MODIFY 
    IMPORTING keys FOR CREATE bdef~action1. 
 
METHODS action2 FOR MODIFY 
    IMPORTING keys FOR CREATE bdef~action2 RESULT result. 
 
METHODS action3 FOR MODIFY 
    IMPORTING keys FOR CREATE bdef~action3 
    REQUEST requested_fields RESULT result. 
 
METHODS activate FOR MODIFY 
    IMPORTING keys FOR ACTION bdef~activate. 
 
METHODS additionalsave FOR MODIFY 
    IMPORTING keys FOR ACTION bdef~additionalsave. 
 
METHODS discard FOR MODIFY 
    IMPORTING keys FOR ACTION bdef~discard. 
 
METHODS create FOR MODIFY 
    IMPORTING entities FOR CREATE bdef. 
 
METHODS edit FOR MODIFY 
    IMPORTING keys FOR ACTION bdef~edit. 
 
METHODS resume FOR MODIFY 
    IMPORTING keys FOR ACTION bdef~resume. 
...
```

## Executable Examples

- [Example for RAP Handler Methods](abenrap_handler_methods_abexa.md): Demonstrates this RAP handler method within a RAP handler class using a simple unmanaged RAP BO that is draft-enabled.

- [RAP BDL - Examples of actions](../rap-behavior-definitions/abenbdl_action_abexas.md)

- The example [ABAP EML - `MODIFY AUGMENTING ENTITY`](abeneml_modify_augmenting_abexa.md) demonstrates the three handler methods `augment_create`, `augment_update` and `augment_cba_assoc` (`assoc` refers to the name of the association) with a RAP projection business object.
