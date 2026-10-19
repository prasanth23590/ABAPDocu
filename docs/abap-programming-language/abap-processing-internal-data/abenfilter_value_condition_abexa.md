---
title: "FILTER, Single Values"
source_file: abenfilter_value_condition_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FILTER, Filter Operator > itab - Examples for FILTER"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FILTER, Single Values

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [table filtering](abenconstructor_expression_filter.md) using single values.

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
CLASS cl_demo_filter_value_condition DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_filter_value_condition IMPLEMENTATION. 
  METHOD main. 
    DATA carrid TYPE spfli-carrid VALUE 'LH'. 
    DATA cityfrom TYPE spfli-cityfrom VALUE 'Frankfurt'. 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = carrid 
     )->request( CHANGING field = cityfrom ). 
 
    DATA spfli_tab TYPE STANDARD TABLE OF spfli 
                   WITH EMPTY KEY 
                   WITH NON-UNIQUE SORTED KEY carr_city 
                        COMPONENTS carrid cityfrom. 
 
    SELECT * 
           FROM spfli 
           INTO TABLE @spfli_tab. 
 
    FINAL(extract) = 
      FILTER #( spfli_tab USING KEY carr_city 
                  WHERE carrid   = CONV #( to_upper( carrid ) ) AND 
                        cityfrom = CONV #( to_upper( cityfrom ) ) ). 
 
    out->write( extract ). 
 
    FINAL(rest) = 
      FILTER #( spfli_tab EXCEPT USING KEY carr_city 
                  WHERE carrid   = CONV #( to_upper( carrid ) ) AND 
                        cityfrom = CONV #( to_upper( cityfrom ) ) ). 
 
    ASSERT lines( extract ) + lines( rest ) = lines( spfli_tab ). 
 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Those lines are filtered from an internal table `spfli_tab` filled with flight data that have a specific value in the columns `carrid` and `cityfrom` and the result is assigned to an internal table `extract`. A suitable secondary key `carr_city` is defined for the internal table here.

A further internal table, `rest`, is given the same table filtering, but the addition `EXCEPT` is specified. The assertion `ASSERT` demonstrates that `rest` contains all lines from `spfli_tab` that are not in `extract`.
