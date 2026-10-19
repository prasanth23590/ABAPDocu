---
title: "Sorting Internal Tables with Secondary Keys"
source_file: abensort_itab_sec_key_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > SORT itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Sorting Internal Tables with Secondary Keys

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how tables with secondary table keys are sorted.

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
CLASS cl_demo_int_tbls_sort_sec_key DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_int_tbls_sort_sec_key IMPLEMENTATION. 
  METHOD main. 
 
    DATA: BEGIN OF struct, 
            col1 TYPE c LENGTH 1, 
            col2 TYPE c LENGTH 1, 
          END OF struct. 
 
    DATA itab LIKE STANDARD TABLE OF struct 
         WITH NON-UNIQUE KEY col1 
         WITH UNIQUE HASHED KEY sec_key COMPONENTS col2. 
 
    DATA jtab LIKE itab. 
 
    itab = VALUE #( ( col1 = 'A' col2 = '1' ) 
                    ( col1 = 'A' col2 = '2' ) 
                    ( col1 = 'B' col2 = '3' ) 
                    ( col1 = 'B' col2 = '4' ) ). 
 
    LOOP AT itab INTO struct. 
      APPEND struct TO jtab. 
    ENDLOOP. 
    out->write_data( jtab ). 
 
    CLEAR jtab. 
    SORT itab BY col2 DESCENDING. 
 
    LOOP AT itab INTO struct. 
      APPEND struct TO jtab. 
    ENDLOOP. 
    out->write_data( jtab ). 
 
    CLEAR jtab. 
    LOOP AT itab INTO struct USING KEY sec_key. 
      APPEND struct TO jtab. 
    ENDLOOP. 
    out->write_data( jtab ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The table `itab` has a secondary hash key for the column `col2`. If the table is sorted in descending order using this column, the primary index is applied accordingly and a `LOOP` without a key produces the new order. If, however, [`USING KEY`](abaploop_at_itab_cond.md) is used to specify the secondary hash key in the loop, the table is processed in the order in which it was filled.
