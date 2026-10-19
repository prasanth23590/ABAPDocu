---
title: "bit_exp - ( )"
source_file: abenbit_brackets.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Character String and Byte String Processing > Expressions and Functions for Byte Chain Processing > Bit Expressions (bit_exp)"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# bit_exp - ( )

## Syntax

``` abap
... ( bit_exp ) ...  
```

## Description

A complete bit expression `bit_exp` can be placed in parentheses. A bit expression in parentheses can be used as the operand of another bit expression and is not calculated until used in this way.

## Example

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

Parentheses in bit expressions

``` abap
FINAL(out) = cl_demo_output=>new( ). 
 
TYPES output TYPE TABLE OF xstring WITH EMPTY KEY. 
DATA hex1 TYPE xstring VALUE '0011'. 
DATA hex2 TYPE xstring VALUE '0101'. 
DATA hex3 TYPE xstring VALUE '1100'. 
out->write( VALUE output( 
  (   hex1 BIT-AND hex2   BIT-OR hex3  ) 
  ( ( hex1 BIT-AND hex2 ) BIT-OR hex3  ) 
  (   hex1 BIT-AND ( hex2 BIT-OR hex3 ) ) ) ). 
 
out->display( ).
```

The displayed result is:

``` abap
1101 
1101 
0001
```
