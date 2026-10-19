---
title: "itab - Table Comprehensions, Multiple Lines"
source_file: abentable_cmprhnsns_lines_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Table Comprehensions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Table Comprehensions, Multiple Lines

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how multiple lines in a [`FOR` expression](abenfor_in_itab.md) of a table [comprehension](../../abap-glossary/abentable_comprehension_glosry.md) are created.

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
CLASS cl_demo_table_comprh_lines DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_table_comprh_lines IMPLEMENTATION. 
  METHOD main. 
    TYPES: 
      BEGIN OF line1, 
        col1 TYPE i, 
        col2 TYPE i, 
        col3 TYPE i, 
      END OF line1, 
      itab1 TYPE STANDARD TABLE OF line1 WITH EMPTY KEY, 
      itab2 TYPE STANDARD TABLE OF i     WITH EMPTY KEY. 
 
    FINAL(itab1) = VALUE itab1( 
      ( col1 = 11 col2 = 12 col3 = 13 ) 
      ( col1 = 21 col2 = 22 col3 = 23 ) 
      ( col1 = 31 col2 = 32 col3 = 33 ) ). 
    out->write( itab1 ). 
 
    FINAL(itab2) = VALUE itab2( 
      FOR wa IN itab1 
        ( wa-col1 ) 
        ( wa-col2 ) 
        ( wa-col3 ) ). 
    out->write( itab2 ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The columns of `itabl` are created as individual lines after its `FOR` expression. The result is a single-column internal table `itab2` that contains the content of `itab1` as an array
