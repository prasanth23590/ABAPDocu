---
title: "VALUE, Addition BASE for Internal Tables"
source_file: abenvalue_itab_base_abexa.html
section: "ABAP Programming Language > ABAP - Creating Objects and Values > VALUE, Value Operator > VALUE, Internal Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# VALUE, Addition BASE for Internal Tables

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the value operator [`VALUE`](abenvalue_constructor_params_itab.md) for internal tables with and without the addition `BASE`

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
CLASS cl_demo_value_base DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_value_base IMPLEMENTATION. 
  METHOD main. 
    TYPES itab TYPE TABLE OF i. 
 
    DATA itab_no_base TYPE itab. 
    DO 10 TIMES. 
      itab_no_base = VALUE #( ( sy-index ) ). 
    ENDDO. 
 
    DATA itab_base TYPE itab. 
    DO 10 TIMES. 
      itab_base = VALUE #( BASE itab_base ( sy-index ) ). 
    ENDDO. 
 
    out->write( itab_no_base 
      )->write( itab_base ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Without the addition `BASE`, the value operator constructs a new internal table from scratch during each call and this is assigned to `itab_no_base`. As a result, `itab_no_base` contains only one line after the `DO` loop.

With the addition `BASE`, the value operator inserts a line into an internal table that is prefilled with the content of `itab_base` during each call. As a result, `itab_base` contains 10 lines after the `DO` loop.
