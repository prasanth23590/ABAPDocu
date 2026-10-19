---
title: "table_exp - Side Effects"
source_file: abentable_exp_side_effect_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > itab - Table Expressions (table_exp) > table_exp - Result"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# table_exp - Side Effects

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a possible side effect when field symbols are produced as the result.

## Source Code

``` abap
* CCDEF 
TYPES itab TYPE STANDARD TABLE OF i WITH EMPTY KEY. 
* Public class definition 
"! <p class="shorttext">Demo for ABAP Keyword Documentation</p> 
"! 
"! <p><strong>Disclaimer:</strong><br> 
"! This class represents a demonstration program of the ABAP Keyword 
"! Documentation, primarily intended to provide a better explanation 
"! and visualization of syntax. It is not intended for production use 
"! and may use demo artifacts that are not released as APIs for use 
"! in ABAP for Cloud Development.</p> 
CLASS cl_demo_tab_exp_side_effect DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    METHODS meth IMPORTING idx          TYPE i 
                           line1        TYPE i OPTIONAL 
                           VALUE(line2) TYPE i OPTIONAL 
                 CHANGING  ptab         TYPE itab. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_tab_exp_side_effect IMPLEMENTATION. 
  METHOD main. 
    DATA(itab) = VALUE itab( ( 1 ) ( 2 ) ( 3 ) ( 4 ) ). 
 
    meth( EXPORTING idx    = 1 
                           line1 = itab[ 1 ] ##operator 
                 CHANGING  ptab  = itab ). 
 
    meth( EXPORTING idx   = 2 
                           line1 = VALUE #( itab[ 2 ] ) 
                 CHANGING  ptab  = itab ). 
 
    meth( EXPORTING idx   = 3 
                           line2 = itab[ 3 ] 
                 CHANGING  ptab  = itab ). 
 
    meth( EXPORTING idx   = 4 
                           line2 = VALUE #( itab[ 4 ] ) 
                 CHANGING  ptab  = itab ). 
  ENDMETHOD. 
  METHOD meth. 
    ptab[ idx ] = 111. 
    IF line1 IS SUPPLIED. 
      out->write_data( line1 ). 
    ELSEIF line2 IS SUPPLIED. 
      out->write_data( line2 ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A table expression is used to pass a line of an internal table and the internal table itself to a method. The passed line of the internal table is modified in the method by specifying a table expression on the left side of an assignment.

- In the first method call, the table expression is passed by reference without the `VALUE` operator. The result is a temporary field symbol to which the read line is assigned throughout the entire method call. The change made to the line in the table also affects the formal parameter.

- In the second method call, the table expression is passed by reference with the `VALUE` operator. The result is a temporary work area that exists throughout the entire method call. The change made to the line in the table does not affect the formal parameter.

- The third and fourth method calls repeat the previous calls, but use pass by value instead of pass by reference. Pass by value does not produce any side effects, regardless of the result.

The critical point demonstrated here also produces a syntax check warning in the extended program check for performance reasons, if not hidden using the pragma `##operator`.
