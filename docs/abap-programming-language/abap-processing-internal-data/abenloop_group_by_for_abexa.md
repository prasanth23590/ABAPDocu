---
title: "itab - Grouping with LOOP and FOR"
source_file: abenloop_group_by_for_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY > Examples of Grouping with LOOP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with LOOP and FOR

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates aggregates using table reductions.

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
CLASS cl_demo_loop_grp_by_for DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
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
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_grp_by_for IMPLEMENTATION. 
  METHOD main. 
    initialize( ). 
 
    DATA: 
      BEGIN OF aggregate, 
        sum TYPE i, 
        max TYPE i, 
        min TYPE i, 
        avg TYPE decfloat34, 
      END OF aggregate. 
 
    out->next_section( `Table` 
      )->write( numbers ). 
 
    LOOP AT numbers ASSIGNING FIELD-SYMBOL(<wa>) 
         GROUP BY ( key = <wa>-key  count = GROUP SIZE ) 
         ASCENDING 
         ASSIGNING FIELD-SYMBOL(<group_key>). 
 
      out->next_section( |Group Key: { <group_key>-key }| ). 
      DATA(members) = VALUE itab( FOR m IN GROUP <group_key> ( m ) ). 
      aggregate-sum = REDUCE i( INIT sum = 0 
                                FOR m IN GROUP <group_key> 
                                NEXT sum += m-num ). 
      aggregate-max = REDUCE i( INIT max = 0 
                                FOR m IN GROUP <group_key> 
                                NEXT max = nmax( val1 = max 
                                                 val2 = m-num ) ). 
      aggregate-min = REDUCE i( INIT min = 101 
                                FOR m IN GROUP <group_key> 
                                NEXT min = nmin( val1 = min 
                                                 val2 = m-num ) ). 
      aggregate-avg = aggregate-sum / <group_key>-count. 
 
      SORT members BY num DESCENDING.                  "#EC CI_SORTLOOP 
      out->write( members 
        )->write( aggregate ). 
    ENDLOOP. 
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
ENDCLASS.
```

## Example Description

This example works in the same way as the [executable example](abenloop_group_by_aggregates_abexa.md) for aggregates. Here, expressions [`FOR ... IN GROUP`](abenfor_in_group.md) are used instead of the [member loop](../../abap-glossary/abenmember_loop_glosry.md) to calculate aggregates using [table reductions](../../abap-glossary/abentable_reduction_glosry.md) and to determine the group members using a [table comprehension](../../abap-glossary/abentable_comprehension_glosry.md). A further [executable example](abenfor_group_by_aggregates_abexa.md) demonstrates how the entire group loop can be implemented using expressions.
