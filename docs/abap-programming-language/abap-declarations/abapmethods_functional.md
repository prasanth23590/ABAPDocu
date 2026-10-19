---
title: "METHODS, RETURNING"
source_file: abapmethods_functional.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Methods > METHODS"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# METHODS, RETURNING

## Syntax

``` abap
METHODS meth [ABSTRACT|FINAL] 
            |[DEFAULT IGNORE|FAIL]   
  [IMPORTING parameters [PREFERRED PARAMETER p]]   
  [EXPORTING parameters]   
  [CHANGING  parameters]   
  RETURNING VALUE(r) typing   
  [{RAISING exc1|RESUMABLE(exc1) exc2|RESUMABLE(exc2) ...}   
  |{EXCEPTIONS exc1 exc2 ...}].  
```

[`ABSTRACT|FINAL]`](abapmethods_abstract_final.html) · [`DEFAULT IGNORE|FAIL`](abapmethods_default.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`parameters`](abapmethods_parameters.md) · [`typing`](abentyping_complete.md)

### Addition

[`... RETURNING VALUE(r) typing`](abapmethods_functional.md#addition)

## Overview

### Description

This statement declares a [functional](../../abap-glossary/abenfunctional_method_glosry.md) instance method `meth`. The same applies to the additions `ABSTRACT`, `FINAL`, `DEFAULT`, `IMPORTING`, `EXPORTING`, `CHANGING`, `RAISING`, and `EXCEPTIONS` as to [general instance methods](abapmethods_general.md).

A functional method can be [called as a function](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) in a suitable read position.

## Addition

`... RETURNING VALUE(r) typing`

### Description

In addition to any other formal parameters, a functional method has exactly one return value `r` declared using the addition `RETURNING`. The return value must be passed by [value](../../abap-glossary/abenpass_by_value_glosry.md) using `VALUE` and be completely typed using [`typing`](abentyping_complete.md). In the typing check, [special rules](abentyping_return_values.md) apply, depending on whether an explicit actual parameter is bound using [`RECEIVING`](../abap-calling-and-exiting-program-units/abapcall_method_parameters.md) or the functional method is used in an operand position.

### Hints

- In the methods of a class, one method of the class [hides](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions_syntax.md) a [built-in function](../../abap-glossary/abenbuiltin_function_glosry.md) with the same name. The same applies in functional method calls. Functional method calls and specified built-in functions have similar syntax, which means it is important that a functional method is not given the same name as a built-in function.

- Functional methods are allowed as [actual parameters](abentyping_arith_expr.md) of methods, which enables the option of nesting method calls in an operand position.

- The return value of a functional method is always passed by value, which means it is passed only if the functional method is completed without errors.

- In functional methods, the statement [`RETURN`](../abap-calling-and-exiting-program-units/abapreturn.md) can be used to assign the result of an expression [`expr`](../abap-calling-and-exiting-program-units/abapreturn.md) to the return value when terminating the method.

### Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Declaration of a functional method with input parameter and return value. The method is called functionally as an actual parameter for the input parameter of another method.

``` abap
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    METHODS 
      meth 
        IMPORTING 
          name          TYPE string 
        RETURNING 
          VALUE(result) TYPE string. 
ENDCLASS. 
 
CLASS exa DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS main. 
ENDCLASS. 
 
CLASS cls IMPLEMENTATION. 
  METHOD meth. 
    result = |Hello { name }!|. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS exa IMPLEMENTATION. 
  METHOD main. 
    FINAL(out) = cl_demo_output=>new( ). 
 
    out->write( 
      NEW cls( )->meth( CONV #( sy-uname ) ) ). 
 
    out->display( ). 
  ENDMETHOD. 
ENDCLASS.
```
