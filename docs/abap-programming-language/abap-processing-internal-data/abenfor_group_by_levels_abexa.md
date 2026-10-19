---
title: "itab - Grouping with FOR in Group Levels"
source_file: abenfor_group_by_levels_abexa.html
section: "ABAP Programming Language > ABAP - Processing Internal Data > Internal Tables (itab) > itab - Expressions and Functions > FOR, Table Iterations > itab - Examples of Grouping with FOR"
source: https://help.sap.com/docs/abap-cloud/abap-keywords/abap-keyword-documentation
---
# itab - Grouping with FOR in Group Levels

**Caution**

The programs and program extracts presented in the ABAP Keyword Documentation are only syntax examples and are not intended for direct use in a production system environment. The source texts of the examples are primarily intended to provide a better explanation and visualization of the syntax and semantics of ABAP statements and not to solve concrete programming tasks. For production application programs, a dedicated solution should therefore always be worked out for each individual case. The example can use demo artifacts that are not released as APIs for use in ABAP for Cloud Development.

This example demonstrates simple group level processing using [`GROUP BY`](abenfor_groups_of.md) in a `FOR` expression.

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
CLASS cl_demo_for_grps_by_levels DEFINITION 
  INHERITING FROM cl_demo_classrun 
  PUBLIC 
  CREATE PUBLIC. 
  PUBLIC SECTION. 
    METHODS main REDEFINITION. 
 
  PRIVATE SECTION. 
    TYPES: BEGIN OF line, 
             col1 TYPE c LENGTH 1, 
             col2 TYPE i, 
             col3 TYPE i, 
           END OF line, 
           i_tab TYPE HASHED TABLE OF line 
                 WITH UNIQUE KEY col1 col2. 
    METHODS sum IMPORTING line       TYPE line 
                          base       TYPE line 
                RETURNING VALUE(sum) TYPE line. 
ENDCLASS. 
 
* Public class implementation 
CLASS cl_demo_for_grps_by_levels IMPLEMENTATION. 
  METHOD main. 
    DATA itab TYPE i_tab. 
 
    itab = VALUE #( 
      FOR j = 1 UNTIL j > 3 
       ( col1 = 'A' 
         col2 = j 
         col3 = j ** 2 ) 
       ( col1 = 'B' 
         col2 = 2 * j 
         col3 = ( 2 * j ) ** 2 ) ). 
 
    out->write( itab )->line( ). 
 
    FINAL(total) = REDUCE line( 
      INIT t = VALUE line( ) 
      FOR GROUPS OF <line> IN itab GROUP BY <line>-col1 ASCENDING 
      LET sum = REDUCE line( INIT s = VALUE line( ) 
                             FOR line IN GROUP <line> 
                             NEXT s = sum( EXPORTING line = line 
                                                     base = s ) ) 
          group = VALUE i_tab( FOR <wa> IN GROUP <line> ( <wa> ) ) 
          o1 = out->write( group )->line( )->write( sum )->line( ) IN 
      NEXT t = sum( EXPORTING 
                      line = VALUE line( BASE sum col1 = '*' ) 
                      base = t ) ). 
 
    out->line( )->write( total ). 
  ENDMETHOD. 
  METHOD sum. 
    sum = VALUE #( BASE base 
                   col1 = line-col1 
                   col2 = sum-col2 + line-col2 
                   col3 = sum-col3 + line-col3 ). 
  ENDMETHOD. 
ENDCLASS.
```

## Example Description

This example works in the same way as the corresponding [executable example](abenloop_group_by_levels_abexa.md) for [`LOOP AT ... GROUP BY`](abaploop_at_itab_group_by.md), but uses the expression [`FOR GROUPS ... OF`](abenfor_groups_of.md) for a [table reduction](../../abap-glossary/abentable_reduction_glosry.md) with [`REDUCE`](../abap-program-flow-logic/abenconstructor_expression_reduce.md) instead of the [group loop](../../abap-glossary/abengroup_loop_glosry.md). In both cases, the group key after `GROUP BY` is constructed in exactly the same way.

The result of the table reduction is a structure to which the total of the numeric columns is written. The subtotals and the group members are written to the local helper variables `sum` and `members` using a further table reduction and a [table comprehension](../../abap-glossary/abentable_comprehension_glosry.md). This table reduction table comprehension could also be used in the [executable example](abenloop_group_by_levels_abexa.md) for `LOOP AT ... GROUP BY` instead of the [member loop](../../abap-glossary/abenmember_loop_glosry.md).
