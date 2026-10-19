---
title: "rel_exp - Comparing Text Strings of Different Length"
source_file: abenstring_comparison_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules > rel_exp - Comparing Elementary Data Types > rel_exp - Comparison Type of Elementary Data Objects > rel_exp - Comparison Type of Character-Like Data Objects"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparing Text Strings of Different Length

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how text strings of different lengths are compared.

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
CLASS cl_demo_str_comparison DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_str_comparison IMPLEMENTATION. 
  METHOD main. 
    DATA length1 TYPE n LENGTH 1 VALUE '4'. 
    DATA length2 TYPE n LENGTH 1 VALUE '6'. 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = length1 
     )->request(   CHANGING field = length2 ). 
 
    FINAL(len1) = CONV i( length1 ). 
    FINAL(len2) = CONV i( length2 ). 
    IF len1 = 0 OR len2 = 0. 
      out->write( 'Try again!' ). 
      RETURN. 
    ENDIF. 
 
    FINAL(text1) = REDUCE string( INIT str = `` 
                                 FOR i = 0 UNTIL i >= len1 
                                 NEXT str &&= `X`  ). 
    FINAL(text2) = REDUCE string( INIT str = `` 
                                 FOR i = 0 UNTIL i >= len2 
                                 NEXT str &&= `X`  ). 
 
    out->write( 
      COND #( WHEN text1 < text2 THEN |{ text1 } < { text2 }| 
              WHEN text1 > text2 THEN |{ text1 } > { text2 }| 
                                 ELSE |{ text1 } = { text2 }| ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Two text strings `text1` and `text2` are filled using their respective input length with the character *X* and then compared. The shorter text string is smaller than the longer one.
