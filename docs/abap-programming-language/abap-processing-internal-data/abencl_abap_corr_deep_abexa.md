---
title: "CL_ABAP_CORRESPONDING for Tabular Components"
source_file: abencl_abap_corr_deep_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning Structure Components > Assigning Components, Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CL_ABAP_CORRESPONDING for Tabular Components

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the system class [`CL_ABAP_CORRESPONDING`](abencl_abap_corresponding.md) for tabular components of structures.

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
CLASS cl_demo_crrspndng_class_strtb DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_crrspndng_class_strtb IMPLEMENTATION. 
  METHOD main. 
    TYPES: BEGIN OF line1, 
             col1 TYPE i, 
             col2 TYPE i, 
           END OF line1, 
           BEGIN OF line2, 
             col2 TYPE i, 
             col3 TYPE i, 
           END OF line2. 
 
    DATA: BEGIN OF struc1, 
            itab TYPE TABLE OF line1 WITH EMPTY KEY, 
          END OF struc1. 
 
    DATA: BEGIN OF struc2, 
            itab TYPE TABLE OF line2 WITH EMPTY KEY, 
          END OF struc2. 
 
    struc1-itab = VALUE #( 
      ( col1 = 11 col2 = 12 ) 
      ( col1 = 21 col2 = 22 ) ). 
    out->write( struc1 ). 
 
 
    MOVE-CORRESPONDING struc1 TO struc2. 
    out->write( struc2 ). 
 
    CLEAR struc2-itab. 
    MOVE-CORRESPONDING struc1 TO struc2 EXPANDING NESTED TABLES. 
    out->write( struc2 ). 
 
    CLEAR struc2-itab. 
    struc2 = CORRESPONDING #( struc1 ). 
    out->write( struc2 ). 
 
    CLEAR struc2-itab. 
    struc2 = CORRESPONDING #( DEEP struc1 ). 
    out->write( struc2 ). 
 
    CLEAR struc2-itab. 
    cl_abap_corresponding=>create( 
      source            = struc1 
      destination       = struc2 
      mapping           = VALUE cl_abap_corresponding=>mapping_table(  ) 
      )->execute( EXPORTING source      = struc1 
                  CHANGING  destination = struc2 ). 
    out->write( struc2 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example compares the options for component-by-component assignments of structures with tabular components.

- The statement [`MOVE-CORRESPONDING`](abapmove-corresponding.md) can be executed with and without the addition `EXPANDING NESTED TABLES`. Depending on this, the tabular component is assigned as a whole or by component using identical names.

- The operator [`CORRESPONDING`](abencorresponding_constr_arg_type.md) can be executed with and without the addition `DEEP`. Depending on this, the tabular component is assigned as a whole or by component using identical names.

- The class [`CL_ABAP_CORRESPONDING`](abencl_abap_corresponding.md) always resolves tabular components.
