---
title: "itab - Grouping with FOR for Aggregates"
source_file: abenfor_group_by_aggregates_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Grouping with FOR"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with FOR for Aggregates

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates aggregates with `FOR` expressions.

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
CLASS cl_demo_for_grps_by_aggregates DEFINITION 
  PUBLIC 
  INHERITING FROM cl_demo_classrun 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS initialize. 
 
  PRIVATE SECTION. 
    TYPES: 
      BEGIN OF line, 
        key TYPE i, 
        num TYPE i, 
      END OF line, 
      itab TYPE STANDARD TABLE OF line WITH EMPTY KEY. 
    DATA 
      numbers TYPE itab. 
    METHODS sort 
      IMPORTING itab        TYPE itab 
      RETURNING VALUE(rtab) TYPE itab. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_for_grps_by_aggregates IMPLEMENTATION. 
  METHOD main. 
    TYPES: 
      BEGIN OF aggregate, 
        sum TYPE i, 
        max TYPE i, 
        min TYPE i, 
        avg TYPE decfloat34, 
      END OF aggregate. 
    TYPES ot TYPE REF TO if_demo_output. 
 
    initialize( ). 
 
    out->next_section( `Table` )->write( numbers ). 
 
    out = REDUCE #( 
      INIT ol TYPE ot 
           aggregate = VALUE aggregate( ) 
           members   = VALUE itab( ) 
      FOR GROUPS <group_key> OF <wa> IN numbers 
            GROUP BY ( key = <wa>-key count = GROUP SIZE ) 
            ASCENDING 
      NEXT aggregate = VALUE #( 
             sum = REDUCE i( INIT sum = 0 
                     FOR m IN GROUP <group_key> 
                     NEXT sum += m-num ) 
             max = REDUCE i( INIT max = 0 
                     FOR m IN GROUP <group_key> 
                     NEXT max = nmax( val1 = max 
                                      val2 = m-num ) ) 
             min = REDUCE i( INIT min = 101 
                     FOR m IN GROUP <group_key> 
                     NEXT min = nmin( val1 = min 
                                val2 = m-num ) ) 
             avg = aggregate-sum / <group_key>-count ) 
           members = sort( 
                       VALUE itab( FOR m IN GROUP <group_key> ( m ) ) ) 
           ol = out->next_section( |Group Key: { <group_key>-key }| 
             )->write( members 
             )->write( aggregate ) ). 
 
 
  ENDMETHOD. 
  METHOD initialize. 
    DATA(keys) = 3. 
    DATA(lines) = 10. 
    cl_demo_input=>new( 
     )->add_field( CHANGING field = keys 
     )->request(   CHANGING field = lines ). 
    IF keys <= 0 OR lines <= 0. 
      RETURN. 
    ENDIF. 
 
    FINAL(rnd_key) = cl_abap_random_int=>create( 
      seed = CONV i( 
          cl_demo_date_time=>get_user_time( ) ) min = 1 max = keys ). 
    FINAL(rnd_num) = cl_abap_random_int=>create( 
      seed = 
          cl_demo_date_time=>get_user_time( ) + 1  min = 1 max = 100 ). 
    numbers = VALUE #( FOR j = 1 UNTIL j > lines 
                        ( key = rnd_key->get_next( ) 
                          num = rnd_num->get_next( ) ) ). 
  ENDMETHOD. 
  METHOD sort. 
    rtab = itab. 
    SORT rtab  BY num DESCENDING. 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example works in the same way as the [executable example](abenloop_group_by_aggregates_abexa.md) for [group loops](../../abap-glossary/abengroup_loop_glosry.md) with [member loops](../../abap-glossary/abenmember_loop_glosry.md) and the [executable example](abenloop_group_by_for_abexa.md) for group loops without member loops. Here, the group loop is also replaced by a [`FOR` expression](abenfor_groups_of.md). The aggregates are calculated in a `VALUE` expression, to avoid having to specify the name of the structure too often. The descending sort of the member table `members` must be passed to a method here, since there is no corresponding additions in table comprehensions.
