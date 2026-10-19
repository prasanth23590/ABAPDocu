---
title: "Creating Tables Using FOR and VALUE"
source_file: abencond_iteration_value_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Iteration Expressions > FOR, Iteration Expressions > Examples of Iteration Expressions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Creating Tables Using FOR and VALUE

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [conditional iterations](abenfor_conditional.md) with the operator [`VALUE`](../abap-creating-objects-and-values/abenconstructor_expression_value.md).

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
CLASS cl_demo_value_cond_iteration DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_value_cond_iteration IMPLEMENTATION. 
  METHOD main. 
    TYPES: 
      BEGIN OF line, 
        col1 TYPE i, 
        col2 TYPE i, 
        col3 TYPE i, 
      END OF line, 
      itab TYPE STANDARD TABLE OF line WITH EMPTY KEY. 
 
    out->write( 
        VALUE itab( 
          FOR j = 11 THEN j + 10 WHILE j < 40 
          ( col1 = j col2 = j + 1 col3 = j + 2  ) ) ). 
 
    out->write( 
        VALUE itab( 
          FOR j = 31 THEN j - 10 UNTIL j < 10 
          ( col1 = j col2 = j + 1 col3 = j + 2  ) ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example demonstrates the construction of internal tables using condition iterations with a constructor expression and the corresponding variant of the value operator [`VALUE`](../abap-creating-objects-and-values/abenvalue_constructor_params_itab.md). Two internal tables with different iterations are created and directly output.
