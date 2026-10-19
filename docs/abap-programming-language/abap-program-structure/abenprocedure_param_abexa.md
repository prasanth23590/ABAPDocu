---
title: "Parameter Passing"
source_file: abenprocedure_param_abexa.html
section: "ABAP Programming Language > ABAP - Program Structure > Modularization Statements > Procedures > Parameter Interface of Procedures"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Parameter Passing

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the difference between passing a parameter to a procedure by value or by reference.

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
CLASS cl_demo_procedure_param DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    TYPES: BEGIN OF line, 
             x     TYPE i, 
             y     TYPE i, 
             range TYPE i, 
           END OF line. 
    DATA: param TYPE STANDARD TABLE OF line, 
          res   TYPE i. 
    METHODS: 
      fill_table  CHANGING  g_param LIKE param, 
      solve_table IMPORTING g_param LIKE param, 
      fibb IMPORTING VALUE(l_line) TYPE line 
           EXPORTING VALUE(r)      TYPE i. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_procedure_param IMPLEMENTATION. 
  METHOD main. 
    fill_table(  CHANGING  g_param = param ). 
    solve_table( EXPORTING g_param = param ). 
  ENDMETHOD. 
  METHOD fibb. 
    IF l_line-range = 1. 
      IF l_line-x < l_line-y. 
        r = l_line-x. 
      ELSE. 
        r = l_line-y. 
      ENDIF. 
    ELSEIF l_line-range = 2. 
      IF l_line-x < l_line-y. 
        r = l_line-y. 
      ELSE. 
        r = l_line-x. 
      ENDIF. 
    ELSE. 
      l_line-range -= 2. 
      DO l_line-range TIMES. 
        IF l_line-x < l_line-y. 
          l_line-x += l_line-y. 
          r = l_line-x. 
        ELSE. 
          l_line-y += l_line-x. 
          r = l_line-y. 
        ENDIF. 
      ENDDO. 
    ENDIF. 
  ENDMETHOD. 
  METHOD fill_table. 
    g_param = VALUE #( FOR j = 1 UNTIL j > 3 
                       ( x = j 
                         y = j ** 2 
                         range = 12 / j ) ). 
  ENDMETHOD. 
  METHOD solve_table. 
    DATA l_line LIKE LINE OF g_param. 
    LOOP AT g_param INTO l_line. 
      fibb( EXPORTING l_line = l_line IMPORTING r = res ). 
      out->write( 
      |Fibb( { l_line-x }, { l_line-y }, { l_line-range }) = { res }| ). 
    ENDLOOP. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The method `fibb` calculates the sequence term with the number `range` in a Fibonacci sequence with the start values `x` and `y`. In this case, the next sequence term is always the sum of two previous sequence terms (that is, two start values). The method inherits two parameters, a structured parameter `l_line` with which input values are passed, and a parameter `r` of type `i` used to provide the result. Since the parameter `l_line` is defined as an `IMPORTING` parameter but still has to be changed in the method, the keyword `VALUE` must be set before the parameter when the method is defined. Otherwise, a syntax error occurs. This ensures that a local copy of the parameter is used within the method. The addition `VALUE` of the output parameter `r` assigns the result to the static class attribute `res` only after the method has been processed completely. Otherwise `res` would be changed for each step of the algorithm.

The internal table `param` contains the input values for calculating three different sequence terms of the Fibonacci sequence. The method `fill_table` is used to provide `param` with values and the method `solve_table` is used to calculate and output `fibb` for each line of `param`.
