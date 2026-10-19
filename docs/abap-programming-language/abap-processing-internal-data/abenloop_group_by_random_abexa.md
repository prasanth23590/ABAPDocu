---
title: "itab - Random Grouping with LOOP"
source_file: abenloop_group_by_random_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY > Examples of Grouping with LOOP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Random Grouping with LOOP

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a construction of the group key that does not depend on the table lines.

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
CLASS cl_demo_loop_grp_by_random DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA numbers TYPE STANDARD TABLE OF i WITH EMPTY KEY. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_grp_by_random IMPLEMENTATION. 
  METHOD main. 
 
    FINAL(rnd) = cl_abap_random_int=>create( 
      seed = CONV i( 
        cl_demo_date_time=>get_user_time( ) ) min = 1 max = 10 ). 
 
    DATA members LIKE numbers. 
    LOOP AT numbers INTO FINAL(line) 
         GROUP BY rnd->get_next( ) 
                  ASCENDING 
                  ASSIGNING FIELD-SYMBOL(<group>). 
      out->begin_section( |Group Key: { <group> }| ). 
      members = VALUE #( FOR <wa> IN GROUP <group> ( <wa> ) ). 
      out->write( members 
        )->write( |Lines: { lines( members ) }| 
        )->end_section( ). 
    ENDLOOP. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    numbers = VALUE #( FOR j = 1 UNTIL j > 100 ( j ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

[Grouping](abaploop_at_itab_group_by.md) of an internal table `numbers` with [group key binding](abaploop_at_itab_group_by_binding.md). The [group key](abaploop_at_itab_group_by_key.md) of the [group loop](../../abap-glossary/abengroup_loop_glosry.md) is constructed as a value of the type `i`, which is determined as a random number completely independent of the internal table. This casts the table lines into groups of approximately the same size.

In the group loop, the lines of each group are placed in an internal table `members` using a [table comprehension](../../abap-glossary/abentable_comprehension_glosry.md). This table is then output.
