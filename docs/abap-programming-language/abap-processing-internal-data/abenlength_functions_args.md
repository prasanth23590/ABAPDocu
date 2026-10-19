---
title: "cstring_func - char_off"
source_file: abenlength_functions_args.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Description Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - char_off

This [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) length function has a named character-like parameter.

## Syntax

``` abap
... char_off( val = text add = pos [off = off] ) ...  
```

## Description

The function returns the offset of the character in `text` that is `pos` places away from the character in the offset specified in `off`. The default value for `off` is 0. `text` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md). `pos` and `off` are [numeric expression positions](../../abap-glossary/abennumerical_expr_position_glosry.md) with the type `i`.

This function can be specified in [general](../../abap-glossary/abengeneral_expr_position_glosry.md) and [numeric expression positions](../../abap-glossary/abennumerical_expr_position_glosry.md). The return value has the type `i`.

The value of `pos` can be positive and negative and describes the places to the right or on the left accordingly. If `pos` identifies a position outside of `text`, the function returns the value -1. If `off` is greater than the length of `text`, an exception of the class `CX_SY_RANGE_OUT_OF_BOUNDS` is raised.

## Hint

The function `char_off` was suitable for finding the correct offsets of characters in non-Unicode double-byte systems.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following function call is 7.

``` abap
FINAL(result) = char_off( val = `12345678` add = 4 off = 3 ).
```
