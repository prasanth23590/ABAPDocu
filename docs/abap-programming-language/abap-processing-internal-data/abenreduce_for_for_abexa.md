---
title: "itab - Multiple FOR Expressions"
source_file: abenreduce_for_for_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Table Reductions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Multiple FOR Expressions

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a [reduction](../abap-program-flow-logic/abenconstructor_expression_reduce.md) of the columns of a nested internal table to a text string.

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
CLASS cl_demo_reduce_for_for DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_reduce_for_for IMPLEMENTATION. 
  METHOD main. 
    TYPES: 
      BEGIN OF line, 
        col1 TYPE i, 
        col2 TYPE i, 
      END OF line, 
      BEGIN OF line1, 
        col1 TYPE i, 
        col2 TYPE STANDARD TABLE OF line WITH EMPTY KEY, 
      END OF line1, 
      itab1 TYPE STANDARD TABLE OF line1 WITH EMPTY KEY, 
      BEGIN OF line2, 
        col1 TYPE i, 
        col2 TYPE i, 
        col3 TYPE i, 
      END OF line2. 
 
    FINAL(itab1) = VALUE itab1( 
      ( col1 = 1 col2 = VALUE line1-col2( ( col1 = 111 col2 = 112 ) 
                                          ( col1 = 121 col2 = 122 ) ) ) 
      ( col1 = 2 col2 = VALUE line1-col2( ( col1 = 211 col2 = 212 ) 
                                          ( col1 = 221 col2 = 222 ) ) ) 
      ( col1 = 3 col2 = VALUE line1-col2( ( col1 = 311 col2 = 312 ) 
                                          ( col1 = 321 col2 = 322 ) ) ) 
                             ). 
    LOOP AT itab1 INTO FINAL(line1). 
      out->write( name = |ITAB1, Line { sy-tabix }, COL2| 
                  data = line1-col2 ). 
    ENDLOOP. 
 
    FINAL(result) = REDUCE string( 
      INIT text TYPE string 
      FOR wa1 IN itab1 
      FOR wa2 IN wa1-col2 
      NEXT text = 
             |{ text } { wa1-col1 }, { wa2-col1 }, { wa2-col2 }\n| ). 
    out->write_html( `<b>Result</b>` 
      )->write(  result  ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The example uses the same nested source table as in the executable example for [table comprehensions](abentable_cmprhnsns_for_for_abexa.md). Its `VALUE` operator is replaced here by the `REDUCE` operator with the data type `string` and the content of the nested loop is chained to the text string after the last [`FOR` expression](abenfor_in_itab.md).
