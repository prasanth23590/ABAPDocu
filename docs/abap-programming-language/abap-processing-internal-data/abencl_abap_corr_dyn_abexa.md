---
title: "CL_ABAP_CORRESPONDING for Simple Structures"
source_file: abencl_abap_corr_dyn_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_CORRESPONDING for Simple Structures

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the system class [`CL_ABAP_CORRESPONDING`](abencl_abap_corresponding.md) for simple structures.

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
CLASS cl_demo_crrspndng_class_dyn DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_crrspndng_class_dyn IMPLEMENTATION. 
  METHOD main. 
    TYPES: 
      BEGIN OF names, 
        n1 TYPE c LENGTH 2, 
        n2 TYPE c LENGTH 2, 
        n3 TYPE c LENGTH 2, 
      END OF names. 
 
    DATA: 
      BEGIN OF struct1, 
        a1 TYPE string VALUE 'a1', 
        a2 TYPE string VALUE 'a2', 
        a3 TYPE string VALUE 'a3', 
      END OF struct1, 
      BEGIN OF struct2, 
        b1 TYPE string VALUE 'b1', 
        b2 TYPE string VALUE 'b2', 
        b3 TYPE string VALUE 'b3', 
      END OF struct2. 
 
    DATA(src) = VALUE names( n1 = 'a1' n2 = 'a2' n3 = 'a3' ). 
    DATA(dst) = VALUE names( n1 = 'b3' n2 = 'b2' n3 = 'b1' ). 
 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = src-n1 
      )->add_field( CHANGING field = dst-n1 
      )->add_line( 
      )->add_field( CHANGING field = src-n2 
      )->add_field( CHANGING field = dst-n2 
      )->add_line( 
      )->add_field( CHANGING field = src-n3 
      )->add_field( CHANGING field = dst-n3 
      )->request( ). 
 
    TRY. 
        FINAL(mapper) = 
          cl_abap_corresponding=>create( 
            source      = struct1 
            destination = struct2 
            mapping     = VALUE cl_abap_corresponding=>mapping_table( 
              ( level = 0 kind = 1 srcname = src-n1 dstname = dst-n1 ) 
              ( level = 0 kind = 1 srcname = src-n2 dstname = dst-n2 ) 
              ( level = 0 kind = 1 srcname = src-n3 dstname = dst-n3 ) 
            ) ). 
 
        mapper->execute( EXPORTING source      = struct1 
                         CHANGING  destination = struct2 ). 
      CATCH cx_corr_dyn_error INTO FINAL(exc). 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
 
    out->write( struct2 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The components of the structure `struct1` are assigned to the structure `struct2` using the system class [`CL_ABAP_CORRESPONDING`](abencl_abap_corresponding.md). User input can control which components are mapped to each other.
