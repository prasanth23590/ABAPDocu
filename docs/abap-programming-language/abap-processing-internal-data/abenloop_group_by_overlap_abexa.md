---
title: "itab - Grouping with LOOP in Overlaps"
source_file: abenloop_group_by_overlap_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY > Examples of Grouping with LOOP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with LOOP in Overlaps

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates the construction of the group key if conditions overlap.

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
CLASS cl_demo_loop_grp_by_overlap DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA 
      itab TYPE TABLE OF i WITH EMPTY KEY. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_grp_by_overlap IMPLEMENTATION. 
  METHOD main. 
    DATA members LIKE itab. 
 
    out->begin_section( `LE 5, BT 2 AND 7, GT 5` ). 
    LOOP AT itab INTO DATA(wa) 
         GROUP BY COND string( WHEN wa <= 5 THEN `LE 5` 
                               WHEN wa >  2 AND 
                                    wa <= 7 THEN `BT 2 AND 7` 
                               WHEN wa >  5 THEN `GT 5` ) 
                 ASSIGNING FIELD-SYMBOL(<group>). 
      out->begin_section( <group> ). 
      CLEAR members. 
      LOOP AT GROUP <group> ASSIGNING FIELD-SYMBOL(<wa>). 
        members = VALUE #( BASE members ( <wa> ) ). 
      ENDLOOP. 
      out->write( members )->end_section( ). 
    ENDLOOP. 
 
    out->next_section( `BT 2 AND 7, LE 5, GT 5` ). 
    LOOP AT itab INTO wa 
         GROUP BY COND string( WHEN wa >  2 AND 
                                    wa <= 7 THEN `BT 2 AND 7` 
                               WHEN wa <= 5 THEN `LE 5` 
                               WHEN wa >  5 THEN `GT 5` ) 
                 ASSIGNING <group>. 
      out->begin_section( <group> ). 
      CLEAR members. 
      LOOP AT GROUP <group> ASSIGNING <wa>. 
        members = VALUE #( BASE members ( <wa> ) ). 
      ENDLOOP. 
      out->write( members )->end_section( ). 
    ENDLOOP. 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    itab = VALUE #( FOR j = 1 UNTIL j > 10 ( j ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example works in a similar way to the [executable example](abenloop_group_by_comparison_abexa.md) for constructions using comparison expressions. The following shows how the result of comparison expressions that overlap depends on the order in which the expressions are evaluated.

In the first group loop,

- those lines are identified first whose value is less than or equal to 5,

- then the lines whose value is between 2 and 7,

- then the lines whose value is greater than 5.

In the second group loop,

- those lines are identified first whose value is between 2 and 7,

- then the lines whose value is less than or equal to 5,

- then the lines whose value is greater than 5.

The result of this is that the lines with the values 3, 4, and 5 are assigned to different groups. The group assignments of the lines would not change, however, even if the internal table were sorted differently.

The executable example for [grouping with `FOR`](abenfor_group_by_overlap_abexa.md) demonstrates how the entire group loop can be implemented using expressions.
