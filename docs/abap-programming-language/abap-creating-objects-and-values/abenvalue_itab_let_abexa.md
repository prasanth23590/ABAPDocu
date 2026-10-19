---
title: "VALUE, Operator with LET for Internal Tables"
source_file: abenvalue_itab_let_abexa.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > VALUE, Value Operator > VALUE, Internal Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# VALUE, Operator with LET for Internal Tables

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the value operator [`VALUE`](abenvalue_constructor_params_itab.md) for internal tables with a [`LET` expression](../abap-declarations/abaplet.md).

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
CLASS cl_demo_value_constr_itab_let DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* CCIMP 
CLASS date DEFINITION. 
  PUBLIC SECTION. 
    CLASS-METHODS get RETURNING VALUE(d) TYPE d. 
ENDCLASS. 
 
CLASS date IMPLEMENTATION. 
  METHOD get. 
    d = cl_demo_date_time=>get_user_date( ). 
  ENDMETHOD. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_value_constr_itab_let IMPLEMENTATION. 
  METHOD main. 
    TYPES t_date_tab TYPE TABLE OF string  WITH EMPTY KEY. 
 
    out->write( 
      VALUE t_date_tab( 
        LET d = date=>get( ) IN 
        ( |{ CONV d( d - 1 ) DATE = ENVIRONMENT }| ) 
        ( |{         d       DATE = ENVIRONMENT }| ) 
        ( |{ CONV d( d + 1 ) DATE = ENVIRONMENT }| ) ) ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Construction of an internal table with an elementary line type with type `string` and filling it with three lines. The result is a table that contains the previous day, today, and the next day in the formatting for the current language environment. Today's date is produced using a method. To make sure that the method is called only once, the return value is assigned to a local helper field in a [`LET` expression](../abap-declarations/abaplet.md).
