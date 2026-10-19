---
title: "MOVE-CORRESPONDING for Structures"
source_file: abenmove_corresponding_struc_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# MOVE-CORRESPONDING for Structures

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the statement [`MOVE-CORRESPONDING`](abapmove-corresponding.md) for structures.

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
CLASS cl_demo_move_crrspndng_struct DEFINITION 
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
      struct1 TYPE        line1, 
      struct2 TYPE        line2. 
    METHODS: 
      fill_structures. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_move_crrspndng_struct IMPLEMENTATION. 
  METHOD main. 
    fill_structures( ). 
 
    out->begin_section( `struct1` 
      )->write( struct1 
      )->next_section( `struct2` 
      )->write( struct2 ). 
 
    out->begin_section( 
      `MOVE-CORRESPONDING` ). 
 
    MOVE-CORRESPONDING struct1 TO struct2. 
 
    out->write( struct2 
      )->next_section( 
      `MOVE-CORRESPONDING EXPANDING NESTED TABLES` ). 
 
    MOVE-CORRESPONDING struct1 TO struct2 EXPANDING NESTED TABLES. 
 
    out->write( struct2 ). 
  ENDMETHOD. 
  METHOD fill_structures. 
    struct1 = VALUE #( 
       col1 = 'a1' 
       col2 = 'a2' 
       col3 = VALUE #( ( col1 = 'a11'  col2 = 'a12' ) 
                       ( col1 = 'a21'  col2 = 'a22' ) ) ). 
 
    struct2 = VALUE #( 
       col2 = 'x11' 
       col3 = VALUE #( ( col2 = 'x11'  col3 = 'x12' ) 
                       ( col2 = 'x21'  col3 = 'x22' ) 
                       ( col2 = 'x31'  col3 = 'x32' ) ) 
       col4 = 'x12'  ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Two structures, `struct1` and `struct2` are declared using the available additions and [`MOVE-CORRESPONDING`](abapmove-corresponding.md) assigns `struct1` to `struct2`.

- `struct1` contains two elementary components, `col1` and `col2`, and a tabular component `col3` with the components `col1` and `col2`.

- `struct2` contains two elementary components, `col2` and `col4`, and a tabular component `col3` with the components `col2` and `col3`.

The structures are filled with values. For the output, the structured components are resolved to elementary components of an output table, `output`.

The statement `MOVE-CORRESPONDING` finds the identically named components `col2` and `col3` in `struct1` and `struct2` and the assignments work as follows:

- `MOVE-CORRESPONDING`

  After the assignment, the components `col2` and `col3` in `struct2` have the same content as in `struct1`. Component `col4` keeps its value.

- `MOVE-CORRESPONDING EXPANDING NESTED TABLES`

  After the assignment, the component `col2` in `struct2` has the same content as in `struc1`. `col4` preserves its value. The tabular component `col3` is resolved and the identically named component `col2` is found there. The original content of `struct2-col3` is deleted. After the assignment, the column `col2` has the same content as in `struct1-col3`, whereas the column `col3` remains initial.
