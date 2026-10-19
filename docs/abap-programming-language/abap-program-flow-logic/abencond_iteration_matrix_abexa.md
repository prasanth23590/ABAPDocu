---
title: "Creating a Matrix Using FOR and VALUE"
source_file: abencond_iteration_matrix_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Iteration Expressions > FOR, Iteration Expressions > Examples of Iteration Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Creating a Matrix Using FOR and VALUE

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a matrix is created using iterations.

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
CLASS cl_demo_matrix DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    TYPES: t_column TYPE STANDARD TABLE OF string   WITH EMPTY KEY, 
           t_rows   TYPE STANDARD TABLE OF t_column WITH EMPTY KEY. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    DATA: 
      rows    TYPE i, 
      columns TYPE i, 
      x       TYPE i VALUE 1, 
      y       TYPE i VALUE 1, 
      abcde   TYPE string VALUE 'abcdefghijklmnopqrstuvwxyz'. 
    METHODS initialize. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_matrix IMPLEMENTATION. 
  METHOD main. 
    initialize( ). 
    "Old way 
    DATA: column     TYPE t_column, 
          matrix_old TYPE t_rows. 
    DO columns TIMES. 
      FINAL(idx) = sy-index - 1. 
      CLEAR column. 
      DO rows TIMES. 
        APPEND abcde+idx(1) && |{ sy-index }| TO column. 
      ENDDO. 
      APPEND column TO matrix_old. 
    ENDDO. 
 
    "New way 
    FINAL(matrix_new) = 
      VALUE t_rows( 
        FOR i = 0 UNTIL i > columns - 1 ( 
          VALUE t_column( 
            FOR j = 1 UNTIL j > rows 
              ( abcde+i(1) && |{ j }| ) ) ) ). 
 
    ASSERT matrix_new = matrix_old. 
 
    TRY. 
        out->write( matrix_new[ x ][ y ] ). 
      CATCH cx_sy_itab_line_not_found. 
        out->write( 'Not found' ). 
    ENDTRY. 
  ENDMETHOD. 
  METHOD initialize. 
    rows = 100. 
    columns = strlen( abcde ). 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = x 
     )->add_field( CHANGING field = y 
     )->request( ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The lines and columns of a matrix are simulated using an internal table whose line types are arrays. These tables are filled using nested [`DO`](abapdo.md) loops and equivalent iteration expressions for [conditional iterations](abenfor_conditional.md) in a constructor expression with the operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md). The [`ASSERT`](../abap-program-maintenance/abapassert.md) statement shows that both internal tables have the same content. It is possible to access each individual element.
