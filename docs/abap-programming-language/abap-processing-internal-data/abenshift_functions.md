---
title: "cstring_func - shift_left, shift_right"
source_file: abenshift_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Processing Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - shift_left, shift_right

The shift functions shift the content of a character-like argument.

## Syntax

``` abap
1. ... shift_left( [val =] text 
                  [places = places]|[circular = places]|[sub = substring] ) ...  

2. ... shift_right( [val =] text 
                   [places = places]|[circular = places]|[sub = substring] ) ...  
```

[`[val =] text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md) · [`[val =] text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md)

## Description

The [built-in functions](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) `shift_left` and `shift_right` shift the character string [`text`](abenstring_functions_val.md) to the left or to the right and return the result. The shift depends on the parameter pass as follows:

- If the parameter `places` is supplied with a numeric value, the corresponding number of characters is removed on the left or right of the character string and the length of the character string is reduced accordingly. If the value of `places` is negative or longer than the character string, an exception of the class `CX_SY_RANGE_OUT_OF_BOUNDS` is raised.

- If the parameter `circular` is supplied with a numeric value, the functions behave like `places`, but insert the removed substring at the end or start of the character string.

- If the parameter `sub` is supplied with a character string in [`substring`](abenstring_functions_sub.md), all substrings in the character string from `text` are removed on the left or right that match the content of `substring`. The character string from `text` remains unchanged and preserves, for example, blanks if no substrings are found or if `substring` is given an empty string. Note that a character string in `substring` of a fixed length containing only blanks is handled like an empty string. This also applies to the predefined constant `space`. For more information, refer to [Trailing Blanks in Character String Processing](abenstring_processing_trail_blanks.md).

- If none of the parameter `places`, `circular`, or `sub` are supplied, the functions behave as if the `sub` parameter were passed a blank character. All blank characters to the left or right are removed. In this case, an explicit `val` can also be omitted.

`places` and `circular` are [numeric expression positions](../../abap-glossary/abennumerical_expr_position_glosry.md) of type `i`.

The return value has the type `string`.

## Hint

When `places` is specified, the function `shift_right` behaves differently than the statement `SHIFT` with the additions `RIGHT` and `PLACES`. The function `shift_right` reduces the length of the string, but the statement `SHIFT` lengthens it or it remains the same.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following program line

txt = shift_right( txt ).

has the same meaning as

txt = shift_right( val = txt sub = ` ` ).

and removes the trailing blanks from a string `txt`.

## Executable Example

[String Functions, `shift` and `substring`](abenstring_function_shift_abexa.md)

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_RANGE_OUT_OF_BOUNDS`

- *Cause:* Invalid value in `places`.

  *Runtime error:* `STRING_LENGTH_TOO_LARGE` or `STRING_LENGTH_NEGATIVE`
