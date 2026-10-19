---
title: "itab - Grouping with LOOP, Nesting"
source_file: abenloop_group_by_lvls_nst_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Processing Statements > LOOP AT itab > LOOP AT itab, GROUP BY > Examples of Grouping with LOOP"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with LOOP, Nesting

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates nested group level processing using [`GROUP BY`](abaploop_at_itab_group_by.md).

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
CLASS cl_demo_loop_grp_by_levels_nst DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_loop_grp_by_levels_nst IMPLEMENTATION. 
  METHOD main. 
    TYPES: BEGIN OF group, 
             fldate   TYPE sflight-fldate, 
             seatsocc TYPE sflight-seatsocc, 
           END OF group. 
 
    DATA: sflight_tab TYPE SORTED TABLE OF sflight 
                      WITH UNIQUE KEY carrid connid fldate, 
          group       TYPE TABLE OF group WITH EMPTY KEY. 
 
 
    DATA(display_members) = abap_false. 
    cl_demo_input=>new( 
     )->request( EXPORTING text  = `Display Group Members?` 
                 CHANGING  field = display_members ). 
 
    SELECT *                                  "#EC CI_ALL_FIELDS_NEEDED 
           FROM sflight 
           INTO TABLE @sflight_tab UP TO 1000 ROWS. 
 
    DATA(total_sum)  = 0. 
    LOOP AT sflight_tab INTO FINAL(carrid_group) 
         GROUP BY carrid_group-carrid. 
      DATA(carrid_sum) = 0. 
      LOOP AT GROUP carrid_group INTO FINAL(connid_group) 
           GROUP BY connid_group-connid. 
        out->next_section( |{ connid_group-carrid } | && 
                           |{ connid_group-connid }| ). 
        CLEAR group. 
        DATA(connid_sum) = 0. 
        LOOP AT GROUP connid_group INTO FINAL(connid_member). 
          group = VALUE #( BASE group 
                         ( CORRESPONDING #( connid_member ) ) ). 
          connid_sum += connid_member-seatsocc. 
        ENDLOOP. 
        carrid_sum += connid_sum. 
        IF to_upper( display_members ) = abap_true. 
          out->write( group ). 
        ENDIF. 
        out->write( |Sum: | && 
                    |{ connid_sum }| ). 
      ENDLOOP. 
      out->line( 
        )->write( |Carrier Sum: | && 
                  |{ carrid_sum }| 
        )->line( ). 
      total_sum += carrid_sum. 
    ENDLOOP. 
    out->write( |Overall Sum: | && 
                |{ total_sum }| ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example works in the same way as the executable example for group level processing with nested groups. The [member loop](../../abap-glossary/abenmember_loop_glosry.md) of the outer [group loop](../../abap-glossary/abengroup_loop_glosry.md) is itself a group loop using the addition `GROUP BY` and contains a further member loop. The group keys of the outer and inner grouping are constructed by specifying the required columns explicitly and, unlike in group level processing, do not depend on the structure of the table and its sorting. The totals of the space used per group are calculated explicitly.

The executable example for [grouping with `FOR`](abenfor_group_by_lvls_nst_abexa.md) demonstrates how the nested group loops can be implemented using expressions.
