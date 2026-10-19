---
title: "itab - Insert Lines"
source_file: abeninsert_lines_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > INSERT itab"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Insert Lines

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how lines are inserted into internal tables.

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
CLASS cl_demo_int_tbls_insert DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_int_tbls_insert IMPLEMENTATION. 
  METHOD main. 
    TYPES: BEGIN OF line, 
             col1 TYPE i, 
             col2 TYPE i, 
           END OF line. 
 
    DATA: itab  TYPE TABLE OF line WITH EMPTY KEY, 
          jtab  LIKE itab, 
 
          itab1 TYPE TABLE OF line WITH EMPTY KEY, 
          jtab1 LIKE itab, 
          itab2 TYPE TABLE OF line WITH EMPTY KEY, 
          jtab2 TYPE SORTED TABLE OF line 
                WITH NON-UNIQUE KEY col1 col2. 
 
    itab = VALUE #( FOR i = 1 UNTIL i > 3 
                   ( VALUE #( col1 = i col2 = i ** 2 ) ) ). 
    out->write( itab ). 
    jtab = VALUE #( FOR i = 1 UNTIL i > 3 
                   ( VALUE #( col1 = i col2 = i ** 3 ) ) ). 
    out->write( jtab ). 
 
    "Insert a single line into an index table 
    itab1 = itab. 
    INSERT VALUE #( col1 = 11 col2 = 22 ) INTO itab1 INDEX 2. 
    INSERT INITIAL LINE INTO itab1 INDEX 1. 
    out->write( itab1 ). 
 
    "Insert lines into an index table with LOOP 
    itab1 = itab. 
    LOOP AT itab1 ASSIGNING FIELD-SYMBOL(<line>). 
      INSERT VALUE #( col1 = 3 * sy-tabix col2 = 5 * sy-tabix ) 
             INTO itab1. 
    ENDLOOP. 
    out->write( itab1 ). 
 
    "Insert lines into an index table 
    itab1 = itab. 
    jtab1 = jtab. 
    INSERT LINES OF itab1 INTO jtab1 INDEX 1. 
    out->write( jtab1 ). 
 
    "Insert lines into a sorted table 
    itab2 = itab. 
    jtab2 = jtab. 
    INSERT LINES OF itab2 INTO TABLE jtab2. 
    out->write( jtab2 ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example is consists of four parts where lines are inserted in different ways. First, two internal tables, `itab` and `jtab`, are filled with squared and cubic numbers. These are also used to reset the tables above to their initial values, using an assignment, between the individual parts of the example.

- In the first part, a new line is inserted in front of the second line and a line with initial values is inserted in front of the first line.

- Next, using a `LOOP`, a new line is inserted before each existing line.

- In the third part, the whole of the table `itab1` is inserted in front of the first line of `jtab1`.

- In the final part, the whole of the table `itab2` is inserted into the sorted table `jtab2`.
