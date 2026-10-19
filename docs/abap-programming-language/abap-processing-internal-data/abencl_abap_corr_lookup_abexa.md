---
title: "CL_ABAP_CORRESPONDING with Lookup Table"
source_file: abencl_abap_corr_lookup_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_CORRESPONDING with Lookup Table

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the system class [`CL_ABAP_CORRESPONDING`](abencl_abap_corresponding.md) with a lookup table

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
CLASS cl_demo_crrspndng_class_lkup DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    TYPES: 
      BEGIN OF struct1, 
        a1 TYPE string, 
        a2 TYPE string, 
        b1 TYPE string, 
        b2 TYPE string, 
        c1 TYPE string, 
        c2 TYPE string, 
      END OF struct1, 
      BEGIN OF struct2, 
        a1 TYPE string, 
        a2 TYPE string, 
        b1 TYPE string, 
        b2 TYPE string, 
        c1 TYPE string, 
        d2 TYPE string, 
      END OF struct2. 
    DATA: 
      itab       TYPE STANDARD TABLE OF struct1, 
      lookup_tab TYPE SORTED TABLE OF struct2 
                 WITH NON-UNIQUE KEY  b1 b2. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_crrspndng_class_lkup IMPLEMENTATION. 
  METHOD main. 
    out->begin_section( `itab` 
      )->write( itab ). 
 
    out->next_section( 
      `lookup_tab` 
      )->write( lookup_tab ). 
 
    DATA(mapping_tab) = VALUE cl_abap_corresponding=>mapping_table( 
      ( level = 0 kind = 4 srcname = 'PRIMARY_KEY' ) 
      ( level = 0 kind = 5 srcname = 'B1' dstname = 'A1' ) 
      ( level = 0 kind = 5 srcname = 'B2' dstname = 'A2' ) ). 
    cl_abap_corresponding=>create_using( 
      destination       = itab 
      using             = lookup_tab 
      mapping           = mapping_tab 
      )->execute_using( EXPORTING using       = lookup_tab 
                        CHANGING  destination = itab ). 
    out->next_section( 
      `CL_ABAP_CORRESPONDING=>EXECUTE_USING without mapping` 
      )->write( itab ). 
 
    mapping_tab = VALUE cl_abap_corresponding=>mapping_table( 
       ( level = 0 kind = 4 srcname = 'PRIMARY_KEY' ) 
       ( level = 0 kind = 5 srcname = 'B1' dstname = 'A1' ) 
       ( level = 0 kind = 5 srcname = 'B2' dstname = 'A2' ) 
       ( level = 0 kind = 1 srcname = 'A1' dstname = 'A1' ) 
       ( level = 0 kind = 1 srcname = 'A2' dstname = 'A2' ) 
       ( level = 0 kind = 1 srcname = 'B1' dstname = 'B1' ) 
       ( level = 0 kind = 1 srcname = 'B2' dstname = 'B2' ) 
       ( level = 0 kind = 1 srcname = 'D2' dstname = 'C2' )  ). 
    cl_abap_corresponding=>create_using( 
      destination       = itab 
      using             = lookup_tab 
      mapping           = mapping_tab 
      )->execute_using( EXPORTING using       = lookup_tab 
                        CHANGING  destination = itab ). 
    out->next_section( 
    `CL_ABAP_CORRESPONDING=>EXECUTE_USING with mapping` 
      )->write( itab ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    itab = VALUE #( 
      ( a1 = `id1_1` a2 = `id2_1` 
        b1 = `000`   b2 = `000` 
        c1 = `000`   c2 = `000` ) 
      ( a1 = `id1_2` a2 = `id2_2` 
        b1 = `000`   b2 = `000` 
        c1 = `000`   c2 = `000` ) 
      ( a1 = `id1_3` a2 = `id2_3` 
        b1 = `000`   b2 = `000` 
        c1 = `000`   c2 = `000` ) ). 
    lookup_tab = VALUE #( 
      ( a1 = `a_11`  a2 = `a_12` 
        b1 = `id1_1` b2 = `id2_1` 
        c1 = `c_11`  d2 = `d_12` ) 
      ( a1 = `a_21`  a2 = `a_22` 
        b1 = `id1_3` b2 = `id2_3` 
        c1 = `c_21`  d2 = `d_22` ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example shows how the first two uses of the component operator `CORRESPONDING` in the executable example [Component Operator, Lookup Table](abencorresponding_using_abexa.md) can be transformed to method calls for the class `CL_ABAP_CORRESPONDING`. The results are the same in both cases. There is no equivalent for the third option of using the component operator, since the method `EXECUTE_USING` uses a `CHANGING` parameter and the source table therefore always matches the target table.
