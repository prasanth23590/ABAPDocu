---
title: "ABAP Objects - Classes"
source_file: abenclass_abexa.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Classes

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a class for counters.

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
CLASS cl_demo_class_counter DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* CCIMP 
CLASS counter DEFINITION. 
  PUBLIC SECTION. 
    METHODS: set 
    IMPORTING VALUE(set_value) TYPE i, 
    increment, 
    get 
    EXPORTING VALUE(get_value) TYPE i. 
  PRIVATE SECTION. 
    DATA count TYPE i. 
ENDCLASS. 
 
CLASS counter IMPLEMENTATION. 
  METHOD set. 
    count = set_value. 
  ENDMETHOD. 
  METHOD increment. 
    count += 1. 
  ENDMETHOD. 
  METHOD get. 
    get_value = count. 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_class_counter IMPLEMENTATION. 
  METHOD main. 
    DATA number TYPE i VALUE 5. 
    FINAL(cnt) = NEW counter( ). 
 
    cnt->set( number ). 
 
    DO 3 TIMES. 
      cnt->increment( ). 
    ENDDO. 
 
    cnt->get( IMPORTING get_value = number ). 
 
    out->write( number ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The local class `counter` contains three public methods, `set`, `increment`, and `get`, which work with the private integer field `count`. Two of the methods have input and output parameters and therefore define the data interface of the class. The field `count`, on the other hand, is not visible externally.
