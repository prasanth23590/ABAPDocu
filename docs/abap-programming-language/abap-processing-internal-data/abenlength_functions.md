---
title: "cstring_func - charlen, dbmaxlen, numofchar, strlen"
source_file: abenlength_functions.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Description Functions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - charlen, dbmaxlen, numofchar, strlen

These [built-in](../abap-built-in-types-data-objects-functions-and-constructors/abenbuilt_in_functions.md) length functions have an unnamed character-like parameter.

## Syntax

``` abap
... func( arg ) ...  
```

## Description

The following table shows the length functions with an unnamed parameter. The arguments `arg` of all length functions except `dbmaxlen` are [character-like expression positions](../../abap-glossary/abencharlike_expr_position_glosry.md). The argument of `dbmaxlen` is a character-like [functional operand position](../../abap-glossary/abenfunctional_position_glosry.md). The return value has the type `i` for all length functions.

| **Function func** | **Return Value**                                                                                                                                                                                                                                                                                                                                                    |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `charlen`         | Length of the first character of `arg` in the [code page](../../abap-glossary/abencodepage_glosry.md) used: 1 for a single Unicode character; 2 for [surrogate pairs](../../abap-glossary/abensurrogates_glosry.md).                                                                                                                                                                                    |
| `dbmaxlen`        | Maximum length of a string defined in the ABAP Dictionary (`RAWSTRING`, `SSTRING`, `STRING`, or `GEOM_EWKB`). If the string is unrestricted, the constant `abap_max_db_string_ln` or `abap_max_db_rawstring_ln` from the [type pool](../../abap-glossary/abentype_pool_glosry.md) `ABAP` is returned. The latter is also returned for the built-in ABAP types `string` and `xstring`. |
| `numofchar`       | Number of characters in `arg`, where trailing blanks are neither counted in data objects with fixed lengths nor in data objects with the type `string`.                                                                                                                                                                                                             |
| `strlen`          | Number of characters in `arg`, where trailing blanks in data objects with fixed lengths are not counted, whereas in data objects with the type `string` they are.                                                                                                                                                                                                   |

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The results of the following length determinations are 10 and 5.

``` abap
DATA: 
  str TYPE string      VALUE `12345     `, 
  txt TYPE c LENGTH 10 VALUE '12345     '. 
 
cl_demo_output=>display( |{ strlen( str ) 
                       }, { strlen( txt ) }| ).
```

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The result of function `strlen` is 2 because ABAP handles the [surrogate pair](../../abap-glossary/abensurrogate_pair_glosry.md) in the character string as two [UCS-2](../../abap-glossary/abenucs2_glosry.md) characters. When [counting](abencount_functions.md) with a regular expression in [PCRE syntax](abenregex_pcre_syntax.md) that is introduced with `(*UTF)`, the result is 1, because the surrogate pair is interpreted as one [UTF-16](../../abap-glossary/abenutf16_glosry.md) character.

``` abap
FINAL(surrogate_pair) = cl_abap_codepage=>convert_from( 
  codepage = 'UTF-8' 
  source    = CONV xstring( 'F09F91BD' ) ). 
                            "U+1F47D, EXTRATERRESTRIAL ALIEN 
 
cl_demo_output=>write_text( surrogate_pair ). 
 
FINAL(ucs2_len)  = strlen( surrogate_pair ). 
cl_demo_output=>write( ucs2_len ). 
FINAL(utf16_len) = count( val = surrogate_pair pcre = `(*UTF).` ). 
cl_demo_output=>write( utf16_len ). 
 
cl_demo_output=>display( ).
```
