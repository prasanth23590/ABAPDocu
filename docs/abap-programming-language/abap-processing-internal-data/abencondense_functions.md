---
title: "cstring_func - condense"
source_file: abencondense_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Processing Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - condense

## Syntax

``` abap
... condense( [val =] text [del = del] [from = from] [to = to] ) ...  
```

[`[val =] text`](abenstring_functions_val.md)

## Description

This [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) returns a condensed content of [`text`](abenstring_functions_val.md). The function works as follows:

1.  First, all leading and trailing characters are removed, that are specified in `del`. If `del` is an empty string, no leading and trailing characters are removed.

2.  Second, in the remaining string all substrings composed of characters specified in `from` are replaced with the first character of the string specified in `to`. If `from` is an empty string, no characters are replaced. If `to` is an empty string, the characters specified in `from` are removed.

The default values for `del`, `from`, and `to` are one blank each. If neither `del`, `from`, nor `to` are specified, `val =` can also be omitted. Then, the `condense` function first removes any leading and trailing blanks and then all substrings of the remaining character string that contain nothing but blanks are replaced by exactly one blank.

`del`, `from`, and `to` are [character-like expression positions](../../abap-glossary/abencharlike_expr_position_glosry.md). If these have a fixed length, trailing blanks are ignored.

The return value has the type `string`.

## Hints

- Comparison with the [`CONDENSE`](abapcondense.md) statement:

  - When `del`, `from`, and `to` are not specified or their default values (one blank) are passed, the `condense` function works in the same way as the [`CONDENSE`](abapcondense.md) statement without the `NO-GAPS` addition.

  - When for `del` and `from` their default values (one blank) are passed and for `to` an empty string is passed, the `condense` function works in the same way as the [`CONDENSE`](abapcondense.md) statement with the `NO-GAPS` addition.

- When using default values, the effect of condensing substrings containing nothing than blanks to one blank, comes from applying the default values for `from` and `to` and has nothing to do with the value of `del`.

- For removing the leading and trailing blanks without affecting the remaining character string, you can use the default value for `del` and an empty string for `from`. The latter must be specified explicitly, because the default value (blank) causes substrings consisting of blanks to be replaced by the first character from `to`, which also is a blank.

- Specifying a text field literal `' '` containing one blank for `del`, `from`, and `to` is the same as specifying \`\`\`\` but not the same as\` `` ` ` ``. Only the latter represents the default value.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The return values of the following functions are *abc_def*, *abc\_\_\_def*, *abcdef* and *abcXdef*, where *\_* stands for a blank.

``` abap
DATA result TYPE string. 
 
result = condense( val = `  abc   def  ` ). 
 
result = condense( val = `  abc   def  ` from = `` ). 
 
result = condense( val = `  abc   def  ` to = `` ). 
 
result = condense( val = `XXabcXXXdefXX` 
                   del = 'X' from = 'X' to = 'X' ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The return value of the following function call is *Rock'n'Roll*.

``` abap
FINAL(result) = condense( val  = `  Rock'xxx'Roller` 
                         del  = `re ` 
                         from = `x` to = `n`  ).
```
