---
title: "arith_exp - ( )"
source_file: abenarith_brackets.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Numeric Calculations > Arithmetic Expressions (arith_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# arith_exp - ( )

## Syntax

``` abap
... ( arith_exp ) ...  
```

## Description

A full arithmetic expression `arith_exp` can be placed in parentheses. An arithmetic expression in parentheses can be used as the operand for another arithmetic expression and is calculated first when used in this way.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

The parentheses in the second calculation correspond to the implicit parentheses in the first calculation. The parentheses in the third calculation change its order. The results are `2`, `2`, and `3`. In the third calculation, the result of the parenthesis is rounded to the value 1.

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
out->write( 
  |  3 *   2   / 3   = {   3 *   2   / 3   }\n| && 
  |( 3 *   2 ) / 3   = { ( 3 *   2 ) / 3   }\n| && 
  |  3 * ( 2   / 3 ) = {   3 * ( 2   / 3 ) }| ). 
 
out->display( ).
```
