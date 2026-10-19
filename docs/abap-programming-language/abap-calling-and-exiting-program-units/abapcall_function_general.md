---
title: "CALL FUNCTION func"
source_file: abapcall_function_general.html
section: "ABAP Programming Language > ABAP - Calling and Exiting Program Units > Calling Processing Blocks > Calling Procedures > CALL FUNCTION"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CALL FUNCTION func

## Syntax

``` abap
CALL FUNCTION func { parameter_list   
                   | parameter_tables }.  
```

[`parameter_list`](abapcall_function_parameter.md) · [`parameter_tables`](abapcall_function_dynamic.md)

## Description

This statement calls the [function module](../../abap-glossary/abenfunction_module_glosry.md) specified in `func`. The name `func` must be a character-like data object that contains the name of a function module allowed by the package check in uppercase letters when the statement is executed. Since each function module in [AS ABAP](../../abap-glossary/abenas_abap_glosry.md) has a unique name, the function pool does not need to be specified. The following can be specified for `func`:

- Literal or constant

  If the data object `func` is specified as a [character literal](../../abap-glossary/abentext_literal_glosry.md) or as a [constant](../../abap-glossary/abenconstant_glosry.md), it is evaluated as a statically specified object by tools such as the where-used list.

- Variable

  If the data object `func` is specified as a [variable](../../abap-glossary/abenvariable_glosry.md), it is specified only dynamically, and the content is not evaluated statically.

When the statement is executed, `func` is not evaluated until runtime in both cases. In particular, the types of the [parameters](abapcall_function_parameter.md) are not known until runtime. In both cases, incorrectly specified function modules or parameters produce runtime errors and not syntax errors

The additions [`parameter_list`](abapcall_function_parameter.md) or [`parameter_tables`](abapcall_function_dynamic.md) are used to statically or dynamically assign actual parameters to the formal parameters of the function module and return values to the non-class-based exceptions.

## Security Hint

If the name of a program unit is specified dynamically when it is called, and this name is passed to a program from outside, this a serious security risk. Any names passed to a program from outside must be checked thoroughly before being used in calls. The system class `CL_ABAP_DYN_PRG`, for example, can be used to do this.

## Hint

Since `func` is not evaluated until runtime when function modules are called, no [writable expressions](../../abap-glossary/abenwritable_expression_glosry.md) and no [inline declarations](../../abap-glossary/abeninline_declaration_glosry.md) can be specified as actual parameters, unlike in static method calls.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Call of function modules `READ_SPFLI_INTO_TABLE` and `READ_SPFLI_INTO_TABLE_NEW` with parameter passing and handling of non-classified and class-based exceptions.

``` abap
DATA itab TYPE spfli_tab. 
 
CALL FUNCTION 'READ_SPFLI_INTO_TABLE' 
  EXPORTING 
    id        = 'LH' 
  IMPORTING 
    itab      = itab 
  EXCEPTIONS 
    not_found = 4. 
IF sy-subrc <> 0. 
   ... 
ENDIF. 
 
TRY. 
    CALL FUNCTION 'READ_SPFLI_INTO_TABLE_NEW' 
      EXPORTING 
        id   = 'LH' 
      IMPORTING 
        itab = itab. 
  CATCH cx_no_flight_found INTO FINAL(exc). 
    ... 
ENDTRY.
```

## Executable Example

[Calling Function Modules](abencall_function_abexa.md)

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_NO_HANDLER`

- See [Class-Based Exceptions in Procedures](../abap-program-flow-logic/abenexceptions_procedures.md).

  *Runtime error:* `UNCAUGHT_EXCEPTION`

`CX_SY_DYN_CALL_ILLEGAL_FUNC`

- *Cause:* The called function is known but not active.

  *Runtime error:* `CALL_FUNCTION_NOT_ACTIVE`

- *Cause:* The called function is unknown.

  *Runtime error:* `CALL_FUNCTION_NOT_FOUND`

`CX_SY_DYN_CALL_ILLEGAL_TYPE`

- *Cause:* The type of the actual parameter does not meet the requirements of the function interface.

  *Runtime error:* `CALL_FUNCTION_CONFLICT_GEN_TYP`

- *Cause:* The actual parameter does not have the length expected by the function.

  *Runtime error:* `CALL_FUNCTION_CONFLICT_LENG`

- *Cause:* The actual parameter does not have the type expected by the function.

  *Runtime error:* `CALL_FUNCTION_CONFLICT_TYPE`

- *Cause:* Only valid functions can be called in the update.

  *Runtime error:* `CALL_FUNCTION_NO_VB`

- *Cause:* An actual parameter does not meet the alignment requirements of the corresponding formal parameter.

  *Runtime error:* `CALL_FUNCTION_WRONG_ALIGNMENT`

`CX_SY_DYN_CALL_PARAM_MISSING`

- *Cause:* The function expects a parameter that was not passed by the caller.

  *Runtime error:* `CALL_FUNCTION_PARM_MISSING`

`CX_SY_DYN_CALL_PARAM_NOT_FOUND`

- *Cause:* The caller passed a parameter that is not recognized by the function.

  *Runtime error:* `CALL_FUNCTION_PARM_UNKNOWN`
