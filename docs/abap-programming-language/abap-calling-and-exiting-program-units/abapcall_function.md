---
title: "CALL FUNCTION"
source_file: abapcall_function.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL FUNCTION

## Syntax Forms

**[General Function Module Call](abapcall_function_general.md)**

``` abap
1. CALL FUNCTION func { parameter_list 
                     | parameter_tables }.
```

**[Remote Function Call](abapcall_function_destination-.md)**

``` abap
2. CALL FUNCTION ... DESTINATION ...
```

[`parameter_list`](abapcall_function_parameter.md) · [`parameter_tables`](abapcall_function_dynamic.md)

## Description

Call of a function module. Static and dynamic function module calls have no syntactic differences. The function module is always specified by a data object and the name of the called function module not determined until runtime.

## System Fields

The system field `sy-subrc` is set to 0 when a function module is called. If a [non-class-based exception](../abap-program-flow-logic/abenexceptions_non_class.md) is raised and is handled by the assignment of a value, `sy-subrc` is set to this value. After the registration of an update function module using `CALL FUNCTION ... IN UPDATE TASK`, `sy-subrc` is undefined.

## Hints

- Unlike in method calls, there are no different syntax variants for static calls and dynamic calls of function modules. They can, however, be distinguished as follows

  - In a dynamic function module call, the name of the function module is specified in a variable and the parameter is passed dynamically. This is possible in general function module calls.

    In both cases, incorrectly specified function modules or parameters produce runtime errors and not syntax errors

  - In static function module calls, a statically known function module is specified as a [character literal](../../abap-glossary/abencharacter_literal_glosry.md) or as a constant and the parameter is passed statically.

## Security Hint

If the name of a program unit is specified dynamically when it is called, and this name is passed to a program from outside, this a serious security risk. Any names passed to a program from outside must be checked thoroughly before being used in calls. The system class `CL_ABAP_DYN_PRG`, for example, can be used to do this.
