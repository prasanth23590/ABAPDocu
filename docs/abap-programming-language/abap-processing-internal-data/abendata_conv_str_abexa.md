---
title: "Conversion Rules for Structures"
source_file: abendata_conv_str_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Assignments > Assignment and Conversion Rules > Conversion Rules for Structures > Conversion Between Flat Structures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Conversion Rules for Structures

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how structures can be converted from one type to another.

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
CLASS cl_demo_data_conversion_struct DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_data_conversion_struct IMPLEMENTATION. 
  METHOD main. 
 
    DATA: BEGIN OF fs1, 
            int   TYPE i            VALUE 5, 
            pack  TYPE p DECIMALS 2 VALUE '2.26', 
            text  TYPE c LENGTH 10  VALUE 'Fine Text', 
            float TYPE decfloat16   VALUE '1.234e+05', 
            date  TYPE d            VALUE '19950916', 
          END OF fs1. 
 
    DATA: BEGIN OF fs2, 
            int  TYPE i            VALUE 3, 
            pack TYPE p DECIMALS 2 VALUE '72.34', 
            text TYPE c LENGTH 5   VALUE 'Hello', 
          END OF fs2. 
 
    out->begin_section( 'Source' 
      )->write( |{ fs1-int   WIDTH = 10 } { 
                   fs1-pack  WIDTH = 10 } { 
                   fs1-text  WIDTH = 10 } { 
                   fs1-float WIDTH = 10 } { 
                   fs1-date  WIDTH = 10 }| ). 
 
    out->next_section( 'Target' 
      )->write( |{ fs2-int  WIDTH = 10 } { 
                   fs2-pack WIDTH = 10 } { 
                   fs2-text WIDTH = 10 }| ). 
 
    fs2 = fs1. 
 
    out->next_section( 'Result' 
      )->write( |{ fs2-int  WIDTH = 10 } { 
                     fs2-pack WIDTH = 10 } { 
                     fs2-text WIDTH = 10 }| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

In this example, two different structures are defined, `fs1` and `fs2`. The prerequisites of the third [conversion rule for flat structures](abenconversion_flat_flat.md) apply to both structures and the corresponding rule is also applied. After the assignment of `fs1` to `fs2`, only the result for the first two components is the same as if they were passed component by component. `fs2-text` is filled with the first five places from `fs1-text`. None of the remaining components of `fs1` are passed.
