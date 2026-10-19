---
title: "num_func - Integer Power Function ipow"
source_file: abenipow_function_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Numeric Functions (num_func) > num_func - Examples"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# num_func - Integer Power Function ipow

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the integer power function [`ipow`](abenpower_function.md).

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
CLASS cl_demo_ipow DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_ipow IMPLEMENTATION. 
  METHOD main. 
    DATA n TYPE i. 
    DATA arg1 TYPE p DECIMALS 1. 
    DATA arg2 TYPE int8. 
 
    n = 2. 
    arg1 = `1.2`. 
    out->write( |**  : { arg1 ** n }| 
      )->write( |ipow: { ipow( base = arg1 exp = n ) }| ). 
 
    out->line( ). 
 
    n = 62. 
    arg2 = 2. 
    out->write( |**  : { arg2 ** n }| 
      )->write( |ipow: { ipow( base = arg2 exp = n ) }| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The class demonstrates that the integer power function `ipow` can be used to achieve more precise results than with the [arithmetic operator `**`](abenarith_operators.md). In the cases shown here, the operator `**` produces the [calculation type](../../abap-glossary/abencalculation_type_glosry.md) `f`. If `ipow` is used, the calculation type is determined by the arguments `arg1` and `arg2`.
