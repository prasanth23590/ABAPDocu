---
title: "Comparing Internal Tables"
source_file: abencompare_table_abexa.html
section: "ABAP Programming Language > ABAP - Program Flow Logic > Expressions and Functions for Conditions > Logical Expressions (log_exp) > Comparison Expressions (rel_exp) > rel_exp - Comparison Rules > rel_exp - Comparing Internal Tables"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# Comparing Internal Tables

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates how internal tables are compared.

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
CLASS cl_demo_int_tbls_compare DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_int_tbls_compare IMPLEMENTATION. 
  METHOD main. 
 
    TYPES: BEGIN OF line, 
             col1 TYPE i, 
             col2 TYPE i, 
           END OF line. 
 
    DATA: itab TYPE TABLE OF line WITH EMPTY KEY, 
          jtab TYPE TABLE OF line WITH EMPTY KEY. 
 
    itab = VALUE #( FOR j = 1 UNTIL j > 3 
      ( col1 = j col2 = j ** 2 ) ). 
 
    jtab = itab. 
 
    itab = VALUE #( BASE itab 
                    ( col1 = 10 col2 = 20 ) ). 
 
    IF itab > jtab. 
      out->write( 'ITAB >  JTAB' ). 
    ENDIF. 
 
    jtab = VALUE #( BASE jtab 
                    ( col1 = 10 col2 = 20 ) ). 
 
    IF itab = jtab. 
      out->write( 'ITAB =  JTAB' ). 
    ENDIF. 
 
    itab = VALUE #( BASE itab 
                    ( col1 = 30 col2 = 80 ) ). 
 
    IF jtab <= itab. 
      out->write( 'JTAB <= ITAB' ). 
    ENDIF. 
 
    jtab = VALUE #( BASE jtab 
                    ( col1 = 50 col2 = 60 ) ). 
 
    IF itab <> jtab. 
      out->write( 'ITAB <> JTAB' ). 
    ENDIF. 
 
    IF itab < jtab. 
      out->write( 'ITAB <  JTAB' ). 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Two standard tables, `itab` and `jtab`, are created. `itab` is filled with three lines and assigned to `jtab`. An additional line is added to `itab` and the first relational expression returns the result that `itab` is greater than `jtab`. After the same line was added to `itab`, the second relational expression shows that both tables are the same. Another line is appended to `itab` and the third relational expression indicates the result that `jtab` is less than or equal to `itab`. Next, a further line is added to `jtab`, the content of which is different from the final line of `itab`. The next relational expression returns the result that `itab` is not equal to `jtab`. The first table field whose content is different for `itab` and `jtab` is `col1` in the last line of the table, namely 30 for `itab` and 50 for `jtab`. In the last relational expression, `itab` is therefore less than `jtab`.
