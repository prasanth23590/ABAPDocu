---
title: "itab - Table Comprehensions, Join"
source_file: abentable_cmprhnsns_join_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Table Comprehensions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Table Comprehensions, Join

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a join between internal tables using a [table comprehension](../../abap-glossary/abentable_comprehension_glosry.md).

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
CLASS cl_demo_table_comprh_join DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_table_comprh_join IMPLEMENTATION. 
  METHOD main. 
    TYPES: 
      BEGIN OF line1, 
        key  TYPE c LENGTH 1, 
        col1 TYPE i, 
        col2 TYPE i, 
      END OF line1, 
      itab1 TYPE STANDARD TABLE OF line1 WITH EMPTY KEY, 
      BEGIN OF line2, 
        key  TYPE c LENGTH 1, 
        col1 TYPE i, 
        col2 TYPE i, 
      END OF line2, 
      itab2 TYPE STANDARD TABLE OF line2 WITH EMPTY KEY, 
      BEGIN OF line3, 
        key   TYPE c LENGTH 1, 
        col11 TYPE i, 
        col12 TYPE i, 
        col21 TYPE i, 
        col22 TYPE i, 
      END OF line3, 
      itab3 TYPE STANDARD TABLE OF line3 WITH EMPTY KEY. 
 
    FINAL(itab1) = VALUE itab1( 
      ( key = 'a' col1 = 11 col2 = 12 ) 
      ( key = 'b' col1 = 21 col2 = 22 ) 
      ( key = 'c' col1 = 31 col2 = 32 ) ). 
    out->write( itab1 ). 
 
    FINAL(itab2) = VALUE itab2( 
      ( key = 'a' col1 = 13 col2 = 14 ) 
      ( key = 'b' col1 = 23 col2 = 24 ) 
      ( key = 'c' col1 = 33 col2 = 34 ) ). 
    out->write( itab2 ). 
 
    FINAL(itab3) = VALUE itab3( 
      FOR wa IN itab1 
        ( key   = wa-key 
          col11 = wa-col1 
          col12 = wa-col2 
          col21 = itab2[ key = wa-key ]-col1 
          col22 = itab2[ key = wa-key ]-col2 ) ). 
    out->write( itab3 ). 
 
    FINAL(itab4) = VALUE itab3( 
      FOR wa1 IN itab1 INDEX INTO idx 
      FOR wa2 IN itab2 WHERE ( key = wa1-key ) 
        ( key   = wa1-key 
          col11 = wa1-col1 
          col12 = wa1-col2 
          col21 = wa2-col1 
          col22 = wa2-col2 ) ). 
    out->write( itab4 ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The lines of two internal tables `itab1` and `itab2` that have the same value in the column `key` are combined in a table. This example shows two options:

- The table `itab3` is created after a simple `FOR` expression for `itab1` in which the associated values are read using [table expressions](../../abap-glossary/abentable_expression_glosry.md) from `itab2`.

- The table `itab4` is created after consecutive `FOR` expressions for `itab1` and `itab2`. The last `FOR` expression is restricted by a `WHERE` condition.

In both cases, only those key values are evaluated in ` itab1`. In the second case, duplicate key values in `itab2` would also produce multiple lines in `itab4`.
