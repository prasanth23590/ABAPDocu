---
title: "cstring_func - distance"
source_file: abendistance_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Description Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - distance

## Syntax

``` abap
... distance( val1 = text1 val2 = text2 [max = max] ) ...  
```

[`val1 = text1`](abenstring_functions_val.md) · [`val2 = text2`](abenstring_functions_val.md)

## Description

This [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) returns the Levenshtein distance between two strings [`text1`](abenstring_functions_val.md) and [`text2`](abenstring_functions_val.md). This distance is the minimum number of insert, delete, and replace operations required to pass one string to another and hence reflects the similarity of the two strings. The return value has the type `i`.

`max` can be used to specify a positive value other than 0, that terminates the calculation of the Levenshtein distance if the distance is greater than `max`. The value `max` is then returned instead. `max` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) with type `i`. If the value of `max` is less than or equal to 0, an exception of the class `CX_SY_STRG_PAR_VAL` is raised. If `max` is not specified, the calculation is not terminated

## Hints

- The complexity of the function increases in line with the product of the lengths of the two strings. The calculation time can be limited by specifying `max`.

- This function can typically be used to find those words in a word set that are most similar to a word entered in a search using the minimum editing space.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of the following function calls is 0, 1, and 3.

``` abap
FINAL(result1) = distance( val1 = `abcdefg` val2 = `abcdefg` ). 
FINAL(result2) = distance( val1 = `abcdefg` val2 = `abcXefg` ). 
FINAL(result3) = distance( val1 = `abcdefg` val2 = `aXcdXXg` ).
```

## Executable Example

String Functions, `distance`

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_STRG_PAR_VAL`

- *Cause:* Value in `max` is less than or equal to 0.

  *Runtime error:* `STRG_ILLEGAL_PAR`
