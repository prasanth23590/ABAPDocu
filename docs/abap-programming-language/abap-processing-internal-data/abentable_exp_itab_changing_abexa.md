---
title: "table_exp - Write Positions"
source_file: abentable_exp_itab_changing_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > itab - Table Expressions (table_exp) > table_exp - Write Positions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# table_exp - Write Positions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates table expressions in write positions.

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
CLASS cl_demo_tab_exp_changing DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    TYPES: 
      BEGIN OF struct, 
        col1 TYPE i, 
        col2 TYPE i, 
      END OF struct, 
      itab TYPE STANDARD TABLE OF struct WITH EMPTY KEY. 
    METHODS: 
      change_component 
        IMPORTING p1 TYPE i 
        EXPORTING p2 TYPE i, 
      change_line 
        CHANGING p TYPE struct. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_tab_exp_changing IMPLEMENTATION. 
  METHOD main. 
    DATA(itab) = VALUE itab( 
                   ( col1 = 3 ) 
                   ( col1 = 5 ) 
                   ( col1 = 7 ) ). 
 
    out->begin_section( `Before` 
      )->write( itab ). 
 
    DO lines( itab ) TIMES. 
      change_component( EXPORTING p1 = itab[ sy-index ]-col1 
                        IMPORTING p2 = itab[ sy-index ]-col2 ). 
    ENDDO. 
 
    out->next_section( `After change_component` 
      )->write( itab ). 
 
    DO lines( itab ) TIMES. 
      change_line( CHANGING p = itab[ sy-index ] ). 
    ENDDO. 
 
    out->next_section( `After change_line` 
      )->write( itab ). 
 
  ENDMETHOD. 
  METHOD change_component. 
    p2 = ipow( base = p1 exp = 2 ). 
  ENDMETHOD. 
  METHOD change_line. 
    p-col2 = ipow( base = p-col1 exp = 3 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In a `DO` loop, the content of an internal table

- is passed component by component to an `IMPORTING` parameter and `EXPORTING` parameter of a method using two [table expressions](abentable_expressions.md). This modifies one column of the current line.

- is passed line by line to a `CHANGING` parameter of a method using one [table expression](abentable_expressions.md). This modifies one column of the table line.

The second method is quicker, of course, since only one read is performed on the internal table instead of two.
