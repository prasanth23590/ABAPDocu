---
title: "LET Expression"
source_file: abenlet_abexa.html
section: "ABAP Programming Language > ABAP - Declarations > Local Declarations in Constructor Expressions > let_exp, LET ... IN"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# LET Expression

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a `LET` expression in a constructor expression.

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
CLASS cl_demo_let_it_be DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_let_it_be IMPLEMENTATION. 
  METHOD main. 
 
    TYPES text TYPE STANDARD TABLE OF string WITH EMPTY KEY. 
 
    out->write( 
     VALUE text( LET it = `be` IN 
                   ( |To { it } is to do|          ) 
                   ( |To { it }, or not to { it }| ) 
                   ( |To do is to { it }|          ) 
                   ( |Do { it } do { it } do|      ) ) ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A constructor expression with the value operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md) constructs lines in an internal table to which the value of the local helper variable `it` is passed.
