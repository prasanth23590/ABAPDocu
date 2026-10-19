---
title: "CL_ABAP_CORRESPONDING for Internal Tables"
source_file: abencl_abap_corr_itab_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_CORRESPONDING for Internal Tables

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the system class [`CL_ABAP_CORRESPONDING`](abencl_abap_corresponding.md) for internal tables.

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
CLASS cl_demo_crrspndng_class_tb DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_crrspndng_class_tb IMPLEMENTATION. 
  METHOD main. 
    TYPES: BEGIN OF line1, 
             col1 TYPE i, 
             col2 TYPE i, 
           END OF line1, 
           BEGIN OF line2, 
             col2 TYPE i, 
             col3 TYPE i, 
           END OF line2. 
 
    DATA: itab1 TYPE TABLE OF line1 WITH EMPTY KEY, 
          itab2 TYPE TABLE OF line2 WITH EMPTY KEY. 
 
    itab1 = VALUE #( 
      ( col1 = 11 col2 = 12 ) 
      ( col1 = 21 col2 = 22 ) ). 
 
    itab2 = VALUE #( 
      ( col2 = 212 col3 = 312 ) 
      ( col2 = 222 col3 = 322 ) ). 
 
    cl_abap_corresponding=>create( 
       source            = itab1 
       destination       = itab2 
       mapping  = VALUE cl_abap_corresponding=>mapping_table(  ) 
       )->execute( EXPORTING source      = itab1 
                   CHANGING  destination = itab2 ). 
    out->write( itab2 ). 
 
    cl_abap_corresponding=>create( 
      source            = itab1 
      destination       = itab2 
      mapping           = VALUE cl_abap_corresponding=>mapping_table( 
       ( level = 0 kind = 1 srcname = 'col1' dstname = 'col2' ) 
       ( level = 0 kind = 1 srcname = 'col2' dstname = 'col3' ) ) 
      )->execute( EXPORTING source      = itab1 
                  CHANGING  destination = itab2 ). 
    out->write( itab2 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The components of the internal table `itab1` are assigned to the internal table `itab2` using the system class [`CL_ABAP_CORRESPONDING`](abencl_abap_corresponding.md).

- The mapping table is empty in the first assignment. The assignment is made as in [`MOVE-CORRESPONDING`](abapmove-corresponding.md) using identical names and the column `col3` of the target table is not filled.

- In the second assignment, a mapping table is passed that assigns all columns of the source table to a column in the target table regardless of their names.
