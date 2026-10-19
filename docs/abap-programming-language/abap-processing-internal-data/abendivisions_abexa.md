---
title: "arith_exp - Calculations"
source_file: abendivisions_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Arithmetic Expressions (arith_exp) > arith_exp - Arithmetic Operators"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# arith_exp - Calculations

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the function of arithmetic operators.

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
CLASS cl_demo_data_calculate DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_data_calculate IMPLEMENTATION. 
  METHOD main. 
    DATA num1 TYPE decfloat34 VALUE 2. 
    DATA num2 TYPE decfloat34 VALUE 3. 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = num1 
     )->request(   CHANGING field = num2 ). 
 
    TRY. 
        out->write( |{ num1 } +   { num2 } = { num1 +   num2 }| 
          )->write( |{ num1 } -   { num2 } = { num1 -   num2 }| 
          )->write( |{ num1 } *   { num2 } = { num1 *   num2 }| 
          )->write( |{ num1 } /   { num2 } = { num1 /   num2 }| 
          )->write( |{ num1 } DIV { num2 } = { num1 DIV num2 }| 
          )->write( |{ num1 } MOD { num2 } = { num1 MOD num2 }| 
          )->write( |{ num1 } **  { num2 } = { num1 **  num2 }| ). 
      CATCH cx_sy_arithmetic_error INTO FINAL(exc). 
        out->write( exc->get_text( ) ). 
    ENDTRY. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The possible [arithmetic operators](abenarith_operators.md) are applied to numbers that can be entered.
