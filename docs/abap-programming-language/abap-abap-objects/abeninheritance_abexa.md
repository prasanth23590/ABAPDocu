---
title: "ABAP Objects - Inheritance"
source_file: abeninheritance_abexa.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Inheritance

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how a counter is specialized using inheritance.

## Source Code

``` abap
* CCDEF 
CLASS o DEFINITION. 
  PUBLIC SECTION. 
    CLASS-DATA out TYPE REF TO if_demo_output. 
ENDCLASS. 
 
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_inheritance DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* CCIMP 
CLASS counter DEFINITION. 
  PUBLIC SECTION. 
    METHODS: 
    set 
    IMPORTING VALUE(set_value) TYPE i, 
    increment, 
    get 
    EXPORTING VALUE(get_value) TYPE i. 
  PROTECTED SECTION. 
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
 
CLASS counter_ten DEFINITION INHERITING FROM counter. 
  PUBLIC SECTION. 
    METHODS increment REDEFINITION. 
    DATA count_ten TYPE c LENGTH 1. 
ENDCLASS. 
 
CLASS counter_ten IMPLEMENTATION. 
  METHOD increment. 
    DATA modulo TYPE i. 
    super->increment( ). 
    modulo = count MOD 10. 
    IF modulo = 0. 
      count_ten += 1. 
      o=>out->write_text( 
      |{ count } - { count_ten }| ). 
    ELSE. 
      o=>out->write_text( |{ count }| ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_inheritance IMPLEMENTATION. 
  METHOD main. 
    o=>out = out. 
 
    DATA: count  TYPE REF TO counter, 
          number TYPE i VALUE 5. 
 
    count = NEW counter_ten( ). 
 
    count->set( number ). 
 
    DO 20 TIMES. 
      count->increment( ). 
    ENDDO. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The local class `counter_ten` is derived from `counter` and redefines the method `increment`. In `counter`, the visibility of the attribute `count` must be set from `PRIVATE` to `PROTECTED`. In the redefined method, the hidden method with the pseudo reference `super->` is called. The redefined method specializes the inherited method.

An object of the subclass is created to which a reference variable of the superclass type points. When the method `increment` is executed using the superclass reference, the redefined method of the subclass is executed.
