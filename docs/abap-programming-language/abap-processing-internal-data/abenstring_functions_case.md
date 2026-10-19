---
title: "cstring_func - case"
source_file: abenstring_functions_case.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Common Parameters"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - case

## Syntax

``` abap
... ( ... case = case ...  ) ...  
```

## Description

Searches and comparisons in string functions are case-sensitive by default, but this can be overridden, if necessary, using the parameter `case`. The parameter `case` requires a constant or a literal of the type `abap_bool` from the type pool `ABAP` with the value of the constants `abap_true` or `abap_false`. If `case` contains the value of `abap_true`, the search is case-sensitive; if it contains the value of `abap_false`, it is not.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following function calls is 2 and 3.

``` abap
FINAL(result1) = find( val = `aAbBcC` sub  = `B` case = abap_false ). 
FINAL(result2) = find( val = `aAbBcC` sub  = `B` case = abap_true  ).
```
