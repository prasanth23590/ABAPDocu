---
title: "Creating Data Objects with Implicit Type"
source_file: abencreate_data_implicit_abexa.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE DATA > CREATE DATA dref"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Creating Data Objects with Implicit Type

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how data objects are created with an implicit type.

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
CLASS cl_demo_create_data_implicit DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_create_data_implicit IMPLEMENTATION. 
  METHOD main. 
    TYPES t_itab TYPE TABLE OF i WITH NON-UNIQUE KEY table_line. 
 
    DATA: tab_ref TYPE REF TO t_itab, 
          i_ref   TYPE REF TO i. 
 
    IF tab_ref IS INITIAL. 
      CREATE DATA tab_ref. 
    ENDIF. 
 
    tab_ref->* = VALUE #( FOR j = 1 UNTIL j > 10 ( j ) ). 
 
    IF tab_ref IS NOT INITIAL. 
      IF i_ref IS INITIAL. 
        CREATE DATA i_ref. 
      ENDIF. 
      LOOP AT tab_ref->* INTO i_ref->*. 
        out->write( |{ i_ref->* }| ). 
      ENDLOOP. 
    ENDIF. 
 
    CLEAR: tab_ref, i_ref. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Creation of an internal table and a data object of type `i`. The data types of the created objects are the static types of the reference variables `tab_ref` and `i_ref`. The data objects are created directly before they are used and are then passed to the [Garbage Collector](../../abap-glossary/abengarbage_collector_glosry.md) by the initialization of the reference variable. The data objects are accessed by dereferencing the data references.
