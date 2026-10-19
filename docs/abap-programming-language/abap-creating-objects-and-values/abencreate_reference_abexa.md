---
title: "Creating Reference Variables"
source_file: abencreate_reference_abexa.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > CREATE DATA > CREATE DATA, REF TO"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Creating Reference Variables

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how reference variables are created.

## Source Code

``` abap
* CCDEF 
INTERFACE intf. 
  CONSTANTS attr TYPE string VALUE `Interface constant`. 
ENDINTERFACE. 
CLASS cls DEFINITION. 
  PUBLIC SECTION. 
    INTERFACES intf. 
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
CLASS cl_demo_create_reference DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_create_reference IMPLEMENTATION. 
  METHOD main. 
    DATA intf_name TYPE string. 
    DATA cls_name  TYPE string. 
    DATA dref TYPE REF TO data. 
 
    FIELD-SYMBOLS <ref>  TYPE any. 
 
    intf_name = '\CLASS=CL_DEMO_CREATE_REFERENCE\INTERFACE=INTF'. 
    CREATE DATA dref TYPE REF TO (intf_name). 
    ASSIGN dref->* TO <ref>. 
 
    cls_name = '\CLASS=CL_DEMO_CREATE_REFERENCE\CLASS=CLS'. 
    CREATE OBJECT <ref> TYPE (cls_name). 
 
    out->write_data( <ref>->('attr') ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Creates an interface reference variable dynamically. The [absolute type name](../../abap-glossary/abenabsolute_typename_glosry.md) is used for the description of the local interface.

The reference variable is assigned to a field symbol `<ref>` using dereferencing. According to the [general typing rules](../abap-declarations/abentyping_check_general.md), this field symbol an only be typed completely generically or typed with reference to the interface `intf`.

The dynamically created reference variable is used to create and address an object of a class.
