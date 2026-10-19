---
title: "cstring_func - val"
source_file: abenstring_functions_val.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Common Parameters"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - val

## Syntax

``` abap
... ( ... val = text ...  ) ...  
```

## Description

The argument `text` passes the text string to be processed by the function to the named parameter `val`. `text` is an extended [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md). Functional method calls, table expressions, and constructor expressions whose return value is convertible to the type `string` can also be specified. Only elementary data types can be processed.

If a character-like data object with a fixed length is specified, any trailing blanks are ignored. Non-character-like return values are converted to the data type `string`.

## Hints

- The conversion operator [`CONV`](abenconstructor_expression_conv.md) can be applied to process those non-elementary data types that can be converted to an elementary character-like data type, such as structures with character-like-only flat components.

- Explicit specification of `val =` can also be optional.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following two function calls are equivalent, since the specification of `val =` in `to_upper` is optional.

``` abap
FINAL(result1) = to_upper( val = 'aAbBcC' ). 
FINAL(result2) = to_upper(       'aAbBcC' ).
```
