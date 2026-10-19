---
title: "cstring_func - segment"
source_file: abensegment_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Processing Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - segment

## Syntax

``` abap
 ... segment( val = text index = idx [sep|space = delim] ) ...  
```

[`val = text`](abenstring_functions_val.md)

## Description

This [built-in function](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) returns the occurrence of a segment of the argument `text` specified by [`index`](abenstring_functions_val.md). A segment is defined by limits. The start and end of the string in `text` are the outer limits. Inner limits `delim` can be passed to `sep` or `space` as follows:

- If the parameter `sep` is supplied, the substring specified in `delim` is searched for (case-sensitive) in `text` and used as a limit. If a substring specified in `delim` occurs directly one after another in `text`, an empty segment is created, and an empty string is returned for this segment.

- If the parameter `space` is supplied, each individual character is searched for in `delim` (case-sensitive) and this is used as a limit. If the individual characters specified in `delim` occur directly one after another in `text`, no empty segment is created, and no result is returned.

The limits are not part of the segments. If `sep` or `space` are not specified, the parameter `sep` is supplied implicitly a single blank. In both cases, specifying an empty string raises an exception of the class `CX_SY_STRG_PAR_VAL`.

If `index` is positive, the occurrences are counted from the left and if `index` is negative from the right. The values 1, 2, .... indicate the first, second, ... occurrence. The values -1, -2, .... indicate the last, last but one, ... occurrences. If the value of `index` is 0, or the specified segment does not exist, an exception of the class `CX_SY_STRG_PAR_VAL` is raised.

`delim` is a [character-like expression position](../../abap-glossary/abencharlike_expr_position_glosry.md) and `index` is a [numeric expression position](../../abap-glossary/abennumerical_expr_position_glosry.md) with type `i`. If `delim` has a fixed length, any trailing blanks are ignored.

The return value has the type `string`.

## Hint

If the substring specified in `delim` is not found, the entire character string forms a single segment, which can only be addressed by using the values 1 or -1 for `index`.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The following function calls return *AB*, *CD*, *EF*, and *GH* respectively, and raise an exception at the end.

``` abap
DATA  result TYPE string. 
 
DO. 
  TRY. 
      result = segment( val   = 'AB\brCD\brEF\brGH' 
                        index = sy-index 
                        sep   = `\br` ). 
      ... 
    CATCH cx_sy_strg_par_val. 
      EXIT. 
  ENDTRY. 
ENDDO. 
 
DO. 
  TRY. 
      result = segment( val   = 'AB  CD - EF_GH' 
                        index = sy-index 
                        space = ` -_` ). 
      ... 
    CATCH cx_sy_strg_par_val. 
      EXIT. 
  ENDTRY. 
ENDDO.
```

## Executable Example

[String Functions, `cmax`, `cmin`, and `segment`](abencmax_cmin_function_abexa.md)

**[Exceptions](../abap-program-flow-logic/abenabap_language_exceptions.md)**

### Catchable Exceptions

`CX_SY_STRG_PAR_VAL`

- *Cause:* limit in `sep` is empty or the occurrence in `index` is 0 or was not found.

  *Runtime error:* `STRG_ILLEGAL_PAR`
