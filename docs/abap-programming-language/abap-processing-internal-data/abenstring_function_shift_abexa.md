---
title: "cstring_func - shift and substring"
source_file: abenstring_function_shift_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - shift and substring

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the string functions [`shift`](abenshift_functions.md) and [`substring`](abensubstring_functions.md).

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
CLASS cl_demo_shift_substring DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_shift_substring IMPLEMENTATION. 
  METHOD main. 
    DATA output TYPE TABLE OF string. 
    output = VALUE #( 
      ( `            oo            ` ) ). 
    output = VALUE #( 
      LET n = strlen( output[ 1 ] ) IN 
      BASE output 
      FOR j = 2 UNTIL j > n / 2 
      LET r = output[ j - 1 ] l = strlen( r ) / 2 IN 
        ( shift_left(  val = substring( val = r 
                                        len = l ) 
                                        circular = 1 ) && 
          shift_right( val = substring( val = r 
                                        off = l ) 
                                        circular = 1 ) ) ). 
    output = VALUE #( 
      LET n = strlen( output[ 1 ] ) IN 
      BASE output 
      FOR j = n / 2 + 1 UNTIL j > n - 1 
      LET r = output[ j - 1 ] l = strlen( r ) / 2 IN 
        ( shift_right( val = substring( val = r 
                                        len = l ) 
                                        circular = 1 ) && 
          shift_left(  val = substring( val = r 
                                        off = l ) 
                                        circular = 1 ) ) ). 
    out->write( output ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This class creates a diamond shape in the display.
