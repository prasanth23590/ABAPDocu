---
title: "Built-In Functions, Syntax for Calling"
source_file: abenbuilt_in_functions_syntax.html
section: "ABAP Programming Language > ABAP - Built-In Types, Data Objects, Functions, and Constructors > Built-In Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Built-In Functions, Syntax for Calling

## Syntax Forms

**[Functions with an Unnamed Parameter](abenbuilt_in_functions_unnmd.md)**

``` abap
1. ... func( arg ) ...
```

**[Functions with Named Parameters](abenbuilt_in_functions_nmd.md)**

``` abap
2. ... func( val = arg p1 = arg1 p2 = arg2 ... ) ...
```

## Description

General syntax for calling built-in functions in operand positions.

In functions with named [formal parameters](../../abap-glossary/abenformal_parameter_glosry.md), there is usually a main input parameter `val` and the option of passing [arguments](../../abap-glossary/abenargument_glosry.md) to further input parameters, some of which are optional.
