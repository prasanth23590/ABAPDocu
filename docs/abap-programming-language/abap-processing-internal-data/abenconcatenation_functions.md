---
title: "cstring_func - concat_lines_of"
source_file: abenconcatenation_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Processing Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - concat_lines_of

## Syntax

``` abap
... concat_lines_of( [table =] itab [sep = sep] ) ...  
```

## Description

This [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) concatenates all line content of an internal table `itab` and returns the result as a character string. `itab` expects an [index table](../../abap-glossary/abenindex_table_glosry.md) with character-like line type. `itab` is a [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md).

`sep` can be used to specify a string as a separator, which is then inserted between the lines. `sep` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md). If `sep` is not specified, the line content of the internal table is appended to each other directly. If the line types or the argument `sep` have a fixed length, trailing blanks are ignored.

The formal parameter `table` must be specified explicitly only if `sep` is also specified.

The return value has the type `string`.

## Hint

The [concatenation operator](../../abap-glossary/abenconcatenation_operator_glosry.md) `&&` can be used to concatenate elementary character strings.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This function returns *ABAP Objects*.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES: c80  TYPE c LENGTH 80, 
       itab TYPE TABLE OF c80 WITH EMPTY KEY. 
 
FINAL(itab) = VALUE itab( ( 'ABAP' ) ( 'Objects' ) ). 
 
out->write( 
  concat_lines_of( table = itab sep = ` ` ) ). 
 
out->display( ).
```
