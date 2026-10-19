---
title: "ABAP Objects - Events in Inheritance"
source_file: abenevent_inheritance_abexa.html
section: "ABAP Programming Language > ABAP - Declarations > Declaration Statements > Classes and Interfaces > ABAP Objects - Components in Classes and Interfaces > ABAP Objects - Events"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Events in Inheritance

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the behavior of [events in inheritance](../abap-abap-objects/abeninheritance_events.md).

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
CLASS cl_demo_event_inheritance DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    CLASS-DATA handle_flag TYPE c LENGTH 1. 
ENDCLASS. 
 
* CCIMP 
CLASS c1 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-EVENTS ce1. 
    CLASS-METHODS cm1. 
    EVENTS ie1. 
    METHODS im1. 
ENDCLASS. 
 
CLASS c2 DEFINITION INHERITING FROM c1. 
  PUBLIC SECTION. 
    CLASS-METHODS cm2. 
    METHODS im2. 
ENDCLASS. 
 
CLASS c3 DEFINITION INHERITING FROM c2. 
  PUBLIC SECTION. 
    CLASS-METHODS cm3. 
    METHODS im3. 
ENDCLASS. 
 
CLASS c4 DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS cm4 FOR EVENT ce1 OF c2. 
    METHODS im4 FOR EVENT ie1 OF c2. 
ENDCLASS. 
 
CLASS c1 IMPLEMENTATION. 
  METHOD cm1. 
    CLEAR cl_demo_event_inheritance=>handle_flag. 
    RAISE EVENT ce1. 
  ENDMETHOD. 
  METHOD im1. 
    CLEAR cl_demo_event_inheritance=>handle_flag. 
    RAISE EVENT ie1. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS c2 IMPLEMENTATION. 
  METHOD cm2. 
    CLEAR cl_demo_event_inheritance=>handle_flag. 
    RAISE EVENT ce1. 
  ENDMETHOD. 
  METHOD im2. 
    CLEAR cl_demo_event_inheritance=>handle_flag. 
    RAISE EVENT ie1. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS c3 IMPLEMENTATION. 
  METHOD cm3. 
    CLEAR cl_demo_event_inheritance=>handle_flag. 
    RAISE EVENT ce1. 
  ENDMETHOD. 
  METHOD im3. 
    CLEAR cl_demo_event_inheritance=>handle_flag. 
    RAISE EVENT ie1. 
  ENDMETHOD. 
ENDCLASS. 
 
CLASS c4 IMPLEMENTATION. 
  METHOD cm4. 
    cl_demo_event_inheritance=>handle_flag = 'X'. 
  ENDMETHOD. 
  METHOD im4. 
    cl_demo_event_inheritance=>handle_flag = 'X'. 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_event_inheritance IMPLEMENTATION. 
  METHOD main. 
 
    DATA oref1 TYPE REF TO c1. 
    DATA oref2 TYPE REF TO c2. 
    DATA oref3 TYPE REF TO c3. 
    DATA oref4 TYPE REF TO c4. 
 
    out->begin_section( 'Static event' ). 
    SET HANDLER c4=>cm4. 
    c1=>cm1( ). 
    out->write( |c1=>cm1( ): { handle_flag }| ). 
    c2=>cm1( ). 
    out->write( |c2=>cm1( ): { handle_flag }| ). 
    c3=>cm1( ). 
    out->write( |c3=>cm1( ): { handle_flag }| ). 
    c2=>cm2( ). 
    out->write( |c2=>cm2( ): { handle_flag }| ). 
    c3=>cm2( ). 
    out->write( |c3=>cm2( ): { handle_flag }| ). 
    c3=>cm3( ). 
    out->write( |c3=>cm3( ): { handle_flag }| ). 
 
    out->next_section( 'Instance event' ). 
    CREATE OBJECT: oref1, oref2, oref3, oref4. 
    SET HANDLER oref4->im4 FOR ALL INSTANCES. 
    oref1->im1( ). 
    out->write( |oref1->im1( ): { handle_flag }| ). 
    oref2->im1( ). 
    out->write( |oref2->im1( ): { handle_flag }| ). 
    oref3->im1( ). 
    out->write( |oref3->im1( ): { handle_flag }| ). 
    oref2->im2( ). 
    out->write( |oref2->im2( ): { handle_flag }| ). 
    oref3->im2( ). 
    out->write( |oref3->im2( ): { handle_flag }| ). 
    oref3->im3( ). 
    out->write( |oref3->im3( ): { handle_flag }| ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A static event `ce1` and an instance event `ie1` are declared in a superclass `c1`. The superclass `c1`, its subclass `c2`, and its subclass `c3` each contain a static method and an instance method for raising the events.

In the class `c4`, event handlers are declared in `c2` for the events inherited from `c1`. The method `main` of the class `event_demo` registers the events and calls all methods that can raise events, whereby different options are used to address the methods. An *X* is displayed after the method call for a handled event.

- The event handler `cm4` declared for the class `c2` can only handle events that are raised in this class or in its subclass. Events that are raised by the static method `cm1` in `c1` are not handled, regardless of the class name specified for the call (see also [Inheritance and Static Components](../abap-abap-objects/abeninheritance_statical.md)).

- The event handler `im4` declared for the class `c2` can also only handle events raised in this class or in its subclass. Unlike when calling static methods, the class of the object is always addressed when addressing an object using an object reference and raised events in the inherited method `im1` of the classes `c2` and `c3` are handled.
