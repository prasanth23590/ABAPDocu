---
title: "bchain_func - Setting Bits"
source_file: abenbit_func_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Byte Chain Processing > Byte Chains Functions (bchain_func) > bchain_func - bit-set"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# bchain_func - Setting Bits

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how `bit-set` works.

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
CLASS cl_demo_bit_set DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_bit_set IMPLEMENTATION. 
  METHOD main. 
    DATA(number) = 1. 
    cl_demo_input=>new( )->request( CHANGING field = number ). 
    IF abs( number ) <= 200. 
      out->write( CONV xstring( bit-set( number ) ) ). 
    ELSE. 
      out->write( 
       'Number in Example must not exceed 200' ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The output of the class shows how bits are set in a specified place in hexadecimal form.
