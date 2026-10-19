---
title: "itab - Table Reduction, Summation of an Array"
source_file: abenreduce_simple_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Table Reductions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Table Reduction, Summation of an Array

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a simple [table reduction](../../abap-glossary/abentable_reduction_glosry.md) using [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md).

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
CLASS cl_demo_reduce_simple DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_reduce_simple IMPLEMENTATION. 
  METHOD main. 
    DATA itab TYPE TABLE OF i WITH EMPTY KEY. 
    itab = VALUE #( FOR j = 1 WHILE j <= 10 ( j ) ). 
    out->write( itab ). 
 
    FINAL(sum) = REDUCE i( INIT x = 0 FOR wa IN itab NEXT x += wa ). 
    out->write( sum ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

After the [`FOR` expression](abenfor_in_itab.md), the content of the table lines in `itab` is added to the local variable `x` and this variable is provided as the result. Instead of `x = 0`, `x TYPE i` could also be specified after `INIT`.
