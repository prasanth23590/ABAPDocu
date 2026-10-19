---
title: "string_exp - Concatenating Strings"
source_file: abenstring_concatenation_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Character String Processing > String Expressions (string_exp) > string_exp - Performance Note"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# string_exp - Concatenating Strings

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how string concatenations can be optimized.

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
CLASS cl_demo_str_concatenation DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_str_concatenation IMPLEMENTATION. 
  METHOD main. 
    DATA(n) = 10000. 
 
 
    FINAL(t1) = utclong_current( ). 
    FINAL(result1) = 
      REDUCE string( INIT s = `` 
                     FOR i = 1 UNTIL i > n 
                     NEXT s &&= CONV string( i ) ). 
    FINAL(t2) = utclong_current( ). 
    cl_abap_utclong=>diff( EXPORTING high    = t2 
                                     low   = t1 
                           IMPORTING seconds = DATA(t21) ). 
 
    FINAL(t3) = utclong_current( ). 
    FINAL(result2) = 
      REDUCE string( INIT s = `` 
                     FOR i = 1 UNTIL i > n 
                     LET num = CONV string( i ) IN 
                     NEXT s &&= num ). 
    FINAL(t4) = utclong_current( ). 
    cl_abap_utclong=>diff( EXPORTING high    = t4 
                                     low   = t3 
                           IMPORTING seconds = DATA(t43) ). 
    ASSERT result1 = result2. 
    out->write( |Optimization factor: { CONV i( t21 / t43 ) }| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example demonstrates the optimization of a string concatenation, if a string is lengthened on the right side by appending content during an [assignment](abenequals_string_expr.md) to a string. In this case, the strings are processed in a loop using a [`REDUCE` expression](../abap-program-flow-logic/abenconstructor_expression_reduce.md).

- There is no optimization in the first `REDUCE` expression since an expression is appended to the string `s`.

- In the second `REDUCE` expression, the expression is assigned to a helper variable `num` using `LET`. This variable can be appended to `s` directly without an interim result needing to be produced.

Without optimization, the runtime increases quadratically with the number of iterations, which has a noticeable effect for large numbers `n`.
