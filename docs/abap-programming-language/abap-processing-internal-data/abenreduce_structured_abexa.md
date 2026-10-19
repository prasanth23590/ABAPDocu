---
title: "itab - Table Reductions, Structured Result"
source_file: abenreduce_structured_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Table Reductions"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Table Reductions, Structured Result

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a reduction of the columns of a table to a structure.

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
CLASS cl_demo_reduce_structured DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor . 
 
  PRIVATE SECTION. 
    TYPES: 
      BEGIN OF line, 
        id  TYPE string, 
        num TYPE i, 
      END OF line, 
      BEGIN OF result, 
        text TYPE string, 
        sum  TYPE i, 
        max  TYPE i, 
      END OF result. 
    DATA 
      itab TYPE TABLE OF line WITH EMPTY KEY. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_reduce_structured IMPLEMENTATION. 
  METHOD main. 
    out->write( itab ). 
 
    FINAL(result) = REDUCE result( 
                     INIT res = VALUE result( max  = 0 
                                              text = `Result: ` ) 
                          sep  = `` 
                     FOR <wa> IN itab 
                     NEXT res-text &&= sep && <wa>-id 
                          res-sum += <wa>-num 
                          res-max = nmax( val1 = res-max 
                                          val2 = <wa>-num ) 
                          sep     = `-` ). 
 
    out->write( result ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    FINAL(rnd) = cl_abap_random_int=>create( seed = 
                    CONV i( cl_demo_date_time=>get_user_time( ) ) 
                                            min  = 0 
                                            max  = 1000 ). 
    FINAL(abcde) = 'abcdefghijklmnopqrstuvwxyz'. 
    itab = VALUE #( FOR j = 0 UNTIL j > 9 
                    ( id  = abcde+j(1) 
                      num = rnd->get_next( ) ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Reduces a two-column internal table `itab` using [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md). The content of the first column of all lines is concatenated after the [`FOR` expression](abenfor_in_itab.md), the total of the second column is calculated, and the maximum value of the second column is determined. These values are assigned to the components of the local structure `res`, which is provided as the result.

The separator `sep` in the concatenation is declared as a helper variable after `INIT`. It is initial for the first line read and set to a value here for the evaluation of the following lines.
