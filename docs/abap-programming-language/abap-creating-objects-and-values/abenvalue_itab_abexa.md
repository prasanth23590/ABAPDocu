---
title: "VALUE, Operator for Internal Tables"
source_file: abenvalue_itab_abexa.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > VALUE, Value Operator > VALUE, Internal Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# VALUE, Operator for Internal Tables

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the value operator [`VALUE`](abenvalue_constructor_params_itab.md) for internal tables.

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
CLASS cl_demo_value_constructor_itab DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_value_constructor_itab IMPLEMENTATION. 
  METHOD main. 
 
    TYPES itab TYPE STANDARD TABLE OF i WITH EMPTY KEY. 
 
    FINAL(itab) = VALUE itab( ( 1 ) ( 2 ) ( 3 ) ). 
 
    DATA(itab1) = itab. 
    itab1 = VALUE #(  BASE itab1 
                     ( 4 ) 
                     ( 5 ) ). 
    out->write( itab1 ). 
 
    DATA(itab2) = itab. 
    itab2 = VALUE #( ( LINES OF itab2 ) 
                      ( 4 ) 
                      ( 5 ) ). 
    out->write( itab2 ). 
 
    DATA(itab3) = itab. 
    itab3 = VALUE #( BASE itab3 
                     ( LINES OF itab3 ) 
                     ( 4 ) 
                     ( 5 ) ). 
    out->write( itab3 ). 
 
    DATA(itab4) = itab. 
    itab4 = VALUE #( LET x = itab4 IN 
                     ( LINES OF x ) 
                     ( 4 ) 
                     ( 5 ) ). 
    out->write( itab4 ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example shows various effects when using the left side of an assignment in line specifications of the operator `VALUE` in the construction of internal tables.

- In the construction of `itab1`, the left side is used after `BASE`. Here, it is passed the original three lines as a start value before the line specifications are evaluated. Two single lines are then appended to this start value.

- In the construction of `itab2`, the left side is initialized before the line specifications are evaluated. This is why no lines are inserted by `LINES OF itab2` and the table contains only two single lines.

- In the construction of `itab3`, the left side is given its original three lines as a start line using `BASE`. They are then appended again using `LINES OF`, before the two single lines are appended.

- In the construction of `itab4`, the left side is saved in the helper variable `x` before it is initialization and is then used in `LINES OF`. The result is the same as when the left side is used after `BASE`.
