---
title: "Sorting Internal Tables"
source_file: abensort_stable_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > SORT itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Sorting Internal Tables

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how internal tables are sorted using [`SORT itab`](abapsort_itab.md).

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
CLASS cl_demo_int_tbls_sort DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_int_tbls_sort IMPLEMENTATION. 
  METHOD main. 
 
    TYPES: BEGIN OF line, 
             land   TYPE c LENGTH 3, 
             name   TYPE c LENGTH 10, 
             age    TYPE i, 
             weight TYPE p LENGTH 8 DECIMALS 2, 
           END OF line. 
 
    DATA itab TYPE STANDARD TABLE OF line WITH NON-UNIQUE KEY land. 
 
    itab = 
      VALUE #( 
        ( land = 'D'   name = 'Hans'    age = 20 weight = '80.00' ) 
        ( land = 'USA' name = 'Nancy'   age = 35 weight = '45.00' ) 
        ( land = 'USA' name = 'Howard'  age = 40 weight = '95.00' ) 
        ( land = 'GB'  name = 'Jenny'   age = 18 weight = '50.00' ) 
        ( land = 'F'   name = 'Michele' age = 30 weight = '60.00' ) 
        ( land = 'G'   name = 'Karl'    age = 60 weight = '75.00' ) ). 
 
    SORT itab. 
    out->write_data( itab ). 
 
    SORT itab. 
    out->write_data( itab ). 
 
    SORT itab STABLE. 
    out->write_data( itab ). 
 
    SORT itab DESCENDING BY land weight ASCENDING. 
    out->write_data( itab ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The class sorts a standard table with one key field four times. First, the table is sorted twice by the key field (`land`) without the `STABLE` addition. The sort is unstable. The order of lines in which multiple keys appear can change. The same sort is then performed using the `STABLE` addition. The sort is stable. The lines remain in the same sequence. Then, it is sorted by a sort key defined as `land` and `weight`. The general sort order is defined as descending, but for `weight` it is defined as ascending.
