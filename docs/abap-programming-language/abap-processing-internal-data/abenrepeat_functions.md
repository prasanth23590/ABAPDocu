---
title: "cstring_func - repeat"
source_file: abenrepeat_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Processing Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - repeat

## Syntax

``` abap
... repeat( val = text  occ = occ ) ...  
```

[`val = text`](abenstring_functions_val.md)

## Description

This [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) returns a character string that contains the content of [`text`](abenstring_functions_val.md) as many times as specified in `occ`. If `text` is an empty string or if `occ` contains the value 0, an empty string is returned.

`occ` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) with type `i`. If the value of `occ` is negative, an exception of the class `CX_SY_STRG_PAR_VAL` is raised.

The return value has the type `string`.

## Hint

The parameter `occ` has a different meaning here than in functions used for searching.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The function `repeat` is used to create a string with ten blanks.

``` abap
FINAL(result) = repeat( val = ` ` occ = 10 ).
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_STRG_PAR_VAL`

- *Cause:* Occurrences in `occ` are less than 0.

  *Runtime error:* `STRG_ILLEGAL_PAR`
