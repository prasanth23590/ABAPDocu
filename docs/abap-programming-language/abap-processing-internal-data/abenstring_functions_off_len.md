---
title: "cstring_func - off, len"
source_file: abenstring_functions_off_len.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Common Parameters"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - off, len

## Syntax

``` abap
... ( ... off = off len = len ...  ) ...  
```

## Description

`off` is used to pass an [offset](../../abap-glossary/abenoffset_glosry.md) and `len` is used to pass a length. In functions where both `off` and `len` can be passed, they determine the subarea in which a string is to be processed.

`off` and `len` are [numeric expression positions](../../abap-glossary/abennumerical_expr_position_glosry.md) with the type `i`.

The default value of `off` is generally 0 and the default value of `len` is generally the length of the string minus a predefined offset or an offset passed using `off`. Only if a negative argument is passed for the occurrence [`occ`](abenstring_functions_occ.md) simultaneously for functions where this is possible, is the default value of `off` the length of the string and the default value of `len` the value of the associated offset.

If the value of `off` or `len` is negative, an offset defined using `off` is outside the string, or a subarea defined using `off` and `len` is not completely contained in the string, an exception of the class `CX_SY_RANGE_OUT_OF_BOUNDS` is raised.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following function calls is 17 and 12.

``` abap
FINAL(result1) = count( val   = `Intro: blahblahblah` 
                       pcre  = `\w` ). 
FINAL(result2) = count( val   = `Intro: blahblahblah` 
                       pcre = `\w` off = 6 ).
```
