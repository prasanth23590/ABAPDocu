---
title: "MOVE-CORRESPONDING for Internal Tables"
source_file: abenmove_corresponding_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MOVE-CORRESPONDING for Internal Tables

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the statement [`MOVE-CORRESPONDING`](abapmove-corresponding.md) for internal tables.

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
CLASS cl_demo_move_crrspndng_itab DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    TYPES: 
      c3 TYPE c LENGTH 3, 
      BEGIN OF iline1, 
        col1 TYPE c3, 
        col2 TYPE c3, 
      END OF iline1, 
      BEGIN OF iline2, 
        col2 TYPE c3, 
        col3 TYPE c3, 
      END OF iline2, 
      BEGIN OF line1, 
        col1 TYPE                   c3, 
        col2 TYPE                   c3, 
        col3 TYPE STANDARD TABLE OF iline1 WITH EMPTY KEY, 
      END OF line1, 
      BEGIN OF line2, 
        col2 TYPE                   c3, 
        col3 TYPE STANDARD TABLE OF iline2 WITH EMPTY KEY, 
        col4 TYPE                   c3, 
      END OF line2. 
    DATA: 
      itab1 TYPE STANDARD TABLE OF line1 WITH EMPTY KEY, 
      itab2 TYPE STANDARD TABLE OF line2 WITH EMPTY KEY. 
    METHODS: 
      fill_tables. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_move_crrspndng_itab IMPLEMENTATION. 
  METHOD main. 
    DATA buffer LIKE itab2. 
 
    fill_tables( ). 
 
    out->begin_section( `itab1` 
      )->write( itab1 
      )->next_section( `itab2` 
      )->write( itab2 ). 
    buffer = itab2. 
 
    out->begin_section( 
      `MOVE-CORRESPONDING` ). 
 
    MOVE-CORRESPONDING itab1 TO itab2. 
 
    out->write( itab2 ). 
    itab2 = buffer. 
    out->next_section( 
      `MOVE-CORRESPONDING KEEPING TARGET LINES` ). 
 
    MOVE-CORRESPONDING itab1 TO itab2 KEEPING TARGET LINES. 
 
    out->write( itab2 ). 
    itab2 = buffer. 
    out->next_section( 
      `MOVE-CORRESPONDING EXPANDING NESTED TABLES` ). 
 
    MOVE-CORRESPONDING itab1 TO itab2 EXPANDING NESTED TABLES. 
 
    out->write( itab2 ). 
    itab2 = buffer. 
    out->next_section( 
      `MOVE-CORRESPONDING EXPANDING NESTED TABLES ` && 
      `KEEPING TARGET LINES` ). 
 
    MOVE-CORRESPONDING itab1 TO itab2 EXPANDING NESTED TABLES 
                                      KEEPING TARGET LINES. 
 
    out->write( itab2 ). 
  ENDMETHOD. 
  METHOD fill_tables. 
    itab1 = VALUE #( 
      ( col1 = 'a11' 
        col2 = 'a12' 
        col3 = VALUE #( ( col1 = 'a11'  col2 = 'a12' ) 
                        ( col1 = 'a21'  col2 = 'a22' ) ) ) 
      ( col1 = 'b21' 
        col2 = 'b22' 
        col3 = VALUE #( ( col1 = 'b11'  col2 = 'b12' ) 
                        ( col1 = 'b21'  col2 = 'b22' ) ) ) 
      ( col1 = 'c31' 
        col2 = 'c32' 
        col3 = VALUE #( ( col1 = 'c11'  col2 = 'c12' ) 
                        ( col1 = 'c21'  col2 = 'c22' ) ) ) ). 
 
    itab2 = VALUE #( 
      ( col2 = 'x11' 
        col3 = VALUE #( ( col2 = 'x11'  col3 = 'x12' ) 
                        ( col2 = 'x21'  col3 = 'x22' ) 
                        ( col2 = 'x31'  col3 = 'x32' ) ) 
        col4 = 'x12' ) 
      ( col2 = 'y21' 
        col3 = VALUE #( ( col2 = 'y11'  col3 = 'y12' ) 
                        ( col2 = 'y21'  col3 = 'y22' ) 
                        ( col2 = 'y31'  col3 = 'y32' ) ) 
        col4 = 'y22' ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Two structures, `struct1` and `struct2` are declared using the available additions and [`MOVE-CORRESPONDING`](abapmove-corresponding.md) assigns `struct1` to `struct2`.

- `itab1` contains two elementary components, `col1` and `col2`, and a tabular component `col3` with the components `col1` and `col2`.

- `itab2` contains two elementary components, `col2` and `col4`, and a tabular component `col3` with the components `col2` and `col3`.

The internal tables are filled with values. For the output, the structured components are resolved to elementary components of an output table, `output`.

The statement `MOVE-CORRESPONDING` finds the identically named components `col2` and `col3` in `itab1` and `itab2` and the assignments work as follows:

- `MOVE-CORRESPONDING`

  The original content of `itab2` is deleted. After the assignment, the columns `col2` and `col3` have the same content as in `itab1`, whereas `col4` remains initial.

- `MOVE-CORRESPONDING KEEPING TARGET LINES`

  The original content of `itab2` is preserved. Three new lines are added in which the columns `col2` and `col3` have the same content as in `itab1`, whereas `col4` remains initial.

- `MOVE-CORRESPONDING EXPANDING NESTED TABLES`

  The original content of `itab2` is deleted. After the assignment, the column `col2` has the same content as in `itab1` and `col4` remains initial. The tabular component `col3` is resolved and the identically named component `col2` is found there. The original content of `itab2-col3` is deleted. After the assignment, the column `col2` has the same content as in `itab1-col3`, whereas the column `col3` remains initial.

- `MOVE-CORRESPONDING EXPANDING NESTED TABLES KEEPING TARGET LINES`

  The original content of `itab2` is preserved. Three new lines are added, to which the same applies as to the results of the previous assignment.
