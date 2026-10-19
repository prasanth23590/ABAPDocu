---
title: "cstring_func - to_upper, to_lower, to_mixed, from_mixed"
source_file: abencase_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Processing Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - to_upper, to_lower, to_mixed, from_mixed

## Syntax

``` abap
1. ... to_upper( [val =] text ) ...  

2. ... to_lower( [val =] text ) ...  

3. ... to_mixed( [val =] text [sep = sep] [case = case] [min = min] ) ...  

4. ... from_mixed( [val =] text [sep = sep] [case = case] [min = min] ) ...  
```

[`[val =] text`](abenstring_functions_val.md) · [`[val =] text`](abenstring_functions_val.md) · [`[val =] text`](abenstring_functions_val.md) · [`[val =] text`](abenstring_functions_val.md)

## Description

These [built-in functions](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) return the character string from [`text`](abenstring_functions_val.md) after it has been converted in accordance with the following case rules:

- The function `to_upper` transforms all letters in the character string to uppercase letters.

- The function `to_lower` transforms all letters in the character string to lowercase letters.

- The function `to_mixed` transforms all letters in the character string to lowercase letters from the second position. Then, from left to right from the second position, it removes occurrences of the first character specified in `sep` from the character string and transforms the next letter to an uppercase letter. The default value for separator `sep` is an underscore (`_`). If `case` is not specified, the first character of the string remains unchanged. If `case` is specified and the first character of `case` is an uppercase letter, the first character in the string is also uppercase and otherwise lowercase. A positive number can be passed to `min` to specify a minimum number of characters that must appear before a separator from the start of the string or since the last replacement so that it works as described. The default value for `min` is 1.

- The function `from_mixed` inserts the first character specified in `sep` before each uppercase letter from left to right and from the second position. The default value for separator `sep` is an underscore (`_`). If `case` is not specified or if the first character in `case` is an uppercase letter, the entire string is transformed to uppercase, otherwise to lowercase. A positive number can be passed to `min` to specify a minimum number of characters that must appear before an uppercase letter from the start of the string or since the last insert so that a separator is inserted. The default value for `min` is 1.

`sep` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md). If they have a fixed length, trailing blanks are ignored. `min` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) of type `i`. `case` expects a character-like data object with fixed length. `val =` can be omitted only if no arguments are specified for the optional parameters. If `sep` is an empty string or if `min` is negative, an exception of class `CX_SY_STRG_PAR_VAL` is raised.

The return value has the type `string`.

## Hint

The functions `to_mixed` and `from_mixed` are intended for transforming standard ABAP naming conventions for names with underscores to standard Java naming conventions with uppercase and lowercase letters (Mixed Case Style and Camel Case Style) and vice versa.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Outputs the Latin alphabet in lowercase letters.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
FINAL(abcde) = `ABCDEFGHIJKLMNOPQRSTUVXYZ`. 
out->write( to_lower( abcde ) ). 
 
out->display( ).
```

## Executable Example

[String Functions, `to_mixed` and `from_mixed`](abenstring_function_mixed_abexa.md)

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_STRG_PAR_VAL`

- *Cause:* The separator in `sep` is empty or the minimum number in `min` is negative.

  *Runtime error:* `STRG_ILLEGAL_PAR`
