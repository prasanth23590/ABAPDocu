---
title: "Built-In Functions, Unnamed Parameter"
source_file: abenbuilt_in_functions_unnmd.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Functions > Built-In Functions, Syntax for Calling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Built-In Functions, Unnamed Parameter

## Syntax

``` abap
... func( arg ) ...  
```

## Description

For calling functions with an unnamed parameter, the syntax is the same as the syntax for [calling functional methods](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) with one input parameter. `func` is the built-in function and the argument `arg` passed to the function is an operand whose data type matches the function. The blanks after the opening parentheses and before the closing parentheses are relevant.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The built-in function [`line_exists`](../abap-program-flow-logic/abenline_exists_function.md) has an unnamed parameter that expects a table expression.

``` abap
DATA itab TYPE TABLE OF i WITH EMPTY KEY. 
 
... 
 
IF line_exists( itab[ 1 ] ). 
  ... 
ENDIF.
```
