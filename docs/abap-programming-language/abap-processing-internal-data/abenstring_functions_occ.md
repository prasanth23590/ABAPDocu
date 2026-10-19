---
title: "cstring_func - occ"
source_file: abenstring_functions_occ.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Common Parameters"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - occ

## Syntax

``` abap
... ( ... occ = occ ...  ) ...  
```

## Description

In string functions where searches are performed, the parameter `occ` specifies the occurrence of a match. `occ` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) of type `i`.

If `occ` is positive, the occurrences are counted from the left; if `occ` is negative, they are counted from the right. The values 1, 2, .... indicate the first, second, ... occurrences. The values -1, -2, .... indicate the last, last but one, ... occurrences.

The default value of `occ` is 1. Except in the case of the replacement function [`replace`](abenreplace_functions.md), the value 0 raises an exception from the class `CX_SY_STRG_PAR_VAL`. If `replace` is used, the value 0 replaces all occurrences.

## Hint

The sign of `occ` also affects the default values of [`off`](abenstring_functions_off_len.md) and [`len`](abenstring_functions_off_len.md).

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following function calls is `UX` and `XU`.

``` abap
FINAL(result1) = replace( val = `XX` sub  = `X` with = `U` occ =  1 ). 
FINAL(result2) = replace( val = `XX` sub  = `X` with = `U` occ = -1 ).
```
