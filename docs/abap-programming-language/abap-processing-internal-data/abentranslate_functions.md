---
title: "cstring_func - translate"
source_file: abentranslate_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Processing Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - translate

## Syntax

``` abap
... translate( val = text from = from to = to ) ...  
```

[`val = text`](abenstring_functions_val.md)

## Description

This [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) returns the character string from [`text`](abenstring_functions_val.md) where each character that occurs in `from` is replaced by the character that occurs in the same place in `to` as in `from`. If `to` is shorter than `from`, the surplus characters from `from` are removed from the character string. If `from` is an empty string, the content of `text` is returned unchanged.

`from` and `to` are [character-like expression positions](../../abap-glossary/abencharlike_expr_position_glosry.md). If they have a fixed length, trailing blanks are ignored.

The return value has the type `string`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The return value of the following function call is *Horray!*.

``` abap
FINAL(result) = translate( 
  val = `---Hur-rah!---` from = `uh-` to = `oy` ).
```
