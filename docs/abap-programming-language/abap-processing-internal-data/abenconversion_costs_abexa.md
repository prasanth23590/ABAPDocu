---
title: "Conversion Costs"
source_file: abenconversion_costs_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversions, Performance Notes"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Conversion Costs

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates costs for type conversions in assignments and operand positions.

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
CLASS cl_demo_conversion_costs DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_conversion_costs IMPLEMENTATION. 
  METHOD main. 
    DATA: num     TYPE n LENGTH 10, 
          int     TYPE i, 
          itab    TYPE STANDARD TABLE OF i, 
          t1      TYPE utclong, 
          t2      TYPE utclong, 
          tn      TYPE decfloat34, 
          ti      TYPE decfloat34, 
          seconds TYPE decfloat34. 
    CONSTANTS n TYPE i VALUE 100000. 
 
    t1 = utclong_current( ). 
    DO n TIMES. 
    ENDDO. 
    t2 = utclong_current( ). 
    cl_abap_utclong=>diff( EXPORTING high    = t2 
                                       low   = t1 
                           IMPORTING seconds = DATA(toff1) ). 
 
 
    t1 = utclong_current( ). 
    DO n TIMES. 
      num = sy-index. 
    ENDDO. 
    t2 = utclong_current( ). 
    cl_abap_utclong=>diff( EXPORTING high    = t2 
                                     low   = t1 
                           IMPORTING seconds = DATA(toff2) ). 
 
    tn = toff2 - toff1. 
 
    t1 = utclong_current( ). 
    DO n TIMES. 
      int = sy-index. 
    ENDDO. 
    t2 = utclong_current( ). 
    cl_abap_utclong=>diff( EXPORTING high    = t2 
                                     low   = t1 
                           IMPORTING seconds = DATA(toff3) ). 
    ti = toff3 - toff1. 
 
    out->write( 
      |Ratio of conversion to copy during assignment: | && 
      |{ tn / ti DECIMALS = 2 }| ). 
 
    itab = VALUE #( ( 1 ) ). 
    CLEAR: tn, ti. 
 
    num = '1'. 
    t1 = utclong_current( ). 
    DO n TIMES. 
      READ TABLE itab TRANSPORTING NO FIELDS INDEX num. 
    ENDDO. 
    t2 = utclong_current( ). 
    cl_abap_utclong=>diff( EXPORTING high    = t2 
                                     low   = t1 
                           IMPORTING seconds = DATA(toff4) ). 
    tn = toff4 - toff1. 
 
    int = 1. 
    t1 = utclong_current( ). 
    DO n TIMES. 
      READ TABLE itab TRANSPORTING NO FIELDS INDEX int. 
    ENDDO. 
    t2 = utclong_current( ). 
    cl_abap_utclong=>diff( EXPORTING high    = t2 
                                     low   = t1 
                           IMPORTING seconds = DATA(toff5) ). 
    ti = toff5 - toff1. 
 
    out->write( 
      |Ratio of conversion to copy during assignment: | && 
      |{ tn / ti DECIMALS = 2 }| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The class calculates the ratio of the costs of a conversion from type `n` to `i` and the costs of a direct memory copy from type `i` to `i`. The conversion is much slower than the unconverted copy, which is visible directly in the assignment. The difference is less significant in an operand position, here when specifying the index of a `READ` statement. This is because the conversion costs are not as high as for a table access.
