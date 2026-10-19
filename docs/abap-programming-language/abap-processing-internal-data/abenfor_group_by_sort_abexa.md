---
title: "itab - Grouping with FOR for Sorts"
source_file: abenfor_group_by_sort_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Grouping with FOR"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with FOR for Sorts

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates sorts with `FOR` expressions.

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
CLASS cl_demo_for_grps_by_sort DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_for_grps_by_sort IMPLEMENTATION. 
  METHOD main. 
    TYPES itab TYPE STANDARD TABLE OF string WITH EMPTY KEY. 
 
    FINAL(itab) = 
      VALUE itab( ( `d` ) ( `B` ) ( `D` ) ( `b` ) ( `a` ) 
                  ( `D` ) ( `a` ) ( `C` ) ( `A` ) ( `c` ) ). 
    out->write( itab ). 
 
    DATA jtab TYPE itab. 
    jtab = VALUE #( FOR GROUPS <grp1> OF <line> IN itab 
                        GROUP BY to_upper( <line> ) ASCENDING 
                    FOR GROUPS <grp2> OF <mbr1> IN GROUP <grp1> 
                        GROUP BY <mbr1> DESCENDING 
                    FOR <mbr2> IN GROUP <grp2> ( <mbr2> ) ). 
    out->write( jtab ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example works in the same way as the [executable example](abenloop_group_by_sort_abexa.md) for sorts across groupings using `LOOP`. Here, all groupings are collected in a single expression using three [`FOR` expressions](abenfor_groups_of.md).
