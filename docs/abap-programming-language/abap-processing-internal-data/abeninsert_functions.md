---
title: "cstring_func - insert"
source_file: abeninsert_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Processing Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - insert

## Syntax

``` abap
... insert( val = text sub = substring [off = off] ) ...  
```

[`val = text`](abenstring_functions_val.md) · [`sub = substring`](abenstring_functions_sub.md) · [`off = off`](abenstring_functions_off_len.md)

## Description

This [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) inserts the character string specified in [`substring`](abenstring_functions_sub.md) into the string specified in [`text`](abenstring_functions_val.md), either before the first character or at the optional offset specified [`off`](abenstring_functions_off_len.md) and returns the corresponding extended result. If `substring` is empty, the unchanged content of `text` is returned. Note that a character string in `substring` of a fixed length containing only blanks is handled like an empty string. This also applies to the predefined constant `space`. For more information, refer to [Trailing Blanks in Character String Processing](abenstring_processing_trail_blanks.md).

The return value has the type `string`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

After the following iteration has been executed, the result is in `result` *X X X X X*.

``` abap
DATA(result) = `XXXXX`. 
 
result = 
  REDUCE #( INIT r = result 
            FOR j = 1 UNTIL j > strlen( result ) - 1 
            NEXT r = insert( val = r sub = ` ` off = j * 2 - 1 ) ).
```

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_RANGE_OUT_OF_BOUNDS`

- *Cause:* Invalid offset specified in `places`.

  *Runtime error:* `STRING_OFFSET_TOO_LARGE`
