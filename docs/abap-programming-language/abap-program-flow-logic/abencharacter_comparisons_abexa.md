---
title: "rel_exp - Comparison Operators for Character-Like Data Types"
source_file: abencharacter_comparisons_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Operators > rel_exp - Comparison Operators for Character-Like Data Types"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison Operators for Character-Like Data Types

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the [comparison operators for character-like data types](abenlogexp_strings.md).

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
CLASS cl_demo_character_comparison DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_character_comparison IMPLEMENTATION. 
  METHOD main. 
    TYPES: 
      BEGIN OF result, 
        operand TYPE string, 
        result  TYPE string, 
        fdpos   TYPE sy-fdpos, 
      END OF result. 
    DATA results TYPE STANDARD TABLE OF result WITH EMPTY KEY. 
 
    DATA: f1 TYPE c LENGTH 5 VALUE 'BD   ', 
          f2 TYPE c LENGTH 5 VALUE 'ABCDE'. 
    cl_demo_input=>new( 
      )->add_field( CHANGING field = f1 
      )->add_field( CHANGING field = f2 )->request( ). 
 
    results = VALUE #( BASE results 
     ( operand = 'CO' 
       result     = COND #( WHEN f1 CO f2 THEN abap_true ) 
       fdpos      = sy-fdpos ) ). 
    results = VALUE #( BASE results 
     ( operand = 'CN' 
       result     = COND #( WHEN f1 CN f2 THEN abap_true ) 
       fdpos      = sy-fdpos ) ). 
    results = VALUE #( BASE results 
     ( operand = 'CA' 
       result     = COND #( WHEN f1 CA f2 THEN abap_true ) 
       fdpos      = sy-fdpos ) ). 
    results = VALUE #( BASE results 
     ( operand = 'NA' 
       result     = COND #( WHEN f1 NA f2 THEN abap_true ) 
       fdpos      = sy-fdpos ) ). 
    results = VALUE #( BASE results 
     ( operand = 'CS' 
       result     = COND #( WHEN f1 CS f2 THEN abap_true ) 
       fdpos      = sy-fdpos ) ). 
    results = VALUE #( BASE results 
     ( operand = 'NS' 
       result     = COND #( WHEN f1 NS f2 THEN abap_true ) 
       fdpos      = sy-fdpos ) ). 
    results = VALUE #( BASE results 
     ( operand = 'CP' 
       result     = COND #( WHEN f1 CP f2 THEN abap_true ) 
       fdpos      = sy-fdpos ) ). 
    results = VALUE #( BASE results 
     ( operand = 'NP' 
       result     = COND #( WHEN f1 NP f2 THEN abap_true ) 
       fdpos      = sy-fdpos ) ). 
 
    out->write( |'{ f1 WIDTH = 5 }' operand '{ f2 WIDTH = 5 }'| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Text fields with length 5 can be supplied with different content and compared with each other using the available comparison operators.
