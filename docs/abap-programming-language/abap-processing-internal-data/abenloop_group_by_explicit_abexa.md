---
title: "itab - Grouping with LOOP, Explicit and Implicit"
source_file: abenloop_group_by_explicit_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY > Examples of Grouping with LOOP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with LOOP, Explicit and Implicit

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates a self-programmed group loop and how it is replaced by [`GROUP BY`](abaploop_at_itab_group_by.md).

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
CLASS cl_demo_loop_at_group_by_expl DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
    METHODS constructor. 
 
  PRIVATE SECTION. 
    DATA: 
      numbers TYPE TABLE OF i WITH EMPTY KEY, 
      limit1  TYPE i VALUE 3, 
      limit2  TYPE i VALUE 6. 
    METHODS: 
      group_explicit, 
      group_by. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_at_group_by_expl IMPLEMENTATION. 
  METHOD main. 
 
    group_explicit( ). 
    group_by( ). 
 
  ENDMETHOD. 
  METHOD group_by. 
    out->next_section( 'Group By' ). 
 
    DATA members LIKE numbers. 
    LOOP AT numbers INTO FINAL(number) 
         GROUP BY COND string( 
           WHEN number <  limit1 THEN `below` 
           WHEN number <= limit2 THEN `between` 
           ELSE `above` ) 
         INTO FINAL(group). 
      out->begin_section( group ). 
      members = VALUE #( FOR m IN GROUP group ( m ) ). 
      out->write( members )->end_section( ). 
    ENDLOOP. 
  ENDMETHOD. 
  METHOD group_explicit. 
    TYPES: 
      BEGIN OF helper_struc, 
        key  TYPE string, 
        refs TYPE STANDARD TABLE OF REF TO i WITH EMPTY KEY, 
      END OF helper_struc, 
      helper_tab TYPE STANDARD TABLE OF helper_struc WITH EMPTY KEY. 
 
    DATA(helper_tab) = VALUE helper_tab( 
     ( key = `below`   ) 
     ( key = `between` ) 
     ( key = `above`   ) ). 
 
    out->next_section( 'Group Explicit' ). 
 
    "Grouping 
    LOOP AT numbers REFERENCE INTO FINAL(dref). 
      IF dref->* < limit1. 
        ASSIGN helper_tab[ key = |below| ]-refs TO FIELD-SYMBOL(<fs>). 
        INSERT dref INTO TABLE <fs>. 
      ELSEIF dref->* <= limit2. 
        ASSIGN helper_tab[ key = |between| ]-refs TO <fs>. 
        INSERT dref INTO TABLE <fs>. 
      ELSE. 
        ASSIGN helper_tab[ key = |above| ]-refs TO <fs>. 
        INSERT dref INTO TABLE <fs>. 
      ENDIF. 
    ENDLOOP. 
 
    "Group loop 
    DATA members LIKE numbers. 
    LOOP AT helper_tab INTO FINAL(helper_struc). 
      out->begin_section( helper_struc-key ). 
      members = VALUE #( FOR m IN helper_struc-refs ( m->* ) ). 
      out->write( members )->end_section( ). 
    ENDLOOP. 
 
  ENDMETHOD. 
  METHOD constructor. 
    super->constructor( ). 
    numbers = VALUE #( FOR j = 1 UNTIL j > 10 ( j ) ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

The task of splitting the lines in a single one-column table into three groups by comparison criteria is solved in two different ways:

- The method `group_explicit` works without `GROUP BY`. Instead, the grouping takes place explicitly in the ABAP class, which requires an explicit helper table `helper_tab`. After the grouping, the lines of the nested table `refs` in `helper_tab` point to the associated lines of the original table `numbers` for each group defined using the column `key`. This grouping loop is followed by the group loop across the helper table, where every loop pass accesses the group members by evaluating the nested tables `refs`.

- The method `group_by` works with `GROUP BY`. The result matches the result of `group_explicit`. A comparison of the methods shows that the grouping loop of the first method in the second method is done implicitly by [`GROUP BY`](abaploop_at_itab_group_by.md) and no explicit helper table is required. Only the group loop can be seen.

Both methods perform three types of loops, the grouping loop, the group loop, and the optional member loops. Using `GROUP BY` is easier since the grouping loop does not need to be programmed explicitly and the second method becomes significantly shorter.
