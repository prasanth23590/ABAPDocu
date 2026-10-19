---
title: "CDS DDL - Using a CDS Simple Type for Typing in ABAP"
source_file: abencds_st_abexa.html
section: "ABAP Core Data Services (ABAP CDS) > ABAP CDS - Data Definitions > ABAP CDS - DDL for Data Definitions > ABAP CDS - Type Definitions > CDS DDL - DEFINE TYPE > ABAP CDS - Simple Types > CDS DDL - DEFINE TYPE simple_type"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# CDS DDL - Using a CDS Simple Type for Typing in ABAP

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how to use CDS simple types for declaring data objects in an ABAP class.

The following CDS simple types are used:

- First name

``` abap
@EndUserText.heading: 'First name' 
define type demo_bt_first_name: abap.char( 30 );
```

- Last name

``` abap
@EndUserText.heading: 'Last name' 
define type DEMO_BT_LAST_NAME: abap.char( 30 );
```

- Assets

``` abap
@EndUserText.heading: 'Assets' 
define type demo_bt_assets: abap.dec( 10,2 );
```

- Liabilities

``` abap
@EndUserText.heading: 'Liabilities' 
define type DEMO_BT_LIABILITIES: abap.dec( 10,2 );
```

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
CLASS cl_demo_simple_type_exec DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    DATA: result TYPE demo_bt_assets, 
          fname  TYPE demo_bt_first_name VALUE 'Lisa', 
          lname  TYPE demo_bt_last_name VALUE 'Mustermann', 
          activ  TYPE demo_bt_assets VALUE '27.5', 
          liabs  TYPE demo_bt_liabilities VALUE '33'. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_simple_type_exec IMPLEMENTATION. 
  METHOD main. 
 
    "Request input parameters 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = fname 
     )->add_line( 
     )->add_field( CHANGING field = lname 
     )->add_line( 
     )->add_field( CHANGING field = activ 
     )->add_line( 
     )->add_field( CHANGING field = liabs 
     )->request( ). 
 
    "Perform calculation 
    result = activ - liabs. 
 
    "Generate screen output 
    out->write( |Client:| && | | && fname && | | && lname ). 
    out->write( |Finance:| && | | && activ && | | && |-| && 
     | | && liabs && | | && |=| && | | && result ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In this example, CDS simple types are used to type variables in an ABAP class.

- First, variables are declared with reference to CDS simple types.

- Then, actual parameters are requested.

- A calculation is performed, i.e. a customer's liabilities are subtracted from their assets.

- A screen output is generated.
