---
title: "Class for Trailing Blanks"
source_file: abenstring_util.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > System Classes for Character String and Byte String Processing"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Class for Trailing Blanks

The class `CL_ABAP_STRING_UTILITIES` contains methods for processing [text strings](../../abap-glossary/abentext_string_glosry.md).

- `C2STR_PRESERVING_BLANKS` assigns text fields while preserving the trailing blanks.

- `DEL_TRAILING_BLANKS` deletes the trailing blanks from strings.

## Hint

Tasks like this can now also be performed using statements and built-in functions.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The program compares the method `C2STR_PRESERVING_BLANKS` with the built-in function [`shift_right`](abenshift_functions.md). The implementation of the method now consists of nothing more than this function.

``` abap
FINAL(str) = `abc   `. 
 
DATA(rslt) = str. 
cl_abap_string_utilities=>del_trailing_blanks( CHANGING str = rslt ). 
 
ASSERT rslt =  shift_right( str ).
```
