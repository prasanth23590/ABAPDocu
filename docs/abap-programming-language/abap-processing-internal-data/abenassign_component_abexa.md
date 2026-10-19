---
title: "Field Symbols, Dynamic Structure Components"
source_file: abenassign_component_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assigning References > Assigning Field Symbols > ASSIGN > ASSIGN, mem_area > ASSIGN, dynamic_components"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Field Symbols, Dynamic Structure Components

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates dynamic assignments of structure components using `ASSIGN`.

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
CLASS cl_demo_assign_component_v5 DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_assign_component_v5 IMPLEMENTATION. 
  METHOD main. 
    DATA: 
      BEGIN OF struc, 
        comp1 TYPE i, 
        comp2 TYPE i, 
        comp3 TYPE i, 
      END OF struc, 
      name TYPE string, 
      t1   TYPE utclong, 
      t2   TYPE utclong, 
      tr   TYPE decfloat34. 
    FIELD-SYMBOLS: <struc> TYPE any, 
                   <comp>  TYPE any. 
 
    ASSIGN struc TO <struc>. 
 
    name = `COMP1`. 
    t1 = utclong_current( ). 
    DO 1000 TIMES. 
      ASSIGN <struc>-(name) TO <comp>. 
    ENDDO. 
    t2 = utclong_current( ). 
    cl_abap_utclong=>diff( EXPORTING high    = t2 
                                     low   = t1 
                           IMPORTING seconds = tr ). 
    out->write( |ASSIGN <struc>-(name): { tr }| ). 
 
    t1 = utclong_current( ). 
    DO 1000 TIMES. 
      ASSIGN <struc>-(1) TO <comp>. 
    ENDDO. 
    t2 = utclong_current( ). 
    cl_abap_utclong=>diff( EXPORTING high    = t2 
                                     low   = t1 
                           IMPORTING seconds = tr ). 
    out->write( |ASSIGN <struc>-(1): { tr }| ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A structure is assigned to a generically typed field symbol. Using the field symbol the individual components of the structure can be addressed dynamically only. This example shows different ways of doing so and measures their runtime. Using the position is better for performance than using the name.
