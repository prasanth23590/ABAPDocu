---
title: "cstring_func - sub"
source_file: abenstring_functions_sub.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Common Parameters"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - sub

## Syntax

``` abap
... ( ... sub = substring ...  ) ...  
```

## Description

`substring` is used to pass a character string whose characters are to be searched for or inserted. `substring` is a [character like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md). Only arguments with elementary types can be specified.

If a character-like data object with a fixed length is specified, any trailing blanks are ignored.

## Hint

The behavior of a function when an empty string is specified in `substring` depends on the corresponding function.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following function call is 2.

``` abap
FINAL(result) = count( val = 'axaxa' sub = 'x' ).
```
