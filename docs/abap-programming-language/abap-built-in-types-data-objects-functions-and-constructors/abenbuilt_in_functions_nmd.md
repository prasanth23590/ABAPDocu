---
title: "Built-In Functions, Named Parameter"
source_file: abenbuilt_in_functions_nmd.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Functions > Built-In Functions, Syntax for Calling"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Built-In Functions, Named Parameter

## Syntax

``` abap
... func( val = arg p1 = arg1 p2 = arg2 ... ) ...  
```

## Description

In functions with one or more named input parameters those are [keyword parameters](../../abap-glossary/abenkeyword_parameter_glosry.md). Arguments are passed with same syntax as when [calling functional methods](../abap-calling-and-exiting-program-units/abapcall_method_functional.md) with multiple input parameters. The data type of the arguments must match the corresponding parameters. The blanks after the opening parentheses and before the closing parentheses are relevant. If such a function has only one parameter, or if only the main parameter is to be supplied, the syntax can be simplified as follows:

`... func( arg ) ...`

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The built-in function [`condense`](../abap-processing-internal-data/abencondense_functions.md) has named parameters and can, for example, be called as follows.

``` abap
FINAL(str1) = condense( `...` ). 
FINAL(str2) = condense( val = `...` ). 
FINAL(str3) = condense( val = `...`  del = ` ` ).
```
