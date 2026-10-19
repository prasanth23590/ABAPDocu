---
title: "FILTER, Filter Table"
source_file: abenfilter_table_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FILTER, Filter Operator > itab - Examples for FILTER"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FILTER, Filter Table

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates [table filtering](abenconstructor_expression_filter.md) using a filter table.

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
CLASS cl_demo_filter_table DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    DATA: 
      cityfrom TYPE spfli-cityfrom VALUE 'Frankfurt', 
      cityto   TYPE spfli-cityto   VALUE 'New York'. 
    METHODS init. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_filter_table IMPLEMENTATION. 
  METHOD main. 
    init( ). 
 
    TYPES: BEGIN OF filter, 
             cityfrom TYPE spfli-cityfrom, 
             cityto   TYPE spfli-cityto, 
           END OF filter, 
           filter_tab TYPE HASHED TABLE OF filter 
                 WITH UNIQUE KEY cityfrom cityto. 
 
    FINAL(filter_tab) = VALUE filter_tab( 
        ( cityfrom = cityfrom cityto = cityto ) 
        ( cityfrom = cityto   cityto = cityfrom ) ). 
 
    SELECT carrid, connid, cityfrom, cityto 
          FROM spfli 
          ORDER BY carrid, connid, cityfrom, cityto 
          INTO TABLE @FINAL(spfli_tab). 
 
    out->write( 
      FILTER #( spfli_tab IN filter_tab 
                  WHERE cityfrom = cityfrom  AND cityto = cityto ) ). 
  ENDMETHOD. 
  METHOD init. 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = cityfrom 
     )->request(   CHANGING field = cityto ). 
    cityfrom = to_upper( cityfrom ). 
    cityto = to_upper( cityto ). 
    IF cityfrom = cityto. 
      EXIT. 
    ENDIF. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

Those lines are filtered out of an internal table `spfli_tab` filled with flight data that have specific values in the columns `cityfrom` and `cityto`. The filter is applied using a filter table of the type `filter_tab` constructed using `VALUE` filled with input values. The result includes all outbound and return flights for the entered cities.
