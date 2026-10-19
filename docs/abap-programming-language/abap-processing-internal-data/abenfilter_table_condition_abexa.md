---
title: "FILTER, Filterings with Table Filter"
source_file: abenfilter_table_condition_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FILTER, Filter Operator > itab - Examples for FILTER"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# FILTER, Filterings with Table Filter

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates various types of [table filtering](abenconstructor_expression_filter.md) using a filter table.

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
CLASS cl_demo_filter_table_condition DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    DATA: 
      itab TYPE SORTED TABLE OF i WITH NON-UNIQUE KEY table_line, 
      ftab TYPE SORTED TABLE OF i WITH NON-UNIQUE KEY table_line. 
    METHODS constructor. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_filter_table_condition IMPLEMENTATION. 
  METHOD main. 
    out->next_section( 'itab' 
       )->write( itab 
       )->next_section( 'ftab' 
       )->write( ftab 
       )->next_section( 
         'FILTER #( itab IN ftab WHERE table_line = table_line )' 
       )->write( 
          FILTER #( itab IN ftab WHERE table_line = table_line ) 
       )->next_section( 
         'FILTER #( itab EXCEPT IN ftab WHERE table_line = table_line )' 
       )->write( 
          FILTER #( itab EXCEPT IN ftab WHERE table_line = table_line ) 
       )->next_section( 
         'FILTER #( itab IN ftab WHERE table_line > table_line )' 
       )->write( 
          FILTER #( itab IN ftab WHERE table_line > table_line ) 
       )->next_section( 
         'FILTER #( itab IN ftab WHERE table_line <> table_line )' 
       )->write( 
          FILTER #( itab IN ftab WHERE table_line <> table_line ) 
       )->next_section( 
         'FILTER #( itab IN ftab WHERE table_line <= table_line )' 
       )->write( 
          FILTER #( itab IN ftab WHERE table_line <= table_line ) ). 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    FINAL(rnd1) = cl_abap_random_int=>create( 
      seed = CONV i( 
         cl_demo_date_time=>get_user_time( ) ) min = 1 max = 7 ). 
    FINAL(rnd2) = cl_abap_random_int=>create( 
     seed = CONV i( 
        cl_demo_date_time=>get_user_time( ) ) min = 3 max = 10 ). 
    itab = VALUE #( FOR j = 1 UNTIL j > 5 ( rnd1->get_next( ) ) ). 
    ftab = VALUE #( FOR j = 1 UNTIL j > 5 ( rnd2->get_next( ) ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

A table `itab` contains five random numbers between 1 and 7, a table `ftab` contains five random numbers between 3 and 10. Different types of table filters for `itab` are performed using the table `ftab` as a filter table:

- The first filtering creates a table of all lines from `itab` for which there is at least one line with the same value in `ftab`.

- The second filtering creates a table of all lines from `itab` for which there is no line with the same value in `ftab`.

- The third filtering creates a table of all lines from `itab` for which there is at least one line with a lesser value in `ftab`.

- The fourth filtering creates a table of all lines from `itab` for which there is at least one line with a non-equal value in `ftab`.

- The fifth filtering creates a table of all lines from `itab` for which there is at least one line with a greater or lesser value in `ftab`.

When merged, the results from the first and second filtering are all lines from `itab`. The first filtering creates the union and the second filtering the difference of the two tables `itab` and `ftab`.

The fourth filtering does not produce the same result as the second filtering. The fifth filtering does not produce the lines from `itab` that remain after the third filtering.
