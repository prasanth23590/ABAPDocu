---
title: "CL_ABAP_CORRESPONDING for Nested Structures"
source_file: abencl_abap_corr_struc_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_CORRESPONDING for Nested Structures

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the system class [`CL_ABAP_CORRESPONDING`](abencl_abap_corresponding.md) for nested structures.

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
CLASS cl_demo_crrspndng_class_str DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_crrspndng_class_str IMPLEMENTATION. 
  METHOD main. 
    DATA: 
      BEGIN OF struct1, 
        a1 TYPE string VALUE 'a1', 
        a2 TYPE string VALUE 'a2', 
        a3 TYPE string VALUE 'a3', 
        a4 TYPE string VALUE 'a4', 
        a5 TYPE string VALUE 'a5', 
        BEGIN OF asub1, 
          s1_a1 TYPE string VALUE 's1_a1', 
          s1_a2 TYPE string VALUE 's1_a2', 
          s1_a3 TYPE string VALUE 's1_a3', 
          BEGIN OF asub2, 
            s2_a1 TYPE string VALUE 's2_a1', 
            s2_a2 TYPE string VALUE 's2_a2', 
            s2_a3 TYPE string VALUE 's2_a3', 
          END OF asub2, 
        END OF asub1, 
      END OF struct1, 
      BEGIN OF struct2, 
        b1 TYPE string VALUE 'b1', 
        b2 TYPE string VALUE 'b2', 
        b3 TYPE string VALUE 'b3', 
        a4 TYPE string VALUE 'b4', 
        a5 TYPE string VALUE 'b5', 
        BEGIN OF bsub1, 
          s1_b1 TYPE string VALUE 's1_b1', 
          s1_b2 TYPE string VALUE 's1_b2', 
          s1_b3 TYPE string VALUE 's1_b3', 
          BEGIN OF bsub2, 
            s2_b1 TYPE string VALUE 's2_b1', 
            s2_b2 TYPE string VALUE 's2_b2', 
            s2_b3 TYPE string VALUE 's2_b3', 
          END OF bsub2, 
        END OF bsub1, 
      END OF struct2. 
 
    FINAL(mapping_tab) = VALUE cl_abap_corresponding=>mapping_table( 
    ( level = 0 kind = 1 srcname = 'a1' dstname = 'b3' ) 
    ( level = 0 kind = 1 srcname = 'a3' dstname = 'b1' ) 
    ( level = 0 kind = 2 srcname = 'a5' ) 
    ( level = 0 kind = 1 srcname = 'asub1' dstname = 'bsub1' ) 
    ( level = 1 kind = 1 srcname = 's1_a1' dstname = 's1_b3' ) 
    ( level = 1 kind = 1 srcname = 's1_a3' dstname = 's1_b1' ) 
    ( level = 1 kind = 1 srcname = 'asub2' dstname = 'bsub2' ) 
    ( level = 2 kind = 1 srcname = 's2_a1' dstname = 's2_b3' ) 
    ( level = 2 kind = 1 srcname = 's2_a3' dstname = 's2_b1' ) ). 
 
    cl_abap_corresponding=>create( 
      source            = struct1 
      destination       = struct2 
      mapping           = mapping_tab 
      )->execute( EXPORTING source      = struct1 
                  CHANGING  destination = struct2 ). 
 
    out->write( struct1 
      )->write( mapping_tab 
      )->write( struct2 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The components of the structure `struct1` are assigned to the structure `struct2` using the system class [`CL_ABAP_CORRESPONDING`](abencl_abap_corresponding.md).

- At the top level:

  - `a1` is mapped to `b3` and `a3` is mapped to `b1`.

  - `a2` to `b2` are ignored, since their names do not match and `b2` keeps their value.

  - The component `a4` occurs in both structures and is assigned using identical names.

  - `a5` also occurs in both structures but is excluded explicitly by the mapping type.

  - The substructure `asub1` is mapped to the substructure `bsub1`.

- At the level of the first substructure:

  - `s1_a1` is mapped to `s1_b3` and `s1_a3` is mapped to `s1_b1`.

  - `s1_a2` to `s1_b2` are ignored, since their names are not identical and `s1_b2` keeps their value.

  - The substructure `asub2` is mapped to the substructure `bsub2`.

- At the level of the second substructure:

  - `s2_a1` is mapped to `s2_b3` and `s2_a3` is mapped to `s2_b1`.

  - `s2_a2` to `s2_b2` are ignored, since their names are not identical and `s2_b2` keeps their value.
