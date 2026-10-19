---
title: "Component Operator for Structures"
source_file: abencorresponding_struct_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Component Operator for Structures

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the [component operator](abenconstructor_expr_corresponding.md) for structures.

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
CLASS cl_demo_crrspndng_struct DEFINITION 
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
CLASS cl_demo_crrspndng_struct IMPLEMENTATION. 
  METHOD main. 
    fill_structures( ). 
    out->begin_section( `struct1` 
      )->write( struct1 ). 
    out->next_section( `struct2` 
      )->write( struct2 ). 
 
    FINAL(base) = struct2. 
 
    out->begin_section( 
      `CORRESPONDING struct2( struct1 )` ). 
 
    struct2 = CORRESPONDING #( struct1 ). 
 
    out->write( struct2 
     )->next_section( 
      `CORRESPONDING struct2( BASE ( struct2 ) struct1 )` ). 
 
    struct2 = CORRESPONDING #( BASE ( base ) struct1 ). 
 
    out->write( struct2 
     )->next_section( 
      `CORRESPONDING struct2( DEEP struct1 )` ). 
 
    struct2 = CORRESPONDING #( DEEP struct1 ). 
 
    out->write( struct2 
     )->next_section( 
      `CORRESPONDING struct2( DEEP BASE ( struct2 ) struct1 )` ). 
 
    struct2 = CORRESPONDING #( DEEP BASE ( base ) struct1 ). 
 
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

This example uses the same structures as the [executable example](abenmove_corresponding_struc_abexa.md) for `MOVE-CORRESPONDING`. Here, the source structure `struct1` is used as a parameter of a constructor expression with the component operator `CORRESPONDING` and the result is assigned to the target structure `struct2`. The source structure `struct1` is assigned to the result with the type of `struct2` with and without the addition `DEEP`. If the addition `BASE` is used, the result is given the original value of `struct2` as its start value and otherwise stays initial. The assignment is made exactly as described in the [executable example](abenmove_corresponding_struc_abexa.md) for `MOVE-CORRESPONDING` with or without `EXPANDING NESTED TABLES`. If `DEEP` is used, the name comparison is made for the components of the substructure `col3`, which means that fewer assignments are made than when omitting `DEEP`. The uninvolved component `col4` keeps its initial value without using the addition `BASE`. If `BASE` is used, it keeps the set value. The result is assigned to the target structure `struct2`.

The result of the component operator matches the result of `MOVE-CORRESPONDING` only if the addition `BASE` is used.
