---
title: "itab - Grouping with FOR, Nesting"
source_file: abenfor_group_by_lvls_nst_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Grouping with FOR"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with FOR, Nesting

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates nested group level processing using [`GROUP BY`](abenfor_groups_of.md) in a `FOR` expression.

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
CLASS cl_demo_for_grps_by_lvls_nest DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_for_grps_by_lvls_nest IMPLEMENTATION. 
  METHOD main. 
    TYPES: BEGIN OF group, 
             fldate   TYPE sflight-fldate, 
             seatsocc TYPE sflight-seatsocc, 
           END OF group, 
           group_tab TYPE STANDARD TABLE OF group WITH EMPTY KEY. 
 
    DATA: sflight_tab TYPE SORTED TABLE OF sflight 
                      WITH UNIQUE KEY carrid connid fldate. 
 
    DATA(display_members) = abap_false. 
    cl_demo_input=>new( 
     )->request( EXPORTING text  = `Display Group Members?` 
                 CHANGING  field = display_members ). 
 
    SELECT * 
           FROM sflight 
           INTO TABLE @sflight_tab UP TO 1000 ROWS. 
 
    FINAL(total_sum) = 
      REDUCE i( 
        LET wg = xsdbool( to_upper( display_members ) = abap_true ) IN 
        INIT t = 0 
             o1 = out 
        FOR GROUPS OF carrid_group IN sflight_tab 
              GROUP BY carrid_group-carrid 
        LET carrid_sum = 
          REDUCE i( 
            INIT s1 = 0 
                 o2 = out 
            FOR GROUPS OF connid_group IN GROUP carrid_group 
                  GROUP BY connid_group-connid 
            LET connid_sum = 
              REDUCE i( 
                INIT s2 = 0 
                FOR m IN GROUP connid_group 
                NEXT s2 += m-seatsocc ) 
                o3 = out->next_section( 
                    |{ connid_group-carrid } { connid_group-connid }| ) 
                o4 = COND #( WHEN wg = abap_true 
                               THEN LET group = VALUE group_tab( 
                                 FOR m IN GROUP connid_group 
                                   ( CORRESPONDING #( m ) ) ) IN 
                                     out->write( group ) ) IN 
            NEXT s1 += connid_sum 
                 o2 = o2->write( |Sum: { connid_sum }| ) ) IN 
        NEXT t += carrid_sum 
             o1 = o1->line( 
                  )->write( |Carrier Sum: { carrid_sum }| 
                  )->line( ) ). 
 
    out->write( |Overall Sum: | && 
                |{ total_sum }| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example works in the same way as the corresponding [executable example](abenloop_group_by_lvls_nst_abexa.md) for [`LOOP AT ... GROUP BY`](abaploop_at_itab_group_by.md), but uses the expression [`FOR GROUPS ... OF`](abenfor_groups_of.md) for [table reductions](../../abap-glossary/abentable_reduction_glosry.md) with [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md) instead of the [group loops](../../abap-glossary/abengroup_loop_glosry.md). In both cases, the group keys after `GROUP BY` are constructed in exactly the same way. Instead of the [member loops](../../abap-glossary/abenmember_loop_glosry.md), further table reductions and a [table comprehension](../../abap-glossary/abentable_comprehension_glosry.md) are used here.
