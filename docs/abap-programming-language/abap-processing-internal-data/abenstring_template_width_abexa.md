---
title: "string_tmpl - Specified Length"
source_file: abenstring_template_width_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp) > string_exp - String Templates (string_tmpl) > string_tmpl - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# string_tmpl - Specified Length

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how to specify a length for embedded expressions.

## Source Code

``` abap
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_str_template_width DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_str_template_width IMPLEMENTATION. 
  METHOD main. 
    TYPES result TYPE STANDARD TABLE OF string WITH EMPTY KEY. 
    FINAL(abcde) = 'abcdefghijklmnopqrstuvwxyz'. 
    out->write( 
      VALUE result( 
        FOR j = 1 UNTIL j > strlen( abcde ) 
        ( |{ substring( val = abcde len = j ) 
             WIDTH = j + 4 }<---| ) ) ). 
 
    out->write( 
      VALUE result( 
        FOR j = 1 UNTIL j > strlen( abcde ) 
        ( |{ substring( val = abcde len = j ) 
             WIDTH = strlen( abcde ) / 2 } <---| ) ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Two [iteration expressions](../abap-program-flow-logic/abenfor_conditional.md) perform the built-in function `substring` for the system field `sy-abcde` in an embedded expression of a string template. The first iteration calculates the length from the length of the substring plus a fixed value. The second iteration constantly sets the length to half the length of the full string and is therefore ignored for longer substring accesses.
