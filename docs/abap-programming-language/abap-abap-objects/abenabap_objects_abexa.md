---
title: "ABAP Objects - Overview"
source_file: abenabap_objects_abexa.html
section: "ABAP Programming Language > ABAP - ABAP Objects > ABAP Objects - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# ABAP Objects - Overview

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The example demonstrates objects, object references, inheritance, interfaces, and events.

## Source Code

``` abap
* CCDEF 
CLASS o DEFINITION. 
  PUBLIC SECTION. 
    CLASS-DATA out TYPE REF TO if_demo_output. 
ENDCLASS. 
 
*---------------------------------------------------------------------* 
* INTERFACE status 
*---------------------------------------------------------------------* 
* Interface definition * 
*---------------------------------------------------------------------* 
INTERFACE status. 
  METHODS write. 
ENDINTERFACE. 
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_abap_objects DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS: 
      objects, 
      inheritance, 
      interfaces, 
      events. 
ENDCLASS. 
 
* CCIMP 
*---------------------------------------------------------------------* 
* CLASS vessel DEFINITION 
*---------------------------------------------------------------------* 
* Superclass definition * 
*---------------------------------------------------------------------* 
CLASS vessel DEFINITION. 
  PUBLIC SECTION. 
    METHODS: 
    constructor, 
    drive 
    IMPORTING speed_up TYPE i, 
    get_id 
    RETURNING VALUE(id) TYPE i. 
  PROTECTED SECTION. 
    DATA: speed TYPE i, 
    max_speed TYPE i VALUE 100. 
  PRIVATE SECTION. 
    CLASS-DATA object_count TYPE i. 
    DATA id TYPE i. 
ENDCLASS. 
 
*---------------------------------------------------------------------* 
* CLASS vessel IMPLEMENTATION 
*---------------------------------------------------------------------* 
* Superclass implementation * 
*---------------------------------------------------------------------* 
CLASS vessel IMPLEMENTATION. 
  METHOD constructor. 
    object_count += 1. 
    id = object_count. 
  ENDMETHOD. 
  METHOD drive. 
    speed += speed_up. 
    IF speed > max_speed. 
      speed = max_speed. 
    ENDIF. 
  ENDMETHOD. 
  METHOD get_id. 
    id = me->id. 
  ENDMETHOD. 
ENDCLASS. 
 
*---------------------------------------------------------------------* 
* CLASS ship DEFINITION 
*---------------------------------------------------------------------* 
* Subclass definition * 
*---------------------------------------------------------------------* 
CLASS ship DEFINITION INHERITING FROM vessel. 
  PUBLIC SECTION. 
    INTERFACES status. 
    DATA name TYPE string READ-ONLY. 
    METHODS: 
    constructor 
    IMPORTING name TYPE string, 
    drive 
    REDEFINITION. 
    EVENTS emergency_call. 
ENDCLASS. 
 
*---------------------------------------------------------------------* 
* CLASS ship IMPLEMENTATION 
*---------------------------------------------------------------------* 
* Subclass implementation * 
*---------------------------------------------------------------------* 
CLASS ship IMPLEMENTATION. 
  METHOD constructor. 
    super->constructor( ). 
    max_speed = 30. 
    me->name = name. 
  ENDMETHOD. 
  METHOD status~write. 
    DATA id TYPE c LENGTH 1. 
    id = me->get_id( ). 
    o=>out->write( |{ name } is vessel { id 
    } and has speed { speed }| ). 
  ENDMETHOD. 
  METHOD drive. 
    speed += speed_up. 
    IF speed > max_speed. 
      max_speed = 0. 
      speed = 0. 
      RAISE EVENT emergency_call. 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS. 
 
*---------------------------------------------------------------------* 
* CLASS coast_guard DEFINITION 
*---------------------------------------------------------------------* 
* Event handler definition * 
*---------------------------------------------------------------------* 
CLASS coast_guard DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES status. 
    METHODS receive 
    FOR EVENT emergency_call OF ship 
    IMPORTING sender. 
    ALIASES write FOR status~write. 
  PRIVATE SECTION. 
    DATA caller TYPE string. 
ENDCLASS. 
 
*---------------------------------------------------------------------* 
* CLASS coast_guard IMPLEMENTATION 
*---------------------------------------------------------------------* 
* Event handler implementation * 
*---------------------------------------------------------------------* 
CLASS coast_guard IMPLEMENTATION. 
  METHOD status~write. 
    IF caller IS INITIAL. 
      o=>out->write( 
      `Coast guard received no call` ). 
    ELSE. 
      o=>out->write( 
      |Coast guard received a call from { caller }| ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD receive. 
    caller = sender->name. 
    write( ). 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_abap_objects IMPLEMENTATION. 
  METHOD main. 
    o=>out = out. 
 
    DATA: button1 TYPE abap_bool VALUE abap_true, 
          button2 TYPE abap_boolean, 
          button3 TYPE abap_boolean, 
          button4 TYPE abap_boolean. 
    cl_demo_input=>new( 
      )->add_field( EXPORTING text = `Objects and Object References` 
                              as_checkbox = abap_true 
                    CHANGING  field = button1 
      )->add_field( EXPORTING text = `Inheritance` 
                              as_checkbox = abap_true 
                    CHANGING  field = button2 
      )->add_field( EXPORTING text = `Interfaces` 
                              as_checkbox = abap_true 
                    CHANGING  field = button3 
      )->add_field( EXPORTING text = `Events` 
                              as_checkbox = abap_true 
                    CHANGING  field = button4 
      )->request( ). 
 
    IF strlen( button1 && button2 && button3 && button4 ) > 1. 
      EXIT. 
    ELSEIF button1 = abap_true. 
      objects( ). 
    ELSEIF button2 = abap_true. 
      inheritance( ). 
    ELSEIF button3 = abap_true. 
      interfaces( ). 
    ELSEIF button4 = abap_true. 
      events( ). 
    ENDIF. 
  ENDMETHOD. 
  METHOD events. 
    FINAL(ship)    = NEW ship( 'Titanic' ). 
    FINAL(station) = NEW coast_guard( ). 
    SET HANDLER station->receive FOR ship. 
    DO 5 TIMES. 
      ship->drive( 10 ). 
    ENDDO. 
  ENDMETHOD. 
  METHOD inheritance. 
    FINAL(ship) = NEW ship( 'Titanic' ). 
    ship->drive( 20 ). 
    FINAL(vessel) = CAST vessel( ship ). 
    vessel->drive( 10 ). 
    ship->status~write( ). 
  ENDMETHOD. 
  METHOD interfaces. 
    DATA status_tab TYPE TABLE OF REF TO status WITH EMPTY KEY. 
    status_tab = VALUE #( ( NEW ship( name = 'Titanic' ) ) 
                          ( NEW coast_guard( ) ) ). 
    LOOP AT status_tab ASSIGNING FIELD-SYMBOL(<status>). 
      <status>->write( ). 
    ENDLOOP. 
  ENDMETHOD. 
  METHOD objects. 
    FINAL(vessel1) = NEW vessel( ). 
    FINAL(vessel2) = NEW vessel( ). 
    vessel1->drive( 50 ). 
    vessel2->drive( 80 ). 
    o=>out->write( |Vessel ID is { vessel1->get_id( ) }| ). 
    o=>out->write( |Vessel ID is { vessel2->get_id( ) }| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The class demonstrates how ABAP Objects can be used based on example classes for boats.
