---
title: "table_exp - Accessing Components Dynamically"
source_file: abentable_exp_dynamic_comp_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > itab - Table Expressions (table_exp) > table_exp - Chainings"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# table_exp - Accessing Components Dynamically

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how components or internal tables can be accessed dynamically.

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
CLASS cl_demo_itab_get_component DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC . 
  PUBLIC SECTION. 
    METHODS main 
      REDEFINITION . 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_itab_get_component IMPLEMENTATION. 
  METHOD main. 
 
    SELECT * 
           FROM scarr 
           INTO TABLE @FINAL(scarr_tab). 
 
    DATA(line) = 1. 
    DATA(column) = 1. 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = line 
     )->add_field( CHANGING field = column 
     )->request( ). 
 
    out->write( scarr_tab 
      )->write( |Line { line }, Column { column }: { 
          cl_demo_itab_struct_comp=>get( itab  = scarr_tab 
                                         line  = line 
                                         comp = column ) }| ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Method `GET` of class `CL_DEMO_ITAB_STRUCT_COMP` returns the textual content of any component of any structured line of an internal table:

``` abap
METHOD get. 
  TRY. 
      comp_string = CONV string( itab[ line ]-(comp) ). 
    CATCH cx_sy_itab_line_not_found 
          cx_sy_assign_illegal_component INTO FINAL(exc). 
      comp_string = `Error: ` && exc->get_text( ). 
  ENDTRY. 
ENDMETHOD.
```

The above example calls that method for an internal table `scarr_tab`. The line and column can be freely specified.
