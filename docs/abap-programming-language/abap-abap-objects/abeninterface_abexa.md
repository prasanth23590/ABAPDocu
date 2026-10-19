---
title: "ABAP Objects - Interfaces"
source_file: abeninterface_abexa.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Interfaces

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the use of interfaces.

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
CLASS cl_demo_interface DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* CCIMP 
INTERFACE status. 
  METHODS write. 
ENDINTERFACE. 
CLASS counter DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES status. 
    METHODS increment. 
  PRIVATE SECTION. 
    DATA count TYPE i. 
ENDCLASS. 
 
CLASS counter IMPLEMENTATION. 
  METHOD status~write. 
    o=>out->write_text( 
    |Count in counter is { count }| ). 
  ENDMETHOD. 
  METHOD increment. 
    count += 1. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS bicycle DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES status. 
    METHODS drive. 
  PRIVATE SECTION. 
    DATA speed TYPE i. 
ENDCLASS. 
 
CLASS bicycle IMPLEMENTATION. 
  METHOD status~write. 
    o=>out->write_text( 
    |Speed of bicycle is { speed }| ). 
  ENDMETHOD. 
  METHOD drive. 
    speed += 10. 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_interface IMPLEMENTATION. 
  METHOD main. 
    o=>out = out. 
 
    DATA status_tab TYPE TABLE OF REF TO status WITH EMPTY KEY. 
 
    FINAL(count) = NEW counter( ). 
    FINAL(bike) =  NEW bicycle( ). 
 
    DO 5 TIMES. 
      count->increment( ). 
      bike->drive( ). 
    ENDDO. 
 
    status_tab = VALUE #( ( count ) 
                          ( bike ) ). 
 
    LOOP AT status_tab ASSIGNING FIELD-SYMBOL(<status>). 
      <status>->write( ). 
    ENDLOOP. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example shows a local interface `status` for displaying the attributes of an object and its implementation in two different local classes.

The interface `status` contains a method `write`. The classes `counter` and `bicycle` implement the interface in the public area. Both classes must implement the interface method in the implementation part according to the required semantics.

First, two class reference variables `count` and `bike` are declared for the classes `counter` and `bicycle`. An interface reference variable `status` and an internal table `status_tab` with a suitable line type for the interface reference variable are created for the interface `status`. All reference variables begin with initial values.

Using the constructor operator `NEW`, an object is created for each class to which the references in `count` and `bike` point. Using the class reference variable, the methods `increment` and `drive` are called in the respective objects.

Class reference variables are inserted in the interface reference table to have the lines in `status_tab` point to the two objects as well. Using the interface references, it is possible to call the interface method `write` in the objects, but not the class methods `increment` or `drive`.
