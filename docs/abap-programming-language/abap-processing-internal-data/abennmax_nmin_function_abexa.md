---
title: "num_func - Extremum Functions nmax, nmin"
source_file: abennmax_nmin_function_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func) > num_func - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - Extremum Functions nmax, nmin

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the extremum functions [`nmax`](abennmax_nmin_functions.md) and [`nmin`](abennmax_nmin_functions.md).

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
CLASS cl_demo_nmax_nmin DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_nmax_nmin IMPLEMENTATION. 
  METHOD main. 
    DATA: a TYPE i VALUE 1, 
          b TYPE i VALUE 0, 
          c TYPE i VALUE 0. 
    cl_demo_input=>new( 
      )->add_text( `Parabola:` 
      )->add_field( CHANGING field = a 
      )->add_field( CHANGING field = b 
      )->add_field( CHANGING field = c )->request( ). 
    IF a = 0. 
      out->write( 
        'You must enter a non-zero value for a' ). 
      RETURN. 
    ENDIF. 
 
    CONSTANTS: xmin TYPE i VALUE -100, 
               xmax TYPE i VALUE 100, 
               n    TYPE i VALUE 20000. 
    DATA: x  TYPE decfloat34, 
          y  TYPE decfloat34, 
          y0 TYPE decfloat34. 
    DATA       txt  TYPE string. 
 
    DO n + 1 TIMES. 
      x = ( xmax - xmin ) / n * ( sy-index - 1 ) + xmin. 
      y = a * x ** 2 + b * x + c. 
      IF sy-index = 1. 
        y0 = y. 
      ELSE. 
        IF a > 0. 
          txt = 'Minimum'. 
          y0 = nmin( val1 = y0 val2 = y ). 
        ELSE. 
          txt = 'Maximum'. 
          y0 = nmax( val1 = y0 val2 = y ). 
        ENDIF. 
      ENDIF. 
    ENDDO. 
    out->write( |{ txt } value of parabola is: { y0 }| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This class determines the minimum or maximum value of a parabola opened up or down and whose parameters can be entered on the selection screen.
