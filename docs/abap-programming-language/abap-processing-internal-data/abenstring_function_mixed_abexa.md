---
title: "cstring_func - to_mixed and from_mixed"
source_file: abenstring_function_mixed_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > Character String Functions (cstring_func) > cstring_func - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# cstring_func - to_mixed and from_mixed

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the string functions [`to_mixed`](abencase_functions.md) and [`from_mixed`](abencase_functions.md).

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
CLASS cl_demo_to_from_mixed DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_to_from_mixed IMPLEMENTATION. 
  METHOD main. 
    DATA: 
      original  TYPE c LENGTH 30 VALUE 'ABAP_DOCU_START', 
      to_sep    TYPE c LENGTH 1  VALUE '_', 
      to_case   TYPE c LENGTH 1 VALUE 'a', 
      to_min    TYPE i VALUE 1, 
      from_sep  TYPE c LENGTH 1  VALUE '.', 
      from_case TYPE c LENGTH 1  VALUE 'A', 
      from_min  TYPE i VALUE 5. 
 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = original 
     )->add_line( 
     )->add_field( CHANGING field = to_sep 
     )->add_field( CHANGING field = to_case 
     )->add_field( CHANGING field = to_min 
     )->add_line( 
     )->add_field( CHANGING field = from_sep 
     )->add_field( CHANGING field = from_case 
     )->add_field( CHANGING field = from_min 
     )->request( ). 
 
    TRY. 
        out->write( |original:   { original }| ). 
        FINAL(to_mixed) = to_mixed( val  = original 
                                   sep  = to_sep 
                                   case = to_case 
                                   min  = to_min ). 
        out->write( |to_mixed:   { to_mixed }| ). 
        FINAL(from_mixed) = from_mixed( val  = to_mixed 
                                       sep  = from_sep 
                                       case = from_case 
                                       min  = from_min ). 
        out->write( |from_mixed: { from_mixed }| ). 
      CATCH cx_sy_strg_par_val. 
        out->write( 'Invalid parameters' ). 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The class queries the parameters for the functions `to_mixed` and `from_mixed`. The result of `to_mixed` is processed by `from_mixed`.
