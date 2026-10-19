---
title: "cstring_func - reverse"
source_file: abenreverse_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Processing Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - reverse

## Syntax

``` abap
... reverse( [val =] text  ) ...  
```

[`[val =] text`](abenstring_functions_val.md)

## Description

This [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) returns a character string that reverses the content of [`text`](abenstring_functions_val.md).

The return value has the type `string`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Returns the Latin alphabet in reverse.

``` abap
FINAL(abcde) = `&#x00E0;bcdefghijklmnopqrstuvwxyz`. 
FINAL(result) = reverse( abcde ).
```
