---
title: "rel_exp - Comparison with Ranges Table"
source_file: abenlogexp_in_ranges_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Operators > rel_exp - Comparison Operators for All Data Types > rel_exp - Tabular Comparison Operator IN"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# rel_exp - Comparison with Ranges Table

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the evaluation of ranges tables in a comparison expression.

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
CLASS cl_demo_logexp_in DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_logexp_in IMPLEMENTATION. 
  METHOD main. 
 
    DATA letter TYPE c LENGTH 1 VALUE 'F'. 
    cl_demo_input=>new( )->request( CHANGING field = letter ). 
 
    DATA rtab LIKE RANGE OF letter. 
 
    rtab = VALUE #( 
      ( sign = 'I' option = 'EQ' low = 'A' ) 
      ( sign = 'I' option = 'BT' low = 'H' high = 'K' ) 
      ( sign = 'E' option = 'EQ' low = 'M' ) 
      ( sign = 'E' option = 'BT' low = 'X' high = 'Z' ) ). 
 
    out->write( rtab ). 
 
    IF letter IN rtab. 
      out->write( |{ letter } in rtab| ). 
    ELSE. 
      out->write( |{ letter } not in rtab| ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example constructs a [ranges table](../../abap-glossary/abenranges_table_glosry.md) and compares input values with this table using the [`IN`](abenlogexp_select_option.md) operator.
