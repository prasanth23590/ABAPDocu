---
title: "CL_ABAP_BIGINT, Square Root Calculation"
source_file: abenbigint1_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > System Classes for Numbers > System Class CL_ABAP_BIGINT"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_BIGINT, Square Root Calculation

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example uses methods of the system class `CL_ABAP_BIGINT` to calculate the square root of a natural number to any number of decimal places.

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
CLASS cl_demo_bigint_sqrt DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    DATA:p_int    TYPE i VALUE 2, 
         p_digits TYPE i VALUE 1000. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_bigint_sqrt IMPLEMENTATION. 
  METHOD main. 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = p_int 
     )->add_field( CHANGING field = p_digits 
     )->request( ). 
 
    " compute arbitrary many digits of sqrt( p_int ) 
 
 
    " compute the integer square root and add "2 * p_digits" 
    " 0s at the end to get the "rational" part 
    " at the end only the decimal point has to be positioned at the 
    " right place 
    out->write_html( 
      shift_right( val = 
        shift_right( val = REDUCE string( LET number_string = 
          shift_left( val = |{ p_int NUMBER = RAW }| && 
          repeat( val = `0` occ = p_digits * 2 ) sub = `0` ) 
          sqrt = cl_abap_bigint=>factory_from_string( 
            number_string )->sqrt( )->to_string( ) 
                             IN INIT sqrt_str = `` 
                             FOR n = 0 UNTIL n >= strlen( sqrt ) 
                             LET char = sqrt+n(1) IN 
                             NEXT  sqrt_str = sqrt_str && 
                             COND #( WHEN n = strlen( sqrt ) - p_digits 
                             THEN `.` && char ELSE char ) ) 
                  sub = `0` ) 
                  sub = `.` ) 
    ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The user can enter two integers:

- `p_int` is an integer that the square root will be calculated from.

- `p_digits` specifies the number of decimal places of the result.

Methods of the system class `CL_ABAP_BIGINT` are used to return the square root of `p_int` with the required number of decimal places.
